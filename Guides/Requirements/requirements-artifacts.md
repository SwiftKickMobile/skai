Managed-By: skai
Managed-Id: guide.requirements-artifacts
Managed-Source: Guides/Requirements/requirements-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-27

# Requirements Artifact Formats

The typed formats the requirements workflows produce and consume. This is the consumer-facing layer:
a downstream reader resolves any field or value here without reading the authoring method
([`requirements-authoring.md`](requirements-authoring.md)). For the catalog's own content rules —
scopes, layout, requirement format, IDs, writing style — see
[`requirements-catalog.md`](requirements-catalog.md).

A change package lives at `skai/changes/<change-id>/`. It holds the draft catalog files
(`proposed-requirements/**`) and the authoring artifact (`requirements-authoring.md`), whose
`## Requirement Changes` section lists **requirement change items**. The package may also hold
**change requests** raised by promotion. Both formats are defined below.

## Requirement change items

`## Requirement Changes` lists exactly the differences between the catalog and the drafts
under `proposed-requirements/`, one typed entry per difference. The comparison covers **only the
files the package holds** — a file absent from `proposed-requirements/` is untouched, and never
reported as removed. Each entry:

```
- R<n> <Type>: <identity>
  - **Description** what changes. Single operation: 1-2 lines.
    Multiple operations of the same kind under one identity: a sub-list,
    one bullet per operation.
  - **Justification** <Source>: <reference or rationale>
  - **Touches** the catalog files affected, written relative to the catalog root — the same paths
    `proposed-requirements/` mirrors. An index line or a file header this item changes rides here
    rather than earning an item of its own.
```

- **ID** — `R1`, `R2`, … assigned sequentially in document order and never renumbered or reused, so
  cross-references stay stable across revisions. The ID identifies; it does not order.
- **Type** — one of the pairings the package can express: `add folder` | `add file` |
  `add requirement` | `add glossary entry` | `modify requirement` | `retire requirement` (choosing
  between those two is governed by *Modify vs. retire* in
  [`requirements-catalog.md`](requirements-catalog.md)) | `modify glossary entry` | `retire glossary entry`. Retiring a glossary entry removes it — only a
  requirement keeps its heading and takes `(retired)`.
- **Source** (the leading token of Justification) — one of: `Design` | `Implementation` |
  `Human spec` | `Resolved decision` | `Agent inference` | `Change request` | `Catalog`. When the
  source is a design, a spec, or a change request, the Justification is just the citation.
  `Resolved decision: D#` cites a resolved Discussion item. `Agent inference` is a requirement the
  agent derived rather than read directly from a source, and carries a real rationale.

Entries are written top-down in catalog order — scope, then file, then requirement — mirroring the
layout. Items carry **no checkbox**: the change is realized by the draft files that accompany the
section.

### Naming the source is the check on leaked detail

Every item must name where its requirement came from. This is the cheapest available guard against
technical detail reaching the catalog: a requirement whose only honest justification is
`Implementation: the list is rebuilt whenever either stream emits` is visibly a description of code,
not a statement of product behavior. If the Justification cannot be written without naming
mechanism, the requirement is wrong, not the Justification.

✅ `Implementation: the list reorders itself whenever either source changes, and no design covers
what the user sees while that happens` — names observed behavior and the gap it fills, without
naming how the reordering works.

`Agent inference` deserves particular scrutiny. It is legitimate — much of a backfill is inference —
but an item carrying it has no external source vouching for it, so it is the first place to look
when reviewing.

### Granularity follows the file

A subject file the catalog does not yet have is one item — as is the package that creates the catalog root, whose `_requirements.md` and `glossary.md` ride in it, entries included — the folder that holds it and its index riding in
`Touches` — listing its requirements individually
restates the draft and says nothing a reader could not get from opening it. Inside a file the
catalog already has, each
requirement or glossary entry added, changed, or retired is its own item, carrying its diff.

**Baseline example** (LumenNotes — the whole catalog is new, so the items are file-granular and there
are no diffs to show):

```markdown
- R1 add folder: requirements/
  - **Description** Creates the catalog root with `_requirements.md` and `glossary.md`. Four scopes
    declared; `platform/` and `domains/` populated by this package. `features/` and `apps/` get no
    folder until something goes in them.
  - **Justification** Human spec: the product description and scope set were confirmed at drafting.
  - **Touches** _requirements.md, glossary.md

- R2 add file: domains/note.md
  - **Description** The Note entity: eleven requirements covering its states, the legal transitions
    between them, and what a discarded note retains. Prefix `NOTE-`.
  - **Justification** Resolved decision: D1, D4 — the two state-boundary rules the designs left
    open.
  - **Touches** domains/note.md, domains/_domains.md

- R3 add file: platform/sync.md
  - **Description** Six requirements on what synchronises between a user's devices and what stays
    per-device, plus conflict resolution. Prefix `SYNC-`.
  - **Justification** Design: the settings screens distinguish synced from per-device settings.
  - **Touches** platform/sync.md, platform/_platform.md
```

### Showing the diff

In a scoped change, the entry shows what changed inline. The conventions:

- **Unchanged requirements → omit entirely.** Do not list them, do not note their absence. Omission
  *is* the signal that a requirement is unchanged.
- **Added → show the requirement**, marked new.
- **Modified → show the old text struck through, immediately followed by the new text.**
- **Retired → show the text struck through.** The ID is burned: never reused, never renumbered.

Context is the file path in `Touches` plus the requirement's ID. Unlike a code signature, a
requirement is identified by an ID that survives the change, so neighbouring requirements never need
restating to locate it.

**Example** (LumenNotes):

```markdown
- R3 modify requirement: REMIND-04
  - **Description**
    ~~A reminder that fires while the app is closed remains pending until acknowledged.~~
    A reminder that fires while the app is closed remains pending until acknowledged or until
    thirty days elapse, whichever comes first.
  - **Justification** Resolved decision: D2
  - **Touches** features/reminders.md

- R4 retire requirement: REMIND-07
  - **Description** ~~A pending reminder may be re-issued from the reminder list.~~
  - **Justification** Resolved decision: D2 — re-issuing a reminder that now expires has no
    defined meaning past expiry, and the behavior was never designed.
  - **Touches** features/reminders.md

- R5 add glossary entry: Pending reminder
  - **Description** Defines the pending state and points at REMIND-04 and REMIND-06.
  - **Justification** Catalog: expiry is now a cross-cutting rule, so the term needs an index entry.
  - **Touches** glossary.md
```

## Change requests

A change request is what **promotion** raises when the catalog itself — not the package — turns out
to be wrong: a requirement promoted by an earlier package contradicts what is landing now, or is
internally inconsistent with what promotion is about to write. Authoring consumes it when the
package returns to authoring; one raised on promotion's continue branch rides through to completion
still `Proposed`, and the defect it names is carried by a new scoped-change package instead.

That is its only raiser. A defect *in the package* does not need a change request — promotion blocks
and the package goes back to authoring. A finding that the catalog is wrong, discovered anywhere
else (a retro, a work spec, someone reading it), opens a new scoped-change package instead; it does
not file a request against a package it has nothing to do with.

One markdown file per request:

`skai/changes/<change-id>/change-requests/requirements-<nnn>.md`

It carries two fields as inline `Label: value` lines — a `Change Request Status` (exactly one of
`Proposed | Incorporated | Rejected | Superseded`) and a `Reviewer Response` — above a free-form body
stating the concern, the requirement IDs involved, and the requested change:

```
Change Request Status: Proposed
Reviewer Response: <filled by authoring on reopen>
```

Lifecycle: the request opens `Proposed`; if the package returns to authoring its reviewer fills
`Reviewer Response` and moves the status to `Incorporated` (only once the adjustment is reflected in the drafts and in Requirement
Changes), `Rejected`, or `Superseded`.

## Cross-references

- [`requirements-catalog.md`](requirements-catalog.md) — catalog content rules
- [`requirements-authoring.md`](requirements-authoring.md) — the authoring workflow
- [`requirements-promotion.md`](requirements-promotion.md) — the promotion workflow
