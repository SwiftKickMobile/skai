Managed-By: skai
Managed-Id: guide.product-specs-artifacts
Managed-Source: Guides/ProductSpecs/product-specs-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Product Specs Artifact Formats

Print `📖 SKAI guide: product-specs-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

Typed formats for product spec workflows. Content rules:
[`product-specs-catalog.md`](product-specs-catalog.md). File shape and the spec tool:
[`spec-file-shape.md`](../Core/spec-file-shape.md).

## The Package

In the catalog's repository, `skai/changes/<change-id>/product-specs/`; after promotion,
`skai/promoted/<change-id>/product-specs/`. Promoted packages are closed; new work needs a new ID/type pair. Sibling packages of other types
are independent. For the **base** and requests, read
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

**The supervisor reads the package through `product-specs-review.html`.** Render and commit it; after material changes, validate and re-render first. Both workflow artifacts link
it under their titles.

End the authoring artifact with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>`
per Discussion state change. An open **Gap** item marks a draft placeholder or its absence
([`known-gaps.md`](../Core/known-gaps.md)). The page counts gaps and filters to them and their footnoted requirements; it omits the log.
`check-changes` compares each item's state with its last log entry.

In the promotion artifact, checked `C7` means the base is written; checked `C8`, the package
archived.

## Requirement Change Items

`## Requirement Changes` gives each base-to-draft difference one typed entry, by prose and resolved
target identity. Entries omit spec text; the page shows each difference under its justification.

```
- R<n> <type>: <identity>
  - **Justification** <why the change is needed>; <Source>: <reference>
  - **Touches** catalog-relative paths of the files this entry changes
```

- **ID** `R01`, `R02`, …: never renumbered or reused. Entries run in catalog order, no checkbox.
- **Type** `add folder` | `add file` | `add requirement` | `modify requirement` |
  `retire requirement` | `add glossary entry` | `modify glossary entry` | `retire glossary entry`.
  *Modify vs. retire* in the catalog guide decides between the two; a note-only change is
  `modify requirement`; a retired glossary entry is removed.
- **Identity** the requirement ID linked to its draft, the glossary term, or the catalog-relative
  path.
- **Source** `Design` | `Implementation` | `Supervisor input` | `Resolved decision` |
  `Agent inference` | `Change request` | `Catalog`. A Justification is a reason a reader follows
  without opening anything, then its source. `Design` names the screen or state by product
  name, never a design-tool link; `Resolved decision: D#` cites a Discussion item, `Base decision: D#`
  its base's; `Agent inference` draws first scrutiny; promotion ends a folded entry's Justification
  with `; Change request: <nnn> R<n>`.

`check-changes` confirms the list matches the projection: entries name every changed requirement
and glossary entry; entries or `Touches` lines name every changed index line, intro or added file;
nothing names unchanged content.

**Implementation words in a reason are a signal.** ❌ `The list is rebuilt whenever either stream
emits; Implementation` describes code: read the requirement and the reason, and fix whichever holds the mechanism; a
reason says why the requirement changes, not what the app does.

**Granularity follows the file.** A file absent from the base gets one entry, its folder and index line in `Touches`;
so does catalog root creation, with the root index and glossary. In base files, each added,
changed or retired requirement or glossary entry gets an entry.

```markdown
- R01 modify requirement: [REMIND-04]
  - **Justification** Reminders that fired while the app was closed were lost; Resolved decision: [D02]
  - **Touches** features/reminders.md

- R02 add file: features/sharing.md
  - **Justification** Sharing a note is designed and the catalog has no requirement for it; Design: the share sheet screens
  - **Touches** features/sharing.md, features/_features.md

[D02]: #missed-reminders
[REMIND-04]: proposed-product-specs/features/reminders.md#remind-04
```

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-artifacts-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
