Managed-By: skai
Managed-Id: guide.design-promotion
Managed-Source: Guides/Design/design-promotion.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-21

# Design Promotion

Print `📖 SKAI guide: design-promotion` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Move an approved package's designs from its change page into production, have the supervisor
confirm the result, delete the change page, and archive the package.

Promotion refactors production to absorb the drafts; it does not redesign them. A design that needs
changing returns the package to authoring. The tool guide owns what "page", "production" and
"component library" mean and the conventions the designs must meet: load
[`figma-designer-guide.md`](figma-designer-guide.md) for Figma.

## The promotion artifact

Promotion writes `skai/changes/<change-id>/design/design-promotion.md` beside the authoring artifact:

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
- At the Promotion Checks gate — after the readiness screen, before production changes — `Next`
  means execute `C1`–`C4`; the summary names the screens added or replaced, from
  `## Design Changes`.
  - `⏳ GATE: Next: Promote <N> screens from <change-id> to production. Say "next" or what to change.`
- The Production review gate is non-standard: the supervisor reviews production in the design file
  before anything is deleted; a requested design change is a blocked gate — the package returns to
  authoring and production is restored from the tool's version history.
  - `⏳ GATE: Next: Review production in the design file. Say "next" to confirm it and delete the change page <change-id>, or what to change.`

Workflow-specific blocked gates:
- A readiness failure (conditions 1–3, or 5 when a ruling invalidates mockups), a `C1` or `C2`
  failure, or a design change the supervisor asks for at either gate: only authoring resolves them; each takes:
  `⏳ GATE: Blocked: <C1 | C2 | readiness condition | requested design change> — <what failed>. The package returns to authoring; re-run promotion once it is resolved.`
- A promoted path already present (condition 4) or a `Proposed` change request (condition 5)
  waits at the standard blocked gate naming it; the ruling is the product spec supervisor's.
- A `C3` (production) or `C4` (links) fault is a promotion mistake repaired in place, never by
  redesigning; one needing access or a library the agent lacks takes the standard blocked line.

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

**Workflow-specific marker lifecycle.** This workflow's markers are the `- [ ] C<n>` items in
`## Promotion Checks`, written unchecked before the first gate. After advance intent, `C1`–`C4`
run in order and are checked as each passes, with evidence; a failing `C1` or `C2` is
left unchecked and nothing after it runs. `C5` and `C6` run only after the Production review gate
advances. An unfinished promotion (`C6` unchecked) continues from its pending check or gate, never
restarts. **A new run after an authoring return unchecks every check** and starts from `C1`; prior
evidence stays under `### Run <n>`.

**Workflow-specific `auto` behavior.** `auto` bypasses the Promotion Checks gate but never the
Production review gate: the supervisor looks at production before the drafts are deleted.

## Initiation

Begin only on an explicit signal ("promote the designs"), never automatically after authoring.

Read the tool guide. The package is the one named or already in context; one already holding an
unfinished `design-promotion.md` continues (*Advance intent*), `C3` re-checking condition 5; the
readiness screen is for a new run.

### Readiness screen

Before writing `## Promotion Checks`, verify:

1. Every `- [ ]` item in `## Discussion` is resolved, gaps included
   ([`known-gaps.md`](../Core/known-gaps.md)).
2. `## Design Changes` is written (the mockups were approved).
3. The change page exists and every Design Changes entry links a draft on it.
4. `skai/promoted/<change-id>/design/` does not exist.
5. Every change request the package filed against the product spec package (listed under
   `## Assumptions and TODOs`) is `Incorporated`, `Rejected`
   or `Superseded` per [`product-specs-artifacts.md`](../ProductSpecs/product-specs-artifacts.md)
   § Change Requests, with the ruling applied to the approved mockups: one invalidating what the drawings
   assumed returns the package to authoring; one leaving them valid needs nothing. A `Proposed` one blocks, now and when the production write begins.

A failure is a blocked gate (*Gates*), recorded in `## Evidence` instead of a checks section.

## Promotion Checks

Write one `- [ ] C<n> <identity>` item per check, all unchecked, in execution order.

- `C1 Drafts meet the conventions` — every draft on the change page follows the tool guide, and
  none still mirrors a gap. A script, where one exists, covers the rules it tests; inspect the rest.
- `C2 Inventory matches the page` — every `## Design Changes` entry has its draft, and every screen
  draft on the change page has an entry. Components a draft needs are not screens; no entry.
- `C3 Production absorbs the change page` — condition 5 still holding by current statuses, per
  entry: a changed screen's production design is
  updated to the draft, keeping its identity; a new screen is placed where the tool guide's layout
  rules put it; the components a draft needs are integrated as the tool guide says. Designs outside
  the inventory change only by the placement and relocation the tool guide's rules need to absorb
  them.
- `C4 Links point at production` — each `## Design Changes` link is repointed from the draft to its
  production design.
- `C5 Delete the change page` — after the Production review gate advances, delete the page.
- `C6 Archive the package` — move `skai/changes/<change-id>/design/` intact (with `working-docs/`) to
  `skai/promoted/<change-id>/design/`, leaving siblings in place and removing an emptied
  `<change-id>` folder; repair live links into the moved files and relative links inside them,
  keeping their targets; verify the move and check `C6` in the archived artifact.

**Excerpt** (at the Production review gate: `C1`–`C4` checked, `C5`–`C6` unchecked):

```markdown
## Evidence

[evidence: C1; script over page `pinned-notes` (bindings, names) passed, output: skai/changes/pinned-notes/design/evidence/promotion-run1-c1.txt; inspection of the remaining rules (components in context, sample data) — no finding]
[evidence: C2; inspection — 3 entries, 3 frames on `pinned-notes`, each entry links one frame; none extra]
```

## Evidence

One bracket per check:

```
[evidence: C<n>; <command or inspection>; <outcome>; output: <path when persisted>]
```

Persist and link full failure output. An inspection names its subject precisely enough to repeat
it; silence is not a pass: name what was compared and found.

## Completion

When `C6` is checked, production holds the designs, the change page is gone and the package is
archived at `skai/promoted/<change-id>/design/`; link its artifact and end with
`🏁 Complete. Let me know if anything needs adjustment.`
If archival fails after `C5`, report production promoted but archival incomplete, use the standard
blocked gate and later resume only the archival.

## Project Addendum

If `<active-project-root>/skai/addenda/design-promotion-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
