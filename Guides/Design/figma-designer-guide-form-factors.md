Managed-By: skai
Managed-Id: guide.figma-designer-guide-multiple-sizes
Managed-Source: Guides/Design/figma-designer-guide-form-factors.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-18

# Figma Designer Guide: Multiple Form Factors

Print `📖 SKAI guide: figma-designer-guide-form-factors` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

For a file whose `Conventions` list more than one form factor. It extends the
[Figma Designer Guide](figma-designer-guide.md); a file with one form factor never needs it.
Names come from `Conventions`; examples use `Compact` and `Wide`, with `Compact` the base.

1. **A mode per form factor.** The `Dimensions` collection has a mode named for each form factor
   and a `target` string variable naming it. Each form factor's Sections are set to its mode.

2. **Adaptive values only where the app differs.** A value that changes with the form factor is an
   adaptive variable in a `-adapt` group, named for its smallest value: `spacing-adapt/20` is 20 at
   `Compact` and 30 at `Wide`. Add one only while building a screen that needs it. The code mirrors
   the names in its own convention.

3. **Screens are components on `Production`.** Each screen on `Production` is a component built to
   stretch (the main guide's auto layout rule). Each further form factor has a page
   (`Production (<form factor name>)`, as `Production (Wide)`) with the same Sections, holding an
   instance of each screen, or its own screen component where the layout differs (rule 4), sized
   by the main guide's Frames rules. Screen components have no variants; modes resolve adaptive values.

4. **A layout that differs is assembled from the same content.** Where a form factor's layout
   genuinely differs (a split view; a side panel where `Compact` uses a full screen; a sheet that fills the screen at
   `Compact` and is a card over its host screen at `Wide`), the content is built once as its own component (main guide's Components rules),
   and what differs is the container around it: the whole screen, a card over another screen, a
   side panel. Each version is assembled from that content and any shared screens; one whose
   layout differs is its own screen component under the same name, on its form factor's page or
   change-page Section.

5. **Chrome switches by variable.** App chrome (navigation, tab bar, header) that differs by form factor, or whose kit component
   does while the app looks the same, is a local component
   whose `Target` variant property is bound to the `target` variable. A variant with no counterpart at another form factor is left unbound.
   Every variant uses auto layout and hugs its content, and each instance hugs; otherwise an
   instance can keep one variant's size when it switches. Content goes in through component
   properties, set in the screen component and again on each further form factor's screen: a
   value set only inside the screen component is lost when the variable switches the variant.

6. **A further form factor is a full set.** Its page repeats every base frame, a state or a crop
   included, in the same Sections and order, and holds no frame of its own that repeats what
   another Section shows.

7. **The base form factor is bound first.** Dimension variables are bound throughout the base form
   factor's screens before any screen of a further one is built.

8. **A part shown at only some form factors binds its visibility to a variable:** a boolean in
   `Dimensions` named for where it shows (e.g. `visible/Wide`), true where it
   shows and false elsewhere. This holds for a nested instance too. A layer inside an instance
   cannot be moved, so differing placement uses this variable or an adaptive value.

9. **Sample data is the same at every form factor.** Keep the same people and records; a larger one adds without swapping them. Content the base
   has no room for sits in the screen component, shown through rule 8's variable, or in the
   screen's own component where its layout differs (rule 4). Check the data again at the larger
   form factor.

10. **An image drawn for one form factor is named for it.**

11. **A change page has a Section per form factor,** side by side at the top level: the
    base one named for the package, each further one `<package> (<form factor name>)`, each set to
    its mode. Each holds the same per-screen Sections. A further one repeats every screen frame the
    package draws in the base Section: an instance of the base Section's screen, or the screen's own version where its
    layout differs. Any `Components` and `Design System` Sections stay single, in the base Section. A
    request does the same, each further Section named `<request ID> — <name> (<form factor name>)`.
    The main guide's rules for a package or request Section, backup and fold included, hold for
    each.

12. **A base screen's instance at a further form factor carries no purpose note;** its note is
    on the matching base frame. A screen with its own layout carries one, saying what differs
    there.

## Project Addendum

If `<active-project-root>/skai/addenda/figma-designer-guide-form-factors-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
