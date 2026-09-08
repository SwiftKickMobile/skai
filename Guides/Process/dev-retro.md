Managed-By: skai
Managed-Id: guide.dev-retro
Managed-Source: Guides/Process/dev-retro.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# Dev-session retro (agent + operator)

Purpose: a completeness backstop for an LLM-driven development session in a host repo. This retro covers **everything since the previous dev retro** (if any); if none, it covers the current session.

Do not do a git/diff report unless asked. Prefer evidence-backed review and consistency checks.

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
- The requirements handoff is a non-standard planned gate, emitted only when step 5 seeded a change package. `Next` there means: hand that package to `Guides/Requirements/requirements-authoring.md`, where that workflow will own resolving the discussion items and, in turn, promotion. Retro never resolves them itself and never writes the catalog.
- At that handoff gate, the seeded package is the handoff artifact. Its unchecked `- [ ] D<n>` items remain pending while waiting for the operator.
- The ticket-filing handoff is a non-standard planned gate. `Next` there means: hand the current SKAI process suggestions to `Guides/Process/ticket-filing.md`, where that workflow will own ticket drafting, review, and filing.
- At that handoff gate, the retro output's `SKAI process suggestions` section is the handoff artifact. The unchecked `- [ ]` suggestion items there remain pending while waiting for the operator to approve drafting.
- **Both handoffs come after the full retro output is prepared, and the requirements handoff comes first.** Complete all six checklist steps before emitting either gate: step 6's reflection can be informed by what step 5 found, and a half-run retro should never be left open while its handoffs are worked.
- Emit one handoff gate at a time. Taking the requirements handoff enters another workflow and the retro does not resume afterwards — so when both handoffs are pending, say so in the summary at the first gate. The retro output is what keeps the second discoverable: its unchecked `- [ ] S<n>` items remain, and the operator takes that handoff by invoking ticket filing when ready.

Planned gates for this workflow:
- After the retro output is prepared and step 5 seeded a change package, but before handing it off to requirements authoring. Skipped when step 5 found nothing.
- After the retro output is prepared and SKAI process suggestions have been identified, but before handing them off to the ticket-filing workflow for drafting.

Workflow-specific blocked gates:
- Required session artifacts are missing or cannot be located, so the retro cannot be completed with evidence.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-phase rules below. Do not use them to skip required review or filing decisions.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit operator resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking:
- Default marker convention: `- [ ]` / `- [x]` in the retro output (process artifact). See `Guides/Core/process-flow.md`, "Progress markers".
- Default rule: a `- [ ]` item means TODO or pending approval. Do not check it without operator approval.
- This guide does not require a separate phase marker for ordinary retro work.
- If SKAI process suggestions are generated, the workflow-owned handoff artifact is the retro output's `SKAI process suggestions` section.
- In that section, each suggestion is a `- [ ]` item with a stable letter-led ID (`S1`, `S2`, …). The unchecked state shows it is pending handoff into the drafting workflow.
- At the ticket-filing handoff gate, STOP with the suggestion items still unchecked.
- If the operator gives advance intent at that handoff gate, transfer control to `Guides/Process/ticket-filing.md` starting at Phase 1, step 2 using the unchecked `S<n>` suggestions as the draft inputs.
- Do not draft `process-tickets.md` in this guide. `Guides/Process/ticket-filing.md` owns ticket drafting, review, and filing.

Workflow-specific advance behavior:
- `auto` may complete the retro itself and may develop suggestions, but if any SKAI process suggestions were identified it must still STOP at the ticket-filing handoff gate.
- Use `draft process tickets` as the stable bounded-auto target for this guide's planned handoff gate.

## Inputs (read what exists)

Read the documents and artifacts that were produced or used during this session, as applicable:

- The **plan** for the session:
  - work spec doc(s) (if used)
  - planning docs / analysis docs (including unit-testing planning + infrastructure + writing work docs)
- The project's Integration doc:
  - `skai/integration.md`
- Evidence artifacts produced during the session:
  - build/test outputs, logs, result bundles/reports, screenshots/screen recordings, crash reports, etc.
- The canonical requirements catalog:
  - the requirements catalog, at the root named in `skai/integration.md`'s `Section: requirements`
    block — not a literal path, which is wrong under the `shared` shape
- Open requirements change packages:
  - `skai/changes/*/requirements-authoring.md` — behavior already captured but not yet promoted. Read these before step 5 so it does not re-raise what is already pending.

If any of these inputs are missing but required to perform the retro, STOP and ask the operator where they are.

## Retro checklist

### 1) Self-review (evidence-backed)

- Summarize what was attempted and what was achieved.
- For each key outcome, cite the best available evidence:
  - tests passing/failing + artifacts
  - logs / screenshots / crash output
  - observable behavior changes

### 2) Gaps and flaws

Identify:
- what might still be wrong (known unknowns)
- what assumptions were made
- what risks remain

For each gap, propose the smallest next verification step (or STOP and ask the operator for required evidence).

### 3) Plan drift / consistency

If the session deviated from the documented plan(s):
- Update the plan docs so they match reality (or explicitly record why the plan changed).
- Ensure the "next steps" reflect the new reality.

### 4) Documentation updates (only what changed)

If the session changed behavior, conventions, or integration details:
- Update the most relevant docs (choose the minimum set):
  - code comments where correctness depends on subtle behavior
  - README / developer docs
  - integration doc values/commands (inside managed blocks only, if using `skai` Integration format)
  - process docs/runbooks (if a repeatable workflow changed)

If you are not confident what should be documented, STOP and ask the operator what level of documentation is expected.

### 5) Product requirements backfill (retro requirements)

Goal: if the session discovered or clarified externally observable behavior, capture it so the catalog can reflect it.

Detection is this step's work, and it is unchanged:
- Infer externally observable or cross-component behavioral contracts from the code + evidence from this session.
- Compare them to the existing catalog and to any open change package. Under shape `none` this
  project keeps no catalog, so step 5 seeds nothing.
- Identify what is missing, and what is recorded but now incorrect or outdated.

**Retro does not write the catalog.** Findings are seeded into a change package at `skai/changes/<change-id>/`, per `Guides/Requirements/requirements-authoring.md` — draft requirement files plus a `## Discussion` holding what this session could not settle as `- [ ] D<n>` items. Write the requirement under the recommended reading and cite its item rather than leaving a hole; content rules are in `Guides/Requirements/requirements-catalog.md`.

If a package for this work is already open, add to it rather than creating a second. If the session found nothing, create no package and skip the requirements handoff gate.

Retro seeds and hands off. It does not resolve discussion items and it does not promote; both belong to the requirements workflow.

### 6) Process reflection

Reflect on the session since the last retro (or since session start). Consider:

- **Pattern violations**: Did you break an established convention or project pattern? What cue did you miss, and what check would have caught it earlier?
- **Recurring friction**: Were there repeated failures (e.g., build issues, test flakiness, tooling problems, unclear requirements) that a process or infrastructure change could prevent?
- **Missing knowledge**: Did you lack context that a rule, skill, or documentation improvement would provide?
- **Documentation gaps**: Are there undocumented invariants, conventions, or patterns that you had to learn the hard way or that the operator had to explain?
- **Operator corrections**: Did the operator have to point out something you should have caught yourself? What was the root cause -- a missing check, a missing convention, or a gap in your understanding of the project?

Output is two sections in the retro output, written directly as you reflect (not brainstormed then sorted).

#### Session observations

Agent behavior issues, project-specific friction, one-off observations, or problems outside the skai repo's scope. These are worth noting for the operator but do not belong in the skai issue tracker and do not flow into the ticket-filing handoff.

Format: brief bullets, no progress markers. If none, say **"None."**

#### SKAI process suggestions

Process, tooling, or documentation improvements to the skai framework itself (guides, templates, skills, policies, install runbooks). These belong in the skai repo's issue tracker.

Suggestion quality bar (problem-first; solution optional):
- Required for a ticket-worthy suggestion:
  - **Friction/problem** (concrete)
  - **Evidence/example** from the session (what happened)
  - **Failure mode** it prevents (what goes wrong if this repeats)
- Optional (only if confident):
  - **Candidate approach** (direction, not a mandate)
  - **Likely file(s)** to change (or "Unknown")
  - **Verification plan** (how to know next time)
- Hard rule: do not output suggestions that are purely abstract ("be more careful", "improve quality") without evidence and a verifiable check.

Format each as a `- [ ] S<n> <concise summary>` item (stable letter-led ID — `S1`, `S2`, …) with sub-bullets for the required details:
  - **Friction/problem** — concrete.
  - **Evidence/example** — what happened in this session.
  - **Failure mode** — what goes wrong if this repeats.
  - **Candidate approach** — optional; direction, not a mandate.
  - **Likely files** — optional; or `Unknown`.
  - **Verification** — optional; how to know next time.
- Do not draft `process-tickets.md` here.
- If none, say **"None."**

Example:

```
- [ ] S1 Retro forgets to scan README for stale paths
  - **Friction/problem** Three retros in a row missed a stale `Templates/` reference because the consistency check didn't run on README.
  - **Evidence/example** This session's retro skipped step 5 (consistency check) and shipped with a stale path.
  - **Failure mode** Stale paths in README slip into production until review notices them.
  - **Candidate approach** Add a README path-staleness check to `maintain-retro.md` step 5.
  - **Likely files** `maintain-retro.md`.
  - **Verification** Next retro flags the stale path; operator verifies.
```

## Retro output (keep it short)

Always start your message with a one-line declaration that the retro was performed:
- `Dev retro: DONE`

Then output only:
- what you fixed immediately (if any)
- remaining follow-ups (1-8 bullets)
- or: "Dev retro complete; no misses found."
- **Session observations** section from step 6 (brief bullets, no markers).
- **SKAI process suggestions** section from step 6 (with `- [ ]` items and `S<n>` IDs if any).
- If the "SKAI process suggestions" section has entries: end with `⏳ GATE: Next: Draft process tickets from these retro suggestions. Say "next" or what to change.`
- On advance intent from that gate, follow `Guides/Process/ticket-filing.md` starting at Phase 1, step 2.
