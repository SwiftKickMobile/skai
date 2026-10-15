Managed-By: skai
Managed-Id: guide.design-specs-promotion
Managed-Source: Guides/DesignSpecs/design-specs-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Specs Promotion

Print `📖 SKAI guide: design-specs-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Write approved specs and archive the package. Promotion owns canonical writes except verified
work-spec known-difference cleanup. Validate and prepare destination links; never change prose,
IDs, notes or drafts. Return package defects to authoring; handle canonical defects under
*Raising a Change Request*.

Supervisor approval permits promotion regardless of implementation or design state beyond `V5`.
Use [content rules/checks](design-specs.md) and [artifact formats](design-specs-artifacts.md).

## The Promotion Artifact

Promotion writes `skai/changes/<change-id>/design-specs/design-specs-promotion.md`, beside the
authoring artifact:

```
# Design Specs Promotion — <name>
## Inputs               the package being promoted; the specs it targets
## Promotion Checks     - [ ] C<n> items, unchecked until executed
## Change Requests      links to any request this run raised; may be absent
## Evidence             the verification trail
```

## Gates

Core rule: every time the agent is waiting on the supervisor, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion items and reviews its gates; the executing agent does not resolve or approve its own.

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the supervisor.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the supervisor gives advance intent. If the gate is non-standard, make it describe the exact supervisor response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the supervisor resolves it.

Workflow-specific gate notes:
- Promotion Checks is the single review point: after the readiness screen and the unchecked
  checklist, before the specs change. `next` executes the checks, writes the specs and archives the
  package. Summarize the destination files and **every item in those whole-file writes**, carried-
  forward items included, not the checklist or the change-item count. Requested draft edits return
  to authoring.
  - `⏳ GATE: Next: Promote <N> items to <paths>. Say "next" or what to change.`

Workflow-specific blocked gates:
- A readiness failure, a `V1`–`V10` failure, requested draft edits, or a contradiction in the
  existing specs that would make the write inconsistent return the package to authoring. Record the
  cause and use:
  `⏳ GATE: Blocked: <V# | readiness condition | requested wording | spec contradiction> failed — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- An archive collision, inaccessible references, the design file unreachable for `V5`, or an
  archival failure use the standard blocked gate. Mechanical faults after
  `C3`'s write are repaired in place, without rewording; archival recovery follows *Archive the
  Package*.

## Advance Intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestone in this workflow: `promotion checks`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the supervisor gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns the `- [ ] C<n>` items in
`## Promotion Checks`. For a fresh or changed-draft run, write every `C<n>` unchecked for review.
After advance intent, execute in order, record evidence and check each success. A failure in `C1`
leaves it and everything after unchecked; a mechanical fault after `C3`'s write is repaired in place,
never reworded. Record writes honestly; prose defects return to authoring. Canon carries no markers.

After changed drafts, reset all checks, retain prior evidence under `### Run <n>` and restart at
`C1`. Archival-only recovery is separate: retain `C1`–`C3` and their evidence; never repeat a
successful write to finish `C4`. Check `C4` only after the move, link repair and archived
verification succeed.

**Workflow-specific `auto` behavior.** `auto` skips the review only for already-reviewed drafts;
verification failures and the other blockers still stop it.

## Initiation

Begin only on explicit promotion intent, never automatically after authoring. Target the named
or contextual package, not siblings or promoted history.

Before fresh readiness, inspect Evidence. A recorded `C3` write awaiting confirmation/repair
resumes there: retain `C1`–`C2`, repair without rewording, verify, check `C3`, archive.
Changed drafts, intervening canon or uncertain outcomes block; never assume an unrecorded write.
Checked `C3` resumes incomplete archival only. Fully archived packages never re-promote.

Before writing, ensure `skai/promoted/<change-id>/design-specs/` is absent. Identify live incoming
references from specs/app repositories and related packages/work specs. Collisions or inaccessible
required references block; never overwrite or merge a destination.

### Readiness Screen

Prerequisite: every cited requirement's contract is canonical, even if its link still targets a
draft (`C2` repoints it). Otherwise record it in Evidence and wait at the standard blocked gate
naming it; do not return the package. Then, before creating Promotion Checks, verify:

1. Discussion has no unresolved items.
2. Current canon/draft diff by prose and resolved targets matches Spec Changes exactly; moves
   preserve identity and text before any separately declared modify.
3. No request remains `Proposed`.

Record failures in Evidence, not Promotion Checks; each returns the package to authoring.

## Promotion Checks

Write unchecked `- [ ] C<n> <identity>` items in execution order. Check projected canonical
locations over changed items and whole touched files; unrelated untouched canonical defects do not block. Contradictions making the write inconsistent
follow *Raising a Change Request*.
Known-difference notes are observations, not obligations or markers.

- `C1 Verification` — run [`V1`–`V10`](design-specs.md#verification-checks) with evidence per
  check. Open the design for `V5`; unavailable access blocks. Failures return to authoring.
- `C2 Prepare destination links` — map package draft targets to canonical destinations,
  including now-canonical requirements; retain untouched dependency targets. For moves, repoint
  incoming spec links through the prepared package files and annotate external references (packages/work specs) with the new location.
  Preserve prose, IDs, notes and target identities; do not edit drafts. Record adjusted definitions
  or that none needed changes.
- `C3 Write the specs` — write prepared whole files to the resolved root, creating it if absent;
  leave other files untouched. Record write outcome before confirmation. Confirm intended link
  targets and absence of Discussion citations, checkboxes and `🟡`; only retirement marks and
  labeled known differences accompany contracts. Repair mechanically, never reword. Add confirmation
  evidence and check `C3` only on success.
- `C4 Archive the package` — follow *Archive the Package*. Only verified write and archival
  complete promotion.

**Excerpt** (LumenNotes: `C1/V5` failed; later checks did not run):

```markdown
## Promotion Checks

- [ ] C1 Verification
- [ ] C2 Prepare destination links
- [ ] C3 Write the specs
- [ ] C4 Archive the package

## Evidence

[evidence: C1/V1; UI-NOTES-01.02, UI-NOTES-02.02, UI-NOTES-05 compared with cited contracts; each adds a screen binding]
[evidence: C1/V3; all touched-file text checked for design-tool, platform, mechanism and code terms; platform name only in UI-NOTES-03's known-difference note]
[evidence: C1/V5; Production › Notes: `notes`, `notes — empty`, `notes — stale` found; `notes — acknowledged reminder` named by UI-NOTES-02.02 NOT FOUND on Production or any approved change page; FAILED]
```

## Evidence

Use one bracket per check, including each `V` within `C1`:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
[evidence: C1/V<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Preserve reruns under `### Run <n>`. Persist/link full failure output at unique run/check paths;
success includes output only if persisted. Inspections name repeatable inputs and observations.
Unresolved paths fail; empty subjects need reasons. Compare IDs per rewritten file and retired
IDs across specs; strip path prefixes (`grep -rhoE`) before comparison.

## Raising a Change Request

For existing-spec contradictions/inconsistencies, raise and link a request under Change Requests
using [artifact formats](design-specs-artifacts.md). Block if the write would leave inconsistent
specs; otherwise continue, checking the passing check with its linked request. Report any
still-Proposed request at completion; its defect needs a new package.

## Archive the Package

After verified `C3`, execute `C4`:

1. Move `skai/changes/<change-id>/design-specs/` intact to
   `skai/promoted/<change-id>/design-specs/` in the specs repository. Preserve sibling types;
   remove the active grouping directory only if empty.
2. Repair live incoming links across resolved repositories/packages/work specs and relative links
   inside moved files. Preserve target identities, prose, IDs, decisions, commands and results;
   annotate historical paths with current locations. Inaccessible/unrepaired required links block.
3. Verify archived files/links, absent active type path and preserved siblings. Record move/link
   evidence; check `C4` in the archived promotion artifact.

On failure report “specs promoted, archival incomplete” with the standard blocked gate.
Resume at either package path; finish archival only, never repeat `C3`.

## Completion

With `C3` and `C4` evidenced, link the archived artifact and any still-Proposed requests (new
scoped packages own their defects). Emit
`🏁 Complete. Let me know if anything needs adjustment.`

Never reopen or re-promote archived drafts.

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
