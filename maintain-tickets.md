Managed-By: skai
Managed-Id: guide.ticket-implementation
Managed-Source: maintain-tickets.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# Ticket implementation session

Purpose: work through process improvement tickets filed against this repo. The operator initiates a session, the agent summarizes ready tickets, they discuss approach, and the agent implements with approval.

This is an internal maintenance workflow for the `skai` repo, not a guide for host projects.

## Prerequisites

- You are working in the `skai` repo.
- A GitHub MCP server configured with issue read/write permissions.
- The repo has open issues labeled `agent ready` (triaged and approved for agent implementation).

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
- The phase-start gate uses the canonical Discussion-phase gate behavior (see `Guides/Core/process-flow.md`, "Structured discussion items"): while any `- [ ]` discussion items remain inside the active phase, the workflow emits a blocked gate citing the remaining count; the moment every item is resolved, the agent emits the planned gate that moves the phase to its file-change plan.
- The phase-completion gate is non-standard. `Next` there means: approve the implemented phase, check the phase's box in the top-of-document phase checklist, close the tickets covered by that phase, and move on.

Planned gates for this workflow:
- After creating/updating `skai/working-docs/<branch-path>/<session-name>/ticket-planning.md` with the ready-ticket inventory and proposed phases, and after confirming which phases/tickets will be tackled in this session, but before initializing the first selected phase.
- Per phase: after every `- [ ]` discussion item in the phase has been resolved (the first planned gate of the phase — emitted on resolution of the last item; advances to the file-change plan).
- Before making repo changes for a phase, after proposing the concrete file-change plan.
- After implementing a phase, after reporting what changed and before approving the phase as complete.

## Procedure

### 1. Fetch ready tickets

Use the GitHub MCP server to list open issues labeled `agent ready`.

If no issues match, say **"No ready tickets found."** and stop.

### 2. Create the planning document

Choose a `session-name` for this ticket-maintenance session so multiple planning efforts on the same branch stay separate.

Create or update a working planning document at `skai/working-docs/<branch-path>/<session-name>/ticket-planning.md` (path per `Guides/Core/working-doc-conventions.md`, session name: `<session-name>`, subpath: none, filename: `ticket-planning.md`).

For each ticket, include:
- A markdown link to the GitHub issue (not just `#123`).
- Paraphrased summary:
  - friction/problem (what is going wrong)
  - suggestion (what it proposes changing)
  - anything else of note (e.g., affected files, constraints, overlaps)
- Keep paraphrases concise (1-3 bullets per ticket). Do not paste the full ticket body.

Reconcile before proceeding: ensure every open issue labeled `agent ready` is represented in the planning document. If any are missing, add them before moving on.

### 3. Bucket into phases (when applicable)

Default behavior: group tickets by common theme into execution phases before implementing.

The goal is to implement cohesive improvements (one phase at a time), not blindly apply each ticket's suggested solution in isolation.

Rules:
- Treat the buckets as **execution phases** (Phase A, Phase B, etc.). Implement one phase fully before moving to the next.
- Capture overlaps explicitly so changes that touch the same area are coordinated.
- Track phase completion via a `## Phases` checklist at the top of the planning document (`- [ ] Phase A: <theme>`). Phase sections themselves use plain `###` headings without markers — markdown task lists are scoped to list items, not headings.
- Seed each phase with `- [ ]` discussion items per the canonical Structured discussion items schema (`Guides/Core/process-flow.md`) — `- [ ] PA<n> [Kind] <summary>` for Phase A items, `- [ ] PB<n>` for Phase B, etc. Check the box and append `- **Decision** <resolution>.` as the operator approves each item.

Format example:

```
## Phases

- [ ] Phase A: <theme> (#N, #M)
- [ ] Phase B: <theme> (#P)

### Phase A: <theme> (#N, #M, …)

Primary tickets:
- [#20 Hard prohibition on destructive git operations without explicit operator approval](https://github.com/<owner>/<repo>/issues/20)
  - Friction: agent ran a destructive git command without permission and destroyed uncommitted work.
  - Suggestion: hard rule requiring explicit approval for destructive git commands, with scope/warning requirements.
  - Notes: should live in policy for universal enforcement.

#### Discussion

- [ ] PA1 [Proposal] Where does this rule live?
  - **Concern** Could be a new policy file or extend an existing one.
  - **Proposal** Extend `Policies/safe-operations.md` rather than introduce a new file.
  - **Why** Safe-operations is already loaded as a universal policy; adding a new file fragments the safety story.
```

If there are only 1-2 tickets and they are obviously independent, you may make each one its own single-ticket phase rather than grouping multiple tickets into a broader theme.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip planning, phase discussion, or implementation approval.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit operator resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking:
- Default marker convention: `- [ ]` / `- [x]` in the planning document (process artifact). See `Guides/Core/process-flow.md`, "Progress markers".
- Default rule: a `- [ ]` item means TODO or pending approval. Do not check it without operator approval.
- The workflow-owned artifact is `skai/working-docs/<branch-path>/<session-name>/ticket-planning.md`.
- The top-of-document `## Phases` checklist tracks per-phase completion: `- [ ] Phase A: <theme>`, `- [ ] Phase B: <theme>`, etc. These are the durable phase markers.
- Inside each phase, `- [ ]` discussion items (`PA1`, `PA2`, `PB1`, …) track open planning questions, proposal choices, or unresolved scope details — per the canonical Structured discussion items schema.
- At the planning-document gate, STOP with all phase items unchecked.
- At the phase-start (discussion) gate, while any `- [ ]` discussion item in the active phase remains unresolved the workflow is at a blocked gate. The moment they're all resolved (check the box, append `- **Decision**`), the agent emits the planned gate that advances the phase to its file-change plan. The top-of-document phase entry stays `- [ ]` until phase completion is approved.
- At the file-change-plan gate, STOP with the top-of-document phase entry still `- [ ]`.
- At the phase-completion gate, STOP with the top-of-document phase entry still `- [ ]`.
- After advance intent at the phase-completion gate, check the box on that phase in the top-of-document checklist (`- [x]`), close the tickets implemented in that phase, and move to the next unchecked phase.

Workflow-specific advance behavior:
- After the planning-document gate, advance intent means: initialize the first selected phase's discussion items and stop at that phase's discussion gate.
- At the phase-start (discussion) gate, `next` means the phase scope is settled enough to move to a concrete file-change plan.
- At the file-change-plan gate, `next` means implement the approved phase.
- At the phase-completion gate, `next` means approve the implemented phase, check the phase's box, close its tickets, and continue.
- `auto` may batch work inside an already-approved phase, but it does not bypass the planning-document, phase-start, file-change-plan, or phase-completion gates.

## Procedure (continued)

### 4. Summarize

Present a summary of all ready tickets, grouped if natural categories emerge. For each ticket, show:

- Issue number and title
- One-line summary of what needs to change
- Affected files (if noted in the ticket)

### 5. Discuss and prioritize

Ask the operator which tickets to tackle in this session and in what order. The operator may:

- Select specific tickets by number.
- Reorder priorities.
- Defer tickets to a future session.
- Ask questions or discuss implementation approach for specific tickets.

Do not proceed until the operator confirms the selection.

Gate: STOP after the planning document is updated, summarized, and the session's selected phases/tickets are confirmed. End with `⏳ GATE: Next: Initialize the first selected phase for discussion. Say "next" or what to change.`

### 6. Implement

For each selected ticket, in the agreed order:

1. **Read the maintainer runbook.** Before making changes, read `maintain-skai.md` and follow its rules (safety defaults, bookkeeping, content rules).
2. **Propose a plan.** State what files you will change and how. Wait for approval.
3. **Make the changes.** Follow the repo's conventions:
   - Guides under `Guides/`, policies under `Policies/`, templates under `Templates/`.
   - Managed headers on all repo-source files.
   - Keep examples project-agnostic.
4. **Update bookkeeping.** For each change set:
   - `assets.manifest.json` (if assets were added/moved/renamed)
   - `README.md` Usage section (if a developer-facing workflow changed)
   - `CHANGELOG.md` (under "Unreleased", prefixed with today's date)
5. **Report.** Summarize what changed and list touched files.

After implementing a phase, report what changed and STOP at the phase-completion gate before moving to the next phase.

### 7. Close tickets

Close is triggered by operator approval.

Default approval signal (phase-based sessions):
- Advance intent after a phase implementation report is approval. Close all tickets implemented in that phase.

Mechanics:
- Use the GitHub MCP server to close the issue with a comment noting it was implemented.
- If the implementation will be committed and pushed in a follow-up step, note that in the close comment instead.

### 8. Post-session

After all selected tickets are implemented:

- Run the `maintain-retro.md` checklist and report any misses.
- Remind the operator to commit if they haven't already.
