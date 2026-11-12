# Fold Audit — ui-map-form-factors into Production

C3's working document: the rules `## Design Changes` sets, then every base frame on `Production` against them, with what changed.

## Rules

- **R1 Form-factor drop-down** (V01 01, V02, V10, V11, V12, V13): shown only on a map that declares two or more form factors.
- **R2 Scene icon** (V01 02, V07, V08): a scene with form factors shows the form-factor icon.
- **R3 Route label icon** (V01 03, V16): a route label whose box holds a marked route shows the icon.
- **R4 Graying out and the swap** (V03, V17, V04 01): only with a form factor chosen.
- **R5 Side panel** (V04 02, V05, V09, V14, V15): route form factors, a Form factors section, and the Modal style section (one chip per style, or per form factor).
- **R6 Help** (V06): form-factor rows and sentence only on a map with form factors.

## Base Frames

| Frame | Rules | Change |
| --- | --- | --- |
| `ui map` (16:46) | — | none: the map has no form factors; components relinked |
| `ui map — scene selected` (16:358) | R5 | none: Library has no modal style or form factors; components relinked |
| `ui map — 2 hops` (16:583) | R5 | none, as above |
| `ui map — all` (16:828) | R5 | none, as above |
| `ui map — panel closed` (17:753) | — | none; components relinked |
| `ui map — domains filtered` (17:911) | — | none; components relinked |
| `ui map — search` (17:1137) | — | none; components relinked |
| `ui map — help` (18:1160) | R6 | none: no form factors; components relinked |
| `ui map — production top bar` (152:7535) | R1 | none: no form factors; components relinked |
| `ui map — hops menu` (152:7537) | R1 | none; components relinked |
| `ui map — changes` (152:7540) | — | none; components relinked |
| `ui map — changes on` (152:7579) | — | none; components relinked |
| `ui map — changed scene selected` (152:7618) | R5 | none: Note has no modal style or form factors; components relinked |
| `ui map — changes help` (152:7665) | R6 | none: no form factors; components relinked |
| `ui map — review` (152:7812) | — | none |
| `product specs review` (40:4), `— term popover` (42:172), `— filtered` (42:267), `design review` (44:2) | — | none |

## Components

| Component | Change |
| --- | --- |
| Icon, Scene Cell, Route Label, Top Bar, Change Top Bar, Panel Row | replaced by the package's versions; every instance on `Production`, `Components` and the change page swapped (301 on `Production`), then the old ones removed |
| Form Factor, Form Factor Menu | added to `Controls`, after Hops Menu |

## Added Frames

Copied into `UI Map` as three columns after `ui map — review`, every instance switched to `Components`: `ui map — form factors` and `— form factor menu`; `— phone`, `— tablet` and `— tablet scene selected`; `— form factors scene selected`, `— modal style scene selected`, `— modal style scene selected without form factors` and `— form factors help`. `Review Pages` moved right to keep 100 between Sections.

## Backups

`Production — Pre ui-map-form-factors` and `Components — Pre ui-map-form-factors`; every instance in them linked to the Components backup, whose standalone components were copied in as components (the page copy had turned them into instances).
