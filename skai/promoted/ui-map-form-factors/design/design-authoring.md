# Design — UI Map Form Factors
[Review page](design-review.html)

## Goal

Let a reader of the UI Map page see the map for one form factor, and see which scenes and routes exist only on some form factors, for the form-factor marking in skai#67.

## Inputs

- Base: production in the [SKAI design file](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=0-1), including the UI Map designs promoted from `ui-map-chg-mgmt`.
- How a map marks form factors: [`ui-map-form-factors.md`](../../../../Guides/UIMap/ui-map-form-factors.md), and the form factors the renderer passes to the page in [`Bin/ui-map-render.py`](../../../../Bin/ui-map-render.py).
- The page today: [`Bin/ui-map-viewer.v2.js`](../../../../Bin/ui-map-viewer.v2.js), which shows a modal style that differs by form factor as one chip per form factor and shows nothing else about form factors.
- The issue: [skai#67](https://github.com/SwiftKickMobile/skai/issues/67).
- Sample content: SKAI's demo map, LumenNotes, from [`ui-map-demo.md`](../../../../Guides/UIMap/ui-map-demo.md), with made-up phone and tablet differences.
- Supervisor input:
  - A form-factor drop-down sits to the right of the domain filters and works like the hops drop-down. It appears only when the map declares two or more form factors. Its choices are All, the default, then each form factor.
  - The button is as wide as its longest choice, up to the width of the Changes toggle, and truncates a longer choice. The open menu is as wide as its longest choice.
  - With a form factor chosen, every scene, route and scene placement that doesn't exist on it is grayed out the way search grays the scenes that don't match, whatever else is selected, filtered or searched. Grayed-out items don't respond to clicks. Connectors stay at full strength, and a grayed-out reused scene looks like any other grayed-out scene, keeping its reuse arrow.
  - The side panel lists a scene's form factors when it declares them, and a marked route's form factors beside that route. It keeps every form factor's modal style whatever is chosen.
  - A scene that declares form factors gets an icon on its box, as notes and modal styles do. A scene on every form factor gets none. A route label gets the same icon when a route in its box has form factors of its own.
  - A scene that exists on the chosen form factor stays as it is. When the route it's drawn in full under isn't used there but another route into it is, the two swap: the scene is drawn in full under the used route and the other becomes a grayed reused scene. The boxes don't move; only the scene's connectors start from its full drawing.
  - How to read this map gains a line for the drop-down.

## Discussion

The supervisor's input settled the designs; review them in the mockups on the `ui-map-form-factors` change page.

## Design Changes

### UI Map

- V01 add state: [ui map — form factors](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16661)
  - **01** A form-factor drop-down sits to the right of the domain filters, showing All by default. It appears only when the map declares two or more form factors. It's as wide as its longest choice, up to the width of the Changes toggle, and cuts off a longer choice.
    - **Justification** A reader can pick one form factor without losing the domain filters or search. Source: Supervisor input.
  - **02** A scene that exists on only some form factors shows the form-factor icon beside its other icons. A scene on every form factor shows none.
    - **Justification** A reader can see which scenes are limited without choosing a form factor. Source: Supervisor input.
  - **03** A route label shows the form-factor icon when a route in its box is used on only some form factors, after any note icon.
    - **Justification** A reader can see which routes differ by form factor without choosing one, and the side panel names them. Source: Supervisor input.
- V02 add state: [ui map — form factor menu](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16708)
  - **Description** Opening the form-factor drop-down lists All, then each form factor the map declares, with the current one checked. The menu is as wide as its longest choice.
  - **Justification** It works like the hops drop-down, which readers already know. Source: Supervisor input.
- V03 add state: [ui map — phone](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16711)
  - **Description** With a form factor chosen, a scene that doesn't exist on it is grayed out the way search grays the scenes that don't match, and so is a route that isn't used there: its box and label, and a reused scene inside it. Connectors stay at full strength. A grayed-out reused scene loses its lighter look and grays like any other scene, keeping its reuse arrow. Grayed-out scenes don't respond to clicks. On a phone, the tablet-only route that puts the note beside the notes list and the tablet-only outline are grayed out.
  - **Justification** A reader sees one form factor's map in place, without the layout shifting. Source: Supervisor input.
- V17 add state: [ui map — tablet](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16758)
  - **Description** When the chosen form factor doesn't use the route a scene is drawn in full under, but uses another route into it, the two swap: the scene is drawn in full under the route that's used, and the other becomes a grayed reused scene. Nothing moves; the scene's own routes start from its full drawing. On a tablet, the note is drawn in full beside the notes list, and the phone push route with its reused note is grayed out.
  - **Justification** A scene that exists on the chosen form factor reads as reached, by the route actually used there. Source: Supervisor input.
- V04 add state: [ui map — tablet scene selected](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16805)
  - **01** Graying out stays on while a scene is selected and the map shows only its connections: with Tablet chosen and the notes list selected, the phone-only push route and its reused note are grayed out, and the note is drawn in full beside the notes list.
    - **Justification** The choice applies whatever else is selected, filtered or searched. Source: Supervisor input.
  - **02** In the side panel, a route that exists on only some form factors names them beside it. The panel lists every route whatever form factor is chosen.
    - **Justification** The side panel spells out what the map marks. Source: Supervisor input.
- V05 add state: [ui map — form factors scene selected](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16832)
  - **Description** Selecting a scene that exists on only some form factors adds a Form factors section to the side panel, headed by the form-factor icon, with a chip for each form factor.
  - **Justification** The side panel spells out what the scene's icon marks, as it does for notes and modal styles. Source: Supervisor input.
- V14 add state: [ui map — modal style scene selected](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16852)
  - **Description** Selecting a scene with a modal style shows a Modal style section in the side panel, headed by the modal icon, with a chip naming the style. When the style differs by form factor, there's one chip per form factor, naming the form factor and its style.
  - **Justification** The page already shows this section, but no design did; it's drawn here so the Form factors section can be checked against it. Source: Supervisor input.
- V15 add state: [ui map — modal style scene selected without form factors](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16873)
  - **Description** On a map without form factors, the Modal style section has one chip naming the style, and the top bar has no form-factor drop-down.
  - **Justification** Most maps have one form factor, so this is how the section usually looks. Source: Supervisor input.
- V06 add state: [ui map — form factors help](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-16893)
  - **Description** How to read this map gains a row for the form-factor icon after the modal style icon and one for a route label with it after the route note row, and its instructions say that choosing a form factor in the top bar grays out what doesn't exist on it.
  - **Justification** The help explains every mark on a scene and every control in the top bar. Source: Supervisor input.

### Components

- V07 modify component: [Icon](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13049)
  - **Description** Icon gains a Form Factor type: a tablet and a phone side by side.
  - **Justification** A scene that exists on only some form factors needs a mark, and its side panel section a heading icon. Source: Supervisor input.
- V08 modify component: [Scene Cell](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13066)
  - **Description** Scene Cell gains a Show Form Factor option that shows the form-factor icon after the modal style icon. It's off by default.
  - **Justification** Any kind and state of scene can exist on only some form factors. Source: Supervisor input.
- V09 modify component: [Panel Row](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13249)
  - **Description** Panel Row gains an optional label before reused, naming the route's form factors in muted text. It's off by default.
  - **Justification** The side panel shows which form factors a route is used on. Source: Supervisor input.
- V10 modify component: [Top Bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13192)
  - **Description** Top Bar gains a Show Form Factor option that puts the form-factor drop-down after the domain filters. It's off by default.
  - **Justification** The production map's top bar holds the drop-down. Source: Supervisor input.
- V11 modify component: [Change Top Bar](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13208)
  - **Description** The Map tab of Change Top Bar gains the same Show Form Factor option, putting the drop-down between the domain filters and Changes.
  - **Justification** A change package's map page filters by form factor too. Source: Supervisor input.
- V12 add component: [Form Factor](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13264)
  - **Description** The drop-down's button: the current choice and a chevron, in the hops drop-down's style. A choice too long for the width cap is cut off with an ellipsis.
  - **Justification** The top bar needs a control for choosing a form factor. Source: Supervisor input.
- V13 add component: [Form Factor Menu](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13268)
  - **Description** The drop-down's open menu, in the hops menu's style: All, then each form factor, the current one checked.
  - **Justification** The drop-down needs its list of choices. Source: Supervisor input.
- V16 modify component: [Route Label](https://www.figma.com/design/YiKIvXCvCu8XyS149IT3hS/SKAI?node-id=177-13179)
  - **Description** Route Label gains a Show Form Factor option that shows the form-factor icon after the note icon. It's off by default.
  - **Justification** A route label marks routes used on only some form factors. Source: Supervisor input.

## Assumptions and TODOs

- The sample is made up: on a tablet the note opens beside the notes list instead of being pushed, a tablet-only outline sits beside the editor, and the tag picker opens as a sheet on a phone and as a popover on a tablet.
- Graying out applies to the map. The side panel always lists every route and the full modal style for each form factor.
- The outline opens nothing, so its side panel is drawn without an Opens section; the page today shows Opens with nothing under it.
- On a change package's page with six domains, the form-factor drop-down leaves almost no room in the top bar, and with the hops drop-down showing as well it overflows.
- The page's code is built: `Bin/ui-map-viewer.v2.js` and `.css` carry the drop-down, the graying out, the swap to the route that's used, the scene and route label icons, the side panel's Form factors section and route labels, and the help rows and sentence; `Bin/ui-map-render.py` describes them, and the demo map in `Guides/UIMap/ui-map-demo.md` has phone and tablet differences.
- The components on the change page are drafts copied from production; promotion replaces their production versions.
- The inputs are SKAI's own guides and code, and no decision changed them: the map format and renderer already carried what the page needs, and the page's code is built. There are no requests to file and no design specs to write.

## Out of scope

- Writing the code. It follows the design, as the rest of skai#67's viewer work.

## Decision Log
