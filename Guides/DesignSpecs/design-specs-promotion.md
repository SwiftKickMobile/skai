Managed-By: skai
Managed-Id: guide.design-specs-promotion
Managed-Source: Guides/DesignSpecs/design-specs-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-25

# Design Specs Promotion

Print `📖 SKAI guide: design-specs-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Fold the approved package into its **base** per [`change-requests.md`](../Core/change-requests.md), then archive. Only promotion writes canon except verified work-spec
known-difference cleanup. Validate and prepare destination links; preserve prose, IDs, notes and drafts. Return package defects to authoring; a defect in the base starts a package against it ([`change-requests.md`](../Core/change-requests.md)).

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
- Promotion Checks is the sole review before the base changes; `next` executes checks, writes the
  base and archives the package. Summarize destination files and **every item in those whole-file
  writes**, carried-forward items included, not the checklist or item count.
  - `⏳ GATE: Next: Write <N> items into <paths>. Say "next" or what to change.`

Workflow-specific blocked gates:
- A readiness failure, a `V1`–`V10` failure or requested draft edits return the package to
  authoring; record the cause; use:
  `⏳ GATE: Blocked: <what failed, in words> (<V# | readiness condition | requested wording>). I am reopening the package to fix it, then promotion runs again.`
- A base contradiction that would make the write inconsistent takes the standard blocked
  gate; a package against the base fixes it.
- An archive collision, inaccessible references, the design file unreachable for `V5`, or an
  archival failure use the standard blocked gate; recovery follows *Archive the Package*.

## Advance Intent

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

**Workflow-specific marker lifecycle.** This workflow owns `- [ ] C<n>` items in `## Promotion Checks`; write them unchecked.
After advance intent, execute in order, record evidence and check successes. A `C1` failure leaves
it and later items unchecked; repair mechanical faults after `C3`'s write in place, never reword.
Canon carries no markers.

After draft changes, reset all checks, keep prior evidence under `### Run <n>` and restart at `C1`. Archival-only recovery retains `C1`–`C3` and their evidence; never repeat a successful write
to finish `C4`.

**Workflow-specific `auto` behavior.** `auto` skips the review only for already-reviewed drafts;
blockers still stop it.

## Initiation

Promote only on explicit intent, never automatically after authoring; use the named or contextual
package, not siblings or history. First inspect Evidence: resume a recorded `C3` write needing
confirmation/repair there (keep `C1`–`C2`, repair without rewording, verify, check `C3`, archive);
checked `C3` resumes archival only. Changed drafts, intervening base edits or uncertain outcomes block;
never assume unrecorded writes or reopen/promote archived packages.

Before writing, require an absent promoted path (`skai/promoted/<change-id>/design-specs/`, or
`<base>/promoted-change-requests/<nnn>/`); find live incoming references from specs/app repos,
related packages and work specs. Collisions or inaccessible required references block; never
overwrite or merge destinations.

### Readiness Screen

First run `validate <specs root> <drafts>`, `check-changes` and `render` for a current review page;
then verify:

1. Into production: no open Discussion item, gap ([`known-gaps.md`](../Core/known-gaps.md)) or
   request under the package. Into a package, carry them per `C3`.
2. `validate` reports no fault in a held file and no conflict the projection introduces; a fault already in an untouched base file never blocks: start a package against the base.
3. `check-changes` passes: every change has a `## Spec Changes` entry or Touches line at the artifact
   formats' granularity, with the right operation; no entry names an unchanged or absent target.
4. Every modified or retired ID or glossary entry has its sweep under `## Verification`.
5. Apply the outcome of every request this package filed against an input ([`change-requests.md`](../Core/change-requests.md)), now and at the base write.

Record failures in Evidence, not Promotion Checks, and return to authoring. Then, into production,
require every cited requirement's contract to be canonical (`C2` repoints draft links). Otherwise,
record it in Evidence and wait at the standard blocked gate naming it; do not return the package.

## Promotion Checks

Write unchecked `- [ ] C<n> <identity>` items in execution order. Check projected base
locations over the scope [`design-specs.md`](design-specs.md) § Purpose sets.
Use readiness output as evidence for tool-covered checks; inspect the rest.

- `C1 Verification` — run [`V1`–`V10`](design-specs.md#verification-checks) with evidence per
  check; cite the readiness `validate` output where it covers one (`V6` definitions, `V8`
  duplicates, `V9` term links).
- `C2 Prepare destination links` — map package draft targets, including now-canonical requirements,
  to base destinations; untouched dependencies keep their targets. For moves or retired headings,
  repoint incoming spec links in prepared files and annotate external references. Preserve prose,
  IDs, notes and target identities; never edit drafts. Record adjusted definitions or that none needed it.
- `C3 Write the base` — recheck conditions 1 and 5; write prepared whole files to the base,
  creating the root and files if absent; leave other files untouched. Into production: confirm
  by read-back and `validate <specs root>` (a fault readiness did not note is `C3`'s, wherever
  reported): intended link targets; no Discussion citations, checkboxes or `🟡`; only retirement
  marks and labeled known differences beside contracts. Keep the approved diff; do not render
  after writing. Into a package: replace its drafts; append entries to its `## Spec Changes`
  with its next `S` numbers, each Justification ending `; Change request: <nnn> S<n>`; carry open work and
  name the request in Assumptions and TODOs as the shared guide says; validate and render the
  base, whose author reconciles its list on reopen. Record the write outcome; repair mechanically, never reword; check `C3`
  only on confirmed success.
- `C4 Archive the package` — *Archive the Package* below; promotion completes only after verified
  write and archival.

**Excerpt** (`C1/V5` failed: every check unchecked):

```markdown
## Evidence

[evidence: C1/V5; FAILED: the acknowledged-reminder state (UI-NOTES-02-02) has no mockup on Production or any approved change page; Production › Notes inspected]
```

## Evidence

One bracket per check, each `V` in `C1` its own:

```
[evidence: C<n>; <the result, in words>; <command or inspection>; output: <path when persisted>]
```

Persist/link full failure output at unique run/check paths; `output` on success only if persisted.
Result first; inspections name repeatable inputs. Silence never passes: unresolved paths fail; explain empty subjects.

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

On failure, report the specs written but package not yet archived at the standard blocked gate;
resume archival only at either path, never repeating `C3`.

## Completion

With `C3` and `C4` evidenced, link the archived artifact. Emit `🏁 Complete. Let me know if anything needs adjustment.`

## Project Addendum

If `<active-project-root>/skai/addenda/design-specs-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
