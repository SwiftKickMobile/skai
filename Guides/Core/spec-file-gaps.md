Managed-By: skai
Managed-Id: guide.spec-file-gaps
Managed-Source: Guides/Core/spec-file-gaps.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-24

# Spec File Gaps

Print `📖 SKAI guide: spec-file-gaps` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read when raising a gap; the [workflow](known-gaps.md), the [file shape](spec-file-shape.md).

All artifacts use `[^n]` at a placeholder's sentence, rule, table cell or entry end, defined under the item (spec: after rules and tables, before known differences):

`[^n]: **Gap:** <owning item>. Placeholder: <what this place shows for it>`

Owner: an open gap `D<n>` here or scoped (`base D04`, `product specs D21`). Questions stay only there. Marker-less definitions note the nearest requirement; no Placeholder clause: nothing to proceed on.

```markdown
### REMIND-01
Reminders expire after 30 days.[^1]

[^1]: **Gap:** D02. Placeholder: 30 days.
```

Spec drafts: `validate` requires this form, placement, a definition per marker and labels numbered by first use, unique per file; none in canon (a single root, or a projection's first root).

`check-changes` pairs this artifact's items only: it fails a draft footnote naming no open gap and an open gap no footnote marks (marker-less notes count); a marked open gap passes. Design pages only render; neither check runs.

Pages: plain superscript marks; a card's notes share one box, a line each: owner chip linked to its item (text on hover), then placeholder. Footnoted items count as gaps; the gaps tile filters to them.

## Project Addendum

If `<active-project-root>/skai/addenda/spec-file-gaps-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
