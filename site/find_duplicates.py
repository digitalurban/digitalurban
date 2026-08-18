#!/usr/bin/env python3
"""Find (and optionally remove) duplicate posts in site/src/posts.

Posts are grouped by normalised title + publication date. The keeper is chosen
in this order:

  1. not empty (a 0-word file never wins over one with text)
  2. a real slug beats a lost one - "posts-71.md" came out of the export with no
     slug, so its permalink is junk and any properly-named twin wins
  3. most body text
  4. shortest slug, so "my-post" beats "my-post-2"

Groups where every copy is empty are listed as EMPTY and left alone.

Run from the site directory:

    python3 find_duplicates.py                 # report only, writes duplicates.txt
    python3 find_duplicates.py --delete        # delete the extras
    python3 find_duplicates.py --delete --redirects   # ...and record their old
                                               #    permalinks in _data/redirects.json
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict

POSTS = "src/posts"
REDIRECTS = "src/_data/redirects.json"


def front_matter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    head, body = text[3:end], text[end + 4 :]
    data = {}
    for line in head.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            data[m.group(1)] = m.group(2).strip().strip("\"'")
    return data, body


def rank(i):
    return (i["words"] == 0, i["lost_slug"], -i["words"], len(i["slug"]))


def norm_title(t):
    t = re.sub(r"&[a-z]+;|&#\d+;", " ", t.lower())
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delete", action="store_true")
    ap.add_argument("--redirects", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(POSTS):
        sys.exit("run this from the site directory (no %s here)" % POSTS)

    groups = defaultdict(list)
    total = 0
    for root, _dirs, files in os.walk(POSTS):
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            fm, body = front_matter(text)
            title = fm.get("title", "")
            if not title:
                continue
            total += 1
            date = fm.get("date", "")[:10] or name[:10]
            groups[(norm_title(title), date)].append(
                {
                    "path": path,
                    "title": title,
                    "permalink": fm.get("permalink", ""),
                    "words": len(body.split()),
                    "slug": name,
                    "lost_slug": bool(re.search(r"posts-\d+\.md$", name)),
                }
            )

    dupes = {k: v for k, v in groups.items() if len(v) > 1}
    extra = sum(len(v) - 1 for v in dupes.values())

    lines = []
    empty = 0
    for (title, date), items in sorted(dupes.items(), key=lambda kv: kv[0][1]):
        items.sort(key=rank)
        keep, drop = items[0], items[1:]
        if keep["words"] == 0:
            empty += 1
            lines.append("%s  %s" % (date, items[0]["title"]))
            for i in items:
                lines.append("  EMPTY %s  %s" % (i["path"], i["permalink"]))
            lines.append("")
            continue
        lines.append("%s  %s" % (date, items[0]["title"]))
        lines.append("  KEEP %s  (%d words)" % (keep["path"], keep["words"]))
        for d in drop:
            lines.append("  DROP %s  (%d words)  %s" % (d["path"], d["words"], d["permalink"]))
        lines.append("")

    report = "\n".join(lines)
    with open("duplicates.txt", "w", encoding="utf-8") as fh:
        fh.write(report)

    print("%d posts scanned" % total)
    print("%d titles duplicated, %d extra files" % (len(dupes), extra))
    if empty:
        print("%d groups have no text in any copy - marked EMPTY, not touched" % empty)
    print("written to duplicates.txt")

    if not args.delete:
        print("\nread duplicates.txt, then re-run with --delete when it looks right")
        return

    redirects = {}
    if args.redirects and os.path.exists(REDIRECTS):
        with open(REDIRECTS, encoding="utf-8") as fh:
            try:
                redirects = json.load(fh)
            except ValueError:
                redirects = {}

    removed = 0
    for items in dupes.values():
        items.sort(key=rank)
        keep, drop = items[0], items[1:]
        if keep["words"] == 0:
            continue
        for d in drop:
            if args.redirects and d["permalink"] and keep["permalink"]:
                redirects[d["permalink"]] = keep["permalink"]
            os.remove(d["path"])
            removed += 1

    print("deleted %d files" % removed)

    if args.redirects:
        os.makedirs(os.path.dirname(REDIRECTS), exist_ok=True)
        with open(REDIRECTS, "w", encoding="utf-8") as fh:
            json.dump(redirects, fh, indent=2, sort_keys=True)
        print("%d redirects recorded in %s" % (len(redirects), REDIRECTS))


if __name__ == "__main__":
    main()
