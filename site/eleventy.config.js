const { DateTime } = require("luxon");
const rss = require("@11ty/eleventy-plugin-rss");

module.exports = function (cfg) {
  cfg.addPlugin(rss);

  cfg.addPassthroughCopy({ "../assets": "assets" });
  cfg.addPassthroughCopy("src/css");
  cfg.addPassthroughCopy("src/admin");

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

  cfg.addCollection("tagList", (api) => {
    const tags = {};
    api.getFilteredByGlob("src/posts/**/*.md").forEach((p) => {
      (p.data.tags || []).forEach((t) => { tags[t] = (tags[t] || 0) + 1; });
    });
    return Object.entries(tags).sort((a, b) => b[1] - a[1]);
  });

  cfg.addFilter("date", (d, fmt = "dd.MM.yyyy") =>
    DateTime.fromJSDate(d, { zone: "utc" }).toFormat(fmt)
  );
  cfg.addFilter("iso", (d) => DateTime.fromJSDate(d, { zone: "utc" }).toISO());
  cfg.addFilter("year", () => String(new Date().getFullYear()));

  cfg.addFilter("slugify", (s) =>
    String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "")
  );

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
