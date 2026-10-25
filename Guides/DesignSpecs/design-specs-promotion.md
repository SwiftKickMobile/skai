Managed-By: skai
Managed-Id: guide.design-specs-promotion
Managed-Source: Guides/DesignSpecs/design-specs-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Design Specs Promotion

Print `📖 SKAI guide: design-specs-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Fold the approved package into its **base** per [`change-requests.md`](../Core/change-requests.md); archive. Promotion alone writes canon except verified work-spec
known-difference cleanup. Validate and prepare destination links; keep prose, IDs, notes and drafts
unchanged. Return package defects to authoring; a defect in the base starts a package against it ([`change-requests.md`](../Core/change-requests.md)).

Use [rules/checks](design-specs.md), [formats](design-specs-artifacts.md) and
[shape/tool](../Core/spec-file-shape.md).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## The Promotion Artifact

Write `design-specs-promotion.md` beside the authoring artifact:

```
# Design Specs Promotion — <name>
[Review page](design-specs-review.html)
## Inputs               the package being promoted; its base
## Promotion Checks     - [ ] C<n> items, unchecked until executed
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
- Promotion Checks is the single review point, before the base changes; `next` executes the
  checks, writes the base and archives the package.
  Summarize the destination files and **every item in those whole-file writes**, carried-forward
  items included, not the checklist or change-item count.
  - `⏳ GATE: Next: Promote <N> items to <paths>. Say "next" or what to change.`

Workflow-specific blocked gates:
- A readiness failure, a `V1`–`V10` failure or requested draft edits return the package to
  authoring. Record the cause and use:
  `⏳ GATE: Blocked: <V# | readiness condition | requested wording> failed — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- A contradiction in the base that would make the write inconsistent takes the standard blocked
  gate; a package against the base fixes it.
- An archive collision, inaccessible references, the design file unreachable for `V5`, or an
  archival failure use the standard blocked gate; recovery follows *Archive the Package*.

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

**Workflow-specific marker lifecycle.** This workflow's markers are the `- [ ] C<n>` items in
`## Promotion Checks`, written unchecked; after advance intent, execute in order,
record evidence and check each success. A failure in `C1`
leaves it and everything after unchecked; a mechanical fault after `C3`'s write is repaired in place,
never reworded. Canon carries no markers.

After changed drafts, reset all checks, retain prior evidence under `### Run <n>` and restart at
`C1`. Archival-only recovery retains `C1`–`C3` and their evidence; never repeat a successful write
to finish `C4`.

**Workflow-specific `auto` behavior.** `auto` skips the review only for already-reviewed drafts;
blockers still stop it.

## Initiation

Promote only on explicit intent, never automatically after authoring; use the named or contextual
package, not siblings or history. First inspect Evidence: resume a recorded `C3` write needing
confirmation/repair there (keep `C1`–`C2`, repair without rewording, verify, check `C3`, archive);
checked `C3` resumes archival only. Changed drafts, intervening base edits or uncertain outcomes block;
never assume unrecorded writes or reopen/promote archived packages.

Before writing, require the promoted path (`skai/promoted/<change-id>/design-specs/`, or
`<base>/promoted-change-requests/<nnn>/`) absent; find live incoming
references from specs/app repos, related packages and work specs. Collisions or inaccessible
required references block; never overwrite or merge destinations.

### Readiness Screen

Run `validate <specs root> <drafts>`, `check-changes` and `render` first, so the supervisor reviews
the current page; then verify:

1. Into production: no open Discussion item, gap ([`known-gaps.md`](../Core/known-gaps.md)) or
   request under the package. Into a package, carry them per `C3`.
2. `validate` reports no fault in a held file and no conflict the projection introduces; a fault already in an untouched base file never blocks: start a package against the base.
3. `check-changes` passes: every change has a `## Spec Changes` entry, or rides in one's Touches,
   at the artifact formats' granularity, with the right operation; no entry names an unchanged or
   absent target.
4. Every modified or retired ID or glossary entry has its sweep under `## Verification`.
5. Every request this package filed against an input has its outcome applied ([`change-requests.md`](../Core/change-requests.md)), now and at the base write.

Failures go in Evidence, not Promotion Checks, and return the package to authoring. Then, into
production, every cited requirement's contract is canonical (`C2` repoints a draft link); otherwise record it in
Evidence and wait at the standard blocked gate naming it, without returning the package.

## Promotion Checks

Write unchecked `- [ ] C<n> <identity>` items in execution order. Check projected base
locations over the scope [`design-specs.md`](design-specs.md) § Purpose sets.
Where the tool covers a check, its readiness output is the evidence; the rest is inspection.

- `C1 Verification` — run [`V1`–`V10`](design-specs.md#verification-checks) with evidence per
  check; cite the readiness `validate` output where it covers one (`V6` definitions, `V8`
  duplicates, `V9` term links).
- `C2 Prepare destination links` — map package draft targets, now-canonical requirements
  included, to base destinations; untouched dependencies keep their targets. For moves or
  retired headings, repoint incoming spec links in prepared files and annotate external
  references. Preserve prose, IDs, notes and target identities; never edit drafts; record adjusted
  definitions or that none needed it.
- `C3 Write the base` — recheck conditions 1 and 5; write prepared whole files to the base,
  creating the root and files if absent; leave other files untouched. Into production: confirm
  by read-back and `validate <specs root>` (a fault readiness did not note is `C3`'s, wherever
  reported): intended link targets; no Discussion citations, checkboxes or `🟡`; only retirement
  marks and labeled known differences beside contracts. Keep the approved diff; do not render
  after writing. Into a package: replace its drafts; append entries to its `## Spec Changes`
  with its next `S` numbers and `Change request: <nnn> S<n>; <the entry's own>`; carry open work and
  name the request in Assumptions and TODOs as the shared guide says; validate and render the
  base, whose author reconciles its list on reopen. Record the write outcome; repair mechanically, never reword; check `C3`
  only on confirmed success.
- `C4 Archive the package` — *Archive the Package* below; promotion completes only after verified
  write and archival.

**Excerpt** (`C1/V5` failed: every check unchecked):

```markdown
## Evidence

[evidence: C1/V5; Production › Notes: `notes`, `notes — empty`, `notes — stale` found; `notes — acknowledged reminder` (UI-NOTES-02-02) NOT FOUND on Production or any approved change page; FAILED]
```

## Evidence

One bracket per check, each `V` in `C1` its own:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Persist/link full failure output at unique run/check paths; `output` on success only if persisted.
Inspections name repeatable inputs. Silence is not a pass: unresolved paths fail; an empty subject
records why.

## Archive the Package

After verified `C3`, execute `C4`:

1. Move the package intact (pages, `working-docs/`, `change-requests/`,
   `promoted-change-requests/`): `skai/changes/<change-id>/design-specs/` to
   `skai/promoted/<change-id>/design-specs/`; a request to `<base>/promoted-change-requests/<nnn>/`.
   Preserve siblings; remove only empty grouping directories.
2. Repair live incoming links (repositories, packages, work specs) and relative links inside moved
   files, preserving target identities, prose, IDs, decisions and recorded results; annotate
   historical paths with current locations. Inaccessible or unrepaired required links block.
3. Verify archived files/links, the absent active path and preserved siblings; record move/link
   evidence; check `C4` in the archived artifact.

On failure report “base written, archival incomplete” with the standard blocked gate; resume at
either path, finishing archival only, never repeating `C3`.

## Completion

With `C3` and `C4` evidenced, link the archived artifact. Emit `🏁 Complete. Let me know if anything needs adjustment.`

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
