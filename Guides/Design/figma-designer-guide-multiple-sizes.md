Managed-By: skai
Managed-Id: guide.figma-designer-guide-multiple-sizes
Managed-Source: Guides/Design/figma-designer-guide-multiple-sizes.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-13

# Figma Designer Guide: Multiple Target Sizes

Before using this guide, complete [Project addendum](#project-addendum) loading below.

For a file whose `Conventions` list more than one target size. It extends the
[Figma Designer Guide](figma-designer-guide.md); a file with one target size never needs it. Examples
call the sizes `Compact` and `Wide`.

1. **A mode per target size.** The `Dimensions` collection has a mode for each target size
   (`Compact`, `Wide`) and a `target` string variable naming it. Each target size's Sections are set
   to its mode.

2. **Adaptive values only where the app differs.** A value that changes with the target size is an
   adaptive variable in a `-adapt` group, named for its smallest value: `spacing-adapt/20` is 20 at
   `Compact` and 30 at `Wide`. Add one only when a design needs it. The code mirrors the names
   (`spacing20adapt`).

3. **Screens are components on `Production`.** Each screen on `Production` is a component that
   stretches to its frame size. Each further target size has its own page (`Production (Wide)`) with
   the same Sections, holding an instance of each screen sized by the guide's Frames rules. Screen
   components have no variants; the mode changes their spacing and type.

4. **A layout that differs is assembled, not copied.** When a target size's layout genuinely differs
   (a split view, a side panel where `Compact` uses a full screen), the screen is broken into
   components for its parts, on `Components`. That target size's version is then its own screen
   component on its own page, built from those parts and the shared screens, under the same name.

5. **Chrome switches by variable.** App chrome that differs by target size (navigation, tab bar,
   header) is a local component whose `Target` variant property is bound to the `target` variable,
   with variants that hug their content. Content goes in through component properties: overrides of
   nested layers are lost when the variable switches the variant.

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/figma-designer-guide-multiple-sizes-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Once the lookup is done
and before work, report `- 📖 SKAI guide: figma-designer-guide-multiple-sizes`, nesting `- 📎 Addendum loaded` under it only if one
loaded. If the lookup fails, nest `- ⛔ Addendum lookup failed: <what failed>` and stop. Report each guide
once per task; one addendum line covers referenced documents. Not a gate; keep GATE lines last.
