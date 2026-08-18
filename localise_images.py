#!/usr/bin/env python3
"""
Bring remotely-hosted post images into assets/uploads and rewrite the Markdown.

From the REPO ROOT (where `assets` and `site` sit):

    python3 localise_images.py                  # find remote images, download, rewrite
    python3 localise_images.py --repair         # re-download ones already rewritten
                                                #   but missing on disk
    python3 localise_images.py --hosts a.com,b.com
    python3 localise_images.py --all-hosts

Some servers refuse requests that do not look like a browser, so this sends a
browser user-agent and a Referer from the image's own host.

--repair reads site/broken-images.txt (written by check_images.py) and reconstructs
the original URL from each local path, so it works even after the posts have been
rewritten.
"""

import argparse, os, re, ssl, sys, time, urllib.parse, urllib.request

POSTS = os.path.join("site", "src", "posts")
ASSETS = "assets"
BROKEN = os.path.join("site", "broken-images.txt")
IMPORTED = "/assets/uploads/imported/"
IMG = re.compile(r'(?:src|href)="(https?://[^"]+\.(?:png|jpe?g|gif|webp|svg))"', re.I)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def ctx():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl._create_unverified_context()


def fetch(url, c):
    host = urllib.parse.urlparse(url).netloc
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "image/avif,image/webp,image/png,image/*,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.9",
        "Referer": f"https://{host}/",
    })
    with urllib.request.urlopen(req, timeout=30, context=c) as r:
        return r.read()


def local_for(url):
    u = urllib.parse.urlparse(url)
    path = urllib.parse.unquote(u.path.lstrip("/"))
    path = re.sub(r"[^A-Za-z0-9._/-]", "_", path)
    return f"imported/{u.netloc}/{path}"


def post_files():
    out = []
    for root, _, names in os.walk(POSTS):
        for n in names:
            if n.endswith(".md"):
                out.append(os.path.join(root, n))
    return out


def repair(c):
    if not os.path.exists(BROKEN):
        sys.exit(f"no {BROKEN} — run check_images.py in the site directory first")
    refs = [l.strip() for l in open(BROKEN) if l.startswith(IMPORTED)]
    print(f"{len(refs)} imported images missing on disk\n")
    ok = fail = 0
    for ref in refs:
        rest = ref[len(IMPORTED):]
        host, _, path = rest.partition("/")
        target = os.path.join(ASSETS, "uploads", "imported", host, path)
        got = None
        for url in (f"https://{host}/{path}", f"http://{host}/{path}"):
            try:
                got = fetch(url, c)
                break
            except Exception as e:
                last = e
        if got:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "wb") as f:
                f.write(got)
            ok += 1
            print(f"  ok   {os.path.basename(path)}")
        else:
            fail += 1
            print(f"  fail {host}/{path} — {last}")
        time.sleep(0.2)
    print(f"\nrecovered {ok}, still missing {fail}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hosts", default="connected-environments.org")
    ap.add_argument("--all-hosts", action="store_true")
    ap.add_argument("--repair", action="store_true")
    ap.add_argument("--prefix", default="/assets/uploads/imported")
    args = ap.parse_args()

    if not os.path.isdir(POSTS):
        sys.exit(f"no {POSTS} — run this from the repo root")

    c = ctx()

    if args.repair:
        repair(c)
        return

    hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]
    files = post_files()

    wanted = {}
    for p in files:
        text = open(p, encoding="utf-8").read()
        for url in IMG.findall(text):
            host = urllib.parse.urlparse(url).netloc
            if not args.all_hosts and not any(host.endswith(h) for h in hosts):
                continue
            wanted[url] = local_for(url)

    print(f"{len(files)} posts scanned, {len(wanted)} remote images to bring local\n")
    if not wanted:
        print("nothing to do — if images are already rewritten but missing,")
        print("run: python3 localise_images.py --repair")
        return

    ok = skip = fail = 0
    swaps = {}
    for url, rel in sorted(wanted.items()):
        target = os.path.join(ASSETS, "uploads", rel)
        if os.path.exists(target):
            skip += 1
            swaps[url] = f"{args.prefix}/{rel}"
            continue
        os.makedirs(os.path.dirname(target), exist_ok=True)
        try:
            data = fetch(url, c)
            with open(target, "wb") as f:
                f.write(data)
            ok += 1
            swaps[url] = f"{args.prefix}/{rel}"
            print(f"  ok   {os.path.basename(url)}")
        except Exception as e:
            fail += 1
            print(f"  fail {url} — {e}")
        time.sleep(0.2)

    print(f"\ndownloaded {ok}, already had {skip}, failed {fail}")

    changed = 0
    for p in files:
        text = open(p, encoding="utf-8").read()
        new = text
        for url, local in swaps.items():
            new = new.replace(url, local)
        if new != text:
            open(p, "w", encoding="utf-8").write(new)
            changed += 1
    print(f"rewrote {changed} posts to use local images")


if __name__ == "__main__":
    main()
