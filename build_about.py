#!/usr/bin/env python3
"""
Turn the WordPress About page into structured data for a purpose-built template.

Run from the REPO ROOT:

    python3 build_about.py

Reads  site/src/pages/about.md
Writes site/src/_data/about.json   (bio paragraphs + publications, year-grouped)
Moves  site/src/pages/about.md  ->  wp-pages-archive/  (so /about/ is free for
       the new template)

Publications are split on paragraph boundaries after the "Selected Publications"
heading; the year comes from the first (yyyy) in each citation and the DOI or URL
from its first link.
"""

import json, os, re, shutil, sys

SRC = os.path.join("site", "src", "pages", "about.md")
OUT = os.path.join("site", "src", "_data", "about.json")
ARCHIVE = "wp-pages-archive"

JUNK = re.compile(r"blank line of text in white|^\s*&nbsp;\s*$|^\s*$", re.I)
YEAR = re.compile(r"\((\d{4})[a-z]?(?:,[^)]*)?\)")
LINK = re.compile(r'href="([^"]+)"')
TAGS = re.compile(r"<[^>]+>")


def blocks(html):
    """Split the body into paragraph-level chunks."""
    parts = re.split(r"</p>|\n{2,}", html)
    out = []
    for p in parts:
        t = p.replace("<p>", "").strip()
        if not t or JUNK.match(TAGS.sub("", t).strip()):
            continue
        out.append(t)
    return out


def main():
    if not os.path.exists(SRC):
        sys.exit(f"no {SRC} — has the About page already been converted?")

    raw = open(SRC, encoding="utf-8").read()
    body = raw.split("---", 2)[-1] if raw.startswith("---") else raw

    chunks = blocks(body)

    split_at = None
    for i, c in enumerate(chunks):
        if "selected publication" in TAGS.sub("", c).lower():
            split_at = i
            break

    bio = chunks[:split_at] if split_at is not None else chunks
    refs = chunks[split_at + 1:] if split_at is not None else []

    bio = [b for b in bio if len(TAGS.sub("", b).strip()) > 40]

    pubs = []
    for r in refs:
        plain = TAGS.sub("", r).strip()
        if len(plain) < 30:
            continue
        m = YEAR.search(plain)
        year = m.group(1) if m else ""
        link = LINK.search(r)
        pubs.append({"year": year, "html": r.strip(), "url": link.group(1) if link else ""})

    years = {}
    for p in pubs:
        years.setdefault(p["year"] or "undated", []).append(p)
    grouped = [{"year": y, "items": v} for y, v in
               sorted(years.items(), key=lambda kv: kv[0], reverse=True)]

    data = {"bio": bio, "publications": pubs, "byYear": grouped, "count": len(pubs)}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    os.makedirs(ARCHIVE, exist_ok=True)
    shutil.move(SRC, os.path.join(ARCHIVE, "about.md"))

    print(f"{len(bio)} bio paragraphs, {len(pubs)} publications across "
          f"{len(grouped)} years -> {OUT}")
    print(f"moved the WordPress page to {ARCHIVE}/about.md")


if __name__ == "__main__":
    main()
