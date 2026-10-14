Managed-By: skai
Managed-Id: guide.designer-guide
Managed-Source: Guides/Design/figma-designer-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-13

# Figma Designer Guide

Before using this guide, complete [Project addendum](#project-addendum) loading below.

Conventions for a project's Figma design file, the design source of truth for the app, for anyone
editing it, designer or agent. They hold for any platform the app runs on. Examples use
**LumenNotes**, skai's shared fictional theme.

Designs are upstream of the UI Map, so the file's Sections and frame names need not match its
domains or scenes.

## Pages

1. **Every file has three main pages.**
   - `Production` — the official production designs.
   - `Components` — the component library.
   - `Design System` — variables, text styles, and the app's
     [design conventions](#design-conventions).

   Other pages serve a purpose of their own: a change page, named for its change package, holds
   that change's drafts until they are on `Production`.

2. **Production is canonical.** `Production` holds the approved design of every screen (plus a page
   per further target size; see [Multiple target sizes](figma-designer-guide-multiple-sizes.md)).
   There is no other place to look for the current design.

3. **Components and Design System are edited deliberately**, never as a side effect of screen work.

4. **Older pages are read-only.** Pages from before `Production` existed are a historical record and
   are never edited.

## Design conventions

`Design System` records the choices that differ between apps, in a frame named `Conventions`. The
designer makes them; the guide does not.

- **Target sizes** — the sizes the app is designed at, each with a name and a default frame size.
  Orientation is part of a target size. This can be fewer than the app supports, when some are
  deferred.
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
   their tops aligned.

3. **Each page type fills its Sections differently**, as below.

| Page | Sections are | Inside a Section |
| --- | --- | --- |
| `Production` (and its target-size pages), change pages | Groups of screens | Screens |
| `Components` | Component families (`Controls`, `Icons`, `Images`) | Component sets, components, and reference frames |
| `Design System` | Foundation topics (`Conventions`, `Colors`, `Text Styles`, `Dimensions`) | Documentation frames |
| Asset pages (an app icon page) | Asset groups | Frames set up for export |

### Screen pages

`Production` and its target-size pages, and change pages.

1. **Screens go right, states go down.** Within a Section each distinct screen is its own column, in
   the order a user meets them (notebooks → notes → note editor). A screen's states, and crops of
   them, stack below it. Columns are 50px apart; states are 100px apart.

2. **Choose states for the screen, not screens for states.** A state is drawn when the screen is
   naturally in that situation: its main use, a mode, a lifecycle point, empty, error, loading. A
   control's own states (pressed, selected, disabled) live in its component set, and changes inside
   a component (a slider's value bubble) live in its reference frame; neither gets a screen of its
   own. Pick sample data that shows several things at once (a pinned, a shared, and an untitled
   note).

3. **States are in rough order of importance.** The main case comes first; edge cases and empty
   states come last.

4. **App-wide behaviors are drawn once.** A `Global` Section holds one example of each behavior the
   whole app shares — error banner, toasts, empty state, error state, loading — each over a
   representative host screen.

5. **Platform differences are drawn once.** Screens are drawn in the look of the platform
   `Conventions` names. A `Platforms` Section shows, once, how shared chrome (navigation, tab bar,
   dialogs) looks on each other platform or OS version the app serves, rather than repeating screens.

6. **Overlays are drawn over their host screen.** Dialogs, menus, popovers, and sheets are states of
   the screen beneath them, so the audience has context. Where a kit supplies one, its look is the
   kit's (rule 6 under Components).

7. **Only screens inside a Section.** Every node in a Section is a screen (frame, component, or
   instance) or a crop of one; on a change page, also the new components its drafts need.

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

2. **Documentation is built from the foundations it documents.** Swatches bind the color variables
   they show and type specimens use the text styles they name, so the page updates when a
   foundation changes.

### Asset pages

1. **Frames are set up for export.** Each exported asset is a frame at its export size, with its
   export settings, named for the file it produces.

## Frames

1. **Target size by default.** A screen frame is its target size from `Conventions`. Other target
   sizes follow [Multiple target sizes](figma-designer-guide-multiple-sizes.md).

2. **Smaller sizes are states.** A check below a target size is its own state, named for its width.

3. **Taller to show scrolling content.** When the whole screen scrolls, make the frame tall enough
   to show representative content. A region that scrolls inside a fixed layout does not change the
   frame.

4. **Shorter to show one thing.** When a state changes only one element, crop the frame to just
   enough of the screen to show that element in context.

5. **Unique names.** Screen frames are named `screen — state` in lowercase with a spaced em dash:
   `notes — empty`, `note editor — date picker`. No suffix means the default state. No two frames
   on a page share a name; a copied frame is renamed before anything else.

6. **Frames are never rotated.** A landscape design is a landscape target size, not a rotated frame.

## Styles

1. **Colors are variables.** Every fill and stroke binds a color variable; no hard-coded hex/RGB and
   no color styles. The collection has a `Light` mode, and a `Dark` mode only if the app supports
   dark mode (`Conventions` says which).
   - Names describe the light-mode look (`brandBlue`, `mutedBlueLight`).
   - White and black are variables too: `brandWhite` and `brandBlack`.

   When the app supports dark mode:
   - A single use that must not follow its color's dark value gets its own deviant color. A deviant
     that is the same color in both modes is named `always<Variable>` (`alwaysBrandWhite`). Use
     deviants, not mode pins: a pin is invisible where developers inspect the fill.
   - A whole element that keeps its light look in dark mode is its own frame, pinned to `Light`.
   - Check new work in both modes by switching the page's `Color` mode.

2. **Opacity goes on the layer, never the paint.** A translucent color is a variable that carries
   its transparency (`secondaryText`) or a full-strength variable on a layer with reduced opacity. A
   layer needing different fill and stroke opacities is split in two.

3. **Text uses the text styles** on `Design System` (Body, H1–H4, …). No ad-hoc font settings.
   Each style's font size binds a dimension variable (see [Dimensions](#dimensions)).

4. **Fonts must be loadable.** An agent editing through the Figma MCP can use only fonts Figma holds:
   its library and fonts uploaded to the designer's account, not fonts installed on a machine. When
   a style's font won't load (`figma.listAvailableFontsAsync()`), the agent stops and asks the
   designer to upload it (license permitting) or choose a Figma-hosted equivalent the app can adopt.
   It does not work around a missing font.

## Dimensions

1. **Spacing and radii follow one scale.** Padding, gaps, and corner radii are 1–4, then steps of 5;
   from 30 up, steps of 10 are preferred, though 5 is still allowed.

2. **Dimensions are variables.** A `Dimensions` collection holds `spacing/<n>`, `radius/<n>`
   (`radius/full` for pills), and `type/<n>` for font sizes, named for their value. Every padding,
   gap, corner radius, and font size binds one, defined only when something uses it. The code
   mirrors the names (`spacing20`). A file with several target sizes adds modes and adaptive
   variables: see [Multiple target sizes](figma-designer-guide-multiple-sizes.md).

## Components

1. **Main components live on `Components`.** Two exceptions: a new component a draft needs stays on
   its change page until promotion moves it; and screen components in a file with several target
   sizes (see [Multiple target sizes](figma-designer-guide-multiple-sizes.md)).

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
   keyboards, standard controls) is an instance of that kit, never detached or redrawn. To customize
   one, wrap the instance in a local component on `Components` (`Navigation Bar` wraps the kit's
   navigation bar). Kit colors are overridden with the app's color variables so they follow dark
   mode.

## Copy and sample data

1. **Button labels use the app's case** from `Conventions`; proper nouns keep their capitals.

2. **Placeholder people are obvious fakes**, never real people's names.

3. **Text is shown as the design handles it**: wrapped, truncated with an ellipsis, or scrolled.
   Never cut off by a container that is simply too small.

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

## Agent tooling

Practices for an agent editing the file through the Figma MCP. Reusable tools live in SKAI's `Bin/`;
project-specific ones stay in the project.

1. **Keep a state file.** Scripts share nothing between calls: record page, Section, component,
   variable, and image IDs in a JSON file in the working-doc folder after every write.

2. **Import library components by key in every call** (`importComponentByKeyAsync` /
   `importComponentSetByKeyAsync`); their node IDs do not persist between calls.

3. **Upload files with `upload_assets`.** SVGs become vectors and PNGs image frames. Clip paths in
   an SVG import as masks: for a single-color glyph, intersect each mask with what it clips and
   flatten, keeping the original fill rule.

4. **Lay out component sets as grids explicitly.** Appending variants does not place them: set the
   column and row counts, place each with `setGridChildPosition(row, column)`, and size tracks to hug.

5. **Masks drawn by Figma's servers do not clip frames or instances.** A shape can mask plain shapes
   but not a component instance.

6. **Scaling unlinks text styles.** `rescale()` (the Scale tool) detaches scaled text from its
   style; the component keeps the linked style at its base size.

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/figma-designer-guide-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Once the lookup is done
and before work, report `- 📖 SKAI guide: figma-designer-guide`, nesting `- 📎 Addendum loaded` under it only if one
loaded. If the lookup fails, nest `- ⛔ Addendum lookup failed: <what failed>` and stop. Report each guide
once per task; one addendum line covers referenced documents. Not a gate; keep GATE lines last.
