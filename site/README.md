# digitalurban.org

Static site built with Eleventy, deployed to GitHub Pages from `main`.

## Layout

    site/
      eleventy.config.js     build config, collections, filters
      package.json
      CNAME                  www.digitalurban.org
      src/
        _data/site.json      title, author, giscus ids, social links
        _data/repos.json     the Projects page content
        _includes/           base, post and page layouts
        css/site.css         the whole design, one file
        posts/YYYY/MM/*.md   2,642 posts from the WordPress export
        pages/*.md           About and other WordPress pages
        index.njk            home, paginated 13 per page
        archive.njk          search, year index, tag index
        tag.njk / year.njk   a page per tag and per year
        projects.njk         builds, from _data/repos.json
        books.njk
        feed.njk sitemap.njk search.njk
        admin/               Decap CMS
    assets/uploads/          images recovered from WordPress and Blogger
    .github/workflows/       build and deploy

## Run locally

    cd site
    npm install
    npm run dev        # http://localhost:8080

First build of 2,642 posts takes a minute or two.

## Before it goes live

1. **Move `.github/` and `CNAME` to the repo root** — they must sit at the top level,
   not inside `site/`. Everything else stays where it is. `assets/` also belongs at
   the root, alongside `site/`.
2. **Settings → Pages → Source: GitHub Actions**, then set the custom domain to
   `www.digitalurban.org`.
3. **DNS at your registrar:** a CNAME record for `www` pointing at
   `digitalurban.github.io`. For the bare domain, four A records to
   185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153.
4. **giscus:** enable Discussions on the repo, install the giscus app, then paste the
   repo id and category id into `src/_data/site.json`.
5. **Decap** needs an OAuth backend for GitHub logins — Netlify Identity or a small
   Cloudflare Worker. Until that exists, edit posts directly on GitHub.
6. **Delete the WordPress XML** from the repo. It contains commenter emails and IPs.

## Notes

* Every post keeps its original WordPress URL, so inbound links and search rankings
  survive the move. `src/_data/redirects.json` lists them all.
* Post bodies are HTML inside Markdown files — nothing was lossily converted.
* 22 images could not be recovered; they are listed in `missing-images.txt`.
