Managed-By: skai
Managed-Id: guide.requirements-promotion
Managed-Source: Guides/Requirements/requirements-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# Requirements Promotion

## Purpose

Write an approved change package into the canonical catalog.

Promotion is the **only** writer of the catalog. It is not a file copy: the drafts carry scaffolding
that must not become canon, the IDs must be checked against what the catalog already holds, and the
writing-style rules get their last enforcement here — on the exact text
about to become permanent, which is the point at which enforcement is worth most and costs least.

Promotion **never rewrites a requirement's prose.** Rewriting is authoring. If a requirement fails a
check, promotion blocks and the package goes back to authoring with the finding. The boundary is
what keeps both workflows honest: authoring writes, promotion verifies and writes through.

The boundary is about *wording*. Removing the drafting scaffolding authoring deliberately left
behind — the `(D#)` citations — is mechanical, and doing it is promotion's job, not a rewrite.

Content rules live in [`requirements-catalog.md`](requirements-catalog.md); the package's typed
formats live in [`requirements-artifacts.md`](requirements-artifacts.md).

## When promotion happens

Promotion waits only when the requirements describe behavior the system **does not exhibit yet** —
promoting early would make the catalog claim something untrue. That test, not the package's mode,
decides:

- **Behavior that already ships** — promote on the operator's approval. A backfill of shipping behavior is here,
  and so is a scoped change recording behavior that already shipped, which is what a retro-seeded
  package usually is.
- **Behavior still to come** — promote when the change ships, which may be much later and in another
  session.

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

Core rule: every time the agent is waiting on the operator, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the operator.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the operator gives advance intent. If the gate is non-standard, make it describe the exact operator response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the operator resolves it.

Workflow-specific gate notes:
- The Promotion Checks gate is the workflow's single review point. `Next` there means: execute the
  listed checks, record evidence, and write the catalog. The operator reviews *what will become canon*
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
- The operator asks at the Promotion Checks gate for a change to any requirement's wording — rewriting
  is authoring.
- The catalog contradicts what is landing, and the contradiction is load-bearing enough that writing
  would leave canon inconsistent.
- The Integration doc has no `Section: requirements` block, its values are unfilled, or the shape is
  `none`, so promotion cannot know where to write — or, under `shared`, the root it names does not
  resolve, which is not an empty catalog. Never fall back to a literal path. Under `none` the stop is
  terminal, and `next` does not resolve it.

A failed check, a failed readiness condition, a requested wording change, and a load-bearing catalog
contradiction take a workflow-specific line rather than the standard one, because nothing the operator
can do at the console resolves them — the package goes back to authoring, and inviting a `next` here
would restart the whole checklist:

`⏳ GATE: Blocked: <C# | readiness condition | requested wording | catalog contradiction> failed — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`

The other two take the standard line, naming what the operator supplies — the package, or the block's
values. Under `none` the bullet above governs: nothing supplies a catalog.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit operator resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestones in this workflow: `promotion checks`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without operator approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the operator gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns the `- [ ] C<n>` items in
`## Promotion Checks`. Every item is written unchecked while the gate is open — they are the gate's
marker. After advance intent, each is executed in order and checked as it passes, with its evidence
recorded. A **verifying** check (`C1`–`C5`) that fails on the package is left
unchecked and the items after it are not executed, so the artifact shows exactly how far promotion
got. A fault found *after* a write — `C7`'s confirmation catching scaffolding that survived `C6` —
is repaired in place and the check then checked: re-strip and rewrite, never reword. The artifact
must never claim a write did not happen.

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

On the signal, identify the package. Open packages are the directories under `skai/changes/` that
hold a `requirements-authoring.md` and are not yet promoted (see *Completion*) — `skai/changes/` also
holds other workflows' packages. If more than one is open and the signal does not name which, that is
a blocked gate rather than a guess.

Read `skai/integration.md`'s `Section: requirements` block before writing anything: it names the
repository shape and the catalog root this package promotes into.

Under the `shared` shape that root is **outside this repo** — a submodule's working tree. Say so
before writing, naming the path, so it is never a surprise that a promotion touched files elsewhere.
Writing them is all this workflow does; what happens to those changes afterwards is the operator's.

### Readiness screen

Before writing `## Promotion Checks`, verify the package is promotable at all:

1. Every `- [ ]` item in the authoring artifact's `## Discussion` is resolved.
2. Recompute the catalog-to-drafts diff **against the catalog as it stands now**: every difference
   still has an item, and no item describes a difference that is gone. The diff is a fact about the
   current catalog, never one the artifact can vouch for; if it has moved, the resolution is authoring.
3. No change request in the package remains `Proposed`.

Any of the three failing is a blocked gate, and the resolution is authoring, not promotion. Do not
write a checks section for a package that cannot be promoted; record the failing condition in
`## Evidence` instead.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

The list is not uniform: **`C1`–`C5` verify, `C6` transforms, `C7` writes.** Only the last two change
anything. Every check covers **the requirements, index lines and glossary entries this package adds
or changes** — not the unchanged text a whole-file rewrite carries forward, and not a pre-existing
defect elsewhere in the catalog, which is not this package's to fix and does not block it. Two
checks verify wider and say so, and `C7` confirms the whole text it wrote: `C1` sweeps every ID in a rewritten file, and the whole
catalog for retired-ID reuse; `C2` sweeps the whole catalog for prefix collisions.

The verifying checks read the drafts **as they will be written** — the drafts with the `(D#)`
citations removed, which is what `C6` produces and `C7` writes, the drafts themselves never edited.
Those citations are out of scope for all five.

- `C1 IDs are append-only` — a rewrite must not lose IDs: every ID the catalog holds in a file this
  package rewrites still appears in the draft, no retired ID is reused, and none is renumbered. IDs
  get a check of their own because work specs cite them, so a renumber breaks references outside the
  catalog that nothing here can see. The rest of a rewritten file — glossary entries, index lines,
  header prose — is carried forward when the draft is written whole, per
  [`requirements-authoring.md`](requirements-authoring.md), deliberately not by a check here.
- `C2 Prefixes do not collide` — no prefix introduced here is already claimed by another file in the catalog or this package, and
  every prefix is recorded on its file's line in the scope index.
- `C3 Cross-references resolve` — every ID cited from a requirement, an index, or a glossary entry
  exists after this write.
- `C4 Writing style` — check the requirement and glossary **prose** this package adds or changes, as
  it will be written, against `## Writing style` in
  [`requirements-catalog.md`](requirements-catalog.md): its *Required*, *Forbidden*, and *Nothing
  that decays* lists, in full. An index line is structural — it carries a path and a prefix by
  construction, and what it must *say* is `C5`'s business; its style is not separately checked. A
  file header is orientation rather than specification and carries no requirement to style-check;
  `C5`'s "no behavioral claim in unnumbered prose" is what guards it. Not that section's four-question
  `### Self-check`, which is a during-drafting screen. Do not work from a summary — the categories are easy to half-remember, and the one most often dropped is the
  one most often violated.
- `C5 Traversal` — catalog lines name the questions their files answer; every cross-cutting term
  introduced here has a glossary entry pointing at the requirements that govern it; no behavioral
  claim sits in unnumbered prose.
- `C6 Strip the scaffolding` — remove the `(D#)` citations **from the text being written to the
  catalog, leaving the package's drafts as they are**, recording what was stripped. It changes only
  scaffolding, never a requirement's wording.
- `C7 Write the catalog` — write that text into the catalog root the Integration block
  names — realizing
  `## Requirement Changes`: every file the package holds, and the indexes and glossary it carries. Where the catalog root does not exist yet this creates the tree; otherwise it overwrites
  the files the package holds and leaves every other file untouched. Then confirm the written text
  carries no `(D#)`, no checkboxes, no `🟡`, and no status marker other than a retired requirement's
  `(retired)` — the files now exist, so this is the first point the transform can be verified rather
  than asserted. Terminal item.

`C4` is the check most worth taking seriously and the easiest to wave through.

**Example** (LumenNotes, mid-execution — `C4` failed, so `C5` onward were not run):

```markdown
## Promotion Checks

- [x] C1 IDs are append-only
- [x] C2 Prefixes do not collide
- [x] C3 Cross-references resolve
- [ ] C4 Writing style
- [ ] C5 Traversal
- [ ] C6 Strip the scaffolding
- [ ] C7 Write the catalog

## Evidence

[evidence: C1; comm -23 <(grep -ohE '^## [A-Z-]+-[0-9]+' skai/requirements/features/reminders.md | sed 's/^## //' | sort -u) <(grep -ohE '^## [A-Z-]+-[0-9]+' skai/changes/reminder-expiry/proposed-requirements/features/reminders.md | sed 's/^## //' | sort -u); comm -12 <(grep -rhoE '^## [A-Z-]+-[0-9]+ \(retired\)' skai/requirements/ | grep -oE '[A-Z-]+-[0-9]+' | sort -u) <(grep -rhoE '^## [A-Z-]+-[0-9]+$' skai/changes/reminder-expiry/proposed-requirements/ | grep -oE '[A-Z-]+-[0-9]+' | sort -u); no ID dropped, none renumbered, no retired ID reused]
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

The checks most often left vague have brackets too — the two that change something, and the two
whose evidence is an inspection rather than a command:

```
[evidence: C4; writing-style check over the changed prose — REMIND-04, REMIND-06, REMIND-09 and the `Expiry window` glossary entry — against Required, Forbidden and Nothing that decays in full; no mechanism named, no temporal reference, all four phrased as behavior]
[evidence: C5; inspection — features/_features.md's line for reminders names expiry and dismissal, not just "reminders"; `Pending reminder` and `Expiry window` both have glossary entries pointing at REMIND-04 and REMIND-09; no behavioral claim outside a numbered requirement in the three written files]
[evidence: C6; (D2), (D5) removed from REMIND-04 and REMIND-09; no other scaffolding present]
[evidence: C7; wrote features/reminders.md, features/_features.md, glossary.md; 9 requirements landed; grep -E '\(D[0-9]+\)|- \[[ x]\]|🟡' skai/requirements/features/reminders.md skai/requirements/features/_features.md skai/requirements/glossary.md returned nothing; inspection — no status field on any written requirement other than REMIND-07's (retired)]
```

On failure, persist and link the full output, so `output` is required. Key its path to the run as
well as the check — a later run failing the same check would otherwise overwrite the output an
earlier run's retained bracket still cites. On success, `output` is
optional when nothing was persisted. Where a check is an inspection rather than a command, name what
was inspected precisely enough to repeat it.

**A passing command prints nothing on stdout — but is only a pass if it read something.** A path
that does not resolve prints nothing either, so the outcome names what was compared. Where a check's
subject is legitimately empty — a baseline package rewrites no file, so `C1` has nothing to compare —
it passes by naming the fact that makes it empty, as `C2`'s bracket in the *Promotion Checks*
example above does with "no new prefix introduced". That statement can be false; "no output" cannot. That is what makes a bracket proof rather
than a transcript: a search that prints its expected matches every run cannot be read as a result,
and a check that cannot fail is not a check. Where the check spans the catalog and the drafts, the
command must too — `C1` asks whether the catalog's IDs survived the rewrite, which a search
of the drafts alone cannot see — run that comparison once per rewritten file.

Strip path prefixes before comparing (`grep -rhoE`); with them every match is unique and the
comparison finds nothing. Prefer tools present in a plain shell — `rg` is often a shell alias rather
than a binary and is not reliably callable from a script.

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
