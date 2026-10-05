Managed-By: skai
Managed-Id: guide.requirements-promotion
Managed-Source: Guides/Requirements/requirements-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-05

# Requirements Promotion

## Purpose

Write an approved change package into the canonical catalog.

Promotion writes requirement contracts into the catalog; work-spec implementation's verified
known-difference cleanup is the narrow exception. Promotion validates the text and adjusts link
definitions for the destination, without changing prose, IDs, or notes. A wording change belongs to
authoring: a package defect returns there, while a catalog defect follows *Raising a change request*.

In conversation, link requirement and Discussion IDs to the exact draft or canonical target using
inline links. Prefer real anchors; Discussion checkbox IDs require a supported explicit anchor or
a topic anchor with item context, or a verified file/line link supported by the host.

Content rules live in [`requirements-catalog.md`](requirements-catalog.md); the package's typed
formats live in [`requirements-artifacts.md`](requirements-artifacts.md).

## When promotion happens

Promote shipping behavior on supervisor approval. Approved intended behavior may also promote with
confirmed known-difference notes identifying the affected implementations. Other future behavior waits
until shipment. This depends on the behavior, not Baseline versus Scoped change mode.

## The promotion artifact

Promotion writes `skai/changes/<change-id>/requirements-promotion.md`, parallel to the authoring
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
- The Promotion Checks gate is the workflow's single review point. `Next` there means: execute the
  listed checks, record evidence, and write the catalog. The supervisor reviews *what will become canon*
  — the requirements themselves, not the mechanics — so the summary names the files and the count of
  requirements the write puts into the catalog — every requirement in the files being written,
  carried-forward ones included, because the write replaces whole files — not the checklist and not
  the count of change items. A change to any requirement's wording returns the package
  to authoring — as does a request to change anything else in the package's drafts.
  - `⏳ GATE: Next: Promote <N> requirements to <paths>. Say "next" or what to change.`

Planned gates for this workflow:
- After the Promotion Checks are written and the readiness screen passes, before anything is written
  to the catalog.

Workflow-specific blocked gates:
- The package fails any condition of the readiness screen (see *Readiness screen*). Restating those
  conditions here would give them two homes to drift between; the screen is the one.
- More than one package is open and the signal does not name which (see *Initiation*).
- A verifying check (`C1`–`C5`) fails **on the package** during execution. The checks are enumerated
  once, under *Promotion Checks*; a `C7` fault found after the write is repaired in place instead,
  and a failure whose cause is the catalog goes to *Raising a change request*.
- The supervisor asks at the Promotion Checks gate for a change to any requirement's wording — rewriting
  is authoring.
- The catalog contradicts what is landing, and the contradiction is load-bearing enough that writing
  would leave canon inconsistent.
- The Integration doc has no `Section: requirements` block, its values are unfilled, or the shape is
  `none`, so promotion cannot know where to write — or, under `shared`, the root it names does not
  resolve, which is not an empty catalog. Never fall back to a literal path. Under `none` the stop is
  terminal, and `next` does not resolve it.

A failed check, a failed readiness condition, a requested wording change, and a load-bearing catalog
contradiction take a workflow-specific line rather than the standard one, because nothing the supervisor
can do at the console resolves them — the package goes back to authoring, and inviting a `next` here
would restart the whole checklist:

`⏳ GATE: Blocked: <C# | readiness condition | requested wording | catalog contradiction> failed — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`

The other two take the standard line, naming what the supervisor supplies — the package, or the block's
values. Under `none` the bullet above governs: nothing supplies a catalog.

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
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the supervisor gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns the `- [ ] C<n>` items in
`## Promotion Checks`. Every item is written unchecked while the gate is open — they are the gate's
marker. After advance intent, each is executed in order and checked as it passes, with its evidence
recorded. A **verifying** check (`C1`–`C5`) that fails on the package is left
unchecked and the items after it are not executed, so the artifact shows exactly how far promotion
got. A mechanical fault found after C7's write is repaired in place and then checked: correct
prepared links and rewrite, never reword. Record the write honestly; a prose defect returns to authoring.

**On re-run, every check is unchecked again.** When a failure sends the package back to authoring and
the drafts change, the checks that passed were verified against text that no longer exists. Reset the
whole section, keep the prior evidence brackets as history, and execute from `C1`. Promotion never
resumes mid-list.

Nothing written into the catalog ever carries a marker.

**Workflow-specific `auto` behavior.** `auto` bypasses the Promotion Checks gate, so promotion runs
end to end without review. Use it only for a package whose drafts have already been reviewed. It
never bypasses a failing check: those are blocked gates. And under the `shared` shape the response
still names the outside catalog root before writing to it — `auto` waives the review, not the
warning that this promotion leaves the repo.

## Initiation

The workflow starts on an explicit signal — "promote the requirements", "promote this package", or
equivalent. That signal often comes right after authoring completes, but it is still a signal:
promotion is never a continuation authoring runs into on its own.

Read the app repo's `skai/integration.md` `Section: requirements` block first: it names the
repository shape and catalog root. Resolve the repository that holds the catalog before looking for
packages. `skai/changes/` is relative to that repository, including under `shared`; an unknown or
unresolved repository is a blocked gate, never an empty catalog or a host-repo fallback.

Then identify the package. Open packages are directories under that repo's `skai/changes/` holding
an unpromoted `requirements-authoring.md` (see *Completion*); the directory also holds other
workflows' packages. More than one open package with no named target is a blocked gate rather than
a guess.

Under the `shared` shape that root — and the package, which lives beside it — is **outside this repo**, in a submodule's working tree. Say so
before writing, naming the path, so it is never a surprise that a promotion touched files elsewhere.
Writing them is all this workflow does; what happens to those changes afterwards is the supervisor's.

### Readiness screen

Before writing `## Promotion Checks`, verify the package is promotable at all:

1. Every `- [ ]` item in the authoring artifact's `## Discussion` is resolved.
2. Recompute the catalog-to-drafts comparison against the current catalog using prose and resolved
   link targets. Ignore only location-required relative-path changes; added/removed citations and
   changed targets still count. Every change has an item and every item still matches; otherwise
   return to authoring.
3. No change request in the package remains `Proposed`.

Any of the three failing is a blocked gate, and the resolution is authoring, not promotion. Do not
write a checks section for a package that cannot be promoted; record the failing condition in
`## Evidence` instead.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

**C1–C5 verify, C6 prepares destination links, C7 writes.** Verify new/changed content in its
projected canonical location, retaining link target identities; leave drafts unchanged. Unchanged
carried-forward content and unrelated catalog defects do not block. C1 also sweeps all IDs in each
rewritten file and retired-ID reuse catalog-wide; C2 checks prefixes catalog-wide; C7 confirms all
written text. Known-difference notes are observations, not new obligations or progress markers.

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
  faults in place; never reword. C7 remains the terminal completion item.

`C4` is the check most worth taking seriously and the easiest to wave through.

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

## Evidence

[evidence: C1; comm -23 <(grep -ohE '^## [A-Z-]+-[0-9]+' requirements/features/reminders.md | sed 's/^## //' | sort -u) <(grep -ohE '^## [A-Z-]+-[0-9]+' skai/changes/reminder-expiry/proposed-requirements/features/reminders.md | sed 's/^## //' | sort -u); comm -12 <(grep -rhoE '^## [A-Z-]+-[0-9]+ \(retired\)' requirements/ | grep -oE '[A-Z-]+-[0-9]+' | sort -u) <(grep -rhoE '^## [A-Z-]+-[0-9]+$' skai/changes/reminder-expiry/proposed-requirements/ | grep -oE '[A-Z-]+-[0-9]+' | sort -u); no ID dropped, none renumbered, no retired ID reused]
[evidence: C2; inspection of the prefix on each touched file's line in features/_features.md; both present, no new prefix introduced]
[evidence: C3; every ID this package's new and changed text cites, resolved against the catalog plus the drafts; 0 unresolved]
[evidence: C4; writing-style check over the changed requirements REMIND-04, REMIND-06, REMIND-09, against Required, Forbidden and Nothing that decays in full; FAILED on REMIND-06; output: skai/changes/reminder-expiry/evidence/promotion-run1-c4.md]
```

## Evidence

`## Evidence` records the verification trail. One bracket per check:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

The check ID comes first; `<outcome>` states what the check found — what the command's output
showed, or what an inspection observed. The ID says which check a bracket belongs to, not which run
— every run emits a `C1` — so a re-run appends its brackets below the
previous run's under a `### Run <n>` heading rather than interleaving them.

Inspection and preparation results name what was checked or changed:

```
[evidence: C4; writing-style check over the changed prose — REMIND-04, REMIND-06, REMIND-09 and the `Expiry window` glossary entry — against Required, Forbidden and Nothing that decays in full; no mechanism named, no temporal reference, all four phrased as behavior]
[evidence: C5; inspection — features/_features.md's line for reminders names expiry and dismissal, not just "reminders"; `Pending reminder` and `Expiry window` both have glossary entries pointing at REMIND-04 and REMIND-09; no behavioral claim outside a numbered requirement in the three written files]
[evidence: C6; NOTE-04 definition rebased from the draft location to ../domains/note.md#note-04; canonical target identity unchanged; known-difference notes retained]
[evidence: C7; wrote features/reminders.md, features/_features.md, glossary.md; 9 requirements landed; grep -E '\(D[0-9]+\)|- \[[ x]\]|🟡' requirements/features/reminders.md requirements/features/_features.md requirements/glossary.md returned nothing; inspection — destination links resolve; REMIND-07 retirement and labeled known-difference notes retained]
```

On failure, persist and link the full output, so `output` is required. Key its path to the run as
well as the check — a later run failing the same check would otherwise overwrite the output an
earlier run's retained bracket still cites. On success, `output` is
optional when nothing was persisted. Where a check is an inspection rather than a command, name what
was inspected precisely enough to repeat it.

**Silence is not a pass.** Name the compared inputs and observed result; an unresolved path cannot
pass by returning no matches. A legitimately empty subject passes only with the reason recorded.
Compare catalog and draft IDs per rewritten file and retired IDs catalog-wide. Strip path prefixes
before ID comparisons (`grep -rhoE`); otherwise paths make equivalent IDs appear different.

## Raising a change request

If **the catalog is wrong** — an already-promoted requirement contradicts what is landing, or is
internally inconsistent with what is about to be written, whether a check surfaces it or promotion
reads it while preparing the write — that is not a defect in the package and cannot be fixed by
editing the package's drafts alone. Raise a change request against the package, per
[`requirements-artifacts.md`](requirements-artifacts.md), link it under `## Change Requests`, and
either continue (when the contradiction
does not affect this write) or block (when writing would leave canon inconsistent). On the continue
branch the check is **checked**, with the request linked from its evidence: it passed as far as this
package is concerned, and leaving it unchecked would make the artifact claim promotion stopped before
a write it actually performed.

Promotion is the only workflow that raises these.

## Completion

When `C7` is checked and its evidence is recorded, the catalog holds the package's requirements. End
with `🏁 Complete. Let me know if anything needs adjustment.`

The package stays where it is. It is the durable record of why these requirements say what they say —
the Discussion that produced them, the decisions, and the sources. Nothing about it is deleted on
promotion.

A promoted package is one whose `requirements-promotion.md` has `C7` checked. It is not promoted
again, and it is not one of the open packages *Initiation* counts. If a change request is still
`Proposed` at completion, name it in the completion message: the catalog defect it records needs its
own scoped-change package, and this one will not be reopened to carry it.

## Cross-references

- [`requirements-catalog.md`](requirements-catalog.md) — catalog content rules
- [`requirements-authoring.md`](requirements-authoring.md) — the authoring workflow
- [`requirements-artifacts.md`](requirements-artifacts.md) — change item and change request formats
