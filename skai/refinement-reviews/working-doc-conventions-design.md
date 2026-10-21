# Working Document Conventions Design

## Purpose

This document is the standard for SKAI's working-document conventions: where a working document
lives, that it is committed, where build and test output goes instead, and how an existing host
moves onto the rules. It is used to write and cold-review the guide; it is not something an
operator reads at runtime.

- [`Guides/Core/working-doc-conventions.md`](../../Guides/Core/working-doc-conventions.md) — the
  placement rule, the session path formula, the scratch-output rule and the worked examples.

Derivative surfaces that restate a path or the scratch rule at their point of use: the work spec
guides' path formulas and evidence rule, the UI Map, unit testing, ticket-filing and refinement
guides' path formulas, the artifact references' `working-docs/` package folder, the promotion guides'
archival clause, the integration template's **Scratch root** field, and the release entry's
migration. The guide owns the rule; they point or restate, never redefine.

Backfilled 2026-10-21 from the existing guide after its rewrite for SwiftKickMobile/skai#92
(known-gaps planning, slice 4) and the five Astra rounds that refined it.

## Authority and references

- [`internal/maintain-skai.md`](../../internal/maintain-skai.md), especially Common house style and
  the repository-layout invariants (tests under `internal/tests/`, intermediate build output to the
  scratch root).
- [`Install/component-selection.md`](../../Install/component-selection.md) owns the managed
  `.gitignore` block the guide relies on (only the two local config files are ignored).
- [`work-spec-process-design.md`](work-spec-process-design.md) owns the evidence rule's place in
  work spec implementation; [`product-specs-system-design.md`](product-specs-system-design.md),
  [`design-specs-design.md`](design-specs-design.md), [`design-process-design.md`](design-process-design.md)
  and [`ui-map-system-design.md`](ui-map-system-design.md) record each family's adoption of the
  package `working-docs/` folder and its archival.
- The supervisor's rulings of 2026-10-21 (SwiftKickMobile/skai#92 and the known-gaps planning
  record in the host) are the source of the requirements below.

## Requirements

1. **A working document lives beside the artifact it serves.** One serving a change package goes in
   that sub-package's `working-docs/` folder (`skai/changes/<change-id>/<type>/working-docs/`), in
   the package's canonical repository, and promotion archives it with the package. One serving no
   package goes in `skai/working-docs/<session-name>/`. There is no branch segment: the session name
   is the key, an effort returning to its folder reuses it, and a new effort chooses a name no other
   effort uses.
2. **The association test is stated once.** A document serves a package when it exists because of
   that package (source notes, reviews, audits, scripts). Notes serving two packages go with the
   upstream one and are linked from the other; sibling packages live in different repositories, so
   there is no shared change-level folder. A work spec serves a change, not a package, so it is a
   session document.
3. **Working documents are committed.** Nothing in the guide or its derivatives treats them as
   ephemeral or ignored; skai's own refinement and maintenance working documents follow the same
   rule in skai's repository.
4. **Captured verification output never enters the repository.** Command captures, result bundles,
   extracted results and screenshots go under the scratch root the host's `skai/integration.md`
   names, default `/tmp/skai/<session-name>/` (the change ID for package work). The artifact's
   evidence line names the command, the result and the scratch path and is the record; output is
   reproducible by rerun and need not survive. A deliverable a build produces on purpose is not
   captured output and goes where its own guide says.
5. **Creation instructions follow the placement decision.** The guide's creation steps choose the
   destination by the association test first and only then create a folder; no step prescribes the
   session path unconditionally.
6. **Worked examples cover every branch:** a package document, a session document, a workflow
   subfolder, and scratch output.
7. **The migration is an inventory, not a folder sweep.** The release entry's migration discovers
   every legacy location (branch-keyed session folders, a top-level `working-docs/`, the old
   `evidence/` places, in the app repository, each canonical repository and skai's own checkout),
   classifies every entry (relocate with destination / captured output with disposition / already
   placed after the association test on its contents) before one approval stop, moves within a
   repository or transfers across repositories (copy then remove, each side reviewed in its own
   repository), stops on any existing destination, repairs links into and inside moved documents,
   and verifies each entry against its classification. It is re-runnable: an entry already at its
   approved state is a no-op.
8. **Agent-facing, short, plain.** Rules with a bold lead, a path formula, a table of examples, no
   narrative about why the mechanism exists beyond one sentence of purpose.

## Settled decisions

- The branch segment is dropped (supervisor, 2026-10-21): the change ID was already the branch's
  final component and the session name was always the real key.
- Scratch output is not kept; the evidence line is the record (2026-10-21).
- The scratch root is a skai default with a per-host override in `integration.md` (2026-10-21).
- Package `evidence/` folders holding promotion check output are unchanged (2026-10-21).
- Tests live under `internal/tests/` with no top-level runner and no README; skill tests are
  refinement aids, never regression tests (2026-10-21).
- An interrupted cross-repository copy stops at the collision rule on rerun; no automatic
  duplicate removal (logged, rounds 3 and 5).

## Size budget

No cap yet. The guide is     4044 bytes after the 2026-10-21 rewrite and five review rounds; it has
had no compression review (skai#89's baseline procedure), so a cap is set at its next one, a little
under the compressed result, and binds every repair from then on.

## Boundaries

The guide does not define the managed `.gitignore` block (the installer's), the package layouts
(the artifact references'), promotion's archival mechanics and link repair (the promotion guides'),
the evidence line's place in a workflow (each workflow guide's), or the tests folder's contents
(the maintenance guide's). It names the scratch root's default and leaves the host's value to
`integration.md`.
