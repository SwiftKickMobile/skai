Managed-By: skai
Managed-Id: guide.spec-file-gaps
Managed-Source: Guides/Core/spec-file-gaps.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-24

# Spec File Gaps

Print `📖 SKAI guide: spec-file-gaps` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read when raising a gap; [workflow](known-gaps.md), [shape](spec-file-shape.md).

All artifacts: `[^n]`, numbered by first use and unique per file, ends a placeholder sentence, rule, cell or entry; define under its item (spec: after rules and tables, before known differences):

`[^n]: **Gap:** <owning item>. Placeholder: <the provisional answer this place builds on>`

Owner: open gap `D<n>` where the question was raised, not merely inherited (here or scoped: `base D04`, `product specs D21`). Questions stay only there. Marker-less definitions note the nearest requirement; no Placeholder: nothing to proceed on.

```markdown
### REMIND-01
Reminders expire after 30 days.[^1]

[^1]: **Gap:** D02. Placeholder: 30 days.
```

Spec drafts: `validate` checks form, placement, numbering and defined markers; none in canon (single root or projection's first root).

`check-changes` pairs draft footnotes naming this artifact's own items with its open gaps (marker-less notes count): unpaired ones fail; marked open gaps pass. Design pages only render; neither check runs.

Pages: plain superscripts; a card's notes share a box, one line each: owner chip linked to its item (text on hover), then placeholder. Footnoted items count as gaps, filtered by the gaps tile.

## Project Addendum

If `<active-project-root>/skai/addenda/spec-file-gaps-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
