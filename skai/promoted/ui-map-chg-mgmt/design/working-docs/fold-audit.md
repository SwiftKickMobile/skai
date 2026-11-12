# Fold Audit — ui-map-chg-mgmt into Production

C3's working document: the rules `## Design Changes` sets, then every base frame on `Production` against them, with what changed. Updated as applied.

## Rules

- **R1 Production top bar** (V14, V15, V18, V19): title UI Map Production; domain filters as a bordered group of Filter Choice with scene counts, on the right; the hops drop-down sits before them and shows only while the map is filtered; no Theme or Clear button. Every state of the production map.
- **R2 Search cross** (V17): the search field shows a clearing cross when it has a value.
- **R3 Help text** (V03): the instructions no longer mention a Clear button.
- **R4 Panel headings** (V02): Reached from and Opens lose their counts; heading icons take their heading's color.
- **R5 Reused scene** (V05 02): a grey wash fill and a medium-weight title.
- **R6 Review titles** (V11, V12, V13): one line, the document type in black, then the package's ID in cyan.
- **R7 Summary box** (V12): no title line, only state and goal.
- **R8 Review page look** (D05 via V04, V24; spacing checked against `spec-review.v2.css`): cards at `radius/10` with the Card shadow and the neutral border, 10 apart; content 30 below the top bar; summary box padding 10/15/15/15, gap 5; section headings 40 above, in Section Heading; topic groups 20 above with gap 10; a one-line resolved item 5 top and bottom.
- **R9 Change Marker** (V06): a Moved status; size 12 already in production.
- **R10 Already in production** (V24–V27): text styles, sizes, border color, Card shadow, Body Medium, Design System rows, Kind Pill, Discussion Header, Filter Choice: checked, not applied again.

## Base Frames

| Frame | Rules | Change |
| --- | --- | --- |
| `ui map` (16:46) | R1, R5 | new Top Bar, hops hidden; reused scene washed |
| `ui map — scene selected` (16:358) | R1, R4 | new Top Bar, 1 hop; panel headings without counts, Note icon in the heading's color |
| `ui map — 2 hops` (16:583) | R1, R4, R5 | new Top Bar, 2 hops; panel headings as above; reused scene washed |
| `ui map — all` (16:828) | R1, R4, R5 | new Top Bar, All; panel headings as above; reused scene washed |
| `ui map — panel closed` (17:753) | R1 | new Top Bar, 1 hop |
| `ui map — domains filtered` (17:911) | R1, R5 | new Top Bar, 1 hop, Note and Other pressed in their domain colors; reused scene washed |
| `ui map — search` (17:1137) | R1, R2, R5 | new Top Bar, search focused with its cross; reused scene washed |
| `ui map — help` (18:1160) | R1, R3, R5 | new Top Bar; "or use Clear" gone from the instructions; reused scene washed |
| `product specs review` (40:4) | R6, R7, R8, R9 | one-line title Product Specs pinned-notes; summary box without its title; 10 cards restyled, 2 one-line items, headings 40 above in Section Heading, groups 20 above; frame 2157 tall to show the page |
| `product specs review — term popover` (42:172) | R6, R8, R9 | title; 4 cards restyled; heading in Section Heading; the scrolled content keeps the term under its popover |
| `product specs review — filtered` (42:267) | R6, R8, R9 | title; 2 cards restyled; headings in Section Heading; scroll position kept |
| `design review` (44:2) | R6, R8 | one-line title Design pinned-notes; summary box padding; 9 cards restyled, 3 one-line items; headings and groups as above |

## Components

| Component | Change |
| --- | --- |
| Scene Cell, Change Marker, Top Bar, Review Top Bar, Search Field, Hops | replaced by the package's versions; every instance swapped |
| Change Badge, Change Icon, Tab, Hops Menu, Panel Change, Change Top Bar | added |
| Domain Filter, Hop Choice | removed once unused |
| Button's Text style | removed once unused |

## Added Frames

Copied into `UI Map`, every instance switched to `Components`: `ui map — production top bar` and `ui map — hops menu` under the production states; `ui map — changes`, `— changes on`, `— changed scene selected`, `— changes help` in a third column; the Review tab, named `ui map — review`, in a fourth.

## Repairs While Copying

- Hops: its label wrapped "2 hops" (a fixed-width fill); it now hugs on one line with the chevron pushed right, as the viewer's CSS does, within the 70 width.
- Pressed domain filters lost their domain color (the variant drops the override); restored on `ui map — domains filtered`.
- The scrolled review crops first took the summary-box spacing; restored to their scroll position.
