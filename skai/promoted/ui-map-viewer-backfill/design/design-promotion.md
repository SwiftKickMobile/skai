# Design Promotion — UI Map Viewer Backfill

## Inputs

- Package: [design-authoring.md](design-authoring.md), with 37 entries under `## Design Changes`.
- Base: production, the empty `Production` and `Components` pages.
- Design file: [SKAI](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=0-1), change page `ui-map-viewer-backfill`.

## Promotion Checks

- [x] C1 Drafts meet the conventions
- [x] C2 Inventory matches the drawings
- [x] C3 The base absorbs the package
- [x] C4 Links point at the base
- [x] C5 Delete the drafts
- [x] C6 Archive the package

## Evidence

[evidence: readiness; inspection of `design-authoring.md`, the file's pages and `skai/promoted/`; no open checkbox, gap, footnote or request; Review advanced and inputs reconciled; all 37 entries are `add` entries linking drafts; `skai/promoted/ui-map-viewer-backfill/design/` does not exist; no request was filed, so no outcome is owed]

[evidence: C1; `Bin/figma-page-check.js` on the change page, no findings; inspection of its 3,327 nodes, every solid fill and stroke binds a color variable, every text node uses a text style, no gap annotations, no duplicate screen names, all 12 component sets are grids; one repair, Icon's padding rebound to `spacing/30`; component set corner radii stay Figma's default container look]

[evidence: C2; inspection comparing `## Design Changes` with the change page; 12 screen entries match 12 frames and 25 component entries match 25 components, none missing or extra]

[evidence: C3; moved through the Figma tool; `Production` holds `UI Map` (8 frames) and `Review Pages` (4 frames); `Components` holds `Icons`, `Controls`, `Map` and `Review`; 321 instances on `Production`, none unlinked; `Bin/figma-page-check.js` on `Production` and `Components`, no findings; screenshots of both pages inspected]

[evidence: C4; inspection; moving kept node IDs, so all 37 links in `design-authoring.md` already resolve: 12 on `Production`, 25 on `Components`; `design-review.html` re-rendered]

[evidence: C5; Figma tool; the empty `ui-map-viewer-backfill` page deleted after confirming it held no nodes; the file's pages are `Production`, `Components` and `Design System`]

[evidence: C6; moved to `skai/promoted/ui-map-viewer-backfill/design/` with `working-docs/`; the empty `skai/changes/ui-map-viewer-backfill/` removed; the new folder is the same depth, so relative links are unchanged and were checked to resolve; `design-review.html` re-rendered]
