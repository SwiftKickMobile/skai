Managed-By: skai
Managed-Id: guide.design-specs-promotion
Managed-Source: Guides/DesignSpecs/design-specs-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Specs Promotion

Print `- 📖 SKAI guide: design-specs-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Write an approved change package into the canonical design specs and archive the package.

Promotion owns spec writes; verified work-spec known-difference cleanup is the exception. It
validates text and prepares destination links without changing prose, IDs, notes or drafts. Package
defects return to authoring; defects in the existing specs follow *Raising a Change Request*.

A spec promotes on the supervisor's approval. Promotion has no concern with any state outside the
package — not the implementation, not the design file beyond what `V5` verifies. Content rules and
the checks are in [`design-specs.md`](design-specs.md); typed formats in
[`design-specs-artifacts.md`](design-specs-artifacts.md).

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

Begin on explicit promotion intent — "promote the specs", "promote this package" — including after
authoring completes; authoring never runs into promotion on its own.

The package is the one named or already in context; sibling types and promoted history are not
targets. Before a fresh readiness screen, inspect existing promotion Evidence: a recorded `C3` write with confirmation or
repair pending resumes `C3` in place — retain `C1`–`C2`, repair and verify the output without
rewording, then check `C3` and archive. Changed drafts, intervening canon or uncertain outcomes
block reconciliation; never assume an unrecorded write succeeded. `C3` checked means the specs are
written: an incomplete archive resumes *Archive the Package* from wherever the package is. A fully
archived package is not promoted again.

Before a canonical write, ensure `skai/promoted/<change-id>/design-specs/` is absent and identify
live references into the package from the specs and app repositories and from related packages or
work specs. Collisions or inaccessible required references block; never overwrite or merge a
destination.

### Readiness Screen

Before writing `## Promotion Checks`, verify the package is promotable at all:

1. Every `- [ ]` item in the authoring artifact's `## Discussion` is resolved.
2. Recompute the specs-to-drafts comparison against the current specs, by prose and resolved link
   targets. Every change has an item and every item still matches; a `move` item's text is identical
   at both ends. Otherwise return to authoring.
3. No change request in the package remains `Proposed`.
4. Every requirement the drafts cite is canonical. A link into an active requirements package's
   draft fails this until that requirement promotes; the package waits, with the standard blocked
   gate naming the requirement.

On failure, record the condition in `## Evidence`, not a checks section. Conditions 1–3 return the
package to authoring; condition 4 waits for the requirement's promotion.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order. Verify changed
content at its projected canonical location; unchanged content and unrelated defects in the
existing specs do not block. Known-difference notes are observations, not obligations or markers.

- `C1 Verification` — run `V1`–`V10` from [`design-specs.md`](design-specs.md) § Verification
  Checks over the changed items and every touched file as a whole, one evidence bracket per check.
  `V5` means opening the design file and finding each named state by its product-language name;
  unavailable access blocks rather than passes. Any failure returns the package to authoring.
- `C2 Prepare destination links` — prepare each file's reference definitions for its canonical
  location: draft targets in this package map to their destinations, including a cited requirement
  now canonical; untouched dependencies keep their targets; for each `move`, incoming links within
  the specs are repointed and references from outside the specs (work specs, packages) are
  annotated with the new location. Preserve prose, IDs, known-difference notes and target
  identities; leave the drafts unchanged. Record adjusted definitions, or that none needed it.
- `C3 Write the specs` — write the prepared whole files to the resolved specs root, creating it when
  absent and leaving files outside the package untouched. Confirm destination links reach their
  intended targets and no Discussion citations, checkboxes or `🟡` remain; only retirement marks and
  labeled known-difference notes sit beside the contract. Repair mechanical faults in place; never
  reword. Record the write outcome before confirmation, then extend the evidence with the
  confirmation result; check `C3` only after confirmation succeeds.
- `C4 Archive the package` — execute *Archive the Package* below. This terminal item completes
  promotion only after verified write and archival.

**Example** (LumenNotes, mid-execution — `C1` failed on `V5`, so nothing after it ran):

```markdown
## Promotion Checks

- [ ] C1 Verification
- [ ] C2 Prepare destination links
- [ ] C3 Write the specs
- [ ] C4 Archive the package

## Evidence

[evidence: C1/V1; UI-NOTES-01.02, UI-NOTES-02.02, UI-NOTES-05 read with citations deleted; each keeps a target, format or place]
[evidence: C1/V2; grep -nE 'red|blue|left|right|top|bottom|round|small|large' over the three touched files; 1 hit, "the button at the top left" in glossary `Profile button` — identifying relationship, allowed]
[evidence: C1/V3; grep -nE 'frame|variant|node|figma|iOS|Android|TipKit' over touched files; 1 hit, the known-difference note under UI-NOTES-03 — allowed there]
[evidence: C1/V4; 4 quoted strings, all formats or data]
[evidence: C1/V5; Production › Notes: `notes`, `notes — empty`, `notes — stale` found; `notes — acknowledged reminder` named by UI-NOTES-02.02 NOT FOUND on Production or any approved change page; FAILED]
```

## Evidence

`## Evidence` records the verification trail. One bracket per check — and one per `V` check within
`C1`:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
[evidence: C1/V<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Append re-runs under `### Run <n>`, preserving prior evidence. On failure, persist or link the full
output at a run-and-check-specific path so later runs cannot overwrite it; success needs `output`
only if persisted. Inspections name repeatable inputs and observations. Silence is not a pass:
unresolved paths fail; a genuinely empty subject needs a recorded reason. Compare IDs per rewritten
file and retired IDs specs-wide; strip path prefixes (`grep -rhoE`) before comparing IDs.

## Raising a Change Request

A contradiction or inconsistency in the existing specs needs a change request, not merely draft
edits. Promotion alone raises these: use [`design-specs-artifacts.md`](design-specs-artifacts.md),
link it under `## Change Requests`, and block if writing would leave the specs inconsistent.
Otherwise continue and check the passing check with its linked request; do not leave the artifact
denying a write it performed. Name any still-`Proposed` request at completion; its defect needs a
new package.

## Archive the Package

After verified `C3`, execute `C4`:

1. Move `skai/changes/<change-id>/design-specs/` intact to
   `skai/promoted/<change-id>/design-specs/` in the specs repository. Leave sibling types untouched;
   remove the active change-ID grouping directory only if empty.
2. Repair live incoming links across the resolved repositories, including related packages and work
   specs, and relative links inside the moved files, preserving target identities. Preserve prose,
   IDs, decisions and recorded commands and results; annotate historical paths with current
   locations. Inaccessible or unrepaired required links block.
3. Verify the archived files and links, the absence of the active type path and the preserved
   siblings; record move and link evidence, then check `C4` in the archived
   `design-specs-promotion.md`.

After a failure, report the specs promoted but archival incomplete and use the standard blocked
gate. Locate the package at its active or promoted path, verify identity and evidence, and resume
only the unfinished archival; never overwrite a destination or repeat `C3` to finish `C4`.

## Completion

`C3` plus `C4` with evidence means the specs are written and the package is archived at
`skai/promoted/<change-id>/design-specs/`. Link its artifact and emit
`🏁 Complete. Let me know if anything needs adjustment.`

`C3` alone closes the proposal to authoring; missing archival evidence
needs archival recovery. Promoted drafts are not reopened or re-promoted. Name any still-`Proposed`
request with its archived link; its defect goes to a new scoped-change package.

## Cross-References

- [`design-specs.md`](design-specs.md) — content rules and the verification checks
- [`design-specs-artifacts.md`](design-specs-artifacts.md) — change item and change request formats
- [`design-specs-authoring.md`](design-specs-authoring.md) — the authoring workflow

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-promotion-addendum.md` exists, read it and immediately print
`- 📎 Addendum loaded` as a line of its own, nested under this guide's line; its rules are part of this
guide and win any conflict.
