Managed-By: skai
Managed-Id: guide.work-spec-creation
Managed-Source: Guides/Spec/work-spec-creation.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-05-27

# Work Specification Guide

## Purpose

Orchestrates the work specification creation process. Work specifications provide structured documentation for complex coding tasks that require multiple steps, coordination between components, and careful planning. They serve as both implementation roadmaps and progress tracking tools.

**Key Principles:**
- **Agent-sufficient document**: A fresh agent should be able to implement by reading this spec *and* following the explicitly listed inputs (referenced docs/files/links). No implicit context.
- **Communication Tool**: Describes what code to write, not how to write it
- **No Code**: Contains no actual code - only descriptions of what needs to be implemented

**Overall Process:**
1. **Planning Document Draft + Discussion**: Summarize the scope discussion into a planning document seeded with `- [ ]` discussion items (canonical Structured discussion items schema — see `Guides/Core/process-flow.md`). Resolve the items collaboratively; while any remain unresolved, the workflow is at a blocked gate.
2. **API Sketch**: Capture the non-private API surface implied by the resolved planning discussion.
3. **Requirements Normalization**: Hand the behaviors discovered during planning to requirements authoring, which captures them in a change package.
4. **Work Spec First Pass**: Write high-level tasks only (no subtasks) for review.
5. **Work Spec Second Pass**: Add detailed subtasks after approval.

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
- The Planning-discussion gate uses the canonical Discussion-phase gate behavior (see `Guides/Core/process-flow.md`, "Structured discussion items"): while any `- [ ]` discussion items remain in the planning document, the workflow emits a blocked gate citing the remaining count; the moment every item is resolved (`- [x]`), the agent emits the first planned gate to advance to API sketch.
  - Blocked: `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to the API sketch.`
  - Planned: `⏳ GATE: Next: Discussion complete. Say "next" to advance to the API sketch.`
- There is no separate "planning draft is ready, please review" gate. The drafting response itself ends with whichever gate applies — blocked (typical) or planned (when the draft produced zero items because inputs fully specify the work).

Progress tracking:
- Default marker convention: `- [ ]` / `- [x]` in the planning document and the work spec (process artifacts). See `Guides/Core/process-flow.md`, "Progress markers".
- Default rule: a `- [ ]` item means TODO or pending approval. Do not clear it without human approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned markers completed by the phase that just finished.
- Workflow-specific exception — planning discussion: `- [ ]` items in the planning document are resolved one at a time during the discussion phase, not at a planned gate. Check the box (`- [x]`) and append `- **Decision** <resolution>.` only after the human explicitly approves that specific item.
- Workflow-specific note — work-spec task markers: the second pass creates `- [ ]` task markers (with stable IDs `T1`, `T2`, …) in the work spec, but this workflow does not check them. They are checked off later by the implementation workflow.

Planned gates for this workflow:
- After all planning-discussion items are resolved (the first planned gate — emitted on resolution of the last item; advances to API sketch).
- After completing the API sketch (human confirms readiness to proceed to requirements normalization).
- After requirements normalization has produced a change package (human acknowledges before proceeding).
- After the work spec first pass (high-level tasks only) for review.
- After the work spec second pass (subtasks + traceability) for review.

---

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the active-phase rules below. Do not use them to skip phases or clear unrelated progress markers.

Workflow-specific behavior — planning discussion:
- After the planning document is drafted, the human begins resolving items by responding to them directly (commenting, answering, refining, redirecting). That conversational engagement is local to each item; the agent updates the document accordingly. It is *not* advance intent for the workflow as a whole.
- Each item resolves on the human's explicit approval of that specific item — check the box and append `- **Decision** <resolution>.` See canonical Resolution rules.
- The workflow advances to API sketch only at the first planned gate (the discussion-complete gate), reached when every item is `- [x]`.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit human resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Valid milestones in this workflow: `planning discussion complete`, `api sketch complete`, `requirements normalization`, `work spec first pass`, `work spec second pass`.

**Behavior:** Context determines the action. The same command drives every phase of the process; the agent infers which step to execute based on the current state of the conversation and any existing documents.

**Workflow-specific `auto` rules:** `auto` can be useful after the planning discussion is complete and the API sketch is approved, to batch requirements normalization, work spec first pass, and work spec second pass. If the planning document still has unresolved `- [ ]` items, this workflow is blocked on human decisions and `auto` does not bypass the blocked gate.

**Phase actions when the human says "begin", "next", or "continue":**

- **Planning — Create Planning Document:** summarize the scope discussion into a planning document; seed it with `- [ ]` discussion items per the canonical Structured discussion items schema; end the response with the discussion-phase blocked gate (or the discussion-complete planned gate if zero items were needed).
- **Planning — Resolve Open Items:** continue the iterative discussion, updating the document as decisions are made. Each response re-emits the current blocked gate verbatim per the persistence rule, with the count updated to reflect remaining items.
- **Planning — API Sketch:** after the discussion-complete planned gate is approved, write the API sketch using the resolved planning document as input.
- **Requirements Normalization:** after the API sketch gate is approved, hand the planning document's behaviors to requirements authoring; it produces the change package.
- **Work Spec — First Pass:** create work specification with high-level tasks only (no subtasks, no Traceability). Allows human to review overall sequence before details.
- **Work Spec — Second Pass:** add detailed subtasks, `- [ ]` task indicators with stable IDs, and the Traceability section.

---

## Planning Phase

Before writing a work spec, the design must be worked through in a planning document. The planning phase begins by drafting the planning document, then proceeds through two stages: Stage 1 discussion and Stage 2 API sketch.

**Prerequisite:** An informal scope discussion has already taken place (in chat, a meeting, a Jira ticket, etc.). The human and agent have discussed the problem space -- what is being solved, motivating use cases, scope boundaries, and affected architecture. The human enters the planning phase when they are ready to formalize the discussion into a planning document (e.g., "begin planning").

**Creating the planning document** (begin/next/continue):
1. Summarize the scope discussion so far (Problem, Current Architecture, initial approach framing).
2. Seed the document with `- [ ]` discussion items per the canonical Structured discussion items schema (see `Guides/Core/process-flow.md`). Each item is `- [ ] D<n> [Kind] <summary>` with `[Question]` / `[Proposal]` / `[Tradeoff]` as the Kind, placed inline under the topic it concerns.
3. End the drafting response with the discussion-phase gate — blocked if items remain, planned (discussion-complete) if zero items were needed because inputs fully specify the work.

### Stage 1: Ideation, Questions, Discussion

Work through the design collaboratively. The agent proposes design elements and the human refines, redirects, or approves.

**Schema:** This stage uses the canonical Structured discussion items schema (see `Guides/Core/process-flow.md`, "Structured discussion items"). In summary:

- Item line: `- [ ] D<n> [Kind] <summary>` — letter-led ID (`D1`, `D2`, …), `[Question]` / `[Proposal]` / `[Tradeoff]`, plain-language summary.
- Sub-bullet labels (bold, no separator): `Concern` (always), `Proposal` or `Question`, `Options` (for `[Tradeoff]`), `Detail`, `Why`, `Decision` (added on resolution).
- The agent always takes a position — every item carries a recommendation, and a `[Tradeoff]` names which option it picks.

**Drafting rules (workflow-specific):**

- The agent MUST seed the conversation with proposals. The planning doc is not a passive transcript — it must contain concrete `[Proposal]` / `[Tradeoff]` items that move the design forward.
- IDs (`D1`, `D2`, …) are continuous across the entire Discussion section, not reset per topic. Once assigned, an ID is never renumbered.
- Tight lists: where two or more `- [ ]` items sit under the same topic heading, leave no blank line between them.

**Topic-organized, items inline** (per canonical):

- Each topic is its own `###` subsection inside `## Discussion` (or under a phase section, see Phased planning below).
- The topic's `- [ ]` items live directly inside it.
- Do NOT create aggregator sections (`## Questions`, `## Decisions`, `## Tradeoffs`, `## Open Items`). The marker count across the discussion = the number of real decisions; aggregator sections break that property by pulling items out of their topics.

**Resolution** (per canonical):

- On the human's explicit approval of an item, check the box (`- [x]`) and append `- **Decision** <succinct resolution>.` as the last sub-bullet.
- The original question/proposal stays visible — the decision is appended, not substituted.
- Do not clear an item preemptively. Only check the box when the human has explicitly decided.

**Discussion-phase gate behavior** (per canonical, repeated here for clarity):

- While any `- [ ]` items remain: blocked gate at the end of every response.
  - `⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to proceed to the API sketch.`
- When every item is resolved: planned gate (the first planned gate of the workflow).
  - `⏳ GATE: Next: Discussion complete. Say "next" to advance to the API sketch.`

**Recommended planning document shape:**

- Problem / goal
- Current architecture / constraints (if relevant)
- Discussion (one `###` topic per major area)
  - Each topic contains:
    - brief context
    - one or more `- [ ]` discussion items, per the canonical schema
    - any non-goals / deferrals explicit to that topic

Example topic (unresolved):

```
### Data model

The notes feature needs a schema that supports multiple note kinds (full notes, quick notes, peeks).

- [ ] D1 [Proposal] Use a single notes table
  - **Concern** Three kinds means we either need three tables (clean separation, cross-table joins) or one table with a kind column (compact, mixed concerns).
  - **Proposal** One table with a `kind` column.
  - **Why** Avoids cross-table joins; migration stays a single schema change.
- [ ] D2 [Tradeoff] Where does the `kind` field default live?
  - **Concern** Defaults could live in the schema (DB-level default) or the model layer.
  - **Options**
    - A — DB-level default (`kind` column defaults to `note`)
    - B — Model-layer default (the type constructor supplies it)
  - **Proposal** B (model-layer) — keeps the DB schema agnostic of business semantics.
  - **Why** A future kind change is a code-only edit; no migration needed.
```

After resolution:

```
- [x] D1 [Proposal] Use a single notes table
  - **Concern** Three kinds means we either need three tables (clean separation, cross-table joins) or one table with a kind column (compact, mixed concerns).
  - **Proposal** One table with a `kind` column.
  - **Why** Avoids cross-table joins; migration stays a single schema change.
  - **Decision** Approved as proposed. Single table with `kind` column.
- [x] D2 [Tradeoff] Where does the `kind` field default live?
  - **Concern** Defaults could live in the schema (DB-level default) or the model layer.
  - **Options**
    - A — DB-level default (`kind` column defaults to `note`)
    - B — Model-layer default (the type constructor supplies it)
  - **Proposal** B (model-layer) — keeps the DB schema agnostic of business semantics.
  - **Why** A future kind change is a code-only edit; no migration needed.
  - **Decision** B — model-layer default. Keeps the migration window short.
```

**Optional: phased planning documents (only when the plan is large):**

Sometimes the planning grows large enough that it should be executed in phases. In that case, the planning document is still a single document, but it is structured so each phase has its own planning and API sketch content for traceability.

Rules:
- Default: no phases. Use phases only when the human or agent proposes them and there is an informal agreement on the phase breakdown.
- Phase sections MUST come last in the document (after any global planning content).
- Global planning content MAY exist before phase sections. Later phases may augment or supersede earlier decisions, but do not rewrite earlier phase sections.
- Each phase runs its own mini-cycle in order:
  1. Proposals, questions, discussion (Stage 1)
  2. API sketch (Stage 2)
  3. Requirements normalization
  4. Work spec writing
- Process-flow note: when Phase N is complete, the next step is to begin Phase N+1 (or conclude if there are no more phases).
  - Stopping condition: at the end of Phase N's cycle, STOP and output the standard gate line. The "Next" step should be "Begin Phase N+1" (or "Complete" if there are no more phases).
  - Advance intent at that point is the signal to initialize Phase N+1's Stage 1 discussion content (seed proposals/questions under that phase section).
- Phase sections can start as lightweight placeholders (scope, rough idea). When it is time to begin a phase, the human tells the agent to initialize the phase's discussion content.

Recommended phased planning shape:
- Overview / global context (optional)
- Global topics (optional)
- Phase sections (last):
  - `## Phase 1: <name>`
    - `### Scope` (goal, in-scope, non-goals, dependencies, exit criteria)
    - `### Stage 1: Proposals, questions, discussion` (`- [ ]` items until resolved)
    - `### Stage 2: API sketch` (API "as of Phase 1")
    - `### Requirements normalization` (what this phase hands to requirements authoring)
    - `### Work spec` (link to this phase's work spec)
    - `### Supersedes / changes vs earlier phases` (optional; explicit notes when Phase N counteracts Phase < N)
  - `## Phase 2: <name>` (repeat the same shape)

**Discussion principles:**
- Present findings and analysis, not pre-selected options. The human is the architect.
- When the human asks a question, answer it directly -- do not reframe it as a choice between options you've invented.
- Use concrete scenarios (design-by-use-case) to drive design decisions rather than abstract analysis.
- Capture the resolution in the appended `- **Decision**` sub-bullet; the prior `Concern` / `Proposal` / `Why` lines remain visible so the reasoning trail is preserved.

### Stage 2: API Sketch

Refine the design to the level of non-private API surfaces -- the interfaces through which components in the system connect and interact. This bridges the gap between high-level decisions and the work spec's implementation tasks.

**API sketch conventions:**
- Show APIs in the context of their enclosing type. Do not write isolated function signatures; instead write the type signature with the relevant member(s) enclosed within it.
- **New types/members**: Show the type and its new members.
- **Unchanged APIs**: Omit entirely -- do not list them, do not comment on their absence. Omission *is* the signal that the API is unchanged.
- **Protocol conformances**: When a protocol gains new members, do not repeat the signatures on conforming types. List the conforming types that need updating as a comment, but do not restate the API.
- **Removed APIs**: Show in the context of the enclosing type with ~~strikethrough~~ formatting.
- **Modified APIs**: Show the old signature with ~~strikethrough~~ immediately followed by the new signature.
- **API documentation**: Include doc comments on all new and modified APIs. The sketch is the first place these are written and they carry forward into implementation.
- **Code block formatting**: Use fenced code blocks with the language identifier (e.g., ` ```swift `) for syntax highlighting.

**Example:**

```swift
protocol Storing {
    ~~func save(_ output: StorageOutput, id: String) throws~~
    func save(_ output: StorageOutput, id: String, context: PerformContext) throws
    func loadFile(_ reference: FileReference) throws -> Data    // new
}

struct FileReference: Codable {                                 // new type
    let filename: String
    let type: FileType
}
```

Output: the planning document's "API Sketch" or equivalent section describes the non-private surface area -- types, protocols, and their relationships -- with enough specificity that a work spec can reference them.

Gate: when the API sketch is complete, STOP at the planned gate. `Next` advances to requirements normalization.

### Planning Document Completeness

The planning phase is complete when:
- Every `- [ ]` discussion item in the planning document is `- [x]` with a `- **Decision**` sub-bullet.
- The key types and their relationships are described.
- The design has been validated against concrete use cases.
- The human confirms readiness to proceed to requirements normalization.

If the planning document uses phases:
- The overall planning phase may remain intentionally incomplete for later phases.
- For the current phase to proceed to requirements normalization, that phase section must have:
  - every `- [ ]` discussion item in the phase resolved (`- [x]` with `- **Decision**`), and
  - an API sketch for the phase, and
  - the human's approval to proceed with that phase.

Gate: STOP and output the planned gate line.

---

## Requirements Normalization Step

After the planning phase is complete, the product and system behaviors discovered during planning are
captured as requirements — into a **change package**, never written directly into the catalog.

This workflow does not author requirements itself. Hand off to
[`../Requirements/requirements-authoring.md`](../Requirements/requirements-authoring.md), which owns
mode inference, the discussion over what planning left undecided, and the typed change items. The
content rules — scopes, layout, requirement format, IDs, writing style — live in
[`../Requirements/requirements-catalog.md`](../Requirements/requirements-catalog.md).

The package is promoted when this work ships, by
[`../Requirements/requirements-promotion.md`](../Requirements/requirements-promotion.md), which is the
only writer of the requirements catalog. Requirement IDs are assigned when the package is drafted, so the
work spec can cite them before they are canonical.

Unlike the retro's requirements handoff, this one is **not terminal**: requirements authoring ends
with its own `🏁`, and this workflow then resumes at its next gate, with the package's IDs available
to cite in the work spec. Under repository shape `none` this project keeps no catalog, so the step
and its gate are skipped rather than handed off — authoring's stop under `none` is terminal and would
not return here.

Gate: STOP and output the planned gate line.

---

## File Naming Convention

Work specification and planning files are working documents. Create them following `Guides/Core/working-doc-conventions.md`.

**Planning Document:**
- Session name: `[spec-name]`
- Subpath: (none)
- File name: `[spec-name]-plan.md`
- Full path: `skai/working-docs/<branch-path>/[spec-name]/[spec-name]-plan.md`

**Work Spec Document:**
- Session name: `[spec-name]`
- Subpath: (none)
- File name: `[spec-name]-impl.md`
- Full path: `skai/working-docs/<branch-path>/[spec-name]/[spec-name]-impl.md`

Where `[spec-name]` = the specification name for this workflow session (e.g., `observable-wrapper`). In this workflow, `[spec-name]` serves as the required `session-name` from `Guides/Core/working-doc-conventions.md`, and is also used as the filename prefix so working docs are distinguishable per spec in editor quick-open.

**Examples** (branch: `work/step-refactor`):
- Planning: `skai/working-docs/work/step-refactor/observable-wrapper/observable-wrapper-plan.md`
- Work Spec: `skai/working-docs/work/step-refactor/observable-wrapper/observable-wrapper-impl.md`

## Structure

### 1. Title
Use a clear, descriptive title that captures the main objective:
- ✅ "Crosshairs-Directed Tractor Beam System"
- ❌ "Update Tractor Beam"

### 1.5 Inputs (Required Reading)
At the top of the work spec, list every document/file a fresh agent must read to execute the spec without guessing.

- Planning doc(s) (paths)
- Related work specs (paths), if any
- Key implementation files/folders (paths) for existing conventions
- Any external docs (links), if truly required

### 2. Motivation Section
Explain **why** this work is needed:
- Current limitations or problems
- Desired end state and benefits
- How the change improves user experience or system architecture

### 3. Functional Requirements Section
Break down **what** needs to change into logical categories:
- Group related changes together
- Focus on functional outcomes, not implementation details
- Use bullet points for clarity

### 3.5 Requirements Inventory (Reference + Local, Anti-Omission Mechanism)

To avoid missing requirements from planning, include an inventory with stable IDs.

This inventory is split into two scopes.

#### Canonical requirements (by reference only)
- List only IDs from the canonical requirements catalog or from the change package this spec's planning produced (e.g. `DOC-02`, `PROMPT-04`).
- Mark an ID that is not yet promoted as `(pending)` — it is citable but not yet canonical, and becomes canonical when the package is promoted as this work ships.
- Do NOT restate or redefine their content here.
- Do NOT use progress markers — these are reference IDs, not work items.

#### Work-spec requirements (technical / transitional)
- Each local requirement is a `- [ ]` item with a stable letter-led ID (e.g. `DATA-01`, `MIG-02`, `TEMP-01`).
- These may describe technical or implementation-level decisions.
- The implementation workflow checks each one (`- [x]`) when fully satisfied by a completed task.

**Rules:**
- Inventory must be complete (capture all technical requirements + constraints + deferred / non-goal items introduced by this work).
- Tasks and subtasks must cite requirement IDs.

### 3.6 Non-goals / Deferred
Explicitly list anything deferred/out-of-scope from planning (also with IDs), so it can't disappear.

### 4. Relevant Files Section
List files that will be modified, organized by importance:
- **Core Implementation**: Files central to the main changes
- **Supporting Files**: Files requiring minor updates or configuration changes

### 5. Task List Section
The heart of the specification - actionable implementation steps.

### 5.5 Traceability (Requirement ↔ Task)
Include a short mapping section that ensures every requirement is implemented or explicitly deferred:

- Each requirement ID maps to at least one task, or to a deferred/non-goal item
- No "orphan" tasks (tasks should point back to at least one requirement ID)

## Task List Guidelines

### Task Structure

```markdown
- [ ] T1 **Task Name**
  - **Done when:** [Short, stable completion criteria]
  - **Implementation**
    1. Sub-task description (REQ-ID)
    2. Sub-task description (REQ-ID)
  - **Verification**
    3. Run <command(s)> and define what "pass" means (REQ-ID) [evidence: ...]
```

Tasks are `- [ ]` items with a stable letter-led ID (`T1`, `T2`, …) — letter-led so a leading digit isn't misparsed as an ordered-list item. IDs are sequential in document order, never renumbered, and removing a task retires its ID. Sub-tasks use indented numbered lists; reference them as `T<n>.<m>` (e.g., `T1.2` is task T1, sub-task 2). Number sub-tasks sequentially across Implementation and Verification.

Only mark main tasks with `- [ ]` (sub-tasks are not separately tracked). The implementation workflow checks the box on each task as it completes.

### Task Naming
- Use descriptive action-oriented names
- Focus on what will be accomplished, not how
- Examples: "Update Configuration Model", "Implement Coordinate Conversion"

### Sub-task Numbering
- Use indented numbered lists for sub-tasks; the N.N reference (e.g., 1.1, 2.3) is implied by the task number and sub-task position
- Makes it easy to reference specific items during implementation
- Enables precise progress tracking

### Task Scope
- Each task should be implementable in a single focused session
- Break large tasks into smaller, manageable pieces
- Aim for 3-6 sub-tasks per main task
- Default expectation: each top-level task leaves the codebase in a runnable state for its verification whenever practical (build/tests).
  - Allowed exception (explicit in the work spec): **Refactor tranche** -- a small sequence of top-level tasks that may temporarily break compilation, but must end with a **Green Gate** task/subtask that restores compilation and runs the relevant verification commands.

### Task Dependencies
- Order tasks logically based on dependencies
- Earlier tasks should provide foundation for later ones
- Consider data flow and component relationships

## What to Include

### ✅ Implementation Tasks
- Code changes and refactoring
- Data structure updates
- Algorithm modifications
- Configuration changes
- Documentation updates

### ✅ Integration Tasks
- Connecting components
- Updating interfaces
- Coordinate space conversions
- API modifications

### ✅ Verification Tasks
- Ensuring correct integration
- Validating data flow
- Checking for linter errors
- Confirming expected behavior
  - Verification subtasks are mandatory for each top-level task (build/test/lint as applicable).
  - Source of truth for project-specific commands/paths is `skai/integration.md` (do not invent commands).
  - Evidence must be captured inline on the verification subtask line using an evidence bracket:
    - Format: `[evidence: <command variant>; exit <code>; output: <optional link(s)>]`
    - Example: `[evidence: <command>; exit 0; output: [output](skai/working-docs/<branch-path>/<spec-name>/work-spec/evidence/<slug>.txt)]`
    - On failure: persist full output to a file and link it.
    - On success: a linked output file is optional; still record command variant and exit code inline.

## What to Exclude

### Unit Testing Tasks (optional; ask first; last)

Work specs may or may not require unit testing (e.g., some teams don't unit test view/UI code).

Rules:
- The agent MUST ask the human what unit testing (if any) is required for this work.
- If unit testing is required, add unit testing tasks at the END of the task list.
  - Keep them high-level (what to test and where), and defer the detailed testing workflow to the Unit Testing guides.

### ❌ Deployment Tasks
- Build configuration
- Release preparation
- Environment setup
- Production deployment

### ❌ External Dependencies
- Third-party library updates
- System configuration changes
- Infrastructure modifications

## Writing Style

**Scope note:** This section applies to **work specifications** (tasks, subtasks, and work-spec requirements), not to the canonical requirements catalog.

### Be Specific
- ✅ "Add `deviceDistance: Float` field to `TractorBeamConfig` (default: 0.1)"
- ❌ "Update configuration"

### Use Active Voice
- ✅ "Replace `cameraToPrizeDirection` with `player.aim`"
- ❌ "The camera direction should be replaced"

### Focus on Outcomes
- ✅ "Calculate camera-to-crosshairs direction vector for `player.aim`"
- ❌ "Do some math to figure out the direction"

### No Code Examples
- ✅ "Add `deviceDistance` parameter with default value 0.1"
- ❌ "Add `var deviceDistance: Float = 0.1` to the struct"

### Standalone Clarity
- Provide enough context that implementation can proceed without questions *after reading the Inputs section*
- Define what each component should do and how they should interact
- Explain the purpose behind each change

### Maintain Abstraction Levels
- Keep implementation details in sub-tasks
- Main tasks should describe functional goals
- Avoid mixing high-level and low-level concerns

## Example Template

```markdown
# [Feature/System Name]

## Inputs (Required Reading)
- [Planning doc path]
- [Other referenced docs/specs/links]
- [Key files/folders to inspect for conventions]

## Motivation
[Why this work is needed - current problems and desired outcomes]

## Functional Requirements
### [Category 1]
- [Requirement description]
- [Requirement description]

### [Category 2]
- [Requirement description]
- [Requirement description]

## Requirements Inventory

### Canonical requirements (by reference only)
- DOC-02
- PROMPT-04

### Work-spec requirements (technical / transitional)
- [ ] CAT-A-01 ...
- [ ] CAT-A-02 ...
- [ ] CAT-B-01 ...

## Non-goals / Deferred
- DEFER-01: ...

## Relevant Files
### Core Implementation
- `path/to/main/file.swift` - [Brief description of changes]
- `path/to/other/file.swift` - [Brief description of changes]

### Supporting Files
- `path/to/config/file.swift` - [Brief description of changes]

## Task List

- [ ] T1 **[Task Name]**
  - **Done when:** [Behavioral + verification-based completion criteria]
  - **Implementation**
    1. [Specific sub-task] (CAT-A-01)
    2. [Specific sub-task] (CAT-A-02, CAT-B-01)
    3. [Specific sub-task] (DEFER-01 if deferring something explicitly)
  - **Verification**
    4. [Run command(s) from integration doc; define "pass"] (CAT-A-01) [evidence: exit 0; output: [log](skai/working-docs/<branch-path>/<spec-name>/work-spec/evidence/<slug>.txt)]
- [ ] T2 **[Task Name]**
  - **Done when:** [Behavioral + verification-based completion criteria]
  - **Implementation**
    1. [Specific sub-task] (CAT-A-01)
    2. [Specific sub-task] (CAT-B-01)
  - **Verification**
    3. [Run command(s) from integration doc; define "pass"] (CAT-B-01) [evidence: exit 0; output: [log](skai/working-docs/<branch-path>/<spec-name>/work-spec/evidence/<slug>.txt)]
- [ ] T3 **[Task Name]**
  - **Done when:** [Behavioral + verification-based completion criteria]
  - **Implementation**
    1. [Specific sub-task] (CAT-A-02)
    2. [Specific sub-task] (CAT-A-02)
    3. [Specific sub-task] (CAT-B-01)
  - **Verification**
    4. [Run command(s) from integration doc; define "pass"] (CAT-A-02) [evidence: exit 0; output: [log](skai/working-docs/<branch-path>/<spec-name>/work-spec/evidence/<slug>.txt)]

## Traceability
- CAT-A-01 → T1, T2
- CAT-A-02 → T1, T3
- CAT-B-01 → T1, T2, T3
- DEFER-01 → Non-goals / Deferred
