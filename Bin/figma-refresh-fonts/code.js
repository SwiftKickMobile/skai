// SKAI Refresh Fonts — a local Figma plugin, run from the desktop app.
//
// Text that an agent creates or edits through Figma's servers is laid out there, and the servers
// only have Figma's own fonts. Text in a font installed only on the designer's machine is stored with
// a fallback layout and keeps showing it until Figma lays it out again locally. This plugin does that
// for the whole file: for each text node it can edit, it switches the text style off and back on
// (or re-applies the font for unstyled text), which makes the desktop app lay the text out with the
// real font.
//
// Scope: text in main components and plain frames, plus instance text the instance has overridden.
// Instance text that follows its main component is left alone; it redraws from the refreshed main.

main().then(
  (msg) => figma.closePlugin(msg),
  (e) => figma.closePlugin("Refresh Fonts failed: " + (e && e.message ? e.message : e)),
);

async function main() {
  await figma.loadAllPagesAsync();
  const texts = figma.root.findAllWithCriteria({ types: ["TEXT"] });
  let refreshed = 0, skipped = 0, failed = 0;
  for (const t of texts) {
    if (!(await editable(t))) { skipped++; continue; }
    try {
      await loadFonts(t);
      const styleId = t.textStyleId;
      if (typeof styleId === "string" && styleId) {
        await t.setTextStyleIdAsync("");
        await t.setTextStyleIdAsync(styleId);
      } else if (t.fontName !== figma.mixed) {
        t.fontName = t.fontName;
      } else {
        t.characters = t.characters;
      }
      refreshed++;
    } catch (e) {
      failed++;
    }
  }
  return `Refreshed ${refreshed} text layers` + (failed ? `, ${failed} failed (missing fonts?)` : "") + ".";
}

// A text node is refreshed unless it is inside an instance and the instance has not overridden it.
async function editable(t) {
  let n = t.parent, inst = null;
  while (n && n.type !== "PAGE") { if (n.type === "INSTANCE") inst = n; n = n.parent; }
  if (!inst) return true;
  const ov = inst.overrides || [];
  return ov.some((o) => o.id === t.id);
}

async function loadFonts(t) {
  if (t.fontName !== figma.mixed) { await figma.loadFontAsync(t.fontName); return; }
  const segs = t.getStyledTextSegments(["fontName"]);
  for (const s of segs) await figma.loadFontAsync(s.fontName);
}
