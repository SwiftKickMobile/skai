// figma-page-check.js — check a page's structure against the Figma designer guide's canvas rules.
// It is for `Production` and its form factor pages, change pages, `Components` and `Design System`.
// An asset page is not a target: its frames are laid out for export, and the script would read
// them as screens.
//
// Run through the Figma tool (`use_figma`) with this file's text as the code. Set TARGET_ID to a
// page or Section id ("" checks the current page) and SECTION_FILL to the project's section colour
// (the guide's #FAFAFA unless the project addendum overrides it). The result is a report with two
// lists. `findings` holds breaches, each to fix: one per breach, naming the node, the rule and what
// was measured. `signals` holds things to look at and judge, each of which may be fine as it is.
//
// Breaches, canvas layout:
//
//   loose      a node on a page that is not a Section, or a non-screen node in a Section
//   nesting    a Section inside a Section on a `Production` page, or deeper than one level; on a change
//              page a top-level Section (the package's, a request's `CR-01 — …`, a backup) may hold one level
//   backup     a backup Section (`Base — Pre CR-01`) not stacked 100 under a Section with its left edge aligned
//              (checked on a page; a Section target cannot see its neighbours)
//   prefix     a name carrying a concept prefix (`a · name`, `A — name`)
//   fill       a Section whose fill is not SECTION_FILL
//   padding    content closer to, or farther from, a Section's edge than PADDING
//   columns    columns not COLUMN_GAP apart, or states not STATE_GAP apart within a column
//              (not checked on the `Design System` page or in a `Design System` Section)
//   sections   sibling Sections not SECTION_GAP apart, or tops not aligned (backups aside)
//
// Breaches, what screens and components are made of (a backup Section or backup page aside):
//   color      a visible solid fill or stroke, or a gradient stop, with no color variable (image paints pass)
//   text-style a text layer, or a range of one, with no text style
//   dimension  a padding or gap on an auto-layout frame, or a corner radius, above zero with no variable
//              (which collection the variable comes from is not checked)
//   type-size  a local text style whose font size binds no variable (checked when the target is a page;
//              a `Backup/…` style, and a `Draft/…` style outside this page's own folder, are skipped)
//   purpose    a screen frame on a change page with no annotation in the `Purpose` category
//              (none is asked on `Production` and its form factor pages, on `Components` or
//              `Design System`, or in a `Components` or `Design System` Section; nor of an instance
//              placed as a screen: one that repeats a screen at a further form factor needs none,
//              and whether any other does is for you to look at)
//
// Signals:
//   loose-layers       text and frame layers in a screen that are in no instance, counted per screen
//                      (a component or a specimen is built from layers and gets no such signal)
//   repeated-override  one fill, stroke or corner-radius override, the same value, on the same layer
//                      of REPEAT or more instances of one component, at any depth (the layer is the
//                      instance itself or a layer inside it, matched by name)
//   kit-lookalike      a frame named like a library component the target uses at any depth, that is
//                      not an instance
//
// A page is `Production`, a form factor page (`Production (<form factor name>)`), `Components` or
// `Design System` only by its exact name; one of those names followed by ` — Pre <change-id>` is
// that page's backup; any other page is a change page. A Section target is read on its own: the
// script does not look at what the Section sits inside.
//
// A text layer whose ranges differ in style or fill is read range by range.
//
// In an instance, on the instance itself and on every layer inside it, only what the instance
// overrides is checked: the rest belongs to its component, which is checked where it lives, or to
// a kit. A scratch Section (`Scratch — …`)
// is skipped: exploration is outside the check.
// The checks are pure over a tree of {type, name, x, y, width, height, fills, children, …}; the
// test under internal/tests/tools/figma-page-check/ runs them on a mock without Figma.
const TARGET_ID = "";
const SECTION_FILL = "#FAFAFA";
const PADDING = 50, COLUMN_GAP = 50, STATE_GAP = 100, SECTION_GAP = 100, TOLERANCE = 1;
const REPEAT = 3;  // instances of one component sharing an override before it is a signal
const PURPOSE = "Purpose", UNNOTED = /^(Components|Design System)$/, DOCS = /^Design System$/;
const PAGE_BACKUP = /^(Production(?: \(.+\))?|Components|Design System) — Pre .+$/;  // a backup of the page it is named for
const SPACING = ["paddingLeft", "paddingRight", "paddingTop", "paddingBottom", "itemSpacing", "counterAxisSpacing"];
const RADII = ["topLeftRadius", "topRightRadius", "bottomLeftRadius", "bottomRightRadius"];
const LOOK = ["fills", "strokes", "cornerRadius", ...RADII];
const PREFIX = /^[a-z] · |^[A-Z] — /;
const BACKUP = /^Base — Pre /, SCRATCH = /^Scratch — /;
const KEPT = /^Backup\//;  // a backup copy of a style is a record of what was, and is not checked
const PRODUCTION = /^Production( \(.+\))?$/;  // `Production` and its form factor pages hold no nested Sections
const SCREEN_TYPES = new Set(["FRAME", "COMPONENT", "INSTANCE", "COMPONENT_SET"]);

function hex(c) { return "#" + [c.r, c.g, c.b].map(v => Math.round(v * 255).toString(16).padStart(2, "0")).join("").toUpperCase(); }
function near(a, b) { return Math.abs(a - b) <= TOLERANCE; }

function check(root, pageName, ctx = {}) {
  const findings = [], signals = [];
  const add = (node, rule, detail) => findings.push({ node: node.name, id: node.id, rule, detail });
  const signal = (node, rule, detail) => signals.push({ node: node.name, id: node.id, rule, detail });
  const isPage = root.type === "PAGE";
  const name = isPage ? root.name : pageName || "", kind = (name.match(PAGE_BACKUP) || [0, name])[1];  // a backup page is laid out as its page
  const production = PRODUCTION.test(kind);
  const sections = (isPage ? root.children.filter(n => n.type === "SECTION") : [root]).filter(s => !SCRATCH.test(s.name));
  if (isPage) root.children.filter(n => n.type !== "SECTION").forEach(n => add(n, "loose", `${n.type} on the page, not in a Section`));
  for (const s of sections) checkSection(s, 0, add, production, DOCS.test(kind));
  checkSiblings(sections.filter(s => !BACKUP.test(s.name)), add);
  if (isPage) for (const b of sections.filter(s => BACKUP.test(s.name))) checkBackup(b, sections, add);  // placement needs the page
  if (kind === name) checkContent(sections.filter(s => !BACKUP.test(s.name)), production || UNNOTED.test(kind), UNNOTED.test(kind), ctx, add, signal);
  const others = t => /^Draft\//.test(t.name) && !t.name.startsWith("Draft/" + name + "/");  // another package's drafts
  if (isPage && kind === name) for (const t of ctx.textStyles || []) if (!KEPT.test(t.name) && !others(t) && !(t.boundVariables && t.boundVariables.fontSize)) add(t, "type-size", "font size binds no variable");
  return { target: root.name, sections: sections.length, findings, signals };
}

// Every frame, component or instance placed in a Section under the given Sections, with whether
// it needs a purpose note and whether it is a screen (what a `Components` or `Design System`
// Section or page holds is not).
function screensOf(sections, unnoted, library, noted = true, plain = true, out = []) {
  for (const s of sections) {
    const named = UNNOTED.test(s.name), note = noted && !unnoted && !named, isScreen = plain && !library && !named;
    for (const k of s.children || []) {
      if (k.type === "SECTION") { if (!SCRATCH.test(k.name) && !BACKUP.test(k.name)) screensOf([k], unnoted, library, note, isScreen, out); }
      else if (SCREEN_TYPES.has(k.type)) out.push({ node: k, note, isScreen });
    }
  }
  return out;
}

// A layer and what is under it. `fields` is null for a layer in no instance (all of it is the
// screen's own); in an instance, and for the instance itself, it lists what the outermost
// instance overrides on the layer. `owner` is the nearest instance the layer is in, or itself.
function layers(node, out = [], over = null, owner = null) {
  if (node.type === "INSTANCE") { owner = node; if (!over) over = new Map((node.overrides || []).map(o => [o.id, o.overriddenFields])); }
  out.push({ n: node, fields: over ? over.get(node.id) || [] : null, owner });
  for (const k of node.children || []) layers(k, out, over, owner);
  return out;
}

function unbound(paints) {
  const raw = x => !(x.boundVariables && x.boundVariables.color);
  return Array.isArray(paints) && paints.some(p => p.visible !== false && (p.type === "SOLID" ? raw(p) : /^GRADIENT/.test(p.type || "") && (p.gradientStops || []).some(raw)));
}

// The values a field takes on a layer: one value, or one per range where a text layer's ranges
// differ (Figma then gives the layer no single value).
function values(n, field, single) {
  if (single(n[field])) return [n[field]];
  return typeof n.getStyledTextSegments === "function" ? n.getStyledTextSegments([field]).map(s => s[field]) : [];
}

function checkContent(sections, unnoted, library, ctx, add, signal) {
  const mains = ctx.mains || new Map(), shared = new Map(), kit = new Set(), frames = [];
  for (const { node: screen, note, isScreen } of screensOf(sections, unnoted, library)) {
    if (note && screen.type !== "INSTANCE" && !(screen.annotations || []).some(a => a.categoryId === ctx.purposeId && ctx.purposeId)) add(screen, "purpose", `no annotation in the ${PURPOSE} category`);
    let loose = 0;
    for (const { n, fields, owner } of layers(screen)) {
      const bound = n.boundVariables || {};
      const mine = k => !fields || fields.includes(k);
      if (mine("fills") && values(n, "fills", Array.isArray).some(unbound)) add(n, "color", "a fill with no color variable");
      if (mine("strokes") && unbound(n.strokes)) add(n, "color", "a stroke with no color variable");
      if (n.type === "TEXT" && mine("textStyleId") && values(n, "textStyleId", v => typeof v === "string").some(id => !id)) add(n, "text-style", "text with no text style");
      if (n.layoutMode && n.layoutMode !== "NONE") for (const k of SPACING) if (mine(k) && n[k] > 0 && !bound[k]) add(n, "dimension", `${k} ${n[k]} with no variable`);
      const corners = RADII.some(k => typeof n[k] === "number") ? RADII : ["cornerRadius"];
      for (const k of corners) if (mine(k) && n[k] > 0 && !bound[k]) { add(n, "dimension", `${k} ${n[k]} with no variable`); break; }
      if (!fields && n !== screen && (n.type === "TEXT" || n.type === "FRAME")) loose++;
      if (!fields && n.type === "FRAME") frames.push(n);
      if (n.type === "INSTANCE" && mains.get(n.id) && mains.get(n.id).remote) kit.add(mains.get(n.id).name);  // at any depth: a kit is used inside its wrapper
      const main = owner && mains.get(owner.id);
      // Figma lists a uniform radius override as `cornerRadius` and all four corners: count it once
      if (main) for (const f of fields.filter(f => LOOK.includes(f) && !(RADII.includes(f) && fields.includes("cornerRadius")))) {
        const layer = n === owner ? "" : n.name;  // one component, one layer, one field, one value
        const value = f === "fills" ? values(n, f, Array.isArray) : n[f];  // a text layer's fills, range by range
        const key = [main.id, layer, f, JSON.stringify(value) || "mixed"].join(" ");
        (shared.get(key) || shared.set(key, { main, f, layer, first: owner, owners: new Set() }).get(key)).owners.add(owner.id);
      }
    }
    if (loose && isScreen && screen.type !== "INSTANCE") signal(screen, "loose-layers", `${loose} text and frame layers in no instance`);
  }
  for (const { main, f, layer, first, owners } of shared.values()) if (owners.size >= REPEAT) signal(first, "repeated-override", `${owners.size} instances of "${main.name}" carry the same ${f} override${layer ? ` on "${layer}"` : ""}`);
  for (const f of frames) if (kit.has(f.name)) signal(f, "kit-lookalike", "named like a library component, but not an instance");
}

function checkBackup(b, sections, add) {
  const above = sections.find(s => s !== b && near(s.x, b.x) && near(b.y, s.y + s.height + SECTION_GAP));
  if (!above) add(b, "backup", `not stacked ${SECTION_GAP} under a Section with its left edge aligned`);
}

function checkSection(s, depth, add, production, docs) {
  if (PREFIX.test(s.name)) add(s, "prefix", "concept prefix in the name");
  const fill = s.fills && s.fills.length && s.fills[0].type === "SOLID" ? hex(s.fills[0].color) : "none";
  if (fill !== SECTION_FILL) add(s, "fill", `${fill}, expected ${SECTION_FILL}`);
  const kids = s.children || [];
  const nested = kids.filter(k => k.type === "SECTION");
  const screens = kids.filter(k => SCREEN_TYPES.has(k.type));
  kids.filter(k => k.type !== "SECTION" && !SCREEN_TYPES.has(k.type)).forEach(k => add(k, "loose", `${k.type} in a Section`));
  if (nested.length && production) add(s, "nesting", `${nested.length} Section(s) inside a Section on a Production page`);
  if (nested.length && depth > 0) add(s, "nesting", "nested deeper than one level");
  for (const k of [...screens, ...nested]) if (PREFIX.test(k.name)) add(k, "prefix", "concept prefix in the name");
  const content = [...screens, ...nested];
  if (content.length) {
    const minX = Math.min(...content.map(k => k.x)), minY = Math.min(...content.map(k => k.y));
    const maxX = Math.max(...content.map(k => k.x + k.width)), maxY = Math.max(...content.map(k => k.y + k.height));
    if (!near(minX, PADDING) || !near(minY, PADDING)) add(s, "padding", `content starts at (${r(minX)}, ${r(minY)}), expected (${PADDING}, ${PADDING})`);
    if (!near(s.width, maxX + PADDING) || !near(s.height, maxY + PADDING)) add(s, "padding", `size ${r(s.width)}×${r(s.height)}, content needs ${r(maxX + PADDING)}×${r(maxY + PADDING)}`);
  }
  if (!docs && !DOCS.test(s.name)) checkColumns(s, screens, add);  // swatches and specimens are not laid out as screens
  checkSiblings(nested, add);
  for (const n of nested) checkSection(n, depth + 1, add, production, docs);
}

function checkColumns(s, screens, add) {
  const cols = new Map();
  for (const f of screens) { const key = Math.round(f.x); (cols.get(key) || cols.set(key, []).get(key)).push(f); }
  const xs = [...cols.keys()].sort((a, b) => a - b);
  for (let i = 1; i < xs.length; i++) {
    const prev = cols.get(xs[i - 1]), width = Math.max(...prev.map(f => f.width));
    const gap = xs[i] - (xs[i - 1] + width);
    if (!near(gap, COLUMN_GAP)) add(s, "columns", `columns at x ${xs[i - 1]} and ${xs[i]} are ${r(gap)} apart, expected ${COLUMN_GAP}`);
  }
  for (const [x, frames] of cols) {
    const sorted = frames.slice().sort((a, b) => a.y - b.y);
    for (let i = 1; i < sorted.length; i++) {
      const gap = sorted[i].y - (sorted[i - 1].y + sorted[i - 1].height);
      if (!near(gap, STATE_GAP)) add(sorted[i], "columns", `${r(gap)} below "${sorted[i - 1].name}", expected ${STATE_GAP}`);
    }
  }
}

function checkSiblings(sections, add) {
  const sorted = sections.slice().sort((a, b) => a.x - b.x);
  for (let i = 1; i < sorted.length; i++) {
    const gap = sorted[i].x - (sorted[i - 1].x + sorted[i - 1].width);
    if (!near(gap, SECTION_GAP)) add(sorted[i], "sections", `${r(gap)} right of "${sorted[i - 1].name}", expected ${SECTION_GAP}`);
    if (!near(sorted[i].y, sorted[i - 1].y)) add(sorted[i], "sections", `top at ${r(sorted[i].y)}, "${sorted[i - 1].name}" at ${r(sorted[i - 1].y)}`);
  }
}

function r(n) { return Math.round(n); }

const target = TARGET_ID ? await figma.getNodeByIdAsync(TARGET_ID) : figma.currentPage;
if (!target) throw new Error("no node with id " + TARGET_ID);
if (target.type === "PAGE") await figma.setCurrentPageAsync(target);
let page = target; while (page && page.type !== "PAGE") page = page.parent;
// What the pure checks cannot read from the tree: the Purpose category, each instance's main
// component (its parent set's name when it is a variant), and the file's text styles.
const ctx = { mains: new Map(), textStyles: [], purposeId: null };
const categories = figma.annotations ? await figma.annotations.getAnnotationCategoriesAsync() : [];
ctx.purposeId = (categories.find(c => c.label === PURPOSE) || {}).id || null;
if (figma.getLocalTextStylesAsync) ctx.textStyles = await figma.getLocalTextStylesAsync();
for (const { n } of layers(target)) if (n.type === "INSTANCE") {
  const m = n.getMainComponentAsync ? await n.getMainComponentAsync() : n.mainComponent;  // the plain property throws in Figma
  if (m) ctx.mains.set(n.id, { id: m.parent && m.parent.type === "COMPONENT_SET" ? m.parent.id : m.id, name: m.parent && m.parent.type === "COMPONENT_SET" ? m.parent.name : m.name, remote: !!m.remote });
}
return check(target, page ? page.name : "", ctx);
