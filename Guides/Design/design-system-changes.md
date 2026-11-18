Managed-By: skai
Managed-Id: guide.design-system-changes
Managed-Source: Guides/Design/design-system-changes.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-17

# Design System Changes

Print `📖 SKAI guide: design-system-changes` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

For a design package that adds, changes, renames or removes a style, value or component of the
design system, for promoting one, and for a fix that changes nothing visible. It extends
[`design-authoring.md`](design-authoring.md) and [`design-promotion.md`](design-promotion.md); no
other package needs it. For Figma, load
[`figma-designer-guide-design-system-changes.md`](figma-designer-guide-design-system-changes.md).

A **shared definition** is a style, a value or a component. A **use** of one is anything that
refers to it: a frame's or a component's binding or instance, and another definition's reference
(a text style's size, a value that points at another value).

## Authoring

1. **Production's definitions keep their look until promotion.** Never change their look in place. Draft
   each new or changed definition in the form the tool guide gives; the mockups use the draft.
2. **Draft only what changes,** plus **supporting copies**: the few components copied only to show
   a changed one inside them. Nothing else that depends on a changed definition is drafted.
3. **Every change is a `## Design Changes` entry** of kind `component` or `style`; `style` is any
   named style or value (a color, a text style, an effect, a dimension). One entry per definition,
   in canvas order, under a heading named for the place the design file shows the package's design
   system drafts. Identity is the definition's name: for `add` and `modify`, linked to where the
   draft is shown (after promotion, to where the base shows it); for `remove`, unlinked. The
   Description says what changed in a reader's words, as for a screen.
   - A `remove` entry drafts nothing and says what each use becomes.
   - A rename is a `modify` entry that drafts nothing: its identity is the current name, unlinked,
     and its Description gives the new name.
   - A supporting copy has no entry.

```markdown
### Design System

- V07 modify style: [Brand Blue](<link>)
  - **Description** The brand blue is deeper.
  - **Justification** Buttons failed the contrast check; Resolved decision: D04
- V08 modify style: Caption
  - **Description** Renamed to Footnote.
  - **Justification** It is used only under fields; Supervisor input
```

## Promotion

**`C2`.** Inventory design system drafts as screen drafts, both ways: each draft has an entry, and
each `add` or `modify` entry has a draft unless it is a rename or the no-mockups ruling leaves it
undrawn. A supporting copy has no entry. A `remove` or rename entry names a definition the base
has or uses from production, and is never an undrawn entry. A listed change that should have a draft and has none was
never drafted or was made in place: `C2` fails and names it.

**`C3`.** Three rules hold throughout:

- **Nothing is lost before the base is approved.** The fold deletes no definition and leaves the
  package's drafts as they are.
- **Identity is kept.** A definition the base already has is changed, and restored, in place,
  because its uses follow its identity. Apply to it the change the entry lists; never replace it
  with the draft.
- **Afterward nothing that belongs to the base uses this package's drafts,** in any frame or
  definition. Leave the package's drafts and backups as they are.

Into production, per entry:

- **Changed:** back up production's definition, then apply the change to it in place.
- **New:** copy the draft into place under its final name. It needs no backup.
- **Renamed:** rename production's definition in place.
- **Removed:** point each use in the base at what the entry says it becomes, then move production's definition
  aside into the backup.

Into a base package, production is never touched: the base package's draft of a definition stands
where production's does above. Where the base package has no draft of a
definition that a drawn entry changes, make one from the current definition with that change
applied, and point the base package's uses at it. A removal or rename of a definition only production has carries its entry to
the base's list. For a removal, re-point the base's uses; for a rename, leave them bound until the
base's promotion.

Then point every use of a draft, in what was copied into the base, at the base's definition, a
supporting copy's uses included, with the care after each swap that the tool guide gives. Bring
the base's own documentation of its design system up to date. `C3`'s evidence names each
definition and what was done to it. A run after a return to authoring replaces the earlier run's
backups. The tool guide gives the steps, names and backup locations.

## A Fix That Changes Nothing Visible

Replacing a hand-drawn element with a component, or a raw value with a named one, so that nothing
looks different, is not a change. Make it directly in the base, production included, with no
package, request, draft or entry. Compare each affected screen before and after, save the
comparison as a working document serving no package
([`working-doc-conventions.md`](../Core/working-doc-conventions.md)), and say where it is in your
report.

## Project Addendum

If `<active-project-root>/skai/addenda/design-system-changes-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
