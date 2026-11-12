# Design Promotion — UI Map Change Management

## Inputs

- Package: [design-authoring.md](design-authoring.md) ([review page](design-review.html)), 27 Design Changes: 13 added, 12 modified, 2 removed.
- Base: production in the [SKAI design file](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=0-1): `Production`, `Components` and `Design System`.
- Non-base inputs the decisions changed: SKAI's UI Map guides and page code, changed by skai#101 (`8ca3775`) and skai#94 (`df40e8e`).

## Promotion Checks

- [x] C1 Drafts meet the conventions
- [x] C2 Inventory matches the drawings
- [x] C3 The base absorbs the package — including the production edits made ahead of promotion (text styles, type sizes, border color, Card shadow, Body Medium, Design System rows, and the Kind Pill, Discussion Header, Change Marker and Filter Choice components), checked rather than applied again, and the Button component's Text style removed now that nothing uses it
- [x] C4 Links point at the base
- [x] C5 Archive the package

## Evidence

### Run 1

[evidence: readiness 1; `ls skai/changes/ui-map-chg-mgmt/` and the artifact's Discussion; no `changes/` request folder in the change; D01–D05 resolved, no footnotes or gaps; review page counts `open: 0, gaps: 0`; nothing promoted under the change]
[evidence: readiness 2; `python3 Bin/design-tool.py render --authoring skai/changes/ui-map-chg-mgmt/design/design-authoring.md`; renders, 13 added, 12 modified, 2 removed, 5 resolved; Discussion resolved; the package's code and guide TODOs are carried out by skai#101 and skai#94 (below)]
[evidence: readiness 3; `## Design Changes`; every add and modify entry links a Figma node; the two remove entries (V16 Domain Filter, V21 Hop Choice) name the base component]
[evidence: readiness 4; `ls skai/promoted/`; `skai/promoted/ui-map-chg-mgmt/design/` absent]
[evidence: readiness 5; the package's TODOs against its inputs, checked against skai main: Map Changes grouping and identity rules, "production map" wording and the off-map entry check (`8ca3775`); domain filters with counts, Changes toggle, hops drop-down, panel heading icons and counts, no Theme or Clear button, search cross, help text, system font, Archivo removed, change package page with Map and Review tabs (`8ca3775`, `ui-map-viewer.v2.*`, `ui-map-render.py`); review page colors, summary box without title line, one-line titles with chained IDs (`df40e8e`, `spec-review.v2.*`, `skai-pages.v1.*`, `spec-tool.py`, `design-tool.py`); the backfill's owed items: map laid out left of the open panel and no Specs section (`ui-map-viewer.v2.js`)]
[evidence: C1; `Bin/figma-page-check.js` on the change page (69:1736), no findings; inspection of its 1,734 nodes: no gap annotations, every text node uses a text style, every solid fill and stroke outside instances binds a color variable but the four Sections' own borders, which production's Sections share]
[evidence: C2; inspection comparing `## Design Changes` with the change page; 9 frame entries match the 9 frames and 12 component entries the 12 components, none missing or extra; V24–V27 link production nodes edited in place; V16 and V21 name production components]
[evidence: C3; Figma tool; backups `Production — Pre ui-map-chg-mgmt` and `Components — Pre ui-map-chg-mgmt`, every instance in them linked to the Components backup; 12 components copied in, 6 replacing Scene Cell, Change Marker, Top Bar, Review Top Bar, Search Field and Hops; 128 frame instances and 30 nested ones switched; Domain Filter, Hop Choice, the 6 replaced components and Button's Text style removed once unused (the drafts were pointed at the backup copies first); 7 frames copied; rules carried to all 12 existing frames per [working-docs/fold-audit.md](working-docs/fold-audit.md); Section Heading, Body Medium and Card present (V24–V27 checked, not re-applied); `Bin/figma-page-check.js` on `Production` and `Components`, no findings; 1,149 instances on `Production` and 144 on `Components`, all linked to `Components`; every touched frame screenshotted and inspected, three repairs listed in the audit]
[evidence: C4; 21 links in `design-authoring.md` repointed from the change page to production nodes (V04 now reads `ui map — review`; V12 and V13 to the modified `product specs review` and `design review`), each confirmed by node lookup; V24–V27 already linked production; `design-review.html` re-rendered]
[evidence: C5; `git mv` to `skai/promoted/ui-map-chg-mgmt/design/` with `working-docs/`; the empty `skai/changes/ui-map-chg-mgmt/` removed; the new folder is the same depth, so relative links are unchanged and all resolve (checked); nothing else in the repo links into the old path; `design-review.html` re-rendered; the supervisor deletes the backups and the draft page in Figma]
