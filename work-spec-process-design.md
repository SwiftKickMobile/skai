# Work Specification Process Design

## Purpose

This document defines the intended replacement for SKAI's work-specification design (formerly
creation) and implementation processes. It is the standard used to write and cold-review the runtime
guides; it is not another guide an executing agent must read.

The modernization must make the guides smaller and the process more autonomous while preserving
operator control where expertise has the most leverage. The core process applies to software changes
generally, while its first optimization and validation target is feature work in existing mobile apps.

## Authority and references

Use these references when writing and reviewing the replacement guides:

- [`maintain-skai.md`](maintain-skai.md), especially Guide house style.
- [`Guides/Core/process-flow.md`](Guides/Core/process-flow.md) for gates, advance intent, markers,
  and structured discussion items.
- [`Guides/UIMap/ui-map-architecture.md`](Guides/UIMap/ui-map-architecture.md) and
  [`Guides/UIMap/ui-map-implementation.md`](Guides/UIMap/ui-map-implementation.md) for open-ended
  input, proposal-led discussion, a continuously updated review surface, ownership boundaries, and
  implementation dispositions.
- [`Guides/Requirements/requirements-authoring.md`](Guides/Requirements/requirements-authoring.md)
  and [`Guides/Requirements/requirements-promotion.md`](Guides/Requirements/requirements-promotion.md)
  for focused artifacts, inferred entry conditions, workflow ownership, and verification before a
  canonical write.

This document is authoritative for work-spec behavior. The existing work-spec guides are legacy
inputs when they conflict with it. Their API-diff notation, agent-sufficient inputs, task evidence,
and working-document placement remain useful where this design retains them.

## Complexity baseline

The normal case has one design document, one work spec, and two planned approvals. Optional review
material, additional artifacts, delivery slices, and specialized sub-processes are absent until the
work needs them. Do not emit empty boilerplate or add domain sections in anticipation of hypothetical
work.

Baseline recorded 2026-09-04, measured with `wc -c`:

- `Guides/Spec/work-spec-creation.md`: 33,863 bytes.
- `Guides/Spec/work-spec-implementation.md`: 11,649 bytes.
- Combined: 45,512 bytes.

The replacement guides have a combined size cap of **35,000 bytes**. Record each guide's size, the
combined size, and the delta from both the baseline and the cap after the first rewrite and every
refinement round. A real defect whose fix cannot fit is an operator decision rather than a silent overrun.

A proposed new gate, artifact, checklist, duplicated field, or proof burden is a complexity
tradeoff, not an automatic improvement. Simplification must not move required runtime instructions
into this document, replace actionable rules with vague references, or weaken evidence and safety
boundaries.

## Design invariants

### P1. Input is open-ended

The workflow may begin from a discussion, design, ticket, requirements, another specification,
source code, or any combination. The agent digests the available material, inspects the repository,
and infers scope and current architecture rather than requiring a prescribed intake format or
declared mode.

### P2. The agent supplies the proposal

Incomplete input becomes the agent's current recommendation, not a questionnaire, blank, `TBD`, or
neutral menu. Discussion items let the operator refine material judgment calls; they do not
delegate ordinary design work back to the operator.

### P3. The API sketch is the primary review surface

The design document has an early section titled exactly `## API Sketch`. The heading never changes
to represent status. The sketch always shows the complete current proposal and is updated whenever
discussion changes the design. API covers production-code definitions visible outside their immediate
implementation scope, including module-visible definitions. It excludes tests and private or local
implementation details.

The API sketch is primary, not exclusive. When a material decision cannot be reviewed adequately as
an API diff, the design document exposes it in the smallest useful form. Use prose by default; create
or invoke another artifact only when the subject has independent structure or ownership, as the UI
Map and requirements change packages do.

### P4. Discussion comes before the sketch

Topic-organized `D#` items precede `## API Sketch`. API-specific items clearly name the affected API
or type; broader decisions live with their natural design topic. The sketch does not duplicate the
questions—it shows the proposed contract they currently imply.

### P5. Gates protect judgment

There are two planned approvals: approval of the resolved design direction and API sketch, then
approval of the completed design and implementation plan. Open discussion items use the standard blocked
discussion gate. There are no first-pass/second-pass work-spec gates or default per-task gates.

The work-spec skills do not define `auto` or `auto to`. A planned gate requires an approval decision
from the operator. The operator is the actor outside the executing workflow that reviews gates
and supplies feedback or advance intent; it may be a human or parent agent. The executing agent
does not approve its own gates. Individual skills do not prescribe delegation or escalation behavior.
A blocked gate is never bypassed.

This is an intentional temporary exception to the current SKAI process-flow template. Removing
`auto` from the shared house style and migrating other skills are separate follow-up work; a review
of the replacement work-spec guides must not treat the absence of `auto` as a defect.

### P6. Design leads implementation

The approved design and API are authoritative. Later planning or implementation may reveal a defect,
but the agent reopens discussion rather than silently changing the design to fit implementation.

### P7. Evidence enables continuous implementation

Final plan approval authorizes the implementation run as a whole. The agent checks tasks as their
completion criteria and verification pass, without seeking approval after each one. Material design
changes, contradictory evidence, missing required tooling, destructive work, and unresolved
behavioral ambiguity still block.

Autonomy is not permission to improvise without a contract. The approved design, traceable tasks,
and verification evidence distinguish continuous agent implementation from vibe coding.

### P8. Artifacts are agent-sufficient

A fresh implementation agent can execute by reading the design document, work spec, and their
explicitly linked inputs. Chat history is useful context, never a hidden dependency.

### P9. Workflow ownership stays narrow

Work Spec Design owns the technical design. Work Spec Implementation owns the codebase audit, task
list, code changes, and verification. Requirements Authoring owns requirements change packages, and
Requirements Promotion alone writes the catalog. Each workflow references other artifacts instead
of duplicating their content or progress state.

### P10. Review attention follows leverage

A decision requires operator review when it creates a long-lived contract, has broad blast radius, is
costly to reverse, commits the project to an external system, or materially constrains future work.
The agent handles ordinary reversible implementation choices. This principle, rather than a fixed
catalog of domains, determines what earns a discussion item or supporting review material.

## Artifacts

Both default artifacts are working documents under the session folder required by
[`Guides/Core/working-doc-conventions.md`](Guides/Core/working-doc-conventions.md):

```text
skai/working-docs/<branch-path>/<spec-name>/
  <spec-name>-design.md
  <spec-name>-impl.md
```

### Design document

The ordinary document contains, in order:

1. Title and goal.
2. Inputs with exact paths or links.
3. Relevant current architecture and constraints.
4. Topic-organized Discussion.
5. API Sketch.
6. Implementation Design.
7. Assumptions, TODOs, and non-goals when present.

Discussion, API Sketch, and Implementation Design always appear; omit other empty optional sections.
Implementation Design is written after the first gate; when no additional detail is needed, it says
so explicitly. Its presence is part of the durable handoff proof that the gate advanced. A table of
contents is optional for a long document, never required boilerplate.

Use cases, relevant data flow, component ownership, compatibility concerns, summarized caller or
conformer impact, rejected alternatives, risks, and scope boundaries may live in the design document
when they explain a material design choice. Exhaustive call-site inventories, mechanical file
operations, and verification transcripts do not.

Other review material is conditional. Examples include a third-party service or library choice, data
schema or migration, security or privacy boundary, deployment topology, or porting-parity map. Keep
the decision and its rationale in the design document when prose is sufficient. Link a separate
artifact only when it provides a materially better review surface or belongs to another workflow.

### Work spec

The work spec contains the goal and inputs, the approved design link, a concise ordered task list,
completion criteria and verification for each task, evidence recorded during implementation, and
explicit deferrals or handoffs that affect completion.

Work Spec Implementation creates and maintains this artifact. Task decomposition belongs to the
developer side of the boundary because it depends on auditing the approved design against the actual
codebase and deciding how to sequence the concrete work.

Each task traces to a part of the API sketch, a resolved `D#`, an applicable canonical requirement
ID, or another named input. A task describes a coherent outcome and includes only the structure
needed to execute and verify it. Do not force a fixed number of subtasks or repeat design prose.
Detailed subtasks and a `Touches` list are optional when they materially remove ambiguity.

The runtime guide should define one compact task format and one faithful example.

### Design readiness

A design is ready for Work Spec Implementation when Discussion has no unchecked items, API Sketch
and Implementation Design are present, no assumption or TODO blocks implementation planning, and
every required sibling architecture artifact is ready. Before implementation planning begins,
`skai/integration.md` also defines the required build, test, and runtime commands. This structural
screen is the authority; do not add a mutable readiness status field.

## API sketch

API means production-code definitions visible outside their immediate implementation scope. It
includes module-visible definitions, not only definitions exported outside a package or module. It
excludes tests and private or local implementation details. The goal is to record models and the
surfaces through which types or components interact without exposing their implementation.

For the initially supported language families, apply that boundary directly: include non-private
production declarations in Swift and Kotlin, including module-visible `internal` API; in JavaScript
and TypeScript, include exported module definitions and externally visible type or object members,
while omitting file-local helpers. Do not grow the guide into an exhaustive language taxonomy.

The sketch is a diff of that surface, not an implementation listing. Include every new, modified, or
removed API definition:

- Show members in their enclosing type.
- Omit unchanged APIs and private implementation details.
- Show removed declarations with strikethrough.
- Show a modified declaration as the old declaration followed by the proposed declaration.
- Document new or modified API.
- When a protocol or interface defines an API, show that contract once. For a conforming type, show
  only that it conforms; do not repeat the protocol requirements on the type. Show any independently
  changed non-private definitions on the conforming type normally.
- Use language-tagged code fences.

Declarations and documentation are allowed; implementation bodies are not. This replaces the legacy
guide's contradictory claim that a design document contains "no code."

Every gap receives a proposal, so the sketch remains coherent while `D#` items are open. Update it
before responding whenever a decision changes. If no API changes are needed, say so in the section;
approving the sketch approves that conclusion.

Do not turn the sketch into an impact report. Supporting evidence and architectural reasoning belong
in the surrounding design; mechanical impact belongs in the work spec. If detailed planning later
exposes a material API problem, reopen Discussion and obtain API approval again.

The presence of other review material does not add another planned gate. The resolved design
direction and API sketch are approved together at the first gate.

## Discussion

Use SKAI's structured discussion-item format with stable `D#` IDs under the topics they concern.
Each item contains the agent's recommendation and resolves only on explicit operator approval of that
item. A tradeoff names its options and recommends one. A rare question with insufficient evidence
still has a provisional resolution so the API sketch remains complete.

Only a choice warranting conscious operator judgment earns an item. Implications forced by the inputs,
repository conventions, or existing architecture are encoded directly.

Selecting a third-party service or library is in scope when the change depends on it. The agent
presents the recommendation and material alternatives here; the API sketch shows the resulting code
boundary, and the work spec carries the approved adoption work. Procurement, credentials, contracts,
or other external actions may remain handoffs or blockers during implementation.

The initial drafting response creates the design document through API Sketch and ends at the
discussion gate—never at a separate draft-review gate. While items remain:

```text
⏳ GATE: Blocked: <N> open items in Discussion. Resolve them to approve the API sketch.
```

When all items are resolved, including when drafting required none:

```text
⏳ GATE: Next: Discussion complete. Review the design decisions and API sketch, then say "next" to approve them and complete the design.
```

The runtime guide must use the smallest progress-marker representation that satisfies SKAI's gate
rules. Do not add a general phase checklist merely to narrate the workflow.

## Workflow

The process is implemented by two separate skills. Work Spec Design produces the completed design
document. Work Spec Implementation consumes it, creates the work spec, and executes it. The boundary
supports an architect-to-developer handoff without requiring one: when the initiating request includes
implementation, the same agent transitions between skills without another operator response.

### 1. Initiate design

The operator initiates design or work-spec authoring with any available input. The agent reads that
input, relevant repository sources, applicable canonical requirements, and project-specific integration
information. It chooses a concise spec name when one is evident and creates the design document. Only
a genuinely unresolvable artifact identity blocks creation.

### 2. Draft and discuss

The agent writes the design through API Sketch in one pass, supplying a complete recommendation and
seeding only material discussion items. Operator feedback updates the discussion, design, and sketch
together. Local approval resolves individual `D#` items; it is not advance intent for the workflow.
When a required sibling workflow must run during the draft, it temporarily owns the active gate; the
agent resumes and emits the Work Spec Design gate after the sibling completes.

### 3. Approve the design direction and API

When Discussion has no open items, the first planned gate presents the resolved design direction and
current sketch. Advance intent approves them and authorizes the remaining design work.

### 4. Finish design

The design agent writes Implementation Design and completes the implementation-relevant design without
silently altering the approved API. It uses the explicit empty state when no additional detail is
needed. A material API or design defect returns to step 2; ordinary implementation details do not.

For a design-only request, the skill completes with the design document ready for a developer. When
the request also includes implementation, the same agent transitions directly to Work Spec
Implementation. The skill boundary is not another operator gate.

### 5. Plan implementation

The implementation agent loads the approved design and its inputs, audits them against the current
codebase, and creates the full work spec in one pass. It makes tasks concrete, follows project
conventions, derives verification from `skai/integration.md`, and confirms that every task has a named
source and every in-scope design obligation has a task or explicit disposition.

If the required Integration commands are absent or unfilled, implementation planning blocks until the
operator establishes them through the normal SKAI installation/update process. Greenfield work is
not an exception; the intended commands may name the project structure the setup tasks will create.

If the audit exposes a material problem in the approved design, implementation blocks and returns the
issue to Work Spec Design. It does not encode a different architecture in the task list.

The completed implementation plan stops at the second and final planned gate. Its Next action follows
the initiating request:

- Build: `⏳ GATE: Next: Design and implementation plan ready. Say "next" to approve them and begin implementation, or what to change.`
- Plan: `⏳ GATE: Next: Design and implementation plan ready. Say "next" to approve them for handoff, or what to change.`

### 6. Implement

Advance intent approves implementation as a whole. The implementation guide executes unchecked tasks
in order, records evidence, and checks each task when its completion criteria and verification pass.
It does not wait between tasks.

When implementation is invoked later against an approved design, that explicit request starts at
step 5 without recreating the design gates. It still creates or refreshes the work spec and stops for
implementation-plan approval before changing code. A material stale-design conflict blocks and
returns to design.

The workflow completes after the final task is checked. A blocked task remains unchecked. The operator
may bound a run before a stable `T#`, but stepwise approval is not the default.

## Optional delivery slicing

Most work specs do not use slices. The ordinary design document has no Delivery section, phase
skeleton, or declared sliced mode.

If scope grows beyond one desirable implementation iteration, the agent proposes a cut line as a
material `D#` item. After approval it adds a compact `## Delivery Slices` section containing the
current slice's outcome and boundary, its work-spec link, and brief bullets for follow-up slices.

Only the current slice is planned deeply enough to implement. Future slices remain reminders rather
than empty mini-plans. The API sketch covers the current slice plus only the future-facing constraints
needed to avoid an architectural dead end.

One coherent design may link to multiple work specs over time. Beginning a later slice reopens the
same design document, makes that slice current, and updates Discussion and API Sketch. Work Spec
Implementation then writes the new slice's work spec. It does not create nested per-phase copies of
the workflow.

A whole-app port, greenfield product, or similarly large initiative is not forced into one work spec.
Use one coherent top-level design, the relevant baseline and target artifacts, and multiple buildable
slices. For a mobile port those inputs may include a requirements baseline and UI Map; for another
system they may be different. Slicing is successful decomposition, not a failure of the default
workflow.

## Related workflow composition

Invoke sibling SKAI workflows when the work requires the artifact they own. Work Spec Design invokes
UI Map Architecture when it needs to create or change structural UI design. Work Spec Implementation
invokes UI Map Implementation when it needs to audit or realize that architecture.

A required sibling may run during the initial design draft. While it is active, only its gate is
active; the outer skill resumes after sibling completion and then emits its own gate.

UI Map Implementation already supports participation in a larger effort: it separates work it owns
from `planned` work and `handoff` items for the outer operator. Work Spec Implementation is that
operator when it owns the larger feature. It consumes the UI Map implementation artifact when creating
the overall task list. Each invoked workflow retains ownership of its artifacts and gates, then returns
its result as an input; this composition is not treated as a human handoff.

## Requirements boundary

Ordinary work-spec design reads and references applicable canonical requirements but does not invoke
a requirements-normalization phase, duplicate their prose, or write the catalog.

Missing behavior that already ships is requirements backfill. When `skai/integration.md` declares a
requirements catalog, Work Spec Design invokes Requirements Authoring to create or reopen its change
package; do not place provisional canonical requirements in the design document or work spec. Each
workflow retains its own artifacts and gates. Backfill blocks the design only when its unresolved
behavior is needed to settle the design. Otherwise, Design records the backfill need for the operator
to orchestrate separately and continues without waiting. If the project keeps no catalog, record the
missing behavior as a non-blocking assumption.

New behavior being planned does not automatically invoke Requirements Authoring. It remains grounded
in the supplied product input and approved design unless the operator separately initiates requirements
work. Requirements Promotion is never an automatic continuation of work-spec creation or implementation.

## Verification and testing

Unit tests are required for changes to testable production behavior except view-only presentation code.
Do not create artificial unit tests for views. Unit-test tasks invoke the Unit Testing skill as their
implementation method.

When a user-visible result can be exercised with available tooling, the implementation agent runs the
app in a simulator, emulator, browser, or other suitable runtime and verifies the changed behavior.
This agent-operated UI verification is ordinary implementation evidence. It complements unit tests and
is the primary verification for view-only changes where practical.

Do not create automated UI test suites by default. Adding and maintaining such a suite is a material,
project-specific design decision.

When human testing is known during planning, place one precisely scoped `handoff` task last in the work
spec. State the scenario, expected result, and evidence needed. The agent completes every preceding
task before reaching the final unchecked handoff and blocked gate. Once the operator supplies passing
evidence, the agent records it, checks the task, and completes.

If the need for human testing is discovered unexpectedly, stop immediately at a blocked gate and leave
the current task unchecked. State why available agent tooling cannot establish the result and name the
smallest test and evidence needed to resume. Never weaken verification or silently defer the newly
discovered need.

## Implementation boundaries

The agent may fix obvious identifier mistakes, missing imports, formatting, and clear local compilation
errors caused by the current task. It may resolve implementation-detail mismatches that do not change
behavior, API, architecture, scope, persistence, compatibility, or an explicit constraint.

After plan approval, the agent may add, split, or reorder tasks without another gate when the approved
design, scope, outcomes, and verification standards remain unchanged; record the reason in the work
spec. Changing scope, `Done when`, required verification, a deferral, or the approved design/API
returns to the applicable approval gate.

The agent blocks when:

- The viable implementation would change an approved API or material design decision.
- The work spec and repository evidence disagree about intended behavior.
- An unsettled choice would change behavior, architecture, scope, persistence, compatibility, or
  another non-private contract.
- Required build, test, or evidence tooling is missing or broken.
- Verification contradicts task completion.
- The next action is destructive, irreversible, or outside the workflow's authority.

The blocker identifies the smallest decision or external change needed to resume. The guide should
not enumerate speculative variants of these principles.

## Acceptance checks for the replacement guides

A cold reviewer should verify:

1. Open-ended input produces a complete agent proposal rather than an intake interrogation.
2. Discussion precedes a stable `## API Sketch`, and feedback keeps the sketch current.
3. Design/API approval and implementation approval are the only planned gates.
4. Work Spec Design stops at the technical design boundary, and Work Spec Implementation writes the
   complete work spec in one pass after auditing the approved design against the codebase.
5. Implementation runs continuously after final approval while preserving material stop conditions.
6. Optional slicing is invisible in the common case and lightweight when activated.
7. Requirements work is absent except for correctly routed backfill.
8. Each round reports guide sizes and deltas from the 45,512-byte baseline and 35,000-byte cap; the
   combined guides do not exceed the cap without an explicit operator decision.
9. A fresh agent can execute from the artifacts and linked inputs without chat history.
10. The same core process handles an existing mobile feature, third-party service adoption, a
    greenfield web product, and a whole-app port without adding unused structure to the mobile case.
11. Neither work-spec guide defines `auto`; operator approval advances planned gates, while blocked
    gates still stop.
12. API Sketch covers production interaction surfaces, includes module-visible API, excludes tests
    and implementation-local details, and applies the stated Swift, Kotlin, and JavaScript/TypeScript
    boundary without attempting a universal language taxonomy.
13. Design readiness is determined from artifact structure rather than chat history or a mutable
    status field.
14. Unit tests cover non-view production behavior; agent-operated runtime UI verification is used
    where practical; automated UI test suites remain opt-in.
15. Planned human testing is the final handoff task, while an unexpected need for human testing blocks
    immediately with the current task unchecked.
16. Work Spec Design and Implementation invoke UI Map and requirements workflows when their owned
    artifacts are needed, preserving sibling ownership and returning their results as inputs.
17. Required Integration commands exist before implementation planning; missing commands block rather
    than creating a temporary second source of truth in the work spec.
18. Mechanical task-list evolution remains autonomous and recorded; changes to approved outcomes,
    verification, scope, deferrals, or design re-gate.

Findings that would add ceremony must identify a failure the existing principles cannot cover.
Prefer consolidating or sharpening an existing rule over adding a sibling rule.
