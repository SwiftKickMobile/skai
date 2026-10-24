// figma-page-check.js — check a page's structure against the Figma designer guide's canvas rules.
//
// Run through the Figma tool (`use_figma`) with this file's text as the code. Set TARGET_ID to a
// page or Section id ("" checks the current page) and SECTION_FILL to the project's section colour
// (the guide's #FAFAFA unless the project addendum overrides it). The result is a report: one
// finding per breach, naming the node, the rule and what was measured. Rules checked:
//
//   loose      a node on a page that is not a Section, or a non-screen node in a Section
//   nesting    a Section inside a Section anywhere but inside a request Section (`CR-<nnn> — …`),
//              or deeper than one level
//   prefix     a name carrying a concept prefix (`a · name`, `A — name`)
//   fill       a Section whose fill is not SECTION_FILL
//   padding    content closer to, or farther from, a Section's edge than PADDING
//   columns    columns not COLUMN_GAP apart, or states not STATE_GAP apart within a column
//   sections   sibling Sections not SECTION_GAP apart, or tops not aligned
//
// The checks are pure over a tree of {type, name, x, y, width, height, fills, children}; the
// test under internal/tests/tools/figma-page-check/ runs them on a mock without Figma.
const TARGET_ID = "";
const SECTION_FILL = "#FAFAFA";
const PADDING = 50, COLUMN_GAP = 50, STATE_GAP = 100, SECTION_GAP = 100, TOLERANCE = 1;
const PREFIX = /^[a-z] · |^[A-Z] — /;
const REQUEST = /^CR-\d+ — /;
const SCREEN_TYPES = new Set(["FRAME", "COMPONENT", "INSTANCE", "COMPONENT_SET"]);

function hex(c) { return "#" + [c.r, c.g, c.b].map(v => Math.round(v * 255).toString(16).padStart(2, "0")).join("").toUpperCase(); }
function near(a, b) { return Math.abs(a - b) <= TOLERANCE; }

function check(root) {
  const findings = [];
  const add = (node, rule, detail) => findings.push({ node: node.name, id: node.id, rule, detail });
  const isPage = root.type === "PAGE";
  const sections = isPage ? root.children.filter(n => n.type === "SECTION") : [root];
  if (isPage) root.children.filter(n => n.type !== "SECTION").forEach(n => add(n, "loose", `${n.type} on the page, not in a Section`));
  for (const s of sections) checkSection(s, 0, add);
  checkSiblings(sections, add);
  return { target: root.name, sections: sections.length, findings };
}

function checkSection(s, depth, add) {
  if (PREFIX.test(s.name)) add(s, "prefix", "concept prefix in the name");
  const fill = s.fills && s.fills.length && s.fills[0].type === "SOLID" ? hex(s.fills[0].color) : "none";
  if (fill !== SECTION_FILL) add(s, "fill", `${fill}, expected ${SECTION_FILL}`);
  const kids = s.children || [];
  const nested = kids.filter(k => k.type === "SECTION");
  const screens = kids.filter(k => SCREEN_TYPES.has(k.type));
  kids.filter(k => k.type !== "SECTION" && !SCREEN_TYPES.has(k.type)).forEach(k => add(k, "loose", `${k.type} in a Section`));
  if (nested.length && !(REQUEST.test(s.name) && depth === 0)) add(s, "nesting", `${nested.length} Section(s) inside a Section that is not a request`);
  if (nested.length && depth > 0) add(s, "nesting", "nested deeper than one level");
  for (const k of [...screens, ...nested]) if (PREFIX.test(k.name)) add(k, "prefix", "concept prefix in the name");
  const content = [...screens, ...nested];
  if (content.length) {
    const minX = Math.min(...content.map(k => k.x)), minY = Math.min(...content.map(k => k.y));
    const maxX = Math.max(...content.map(k => k.x + k.width)), maxY = Math.max(...content.map(k => k.y + k.height));
    if (!near(minX, PADDING) || !near(minY, PADDING)) add(s, "padding", `content starts at (${r(minX)}, ${r(minY)}), expected (${PADDING}, ${PADDING})`);
    if (!near(s.width, maxX + PADDING) || !near(s.height, maxY + PADDING)) add(s, "padding", `size ${r(s.width)}×${r(s.height)}, content needs ${r(maxX + PADDING)}×${r(maxY + PADDING)}`);
  }
  checkColumns(s, screens, add);
  checkSiblings(nested, add);
  for (const n of nested) checkSection(n, depth + 1, add);
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
return check(target);
