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

The two guides together are capped at **17,500 bytes** (`wc -c`, managed headers included). That is
in line with `Guides/Requirements/requirements-catalog.md`, which plays the same role (content rules)
for requirements. Every repair states its net size cost; additions over the cap are paired with
trims, and a fix that cannot fit is a supervisor decision.

## Boundaries

The guides do not cover the UI Map (`Guides/UIMap/`), requirements, the code's implementation of the
design system, or the Figma MCP's own documentation. They are conventions, not a workflow: design
authoring and promotion are tool-agnostic process guides that assume every design tool has named
pages and read this guide only for the conventions drafts must meet.

Addendum 2026-10-12: the guide records file conventions only. How colours (including Dark values)
are chosen is the designer's methodology and no concern of the guide.
