Managed-By: skai
Managed-Id: guide.design-cleanup
Managed-Source: Guides/Design/design-cleanup.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-17

# Design Cleanup

Print `📖 SKAI guide: design-cleanup` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Removes what a promoted design package left in the design file. It runs only on the supervisor's
request for a named package ("clean up after <package>"), any time after that package's promotion
([`design-promotion.md`](design-promotion.md)) completes, usually in a later session. The request
is the approval to delete, for that package only. Deleting by hand stays possible.

1. Read the tool guide and its guide to design system changes; for Figma,
   [`figma-designer-guide.md`](figma-designer-guide.md) and
   [`figma-designer-guide-design-system-changes.md`](figma-designer-guide-design-system-changes.md).
   Together they name everything a package leaves: its change pages or request
   Section, its backups, its drafts of styles, values and components, and the definitions
   promotion moved aside. Find them by those names alone, with nothing from the promoting
   session. Cleaning up a change's own package also takes whatever that change's promoted
   requests left.
2. Confirm that nothing outside what will be deleted still uses any of it. Anything still in use
   blocks the cleanup: name it and stop.
3. Delete, report what was removed, and record it as evidence in the archived promotion artifact.

## Project Addendum

If `<active-project-root>/skai/addenda/design-cleanup-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
