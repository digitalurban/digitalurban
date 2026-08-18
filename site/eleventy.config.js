const { DateTime } = require("luxon");
const rss = require("@11ty/eleventy-plugin-rss");

module.exports = function (cfg) {
  cfg.addPlugin(rss);

  cfg.addPassthroughCopy({ "../assets": "assets" });
  cfg.addPassthroughCopy({ "src/css": "css" });
  cfg.addPassthroughCopy({ "src/icons": "." });
  cfg.addPassthroughCopy({ "src/admin": "admin" });

  cfg.addCollection("posts", (api) =>
    api.getFilteredByGlob("src/posts/**/*.md").sort((a, b) => b.date - a.date)
  );

  cfg.addCollection("years", (api) => {
    const years = {};
    api.getFilteredByGlob("src/posts/**/*.md").forEach((p) => {
      const y = DateTime.fromJSDate(p.date, { zone: "utc" }).year;
      years[y] = (years[y] || 0) + 1;
    });
    return Object.entries(years).sort((a, b) => b[0] - a[0]);
  });

  // Tags are merged by slug, so "AI" and "ai" become one page. Each entry is
  // [label, count, slug, [every spelling seen]].
  cfg.addCollection("tagList", (api) => {
    const slug = (s) =>
      String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    const byslug = {};
    api.getFilteredByGlob("src/posts/**/*.md").forEach((p) => {
      (p.data.tags || []).forEach((t) => {
        const k = slug(t);
        if (!k) return;
        if (!byslug[k]) byslug[k] = { label: t, count: 0, names: new Set() };
        byslug[k].count += 1;
        byslug[k].names.add(t);
        // prefer the spelling with a capital letter as the display label
        if (/[A-Z]/.test(t) && !/[A-Z]/.test(byslug[k].label)) byslug[k].label = t;
      });
    });
    return Object.entries(byslug)
      .map(([k, v]) => [v.label, v.count, k, [...v.names]])
      .sort((a, b) => b[1] - a[1]);
  });

  cfg.addFilter("date", (d, fmt = "dd.MM.yyyy") =>
    DateTime.fromJSDate(d, { zone: "utc" }).toFormat(fmt)
  );
  cfg.addFilter("iso", (d) => DateTime.fromJSDate(d, { zone: "utc" }).toISO());
  cfg.addFilter("year", () => String(new Date().getFullYear()));

  // posts carrying any of these tag spellings
  cfg.addFilter("tagged", (posts, names) => {
    if (!Array.isArray(posts) || !Array.isArray(names)) return [];
    const want = new Set(names);
    return posts.filter((p) => (p.data.tags || []).some((t) => want.has(t)));
  });

  cfg.addFilter("head", (arr, n) => (Array.isArray(arr) ? arr.slice(0, n) : []));
  // everything after the lead item, capped at n
  cfg.addFilter("tail", (arr, n) =>
    Array.isArray(arr) ? arr.slice(Math.max(1, arr.length - n)) : []
  );

  cfg.addFilter("slugify", (s) =>
    String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")
  );

  // find the newest post whose title contains a term (used by the Projects page)
  cfg.addFilter("findPost", (posts, needle) => {
    if (!Array.isArray(posts) || !needle) return null;
    const n = String(needle).toLowerCase();
    return posts.find((p) => String(p.data.title || "").toLowerCase().includes(n)) || null;
  });

  cfg.addFilter("firstImage", (content) => {
    const m = /<img[^>]+src="([^"]+)"/.exec(content || "");
    return m ? m[1] : "";
  });

  cfg.addFilter("strip", (content, n = 180) => {
    const t = String(content || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    return t.length > n ? t.slice(0, n).replace(/\s+\S*$/, "") + "\u2026" : t;
  });

  cfg.addFilter("readingTime", (content) => {
    const words = String(content || "").replace(/<[^>]+>/g, " ").split(/\s+/).length;
    return Math.max(1, Math.round(words / 220));
  });

  return {
    dir: { input: "src", output: "_site", includes: "_includes", data: "_data" },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
