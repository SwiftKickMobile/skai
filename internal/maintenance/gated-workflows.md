# Gated workflow authoring

This is a maintainer reference, read only when the routing table in [`../maintain-skai.md`](../maintain-skai.md) applies. It is not an installed asset or a runtime dependency of host workflows.

## Discussion-phase authoring (when applicable)

If the guide you're writing or editing includes a discussion phase (a phase where the agent proposes design items and the supervisor refines, accepts, or rejects them), read `Guides/Core/process-flow.md` § "Structured discussion items" **before drafting the discussion content**. That section is canonical for:

- the item-line shape (`- [ ] <ID> [Kind] <summary>`)
- the Kind taxonomy (`[Question]` / `[Proposal]` / `[Tradeoff]`)
- the sub-bullet labels (`Concern` / `Proposal` / `Options` / `Detail` / `Why` / `Gap` / `Decision`)
- the resolution mechanic (check the box + append `- **Decision** <resolution>.`; at most one Decision line, removed on reopen; a changed decision replaces it and logs `decided` again; `reopened` only for a withdrawn decision with no replacement; a resolved item stays while something current cites it or it explains the current drafts, else it is removed and the log keeps its record)
- gaps: an item that cannot be resolved because something outside the work is not yet known stays open with a `- **Gap** <placeholder, or "no placeholder; waiting on <what>">` line, does not count toward the blocked gate, and blocks promotion; the one pointer sentence every Discussion-phase guide inlines verbatim next to its Discussion rules (copy it from process-flow § Sub-bullet labels — it sends the agent to `Guides/Core/known-gaps.md` for the workflow, which is never inlined)
- `## Decision Log`: the artifact's last section, one `- <ID> <state> — <one line>` per state change (`decided` / `gap` / `reopened`), append-only, no dates, entries may outlive their items; put it in the guide's artifact skeleton
- the discussion-phase gate cycle (blocked while non-gap items remain, planned the moment they're all resolved — the *first planned gate* of a discussion-based workflow — naming any open gaps carried)

Treat it as an authoring input, not a runtime read. Once the discussion phase is drafted per the canonical, the standardized gates template (below) still applies to the workflow's gate behavior overall.

### Standard structure for guides with gates

If the guide is a gated workflow — one where the agent waits on the supervisor and emits `⏳ GATE:` lines — inline the applicable process-flow invariants in the guide's control sections, using the template below as the default. A bare "STOP" inside a method guide (stop and run the self-check; stop and present a tradeoff) is not a gate and needs neither section. Do not reference `Guides/Core/process-flow.md` as a runtime dependency -- agents skip indirect references.

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

Workflow-specific gate notes (optional):
- If a planned gate has workflow-specific semantics rather than the default "review complete, say `next` to advance" behavior, state the exact gate response and what `Next` means there.
- Review/handoff gates are one common example, but not the only allowed variation.
- Recognition test for a non-standard planned gate:
  - If the supervisor response needed there is not simply "review complete; `next` means approve-and-advance", treat it as non-standard.
  - If leaving the gate standard would misdescribe what the supervisor should do next, clear progress markers too early, or advance to the wrong phase, treat it as non-standard.
  - For any non-standard planned gate, document the exact `⏳ GATE: Next: ...` response, what kind of supervisor response resumes the workflow, what `Next` means there, and how progress markers track that gate.
- For any non-standard planned gate, use the workflow's declared marker lifecycle and artifact to show its state (marker convention defined in the Progress tracking block of the Advance intent template below).
- Make the marker lifecycle explicit:
  - which markers track gate/phase state vs local working state
  - what specific supervisor intent approves clearing them
  - that the agent clears them only after that supervisor intent is received
- If the workflow has guide-specific blocked cases discovered through retros, list them here. Otherwise keep blocked behavior generic.

Planned gates for this workflow:
- <gate 1>
- <gate 2>

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking (**authoritative marker convention for skai workflow guides** — sanity scan enforces the same rule at [`guide-authoring.md` § Sanity scan](guide-authoring.md#sanity-scan-after-every-guide-edit) → "Marker convention compliance" in that reference; canonical reference in `Guides/Core/process-flow.md` § "Progress markers"):

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

<workflow-specific advance behavior>
```

**Gates section rules:**
- Use the standardized gate invariants and add workflow-specific planned gates. Preserve explicitly declared control variants; missing or contradictory approval, persistence or blocked-stop behavior is still a defect.
- If the guide has a custom review/handoff gate, explicitly state the exact `⏳ GATE: Next: ...` response and what supervisor action resumes the workflow.
- Keep blocked-gate behavior generic unless the workflow has concrete blocker cases discovered through retros.
- Every place the guide says the agent must STOP and wait on the supervisor must correspond to a `⏳ GATE:` line in the runtime behavior.
- After the template block, list this guide's workflow-specific gates.

**Advance intent section rules:**
- Use the default advance-intent template where applicable. An explicitly declared no-auto workflow keeps its own advance model; do not add auto instructions from the template.
- After the template block, add workflow-specific behavior (if any): custom advance actions, `auto` milestone names, custom marker-lifecycle exceptions, hard gates that `auto` does not bypass.

### Process-flow house style

`Guides/Core/process-flow.md` is the **house style reference** for process-flow mechanics. It is the canonical definition used by maintainers to ensure consistency across guides. It is NOT a runtime reference that agents read during workflow execution.

The operational core is inlined in each guide using the standard template above. When process-flow house style changes:
1. Update `Guides/Core/process-flow.md` (the canonical definition).
2. Update the standard template in this section.
3. Propagate the template changes to all workflow guides.

**What guides should contain (inline):**
- The applicable gate and advance-intent invariants under the explicitly declared control model, using the default template where applicable
- Workflow-specific gate descriptions, phase sequencing, `auto` skip/fix rules
- Workflow-specific procedures, examples, and reference material

**What guides should NOT contain.** Most of these are enforced by a corresponding sanity-scan check ([`guide-authoring.md` § Sanity scan](guide-authoring.md#sanity-scan-after-every-guide-edit)); where a sanity-scan reference is given on a bullet, the authoritative rule phrasing lives there. The list here is for awareness during authoring.

- References to `Guides/Core/process-flow.md` as a required runtime read — sanity scan: "Process-flow template compliance" / "References to `Guides/Core/process-flow.md` that imply it is a required runtime read."
- "Flow" or "Process Overview" subsections that embed checkpoint behavior or marker-clearing steps alongside phase sequencing — state only which phases exist and their order.
- Standalone "Progress Tracking" or "Emoji System" sections that redefine the canonical marker conventions — sanity scan: "Process-flow template compliance" / "Standalone 'Progress Tracking' or 'Emoji System' sections that redefine the canonical marker conventions."
- Inline restatements of marker-clearing timing unless gated on advance intent — sanity scan: "Flow control integrity" / "Any 'remove 🟡' or 'check the box' language…"
- Discussion items in aggregator sections (`## Questions`, `## Decisions`, etc.) instead of inline with their topic — sanity scan: "Marker convention compliance" / "Discussion items in aggregator sections…"

### Flow reflection (required for guides with gates)

After editing a guide with gates, imagine a fresh agent using it from the start of the workflow and mentally step through the first few supervisor/agent exchanges plus each gate transition.

Required post-edit simulation:
- Explicitly simulate at least:
  - one normal transition
  - one blocked case
  - one `auto` case
- If the simulation exposes a gap, patch the guide immediately and re-run the affected simulation.
- If the simulation exposes no issues, record `No issues found in simulation` in the active working notes before moving to the next guide.

For each stop, verify:
- why the agent is stopping
- the exact `⏳ GATE:` line the agent should emit
- what supervisor response resumes the workflow
- whether that response is advance intent, local approval, or some other workflow-specific action
- which workflow-owned artifact is tracking that gate or phase
- which marker/state the declared model uses while waiting; Discussion-only models may retain resolved D items at their planned gate rather than add a new pending marker
- what marker changes on resolution, and only after what supervisor intent
- what exact artifact change happens after that supervisor intent

Look specifically for:
- waits on the supervisor that do not end with a `⏳ GATE:` line
- gates where `Next` is unclear or misleading
- planned gates without a workflow-owned artifact or explicit state/marker lifecycle; do not invent a pending phase marker for a documented Discussion-only model
- marker clearings that happen before approval
- non-standard gates whose custom semantics are implied but not stated
- top-level summaries that do not match the actual gated sequence

### Pre-edit workflow model (required for guides with gates)

Before rewriting a guide with gates:
- Extract the workflow model first:
  - happy-path progression
  - workflow-owned artifact(s)
  - marker lifecycle
  - blocker categories
- Simulate at least:
  - one normal transition
  - one blocked/tooling failure
  - one ambiguity/spec flaw
  - one `auto` case
- Only then apply the standardized gate/advance-intent template.
