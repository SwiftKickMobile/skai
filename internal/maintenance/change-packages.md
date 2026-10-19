# Change package house style

Read this maintainer reference when creating or editing a workflow that authors, consumes, or promotes change packages, including callers that seed packages. It is not an installed asset or a runtime dependency. Put the relevant operational rules in each workflow guide and the consumer-facing path/format rules in its artifact reference.

## Ownership and location

A change package holds a proposal against a canonical artifact and the durable record of its review and promotion. It lives in the repository holding that canonical artifact, including a shared repository or submodule; the README links the artifact, and the agent instruction block says to read it first and block when a resource is not linked. App inputs and `skai/integration.md` still belong to the app repo.

Use these paths, relative to the canonical repository:

```text
skai/
  changes/
    <change-id>/
      product-specs/
      ui-map/
      design/
      design-specs/
  promoted/
    <change-id>/
      product-specs/
      ui-map/
      design/
      design-specs/
```

`<change-id>` groups related work. Each `<type>` folder is one independent package; the parent is a grouping directory, not a package. Current types are `product-specs`, `ui-map`, `design` and `design-specs`. Add future types here when defining their workflows. Each type owns all its drafts, review and execution artifacts, change requests, and evidence under its folder. Do not share evidence or requests at the grouping-directory level.

Use a short, stable kebab-case change ID. Use a supplied ID; if it is unclear, propose one and obtain supervisor resolution before creation. When deriving a proposal from a branch, use its final component (`work/billing-ui` → `billing-ui`). Reuse the ID for related types, including in different canonical repositories, and link their resolved locations. Do not reuse a promoted ID/type pair for a new proposal.

Ordinary conformance or execution work with no proposed canonical change belongs in `skai/working-docs/<branch-path>/<session-name>/`, following `Guides/Core/working-doc-conventions.md`. It does not create a change package just to record that canon is unchanged.

## Workflow boundaries and artifact contracts

Authoring changes only the proposal; canon stays frozen until the owning promotion workflow receives
its defined approval. A ready package must contain a complete proposal and change list that agree
with the current canonical baseline. Verification and promotion follow the owning workflow's
readiness conditions; do not infer approval merely from a folder name or authoring completion.

Define producer methods in workflow guides and consumer-facing formats in artifact references.
Downstream workflows should be able to understand a package's items, paths and completion state
without reading how the author drafted them. Use stable IDs and the shared Discussion schema;
separate review decisions, proposed canonical changes and implementation tasks.

A change request is an input to authoring, not a second mode or an alternate canonical-write path.
Name its raising and consuming workflows, status values and the point at which incorporation is
complete. Preserve its review history. Promotion may precede implementation when the workflow
explicitly supports that (UI Map Plan); archival closes the proposal, not pending downstream tasks.

## Creation, discovery, and reopening

- The package a workflow acts on is the one named or already in context. No guide scans `skai/changes/` for candidates or chooses among several; siblings of other types and all `skai/promoted/` packages are not targets.
- Reopen an existing unpromoted package for the same work rather than creating a duplicate. Preserve resolved decisions, stable item IDs, and prior evidence; refresh the comparison against current canon.
- A review-ready proposal is still active. Authoring completion does not move it; only successful promotion does.
- Canonical-write evidence distinguishes an unpromoted proposal from a package awaiting archival repair. Never redraft or re-promote canon just because such a package still occupies its active path.
- Promoted proposals are closed to further authoring. New canonical changes get a new ID/type pair. Archived implementation plans may still hold unchecked downstream work; their owning workflow may record implementation progress there without reopening the proposal or promoting it again.

## Promotion and archival

Define the canonical-write operation, its approval, and its verification in the owning workflow. Then define archival as an explicit completion operation:

1. Before the canonical write, check that `skai/promoted/<change-id>/<type>/` is available and identify links and derived previews affected by the move in the app/canonical repositories and resolved repositories of linked related packages or callers. An existing destination is not overwritten or merged. If it is the already-moved package on a retry, verify its identity and recorded progress instead.
2. Perform and verify the canonical write. Record that success independently of archival so recovery never repeats a successful write solely to finish a move.
3. Move the complete type folder from `skai/changes/<change-id>/<type>/` to `skai/promoted/<change-id>/<type>/`. Leave sibling types untouched. Remove the source grouping directory only if empty; this authorized empty-directory cleanup never removes sibling content.
4. Update live incoming links across those resolved repositories, including related packages and work specs. Reference repair does not authorize moving sibling packages or editing their proposals or decisions. Rebase links inside moved files when their resolved targets change. Preserve prose, IDs, decisions, and recorded commands/results; annotate historical paths rather than rewriting execution history. If a required reference is in a repository the operator cannot access, block with that limitation rather than claim all links were repaired.
5. Regenerate location-dependent derived output, notably UI Map HTML previews whose viewer paths point at the SKAI checkout. Preserve historical source YAML and evidence. Verify links reach their intended targets, the archived artifacts are intact, the active type path is gone, and sibling types are intact. Record the move, link checks and any render result at the archived location before checking archival completion.

If archival fails after canon was written, report canon as promoted and archival as incomplete. Resume only the unfinished archival operations from whichever path holds the package; do not repeat the canonical write. Workflow completion requires successful archival, including reference repair. Do not clear completion markers for operations that have not succeeded. `auto` bypasses planned gates only; collisions, inaccessible required references, and render failures remain blockers.

### Example: independently promoted related work

LumenNotes has active product specs and UI Map packages for `reminder-expiry`:

```text
skai/changes/reminder-expiry/product-specs/
skai/changes/reminder-expiry/ui-map/
```

Product specs promotion writes and verifies the catalog, then moves only the product specs package to `skai/promoted/reminder-expiry/product-specs/`. The UI Map package remains active, with its links to the product specs package updated. Later, UI Map promotion writes and renders the official map, moves only its own package to `skai/promoted/reminder-expiry/ui-map/`, repairs references and re-renders its preview. With no active types left, the empty `skai/changes/reminder-expiry/` grouping directory is removed.

A product-specs-only or UI-Map-only change follows the same decision procedure: promote the selected type, never the group. If the UI Map run is Plan, its unchecked implementation items remain in the promoted package for the receiving workflow.

## Existing installations

A path change requires migration instructions in the release document (`Releases/unreleased.md`), not just new examples. Discover legacy packages in each canonical repository, determine type ownership and promotion state from their artifacts, and move each type independently. Preserve canonical content, decisions, IDs, evidence and pending implementation work. Unknown ownership, shared evidence, or destination collisions require resolution before moving; never guess or overwrite. Untyped UI Map conformance artifacts without a proposal are working documents.

After a move, repair live incoming/outgoing references and regenerate location-dependent previews. Preserve historical evidence commands/results and annotate old paths. Verify that a second discovery pass finds no unmigrated packages except explicitly blocked cases. Do not fabricate new execution checkmarks on historical artifacts; record migration separately.

## Verification

For every affected authoring, promotion and caller guide, record the applicable checks:

- Path formulas, examples, request paths and evidence paths use the type folder and the artifact's repository; no discovery globs.
- Same-ID product specs and UI Map packages coexist; either can promote first without moving or consuming its sibling.
- Reopen finds active work; a review-ready package stays active; a promoted package is not redrafted or re-promoted.
- Promotion verifies canon before moving, repairs links/previews, records archived evidence, and only then marks completion.
- A collision blocks before the write; a failure after the write resumes archival only, even if the package has already moved.
- UI Map Plan retains pending downstream work at the promoted path; no-proposal conformance runs remain working documents.
- Required migration guidance covers existing mixed folders, per-type completion, evidence ownership, links, previews, collisions and repeat-run behavior.
