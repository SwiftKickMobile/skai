Managed-By: skai
Managed-Id: guide.designer-guide
Managed-Source: Guides/Design/figma-designer-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-27

# Figma Designer Guide

Print `📖 SKAI guide: figma-designer-guide` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Conventions for a project's Figma design file, the design source of truth for the app, for anyone
editing it, designer or agent. They hold across platforms. Examples use **LumenNotes**,
skai's fictional theme.

Designs are upstream of the UI Map, so Sections and frame names need not match its domains or
scenes.

An agent editing through the Figma tool reads
[Agent tooling](figma-designer-guide-agent-tooling.md).

## Pages

1. **Every file has three main pages.**
   - `Production` — the official production designs.
   - `Components` — the component library.
   - `Design System` — variables, text styles, and the app's
     [design conventions](#design-conventions).

   A change page, named for its change package, holds its drafts until they reach `Production`:
   per-screen Sections and any `Components` and
   `Design System` Sections inside a Section named for the package (for several form factors: [Multiple form factors](figma-designer-guide-form-factors.md)). A request uses a `<request ID> — <name>`
   Section (`CR-01`, or `CR-01-01` against `CR-01`), never inside another Section, on its base's draft page (a change page when the base is production), holding per-screen Sections for its added or changed
   screens, a changed screen as a copy, and `Components` and `Design System` Sections when it needs them. Promotion backs up the base, then copies them into its
   Sections: the base's package or request Section copied as `Base — Pre CR-01`, gap annotations
   stripped, 100px under the request Section, left-aligned; into production, each page the fold
   changes (`Production`, `Components`, a form factor page) as `<page> — Pre <change-id>`. A top-level
   `Scratch — <topic>` Section holds exploration.

2. **Production is canonical.** `Production` holds the approved design of every screen (plus a page
   per further form factor; see [Multiple form factors](figma-designer-guide-form-factors.md)).
   There is no other place to look for the current design.

3. **Components and Design System are edited deliberately**, never as a side effect of screen work.
   For a package that adds, changes, renames or removes a style, variable or component, and for
   its promotion, read [Design system changes](figma-designer-guide-design-system-changes.md).

4. **Older pages are read-only.** Pages from before `Production` existed are a historical record and
   are never edited.

## Design conventions

**Read `Conventions` before reading or editing anything else in the file.** It is a frame on
`Design System` that records the choices that differ between apps. The designer makes them; the
guide does not. Its decisions override this guide's examples and defaults, including form factor names. It holds only decisions; build notes and exceptions to
this guide's rules stay out.

- **Form factors** — what the app is designed at, each with a name, a definition and a default
  frame size. Its definition says what the name stands for. Some the app supports may be deferred.
- **Platforms** — the platforms the design serves, and the one whose look the screens are drawn in.
- **Dark mode** — whether the app supports it, and so whether colors have a `Dark` mode.
- **Button label case** — Title Case or sentence case.
- **UI kits** — the kit libraries the file subscribes to, with their versions and what each supplies.

## Canvas layout

### All pages

1. **Every top-level node is a Section.** Nothing sits loose on the canvas. Each Section is named
   for what it holds; the designer chooses the groups.

2. **Sections share one look.** Sections are filled #FAFAFA, lighter than the canvas, so white
   content stands out. A Section fits its content with 50px padding; Sections sit 100px apart with
   their tops aligned, but for a backup stacked under its request.

3. **Each page type fills its Sections differently**, as below.

| Page | Sections are | Inside a Section |
| --- | --- | --- |
| `Production` (and its form factor pages) | Feature areas | Screens |
| Change pages | The package's Section; request, backup and scratch Sections | Package, request and backup Sections: one Section per screen, named for it plainly, `Components` and `Design System` |
| `Components` | Component families (`Controls`, `Icons`, `Images`) | Component sets, components, and reference frames |
| `Design System` | Foundation topics (`Conventions`, `Colors`, `Text Styles`, `Dimensions`) | Documentation frames |
| Asset pages (an app icon page) | Asset groups | Frames set up for export |

### Screen pages

`Production` and its form factor pages, and change pages.

1. **Screens go right, states go down.** Within a Section each distinct screen is its own column, in
   the order a user meets them (notebooks → notes → note editor). A screen's states, and crops of
   them, stack below it; a tall screen spills into a second column beside it. Columns are 50px
   apart; states are 100px apart. Canvas order runs down a column, then across columns. Names
   carry no concept prefix.

2. **A screen's states are the situations it is naturally in:** its main use, a mode, a lifecycle
   point. A screen gets another frame only when its layout changes. Text that varies (a label's value, a status word) and a
   button that is absent do not need frames of their own. ❌ `note editor — shared`, the same
   editor with a "Shared" label. ✅ `notes — selecting`, the list with checkboxes and a toolbar. A state the
   `Global` Section already draws (rule 4) is drawn on a screen only where the screen departs from
   it. Draw each edge case once, on its frame; leave it off frames showing the main case. A control's own states (pressed, selected, disabled) live in its component
   set, and changes inside a component (a slider's value bubble) live in its reference frame;
   neither gets a screen of its own. Pick sample data that shows several things at once (a pinned,
   a shared, and an untitled note), as long as they could occur together.

3. **States are in rough order of importance.** The main case comes first; edge cases and empty
   states come last.

4. **App-wide behaviors are drawn once.** A `Global` Section holds one example of each behavior the
   whole app shares — error banner, toasts, empty state, error state, loading — each over a
   representative host screen. Read it before drawing. How these apply to a screen is written in
   the project's specs; no notes are added to the drawings for it.

5. **Platform differences are drawn once.** Screens are drawn in the look of the platform
   `Conventions` names. A `Platforms` Section shows, once, how shared chrome (navigation, tab bar,
   dialogs) looks on each other platform or OS version the app serves, rather than repeating screens.

6. **Overlays are drawn over their host screen.** Dialogs, menus, popovers, and sheets are states of
   the screen beneath them, so the audience has context. Where a kit supplies one, its look is the
   kit's (rule 6 under Components).

7. **Only screens or crops inside a screen Section** (frames, components, or instances); a
   package, request or backup Section holds screen Sections, a `Components` Section components, a
   `Design System` Section swatches and specimens;
   a scratch Section holds anything and is not checked.

### Components page

1. **One Section per component family.** Related components share a Section (`Controls` for buttons,
   fields, and rows; `Icons`; `Images`).

2. **Complex components get a reference frame.** When variants alone don't show a component's
   behavior, a `<Component> Reference` frame (`Formatting Bar Reference`) in its Section shows the
   interactions, visual rules, and a legend, built from instances with short captions. Behavioral
   rules stay in the requirements.

3. **Component sets stack down.** Within a Section, component sets and standalone components stack
   vertically, 100px apart, in rough order of how basic they are (buttons before the rows that use
   them).

### Design System page

1. **One Section per foundation topic.** `Conventions`, `Colors`, `Text Styles`, and `Dimensions`
   at least.

2. **Every variable and style is documented, from itself.** Each has a swatch or specimen
   binding it: a swatch binds its color variable, a type specimen uses its text style. The page updates
   with its foundations.

### Asset pages

1. **Frames are set up for export.** Each exported asset is a frame at its export size, with its
   export settings, named for the file it produces.

## Frames

1. **Form factor size by default.** A screen frame is its form factor's frame size from
   `Conventions`. Further form factors follow [Multiple form factors](figma-designer-guide-form-factors.md).

2. **A smaller layout is a state.** When a screen's layout changes below its form factor's default frame width, name
   the state for its width.

3. **Taller to show scrolling content.** When the whole screen scrolls, make the frame tall enough
   to show representative content. A region that scrolls inside a fixed layout does not change the
   frame.

4. **Shorter to show one thing.** When a state changes only one element, crop the frame to just
   enough of the screen to show that element in context.

5. **Unique names.** Screen frames are named `screen — state` in lowercase with a spaced em dash:
   `notes — empty`, `note editor — date picker`. No suffix means the default state. Frame names are
   unique per page, except copies in a request, backup or scratch Section and frames in a further
   form factor's Section; any other copy is renamed.

6. **Frames are never rotated.** A design that would need one is a form factor of its own.

## Styles

1. **Colors are variables.** Every solid fill or stroke and every gradient stop binds a color
   variable; no hard-coded hex/RGB and no color styles. The collection has a `Light` mode, and a `Dark` mode only if the app supports
   dark mode (`Conventions` says which).
   - Names describe the light-mode look (`Brand Blue`, `Muted Blue Light`).
   - White and black are variables too: `Brand White` and `Brand Black`.

   When the app supports dark mode:
   - A single use that must not follow its color's dark value gets its own deviant color. A deviant
     that is the same color in both modes is named `Always <Variable>` (`Always Brand White`). Use
     deviants, not mode pins: a pin is invisible where developers inspect the fill.
   - A whole element that keeps its light look in dark mode is its own frame, pinned to `Light`.
   - Check new work in both modes by switching the page's `Color` mode.

2. **Opacity goes on the layer, never the paint.** A translucent color is a variable that carries
   its transparency (`Secondary Text`) or a full-strength variable on a layer with reduced opacity. A
   layer needing different fill and stroke opacities is split in two.

3. **Text uses the text styles** on `Design System` (Body, H1–H4, …). No ad-hoc font settings.
   Each style's font size binds a dimension variable (see [Dimensions](#dimensions)).

4. **Fonts must be loadable.** An agent editing through the Figma MCP can use only fonts Figma holds:
   its library and fonts uploaded to the designer's account, not fonts installed on a machine. When
   a style's font won't load (`figma.listAvailableFontsAsync()`), the agent stops and asks the
   designer to upload it (license permitting) or choose a Figma-hosted equivalent the app can adopt.
   It does not work around a missing font.

5. **Names are written for readers.** Color variables, text and effect styles, components other
   than screens, and all component properties have readable Title Case names. The file records no code names: the code's
   names map one to one from these names, in the project's own naming convention. An agent that has to
   convert a name and does not know that convention stops and asks. In a backfill, a thing keeps
   the app's own name, in Title Case.

## Dimensions

1. **Spacing and radii follow one scale.** Padding, gaps, and corner radii are 1–4, then steps of 5;
   from 30 up, steps of 10 are preferred, though 5 is still allowed.

2. **Dimensions are variables.** A `Dimensions` collection holds `spacing/<n>`, `radius/<n>`
   (`radius/full` for pills), and `type/<n>` for font sizes, named for their value. Every padding,
   gap, corner radius, and font size binds one, defined only when something uses it. These names
   stay as they are; the code mirrors them in its own convention. A file with several form factors adds modes and may use adaptive
   variables: see [Multiple form factors](figma-designer-guide-form-factors.md).

## Components

1. **Main components live on `Components`.** Drafts of new or visibly changed components and supporting
   copies stay in the package's `Components` Section until promotion. Screen components in a file
   with several form factors are another exception (see
   [Multiple form factors](figma-designer-guide-form-factors.md)).

2. **Component sets use auto layout.** A component set is a grid auto layout that arranges its
   variant properties along the axes (`State` across, `Style` down; a single property runs across).
   Sets keep Figma's default container look; add a neutral fill only when the components themselves
   are white.

3. **Use components in their designed context.** A component drawn for one setting (a control on a
   dark photo overlay) is not reused on a different background. Add a variant instead.

4. **Images are components.** Each image exists once, as a component in an `Images` Section; every
   use is an instance, placed inside a clipping frame to show the part wanted.

5. **Start new screens from an existing screen.** Copy a screen with the same shell (the app's
   navigation and bars) and replace only the content; when none has it, build the shell (rule 6).

6. **Kit components are used linked.** Anything a kit named in `Conventions` supplies (system bars,
   keyboards, standard controls) is an instance of that kit. To customize one, or to add what it
   lacks, wrap the instance in a local component (rule 1; `Navigation Bar` wraps the kit's
   navigation bar). Where the kit still cannot do what the app needs, detach a copy, make it a
   local component per rule 1, and change it there. A component the kit supplies is not redrawn.
   A kit look keeps its paint structure, blend mode, opacity, effects and variant properties when
   colors are overridden. Measurements come from the kit's own examples. Kit properties are set to match the app, leftover placeholder text is removed, and
   kit colors are overridden with the app's color variables so they follow dark mode.

7. **Auto layout arranges contents.** Components and screens are built with auto layout, so their
   contents reposition themselves when content changes (a longer label, an added row). Items are
   not placed by hand at fixed positions where auto layout can arrange them. A screen stretches:
   its content fills the space its fixed parts leave, and a part pinned to an edge or laid over the
   content is positioned absolutely with constraints. A narrower state, a taller frame, longer content or
   a further form factor can reuse the screen.

8. **A scaled component is drawn once, at scale 1.** Scale each instance; the component keeps its
   linked text styles.

## Copy and sample data

1. **Button labels use the app's case** from `Conventions`; proper nouns keep their capitals.

2. **Content is plausible and representative of the product;** placeholder copy is not used.
   Placeholder people are obvious fakes, never real people's names.

3. **Sample data is coherent.** What a frame shows could occur together and follows the
   requirements, and the same sample people and records agree across related frames.

4. **Text is shown as the design handles it**: wrapped, truncated with an ellipsis, or scrolled.
   Never cut off by a container that is simply too small.

## Gaps

Gaps are items or footnotes per design authoring. Each gap's mirror is one Dev Mode annotation per change page and
per request Section drawing it (a page's request Sections aside), on the placeholder node of the first frame
there drawing it, in canvas order; move it when another frame becomes first. Three lines: `<owning item ID>: <the question>`, `Placeholder: <what is drawn>`,
`Owner: <owning artifact path relative to skai/changes/>`. Use node `annotations`, keeping others, in the
file's yellow `Gap` category (`figma.annotations`; create it if missing). Update on placeholder or owner-path changes;
remove when the owning item closes; never in `Production`, a backup or scratch.

## Purpose notes

Every screen frame in a package's or request's Sections carries one Dev Mode annotation on the
frame itself, in the file's violet `Purpose` category (`figma.annotations`; create it if missing),
keeping the node's other annotations (an instance repeating a base screen at a further form factor carries none:
[Multiple form factors](figma-designer-guide-form-factors.md)).
The frame of a screen's main state says what the screen is, where a user meets it and what it is
for. Every other frame of the screen, a crop included, says what it shows that the main state does
not, whether or not the package draws the main state. A sentence or two, in product words, with no IDs. Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing. It stays
on the frame in `Production` and in a backup.

## Merge marks

Where promotion merged a package's change with another's to the same item, the
place carries one Dev Mode annotation in the file's orange `Merged` category
(`figma.annotations`; create it if missing), keeping the node's other annotations: on the merged
frame, or for a style, variable or component, on its swatch, specimen or main component. A
sentence says what was merged with which package's change. Remove it when the supervisor confirms
the base; it never stays in `Production`.

## Working a backfill

When the designs are drawn from an existing app rather than ahead of it:

1. **Draw what the product shows, not how it is built.** Work from the running app. Implementation
   details never shape the design.

2. **Draw the intended design, not the app's defects.** Where the app looks wrong (a clipped label,
   a missing word, a size it was meant to have but doesn't), draw the intended look and log the
   defect where the project tracks defects.

3. **Snap to the conventions.** A value off the [Dimensions](#dimensions) scale rounds to the nearest
   step. That and any other departure from the app is a design change, recorded where the project
   records them.

## Structure check

skai's `Bin/figma-page-check.js`, run through the Figma tool on a page or Section, reports breaches
to fix and signals to look at and judge, as its header lists; the process guides say when.

## Project Addendum

If `<active-project-root>/skai/addenda/figma-designer-guide-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
