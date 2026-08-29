Managed-By: skai
Managed-Id: guide.ticket-filing
Managed-Source: Guides/Process/ticket-filing.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-29

# Ticket filing

Purpose: capture process improvement suggestions and file them as GitHub issues on the `skai` repo. Handles both ad-hoc suggestions (human describes a problem or idea) and retro handoffs (drafts already written by the retro).

## Gates

Core rule: every time the agent is waiting on the human, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the human.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the human gives advance intent. If the gate is non-standard, make it describe the exact human response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the human resolves it.

Workflow-specific gate notes:
- The Phase 1 understanding gate is a non-standard planned gate. `Next` there means: the current understanding is good enough to draft ticket(s) now.
- The Phase 1 draft-review gate is the main review/file gate for this workflow. `Next` there means: file the remaining unchecked `- [ ] T<n> Ticket: …` entries now. The human may instead ask to revise drafts further or leave them for later.

Planned gates for this workflow:
- After Phase 1 understanding is complete, but before drafting ticket(s).
- After Phase 1 drafts are written or updated in `skai/working-docs/<branch-path>/<session-name>/process-tickets.md` and presented for review, but before deciding whether to file them now or leave them for later.

Workflow-specific blocked gates:
- GitHub MCP access is unavailable or misconfigured, so filing cannot proceed.
- The required `process-tickets.md` draft file cannot be located and the human has not provided the session/path needed to continue.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip required review or filing decisions.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit human resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking:
- Default marker convention: `- [ ]` / `- [x]` in the process-tickets file (process artifact). See `Guides/Core/process-flow.md`, "Progress markers".
- Default rule: a `- [ ]` ticket item means pending draft / pending filing. Do not check it without human approval.
- The workflow-owned artifact is `skai/working-docs/<branch-path>/<session-name>/process-tickets.md`.
- In that artifact, each ticket is a `- [ ] T<n> Ticket: <summary>` list item (stable letter-led ID — `T1`, `T2`, …) with body fields as sub-bullets.
- The Phase 1 understanding gate does not require its own workflow artifact or marker; it is a human approval stop before drafting begins.
- At the Phase 1 draft-review gate, STOP with the ticket items still unchecked.
- If the human gives advance intent at the Phase 1 draft-review gate, create GitHub issues for each unchecked ticket and update each entry by checking the box (`- [x]`) and appending a `- **Filed** #<number>` sub-bullet.
- If the human decides to skip an entry during draft review, move it to a `## Skipped` subsection of the file with strikethrough on the title text (the line remains a list item but unchecked); see the example below.

Workflow-specific advance behavior:
- `auto` may move past the understanding gate and may draft suggestions, but it must STOP at the draft-review gate before creating issues.
- Use `ready to draft` and `draft review` as the stable bounded-auto targets for this guide.

## Confidentiality rule

This repo is public. Issues must **never** contain project names, client names, domain-specific details, or any information that identifies the source project. Every suggestion must be generalized into a process-level observation.

- Bad: "In Project Acme, the retro missed security edge cases in the auth module"
- Good: "The retro template does not prompt for security considerations, which can lead to gaps in auth-related work"

The human reviews all issue content before creation at the draft-review gate. This is the final approval point before filing, but the agent should make a good-faith effort to generalize first.

## Entry points

- **Ad-hoc**: the human describes a process problem, improvement idea, or feature request. Start at Phase 1.
- **From retro**: the dev retro's process reflection step develops one or more process suggestions and hands them off here. Skip the ad-hoc discussion step and start at Phase 1, step 2 so this guide owns drafting, review, and filing.

## Phase 1: Draft

Goal: produce one or more ticket drafts in `skai/working-docs/<branch-path>/<session-name>/process-tickets.md`.

Before writing the working file, choose a `session-name` for this suggestion-filing effort so multiple draft sessions on the same branch stay separate.

### 1. Understand the suggestion

This step is for the **ad-hoc** entry path only. If you arrived here from `Guides/Process/dev-retro.md`, skip this step and use the handed-off suggestions as the draft inputs for step 2.

Ask the developer to describe what they have in mind. Use follow-up questions to clarify:

- What were you trying to do?
- What went wrong or felt harder than it should?
- Did this happen once, or is it a recurring pattern?
- Do you have a sense of what a fix would look like?

Keep the conversation natural -- don't interrogate. The goal is to get enough detail to write an actionable draft.

If the developer provides a clear description up front, skip the questions and proceed to drafting.

Gate: once you believe you understand the suggestion well enough to draft actionable ticket(s), STOP and end with `⏳ GATE: Next: Draft the process ticket(s). Say "next" or what to change.`

At this gate:
- `next` / advance intent = draft the ticket(s)
- requested changes or clarifications = continue discussion, then stop again at the same gate when ready to draft

### 2. Write drafts to the working file

Write a ticket draft entry to `process-tickets.md` at `skai/working-docs/<branch-path>/<session-name>/process-tickets.md`. If the file already exists for this session, append to it. If it doesn't exist, create it.

Draft inputs:
- **Ad-hoc path**: use the understanding developed in step 1.
- **Retro handoff path**: use the concrete process suggestions handed off from `Guides/Process/dev-retro.md`.

If the retro handoff is not specific enough to draft actionable tickets, STOP and ask the human to clarify before writing the drafts.

Draft format:

```
- [ ] T<n> Ticket: <concise summary>
  - **Labels** <labels>
  - **Friction** <what was painful or suboptimal, described generically — no project references>
  - **Evidence/example** <what happened that shows the problem (generic; no project references)>
  - **Failure mode** <what goes wrong if this repeats>
  - **Candidate approach** <a possible fix direction, if confident> (optional)
  - **Affected files** <paths within the skai repo, if known; `Unknown` is acceptable>
  - **Verification** <how to confirm the change worked next time> (optional)
```

Where `<n>` is sequential within this file — `T1`, `T2`, `T3`, … — never reused. Letter-led so a leading digit isn't misparsed as an ordered-list item.

Sub-bullet field labels are **bold** with no separator after the label — the bold weight is the separator (matching the canonical Structured discussion items conventions).

Tight list: where multiple ticket items sit under the same heading, leave no blank line between them. A blank line makes the list "loose," which pushes the checkbox onto its own line in some renderers; a tight list keeps the checkbox inline with the title.

Full file structure:

```markdown
# Process tickets — <session-name>

## Drafts

- [ ] T1 Ticket: <summary>
  - **Labels** ...
  - **Friction** ...
  - ...
- [ ] T2 Ticket: <summary>
  - ...

## Skipped

- [ ] ~~T3 Ticket: <summary>~~ — skipped during review (<short reason>).
  - (body sub-bullets remain for context, unchanged)
```

After a filing run, filed tickets stay in `## Drafts` with the box checked and a `- **Filed** #<n>` sub-bullet appended. The `## Skipped` subsection holds entries the human chose not to file; the title text gets strikethrough but the checkbox remains unchecked (the entry was neither filed nor "completed" in the workflow's sense).

For `**Labels**`: choose from this list (source of truth for this workflow):
- `enhancement`
- `bug`
- `documentation`
- `help wanted`
- `question`
- `invalid`

Apply the confidentiality rule to all drafts.

Present the drafts to the developer for review.

Gate: STOP after drafts are written or updated and presented. End with `⏳ GATE: Next: File the drafted process tickets. Say "next", "leave for later", or what to change.`

At this gate:
- `next` / advance intent = file the remaining unchecked `- [ ] T<n> Ticket: …` entries now.
- `leave for later` = end the workflow without filing; keep the unchecked `- [ ]` items in place in `process-tickets.md`.
- requested changes = revise drafts, optionally move specific entries to `## Skipped`, re-present them, and stop again at the same gate.

## Phase 2: File

Goal: file approved drafts as GitHub issues.

### 1. Check GitHub MCP access

Verify that a GitHub MCP server is configured and accessible.

If it is not available, tell the human that a GitHub MCP server is required for ticket creation and offer to help set one up (e.g., adding a GitHub MCP server to the project's MCP configuration with a personal access token that has repo issue permissions).

Do not proceed until GitHub MCP access is confirmed.

### 2. Read the approved drafts

Locate the `process-tickets.md` working file at `skai/working-docs/<branch-path>/<session-name>/process-tickets.md`. Read the unchecked `- [ ] T<n> Ticket: …` entries under `## Drafts` that the draft-review gate left in place.

To skip an entry before filing: move it to the `## Skipped` subsection, apply strikethrough to the title text (`~~T<n> Ticket: <summary>~~`), and append `— skipped during review (<short reason>).` to the title line. Leave the checkbox unchecked.

### 3. Create issues

For each unchecked entry in `## Drafts`:

1. Use the GitHub MCP server to create the issue on the `skai` repo with the labels from the draft.
2. Update the working file: check the box (`- [x]`) and append a `- **Filed** #<number>` sub-bullet to the entry. Leave the entry under `## Drafts` (it stays as the historical record of what was filed; do not move it).

Report the created issue numbers and URLs back to the human.

Then complete the workflow.
