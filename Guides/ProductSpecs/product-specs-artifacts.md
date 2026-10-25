Managed-By: skai
Managed-Id: guide.product-specs-artifacts
Managed-Source: Guides/ProductSpecs/product-specs-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Product Specs Artifact Formats

Print `📖 SKAI guide: product-specs-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

The typed formats the product spec workflows produce and consume. Content rules:
[`product-specs-catalog.md`](product-specs-catalog.md). File shape and the spec tool:
[`spec-file-shape.md`](../Core/spec-file-shape.md).

## The Package

In the repository holding the catalog, `skai/changes/<change-id>/product-specs/`; after promotion,
`skai/promoted/<change-id>/product-specs/`. A promoted package is closed; new work takes a new
ID/type pair. A sibling package of another type is independent. For the **base** and requests, read
[`change-requests.md`](../Core/change-requests.md). Supervisor input during authoring is a decision, never a request.

```
product-specs-authoring.md        authoring's artifact; ## Requirement Changes
proposed-product-specs/**         drafts mirroring the catalog: touched files only, each whole
product-specs-review.html         the rendered review page
change-requests/<nnn>/            open requests, each with this layout
promoted-change-requests/<nnn>/   promoted requests
product-specs-promotion.md        promotion's artifact; may be absent
evidence/                         persisted check output; may be absent
working-docs/                     working documents; the tool ignores it
```

**The supervisor reads the package through `product-specs-review.html`.** Render and commit it;
validate and re-render before anything else after material changes. Both workflow artifacts link
it directly under their titles.

End the authoring artifact with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>`
per Discussion state change. An open **Gap** item marks a placeholder in the drafts, or that none exists
([`known-gaps.md`](../Core/known-gaps.md)). The page counts gap items and filters to them and their footnoted requirements; the log is not rendered;
`check-changes` checks each item's state against its last log entry.

In the promotion artifact, checked `C7` means the base is written; checked `C8`, the package
archived.

## Requirement Change Items

`## Requirement Changes` lists each base-to-draft difference by prose and resolved target identity
as one typed entry. Entries carry no text; the page shows each difference under its justification.

```
- R<n> <type>: <identity>
  - **Justification** <Source>: <reference or rationale>
  - **Touches** catalog-relative paths of the files this entry changes
```

- **ID** `R01`, `R02`, …: never renumbered or reused. Entries run in catalog order and carry no
  checkbox.
- **Type** `add folder` | `add file` | `add requirement` | `modify requirement` |
  `retire requirement` | `add glossary entry` | `modify glossary entry` | `retire glossary entry`.
  *Modify vs. retire* in the catalog guide decides between the two; a note-only change is
  `modify requirement`; a retired glossary entry is removed.
- **Identity** the requirement ID linked to its draft, the glossary term, or the catalog-relative
  path.
- **Source** `Design` | `Implementation` | `Supervisor input` | `Resolved decision` |
  `Agent inference` | `Change request` | `Catalog`. `Design` names the screen or state by
  product name, never a design-tool link; for a spec the Justification is the
  citation; `Resolved decision: D#` cites a Discussion item, `Base decision: D#` its base's;
  `Agent inference` carries a real rationale and draws first scrutiny; promotion writes
  `Change request: <nnn> R<n>; <the entry's own>` on folded entries.

The tool's `check-changes` confirms the list matches the projection: every changed requirement
and glossary entry is named by an entry, every changed index line, intro or added file by an
entry or a `Touches` line, and nothing unchanged is.

**Naming the source is the check on leaked detail.** ❌ `Implementation: the list is rebuilt
whenever either stream emits` describes code — the requirement is wrong, not the Justification.
✅ `Implementation: the list reorders itself whenever either source changes, and no design covers
what the user sees while that happens`.

**Granularity follows the file.** A file the base does not have is one entry, its folder and
index line riding in `Touches` — as is the package creating the catalog root, with the root index
and glossary. Inside a file the base has, each requirement or glossary entry added, changed or
retired is its own entry.

```markdown
- R01 modify requirement: [REMIND-04]
  - **Justification** Resolved decision: [D02]
  - **Touches** features/reminders.md

- R02 add file: features/sharing.md
  - **Justification** Design: the share sheet screens.
  - **Touches** features/sharing.md, features/_features.md

[D02]: #missed-reminders
[REMIND-04]: proposed-product-specs/features/reminders.md#remind-04
```

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-artifacts-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
