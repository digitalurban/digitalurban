#!/usr/bin/env python3
"""
Find broken local image references in the built site.

Run from the `site` directory AFTER a build:

    python3 check_images.py

Scans every HTML file in _site for src= / srcset= / href= references that point at
/assets/, checks whether the file exists on disk, and groups what's missing so the
cause is obvious (a whole missing folder, a naming mismatch, a dead external host).

Writes broken-images.txt with the full list and which pages reference each one.
"""

import os, re, sys, urllib.parse
from collections import defaultdict

SITE = "_site"
REF = re.compile(r'(?:src|href)="(/assets/[^"]+)"')
SRCSET = re.compile(r'srcset="([^"]+)"')


def main():
    if not os.path.isdir(SITE):
        sys.exit("no _site directory — run `npm run build` first")

    refs = defaultdict(set)   # url -> set of pages referencing it

    for root, _, names in os.walk(SITE):
        for n in names:
            if not n.endswith(".html"):
                continue
            page = os.path.join(root, n)
            try:
                html = open(page, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            found = set(REF.findall(html))
            for ss in SRCSET.findall(html):
                for part in ss.split(","):
                    u = part.strip().split(" ")[0]
                    if u.startswith("/assets/"):
                        found.add(u)
            rel = os.path.relpath(page, SITE)
            for u in found:
                refs[u].add(rel)

    missing = {}
    for url, pages in refs.items():
        path = urllib.parse.unquote(url.split("?")[0].split("#")[0]).lstrip("/")
        if not os.path.exists(os.path.join(SITE, path)):
            missing[url] = pages

    print(f"{len(refs)} local asset references, {len(missing)} broken\n")

    if not missing:
        print("nothing broken")
        return

    # group by the folder two levels down, which is where the pattern shows up
    groups = defaultdict(int)
    for url in missing:
        parts = url.split("/")
        groups["/".join(parts[:4])] += 1
    print("--- broken by folder ---")
    for g, n in sorted(groups.items(), key=lambda x: -x[1])[:25]:
        print(f"{n:>6}  {g}/")

    exts = defaultdict(int)
    for url in missing:
        exts[os.path.splitext(url)[1].lower()] += 1
    print("\n--- broken by extension ---")
    for e, n in sorted(exts.items(), key=lambda x: -x[1]):
        print(f"{n:>6}  {e or '(none)'}")

    print("\n--- first 15 ---")
    for url in sorted(missing)[:15]:
        print(f"  {url}")
        print(f"      on {sorted(missing[url])[0]}")

    with open("broken-images.txt", "w") as f:
        for url in sorted(missing):
            f.write(url + "\n")
            for p in sorted(missing[url]):
                f.write("\t" + p + "\n")
    print(f"\nfull list in broken-images.txt")


if __name__ == "__main__":
    main()
