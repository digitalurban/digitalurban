#!/usr/bin/env python3
"""
Pull remotely-hosted images in posts down into assets/uploads and rewrite the
Markdown to point at the local copy.

Run from the repo root (where `assets` and `site` sit):

    python3 localise_images.py                       # connected-environments.org
    python3 localise_images.py --hosts a.com,b.com   # any hosts you name
    python3 localise_images.py --all-hosts           # every remote image in every post

Images land in assets/uploads/imported/<host>/<original path> and every reference
to them across site/src/posts is rewritten. Safe to re-run: files already present
are skipped, and posts already rewritten have nothing left to match.
"""

import argparse, os, re, ssl, sys, urllib.parse, urllib.request

POSTS = os.path.join("site", "src", "posts")
ASSETS = "assets"
IMG = re.compile(r'(?:src|href)="(https?://[^"]+\.(?:png|jpe?g|gif|webp|svg))"', re.I)


def ctx():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl._create_unverified_context()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hosts", default="connected-environments.org")
    ap.add_argument("--all-hosts", action="store_true")
    ap.add_argument("--prefix", default="/assets/uploads/imported")
    args = ap.parse_args()

    if not os.path.isdir(POSTS):
        sys.exit(f"no {POSTS} — run this from the repo root")

    hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]

    # collect every remote image reference across the posts
    files = []
    for root, _, names in os.walk(POSTS):
        for n in names:
            if n.endswith(".md"):
                files.append(os.path.join(root, n))

    wanted = {}   # url -> local path
    for p in files:
        text = open(p, encoding="utf-8").read()
        for url in IMG.findall(text):
            host = urllib.parse.urlparse(url).netloc
            if not args.all_hosts and not any(host.endswith(h) for h in hosts):
                continue
            path = urllib.parse.unquote(urllib.parse.urlparse(url).path.lstrip("/"))
            path = re.sub(r"[^A-Za-z0-9._/-]", "_", path)
            wanted[url] = f"imported/{host}/{path}"

    print(f"{len(files)} posts scanned, {len(wanted)} remote images to bring local\n")
    if not wanted:
        return

    c = ctx()
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
            req = urllib.request.Request(url, headers={"User-Agent": "digitalurban-migration"})
            with urllib.request.urlopen(req, timeout=30, context=c) as r:
                data = r.read()
            with open(target, "wb") as f:
                f.write(data)
            ok += 1
            swaps[url] = f"{args.prefix}/{rel}"
            print(f"  ok   {os.path.basename(url)}")
        except Exception as e:
            fail += 1
            print(f"  fail {url} — {e}")

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
