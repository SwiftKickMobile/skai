Managed-By: skai
Managed-Id: guide.figma-designer-guide-design-system-changes
Managed-Source: Guides/Design/figma-designer-guide-design-system-changes.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-17

# Figma Designer Guide: Design System Changes

Print `📖 SKAI guide: figma-designer-guide-design-system-changes` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

For a change package that adds, changes, renames or removes a style, variable or component, and
for promoting one. It extends the [Figma Designer Guide](figma-designer-guide.md); a package with
no such change does not need it.

A package drafts each new style, variable or component and each visible change;
production definitions keep their look until promotion. A rename or a removal needs no draft. A
change that alters nothing visible is not drafted; the design process guides say how it is made.
The process guides say when and in what order.

1. **A drafted style or variable is named `Draft/<package>/<name>`.** `<package>` is the change
   page's name, followed by `/<request ID>` for a request: `Draft/Pinned Notes A/Brand Blue`,
   `Draft/Pinned Notes A/CR-01/Body`. Slashes form folders. A draft variable sits in
   the collection of the one it replaces, with its modes.

2. **A changed component is drafted as a copy** in the package's `Components` Section, keeping its
   name, as a new one is. So is a supporting copy: a component copied only to show a changed one
   nested inside it.

3. **The package's `Design System` Section shows each drafted style and variable** as a swatch or
   specimen bound to the draft. Mockups use the drafts, including within supporting copies.

4. **A backup is a copy.** A style's or variable's is named `Backup/<package>/<name>`. A
   component's is a copy of the component or set, in `Components — Pre <change-id>` or, for a base
   package, in its `Base — Pre …` Section. `Components — Pre <change-id>` is built from copies of
   the `Components` page's Sections: a copy of the page itself turns each standalone component
   into an instance of the original. A page backup stays bound to the file's styles, variables and
   components and shows their changes; the earlier definition of each changed one is in its own backup. A
   run after a return to authoring replaces that package's backups.

5. **A change is applied in place.** The existing style, variable or main component is edited, or
   renamed, and keeps its identity, so every binding and instance follows. It is not swapped for
   another object. A new style or variable is a copy of the draft under its final name; a new
   component is a copy on `Components`. A removed style or variable is renamed into
   `Backup/<package>/`; a removed component moves to the backup of `Components`. Into a base
   package, that package's `Draft/` folder and `Components` Section stand where production's do.

6. **Re-pointing swaps each binding, instance or reference to a draft in the base for the base's.** Before
   swapping an instance, note the properties and overrides that use needs; after the swap, reset
   overrides, then set those again: swaps carry them over.

7. **A restore reverses each step.** Changed definitions are restored in place from their backups;
   newly copied-in ones are removed, renames reversed, moved definitions returned, and re-pointed
   uses restored. Compare restored components with their backups, variants and properties included.

8. **A package leaves** its change pages, its request Section, `Base — Pre …` Sections,
   `<page> — Pre <change-id>` pages, and everything under `Draft/<package>/` and
   `Backup/<package>/`. A request's Draft and Backup folders sit inside its package's folders; its
   request and backup Sections are top-level on the page.

## Agent tooling

These fail with no error:

- Renaming a variant property drops a variable bound to it on existing instances. Bind again
  and check a sample instance.
- A cloned variant loses its component property links. Link them again.

## Project Addendum

If `<active-project-root>/skai/addenda/figma-designer-guide-design-system-changes-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
