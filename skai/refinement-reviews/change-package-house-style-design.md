# Maintenance routing and change package house style — design

## Purpose and authority

This standard records the supervisor's requested change for the current edits. It is a maintainer review input, not a runtime dependency or a new workflow. Implementation choices in the edited guides are subject to review; this document does not certify them.

## Requested maintenance organization

Keep the important, common maintenance instructions in `internal/maintain-skai.md`. Move less common, detailed guidance into separate documents, with a routing table in the main guide. Each table entry must describe when an agent needs that reference and what it contains sufficiently to find relevant material without reading every document during every maintenance task. Preserve existing safety, bookkeeping, installation and release rules when relocating them.

Runtime instructions remain usable by a fresh operator: maintainer references may guide authors, but should not become an extra execution burden on host workflows. The split should reduce the entry document's size without hiding essential rules or requiring all references unconditionally.

## Requested change package layout

Related work must be easy to find by change ID while package types can coexist and promote independently:

```text
skai/changes/<change-id>/product-specs/
skai/changes/<change-id>/ui-map/
skai/promoted/<change-id>/product-specs/
skai/promoted/<change-id>/ui-map/
```

The change-ID directory groups related work. Each type directory is independently owned and contains that package's proposal and collateral. Product specs and UI Map must both conform to the shared house style; supporting creation, discovery, artifact formats and callers must be consistent.

Promotion moves the relevant type folder after its canonical promotion succeeds. It must not move an unpromoted sibling. Completed packages remain available as durable history, and affected live references must remain usable. Existing canonical artifact ownership, authoring/promotion approval boundaries, and UI Map Plan versus Build semantics are preserved. Moving a Plan package must not lose its pending downstream work.

## Migration and recovery

The release document must explain how existing host artifacts adopt the layout, including mixed legacy folders, type-owned evidence and references, completed versus active proposals, and derived previews. Preserve canonical content, proposals, IDs, decisions, history and pending implementation work. Do not overwrite a conflicting destination or fabricate historical execution evidence.

Canonical promotion and archival may be interrupted separately. Operators must be able to finish the remaining work without treating a completed proposal as an unpromoted draft or repeating a successful canonical write solely to complete a move. The specific completion markers and recovery mechanics in the implementation are reviewable choices, not requirements prescribed here.

Conformance work with no proposed canonical change must be distinguishable from active proposals. Its artifact layout and handoff behavior must be coherent with existing working-document conventions; it must not silently trigger map promotion.

## Boundaries and constraints

- This change concerns maintenance routing and change package ownership/lifecycle; it does not redesign requirement prose, ID semantics, catalogs, UI Map schema, rendering behavior, or the process-refinement workflow.
- Existing gate, Discussion and marker semantics are retained except where archival necessarily affects completion. A new gate, duplicate state field, proof burden or substantial checklist expansion needs an explicit tradeoff, not an automatic acceptance as a review fix.
- The product specs system's existing 11,000-word cap across catalog, authoring, promotion and artifact guides has not been raised by this request. Report current size and any repair cost against that constraint; do not silently waive it.
- No new numerical size budget is prescribed for the maintainer reference set. Its organization is judged against selective loading and keeping the main guide concise.
- No commits, release cut, host migration or GitHub issue state change is requested by this review.

## Review acceptance questions

1. Can an agent find the relevant maintenance rules without loading unrelated specialist documents?
2. Did extraction preserve and route the common and specialized rules coherently?
3. Can same-ID product specs and UI Map packages coexist and promote in either order without crossing ownership?
4. Can creation, discovery, reopening, promotion, recovery and downstream consumption operate from the documents without prior chat context?
5. Are existing installations given a usable and nondestructive migration path, with proposals and historical records preserved?
6. Does the implementation keep its added process weight and document size proportionate to the requested behavior?

## Amendment — 2026-10-18

- The `requirements/` type folder becomes `product-specs/` under both `skai/changes/<change-id>/`
  and `skai/promoted/<change-id>/`.
- Change requests are folders, `change-requests/<nnn>/`, holding `request.md` (status, reviewer
  response, title, Goal, Requested Changes in the typed change-item format) and optionally the
  request's own drafts in the spec file shape, written from the requester's input. They are filed
  by a downstream consumer against an open package (never the canonical artifact: with no package
  open, the finder opens one through authoring), for product specs and design specs alike; the
  supervisor rules on each and the owning authoring workflow applies the ruling (decisions of
  2026-10-19 in `product-specs-system-design.md`). Promotion still cannot move a type folder while
  a request in it is `Proposed`.

## Amendment — 2026-10-19

- **Stable IDs in process artifacts are zero-padded to two digits** (supervisor, 2026-10-19):
  Discussion items `D01`, tasks `T01`, findings `F01`, suggestions `S01`, change entries `R01` /
  `S01`, three digits past 99 (`D100`), matching the spec IDs' `-01` form. The rule lives in
  `Guides/Core/process-flow.md` § Stable letter-led IDs; every guide's examples follow it. Artifacts
  written before this change keep their unpadded IDs; tools and readers accept both, and an
  artifact never mixes the two forms within one list.
