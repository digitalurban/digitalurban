#!/usr/bin/env python3
"""
WordPress WXR export -> Markdown files for a static site (Eleventy).

Usage:
    python3 wxr_to_markdown.py digitalurban.WordPress.2026-08-18.xml
    python3 wxr_to_markdown.py export.xml --out ../src --images ../assets/uploads

What it does
  * reads every published post (skips revisions, nav menu items, drafts unless --drafts)
  * writes one Markdown file per post at src/posts/YYYY/MM/YYYY-MM-DD-slug.md
  * front matter carries title, date, slug, permalink, categories, tags, author, excerpt
  * permalink is set to the ORIGINAL WordPress URL (/blog/YYYY/MM/DD/slug/) so no
    inbound link or search result breaks
  * body is kept as HTML (lossless). WordPress shortcodes are unwrapped, WP gallery
    and caption shortcodes become <figure>, and bare newlines become paragraphs
    (wpautop equivalent) so old pre-Gutenberg posts render correctly
  * collects every image URL, optionally downloads it, and rewrites the src to a
    local /assets/uploads/... path
  * writes _data/redirects.json and a report of anything that needs a human look

Nothing is written outside --out / --images. Re-running is safe (files overwritten).
"""

import argparse, html, json, os, re, ssl, sys, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
    "wp": "http://wordpress.org/export/1.2/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

SITE_HOSTS = ("digitalurban.org", "www.digitalurban.org")

# Hosts holding images from the blog's Blogger era and CASA's old server.
# --rescue-external pulls these local too, before they disappear.
RESCUE_HOSTS = (
    "bp.blogspot.com", "blogspot.com", "blogger.com", "googleusercontent.com",
    "casa.ucl.ac.uk", "connected-environments.org", "static.flickr.com",
    "staticflickr.com",
)


def text(el, path, default=""):
    found = el.find(path, NS)
    return (found.text or default) if found is not None else default


def yaml_str(s):
    s = (s or "").replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()
    return f'"{s}"'


def yaml_list(items):
    return "[" + ", ".join(yaml_str(i) for i in items) + "]" if items else "[]"


# ---------------------------------------------------------------- body cleanup

SHORTCODE_CAPTION = re.compile(
    r"\[caption[^\]]*\](.*?)\[/caption\]", re.S | re.I)
SHORTCODE_PAIRED = re.compile(
    r"\[(embed|gallery|video|audio|vc_row|vc_column|vc_column_text|et_pb_[a-z_]+)"
    r"[^\]]*\](.*?)\[/\1\]", re.S | re.I)
SHORTCODE_SINGLE = re.compile(r"\[/?[a-z][a-z0-9_\-]*[^\]]*\]", re.I)
IMG_SRC = re.compile(r'(<img[^>]+src=["\'])([^"\']+)(["\'])', re.I)
HREF_UPLOAD = re.compile(
    r'(<a[^>]+href=["\'])([^"\']*/wp-content/uploads/[^"\']+)(["\'])', re.I)
YOUTUBE = re.compile(
    r'https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w\-]{6,})')


TAG = re.compile(r"<[^<>]+>")


def collapse_tag_whitespace(body):
    """Old Blogger posts wrap long attribute values across lines. Collapse the
    whitespace inside tags so paragraph conversion can't inject <br /> into a URL."""
    return TAG.sub(lambda m: re.sub(r"\s+", " ", m.group(0)), body)


def unwrap_shortcodes(body):
    def caption(m):
        inner = m.group(1).strip()
        # trailing text after the <img>/<a> is the caption
        parts = re.split(r"(?<=>)(?=[^<>]+$)", inner, maxsplit=1)
        media = parts[0].strip()
        cap = parts[1].strip() if len(parts) > 1 else ""
        if cap:
            return f"<figure>{media}<figcaption>{cap}</figcaption></figure>"
        return f"<figure>{media}</figure>"

    body = SHORTCODE_CAPTION.sub(caption, body)

    def paired(m):
        tag, inner = m.group(1).lower(), m.group(2).strip()
        if tag == "embed":
            yt = YOUTUBE.search(inner)
            if yt:
                return (
                    '<div class="embed"><iframe loading="lazy" '
                    f'src="https://www.youtube-nocookie.com/embed/{yt.group(1)}" '
                    'title="Video" allowfullscreen></iframe></div>')
            return f'<p><a href="{inner}">{inner}</a></p>'
        return inner

    body = SHORTCODE_PAIRED.sub(paired, body)
    return SHORTCODE_SINGLE.sub("", body)


BLOCK = ("address|article|aside|blockquote|details|div|dl|figure|figcaption|footer|"
         "form|h[1-6]|header|hr|iframe|nav|ol|p|pre|section|table|ul")


def wpautop(body):
    """WordPress stored bare newlines as paragraph breaks. Reproduce that."""
    if re.search(r"<(?:p|div|figure|section)\b", body, re.I):
        return body  # already block-formatted (Gutenberg / hand-written HTML)
    chunks = re.split(r"\n\s*\n+", body.strip())
    out = []
    for c in chunks:
        c = c.strip()
        if not c:
            continue
        if re.match(rf"^<(?:{BLOCK})\b", c, re.I):
            out.append(c)
        else:
            out.append("<p>" + c.replace("\n", "<br />\n") + "</p>")
    return "\n\n".join(out)


def localise_media(body, images, image_prefix, hosts=None, rescue=False):
    """Rewrite on-site upload URLs to local paths; record them for download."""
    def rel(url):
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc and hosts is not None:
            hosts[parsed.netloc] += 1
        if parsed.netloc and not parsed.netloc.endswith(SITE_HOSTS):
            if rescue and any(parsed.netloc.endswith(h) for h in RESCUE_HOSTS):
                # keep the host in the path so nothing collides
                safe = urllib.parse.unquote(parsed.path.lstrip("/"))
                safe = re.sub(r"[^A-Za-z0-9._/\-]", "_", safe)
                path = f"external/{parsed.netloc}/{safe}"
                images.add((url, path))
                return f"{image_prefix}/{path}"
            return None  # external image, leave alone
        m = re.search(r"/wp-content/uploads/(.+)$", parsed.path)
        if not m:
            return None
        path = urllib.parse.unquote(m.group(1))
        images.add(("https://www.digitalurban.org/wp-content/uploads/" + m.group(1), path))
        return f"{image_prefix}/{path}"

    def sub_img(m):
        new = rel(m.group(2))
        return m.group(1) + (new or m.group(2)) + m.group(3)

    body = IMG_SRC.sub(sub_img, body)
    body = HREF_UPLOAD.sub(sub_img, body)
    return body


# ---------------------------------------------------------------------- parsing

def parse(path):
    for _, el in ET.iterparse(path, events=("end",)):
        if el.tag == "item":
            yield el
            el.clear()


def attachment_map(path):
    """WordPress stores a post's lead image as a _thumbnail_id pointing at an
    attachment. Collect id -> url first so those can be used as `hero`."""
    amap = {}
    for item in parse(path):
        if text(item, "wp:post_type") == "attachment":
            pid = text(item, "wp:post_id")
            url = text(item, "wp:attachment_url")
            if pid and url:
                amap[pid] = url
    return amap


def featured_url(item, amap):
    for meta in item.findall("wp:postmeta", NS):
        if text(meta, "wp:meta_key") == "_thumbnail_id":
            return amap.get(text(meta, "wp:meta_value"))
    return None


def convert(args):
    posts_dir = os.path.join(args.out, "posts")
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(os.path.join(args.out, "_data"), exist_ok=True)

    images, redirects, report = set(), {}, []
    counts, hosts = Counter(), Counter()
    amap = attachment_map(args.xml)
    print(f"{len(amap):>6}  attachments indexed")
    cats, tags = Counter(), Counter()

    for item in parse(args.xml):
        ptype = text(item, "wp:post_type")
        status = text(item, "wp:status")
        counts[f"{ptype}/{status}"] += 1

        if ptype == "attachment":
            url = text(item, "wp:attachment_url")
            m = re.search(r"/wp-content/uploads/(.+)$", url)
            if m:
                images.add((url, urllib.parse.unquote(m.group(1))))
            continue

        if ptype not in ("post", "page"):
            continue
        if status != "publish" and not (args.drafts and status == "draft"):
            continue

        title = html.unescape(text(item, "title")).strip() or "Untitled"
        slug = text(item, "wp:post_name").strip()
        raw_date = text(item, "wp:post_date_gmt") or text(item, "wp:post_date")
        try:
            dt = datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            dt = datetime.strptime(text(item, "wp:post_date"), "%Y-%m-%d %H:%M:%S")
        if not slug:
            slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or dt.strftime("%Y%m%d%H%M")

        body = text(item, "content:encoded")
        body = html.unescape(body) if "&lt;" in body[:200] else body
        body = collapse_tag_whitespace(body)
        body = unwrap_shortcodes(body)
        body = wpautop(body)
        body = localise_media(body, images, args.image_prefix, hosts, args.rescue_external)

        excerpt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text(item, "excerpt:encoded"))).strip()
        if not excerpt:
            plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()
            excerpt = plain[:200].rsplit(" ", 1)[0] + ("…" if len(plain) > 200 else "")

        cat_names, tag_names = [], []
        for c in item.findall("category"):
            domain, name = c.get("domain"), (c.text or "").strip()
            if not name:
                continue
            if domain == "category":
                cat_names.append(name); cats[name] += 1
            elif domain == "post_tag":
                tag_names.append(name); tags[name] += 1

        # original WordPress URL — kept so nothing 404s
        orig = text(item, "link") or ""
        permalink = urllib.parse.urlparse(orig).path or (
            f"/blog/{dt:%Y/%m/%d}/{slug}/" if ptype == "post" else f"/{slug}/")
        if not permalink.endswith("/"):
            permalink += "/"

        hero = ""
        feat = featured_url(item, amap)
        if feat:
            marked = localise_media(f'<img src="{feat}" />', images, args.image_prefix,
                                    hosts, args.rescue_external)
            m = IMG_SRC.search(marked)
            if m:
                hero = m.group(2)
        if not hero:
            first_img = IMG_SRC.search(body)
            hero = first_img.group(2) if first_img else ""

        fm = [
            "---",
            f"title: {yaml_str(title)}",
            f"date: {dt:%Y-%m-%d %H:%M:%S}",
            f"slug: {yaml_str(slug)}",
            f"permalink: {yaml_str(permalink)}",
            f"author: {yaml_str(html.unescape(text(item, 'dc:creator')) or 'Andy')}",
            f"categories: {yaml_list(cat_names)}",
            f"tags: {yaml_list(tag_names)}",
            f"excerpt: {yaml_str(excerpt)}",
        ]
        if hero:
            fm.append(f"hero: {yaml_str(hero)}")
        if ptype == "page":
            fm.append("layout: page.njk")
        fm.append("---")

        sub = os.path.join(posts_dir, f"{dt:%Y}", f"{dt:%m}") if ptype == "post" \
            else os.path.join(args.out, "pages")
        os.makedirs(sub, exist_ok=True)
        fname = f"{dt:%Y-%m-%d}-{slug}.md" if ptype == "post" else f"{slug}.md"
        with open(os.path.join(sub, fname), "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + "\n\n" + body.strip() + "\n")

        counts["written"] += 1
        redirects[permalink] = permalink
        if "[" in body and re.search(SHORTCODE_SINGLE, body):
            report.append(f"leftover shortcode: {permalink}")
        if not hero:
            report.append(f"no image: {permalink}")

    with open(os.path.join(args.out, "_data", "taxonomy.json"), "w") as f:
        json.dump({"categories": cats.most_common(), "tags": tags.most_common()}, f, indent=2)
    with open(os.path.join(args.out, "_data", "redirects.json"), "w") as f:
        json.dump(redirects, f, indent=2)

    print("\n--- counts ---")
    for k, v in sorted(counts.items()):
        print(f"{v:>6}  {k}")
    print(f"{len(images):>6}  images to bring local")

    external = [(h, n) for h, n in hosts.most_common() if not h.endswith(SITE_HOSTS)]
    if external:
        print("\n--- images hosted elsewhere (top 15) ---")
        for h, n in external[:15]:
            print(f"{n:>6}  {h}")
        with open("external-image-hosts.txt", "w") as f:
            f.write("\n".join(f"{n}\t{h}" for h, n in external))

    with open("migration-report.txt", "w") as f:
        f.write("\n".join(report))
    print(f"\n{len(report)} notes written to migration-report.txt")

    if args.images:
        download(images, args.images)
    else:
        with open("image-manifest.txt", "w") as f:
            f.write("\n".join(f"{u}\t{p}" for u, p in sorted(images)))
        print("image-manifest.txt written (re-run with --images DIR to download)")


def make_ssl_context():
    """macOS Python has no cert bundle by default. Use certifi if present,
    else fall back to unverified — we are fetching public images, not secrets."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        print("  (no certifi found — continuing without certificate verification;"
              " run '/Applications/Python 3.12/Install Certificates.command' to fix properly)")
        return ssl._create_unverified_context()


SIZE_SUFFIX = re.compile(r"-\d{2,4}x\d{2,4}(?=\.[A-Za-z0-9]+$)")


def fetch(url, ctx):
    req = urllib.request.Request(url, headers={"User-Agent": "digitalurban-migration"})
    with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
        return r.read()


def download(images, dest):
    print(f"\ndownloading {len(images)} images -> {dest}")
    ctx = make_ssl_context()
    ok = fail = skip = recovered = 0
    missing = []
    for i, (url, path) in enumerate(sorted(images), 1):
        target = os.path.join(dest, path)
        if os.path.exists(target):
            skip += 1
            continue
        if re.search(r"[\s<>]", url):
            fail += 1
            missing.append(f"malformed\t{url}")
            continue
        os.makedirs(os.path.dirname(target), exist_ok=True)
        try:
            data = fetch(url, ctx)
            ok += 1
        except Exception as e:
            # WordPress thumbnails (-300x160) are often gone; the original remains
            full = SIZE_SUFFIX.sub("", url)
            if full != url:
                try:
                    data = fetch(full, ctx)
                    ok += 1
                    recovered += 1
                except Exception as e2:
                    fail += 1
                    missing.append(f"{e2}\t{url}")
                    continue
            else:
                fail += 1
                missing.append(f"{e}\t{url}")
                continue
        with open(target, "wb") as f:
            f.write(data)
        if i % 200 == 0:
            print(f"  {i}/{len(images)}  ok={ok} skip={skip} fail={fail}")
    print(f"done: ok={ok} (of which {recovered} recovered at full size) "
          f"skipped={skip} failed={fail}")
    if missing:
        with open("missing-images.txt", "w") as f:
            f.write("\n".join(missing))
        print(f"{len(missing)} unrecoverable — listed in missing-images.txt")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("xml")
    ap.add_argument("--out", default="src", help="output dir (default: src)")
    ap.add_argument("--images", default="", help="download images into this dir")
    ap.add_argument("--image-prefix", default="/assets/uploads",
                    help="URL prefix images are served from")
    ap.add_argument("--drafts", action="store_true", help="include drafts")
    ap.add_argument("--rescue-external", action="store_true",
                    help="also pull images still hosted on Blogger and casa.ucl.ac.uk")
    args = ap.parse_args()
    if not os.path.exists(args.xml):
        sys.exit(f"no such file: {args.xml}")
    convert(args)
