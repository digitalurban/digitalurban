// Redirect sources that are safe to build: drops the root, self-references, and
// any source that is also a real page or post on the new site (those would
// collide with the real output and stop the build).
const fs = require("fs");
const path = require("path");

const SRC = __dirname + "/..";

function norm(u) {
  u = String(u || "").trim();
  if (!u) return "";
  if (!u.startsWith("/")) u = "/" + u;
  if (!u.endsWith("/")) u += "/";
  return u;
}

function permalinksIn(dir, recurse) {
  const out = new Set();
  let entries = [];
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch (e) {
    return out;
  }
  for (const e of entries) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (recurse && e.name !== "_data" && e.name !== "_includes") {
        for (const u of permalinksIn(p, true)) out.add(u);
      }
      continue;
    }
    if (!/\.(md|njk|html)$/.test(e.name)) continue;
    let text = "";
    try {
      text = fs.readFileSync(p, "utf8");
    } catch (err) {
      continue;
    }
    const m = /^---([\s\S]*?)\n---/.exec(text);
    if (!m) continue;
    const pm = /^permalink:\s*["']?([^"'\n]+)["']?\s*$/m.exec(m[1]);
    if (pm) out.add(norm(pm[1].replace(/index\.html$/, "")));
  }
  return out;
}

module.exports = () => {
  let map = {};
  try {
    map = JSON.parse(fs.readFileSync(SRC + "/_data/redirects.json", "utf8"));
  } catch (e) {
    return [];
  }

  const taken = new Set(["/"]);
  for (const u of permalinksIn(SRC, false)) taken.add(u);
  for (const u of permalinksIn(SRC + "/posts", true)) taken.add(u);

  const list = [];
  const skipped = [];
  for (const [from, to] of Object.entries(map)) {
    const f = norm(from);
    const t = norm(to);
    if (!f || !t || f === t || taken.has(f)) {
      skipped.push(from);
      continue;
    }
    if (list.some((r) => r.from === f)) continue;
    list.push({ from: f, to: t });
  }

  console.log(
    "[redirects] " + list.length + " built, " + skipped.length + " skipped (root, self, or a real page)"
  );
  return list;
};
