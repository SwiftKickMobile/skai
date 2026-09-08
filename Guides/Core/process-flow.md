Managed-By: skai
Managed-Id: guide.process-flow
Managed-Source: Guides/Core/process-flow.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# Process flow (house style reference)

Purpose: canonical definitions for process-flow mechanics (gates, advance intent, `auto`, and progress markers). This file is a **maintainer reference** used to ensure consistency across workflow guides. It is NOT a runtime dependency -- agents should not need to read this file during workflow execution. The operational core is inlined in each guide using the standard template defined in `maintain-skai.md`.

## Gates

Core rule: every time the agent is waiting on the operator, the message must end with a `⏳ GATE:` line.

The only normal exception is full workflow completion, which uses:

`🏁 Complete. Let me know if anything needs adjustment.`

This is not a gate. It does not require advance intent.

### Gate persistence

Once a `⏳ GATE:` line is emitted, every subsequent response from the agent — including responses that answer questions, refine the gate-relevant material, discuss details, or otherwise back-and-forth without resolving the gate — must end with the *same* gate line, verbatim, until the gate actually moves.

The gate stays "on" between turns. Re-emitting the gate line at the end of every response is mandatory, not optional.

Why: long back-and-forth stretches across many responses. By turn five or ten, the operator (and sometimes the agent) can no longer see the original gate line without scrolling back, and the conversation can drift onto an unstated implicit gate. The persistence rule fixes this mechanically — the current gate is always visible in the latest response.

Rules:
- Re-emit the *same* gate line, verbatim. Do not paraphrase, shorten, or omit it across turns.
- Update the gate line only when the gate's content actually changes (e.g., a blocker emerges during discussion, or the `Next` description has to change because the planned next step has changed). When updating, emit the new line in full at the end of that response; do not silently mutate the line across turns.
- Discussion is not a gate. Do not invent `⏳ GATE:` lines to describe local back-and-forth state — see "No fabricated gates" below.

### No fabricated gates

`⏳ GATE:` lines only appear at gates the workflow's `## Gates` section defines, or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, intermediate review, or anything else the guide's gate model doesn't already cover.

If a `⏳ GATE:` line is needed that the guide doesn't currently define, that's a signal the guide is missing a gate — file it as a process improvement; don't paper over it with an ad-hoc gate.

### Planned gates

Planned gates are the expected review points of a workflow.

At a planned gate:
- The agent summarizes what it did and what should happen next.
- The message ends with:
  - `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- The agent STOPs and waits for the operator.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the operator gives advance intent. If the gate is non-standard, it should instead describe the exact operator response or handoff needed to resume the workflow.

### Blocked gates

Blocked gates are unexpected stops that require operator input before the workflow can continue.

Use:

`⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Blocked gates may occur at any point in a workflow. They are not limited to the planned gates listed in a guide.

Keep blocked-gate behavior generic unless a workflow has concrete blocker cases discovered through retros and documented in that guide.

## Advance intent

Advance intent moves past the current gate. Common signals include:
- `"begin"`
- `"next"`
- `"continue"`
- `"go ahead"`
- `"proceed"`
- `"do it"`

### Gate-bound by default

Rules:
- Recognize advance intent as approval to move past a gate only after the agent has output a `⏳ GATE:` line.
- Treat phrases like "we should...", "let's...", or "we'll..." as context-setting or discussion intent, not execution approval.
- If the agent is not currently at a gate, do not infer workflow advancement from collaborative phrasing.

### Local approval vs advance intent

Some workflows use local working markers inside an active phase or discussion loop.

In those workflows:
- Operator approval of a specific local item may authorize clearing that item's local marker (checking `- [ ]` to `- [x]` in a process artifact, or removing the 🟡 in code).
- That local approval does **not** automatically count as advance intent for the whole workflow.
- The workflow still advances phases only when it reaches a gate and the operator then gives advance intent there.

Use a local approval model only when the workflow explicitly documents that narrower exception.

## `auto`

`auto` means: apply advance intent repeatedly, bypassing planned gates until the workflow reaches completion or a required stop.

Blocked gates always require explicit operator resolution. `auto` does not bypass them.

### `auto to <target>`

Bounded auto is a universal capability: the operator may specify an upper bound, e.g. `auto to <target>`.

Meaning:
- Auto-advance as in `auto`, but STOP before the named workflow target.
- The target must refer to a stable identifier in the current workflow.
- The guide should define workflow-specific target names when helpful.
- If the target reference is unclear or there are multiple plausible interpretations, STOP and ask the operator what target they mean.

Examples (infer from context):
- Work spec implementation: `"next auto to task 7"`
- Unit testing: `"next auto to success tests"`
- Any workflow with phases: `"next auto to Phase 2"`

### Universal required stops

`auto` does not bypass these required stops:
- missing or broken required tool/integration for the requested workflow
- ambiguity requiring product intent
- about to deviate from an explicit plan/spec/instruction
- about to run a destructive or irreversible operation
- required evidence or artifacts are unavailable
- new evidence contradicts the current hypothesis or plan

## Progress markers

Progress markers track TODO state in skai workflow artifacts. This section applies to skai workflow documents (work specs, planning docs, unit test plans, working docs, retro outputs, ticket drafts) and to source files written or planned by a skai workflow, not to arbitrary developer notes.

Two marker conventions coexist, chosen by artifact type:

- **`- [ ]` / `- [x]` — process artifacts (default).** Markdown task-list checkboxes. Used in any markdown workflow document where the audit trail of completed items should remain visible: work-spec tasks, planning-doc discussion items, work-doc phase checklists, retro suggestions, ticket drafts, change lists, etc. Completion is a check, not a deletion — the artifact keeps a record of every resolved item.
- **`🟡` — in-code progress only.** A literal 🟡 emoji embedded in source files (test code, application code) to mark sections, functions, or lines as TODO. Completion is **removal** of the marker — the file's remaining work is read by which 🟡s remain. The canonical case is the unit test planning workflow ([`unit-test-planning-guide.md`](../Test/unit-test-planning-guide.md)), where section MARKs and test functions are seeded with 🟡 during planning and the markers come off as tests are implemented and pass.

The dividing line is the artifact: process artifacts use `- [ ]`; source files use 🟡. A workflow that produces both (the unit-testing family) uses both — `- [ ]` in the work document, 🟡 in the test files.

The rest of this section applies to both marker conventions unless noted.

### Default marker model

Default rule:
- A progress marker means TODO, or "implemented but pending approval". The agent does not clear it until the operator approves.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned markers completed by the phase that just finished.

Ordering rule:
- The agent first STOPs and waits at the gate.
- The agent clears the approved markers — checking `- [ ]` to `- [x]` in a process artifact, removing 🟡 in code — only after the operator gives advance intent.

### Gate/phase markers vs local working markers

Some workflows use two layers of markers:
- **Gate/phase markers**: track whether a broader phase or gate is still open.
- **Local working markers**: track unresolved items inside that phase (for example, discussion topics or open questions).

When both exist:
- Keep them distinct in the most natural workflow artifact.
- Local approvals clear local working markers.
- Advance intent clears the gate/phase marker.
- The workflow guide must document the exact operator intent that authorizes clearing each marker type.

### Custom marker lifecycles

Workflows may define narrower marker lifecycles when the default model would misdescribe the artifact's real behavior.

When a guide does this, it must document:
- where the markers live
- which markers track gate/phase state vs local working state
- what operator intent authorizes clearing each kind
- that the agent clears them only after that operator intent is received

### Marker update protocol

Every marker must be individually updatable via a stable identifier on the same line. Do not rely on line numbers.

Do not propagate markers up the hierarchy by accident:
- Do NOT add a marker to a parent heading or line solely because it contains child bullets with markers.
- Only put a marker on the specific unresolved item lines when the unresolved state belongs to those items.
- A section or heading may carry a marker only when it intentionally tracks real gate/phase state for that section, not merely because child items remain open.

**Stable letter-led IDs** (`- [ ]` items):
- Every `- [ ]` item carries a stable letter-led ID on the same line — `D1`, `T1`, `F1`, `S1`, etc. The guide defines its prefix(es) to fit context (`D` for discussion, `T` for tasks/tickets, `F` for findings, `S` for suggestions).
- Letter-led so a leading digit isn't misparsed as an ordered-list item — some markdown renderers see `- [ ] 1 …` as the start of a numbered list and break the checkbox onto its own line. `- [ ] T1 …` renders correctly.
- IDs are continuous within their section and never renumbered; removing an item retires its ID, so cross-references stay stable.

For 🟡 in code, the identifier is whatever stable text already lives on the line (function name, MARK section title, etc.).

**Formatting rules for `- [ ]` items:**
- **Tight lists.** Where two or more `- [ ]` items sit under the same heading, leave no blank line between them. A blank line makes the list "loose," which pushes the checkbox onto its own line in some renderers; a tight list keeps the checkbox inline with the title.
- **Content lines only.** Place the marker on the specific content line that needs attention — never on a heading, never as a roll-up on a parent. The marker count equals the number of real decisions or units of work.
- **No checkbox inside a heading.** Markdown task lists are scoped to list items; `## - [ ] Foo` renders as plain text, not a checkbox. If a unit of work needs heading-shaped structure for its body, give it a stable-ID heading (`## Ticket: T1 <summary>`) and track state with a `- [ ]` list item elsewhere or with an inline status sub-bullet.

Allowed stable identifiers (choose the best fit per artifact):
- Work-spec tasks: `- [ ] T1 **Do thing**` (or similar)
- Discussion items: `- [ ] D1 [Kind] <summary>` (see Structured discussion items below)
- Audit findings: `- [ ] F1 [Kind] <summary>`
- Retro suggestions: `- [ ] S1 <suggestion>`
- Tickets: `- [ ] T1 Ticket: <summary>`
- Unit tests (in code): function name (`@Test func testFoo() … // 🟡`) or MARK section title (`// MARK: - Success Tests 🟡`)

Tooling expectation:
- Individual updates: use editor search (scoped to the current working document), or CLI ripgrep (`rg`) to locate the identifier quickly before editing.
- Bulk updates (optional): constrain to a single working document or a clearly scoped section, never repo-wide.

## Structured discussion items

Workflows with a "discussion phase" — where the agent proposes and the operator refines or redirects — use a structured schema for each discussion item. This schema is canonical for any discussion-based workflow (work-spec planning, UI Map architecture, UI Map implementation, etc.).

### Item line

`- [ ] <ID> [Kind] <summary>`

- `<ID>`: stable letter-led ID per the guide's prefix convention (e.g., `D1`, `F1`).
- `[Kind]`: one of `[Question]`, `[Proposal]`, `[Tradeoff]` (see below).
- `<summary>`: plain-language description of what's being decided.

### Kind taxonomy

- `[Question]` — needs operator input; the agent has no basis to recommend. Rare — propose a default whenever there is one.
- `[Proposal]` — the agent recommends a course of action; the operator accepts / rejects / modifies.
- `[Tradeoff]` — two or more options **plus the agent's recommended pick and why**. Never a neutral menu.

The agent always takes a position: every item carries a recommendation, and a `[Tradeoff]` names which option it recommends.

### Sub-bullet labels

Sub-bullet labels are **bold** with no separator after the label — the bold weight is the separator. Standard labels:

- **Concern** (always) — what the issue is.
- **Proposal** (for `[Proposal]` / `[Tradeoff]`) — the recommended action.
- **Question** (for `[Question]`) — what the agent needs decided and why it can't recommend yet.
- **Options** (for `[Tradeoff]`) — the considered alternatives.
- **Detail** (when needed) — elaboration on the concern.
- **Why** — the rationale.
- **Decision** (added on resolution) — see below.

### Resolution

On the operator's explicit approval of an item:
1. Check the box (`- [x]`).
2. Append `- **Decision** <succinct resolution>.` as the last sub-bullet.

The original question/proposal/tradeoff stays visible. The decision is appended, not substituted — the why-this-was-discussed trail is preserved for later review.

### Discussion-phase gate behavior

A discussion phase is gated by the state of its items, not by a separate phase-completion checkpoint:

- **While one or more `- [ ]` items remain unresolved**, the agent emits a **blocked** gate at the end of each response. The blocker *is* the unresolved items; the operator unblocks by resolving them one at a time.

  `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to <next phase>.`

- **The moment every item is resolved** (all `- [x]`, or the discussion produced zero items because inputs fully specify the work), the agent emits the **planned** gate that advances out of the discussion phase. This is the *first planned gate* of a discussion-based workflow.

  `⏳ GATE: Next: Discussion complete. Say "next" to advance to <next phase>.`

The discussion-resolution gate is itself the first planned gate — there is no separate "draft is ready, please review" gate before the discussion begins. The drafting response ends with either the blocked gate (typical) or the planned gate (when the draft produced zero items).

This pattern makes the discussion-phase state explicit at every turn: the agent is either blocked on the operator's decisions or asking permission to advance. There is no in-between "discussion still going, no gate" state.

### Topic-organized, items inline

Each topic is its own `###` subsection. The topic's `- [ ]` items live directly inside it.

**Anti-pattern: aggregator sections.** Do NOT create workflow-shaped sections (`## Questions`, `## Decisions`, `## Tradeoffs`, `## Open Items`) that pull items out of their topics and roll them up. The aggregator-section anti-pattern adds indirection that makes the discussion harder for the operator to manage, and it breaks the "marker count = real decisions" property when topic headings get marked alongside their items.

The marker count across the discussion equals the number of real decisions. If a heading is being marked, or an aggregator section is forming, both signals indicate the schema is being misused.

### Example

Unresolved:

```
### Sharing a note

A note needs a way to share its contents. Today it has no outgoing share route.

- [ ] D1 [Tradeoff] How is share presented from a note?
  - **Concern** Share can be a modal sheet over the note or a pushed screen.
  - **Options**
    - A — modal sheet over the note
    - B — pushed screen
  - **Proposal** A (modal) — sharing is a transient side-task, not a destination in the note's flow.
  - **Why** A sheet dismisses back to where you were; a push implies a place in the navigation.
```

After resolution:

```
- [x] D1 [Tradeoff] How is share presented from a note?
  - **Concern** Share can be a modal sheet over the note or a pushed screen.
  - **Options**
    - A — modal sheet over the note
    - B — pushed screen
  - **Proposal** A (modal) — sharing is a transient side-task, not a destination in the note's flow.
  - **Why** A sheet dismisses back to where you were; a push implies a place in the navigation.
  - **Decision** A — modal sheet. Aligns with the agent's recommended pick.
```
