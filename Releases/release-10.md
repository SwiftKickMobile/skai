# Release 10 — 2026-10-07

**UI Map renderer**

- **Interactive HTML render.** `Bin/ui-map-render.py --html <page>` is the primary render: a static page holding the map model that loads the new viewer `Bin/ui-map-viewer.js` / `Bin/ui-map-viewer.css` from the SKAI checkout by a relative path. No server, no Mermaid CLI, no browser automation. The page lays the map out in levels at a fixed width; selecting a scene filters the page to its connections (1 hop, 2 hops, or All), and a side panel shows where the scene is reached from, what it opens, and its notes, implements and modal style; an info button opens a legend. The docstring's "RENDER CONVENTIONS" rule 12 describes it. Mermaid text (`-o`, `--markdown`) and `--svg` are unchanged.
- **The render artifact is `.html`.** `ui-map-guide.md`'s canonical command targets `skai/ui-map/ui-map.html`; the architecture guide, its artifact formats and the implementation guide's promote item name `proposed-ui-map.html` / `ui-map.html` where they named `.svg`. `ui-map-demo.md` keeps its Mermaid render, since a Markdown document cannot embed the page.

**Design**

- **New designer guide.** `Guides/Design/designer-guide.md` sets the conventions for a project's Figma design file: the three main pages (`Production`, `Components`, `Design System`), a `Conventions` frame on `Design System` for per-app values (device frame sizes, dark mode, button label case, UI kit), canvas layout (Sections on every page, with per-page-type rules for screen, component, design-system, and asset pages), frame naming, color variables, custom fonts an agent cannot load (a designer sets the font on the style; agents write text under a library-font style, then switch styles), components (component sets use grid auto layout), and copy. It is read from the SKAI checkout; nothing is installed and no existing artifact changes.

**Upgrade instructions**

1. **No adapter re-run is required.** No installed skill, policy or template changed; the edited and new guides are read from the SKAI checkout. A host upgrading from Release 7 or earlier still follows Release 8's upgrade instructions. Release 9's re-render step is superseded by step 2.
2. **Re-render UI Maps to HTML.**
   - **Discover.** In the map repository (the one project documentation names; it may be a shared root), find the official map `skai/ui-map/ui-map.yaml` and every `skai/changes/*/` package holding a `proposed-ui-map.yaml`. A package whose implementation artifact (`ui-map-implementation.md`) has its terminal promote `T#` checked is historical; every other package is open.
   - **Render.** Run the `ui-map-guide.md` command for the official map, producing `skai/ui-map/ui-map.html`, and for each open package, producing `proposed-ui-map.html` beside its YAML. Leave historical packages unchanged. Each page links the viewer by its path relative to the SKAI checkout, so re-render if SKAI later moves.
   - **Preserve.** Map YAML is untouched. Existing `.svg` renders are derived output; delete them only with supervisor approval.
   - **Verify.** The renderer exits 0 for every map, and each page is nonempty and opens showing the map.
3. **Repoint references.**
   - **Discover.** Search the host and map repositories for `ui-map.svg` and `proposed-ui-map.svg`.
   - **Repoint.** Link the `.html` page wherever current documentation links the SVG render: the README, `skai/integration.md`, and each open package's `ui-map-architecture.md` (its `## Provisional preview`). An `integration.md` override of the render command switches `--svg <file>.svg` to `--html <file>.html`.
   - **Preserve.** Do not edit historical packages, recorded Evidence, or changelog-style history.
   - **Verify.** A repeat search finds only historical hits.
