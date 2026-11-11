Managed-By: skai
Managed-Id: guide.spec-file-gaps
Managed-Source: Guides/Core/spec-file-gaps.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-10

# Spec File Gaps

Print `📖 SKAI guide: spec-file-gaps` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read when raising a gap; [workflow](known-gaps.md), [shape](spec-file-shape.md).

All artifacts: `[^n]`, numbered by first use, unique per file, ends a placeholder sentence, rule, cell or entry; define under its item (spec: after rules and tables, before known differences):

`[^n]: **Gap:** <owning item>. Placeholder: <the provisional answer this place builds on>`

Owner: open gap `D<n>` where raised, not where inherited; questions stay only there. Raised here, bare; elsewhere, base too, [linked, label defined](change-requests.md) (`[D27][001 D27]`). Marker-less definitions note the nearest requirement; no Placeholder: nothing to proceed on.

```markdown
### REMIND-01
Reminders expire after 30 days.[^1]

[^1]: **Gap:** D02. Placeholder: 30 days.
```

Spec drafts: `validate` checks form, placement, numbering, defined markers; none in canon (single root or projection's first root).

`check-changes` pairs draft footnotes naming this artifact's own items with its open gaps (marker-less notes count): unpaired ones fail; marked open gaps pass. Design pages only render; neither check runs.

Pages: plain superscripts; a card's notes share a box, one line each: owner chip linked to its item (text on hover), then placeholder. The gaps tile counts and filters gap items and footnoted cards.

## Project Addendum

If `<active-project-root>/skai/addenda/spec-file-gaps-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
