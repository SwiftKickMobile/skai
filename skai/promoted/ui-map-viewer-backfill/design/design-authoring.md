# Design — UI Map Viewer Backfill
[Review page](design-review.html)

## Goal

Mock up SKAI's existing pages as SKAI's first production designs, in SKAI's design system: the UI Map page, the interactive map the renderer writes, and the two review pages, product specs review and design review. Later work that adds change management to the UI Map page will build on these designs.

## Inputs

- Base: production in the [SKAI design file](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=0-1). It's empty, with only a `Production` page.
- The running page: SKAI's demo map, LumenNotes, from [`Guides/UIMap/ui-map-demo.md`](../../../../Guides/UIMap/ui-map-demo.md), rendered by the current viewer. This is the sample content for every frame.
- The page's own description: rule 12 (HTML output) in the header of [`Bin/ui-map-render.py`](../../../../Bin/ui-map-render.py).
- The page's look and behavior: [`Bin/ui-map-viewer.v1.css`](../../../../Bin/ui-map-viewer.v1.css) and [`Bin/ui-map-viewer.v1.js`](../../../../Bin/ui-map-viewer.v1.js).
- The review pages: what they show comes from [`Bin/spec-tool.py`](../../../../Bin/spec-tool.py) (product specs and design specs review) and [`Bin/design-tool.py`](../../../../Bin/design-tool.py) (design review). Their look and behavior come from [`Bin/spec-review.v1.css`](../../../../Bin/spec-review.v1.css) and [`Bin/spec-review.v1.js`](../../../../Bin/spec-review.v1.js), which all three share. Rendered pages in real change packages show the parts and states they use. Only their layout is taken from them; the sample content is made-up LumenNotes specs and designs (supervisor input).

## Discussion

### Setting Up The Design File

- [x] D01 [Proposal] Record the file's conventions to match the page as it is today
  - **Concern** The SKAI file has no `Design System` page, so nothing yet records the choices the designs depend on: target size, platform, dark mode, button label case and UI kits.
  - **Proposal** One target size, `Desktop`, at 1440 × 900. The platform is the web, drawn in a desktop browser with no browser chrome. Dark mode is supported, so colors get `Light` and `Dark` modes. Button labels use sentence case. There are no UI kits.
  - **Why** The page is a desktop tool with a fixed cell width that scrolls instead of shrinking, so a phone size has nothing to show. It follows the system theme and has its own theme toggle. Its labels are single words or sentence case ("How to read this map").
  - **Decision** Adopted as proposed. Smaller windows and phones aren't targeted. The designs use fonts Figma provides; a font the page uses that Figma doesn't provide is replaced.
- [x] D02 [Proposal] Build the `Design System` and `Components` pages as part of this backfill
  - **Concern** The guide says those pages are edited on purpose, never as a side effect of screen work. But the file has neither, and every frame needs their colors, text styles, spacing and components.
  - **Proposal** This backfill builds the `Design System` page, with `Conventions`, `Colors`, `Text Styles` and `Dimensions`, from the page's stylesheet: its color tokens in both themes, the domain palette, and its two fonts, Archivo and JetBrains Mono. The page's parts are drawn as components: scene cells, route boxes, route labels, side panel rows, and the top bar controls. They wait in this change's `Components` Section until promotion.
  - **Why** There's nothing else for the designs to come from. Doing it here, on purpose and recorded as design changes, meets the rule's aim.
  - **Decision** Adopted: this backfill builds the `Design System` and `Components` pages.

### What The Page Shows

- [x] D03 [Proposal] Leave the empty Specs section out of the side panel
  - **Concern** Every scene's side panel ends with a Specs heading over "No sidecar yet." It's reserved for a feature that doesn't exist, so it tells the reader nothing.
  - **Proposal** Don't draw it. The change management work that follows will design what the panel shows about specs.
  - **Why** A design should show what the page is meant to show. A placeholder for an unbuilt feature belongs to the work that builds it.
  - **Decision** The side panel has no Specs section, now or later; the feature is dropped. It's left out of the designs, and the viewer and the renderer's description lose it too.
- [x] D04 [Proposal] With All hops, keep the selected scene clear of the side panel
  - **Concern** The page's own description puts the selected scene fully in view and clear of the side panel ahead of every other placement rule. With All hops, the running page leaves the selected scene in its usual place on the full map, which can sit under the side panel. I saw this with a larger map than the demo; the demo map is small enough that its All view keeps the selected scene clear.
  - **Proposal** Treat it as a viewer defect and file it on the skai repo. The mockups need no change, because the demo map's All view already shows the intended placement.
  - **Why** The description says the selected scene must be visible first, and a hidden selection leaves the reader nothing to look at. The running page breaks that rule only in the All view.
  - **Decision** While the side panel is open, the map is centered in the area to the left of the panel. A map too wide for that area starts at the area's left edge and runs on under the panel, with the selected scene kept clear of it. The running page centers the map in the whole window instead, which is a viewer defect to fix.

## Design Changes

### UI Map

- V01 add screen: [ui map](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=16-46)
  - **01** The whole map: the top bar with the app name, domain legend, search, Clear, Theme and help, and every scene laid out in rows under its home, its route boxes and connectors labelled by route kind.
    - **Justification** This is the page as it runs today. Source: the running page and rule 12 of the renderer's description.
  - **02** Spacing, gaps and corner radii round to the nearest step on the design scale: cell and box gaps become 10, the gap between rows 40, and so on.
    - **Justification** SKAI's design rules allow only scale values, and the designs follow the stylesheet as closely as those rules allow. Source: Supervisor input.
  - **03** Colours the stylesheet mixes on the fly, such as the dimmed route label and the highlighted route box, are fixed colours of their own, with light and dark values.
    - **Justification** Every colour in a design binds a named colour so it follows dark mode. Source: Resolved decision: D02.
  - **04** Colours and text styles that differ too little to matter are merged: 16 colours plus the 9 domain colours, and 7 text styles at four sizes (14, 12, 11 and 10). For example, the hover and note backgrounds share the raised-surface colour; highlighted scene borders are cyan and TODO borders amber; connectors use the line colour; and control text, chips, cell titles and route labels each fold into a style with a neighbouring size or weight. A transparent colour is a solid colour at a round opacity, named for both: brandBlack05, brandCyan05, black20 and black35; the 4% and 6% brand black washes become one 5% wash.
    - **Justification** The stylesheet's near-duplicates add nothing a reader can tell apart. The stylesheet will be updated to the merged set. Source: Supervisor input.
- V02 add state: [ui map — scene selected](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=16-358)
  - **01** A selected scene: the map shows only the scenes one hop away, the selected scene and its routes are highlighted, and the side panel lists where the scene is reached from, what it opens, and its notes.
    - **Justification** Selecting a scene is the page's main use. Source: the running page and rule 12.
  - **02** The side panel ends after the scene's notes, implements and modal style. It has no Specs section.
    - **Justification** The Specs feature is dropped. Source: Resolved decision: D03.
  - **03** The panel's close button is a drawn cross icon instead of a large "×" character.
    - **Justification** A text glyph would need a one-off font size outside the text styles, and an icon matches the other panel icons. Source: Resolved decision: D02.
  - **04** The map is centered in the area to the left of the side panel, not in the whole window.
    - **Justification** The panel covers the right of the window, so a map centered in the whole window sits off-center and partly under it. Source: Resolved decision: D04.
- V03 add state: [ui map — 2 hops](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=16-583)
  - **Description** The filter reaches two hops from the selected scene, so its neighbours' own connections appear too. The map is centered in the area to the left of the side panel (D04).
  - **Justification** The hops control is one of the page's filters. Source: the running page and rule 12.
- V04 add state: [ui map — all](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=16-828)
  - **Description** All hops: the whole map stays, with everything not connected to the selected scene dimmed. The map is too wide for the area to the left of the side panel, so it starts at that area's left edge and its right end runs under the panel (D04).
  - **Justification** The hops control is one of the page's filters. Source: the running page and rule 12.
- V05 add state: [ui map — panel closed](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=17-753)
  - **Description** The side panel is closed while a scene stays selected; the map keeps its place and the area the panel covered shows again.
  - **Justification** Closing the panel without clearing the selection is a separate mode of the page. Source: the running page and rule 12.
- V06 add state: [ui map — domains filtered](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=17-911)
  - **Description** Two domains chosen in the legend: the map shows those domains' scenes and the scenes the hop setting reaches from them, with their connections, and the chosen domains are marked in the top bar.
  - **Justification** The domain legend is a filter that can combine several domains. Source: the running page and rule 12.
- V07 add state: [ui map — search](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=17-1137)
  - **Description** Text in the search field: scenes whose names match are highlighted and everything else is dimmed.
  - **Justification** Search highlights matches before Enter selects one. Source: the running page and rule 12.
- V08 add state: [ui map — help](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=18-1160)
  - **Description** How to read this map, over the dimmed page: the scene and route box vocabulary, the route kinds, and how to use the viewer. The dialog's content scrolls.
  - **Justification** The help button opens this explanation. Source: the running page and rule 12.

### Product Specs Review

- V24 add screen: [product specs review](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=40-4)
  - **01** The whole page, as tall as its content: the top bar with the change and state filters, the package card with its state and summary, the Documents list with each file's change and count, Discussion grouped by topic with resolved items collapsed and an open item and a gap item expanded, and a changed file with its heading and reason, its introduction with changed words marked, and its items, one changed with a table and numbered rules that are added, removed and kept, one added with a gap footnote and its note, and unchanged items collapsed.
    - **Justification** It's the page a reviewer reads from top to bottom; most of a review is settling discussion items and reading changed files. It also serves the design specs review page, which shares this design. Source: Supervisor input.
  - **02** The review pages take SKAI's design system: its fonts, colours, cards and spacing replace the system font and the pages' own colours. Text sizes round to the type scale, with body text at 14 and file headings at 20.
    - **Justification** The review pages are SKAI's own pages and should look like the rest of SKAI. Source: Supervisor input.
  - **03** References to other items are cyan monospace text instead of tinted chips, and changed words are green when added and red with a line through when removed, instead of highlighted.
    - **Justification** Inline chips and highlights break up long wrapped sentences; coloured text marks the same things with less noise. Source: Supervisor input.
  - **04** Colours and text styles are added to the design system for the review pages: green and red for added and removed, and Heading, Reading, Reading Strong, Group Label, Mono and Mono Strong.
    - **Justification** The UI Map's compact styles are too small for pages that are read at length, and the system had no colours for added and removed. Source: Supervisor input.
- V27 add state: [product specs review — term popover](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=42-172)
  - **Description** A glossary term under the pointer opens its definition beside it, with the file it comes from.
  - **Justification** Terms are defined in the glossary, and the page shows a definition without leaving the item being read. Source: Supervisor input.
- V28 add state: [product specs review — filtered](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=42-267)
  - **Description** With a change filter on, only items with that change show, and files and groups with none are left out.
  - **Justification** Filters let a reviewer look at one kind of change across every file. Source: Supervisor input.

### Design Review

- V29 add screen: [design review](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=44-2)
  - **Description** The whole page, as tall as its content: the top bar with the package's name and its filters, the status card with the goal, Discussion with resolved items collapsed and a gap item expanded, then Design Changes grouped by screen, each entry showing its change, the kind of change and the frame it links to, then its description or numbered changes, its reason, and any gap footnotes; a removed entry is greyed out.
  - **Justification** It's the page a reviewer reads from top to bottom, and reviewing the drawings starts from its Design Changes list. Source: Supervisor input.

### Components

- V09 add component: [Domain Swatch](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=5-3)
  - **Description** The small square that shows a scene's domain colour.
  - **Justification** It's used in cells, the legend and the side panel. Source: Resolved decision: D02.
- V10 add component: [Icon](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=5-22)
  - **Description** The page's line icons: note, implements, modal, reused scene, and close.
  - **Justification** Cells, route labels, the side panel and the help dialog share them. Source: Resolved decision: D02.
- V11 add component: [Scene Cell](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=5-163)
  - **Description** One scene on the map, as a full scene, a reused scene or a TODO scene, at rest, under the pointer, highlighted or selected; it shows the scene's domain and which callouts it has.
  - **Justification** Every scene on the map is one of these. Source: Resolved decision: D02.
- V12 add component: [Route Box](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=6-26)
  - **Description** The box around the scenes one scene reaches by one route kind, or the parts a composite scene embeds, at rest or highlighted.
  - **Justification** Every route container on the map is one of these. Source: Resolved decision: D02.
- V13 add component: [Route Label](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=6-42)
  - **Description** The route kind on a connector, with a note mark when the route carries a note; at rest, dimmed or highlighted.
  - **Justification** Every connector carries one. Source: Resolved decision: D02.
- V14 add component: [Domain Filter](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=6-49)
  - **Description** One domain in the top bar legend, chosen or not.
  - **Justification** The legend is the domain filter. Source: Resolved decision: D02.
- V15 add component: [Hop Choice](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=6-54)
  - **Description** One choice in the hops control, chosen or not.
  - **Justification** The hops control is built from these. Source: Resolved decision: D02.
- V16 add component: [Hops](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=6-76)
  - **Description** The 1 hop, 2 hops and All control, shown while the map is filtered.
  - **Justification** It sets how far a filter reaches. Source: Resolved decision: D02.
- V17 add component: [Button](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=6-81)
  - **Description** The top bar buttons: Clear and Theme, and the help button.
  - **Justification** The top bar's actions use it. Source: Resolved decision: D02.
- V18 add component: [Search Field](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=6-88)
  - **Description** Find a scene: empty, filled, or focused while typing.
  - **Justification** Search is one of the page's filters. Source: Resolved decision: D02.
- V19 add component: [Top Bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=7-31)
  - **Description** The page header, with the hops control shown only while the map is filtered.
  - **Justification** Every state shares it. Source: Resolved decision: D02.
- V20 add component: [Panel Header](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=7-68)
  - **Description** The selected scene's name and domain, and the close button.
  - **Justification** The side panel opens with it. Source: Resolved decision: D02.
- V21 add component: [Panel Row](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=7-87)
  - **Description** A route into or out of the selected scene, marked home or reused when the scene appears more than once; at rest or under the pointer.
  - **Justification** The panel's Reached from and Opens lists are made of these. Source: Resolved decision: D02.
- V22 add component: [Panel Note](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=7-88)
  - **Description** A note from the map, led by its route kind when it belongs to a route.
  - **Justification** The panel shows the scene's notes and route notes. Source: Resolved decision: D02.
- V23 add component: [Chip](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=7-91)
  - **Description** A value in the panel: an implemented variant or the modal style.
  - **Justification** The panel's Implements and Modal style sections use it. Source: Resolved decision: D02.
- V31 add component: [Change Marker](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=36-1377)
  - **Description** The small square that marks an item, row or file as added, modified, removed or unchanged.
  - **Justification** Every change on the review pages carries one. Source: Supervisor input.
- V32 add component: [Filter Choice](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=36-1386)
  - **Description** One filter in the top bar, with its marker, count and label, on or off.
  - **Justification** The top bar's filters are made of these. Source: Supervisor input.
- V33 add component: [Kind Pill](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=36-1387)
  - **Description** An outlined label for an item's kind or a package's state, such as Proposal, Add state or Discussion complete.
  - **Justification** Discussion items, design changes and the package card use it. Source: Supervisor input.
- V34 add component: [Footnote Marker](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=36-1389)
  - **Description** The numbered mark that ties a sentence to its gap note.
  - **Justification** Gap footnotes use it. Source: Supervisor input.
- V35 add component: [Review Top Bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=38-2)
  - **Description** The review page header: the page's title, an optional subtitle, and the change and state filters.
  - **Justification** Every review page state shares it. Source: Supervisor input.
- V36 add component: [Discussion Header](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=38-40)
  - **Description** A discussion item's ID, kind, title and state.
  - **Justification** Each discussion item opens with it, collapsed or expanded. Source: Supervisor input.
- V37 add component: [Item Header](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=38-46)
  - **Description** A spec item's or design change's marker and ID, with its kind and linked frame when it has them.
  - **Justification** Each item card opens with it. Source: Supervisor input.
- V38 add component: [Gap Note](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=38-52)
  - **Description** A gap footnote's number and its placeholder.
  - **Justification** Items resting on an open gap list their notes with it. Source: Supervisor input.
- V39 add component: [Document Row](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=38-57)
  - **Description** A file in the Documents list, with its change and how many of its items changed.
  - **Justification** The Documents list is made of these. Source: Supervisor input.
- V40 add component: [Rule Row](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=38-61)
  - **Description** A numbered rule or numbered change, marked when added or removed.
  - **Justification** Spec items' rules and design changes' numbered changes use it. Source: Supervisor input.

## Assumptions and TODOs

- The SKAI file now has a `Design System` page (conventions, colours in light and dark, text styles, spacing) and an empty `Components` page; the components wait on the change page until promotion.
- The screens are drawn from the running page at 1440 × 900, with its spacing rounded to the design scale. A page that scrolls is one screen, as tall as its content.
- Animation, hover feedback on whole screens, and the highlight flash after Enter in search aren't drawn; the components carry the hover looks.
- The page is drawn with SKAI's demo map because it exercises every part of the page: domains, reused scenes, a TODO scene, modal styles, notes, a route note and implements.
- Where the stylesheet breaks SKAI's design rules, the designs come as close to it as the rules allow. For example, spacing, gap and corner values off the design scale (6, 7, 8, 9, 13, 14, 18, 22 and 28 px) round to the nearest step. Each such departure is a design change (supervisor input).
- TODO: update the viewer's stylesheet (`Bin/ui-map-viewer.v1.css`) to match the designs once they're approved, including the merged colours, the rounded opacities and the text sizes (V01 04). The designs lead and the stylesheet follows (supervisor input).
- The review pages take SKAI's design system in place of their own look: its fonts, colours and spacing replace the system font and the pages' own colours, with colours added where the system has none, such as for added and removed (supervisor input).
- TODO: update the review pages' stylesheet (`Bin/spec-review.v1.css`) to match the designs once they're approved (supervisor input).
- TODO: center the map in the area to the left of the open side panel in the viewer (`Bin/ui-map-viewer.v1.js`), and in the renderer's description of the page (rule 12 in `Bin/ui-map-render.py`). The viewer centers it in the whole window today (D04).
- TODO: remove the side panel's Specs section from the viewer (`Bin/ui-map-viewer.v1.js`) and from the renderer's description of the page (rule 12 in `Bin/ui-map-render.py`). The feature is dropped (D03).
- The inputs are SKAI's own code, so there are no requests to file. Where the designs and the inputs differ, the TODOs above carry the change. Those TODOs are the work this package leaves behind, and SKAI has no design specs to write for these pages.

## Out of scope

- The renderer's Mermaid and SVG outputs.
- A separate design specs review mockup. It shares the product specs review design (supervisor input).
- The change request versions of the review pages and the request review page.
- Change management on the UI Map page, which is the next package.
- Marking routes as phone-only or tablet-only (skai#67), which isn't built yet.

## Decision Log

- D01 decided — one desktop size, web, light and dark, sentence case, no UI kits; fonts Figma provides
- D02 decided — this backfill builds the Design System and Components pages
- D03 decided — no Specs section in the side panel; the feature is dropped from the viewer too
- D04 decided — with the side panel open, the map centers in the area left of the panel; the viewer is fixed to match
