Managed-By: skai
Managed-Id: guide.requirements-promotion
Managed-Source: Guides/Requirements/requirements-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-13

# Requirements Promotion

Before using this guide, complete [Project addendum](#project-addendum) loading below.

## Purpose

Write an approved change package into the canonical catalog.

Promotion owns contract writes; verified work-spec known-difference cleanup is the exception.
Validate text and prepare destination links without changing prose, IDs, notes or drafts.
Package wording defects return to authoring; catalog defects follow *Raising a change request*.

In conversation, link requirement and Discussion IDs to the exact draft or canonical target using
inline links. Prefer real anchors; Discussion checkbox IDs require a supported explicit anchor or
a topic anchor with item context, or a verified file/line link supported by the host.

Use [`requirements-catalog.md`](requirements-catalog.md) for content rules and
[`requirements-artifacts.md`](requirements-artifacts.md) for typed formats.

## When promotion happens

Promote shipping behavior on supervisor approval. Approved intended behavior may also promote with
confirmed known-difference notes identifying the affected implementations. Other future behavior waits
until shipment. This depends on the behavior, not Baseline versus Scoped change mode.

## The promotion artifact

Promotion writes `skai/changes/<change-id>/requirements/requirements-promotion.md`, parallel to the authoring
artifact:

```
# Requirements Promotion — <name>
## Inputs               the package being promoted; the catalog it targets
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
- Promotion Checks is the single review point: after readiness and the unchecked checklist, before
  canon changes. `next` executes checks, writes canon and archives the package. Summarize the
  destination files and **all requirements in those whole-file writes**, including carried-forward
  requirements, not the checklist or change-item count. Requested draft edits return to authoring.
  - `⏳ GATE: Next: Promote <N> requirements to <paths>. Say "next" or what to change.`

Workflow-specific blocked gates:
- Readiness failure, package verification failure (`C1`–`C5`), requested draft edits, or a catalog
  contradiction making the write inconsistent return to authoring. Record the cause and use:
  `⏳ GATE: Blocked: <C# | readiness condition | requested wording | catalog contradiction> failed — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- Archive collision, inaccessible references or archival failure use the standard blocked gate. Mechanical post-write C7 faults are repaired in place, without rewording;
  archival recovery follows *Archive the package*.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestones in this workflow: `promotion checks`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs: work specs, planning docs, working docs, retro outputs, ticket drafts, etc.). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** (test code, application code) seeded or planned by a skai workflow. Completion is **removal** of the marker — the file's remaining work is read by which `🟡`s remain. Canonical in-code case: `Guides/Test/unit-test-planning-guide.md`.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers (`- [ ]` → `- [x]` in a process artifact; remove `🟡` in code) only after the supervisor gives advance intent.
- If a workflow needs a custom marker lifecycle (for example, inline discussion items resolved during a supervisor-led discussion loop), define that exception explicitly and narrowly below.
- If a workflow uses both gate/phase markers and local working markers, keep them distinct: local approvals clear local working markers; advance intent clears the gate/phase marker.
- For any custom marker lifecycle, specify both:
  - the artifact where the markers live
  - the exact supervisor intent that authorizes clearing them

**Not workflow progress:** the `🟡` convention in `Templates/docs/skai/integration.md` and `Install/integration-doc-install-update.md` (project-specific missing constants needing supervisor input during host install) is a separate concept, scoped to that section's rules. Don't conflate the two.

**Workflow-specific marker lifecycle.** For a fresh or changed-draft run, write every `C<n>` unchecked for review. After advance
intent, execute in order, record evidence and check each success. A package failure in C1–C5 leaves
that check and later items unchecked; a mechanical fault after C7's write is repaired in place,
never reworded. Record writes honestly; prose defects return to authoring. Canon carries no markers.

After changed drafts, reset all checks, retain prior evidence and restart at C1. Archival-only
recovery is separate: retain C1–C7 and their evidence; never repeat a successful write just to finish
C8. Check C8 only after the move, link repair and archived verification succeed.

`auto` skips review only for already-reviewed drafts; verification and other blockers still stop it.

## Initiation

Begin on explicit promotion intent, including after authoring completes; authoring does not run into
promotion automatically. Git handling after the write belongs to the supervisor.

The package is the one named or already in context; sibling types and promoted history are not
targets. Before fresh readiness, inspect existing promotion Evidence. A recorded C7 write with mechanical
confirmation/repair pending resumes C7 in place, even unchecked: retain C1–C6, repair/verify output
without rewording, then check C7 and archive. Changed drafts, intervening canon or uncertain outcomes
block reconciliation; do not reset execution or assume an unrecorded write succeeded. C7
checked means canon is written: an incomplete archive resumes *Archive the package* from its active
or promoted location, without resetting checks. A fully archived package is not promoted again.

Before a canonical write, ensure `skai/promoted/<change-id>/requirements/` is absent and identify live
references in the catalog/app repositories and resolved repositories of linked related packages or callers. Collisions or inaccessible required references block;
never overwrite or merge a destination.

### Readiness screen

Before writing `## Promotion Checks`, verify the package is promotable at all:

1. Every `- [ ]` item in the authoring artifact's `## Discussion` is resolved.
2. Recompute the catalog-to-drafts comparison against the current catalog using prose and resolved
   link targets. Ignore only location-required relative-path changes; added/removed citations and
   changed targets still count. Every change has an item and every item still matches; otherwise
   return to authoring.
3. No change request in the package remains `Proposed`.

On failure, record the condition in `## Evidence`, not a checks section, and return to authoring.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

Verify changed content at its projected canonical location; unchanged content and unrelated catalog
defects do not block. Known-difference notes are observations, not obligations or markers.

- `C1 IDs are append-only` — every ID in a rewritten catalog file remains in its draft, with no
  renumbering or retired-ID reuse. Non-ID content is carried forward by whole-file drafting, not an
  additional check here.
- `C2 Prefixes do not collide` — no prefix introduced here is already claimed by another file in the catalog or this package, and
  every prefix is recorded on its file's line in the scope index.
- `C3 Cross-references resolve` — citations in changed requirements, indexes, glossary entries and
  known-difference notes use reference-style links with defined targets. Verify relative paths and
  actual anchors against the projected catalog, including untouched dependencies; requirement links
  must reach the intended ID, not merely an existing file. Confirm tracking links identify their issue.
- `C4 Writing style` — inspect changed requirement/glossary prose against the catalog guide's full
  Required, Forbidden, and Nothing that decays rules, not its drafting Self-check. Distinguish labeled
  known-difference observations from the contract. Structural index lines and orientation headers
  belong to C5, not this style check.
- `C5 Traversal` — catalog lines name the questions their files answer; every cross-cutting term
  introduced here has a glossary entry pointing at the requirements that govern it; no behavioral
  claim sits in unnumbered prose.
- `C6 Prepare destination links` — prepare each file's reference definitions for its canonical
  location. Draft targets in this package map to their canonical destinations; untouched dependencies
  retain their catalog targets. Preserve prose, IDs, known-difference notes and target identities;
  leave package drafts unchanged. Record adjusted definitions, or that none needed adjustment.
- `C7 Write the catalog` — write the prepared whole files to the resolved catalog root, creating it
  when absent and leaving files outside the package untouched. Confirm destination links reach their
  intended targets and no Discussion citations, checkboxes, or `🟡` remain. Only retirement marks and
  labeled known-difference observations are allowed alongside the contract. Repair mechanical output
  faults in place; never reword. Record the actual write outcome before output confirmation; extend that C7 evidence with confirmation/repair results, retaining failures. Check C7 only after confirmation succeeds, then archive.
- `C8 Archive the package` — execute *Archive the package* below. This terminal item completes
  promotion only after verified write and archival.

**Example** (LumenNotes, mid-execution — `C4` failed, so `C5` onward were not run):

```markdown
## Promotion Checks

- [x] C1 IDs are append-only
- [x] C2 Prefixes do not collide
- [x] C3 Cross-references resolve
- [ ] C4 Writing style
- [ ] C5 Traversal
- [ ] C6 Prepare destination links
- [ ] C7 Write the catalog
- [ ] C8 Archive the package

## Evidence

[evidence: C1; comm -23 <(grep -ohE '^## [A-Z-]+-[0-9]+' skai/requirements/features/reminders.md | sed 's/^## //' | sort -u) <(grep -ohE '^## [A-Z-]+-[0-9]+' skai/changes/reminder-expiry/requirements/proposed-requirements/features/reminders.md | sed 's/^## //' | sort -u); comm -12 <(grep -rhoE '^## [A-Z-]+-[0-9]+ \(retired\)' skai/requirements/ | grep -oE '[A-Z-]+-[0-9]+' | sort -u) <(grep -rhoE '^## [A-Z-]+-[0-9]+$' skai/changes/reminder-expiry/requirements/proposed-requirements/ | grep -oE '[A-Z-]+-[0-9]+' | sort -u); no ID dropped, none renumbered, no retired ID reused]
[evidence: C2; inspection of the prefix on each touched file's line in features/_features.md; both present, no new prefix introduced]
[evidence: C3; every ID this package's new and changed text cites, resolved against the catalog plus the drafts; 0 unresolved]
[evidence: C4; writing-style check over the changed requirements REMIND-04, REMIND-06, REMIND-09, against Required, Forbidden and Nothing that decays in full; FAILED on REMIND-06; output: skai/changes/reminder-expiry/requirements/evidence/promotion-run1-c4.md]
```

## Evidence

`## Evidence` records the verification trail. One bracket per check:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Name check/outcome; append re-runs under `### Run <n>`, preserving prior evidence.

Inspection and preparation results name what was checked or changed:

```
[evidence: C4; REMIND-04/06/09 and glossary `Expiry window` against Required, Forbidden and Nothing that decays; no mechanisms or temporal references; all describe behavior]
[evidence: C5; features/_features.md names expiry/dismissal; glossary Pending reminder/Expiry window point to REMIND-04/09; no unnumbered behavioral claims in the three written files]
[evidence: C6; NOTE-04 definition rebased from the draft location to ../domains/note.md#note-04; canonical target identity unchanged; known-difference notes retained]
[evidence: C7; wrote features/reminders.md, features/_features.md, glossary.md; 9 requirements landed; grep -E '\(D[0-9]+\)|- \[[ x]\]|🟡' skai/requirements/features/reminders.md skai/requirements/features/_features.md skai/requirements/glossary.md returned nothing; inspection — destination links resolve; REMIND-07 retirement and labeled known-difference notes retained]
```

On failure, persist/link full output at a run-and-check-specific path so later runs cannot overwrite
retained evidence; success needs `output` only if persisted. Inspections name repeatable inputs and
observations. Silence is not a pass: unresolved paths fail; genuinely empty subjects need a recorded
reason. Compare IDs per rewritten file and retired IDs catalog-wide; strip path prefixes
(`grep -rhoE`) before comparing IDs.

## Raising a change request

A contradiction or inconsistency in existing canon needs a change request, not merely draft edits.
Promotion alone raises these: use [`requirements-artifacts.md`](requirements-artifacts.md), link it
under `## Change Requests`, and block if writing would leave canon inconsistent. Otherwise continue
and check the passing check with its linked request; do not leave the artifact denying a write it
performed. Name any still-Proposed request at completion; its catalog defect needs a new package.

## Archive the package

After verified C7, execute C8:

1. Move `skai/changes/<change-id>/requirements/` intact to
   `skai/promoted/<change-id>/requirements/` in the catalog repository. Leave sibling types untouched;
   remove the active change-ID grouping directory only if empty.
2. Repair live incoming links across those resolved repositories, including related packages/work specs,
   and relative links inside moved files, preserving target identities. Preserve prose, IDs, decisions
   and recorded commands/results; annotate historical paths with current locations. Inaccessible or
   unrepaired required links block.
3. Verify archived files/links, absence of the active type path and preserved siblings; record move
   and link evidence, then check C8 in the archived `requirements-promotion.md`.

After a failure, report canon promoted but archival incomplete and use the standard blocked gate.
Locate the same package at its active/promoted path, verify identity/evidence, and resume unfinished
archival only; never overwrite a destination or repeat C7 solely to finish C8.

**Example:** archive `reminder-expiry/requirements/` while `reminder-expiry/ui-map/` remains active;
repair that sibling's incoming links. Then record and check C8 at the promoted location:

```text
[evidence: C8; moved skai/changes/reminder-expiry/requirements/ to skai/promoted/reminder-expiry/requirements/; active requirements path absent; archived files and live link targets verified; active ui-map sibling preserved]
```

## Completion

C7 plus C8 with evidence means canon is written and the package is archived at
`skai/promoted/<change-id>/requirements/`. Link its artifact and emit
`🏁 Complete. Let me know if anything needs adjustment.`

C7 alone closes the proposal to authoring. Newly produced packages
need C8; migrated historical C7-only packages instead require their separately recorded, verified
relocation. Missing completion evidence for the applicable case needs archival recovery. Promoted drafts are not reopened or re-promoted. Name any still-Proposed request
with its archived link; resolve that catalog defect through a new scoped-change package.

## Cross-references

- [`requirements-catalog.md`](requirements-catalog.md) — catalog content rules
- [`requirements-authoring.md`](requirements-authoring.md) — the authoring workflow
- [`requirements-artifacts.md`](requirements-artifacts.md) — change item and change request formats

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/requirements-promotion-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Once the lookup is done
and before work, report `- 📖 SKAI guide: requirements-promotion`, nesting `- 📎 Addendum loaded` under it only if one
loaded. If the lookup fails, nest `- ⛔ Addendum lookup failed: <what failed>` and stop. Report each guide
once per task; one addendum line covers referenced documents. Not a gate; keep GATE lines last.
