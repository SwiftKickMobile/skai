Managed-By: skai
Managed-Id: guide.figma-designer-guide-agent-tooling
Managed-Source: Guides/Design/figma-designer-guide-agent-tooling.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-17

# Figma Designer Guide: Agent Tooling

Print `📖 SKAI guide: figma-designer-guide-agent-tooling` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

For agents editing with the Figma MCP. This extends the
[Figma Designer Guide](figma-designer-guide.md); readers only looking at the file do not need it.
Reusable tools live in SKAI's `Bin/`; project-specific ones stay in the project.

1. **Keep a state file.** Scripts share nothing between calls. After each write, record page,
   Section, component, variable and image IDs in a working-doc JSON file.

2. **Import library components by key each call** (`importComponentByKeyAsync` /
   `importComponentSetByKeyAsync`); node IDs do not persist across calls.

3. **Upload with `upload_assets`.** SVGs become vectors, PNGs image frames. SVG clip paths become
   masks: for a single-color glyph, intersect each mask with what it clips and flatten, keeping the
   original fill rule.

4. **Lay out component sets as grids explicitly.** Appending variants does not place them: set the
   column and row counts, place each with `setGridChildPosition(row, column)`, and size tracks to hug.

5. **Masks drawn by Figma's servers do not clip frames or instances.** A shape can mask plain shapes
   but not a component instance.

6. **Scaling unlinks text styles.** `rescale()` (the Scale tool) detaches scaled text from its
   style; the component keeps the linked style at its base size.

7. **These fail with no error.**
   - Resizing a layer inside an instance is ignored. Use a variant, or top-level instances laid
     over the component.
   - Hidden instance children are skipped unless `figma.skipInvisibleInstanceChildren = false`.
   - A layer cloned into another frame keeps absolute positioning. Reset it.
   - `resize()` on an auto-layout frame turns hugging off on each axis it changes. Restore it.
   - A description reads back escaped. Write it whole.
   - A script that throws is rolled back whole. Throw when a check inside a script fails; check
     for half-built results before retrying a failed run.

## Project Addendum

If `<active-project-root>/skai/addenda/figma-designer-guide-agent-tooling-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
