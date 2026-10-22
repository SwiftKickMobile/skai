Managed-By: skai
Managed-Id: guide.spec-file-gaps
Managed-Source: Guides/Core/spec-file-gaps.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-21

# Spec File Gaps

Print `📖 SKAI guide: spec-file-gaps` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read when raising a gap; the [workflow](known-gaps.md), the [file shape](spec-file-shape.md).

Mark a draft placeholder with `[^n]` ending its sentence, rule or table cell. Define it under the item after rules and tables, before known differences:

`[^n]: **Gap:** D<n> — <question>. Placeholder: <one line>`

`D<n>` names the open gap item. A marker-less definition notes the nearest requirement; no Placeholder clause: nothing to proceed on.

```markdown
### REMIND-01
Reminders expire after 30 days.[^1]

[^1]: **Gap:** D02 — When reminders expire. Placeholder: 30 days.
```

`validate` pairs markers with definitions under their item and rejects a missing definition, a duplicate label in a file, a definition outside an item, off this form or after a known difference, and any footnote in canon (a single root, or a projection's first root).

`check-changes` fails if a draft footnote names no open gap item or an open gap item has no footnote in any draft (marker-less notes count): zero open gaps at promotion means no placeholders.

On the page, a marker is a superscript link to its Gap line under the item, which links the Discussion item; a footnoted item counts as modified. The counts row shows the gaps; the gaps tile filters the page to them.

## Project Addendum

If `<active-project-root>/skai/addenda/spec-file-gaps-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
