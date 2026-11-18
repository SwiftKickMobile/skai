# Figma Designer Guide Design

## Purpose

This document is the standard for SKAI's Figma designer guides: what they are for, what they must
and must not contain, and the decisions behind them. It is used to write and cold-review them; it is
not something a designer or operator reads at runtime.

- [`Guides/Design/figma-designer-guide.md`](../../Guides/Design/figma-designer-guide.md) — the
  conventions every Figma design file follows.
- [`Guides/Design/figma-designer-guide-multiple-sizes.md`](../../Guides/Design/figma-designer-guide-multiple-sizes.md)
  — the extra conventions for a file with more than one target size.

The guides set the conventions for a project's Figma design file, the design source of truth for the
app. They apply to anyone editing the file, designer or agent. A file that follows them can be read
by a developer or agent who has never seen it: they know where the current design of a screen is,
which values are tokens, and what each page holds.

Written 2026-10-10 and revised 2026-10-11 (platform-agnostic scope, Figma naming, linked
multiple-sizes guide).

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md), especially Guide house style.
- The guides are not a gated workflow; they are conventions plus agent practices.

## Requirements

1. **Platform-agnostic.** The guides hold for any front-end platform, web included. They name no
   device, OS, platform UI, or screen size; those are the designer's choices, recorded in the file's
   `Conventions` frame. A web designer should find nothing foreign in them. Examples use LumenNotes,
   SKAI's fictional theme.
2. **No implementation details.** Designs describe what the product shows. The guides never mention
   how an app is or was built (layout files, asset formats of a legacy codebase, frameworks).
3. **Figma-specific by name.** The guides are Figma's; another design tool gets its own guides. A
   tool-agnostic layer is extracted only if a second tool arrives.
4. **Single-size files carry no extra rules.** Most apps design for one target size. Rules that only
   matter with several live in the linked multiple-sizes guide; the core guide links to it only
   where a core rule changes.
5. **Rules, not a log.** Each rule states a convention or a practice that holds across projects. The
   guides do not record individual mistakes from one session or project. Agent tooling lists only
   reusable practices that change what an agent does on most files.
6. **Block, don't work around.** When an agent lacks something it needs (a font that won't load), it
   stops and asks; the guides never describe a workaround.
7. **Plain language.** Name things by what's on screen; define terms; numbered rules with a bold
   lead sentence.

## Settled decisions

- Three main pages (`Production`, `Components`, `Design System`); `Production` is canonical; a
  change page per change package (its lifecycle belongs to the design process guides, not here);
  no archive (Figma's version history holds superseded designs); a feature behind a switch is an
  ordinary state, named for what it shows; every top-level node is a Section.
- `Conventions` records the designer's choices: target sizes (orientation included), platforms and
  the one whose look screens use, dark mode, button case, UI kits and what each supplies.
- Screen states are chosen for the screen; control states live in component sets; changes inside a
  component itself live in its `<Component> Reference` frame. An overlay the screen presents
  (dialog, popover, sheet), even one a component opens, is a screen state.
- One design serves every platform: screens use the primary platform's look, and a `Platforms`
  Section shows once how shared chrome differs on other platforms or OS versions.
- Kit components are used linked, wrapped in a local component to customize, never redrawn.
- Colors are variables (no color styles); opacity on the layer; text uses text styles.
- Dimensions: spacing and radii on one scale (1–4, then steps of 5; from 30 up, steps of 10
  preferred, 5 allowed). Variables are named for their value (`spacing/20`, `radius/full`,
  `type/17`), defined only when used, in a `Dimensions` collection. No semantic tier (`inset/screen`)
  — the taxonomy stays lean even where that means small departures from the app. The code mirrors
  the names.
- Multiple target sizes: a `Dimensions` mode per target size; adaptive values in a `-adapt` group
  (`spacing-adapt/20`), defined only when a design needs one; screens are components on `Production`
  with instances on a page per further target size; screens have no variants; a differing layout is
  assembled from shared parts; app chrome switches through a `target` variable.
- Backfilling: draw what the product shows, not how it is built; draw the intended design, not the
  app's defects, and log them; snap values to the conventions and record the departures.

## Size budget

The two guides together are capped at **19,000 bytes** (`wc -c`, managed headers included; raised
2026-10-12 from 17,500 when SKAI Release 11's mandatory Project addendum footer, about 750 bytes
per guide, was added). That is
in line with `Guides/ProductSpecs/product-specs-catalog.md`, which plays the same role (content rules)
for product specs. Every repair states its net size cost; additions over the cap are paired with
trims, and a fix that cannot fit is a supervisor decision.

## Boundaries

The guides do not cover the UI Map (`Guides/UIMap/`), product specs, the code's implementation of the
design system, or the Figma MCP's own documentation. They are conventions, not a workflow: design
authoring and promotion are tool-agnostic process guides that assume every design tool has named
pages and read this guide only for the conventions drafts must meet.

Addendum 2026-10-12: the guide records file conventions only. How colours (including Dark values)
are chosen is the designer's methodology and no concern of the guide.

## Amendment — 2026-10-21 (known gaps on change pages)

Requirement 8, from the known-gaps decision G01 (skai#82): **the change page mirrors each open design
gap.** The design package's artifact is the source: a design gap is an open Discussion item whose
**Gap** line names the drawn state that stands as the placeholder. The guide states the mirror and
nothing more: one Dev Mode annotation per open gap, on the node that draws the placeholder; its text
the gap line as the artifact writes it (`D<n> — <placeholder>`); added once the item has its Gap line
and the placeholder is drawn, updated when the placeholder changes, removed when the item closes;
never on `Production`; written through the Plugin API's node `annotations` (the Figma connector has
no comment tool), keeping the node's other annotations. Annotations show on the canvas outside Dev
Mode too (tested 2026-10-20). This is the one change-page convention the guide owns; the design
process guides say only to mirror each open gap as this guide says. After the compression review (754 drafted, 512 proposed, 599
applied) the pair is 17,292 bytes; cap **17,300 bytes**, set by the supervisor 2026-10-21, replacing the 19,000 above.

## Amendment — 2026-10-23 (request sections)

Requirement 9, from the change-request decision (skai#99; `design-process-design.md` § Amendment —
2026-10-23): a change request against a change package draws in a Section of its own on that
package's change page, `CR-<nnn> — <name>`, holding only the frames the request adds or changes,
a changed screen as a copy of the package's frame with the change; promotion folds them into the
page's other Sections and removes it. One passage under the page rules; nothing else. Cap set
after the compression review (17,300 before it).
Compression (third round, 2026-10-23): the pair 17,492 bytes; cap set at 17,400 by the
supervisor 2026-10-23, then held at **17,500 bytes** (supervisor, 2026-10-23) after the
refinement series found nothing against the passage: trimming elsewhere would have been cleanup.

## Amendment — 2026-10-23 (page organization for change pages)

Inventory per skai#90 (inventory before prose; sweep; compression; cap after). Decided with the
supervisor 2026-10-23 after the Offers dry run; the Offers Concept A page is the worked case.
Requirement 10, in the screen-page rules:

1. Change pages and request sections group **one section per screen**, named for the screen in
   plain words, its states stacked below it; a tall screen spills into a second column beside
   it (Production already does this; the guide never said so — supervisor, 2026-10-23: keep it).
   `Production` groups by feature area, screens as columns; promotion regroups in general (the
   process guide says when, this guide says where).
2. A change page holds a `Components` section for the components a mockup needs; replaces the
   loose allowance in Screen pages 7 and Components 1.
3. A request draws in one section of its own on the base's page, `CR-<nnn> — <name>`, holding
   the same per-screen sections (Pages 1 reworded).
4. One concept per page: the concept letter is in the page name; frames and sections carry no
   prefix.
5. A **structure check**: one line under Agent tooling naming `Bin/figma-page-check.js`, run
   through the tool, as the check of the rules above; what it reports is the script's header's to
   say; the process guides say when (before the Review gate; promotion's `C1`).
Page-organization amendment, 2026-10-23: the pair 17,966 bytes after compression; cap
**17,900 bytes**, set by the supervisor 2026-10-23 (combined caps cut 100 under the proposal),
replacing the 17,500 above.

## Amendment — 2026-10-23 (gap annotation format)

Requirement 11, replacing requirement 8's text format (supervisor, 2026-10-23: the annotation did
not even say "gap"; terminology stays the guides' own): the annotation on the node that draws a
placeholder reads, on three lines, `Gap: <the question>`, `Placeholder: <what is drawn>`,
`Owner: <the item that owns the question — product specs D21, or this package's D04>`. One
per frame that stands on the placeholder; added once the frame exists, updated when the
placeholder changes, removed when the owning item closes; `Production` never carries one. The
rest of § Gaps (Plugin API `annotations`, keep other annotations) stands. The design gap's
definition moves: an inherited gap is a footnote on the change list entry, a design's own gap an
item (`design-process-design.md` § Amendment — 2026-10-23, inherited gaps).
Gap annotation change, 2026-10-23: the pair 17,897 bytes after compression; cap **17,850 bytes**,
set by the supervisor 2026-10-23, replacing the 17,900 above.


## Amendment — 2026-10-28 (gap annotations: category, ID first, once per gap)

Requirement 12, replacing requirement 11's text and placement (supervisor, 2026-10-28, after the
Offers CR-001 review with Mofe: the same gap repeated on every frame was overwhelming, and the
annotations did not use what Figma offers for telling kinds of notes apart). Inventory:

1. A gap annotation is in the file's annotation category named `Gap`, colored yellow; the agent
   creates the category when the file has none (Plugin API `figma.annotations`
   `getAnnotationCategoriesAsync` / `addAnnotationCategoryAsync`, the annotation's `categoryId`).
2. Its text, on three lines: `<owning item ID>: <the question>`, then
   `Placeholder: <what is drawn>`, then `Owner: <path of the owning artifact relative to
   skai/changes, starting with the change package's folder>` (for example
   `offers/product-specs/product-specs-authoring.md`).
3. Each gap is annotated once in the package's section: on the placeholder node of the first frame,
   in canvas order, that draws it. A later frame drawing the same placeholder carries none. When the
   first occurrence changes (a frame added, moved or removed), the annotation moves with it.
4. Unchanged: added once the frame exists, updated when the placeholder changes, removed when the
   owning item closes; `Production` never carries one; other annotations on the node are kept.
Compression (Astra, 2026-10-28): the pair 18,037 bytes; cap **18,000 bytes**, set by the supervisor
2026-10-28, replacing the 17,850 above; the installed text trimmed to fit.
Ruling (supervisor, 2026-10-28, series GA round 2's logged finding): canvas order runs down a
column, then across columns; stated once in the Canvas layout ordering rule, which § Gaps relies on.

## Amendment — 2026-11-11: Owner Paths, Request Sections, Mirrors (skai#118)

Recorded during the refinement pass for skai#118 (`design-process-design.md` § Amendment — 2026-11-11).

1. **Owner-path updates** (§ Gaps): a gap annotation's `Owner:` line is updated when the owning artifact's path changes, as when promotion archives a request whose gap stays open where it was raised.
2. **Mirror** (§ Gaps): the gap annotation is the design file's mirror of a gap, the word the design process guides use for it.
3. **Request Sections** (§ Pages): a request's Section is named `CR-<nnn> — <name>`, `<nnn>` its number path from the package: `001-002` for request 002 against request 001, the same name a fold gives it when it re-files the request as `001-002`, so no rename and no two Sections share a name (corrected after cold round 1); promotion folds a request's frames into its base's Sections (a package's, or its base request's); a request against a request gets its own Section on the page holding its base's drafts, never inside its base's Section, so deleting that Section at promotion leaves the open request's drafts.

4. **One mirror per change page and per request Section** (§ Gaps; supersedes § Amendment — 2026-10-28 item 3's "once in the package's section"): each change page and each request Section that draws a gap carries one mirror, on the first frame in canvas order drawing it; a page's count excludes its request Sections, so a request that copies a frame carrying a base gap mirrors it in its own Section. First-frame placement and "a later frame carries none" stand (recorded after cold round 4).
5. **Frame names** (§ Frames rule 5): frame names are unique per page, with one exception: a request's copy of a base frame keeps the base frame's name, which the process guides use to match a change to its frame; any other copy is renamed (recorded after cold round 4).

Cap (supervisor, 2026-11-11): the pair **18,100 bytes** (was 18,000; 17,997 before this pass). Compression round skipped: clause additions in place.

## Amendment — 2026-11-11: Requests As Folders Of Sub-Packages; Confirming The Route (skai#108, skai#129)

Adopts [`change-requests-design.md`](change-requests-design.md) § Amendment — 2026-11-11: this standard's guides say the items that amendment lists for their kind of guide (artifacts, authoring, promotion, Figma), and every request path, ID and provenance tag in them takes the new form. Caps for this change: `change-requests-design.md` § Amendment — 2026-11-11 (supervisor, 2026-11-11).

## Amendment — 2026-11-11: Container Sections, Backups, Scratch (skai#111, skai#100)

Rulings: skai#111 and skai#100 (supervisor, 2026-11-11; the B1 plan's Q2, Q3, Q10–Q12; the 2026-10-29 page-layout comment on skai#111). Inventory per skai#90, before prose.

1. **Container Section on change pages.** A change page's per-screen Sections sit inside one Section named for the package; request Sections and scratch Sections sit beside it at the page's top level. `Production` keeps its feature areas with no container.
2. **Backup of the base.** Before a fold changes a package's drawings, a copy of its container Section, `Base — Pre CR-<id>`, gap annotations stripped, stacks under the request Section, left edges aligned, 100 apart. A backup of `Production` goes on a separate page, `Production — Pre <change-id>`, since `Production` holds only approved designs. The supervisor deletes backups.
3. **Scratch Section**: `Scratch — <topic>`, at the page's top level, for whatever exploration the supervisor wants; outside the structure check; no gap mirrors.
4. **Unique names** allow the copies a backup or scratch holds, as a request's copies.
5. **Structure check** (`figma-page-check.js`): one level of nesting in a change page's container Section and backup, as in a request Section; scratch Sections skipped; a backup's stacked placement allowed.

**Cap (supervisor, 2026-11-11, after the proposal review and compression):** the pair **18,820** (compressed 18,860).

**Ruling (supervisor, 2026-11-11, after cold round 1):** a fold into production backs up every page it changes (`Production`, a target-size page, `Components`) as its own page, `<page> — Pre <change-id>`, so a Base review restore puts each back. Supersedes item 2's single `Production — Pre <change-id>` page.

## Amendment — 2026-11-17: How Designs Are Drawn (skai#72, skai#74, skai#107, skai#110, skai#112, skai#113, skai#126, skai#148)

The tool guide's half of one amendment for a whole stream of changes; the process half and the overall picture are [`design-process-design.md`](design-process-design.md) § Amendment — 2026-11-17. Written before any guide text so each guide is rewritten once: `figma-designer-guide.md` in its own refinement pass, then `figma-designer-guide-multiple-sizes.md` in another. Sources: the tickets above; the practices and failures recorded from a full design backfill (the comments on skai#110, skai#126 and skai#72); supervisor rulings of 2026-10-22, 2026-11-16 and 2026-11-17, cited where they apply.

**Supersedes:**

- § Settled decisions, the color and style names (item 3). "The code mirrors the names" keeps its meaning.
- § Settled decisions, "Kit components are used linked, wrapped in a local component to customize, never redrawn": a detached copy is allowed where the kit cannot do what is needed (item 6). Linked, then wrapped, stays the order of preference, and nothing is redrawn.
- Requirement 5's test for an Agent tooling item (item 12).
- § Amendment — 2026-11-11 (Container Sections, Backups, Scratch), item 2's "The supervisor deletes backups" (item 9).
- § Size budget's single cap for the pair (Caps, below).

**figma-designer-guide.md must say:**

*`Conventions` first (skai#74)*

1. Read `Conventions` before reading or editing anything else in the file. What it records wins over the guide's examples and defaults: a size name in one of the guide's examples does not replace a project's own. `Conventions` holds decisions; notes on how the file is built do not belong there.
   `Conventions` records the designer's choices only, and no exception to a rule of the guide (supervisor, 2026-11-17). The guide does not say where an exception goes: every guide's project addendum already serves, and a guide never names a use of its addendum.

*What earns a frame (skai#107, skai#113; supervisor, 2026-10-22 and 2026-11-16)*

2. Screen pages rules 2 and 4 are reconciled. The `Global` Section's designs are read before drawing. A state a `Global` design covers (error, loading, empty, offline) is not a state of every screen: a screen draws it only where it departs from the `Global` design. A screen gets another frame only when its layout changes. Text that varies (a label's value, a status word) and a button that is absent do not need frames of their own. The guide gives one example that needs a frame and one that does not. An edge case is drawn once, on the frame that is about it; frames showing the main case do not also show it. "Sample data that shows several things at once" stays, as long as the states shown could occur together. How the `Global` designs apply is written in the project's specs; no notes are added to the `Global` drawings for it.

*Names (skai#148; supervisor, 2026-11-17)*

3. Names in the file are readable Title Case: color variables (`Brand Blue`, `Muted Blue Light`, `Brand White`, `Always Brand White`), text and effect styles, components and their properties. The `Dimensions` collection keeps its names as they are (`spacing/20`, `radius/full`, `type/16`, `spacing-adapt/20`, `target`). Frame names (`notes — empty`) are unchanged. The file records no code names. The code's name for a thing is its name here put through the project's own naming convention, one to one; the guides give no code-side examples and do not say where a project writes its convention down. An agent that has to convert a name and does not know the convention stops and asks (requirement 6). In a backfill, a name is the app's own name for the thing, in Title Case. Every design and design-spec guide is swept for names in the old form and for code-side examples (`spacing20`, `spacing20adapt`), which go; on 2026-11-17 only the two Figma guides held any.

*Sample data (skai#113)*

4. Copy and sample data gains: content is plausible and representative of the product, and placeholder copy is not used (placeholder people stay obvious fakes); what a frame shows could occur together and follows the requirements; the same sample people and records agree across related frames and across target sizes.

*Components and kits (skai#110)*

5. Components and screens are built with auto layout, so their contents reposition themselves when content changes (a longer label, an added row). Items are not placed by hand at fixed positions where auto layout can arrange them. A component the app scales is drawn at scale 1 and scaled as an instance (the tooling item on scaling says why).
6. The kit rule gains: the local wrapper is also where what the kit lacks is added; where the kit cannot do what the app needs even wrapped, a detached copy is made a local component on `Components` and changed there (supervisor, 2026-11-17), in place of the rule's "never detached"; a kit look is reused whole (fill, blend mode, opacity, effects, variant properties), since copying its color alone does not reproduce it; kit measurements come from the kit's own examples; kit properties are set to match the app, and leftover placeholder text is removed.
7. On `Design System`, every variable and style has a swatch or specimen bound to it.

*Drafts of the design system (skai#126; supervisor, 2026-11-17)*

8. What a package's design system drafts are in the file:
   - A new or changed style or variable is a draft named `Draft/<package>/<name>`: `<package>` is the change page's name, followed by `/<request ID>` for a request. Figma shows the slashes as folders, so a package's drafts sit together in the panels. A draft variable sits in the collection of the one it replaces, with its modes.
   - A changed component is drafted as a copy in the package's `Components` Section, as a new one already is (Components rule 1), keeping its name. So are supporting copies, the few components copied only to show a changed one nested inside them.
   - A `Design System` Section inside the package's Section, beside `Components`, holds a swatch or specimen bound to each drafted style or variable. It is what the change list links and what review looks at.
   - Mockups bind the drafts. Production's styles, variables and components are never changed in place by a package: Pages rule 3 ("edited deliberately") now says how.
9. What each of promotion's steps is in Figma. The process guide owns the order and the cases; this guide says only what each thing is in the file.
   - **A backup** of a style or variable is a copy named `Backup/<package>/<name>`, made before the change is applied. A component's backup is a copy of the component or set, on `Components — Pre <change-id>` (or in the `Base — Pre …` Section for a base package). That backup page is built from copies of `Components`' Sections: a copy of the page itself turns every standalone component into an instance of the original, which is no backup (proven 2026-11-17; this also corrects the 2026-11-11 ruling's "as its own page" for `Components`). A run after a return to authoring replaces an earlier run's backups. A page backup stays bound to the file's styles, variables and components, so it shows their changes too; the "before" of a changed definition is its own backup.
   - **In place** means the existing style, variable or main component is edited, or renamed, and keeps its identity, so every binding and instance follows. It is not swapped for another object.
   - **A new** style or variable is a copy of the draft under its final name (into a base package: under that package's `Draft/` folder); a new component is a copy on `Components` (or in the base package's `Components` Section). The package's drafts stay as they are.
   - **A removed** style or variable is renamed into `Backup/<package>/`; a removed component moves to the page backup. Neither is deleted.
   - **Re-pointing** swaps each binding, instance or reference to a draft for the base's definition. After a swap, overrides are reset, and the component properties and overrides the screen needs are set again, since a reset leaves component property values as they were (proven 2026-11-17); on a target-size page, chrome content is set again (the multiple-sizes guide).
   - **Restoring** reverses each step in place. A style, variable or main component is not replaced by its backup copy: bindings and instances follow identity, so a swapped-in copy would leave them behind. A restored component is compared with its backup copy, variants and properties included.
   - **What a package leaves,** found by name: its change pages, its request Section, `Base — Pre …` Sections, `<page> — Pre <change-id>` pages, and everything under `Draft/<package>/` and `Backup/<package>/`, a request's being inside its package's. The guide names them and no longer says who deletes them; that is the process guide's.

   Each mechanism above is a claim about Figma. The pass proved them on a test file on 2026-11-17, a component's full round trip included (changed in place, then restored from its copy, with variants, properties, nested instances and overridden instances intact); the results are in [`figma-designer-guide-refinement.md`](figma-designer-guide-refinement.md). The one that failed, a page copy as a component backup, is corrected above.

*Purpose notes (skai#112; supervisor, 2026-11-17)*

10. Every screen frame in a package's or request's Sections carries one Dev Mode annotation on the frame itself, in the file's `Purpose` category: a category of its own, violet (supervisor, 2026-11-17, for now), apart from the yellow `Gap`, created when the file has none. The frame of a screen's main state says what the screen is, where a user meets it and what it is for. Every other frame of the screen, a crop included, says what it shows that the main state does not, whether or not the package draws the main state. A sentence or two in the product's words, with no IDs. Unlike a gap annotation it stays on the frame in `Production` and in a backup. At a further target size, a screen that only mirrors the base size carries no note of its own, and a screen with its own layout there says what differs; a mirror's note is found on the frame of the same name in the same Section of `Production` (supervisor, 2026-11-17).

*Agent tooling (the comments on skai#110, skai#126 and skai#72)*

11. The structure check reports two kinds of result, apart.
    - **Breaches,** to fix: a fill or stroke with no color variable; text with no text style; a text style whose font size binds no `Dimensions` variable; a padding, gap or corner radius with no `Dimensions` variable; a screen frame in a package's or request's Sections that should carry a `Purpose` note and has none. These check the app's own layers on screens and components: what sits inside a kit instance is the kit's, and an image fill or a zero value is no breach.
    - **Signals,** to look at and judge, since each may be fine as it is: text and frame layers outside any instance, counted per screen; the same fill, stroke or radius override repeated across instances of one component; a frame named like a kit component that is not an instance. A well-built file still has some: the backfill's finished file kept 47 loose text layers across about 80 screens.

    The script's header lists both and settles their details; its test under `internal/tests/tools/figma-page-check/` holds a passing and a failing case for each result.
12. Requirement 5's test for an Agent tooling item becomes: a reusable practice that changes what an agent does on most files, **or** a behavior of Figma or its plugin API that fails silently (no error, and a result that looks finished) while the agent follows a rule of these guides. Each such item carries its remedy. A failure the agent sees, and can work out, stays out. Candidates, each to be verified in the pass before it is stated:
    - *Instances:* resizing a layer inside an instance is ignored (use a variant, or top-level instances laid over the component); overriding an instance property with the value its main already has can stop the instance rendering (reset the override instead); hidden instance children are skipped unless the script turns that off; setting a property on a hidden nested instance un-hides it.
    - *Swaps and renames:* swapping a component carries over overrides whose layer names match (reset overrides, then restore only those the screen needs); renaming a variant property drops a variable bound to it on existing instances (bind again and check a sample instance); a cloned variant can lose its property links.
    - *Copies:* a layer cloned from another context keeps absolute positioning; a copy can differ from its original in explicit variable modes.
    - *Scripts:* a script that throws is rolled back whole, so a check inside a script throws when it fails, and a run that failed is checked for half-built results before a retry; a description is written whole, because what is read back is escaped; resizing an auto-layout frame turns hugging off on each axis the resize changes (restore it afterwards).
    - *Kits:* a translucent variable fill on a kit instance renders opaque (put a separate layer behind it).

    An item whose remedy the pass cannot establish is not stated. Proven 2026-11-17 (same record): every candidate above except four. Setting a property on a hidden nested instance did not un-hide it; and three were not tested and are not stated: an override equal to the main's value, explicit variable modes on a copy, and the kit fill.

**figma-designer-guide-multiple-sizes.md must say (skai#72 and its comment):**

13. Size names are the project's, from `Conventions`. The rules are written with placeholders (`Production (<size name>)`, a mode named for each target size), with one example clearly labeled as an example.
14. What must exist before what. This states what depends on what and sets no order of work for a designer: dimension variables are bound throughout the base size's screens before any screen of a second size is built; an adaptive value is created while building a screen whose layout really differs, and no earlier.
15. A second size is a full suite: every base frame mirrored into the same Sections in the same order, with no frame that exists only at the second size to repeat what another Section shows. The other orientation is drawn only for a screen with a custom layout at that size.
16. How a screen component is built so it stretches, and how chrome (the app's bars and navigation) switches:
    - Auto layout at the root. Chrome that belongs to the flow sits in it and hugs its content; the screen's content fills what is left. A column of top bar, content and bottom bar is one example; a screen with a persistent side panel arranges its root differently.
    - Whatever is pinned (a bar fixed to an edge, an overlay) is absolutely positioned with constraints, and chrome is drawn over content that scrolls under it.
    - After a screen is converted, every full-width descendant is set to fill; anything left fixed stays at the base width. Hugging works only on an instance whose main component is auto layout in every variant.
    - A piece of chrome whose kit component differs by size is a local wrapper with its `Target` property bound to `target`, even where the design looks the same at every size, since a kit component cannot bind the project's own values. A variant with no counterpart at another size is left unbound.
    - Values set inside a screen component on a nested instance are lost when the variable switches that instance's variant. Sample content therefore stays out of components that switch, and is set on the size page's instance.
17. A nested instance that shows at only one size is made transparent in the variant for each size where it does not show. The reason the field notes give, that setting a property on a hidden nested instance un-hides it, did not reproduce on 2026-11-17; the multiple-sizes pass tests this rule in a file with several sizes before the guide states it, and drops it if hiding works. Any other layer that shows at only one size binds its visibility to a `visible/<size name>` boolean variable in `Dimensions`. Instance children are never repositioned; content that must sit differently uses that variable or an adaptive spacing value.
18. An overlay that covers the screen at one size and floats over it at another is built from the host screen, a dimming layer, a card, and the overlay's content as a component of its own. This is stated for any platform; one platform's sheets, keyboards and navigation are examples at most.
19. Adaptive values step up the Dimensions scale, with none for 1–4. Font sizes follow the same pattern.
20. The same sample state is shown across sizes, and checked again at the larger size.
21. An image that needs a version for one size is named for that size. Where the app stretches the base image instead, the size page's instance carries the override and says so.
22. Promotion keeps every size's suite complete, frame for frame. The package's own mirrors (item 23) fold into the size pages as its base-size frames fold into `Production`. Beyond those, every frame the fold adds to the base size, a state or a crop included, gains its mirror on every size page; every frame it removes loses it; and a change to a screen with its own layout at a size is carried to that layout. Each size page the fold changes is backed up, as the 2026-11-11 ruling already says.
23. A change page in a file with several target sizes (supervisor, 2026-11-17). A package keeps all its drafts on its one change page. The page holds a Section for the package at each target size, side by side at the page's top level: the base size's is named for the package, and each further size's adds the size name, `<package> (<size name>)`, as the size pages are named. Each is set to its size's mode and holds the same per-screen Sections. A further size's Section mirrors every frame the package draws at the base size, as production's size pages mirror every frame, so a reviewer sees each change at each size. The `Components` and `Design System` Sections stay single, in the base size's Section. A request does the same with its own Section.

**Out of this amendment:** one platform's design choices (list separators, sheet recoloring, status bar variants) and a designer's own method, which the guides never hold; tool failures an agent sees happen; a semantic tier of names; a rule on effects; the workflow that uses these conventions, which is the process standard's. § Working a backfill keeps its three rules and gains none; how a backfill is carried out is documented separately, if at all (supervisor, 2026-11-17).

**Caps:** the pass on `figma-designer-guide-multiple-sizes.md` gives that guide a cap of its own, since it grows the most; until then it is held at its present 2,698 bytes. The other guides' caps are in the ruling below.

### Ruling — 2026-11-17: The Guide Is Broken Up

After the first review round the settled text of `figma-designer-guide.md` measured 23,607 bytes against 16,119, and the supervisor would not approve a cap for it: too much growth in a guide every design session reads. Two parts are read only by some sessions, so each becomes a linked guide, as the multiple-sizes guide already is (requirement 4's pattern, extended):

- [`figma-designer-guide-design-system-changes.md`](../../Guides/Design/figma-designer-guide-design-system-changes.md): items 8 and 9 above, and the silent failures of item 12 that arise only in that work (a swap, a renamed variant property, a cloned variant, a copied page). For a package that adds, changes, renames or removes a style, variable or component, and for promoting one. A package that draws its screens from what the file already has never reads it.
- [`figma-designer-guide-agent-tooling.md`](../../Guides/Design/figma-designer-guide-agent-tooling.md): the Agent tooling section, with the rest of item 12. For an agent editing the file through the Figma tool. A reader who only looks at the file, as the design spec guides' readers do, never reads it.

`figma-designer-guide.md` keeps everything else, and one passage on the structure check, since the process guides send every package to it. It links to each of the three guides where a reader needs it. Each linked guide is a managed guide with its own addendum footer.

| Guide | Measured after round 1's triage | Cap |
| --- | ---: | ---: |
| `figma-designer-guide.md` | 18,506 | 18,500 |
| `figma-designer-guide-design-system-changes.md` | 4,438 | 4,400 |
| `figma-designer-guide-agent-tooling.md` | 2,604 | 2,600 |

Caps: supervisor, 2026-11-17 (the split chosen from the measured sizes; each cap a little under its guide's). They replace the pair's 18,820 for these three; every repair states its net size against them.
