Managed-By: skai
Managed-Id: guide.product-specs-promotion
Managed-Source: Guides/ProductSpecs/product-specs-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Product Specs Promotion

Print `📖 SKAI guide: product-specs-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Fold the approved package into its **base** per [`change-requests.md`](../Core/change-requests.md). Only promotion writes contracts except verified
work-spec known-difference cleanup. Validate text, prepare destination links and preserve prose,
IDs, notes and drafts. Return package wording defects to authoring; base defects start a package against it.

In chat, link requirement and Discussion IDs to their exact targets (real anchors or verified file/line links).

Content: [`product-specs-catalog.md`](product-specs-catalog.md). Package, items, review: [`product-specs-artifacts.md`](product-specs-artifacts.md). File shape/tool:
[`spec-file-shape.md`](../Core/spec-file-shape.md).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## When promotion happens

Into production, promote supervisor-approved shipping behavior and approved intended behavior with
confirmed known-difference notes naming affected implementations. Other future behavior waits for shipment.

## The promotion artifact

Write `product-specs-promotion.md` beside the authoring artifact:

```
# Product Specs Promotion — <name>
[Review page](product-specs-review.html)
## Inputs               the package being promoted; its base
## Promotion Checks     - [ ] C<n> items, unchecked until executed
## Evidence             the verification trail
```

## Gates

When waiting on the supervisor, end the message with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is a human or authorized agent outside this workflow who resolves its discussion items and reviews its gates; the executing agent cannot resolve or approve its own.

**Gate persistence.** After emitting a `⏳ GATE:` line, end every response — including discussion, clarifications and refinements — with that line verbatim until the gate moves. Change it only when its content changes (e.g., a blocker emerges or `Next` needs revision); then emit the new line in full at the response's end. Never paraphrase, shorten or silently change it.

**No fabricated gates.** Use `⏳ GATE:` only at gates this `## Gates` section defines or a properly emitted blocked gate. Never invent categories or labels for discussion state, partial completion or intermediate review. If a needed gate is undefined here, file the missing gate as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are this workflow's expected review points. At each:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the supervisor.

In a planned gate, `<what happens after your response>` describes the agent's action after supervisor advance intent. For a non-standard gate, describe the exact supervisor response or handoff needed to resume.

For an unexpected blocker, use the blocked gate line and STOP until the supervisor resolves it.

Workflow-specific gate notes:
- Promotion Checks is the sole review, after readiness and before the base changes. `next` executes checks, writes the base and archives the package. Summarize destination
  files and **every requirement in those whole-file writes**, carried-forward ones included, not the checklist or item count.
  - `⏳ GATE: Next: Write <N> requirements into <paths>. Say "next" or what to change.`

Workflow-specific blocked gates:
- A readiness failure, a `C1`–`C5` failure or requested draft edits return the package to
  authoring; record the cause; use:
  `⏳ GATE: Blocked: <what failed, in words> (<C# | readiness condition | requested wording>). I am reopening the package to fix it, then promotion runs again.`
- A base contradiction that would make the write inconsistent takes the standard blocked gate; a package against the base fixes it.
- An archive collision, inaccessible references or an archival failure use the standard blocked
  gate; recovery follows *Archive the package*.

## Advance intent

Advance intent passes the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- It approves passing a gate only after you emit a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the active-phase rules below; never skip phases or clear unrelated progress markers.

`auto` is advance intent bypassing planned gates only; blocked gates require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestone in this workflow: `promotion checks`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs): check completed items, preserving their audit trail.
  - **`🟡` in source files** seeded or planned by a skai workflow: **remove** on completion.
- By default, markers mean TODO or pending approval; clearing them requires supervisor approval.
- At a planned gate, stop and wait. Supervisor advance intent then approves clearing guide-owned markers completed by the preceding phase.

**Workflow-specific marker lifecycle.** This workflow owns `- [ ] C<n>` items in `## Promotion Checks`.
For fresh or changed-draft runs, write every `C<n>` unchecked for review. After advance intent,
execute in order, record evidence and check successes. Package failures in `C1`–`C5` leave that check
and later items unchecked; repair mechanical faults after `C7`'s write in place, never reword.
Canon carries no markers.

After draft changes, reset all checks, keep prior evidence under `### Run <n>` and restart at `C1`. Archival-only recovery retains `C1`–`C7` and their evidence; never repeat a successful write
to finish `C8`.

**Workflow-specific `auto` behavior.** `auto` skips the review only for already-reviewed drafts;
verification failures and the other blockers still stop it.

## Initiation

Begin only on explicit promotion intent, never automatically after authoring. Git handling after
the write is the supervisor's.

Use the named or contextual package, never siblings or promoted history. Before fresh readiness,
inspect promotion Evidence. Resume recorded `C7` writes awaiting confirmation/repair in place, even
unchecked: retain `C1`–`C6`, repair/verify without rewording, check `C7`, archive. Draft changes,
intervening base edits or uncertain outcomes block; never assume unrecorded writes. Checked `C7`
resumes archival only, from the active or promoted location. Never re-promote archived packages.

Before writing, require an absent promoted path (`skai/promoted/<change-id>/product-specs/`, or
`<base>/promoted-change-requests/<nnn>/`); find live incoming references from catalog/app repositories,
related packages and work specs. Collisions or inaccessible required references block; never
overwrite or merge destinations.

### Readiness screen

First run `validate <catalog root> <drafts>`, `check-changes` and `render` for a current review page;
then verify before writing `## Promotion Checks`:

1. Into production: no open `- [ ]` item in `## Discussion`, gap
   ([`known-gaps.md`](../Core/known-gaps.md)) or request under the package. Into a package, `C7` carries them.
2. `validate` reports no fault in a file the package holds and no conflict the projection
   introduces; a fault already in an untouched base file never blocks: start a package against the base.
3. `check-changes` passes: every change has a `## Requirement Changes` entry or Touches line at the
   artifacts guide's grain, with the right operation; no entry names an unchanged or absent target.
4. Every modified or retired ID or glossary entry has its sweep under `## Verification`.
5. Apply the outcome of every request this package filed against an input ([`change-requests.md`](../Core/change-requests.md)), now and at the base write.

Record failures in `## Evidence`, not a checks section, and return to authoring.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

Verify changed content at its projected base location; unchanged content never blocks. Use readiness output as evidence for tool-covered checks; inspect the rest.

- `C1 IDs are append-only` — every rewritten-file ID remains in its draft, heading its base promise.
  `validate` names duplicate or revived IDs; `check-changes` names items missing without retire
  entries. Inspect that all IDs remain, none renumbered (two live promises exchanging IDs pass both).
  Whole-file drafting carries non-ID content forward; no separate check.
- `C2 Prefixes do not collide` — no prefix introduced here is claimed by another file in the
  base or this package, and every prefix is recorded on its file's index line (`validate`
  checks only the line's shape).
- `C3 Cross-references resolve` — `validate` has every link defined and used. Inspect citations in
  changed requirements, indexes, glossary entries and known-difference notes: they reach intended IDs
  at projected locations (including untouched dependencies), not merely files; tracking links identify issues.
- `C4 Writing style` — inspect changed requirement and glossary prose against the catalog guide's
  writing rules and the writing guide; known-difference notes are not the contract; index lines and headers are `C5`'s.
- `C5 Traversal` — index lines name the questions their files answer; every cross-cutting term
  introduced here has a glossary entry pointing at the requirements that govern it, and `validate`
  has every term linked; no behavioral claim sits in unnumbered prose.
- `C6 Prepare destination links` — map draft targets to base destinations in each file's reference
  definitions; untouched dependencies keep their targets. Preserve prose, IDs, notes, target identities
  and drafts. Record adjusted definitions or that none needed it.
- `C7 Write the base` — recheck conditions 1 and 5; write prepared whole files to the base,
  creating the root and files if absent; leave other files untouched. Into production: confirm
  destination links, no Discussion citations, checkboxes or `🟡`, and only retirement marks and
  known-difference notes beside contracts; read back and run `validate <catalog root>` (a fault
  readiness missed is `C7`'s, wherever reported). Keep the approved diff; do not render after
  writing. Into a package: replace its drafts; append entries to its `## Requirement Changes`
  with its next `R` numbers, each Justification ending `; Change request: <nnn> R<n>`; carry open work and
  name the request in `## Assumptions and TODOs` as the shared guide says; validate and
  render the base, whose author reconciles its list on reopen. Repair mechanically, never reword; record the write outcome,
  then confirmation/repair results, keeping failures. Check `C7` only on confirmed success, then archive.
- `C8 Archive the package` — *Archive the package* below; promotion completes only after verified
  write and archival.

**Example** (`C4` failed: `C1`–`C3` checked, `C4`–`C8` unchecked):

```markdown
## Evidence

[evidence: C1; the 9 requirements each head their own promise, none renumbered; check-changes and validate over the projection: 0 issues, 1 note outside it]
[evidence: C2; both touched files are already listed in features/_features.md, none new; the prefix on each line]
[evidence: C3; every citation reaches the ID it means; validate: every link defined and used; the 6 citations in REMIND-04/06/09; expiry-fix names its issue]
[evidence: C4; REMIND-04/06/09 and glossary `Expiry window` against the writing rules; FAILED: REMIND-06 says how the timer is implemented, not what the user sees; output: skai/changes/reminder-expiry/product-specs/evidence/promotion-run1-c4.md]
```

## Evidence

One bracket per check:

```
[evidence: C<n>; <the result, in words>; <command or inspection>; output: <path when persisted>]
```

The result leads; then the repeatable inputs and what was found or changed:

```
[evidence: C5; index and glossary route to the right requirements: features/_features.md names expiry/dismissal; Pending reminder/Expiry window point to REMIND-04/09; validate: every term linked; no unnumbered behavioral claims]
[evidence: C6; NOTE-04's link now points at its base location with the same target: ../domains/note.md#note-04; notes retained]
[evidence: C7; 9 requirements written to features/reminders.md, features/_features.md, glossary.md, clean of markers and Discussion citations (grep -E '\[D[0-9]+\]|- \[[ x]\]|🟡': nothing); destination links resolve; REMIND-07 retirement and notes retained; validate skai/product-specs: nothing beyond readiness's 1 note]
```

Persist/link full failure output at unique run/check paths; never overwrite it in later runs.
Use `output` on success only if persisted. Silence never passes: unresolved paths fail; explain empty subjects.

## Archive the package

After verified `C7`, execute `C8`:

1. Move the package intact (pages, `working-docs/`, `change-requests/`,
   `promoted-change-requests/`): `skai/changes/<change-id>/product-specs/` to
   `skai/promoted/<change-id>/product-specs/` in the catalog repository; a request to
   `<base>/promoted-change-requests/<nnn>/`. Leave siblings; remove only empty grouping directories.
2. Repair live incoming links across those repositories, related packages and work specs, and
   relative links inside moved files, preserving target identities, prose, IDs, decisions and
   recorded results; annotate historical paths with current locations. Inaccessible or unrepaired
   required links block.
3. Verify archived files/links, absence of the active type path and preserved siblings; record move
   and link evidence, then check `C8` in the archived `product-specs-promotion.md`.

On failure, report the specs written but package not yet archived at the standard blocked gate;
resume archival only at either package path, never overwriting a destination or repeating `C7`.

**Example** — `reminder-expiry/ui-map/` stays active and its incoming links are repaired:

```text
[evidence: C8; moved skai/changes/reminder-expiry/product-specs/ to skai/promoted/reminder-expiry/product-specs/; active path absent; archived files and live link targets verified; ui-map sibling preserved]
```

## Completion

With `C7` and `C8` evidenced, link the archived artifact and emit
`🏁 Complete. Let me know if anything needs adjustment.`

`C7` alone closes the proposal to authoring; a migrated historical `C7`-only package needs its
separately recorded relocation instead of `C8`. Promoted drafts are never reopened or re-promoted.

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
