Managed-By: skai
Managed-Id: guide.product-specs-promotion
Managed-Source: Guides/ProductSpecs/product-specs-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-19

# Product Specs Promotion

Print `📖 SKAI guide: product-specs-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Write an approved change package into the product specs.

Promotion owns contract writes; verified work-spec known-difference cleanup is the exception.
Validate text and prepare destination links without changing prose, IDs, notes or drafts.
Package wording defects return to authoring; defects in the existing product specs follow
*Raising a change request*.

In conversation, link requirement and Discussion IDs inline to their exact targets, by real
anchors or verified file/line links.

Content rules: [`product-specs-catalog.md`](product-specs-catalog.md). The package, change items,
change requests and review page: [`product-specs-artifacts.md`](product-specs-artifacts.md). File
shape and the spec tool: [`spec-file-shape.md`](../Core/spec-file-shape.md).

## When promotion happens

Promote shipping behavior on supervisor approval, and approved intended behavior whose confirmed
known-difference notes name the affected implementations. Other future behavior waits until
shipment.

## The promotion artifact

Promotion writes `skai/changes/<change-id>/product-specs/product-specs-promotion.md` beside the
authoring artifact:

```
# Product Specs Promotion — <name>
[Review page](product-specs-review.html)
## Inputs               the package being promoted; the product specs it targets
## Promotion Checks     - [ ] C<n> items, unchecked until executed
## Change Requests      links to any request this run filed; may be absent
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
- Promotion Checks is the single review point: after readiness and the unchecked checklist, before
  canon changes. `next` executes the checks, writes canon and archives the package. Summarize the
  destination files and **every requirement in those whole-file writes**, carried-forward ones
  included, not the checklist or change-item count.
  - `⏳ GATE: Next: Promote <N> requirements to <paths>. Say "next" or what to change.`

Workflow-specific blocked gates:
- A readiness failure, a `C1`–`C5` failure, requested draft edits, or a contradiction in the
  product specs that would make the write inconsistent return the package to authoring. Record the
  cause and use:
  `⏳ GATE: Blocked: <C# | readiness condition | requested wording | catalog contradiction> failed — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- An archive collision, inaccessible references or an archival failure use the standard blocked
  gate; recovery follows *Archive the package*.

## Advance intent

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
After advance intent, execute in order, record evidence and check each success. A package failure
in `C1`–`C5` leaves that check and later items unchecked; a mechanical fault after `C7`'s write is
repaired in place, never reworded. Canon carries no markers.

After changed drafts, reset all checks, retain prior evidence under `### Run <n>` and restart at
`C1`. Archival-only recovery retains `C1`–`C7` and their evidence; never repeat a successful write
to finish `C8`.

**Workflow-specific `auto` behavior.** `auto` skips the review only for already-reviewed drafts;
verification failures and the other blockers still stop it.

## Initiation

Begin only on explicit promotion intent, never automatically after authoring. Git handling after
the write is the supervisor's.

The package is the one named or already in context, never its siblings or promoted history.
Before fresh readiness, inspect existing promotion Evidence. A recorded `C7` write awaiting
confirmation/repair resumes `C7` in place, even unchecked: retain `C1`–`C6`, repair/verify without
rewording, check `C7`, archive. Changed drafts, intervening canon or uncertain outcomes block; never
assume an unrecorded write. Checked `C7` resumes incomplete archival only, from the active or
promoted location. An archived package is never re-promoted.

Before a canonical write, ensure `skai/promoted/<change-id>/product-specs/` is absent and identify
live incoming references from the catalog/app repositories, related packages and work specs; a
collision or an inaccessible required reference blocks; never overwrite or merge a destination.

### Readiness screen

Run `validate <catalog root> <drafts>`, `check-changes` and `render` first, so the supervisor
reviews the current page, then verify before writing `## Promotion Checks`:

1. Every `- [ ]` item in the authoring artifact's `## Discussion` is resolved.
2. `validate` reports no fault in a file the package holds and no conflict the projection
   introduces; a fault it notes in an untouched canonical file never blocks and becomes a change
   request (*Raising a change request*).
3. `check-changes` passes: every change has a `## Requirement Changes` entry, or rides in one's
   Touches, at the artifacts guide's granularity, with the right operation; no entry names an
   unchanged or absent target.
4. Every modified or retired ID or glossary entry has its sweep under the authoring artifact's
   `## Verification`.
5. No request remains `Proposed`, except one this run filed under *Raising a change request*;
   this still holds when the write begins.

On failure, record the condition in `## Evidence`, not a checks section, and return to authoring.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

Verify changed content at its projected canonical location; unchanged content and untouched
canonical files do not block. Where the tool covers a check, its readiness output is the evidence;
the rest is inspection.

- `C1 IDs are append-only` — every ID in a rewritten file remains in its draft, heading the promise
  it headed in canon: `check-changes` names any item missing from a draft, `validate` any
  duplicate or revived ID; inspect that none is renumbered (two live promises exchanging IDs pass
  both). Whole-file drafting carries non-ID content forward; no separate check.
- `C2 Prefixes do not collide` — no prefix introduced here is claimed by another file in the
  product specs or this package, and every prefix is recorded on its file's index line (`validate`
  checks only the line's shape).
- `C3 Cross-references resolve` — `validate` has every link defined and used; inspect that citations
  in changed requirements, indexes, glossary entries and known-difference notes reach the intended
  ID at its projected location (untouched dependencies included), not merely a file, and that
  tracking links identify their issue.
- `C4 Writing style` — inspect changed requirement and glossary prose against the catalog guide's
  Required, Forbidden and Nothing that decays rules in full; known-difference
  notes are not the contract; index lines and orientation headers are `C5`'s.
- `C5 Traversal` — index lines name the questions their files answer; every cross-cutting term
  introduced here has a glossary entry pointing at the requirements that govern it, and `validate`
  has every term linked; no behavioral claim sits in unnumbered prose.
- `C6 Prepare destination links` — prepare each file's reference definitions for its canonical
  location: package draft targets map to their canonical destinations; untouched dependencies keep
  their catalog targets. Preserve prose, IDs, notes and target identities; leave the drafts
  unchanged. Record adjusted definitions, or that none needed it.
- `C7 Write the catalog` — condition 5 still holding by current statuses, write the
  prepared whole files to the resolved catalog root, creating it
  when absent, leaving files outside the package untouched. Confirm destination links reach their
  targets and no Discussion citations, checkboxes or `🟡` remain; only retirement marks and
  known-difference notes accompany the contract: read the written text back and run
  `validate <catalog root>` (a fault readiness did not note is `C7`'s, wherever reported). No
  render after the write: the page keeps the approved diff. Repair mechanical faults in place,
  never reword; record the write outcome, then the confirmation/repair results, retaining
  failures. Check `C7` only after confirmation succeeds, then archive.
- `C8 Archive the package` — *Archive the package* below; promotion completes only after verified
  write and archival.

**Example** (`C4` failed: `C1`–`C3` checked, `C4`–`C8` unchecked):

```markdown
## Evidence

[evidence: C1; check-changes and validate over skai/product-specs + skai/changes/reminder-expiry/product-specs/proposed-product-specs: 0 issues, 1 note outside the projection; inspection: each of the 9 IDs heads its canonical promise, none renumbered]
[evidence: C2; the prefix on each touched file's line in features/_features.md; both present, none new]
[evidence: C3; validate: every link defined and used; the 6 citations in REMIND-04/06/09 reach their intended IDs; expiry-fix names its issue]
[evidence: C4; REMIND-04/06/09 and glossary `Expiry window` against Required, Forbidden and Nothing that decays in full; FAILED on REMIND-06; output: skai/changes/reminder-expiry/product-specs/evidence/promotion-run1-c4.md]
```

## Evidence

One bracket per check:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Inspections name repeatable inputs and what was found or changed:

```
[evidence: C5; features/_features.md names expiry/dismissal; glossary Pending reminder/Expiry window point to REMIND-04/09; validate: every term linked; no unnumbered behavioral claims]
[evidence: C6; NOTE-04 definition rebased from the draft location to ../domains/note.md#note-04; target identity unchanged; notes retained]
[evidence: C7; wrote features/reminders.md, features/_features.md, glossary.md; 9 requirements landed; grep -E '\[D[0-9]+\]|- \[[ x]\]|🟡' over them returned nothing; destination links resolve; REMIND-07 retirement and notes retained; validate skai/product-specs: nothing beyond readiness's 1 note]
```

Persist/link full failure output at a run-and-check-specific path, never overwritten by a later
run; `output` on success only if persisted. Silence is not a pass: unresolved paths fail; an empty
subject records why.

## Raising a change request

A contradiction or inconsistency in the existing product specs — a fault `validate` notes in an
untouched file included — needs a change request, not draft edits. File it in this package's
`change-requests/<nnn>/` as [`product-specs-artifacts.md`](product-specs-artifacts.md) § Change
Requests says, link it under `## Change Requests`, and block only if the write itself would
contradict canon. Otherwise continue and check the passing check with its linked request.
A request filed here rides to completion still `Proposed`.

## Archive the package

After verified `C7`, execute `C8`:

1. Move `skai/changes/<change-id>/product-specs/` intact, rendered pages included, to
   `skai/promoted/<change-id>/product-specs/` in the catalog repository. Leave sibling types
   untouched; remove the active change-ID grouping directory only if empty.
2. Repair live incoming links across those repositories, related packages and work specs, and
   relative links inside moved files, preserving target identities, prose, IDs, decisions and
   recorded results; annotate historical paths with current locations. Inaccessible or unrepaired
   required links block.
3. Verify archived files/links, absence of the active type path and preserved siblings; record move
   and link evidence, then check `C8` in the archived `product-specs-promotion.md`.

After a failure, report canon promoted but archival incomplete and use the standard blocked gate;
resume unfinished archival only, at either package path, never overwriting a destination or
repeating `C7`.

**Example** — `reminder-expiry/ui-map/` stays active and its incoming links are repaired:

```text
[evidence: C8; moved skai/changes/reminder-expiry/product-specs/ to skai/promoted/reminder-expiry/product-specs/; active path absent; archived files and live link targets verified; ui-map sibling preserved]
```

## Completion

`C7` plus `C8` with evidence means canon is written and the package is archived at
`skai/promoted/<change-id>/product-specs/`. Link its artifact and emit
`🏁 Complete. Let me know if anything needs adjustment.`

`C7` alone closes the proposal to authoring; a migrated historical `C7`-only package needs its
separately recorded relocation instead of `C8`. Promoted drafts are never reopened or re-promoted.
Name any still-Proposed request with its archived link.

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
