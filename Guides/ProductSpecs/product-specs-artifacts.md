Managed-By: skai
Managed-Id: guide.product-specs-artifacts
Managed-Source: Guides/ProductSpecs/product-specs-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-21

# Product Specs Artifact Formats

Print `📖 SKAI guide: product-specs-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

The typed formats the product spec workflows produce and consume. Content rules:
[`product-specs-catalog.md`](product-specs-catalog.md). File shape and the spec tool:
[`spec-file-shape.md`](../Core/spec-file-shape.md).

## The Package

In the repository holding the catalog, `skai/changes/<change-id>/product-specs/`; after promotion,
`skai/promoted/<change-id>/product-specs/`. A promoted package is closed; new work takes a new
ID/type pair. A sibling package of another type is independent.

```
product-specs-authoring.md        authoring's artifact; ## Requirement Changes
proposed-product-specs/**         drafts mirroring the catalog: touched files only, each whole
product-specs-review.html         the rendered review page
change-requests/<nnn>/request.md  a request; its drafts beside it, proposed-product-specs/**
change-requests/<nnn>/request-review.html
product-specs-promotion.md        promotion's artifact; may be absent
evidence/                         persisted check output; may be absent
working-docs/                     working documents; the tool ignores it
```

**The review page is how the supervisor reads the package.** The tool renders it to
`product-specs-review.html`, and a request's page beside `request.md`; both are
committed. When the package materially changes, validate and re-render before anything else. The authoring and promotion artifacts link the page directly
under their title, as does `request.md`.

End the authoring artifact with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>`
per Discussion state change. An open **Gap** item marks a placeholder in the drafts, or that none exists
([`known-gaps.md`](../Core/known-gaps.md)). The page counts gap items and filters to them and their footnoted requirements; the log is not rendered;
`check-changes` checks each item's state against its last log entry.

In the promotion artifact, checked `C7` means the catalog is written; checked `C8`, the package
archived.

## Requirement Change Items

`## Requirement Changes` lists exactly the differences between the catalog and the drafts the
package holds, one typed entry per difference, compared by prose and resolved target identity. The
rendered page
shows each difference under its justification; an entry carries no text of its own.

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
  product name, never a design-tool link; for a spec or request the Justification is the
  citation; `Resolved decision: D#` cites a Discussion item;
  `Agent inference` carries a real rationale and draws first scrutiny.

The tool's `check-changes` confirms the list matches the projection: every changed requirement
and glossary entry is named by an entry, every changed index line, intro or added file by an
entry or a `Touches` line, and nothing unchanged is.

**Naming the source is the check on leaked detail.** ❌ `Implementation: the list is rebuilt
whenever either stream emits` describes code — the requirement is wrong, not the Justification.
✅ `Implementation: the list reorders itself whenever either source changes, and no design covers
what the user sees while that happens`.

**Granularity follows the file.** A file the catalog does not have is one entry, its folder and
index line riding in `Touches` — as is the package creating the catalog root, with the root index
and glossary. Inside a file the catalog has, each requirement or glossary entry added, changed or
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

## Change Requests

Any downstream consumer files a change request for any reason, against the open package for the
subject; with none open, whoever finds the defect opens a change package through authoring. The proposer never edits the package.
Supervisor input during authoring is a decision, never a request.

`change-requests/<nnn>/request.md`, numbered by filing order:

```markdown
Change Request Status: Proposed
Reviewer Response:

# Reminder Expiry On Shared Notes

[Review page](request-review.html)

## Goal

A shared note's reminder must expire for the recipient too.

## Requested Changes

- R01 modify requirement: [REMIND-04]
  …
```

Its drafts, written from the supervisor's input, are diffed on its page against the package's
drafts, falling back to the catalog; what the input leaves unsettled the filer asks at its own
Discussion gate, and only a supervisor who, asked, agrees they cannot be written sends a request
without drafts, its page then listing each requested change.

Lifecycle: filed `Proposed`; only the supervisor's instruction moves the status, applied by
authoring ([`product-specs-authoring.md`](product-specs-authoring.md) § Reopening):
`Incorporated` once the drafts and Requirement Changes reflect it, `Rejected` or `Superseded`
with the supervisor's reason in `Reviewer Response`. `Proposed` blocks promotion's readiness; one
filed on promotion's continue branch rides to completion still `Proposed`.

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-artifacts-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
