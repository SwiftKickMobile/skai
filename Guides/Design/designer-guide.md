Managed-By: skai
Managed-Id: guide.designer-guide
Managed-Source: Guides/Design/designer-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-07

# Designer Guide

Conventions for a project's Figma design file, the design source of truth for the app. They apply to
anyone editing the file, designer or agent. Examples use **LumenNotes**, skai's shared fictional
theme.

Designs are upstream of the UI Map. The UI Map is a development artifact with a different purpose,
so the file's Sections and frame names do not have to match its domains or scenes.

## Where the file is listed

The project README's resources table links each main page of the file separately, one row per page
(`Figma — production`, `Figma — components`, `Figma — design system`), using the page's own link so
a reader lands on the right page. Any other page developers take assets from, such as an app icon
page, gets a row too.

## Pages

1. **Every file has three main pages.**
   - `Production` — the official production designs.
   - `Components` — the component library.
   - `Design System` — the design system: color variables, text styles, and the app's design
     conventions (see [Design conventions](#design-conventions)).

   Other pages may be added for a purpose of their own, such as the two below.

2. **Production is canonical.** `Production` holds the approved design of every screen. When a design
   is approved it replaces the corresponding frame on `Production`. There is no other place to look
   for the current design.

3. **Concept pages are for exploration.** New or speculative work lives on a `<Feature> Concepts`
   page until it is approved.

4. **Archive holds designs that will not return.** Superseded designs move to the `Archive` page
   rather than being deleted, in a Section named for what they were (`sign-in — password (pre-SSO)`).

5. **Components and Design System are edited deliberately.** Changes to either are made on those
   pages on purpose, never as a side effect of screen work.

6. **Older pages are read-only.** A file that predates these conventions may keep pages from before
   `Production` existed. They are a historical record and are never edited.

## Design conventions

`Design System` records the values that differ between apps, in a frame named `Conventions`:

- **Devices and frame sizes** — each device class the file designs for and its default frame size
  (iPhone 393×852, iPad 1024×1366). This can be fewer than the app supports, when designs for a
  device class are deferred.
- **Dark mode** — whether the app supports it, which decides whether color variables have a `Dark`
  mode.
- **Button label case** — Title Case or sentence case.
- **UI kit** — the platform UI kit library the file subscribes to, with its version.

## Canvas layout

1. **Groups of screens are Sections.** Each group is a Figma Section named for the group; the
   designer chooses the groups. Sections are filled #FAFAFA, lighter than the canvas, so white
   screens stand out. A Section fits its content with 50pt padding; Sections sit 100pt apart with
   their tops aligned.

2. **Screens go right, states go down.** Within a Section each distinct screen is its own column, in
   the order a user meets them (notebooks → notes → note editor). A screen's states, and crops of
   its components, stack below it. Columns are 50pt apart; states are 100pt apart.

3. **States are in rough order of importance.** The main case comes first; edge cases and empty
   states come last. There is no stricter rule.

4. **App-wide behaviors are drawn once.** A `Global` Section holds one example of each behavior the
   whole app shares — error banner, toasts, empty state, error state, loading — each over a
   representative host screen.

5. **Overlays are drawn over their host screen** so the audience has context: dialogs, popovers, and
   sheets appear as states of the screen beneath them, over the dimmed host.

6. **Overlays are drawn as the platform renders them.** A sheet is partial height over the dimmed
   presenting screen, whose top stays visible; it is not drawn full-screen.

7. **Dormant designs are kept, and say so.** When a feature is replaced but may return, its designs
   stay on `Production`: whole screens keep their Section; a replaced part of a live screen is kept as
   one crop per state, ending just below that part, with `legacy` in the frame name
   (`note editor — legacy attachments section, expanded`). Designs that will not return move to
   `Archive`. Everything else on `Production` is what the app does today.

8. **Nothing else on the canvas.** Every top-level node is a Section, and everything in a Section is
   a screen frame. No stray frames, slices, or loose elements.

## Frames

1. **Device size by default.** A frame is its device's default size from `Conventions`.

2. **One state per device where layouts differ.** When a screen's layout differs between device
   classes, each device's version is its own state, named for the device (`note editor — iPad`). A
   check at a smaller size of the same device is its own state, named for its width
   (`notes — 375pt`).

3. **Taller to show everything.** When a screen scrolls, make the frame tall enough to show all
   possible content.

4. **Shorter to show one thing.** When a state changes only one element, crop the frame to just
   enough of the screen to show that element in context. A crop of a single component's state is
   named `Component: <component> — <state>` (`Component: tag chip — selected`).

5. **Unique `screen — state` names** in lowercase with a spaced em dash: `notes — empty`,
   `settings — error`, `note editor — date picker`. No suffix means the default state. No two frames
   share a name; a copied frame is renamed before anything else.

6. **Rotation is illustrative.** A frame is rotated only to show how the device is physically held.

## Styles

1. **Colors are variables.** Every fill and stroke binds a color variable; no hard-coded hex/RGB and
   no color styles. The collection has a `Light` mode, and a `Dark` mode only if the app supports
   dark mode (`Conventions` says which).
   - Names describe the light-mode look (`brandBlue`, `mutedBlueLight`).
   - White and black are variables too: `brandWhite` and `brandBlack`.
   - An app that adds dark mode later adds the `Dark` mode, whose values start as copies of
     `Light`. Every fill is already bound, so nothing on the screens is rebound.

   When the app supports dark mode:
   - A new variable's Dark value mirrors its Light value's lightness around the middle, judged by
     eye. A brand color whose mirror would ruin its look (lime) is only darkened.
   - A single use that must not follow its color's dark value gets its own deviant color. A deviant
     that is the same color in both modes is named `always<Variable>` (`alwaysBrandWhite`). Use
     deviants, not mode pins: a pin is invisible where developers inspect the fill.
   - A whole element that keeps its light look in dark mode is its own frame, pinned to `Light`.
   - Check new work in both modes by switching the page's `Color` mode.

2. **Opacity goes on the layer, never the paint.** A fill bound to a variable has no opacity of its
   own, so a translucent color is either a variable that carries its transparency (`secondaryText`)
   or a full-strength variable on a layer with reduced opacity. A layer that needs different
   opacities for its fill and stroke is split into two layers.

3. **Text uses the text styles** on `Design System` (Body, H1–H4, …). No ad-hoc font settings.

## Custom fonts

An agent that edits the file through Figma's servers (the Figma MCP) can load only fonts Figma
holds: its own library, plus any fonts the account has uploaded. Fonts installed on someone's
machine are not available to it.

If the Figma plan allows uploading fonts and the font's license permits it, upload the font and
confirm the agent can load it (`figma.listAvailableFontsAsync()`). Otherwise, text styles that use
the font are handled this way.

1. **A designer sets the custom font on the style.** The agent creates the style with the closest
   library font as a stand-in and names the real font in the style's description
   (`Real font: Helvetica Neue Condensed Black`). A designer with the font installed opens the style
   in the desktop app and changes its font to the real one.

2. **Agents write text through a library-font style.** Applying or switching a text style does not
   need the style's font loaded; changing the characters does.
   - To add text, create it with a style that uses a library font, set the characters, then apply
     the custom-font style.
   - To change existing text, switch it to a library-font style, edit the characters, then switch
     it back.
   - Moving, placing, and instancing the text need no font.

## Spacing

1. **Increments of 10, then 5.** Padding and gaps use multiples of 10; drop to 5 for finer control.
   Deviate only where space is genuinely tight.

## Components

1. **Main components live on `Components`.**

2. **Component sets use auto layout.** A component set is a grid auto layout with one variant
   property across the columns and the other down the rows (`State` across, `Style` down), so
   adding or removing a variant reflows the set and resizes it. Sets keep Figma's default container
   look; add a neutral fill only when the components themselves are white.

3. **Use components in their designed context.** A component drawn for one setting (a control on a
   dark photo overlay) is not reused on a different background. Add a variant instead.

4. **Images are components.** Each image exists once, as a component in an `Images` Section on
   `Components`; every use is an instance, sized and positioned inside a clipping frame to show the
   part wanted. Replacing the image in its component updates every use.

5. **Start new screens from an existing screen.** Copy an existing screen frame for the shell
   (status bar, navigation bar, tab bar) and replace only the content.

6. **System chrome comes from the platform UI kit, linked.** Status bar, home indicator, keyboards,
   and bars are instances of the kit library named in `Conventions` — never detached, so the kit's
   revisions flow through. Where the app customizes a kit element, wrap the kit instance in a local
   component on `Components` (`Navigation Bar` wraps the kit's top navigation bar). A kit instance's
   colors are overridden with the app's color variables so it follows dark mode.

## Copy and sample data

1. **Button labels use the app's case** from `Conventions`, everywhere in the file. Proper nouns
   keep their capitals ("Open Settings").

2. **Placeholder people are obvious fakes**, never real people's names.

3. **Text grows, screens scroll.** Text containers expand to fit their content and the whole screen
   scrolls. Never depict text clipped inside a fixed-height box.
