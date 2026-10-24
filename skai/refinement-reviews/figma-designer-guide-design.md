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

