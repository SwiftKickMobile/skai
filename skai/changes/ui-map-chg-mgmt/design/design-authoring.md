# Design — UI Map Change Management
[Review page](design-review.html)

## Goal

Update the UI Map designs for change packages, for the change management style in skai#101, where a UI Map change request is authoring against a different base. The code follows later.

## Inputs

- Base: production in the [SKAI design file](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=0-1), including the UI Map and Review Pages designs promoted from `ui-map-viewer-backfill`.
- How a map change is recorded: *Map change items* in [`ui-map-architecture-artifacts.md`](../../../../Guides/UIMap/ui-map-architecture-artifacts.md), and the package layout in [`ui-map-architecture.md`](../../../../Guides/UIMap/ui-map-architecture.md).
- The page today: [`Bin/ui-map-render.py`](../../../../Bin/ui-map-render.py), which draws the proposed map alone, with no comparison to the production map.
- The change management style: [skai#101](https://github.com/SwiftKickMobile/skai/issues/101).
- The review page to draw on: the Design Review design in production, and [`Bin/design-tool.py`](../../../../Bin/design-tool.py).
- Sample content: SKAI's demo map, LumenNotes, from [`ui-map-demo.md`](../../../../Guides/UIMap/ui-map-demo.md), with a made-up change to it.
- Supervisor input: this package covers how the UI Map highlights changes and how a review page like the one for designs fits in. The map page gains a tab for discussion and changes, and changed scenes are marked on the map rather than drawn as a true comparison.

## Discussion

### Highlighting Changes

- [x] D01 [Question] How can the UI Map highlight changes?
  - **Concern** A change package's map page shows the proposed map alone, so a reviewer can't see on the map what the package changes.
  - **Question** How should the map show what changed? To be discussed with the supervisor.
  - **Decision** Changed scenes get a special icon or styling on the proposed map, and selecting one opens the side panel with its entries from the change list. A scene counts as changed when anything about it changes or anything about its outgoing connections changes. There is no true comparison view, because a map can change in too many ways to show them all.

### Review Page

- [x] D02 [Question] How can a UI Map package get a review page similar to the one for designs?
  - **Concern** Design packages have a review page for their discussion and list of changes. A UI Map package has only its map page and a markdown document.
  - **Question** What should a UI Map review page look like, and how does it relate to the map page? To be discussed with the supervisor.
  - **Decision** The discussion and changes are another tab on the map page, named Review, not a separate page.

- [x] D03 [Proposal] The tab and the map link to each other
  - **Concern** A reviewer reading a change in the tab has no direct way to see it on the map, and a reviewer reading an entry in the side panel has no direct way to see it among the other changes and the discussion behind it.
  - **Proposal** Each scene a change touches is a link that switches to the map tab and selects that scene. Each entry in the side panel links to that change in the tab.
  - **Why** The two views answer each other's next question, and the links add little to either one. The alternative is no links, which is simpler, but the reviewer then has to find the scene or the change by hand.
  - **Decision** The tab groups changes by domain, with each domain's color square on its heading, and each entry's header names its scene as a link to the map, the way a design change's header links to its frame. Each entry in the side panel links to that change in the tab. A connection change names the scene it starts from, a domain change names its domain with no link, a moved scene sits under its new domain, and a removed scene sits under its old domain with its name greyed and no link.

### Page Titles

- [x] D04 [Proposal] Every change package's page uses one title format
  - **Concern** The specs review pages don't say which artifact they review, the design review repeats its name on a second line, and the UI Map change page leads with the app's name.
  - **Proposal** One line on every page: the package's ID in black, then the artifact type in cyan, such as note-versions UI Map Change or pinned-notes Design Change. The production map keeps LumenNotes UI Map, which has the same two colors.
  - **Why** A reader most needs to know which artifact and which package they're looking at. Color separates the two more cleanly than a colon or a second line, and each color means the same thing on every page.
  - **Decision** One line on every change package's page: the document type in black, then the package's ID in cyan, such as UI Map note-versions or Design pinned-notes. The word Change is dropped because every one of these pages is a change document. The production map follows the same format as UI Map Production, so its bar no longer shows the app's name.

### Review Page Styling

- [x] D05 [Proposal] The real review pages set the styling for review pages and the UI Map page
  - **Concern** The backfill restyled the review pages' designs to match the UI Map, so they no longer match the real pages, whose typography, spacing and cards read better.
  - **Proposal** The real review pages' typography, spacing and cards become the design, on the light blue-grey background. The UI Map page's top bar, side panel, cards and help take the same styling, while map cells, route boxes and route labels stay compact.
  - **Why** Reviewers read these pages at length, and one look across SKAI's pages is simpler to build and maintain.
  - **Decision** Adopted as proposed. The whole page moves to the system font, including map cells; IDs and route kinds stay monospace. The real review pages also take the mockups' colors, plain cyan references, colored changed words and 56 top bar height.

## Design Changes

### UI Map

- V01 add state: [ui map — changes](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-1740)
  - **01** The map on a change package's page marks each changed scene with a badge set into its bottom right corner, in the same color as the scene's border. A scene counts as changed when anything about it or its outgoing connections changes, so a scene that loses its link to a removed scene carries the badge too.
    - **Justification** A reviewer needs to see on the map where the package changes it, and no comparison view could show every kind of change. Source: Resolved decision: D01.
  - **02** The top bar's title becomes UI Map followed by the package's ID, and the bar gains Map and Review tabs.
    - **Justification** The title says which artifact and package this is, and the discussion and list of changes are the Review tab on this page. Source: Resolved decision: D02 and D04.
- V22 add state: [ui map — changes on](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=107-2856)
  - **Description** A single-item Changes toggle sits to the right of the domain filters, showing how many scenes changed. Turning it on displays changed scenes the way search displays its matches: changed scenes are highlighted, and everything else is dimmed. It follows search's rules with other controls: it doesn't show the hops drop-down, and while a selected scene or domain filter narrows the map, nothing is dimmed.
  - **Justification** A reviewer can pick out every changed scene at a glance on a large map. Source: Supervisor input.
- V02 add state: [ui map — changed scene selected](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-1782)
  - **Description** Selecting a changed scene opens the side panel with a Changes section first, headed by the change icon, listing that scene's entries from the change list. Each entry's ID links to that change in the Review tab. An entry with several changes numbers them, as in the design review. Section heading icons, including the Note heading's, match their heading's color, and the Reached from and Opens headings lose their counts.
  - **Justification** The panel answers what changed here at the moment the reviewer asks, and the link leads to the other changes and the discussion behind them. Source: Resolved decision: D01 and D03.
- V03 add state: [ui map — changes help](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-1821)
  - **Description** How to read this map gains a row explaining the change badge, after the three scene styles and before the icons, shown on a change package's page. Its instructions no longer mention a Clear button, on the production map as well, and explain the Changes toggle on a change package's page.
  - **Justification** The help explains everything else drawn on a scene, and a new mark needs the same explanation. Source: Resolved decision: D01.
- V14 add state: [ui map — production top bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=96-2795)
  - **Description** The production map's top bar, titled UI Map Production, with domain filters in the review pages' style: a bordered group of filters, each with its domain's color, its number of scenes and its name. It replaces the plain row of names, moves to the right of the bar as the review pages' filters are, and applies to every state of the production map.
  - **Justification** The filters on the UI Map and the review pages should look and work alike. Source: Supervisor input.
- V18 add state: [ui map — hops menu](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=103-2811)
  - **Description** The hops control is a drop-down showing the current choice. Opening it lists 1 hop, 2 hops and All, with the current one marked. This applies to the production map as well.
  - **Justification** A drop-down takes less room in the top bar than a segmented control now that the domain filters are grouped beside it. Source: Supervisor input.

### Review

- V04 add screen: [review](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-1967)
  - **Description** The whole Review tab, as tall as its content: the summary box, the discussion, then Map Changes grouped by domain, with each domain's color square on its heading, and otherwise laid out like the design review's Design Changes. Each entry's header shows its marker, ID, type and the scene it belongs to, as a link to that scene on the map. A connection change names the scene it starts from, a domain's own change names the domain with no link, a moved scene sits under its new domain, and a removed scene sits under its old domain with its name greyed and no link. An entry with several changes numbers them, and an entry resting on an open gap carries a numbered footnote with the gap's placeholder. The summary box shows the state and goal. The top bar's filters cover added, modified, removed and moved changes, and the discussion states the package has, among open, gap and resolved.
  - **Justification** A reviewer can read the changes in the same order as the map, and go from any scene to the map. The layout follows the design review page, which a reviewer already knows, with the real review pages' typography, spacing and cards. Source: Resolved decision: D02, D03 and D05.

### Review Pages

- V12 modify state: [product specs review — title and summary](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=91-2634)
  - **Description** The title becomes one line: Product Specs, then the package's ID in cyan. It replaces Change Package and an ID, which didn't say which document type the page reviews. The design specs review follows the same format with Design Specs. On both specs review pages, the summary box loses its title line, which the top bar now covers, leaving the state and goal like the other review pages' boxes.
  - **Justification** Every review page should identify its artifact and package the same way, and open with the same summary box. Source: Resolved decision: D04 and supervisor input.
- V13 modify state: [design review — title](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=91-2734)
  - **Description** The title becomes one line: Design, then the package's ID in cyan. It replaces Design Change and a name, followed by the same name again on a second line.
  - **Justification** Every review page should identify its artifact and package the same way. Source: Resolved decision: D04.

### Components

- V07 add component: [Change Badge](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-2809)
  - **Description** A small square with a triangle that marks a changed scene. It takes the scene's border color, with only its inner corner rounded, so it reads as part of the scene's edge.
  - **Justification** It has to read differently from the coloured domain square and the callout icons already on a scene. Source: Resolved decision: D01.
- V23 add component: [Change Icon](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=111-3069)
  - **Description** The change badge's triangle on its own.
  - **Justification** The side panel's Changes heading leads with the mark, as its Note heading leads with an icon. Source: Supervisor input.
- V06 modify component: [Change Marker](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-2113)
  - **Description** Change Marker gains a cyan Moved status, and every status grows from 10 to 12 to match the real review pages. The size change is already on the production component.
  - **Justification** Moving is a kind of map change that a design or spec review doesn't have. Source: *Map change items* in `ui-map-architecture-artifacts.md`.
- V05 modify component: [Scene Cell](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-2024)
  - **01** Scene Cell gains a Changed option that shows the change badge flush in the bottom right corner, colored to match the border in each state. It's off by default.
    - **Justification** Every kind and state of scene can be changed. Source: Resolved decision: D01.
  - **02** A reused scene now has a grey wash as its fill and a medium-weight title in a new Body Medium text style. The production design gave it a normal scene's fill and a semibold title.
    - **Justification** The production design didn't match the real page, where the wash and lighter title make a reused scene look secondary. Source: Supervisor input.
- V08 add component: [Tab](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-2853)
  - **Description** One tab in the top bar, selected or not.
  - **Justification** The change package's page has two tabs. Source: Resolved decision: D02.
- V17 modify component: [Search Field](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=102-2821)
  - **Description** The search field shows a cross inside it whenever it has a value, which clears the text.
  - **Justification** A cross inside the field is the usual way to clear a search, and it replaces the Clear button's text-clearing job. Source: Supervisor input.
- V19 modify component: [Hops](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=103-2789)
  - **Description** The segmented control becomes a drop-down button with the current choice and a chevron. It's a fixed width that fits its longest choice, so it doesn't move when the choice changes.
  - **Justification** The hops control is now a drop-down. Source: Supervisor input.
- V20 add component: [Hops Menu](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=103-2793)
  - **Description** The list the hops drop-down opens, with the current choice marked.
  - **Justification** The drop-down needs its choices drawn. Source: Supervisor input.
- V09 add component: [Panel Change](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=88-2652)
  - **Description** One change list entry in the side panel, as a card like the Review tab's so it stands apart from the map's own details: its marker, linked ID and kind, then what changes and why, or numbered changes with their reasons. An entry resting on an open gap adds a footnote and the gap's placeholder.
  - **Justification** The panel's Changes section is made of these. Source: Resolved decision: D01.
- V11 modify component: [Review Top Bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=91-2619)
  - **Description** The title and subtitle become one line, with the document type in black and the package's ID in cyan.
  - **Justification** The specs and design review pages share this bar. Source: Resolved decision: D04.
- V15 modify component: [Top Bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=96-2748)
  - **Description** The title becomes UI Map Production in the common format. The domain legend becomes a bordered group of filters built from Filter Choice, showing each domain's color, number of scenes and name. It moves to the right of the bar, next to the tools. The hops control sits just before it and appears only while the map is filtered, so the filters don't move when it appears. The Theme and Clear buttons go.
  - **Justification** The production map's domain filters should match the review pages' filters. Source: Supervisor input.
- V10 add component: [Change Top Bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=69-2924)
  - **Description** The top bar on a change package's page, for each tab. The Map tab shows domain filters in the same bordered group and style as the review filters, each with its scene count, on the right of the bar, then the Changes toggle and search. The hops control sits before the domain filters and appears only while the map is filtered, so the filters don't move when it appears; the Review tab shows the review filters. Both keep help. There's no Theme or Clear button.
  - **Justification** The production map has no tabs and keeps its own top bar. Source: Resolved decision: D02.
- V16 remove component: Domain Filter
  - **Description** The separate domain legend button goes, because the domain filters now use Filter Choice.
  - **Justification** One filter component serves every page. Source: Supervisor input.
- V21 remove component: Hop Choice
  - **Description** The segment used by the old hops control.
  - **Justification** The drop-down has no segments. Source: Supervisor input.

### Design System

- V24 modify component: [Design System](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=3-136)
  - **Description** Text styles move to the system font, drawn with SF Pro Text. Reading and Group Label become 15, Mono Strong becomes 15, and Section Heading at 24, Pill and State Label at 12, and Caption styles at 13 are added, all measured from the real review page. A neutral border color and a two-layer Card shadow are added, matching the real review pages, and cards use a 10 corner radius. These are already in production's design system.
  - **Justification** The real review pages set the styling. Source: Resolved decision: D05.
- V25 modify component: [Kind Pill](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=36-1387)
  - **Description** The text becomes 12 semibold in the main text color, with a neutral border. This is already on the production component.
  - **Justification** It should match the real review page's pills. Source: Resolved decision: D05.
- V26 modify component: [Discussion Header](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=38-40)
  - **Description** The state word becomes 12 regular. This is already on the production component.
  - **Justification** It should match the real review page. Source: Resolved decision: D05.
- V27 modify component: [Filter Choice](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=36-1386)
  - **Description** The count and label become 12, with 10 side padding. This is already on the production component.
  - **Justification** It should match the real review page's filters. Source: Resolved decision: D05.

## Assumptions and TODOs

- The sample change is made up: it adds a version history to the LumenNotes demo map, changes how the share sheet opens, moves folders and trash to a new domain, and removes the onboarding scene.
- The `Design System` page gains the Body Medium text style for reused scenes. It's a shared style, so it's in place ahead of promotion.
- The page always follows the system theme. Selection and domain filters are undone the ways they're set, because no single button resets everything now.
- The Button component's Text style has no remaining use once the Theme and Clear buttons go, so it can be removed at promotion.
- The text style changes apply across the whole design file as soon as they're made, so production frames already show the new font and sizes. The shared Kind Pill, Discussion Header, Change Marker and Filter Choice components were corrected in place too. Production's cards and spacing change only at promotion.
- JetBrains Mono stays for IDs and route kinds. The real review pages use the system's monospace font, which isn't available in Figma.
- The page opens on the Map tab, and hover looks and animation aren't drawn.
- A change with no scene to mark, such as a domain change or the removal of a scene nothing linked to, appears only in the Review tab.
- A change that touches several scenes is split into one entry per scene.
- The Review tab and the markers appear only on a change package's map page. The production map has nothing to compare against.
- TODO for the UI Map guide: the *Map change items* rules in `ui-map-architecture-artifacts.md` need to require this grouping and placement, replacing today's flat order, using the format below. They also need numbered changes in place of the sub-list inside **Description**, and gap footnotes on entries, as Design Changes has. The renderer's Review tab depends on this format, so the guide change lands first.
  - `## Map Changes` has a `### <domain>` heading per domain, in the map's domain order, with entries in the map's scene order within it (`M.order` in the viewer).
  - An entry is `- M<n> <Type>: <identity>`. The identity is the scene's ID, or the domain's ID for a domain change. Each entry belongs to one scene, so a change to several scenes is several entries.
  - A route entry's identity is the scene it starts from, and its text names the target. A moved scene sits under its new domain, and its text names the old one. A removed scene sits under its old domain, with its former ID.
  - The **Touches** line goes, because the heading and identity replace it.
  - The badge comes from these entries: a scene is marked when an entry names it. The route rule above is what makes this match the definition of a changed scene.
- TODO for the UI Map guides: say production map in place of official map throughout, and carry this in the skai#101 notes.
- TODO for the code: the renderer needs to fail when an entry names a scene that isn't on the proposed map, except for a removed scene.
- TODO for the code: the viewer needs domain filters that match the review pages' filters, including each domain's scene count, in `Bin/ui-map-viewer.v1.js` and `Bin/ui-map-viewer.v1.css`.
- TODO for the code: add the Changes toggle, its changed-scene count and its highlight display in `Bin/ui-map-viewer.v1.js` and `Bin/ui-map-viewer.v1.css`.
- TODO for the code: replace the segmented hops control with the drop-down in `Bin/ui-map-viewer.v1.js` and `Bin/ui-map-viewer.v1.css`.
- TODO for the code: make the side panel's section heading icons match their heading's color in `Bin/ui-map-viewer.v1.css`, and remove the counts from its Reached from and Opens headings in `Bin/ui-map-viewer.v1.js`.
- TODO for the code: remove the Theme and Clear buttons and the saved theme, add the search field's cross, and update the help text, in `Bin/ui-map-viewer.v1.js`, `Bin/ui-map-viewer.v1.css` and rule 12 in `Bin/ui-map-render.py`.
- The designs lead: the code builds what's drawn, using the Design System's values, including where they round a real page's value to the nearest spacing step in the design rules. The real review pages' typography, spacing and cards are already close, so most of their stylesheet stays.
- TODO for the code: in `Bin/spec-review.v1.css`, take the mockups' colors in light and dark: the page, card, border, text, muted text and link colors, cyan monospace references with no tinted background, and green and red changed words with no highlight. Take the Design System's text sizes and the 56 top bar height. This replaces the backfill's TODO to restyle the review pages to its earlier design.
- TODO for the code: in `Bin/ui-map-viewer.v1.css`, use the system font everywhere except IDs and route kinds, which stay monospace, and use the review pages' cards, border and shadow for the Changes entries in the side panel. Remove Archivo from the font link in `Bin/ui-map-render.py`, and keep the app's name in the page's `<title>`, which a browser tab shows, since the bar no longer does. Dark mode uses the Design System's dark colors, and the Card shadow uses the real review pages' dark values: 1px down with 3px blur at 50%, and 4px down with 12px blur at 35%. Use the Design System's title size in the top bar, the fixed 70 wide hops drop-down, the 20 square change badge with white triangle, and the reused scene styling the running page already has.
- TODO for the code: build the change package's page in `Bin/ui-map-render.py` and the viewer. It reads the discussion and `## Map Changes` from the package's `ui-map-architecture.md`, draws the Map and Review tabs, marks each scene that has a change entry, counts them on the Changes toggle, shows a scene's entries in the side panel, and links scene headings and entry IDs between the tabs. The production map's page has none of this.
- TODO for the code: the backfill's other owed items still stand: updating the viewer's stylesheet to the Design System's merged colors and sizes, centering the map to the left of the open side panel, and removing the side panel's Specs section. They're listed in the promoted `ui-map-viewer-backfill` package.
- TODO for promotion: the text styles, type sizes, border color, Card shadow, Body Medium, Design System page rows, and the Kind Pill, Discussion Header, Change Marker and Filter Choice edits are already in production, so promotion checks them rather than applying them again.
- TODO for the code: remove the title line from the summary box in `Bin/spec-tool.py`, so every review page's box has only the state and goal.
- TODO for the code: `Bin/spec-tool.py`, `Bin/design-tool.py` and `Bin/ui-map-render.py` need to build the title this way, including a request's chained ID, such as offers | 001.
- The inputs are SKAI's own guides and code, so there are no requests to file. Where the designs and the inputs differ, the TODOs here carry the change. SKAI has no design specs to write for these pages.
- TODO for skai#101: add the planning notes and a pointer to this package, and note that all the review documents move to this title format and the same summary box, state and goal with no title line, when the issue is implemented.

## Out of scope

- Writing the guide and code changes. They follow when skai#101 is implemented.
- Keeping production unchanged until promotion. The design system and shared component edits stay in place; skai#126 covers how future packages should draft these.

## Decision Log

- D01 decided — changed scenes are marked on the proposed map and the side panel shows their change entries; no true comparison view.
- D02 decided — discussion and changes are another tab on the map page.
- D02 decided — the tab for discussion and changes is named Review.
- D03 decided — the tab groups changes by domain and scene; scene headings link to the map and side panel entries link to the tab.
- D03 decided — the tab groups changes by domain; each entry's header links to its scene, matching the design review's layout.
- D04 decided — every change package's page shows its ID in black, then its artifact type in cyan.
- D04 decided — every change package's page shows its document type in black, then its ID in cyan, without the word Change.
- D04 decided — the production map's title follows the same format as UI Map Production.
- D05 decided — the real review pages set the styling; the whole page uses the system font.
- D05 decided — the real review pages also take the mockups' colors, references, changed words and top bar height.
