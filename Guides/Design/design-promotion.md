Managed-By: skai
Managed-Id: guide.design-promotion
Managed-Source: Guides/Design/design-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-14

# Design Promotion

Print `📖 SKAI guide: design-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Move an approved change package's designs from its change page into the production designs, have
the supervisor confirm the result, delete the change page, and archive the package.

Promotion refactors production to absorb the drafts; it does not redesign them. A design that needs
changing returns the package to authoring. This guide is tool-agnostic. The conventions the designs
must meet, and what "page", "production", and "component library" mean in the tool, live in the
tool's own guide: load [`figma-designer-guide.md`](figma-designer-guide.md) for Figma.

Implementing the designs in code is outside this workflow.

## The promotion artifact

Promotion writes `skai/changes/<change-id>/design/design-promotion.md`, beside the authoring artifact:

```
# Design Promotion — <name>
## Inputs               the package being promoted; the design file
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
- The Promotion Checks gate: `Next` means execute `C1`–`C4`, which verify the package and then
  change production. The summary names the screens that will be added or replaced, from
  `## Design Changes`.
  - `⏳ GATE: Next: Promote <N> screens from <change-id> to production. Say "next" or what to change.`
- The Production review gate is non-standard: the supervisor reviews production in the design file
  before anything is deleted. A request to change a design is a blocked gate — the package returns
  to authoring, and production is restored from the tool's version history.
  - `⏳ GATE: Next: Review production in the design file. Say "next" to confirm it and delete the change page <change-id>, or what to change.`

Planned gates for this workflow:
- After the Promotion Checks are written and the readiness screen passes, before production changes.
- After production has absorbed the change page, before the page is deleted.

Workflow-specific blocked gates:
- The package fails a condition of the readiness screen (see *Readiness screen*).
- `C1` or `C2` fails on the package: the package returns to authoring; re-run promotion once it is
  resolved. A fault in `C3` (production) or `C4` (the links) is a promotion mistake, repaired in
  place, never by redesigning; one that needs something the agent lacks (access, a library) takes
  the standard blocked line.
- The supervisor asks, at either gate, for a design to change: that is authoring.

A readiness failure, a `C1`/`C2` failure, and a requested design change take this line, because
only authoring resolves them:

`⏳ GATE: Blocked: <C1 | C2 | readiness condition | requested design change> — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestones in this workflow: `promotion checks`, `production review`.

Progress tracking:

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** seeded or planned by a skai workflow. Completion is **removal** of the marker.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without supervisor approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers only after the supervisor gives advance intent.

**Workflow-specific marker lifecycle.** This workflow owns the `- [ ] C<n>` items in
`## Promotion Checks`. All are written unchecked while the first gate is open. After advance intent,
`C1`–`C4` run in order and are checked as each passes, with evidence recorded; a failing `C1` or
`C2` is left unchecked and nothing after it runs. `C5` and `C6` run only after the Production
review gate advances. An unfinished promotion (checks written, `C6` unchecked) is continued from its
pending check or gate, not restarted. **A new run after an authoring return unchecks every check** and
starts from `C1`; prior evidence stays as history under a `### Run <n>` heading.

**Workflow-specific `auto` behavior.** `auto` bypasses the Promotion Checks gate but never the
Production review gate: the supervisor looks at production before the drafts are deleted, always.

## Initiation

The workflow starts on an explicit signal — "promote the designs", "promote this package", or
equivalent. It is never a continuation authoring runs into on its own.

The package is the one named or already in context. Read the tool guide. If the
package already holds an unfinished `design-promotion.md`, continue it (see the marker lifecycle);
the readiness screen below is for a new run.

### Readiness screen

Before writing `## Promotion Checks`, verify the package is promotable:

1. Every `- [ ]` item in the authoring artifact's `## Discussion` is resolved.
2. `## Design Changes` is written, so the mockups were approved.
3. The change page exists and every Design Changes entry links a draft on it.
4. `skai/promoted/<change-id>/design/` does not exist.

Any failing is a blocked gate, and the resolution is authoring. Record the failing condition in
`## Evidence` instead of writing a checks section.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

- `C1 Drafts meet the conventions` — every draft on the change page follows the tool guide: its
  rules for frames, styles and variables, dimensions, and components. A script, where one exists,
  covers the rules it tests; inspect the rest. Record what was checked and how.
- `C2 Inventory matches the page` — every `## Design Changes` entry has its draft, and every screen
  draft on the change page has an entry; a mismatch returns the package to authoring. Components a
  draft needs are not screens and need no entry.
- `C3 Production absorbs the change page` — for each entry: a changed screen's production design is
  updated to the draft, keeping its identity; a new screen is placed where the tool guide's layout
  rules put it; the components a draft needs are integrated as the tool guide says. Designs outside
  the inventory are not changed; the placement and relocation the tool
  guide's rules need to absorb them are.
- `C4 Links point at production` — each `## Design Changes` link is repointed from the draft to its
  production design.
- `C5 Delete the change page` — after the Production review gate advances, delete the page.
- `C6 Archive the package` — move `skai/changes/<change-id>/design/` intact to
  `skai/promoted/<change-id>/design/`, leaving sibling types in place and removing the `<change-id>`
  folder only if empty; repair live links into the moved files and relative links inside them,
  keeping their targets; verify the move, then check `C6` in the archived `design-promotion.md`.

**Example** (mid-execution, waiting at the Production review gate):

```markdown
## Promotion Checks

- [x] C1 Drafts meet the conventions
- [x] C2 Inventory matches the page
- [x] C3 Production absorbs the change page
- [x] C4 Links point at production
- [ ] C5 Delete the change page
- [ ] C6 Archive the package

## Evidence

[evidence: C1; script over page `pinned-notes` (bindings, names) passed, output: skai/changes/pinned-notes/design/evidence/promotion-run1-c1.txt; inspection of the remaining rules (components in context, kit instances linked, sample data) — no finding]
[evidence: C2; inspection — 3 entries, 3 frames on `pinned-notes`, each entry links one frame; none extra]
[evidence: C3; `notes` and `notes — empty` updated in place on Production; `note editor — pin menu` added below `note editor — date picker`; `Pinned Header` moved to Components → Controls, 1 instance]
[evidence: C4; 3 links repointed to Production frames]
```

## Evidence

`## Evidence` records the verification trail, one bracket per check:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

On failure, persist and link the full output. Where a check is an inspection, name what was
inspected precisely enough to repeat it. Silence is not a pass: name what was compared and what was
found.

## Completion

When `C6` is checked, production holds the package's designs, the change page is gone, and the
package is archived at `skai/promoted/<change-id>/design/`, where it stays as the record of why the
designs are what they are. Link its artifact and end with
`🏁 Complete. Let me know if anything needs adjustment.` An archived package is not promoted again.
If archival fails after `C5`, report production promoted but archival incomplete, use the standard
blocked gate, and later resume only the archival.

## Cross-references

- The tool guide for the project's design tool ([`figma-designer-guide.md`](figma-designer-guide.md)
  for Figma)
- [`design-authoring.md`](design-authoring.md) — the authoring workflow

## Project Addendum

If `<active-project-root>/skai/addenda/design-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
