#!/usr/bin/env python3
"""
Repair the handful of image references that never came local.

Run from the `site` directory, after check_images.py has written broken-images.txt:

    python3 fix_broken_images.py            # retry the downloads
    python3 fix_broken_images.py --rewrite  # ...and point any still-dead ones back
                                            #    at their original absolute URL

A path like
    /assets/uploads/external/connected-environments.org/wp-content/uploads/x.jpg
maps back to
    https://connected-environments.org/wp-content/uploads/x.jpg
so each one can be retried directly. Failures are tried over https then http, and
without any -WIDTHxHEIGHT thumbnail suffix, same as the main migration script.

--rewrite edits the Markdown in src/posts: the local path becomes the absolute URL.
The image then loads from the original host for as long as that host lives, instead
of showing as broken.
"""

import argparse, os, re, ssl, sys, urllib.parse, urllib.request

ASSETS = os.path.join("..", "assets")
PREFIX = "/assets/uploads/external/"
SIZE_SUFFIX = re.compile(r"-\d{2,4}x\d{2,4}(?=\.[A-Za-z0-9]+$)")


def ctx():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl._create_unverified_context()


def get(url, c):
    req = urllib.request.Request(url, headers={"User-Agent": "digitalurban-migration"})
    with urllib.request.urlopen(req, timeout=30, context=c) as r:
        return r.read()


def candidates(ref):
    """Every URL worth trying for one broken local reference."""
    rest = ref[len(PREFIX):]
    host, _, path = rest.partition("/")
    for scheme in ("https", "http"):
        base = f"{scheme}://{host}/{path}"
        yield base
        full = SIZE_SUFFIX.sub("", base)
        if full != base:
            yield full
        # www variants
        if host.startswith("www."):
            yield f"{scheme}://{host[4:]}/{path}"
        else:
            yield f"{scheme}://www.{host}/{path}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rewrite", action="store_true",
                    help="point still-dead images back at their original URL")
    ap.add_argument("--list", default="broken-images.txt")
    args = ap.parse_args()

    if not os.path.exists(args.list):
        sys.exit(f"no {args.list} — run check_images.py first")

    refs = [l.strip() for l in open(args.list) if l.startswith("/assets/")]
    print(f"{len(refs)} broken references to repair\n")

    c = ctx()
    fixed, dead = 0, []

    for ref in refs:
        if not ref.startswith(PREFIX):
            dead.append(ref)
            continue
        target = os.path.join(ASSETS, urllib.parse.unquote(ref[len("/assets/"):]))
        got = None
        for url in candidates(ref):
            try:
                got = get(url, c)
                break
            except Exception:
                continue
        if got:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "wb") as f:
                f.write(got)
            fixed += 1
            print(f"  ok   {os.path.basename(ref)}")
        else:
            dead.append(ref)
            print(f"  dead {os.path.basename(ref)}")

    print(f"\nrecovered {fixed}, still dead {len(dead)}")

    if not dead or not args.rewrite:
        if dead:
            print("re-run with --rewrite to point those at their original URLs")
        return

    # rewrite the markdown so dead local paths become absolute original URLs
    swaps = {}
    for ref in dead:
        rest = ref[len(PREFIX):]
        host, _, path = rest.partition("/")
        swaps[ref] = f"https://{host}/{path}"

    changed = 0
    for root, _, names in os.walk(os.path.join("src", "posts")):
        for n in names:
            if not n.endswith(".md"):
                continue
            p = os.path.join(root, n)
            text = open(p, encoding="utf-8").read()
            new = text
            for old, live in swaps.items():
                if old in new:
                    new = new.replace(old, live)
            if new != text:
                open(p, "w", encoding="utf-8").write(new)
                changed += 1

    print(f"rewrote {changed} post files to use the original URLs")


if __name__ == "__main__":
    main()
