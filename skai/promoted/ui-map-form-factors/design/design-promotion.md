# Design Promotion — UI Map Form Factors

## Inputs

- Package: [design-authoring.md](design-authoring.md) ([review page](design-review.html)), 17 Design Changes: 11 added, 6 modified, none removed.
- Base: production in the [SKAI design file](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=0-1), the `Production` and `Components` pages.
- Design file: SKAI; drafts on the `ui-map-form-factors` change page.

## Promotion Checks

- [x] C1 Drafts meet the conventions
- [x] C2 Inventory matches the drawings
- [x] C3 The base absorbs the package
- [x] C4 Links point at the base
- [x] C5 Archive the package

## Evidence

[evidence: readiness 1; the artifact's Discussion holds no items, `design-review.html` counts `open: 0, gaps: 0`, no footnotes; `ls skai/changes/` shows only this change, with no `changes/` request folder; nothing promoted under the change]
[evidence: readiness 2; `## Design Changes` current after the supervisor's approval (2026-11-12) and the inputs reconciled under `## Assumptions and TODOs`]
[evidence: readiness 3; all 17 entries are `add` or `modify` and link drafts on the change page]
[evidence: readiness 4; `ls skai/promoted/ui-map-form-factors` — absent]
[evidence: readiness 5; no decision changed a non-base input; the page's code the designs called for is built (`Bin/ui-map-viewer.v2.*`, `Bin/ui-map-render.py`, `Guides/UIMap/ui-map-demo.md`)]
[evidence: C1; `Bin/figma-page-check.js` on the change page (161:3060), no findings; inspection of its 1,709 nodes: no gap annotations, every text node outside instances uses a text style, three white icon fills inherited from Hops and Hops Menu were unbound and are now bound to `brandWhite`]
[evidence: C2; `## Design Changes` against the change page: 9 frame entries (V01–V06, V14, V15, V17) match the 9 frames in `UI Map`, 8 component entries (V07–V13, V16) match the 8 components in `Components`; none missing or extra]
[evidence: C3; [working-docs/fold-audit.md](working-docs/fold-audit.md) names all 19 base frames against 6 rules — none changes, since no production state shows a map with form factors or a selected scene with a modal style; 6 components replaced and 301 `Production` instances relinked, 2 added; 9 frames copied in as three columns; backups `Production — Pre ui-map-form-factors` (177:6101) and `Components — Pre ui-map-form-factors` (177:5053); `Bin/figma-page-check.js` on `Production` and `Components`, no findings; no `Production` instance links to the change page (0 of 1,644); every touched frame screenshotted]
[evidence: C4; 17 links in `design-authoring.md` repointed from the change page to production nodes, each confirmed by node lookup; `design-review.html` re-rendered]
[evidence: C5; moved to `skai/promoted/ui-map-form-factors/design/` with `working-docs/` (supervisor's go at Base review, 2026-11-12); the empty `skai/changes/ui-map-form-factors/` removed; the new folder is the same depth, so relative links are unchanged and all four resolve (checked); `design-review.html` re-rendered]
