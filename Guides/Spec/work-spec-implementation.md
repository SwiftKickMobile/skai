Managed-By: skai
Managed-Id: guide.work-spec-implementation
Managed-Source: Guides/Spec/work-spec-implementation.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-04

# Work Spec Implementation

## Purpose

Turn a ready design into a task list, obtain one approval, then implement continuously. This skill
writes only the work spec, code, and evidence; the approved design, canonical requirements,
`skai/integration.md`, and sibling artifacts are read-only except for sibling task-state updates
required by *Audit and plan*.

## Inputs and initiation

Start from the exact path to a design created by
[`work-spec-creation.md`](work-spec-creation.md). If no design exists, load Work Spec Design; when the
request includes a work spec or implementation, it returns here after completion. A design is ready
when:

- `## Discussion` has no unchecked items.
- `## API Sketch` and `## Implementation Design` are present.
- No assumption or TODO blocks implementation planning.
- Every required sibling architecture artifact is ready.

An assumption or TODO blocks when its being wrong would change a resolved `D#` or the API Sketch;
otherwise it is a recorded non-blocking note.

If the screen fails on the design's own content, load Work Spec Design; it owns reopening the artifact
and ends at its Discussion gate. For a missing external input, stop at a blocked gate. Do not infer
approval from chat history or repair the design inside the task list.

Before auditing or writing the work spec, require `skai/integration.md` to define the build, test, and
runtime commands this work needs. Missing or unfilled commands are a blocked gate; the supervisor
establishes them through normal SKAI install/update, then resumes planning. Greenfield work is not an
exception—the commands may name the project structure its setup tasks will create.

The supervisor's request determines the endpoint without a stored mode:

- **Plan**: create the work spec, obtain approval, and finish for handoff without changing code.
- **Build**: create the work spec, obtain approval, and implement it.

A request that asks only for a work spec or implementation plan is Plan.

When this skill is initiated and a work spec already exists—after Plan handoff, interruption, a
bounded stop, or a design return—reopen it in place and re-audit the current code and design. Preserve
stable task IDs and checked tasks whose evidence is still current; update only what changed or became
stale. Before changing code, stop at the implementation-plan gate again. A material design conflict
returns to Work Spec Design.

## Work spec artifact

Create beside the design document:

```text
skai/working-docs/<branch-path>/<spec-name>/<spec-name>-impl.md
```

For an activated delivery slice, use the design's declared
`<spec-name>-<slice-name>-impl.md`. In `## Inputs`, record the exact design path, every sibling
artifact a task realizes, and the key implementation or convention sources a fresh agent must read.
If the requested slice is not the one `## Delivery Slices` declares current, load Work Spec Design to
make it current, then return here. Do not add a broad file inventory.

Use this compact shape:

```text
# <Change> Implementation
## Goal
## Inputs
## Task List
## Deferrals                              when present
```

### Task format

```markdown
- [ ] T1 **<coherent outcome>**
  - **Realizes** <API area, D#, requirement ID, sibling item, or named input>
  - **Disposition** handoff <!-- only when another operator owns completion -->
  - **Done when** <observable completion criteria>
  - **Work** <concise changes; nested bullets only when sequence matters>
  - **Touches** <paths or components> <!-- optional -->
  - **Verification** <command or runtime check and pass condition> [evidence: pending]
```

Omit `Disposition` for work this skill owns; omit `Touches` or detailed `Work` when they add no useful
precision. Do not force a fixed number of subtasks. Tasks use stable `T#` IDs in dependency order and
are never renumbered; removing a task retires its ID.

Every in-scope design obligation maps to a task or an explicit deferral/handoff, and every task names
what it realizes. Completion criteria describe observable outcomes, not merely that code exists or
the project builds. Verification proves those outcomes as directly as available tooling permits.

`## Deferrals` lists only in-scope obligations the supervisor approves leaving undone at the
implementation-plan gate. Adding a deferral after approval changes scope and blocks for renewed plan
approval. Handoffs remain tasks with a Disposition; do not duplicate them here.

After plan approval, the agent may add, split, or reorder tasks without another gate when the approved
design, scope, outcomes, and verification standards remain unchanged; record the reason in the work
spec. To change scope, `Done when`, required Verification, or a deferral, propose the exact work-spec
edit at the implementation-plan gate and apply it only after approval. An approved design/API change
returns to Design. Checkbox and evidence updates are ordinary execution, not plan changes.

Each task should leave the repository buildable and its completed behavior verifiable. If a change
cannot sensibly be green in smaller pieces, keep it in one coherent task rather than creating a
sequence of intentionally broken tasks.

Example:

```markdown
- [ ] T1 **Integrate the service-backed image provider**
  - **Realizes** Design API Sketch — `ImageProviding`; D1
  - **Done when** Image requests use `ServiceImageProvider` and surface provider failures to callers.
  - **Work** Add the adapter and connect it at the existing image-provider composition point.
  - **Verification** Run `<build command>` from `skai/integration.md`; launch the app and confirm a
    requested image loads through the provider without a runtime error; T2 unit tests prove failure
    surfacing. [evidence: pending]
- [ ] T2 **Test image-provider behavior**
  - **Realizes** Design API Sketch — `ImageProviding`
  - **Done when** Success and provider-failure paths pass with deterministic results, and the test
    files carry no 🟡 markers.
  - **Work** Follow the Unit Testing guide for one image-provider test scope.
  - **Verification** Run `<targeted test command>` from `skai/integration.md`; all image-provider
    tests pass. [evidence: pending]
```

## Gates

Whenever waiting on the supervisor, end with the active gate line and re-emit it verbatim on every
response until the gate changes. Name the artifact path and what awaits review; for a planned gate,
also state what approval does. Do not invent intermediate gates. Completion is not a gate.

Unexpected blockers use:

- Blocked: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

After the task list and evidence plan are ready, link or summarize Implementation Design, tasks,
verification, deferrals, and handoffs, then use this skill's only approval gate:

- Build request: `⏳ GATE: Next: Design and implementation plan ready. Say "next" to approve them and begin implementation, or what to change.`
- Plan request: `⏳ GATE: Next: Design and implementation plan ready. Say "next" to approve them for handoff, or what to change.`

When the supervisor requested a bounded run, reaching the boundary reuses this same gate category:

`⏳ GATE: Next: Stopped before <T#> as requested. Say "next" to continue implementation, or what to change.`

Advance intent resumes an active bounded run without another audit; a re-initiated skill follows
*Inputs and initiation*.

The supervisor is the human or authorized agent outside this workflow that reviews gates; the
executing agent never approves its own. This guide does not prescribe delegation or escalation.

While an invoked sibling is active, end responses with only its gate line; resume this skill after
the sibling's completion line.

## Advance intent and task markers

Advance intent ("next", "continue", "go ahead", "do it") advances a planned gate only after that
gate is emitted. "We should" and "let's" are discussion. There is no `auto` mode.

At a blocked gate, the supervisor resolves the cause; on the next response the agent re-evaluates and
emits the appropriate gate. Bare advance intent while unresolved re-emits the blocked gate.

Tasks use stable `T#` checkboxes. At the implementation-plan gate, every unverified task remains
unchecked. Advance intent approves the plan and authorizes checking each task as its Done when and
Verification pass; blocked, failed, handoff, and unverified tasks remain unchecked. No per-task
approval is required.

For a Plan request, advance intent approves the artifact for handoff but leaves every implementation
task unchecked, then completes the skill.

## Audit and plan

Read the design and every required input. Inspect the real declarations, callers, tests, project
structure, and integration commands needed to turn the design into executable work. Do not copy the
design into the work spec; reference it.

When the design links a UI Map change package, invoke
[`../UIMap/ui-map-implementation.md`](../UIMap/ui-map-implementation.md) during the audit in the
larger-feature context so it owns map conformance planning and its gates. After it completes, carry
each of its `planned` and `handoff` items as an outer task; Realizes names
the sibling artifact path and item ID. Give the outer task `Disposition handoff` only when this
workflow does not own the work either. The sibling owns map promotion. When an outer task realizes a
sibling item, update its checkbox and clear its in-code scaffold markers as its guide requires without
changing its Disposition.

Write the whole task list in one pass. Include dependency or service adoption, migration, and
documentation only when required by the design or repository. Unit and runtime verification follow
*Testing* below. Use commands from `skai/integration.md`; never invent project-specific variants when
the Integration document defines them.

A material design or API problem found during this audit follows *Local fixes and design returns*;
block before writing or presenting a divergent task list.

Before gating, check:

- The design readiness screen still passes.
- Every task has a named source, observable completion, and verification.
- Every API Sketch definition, resolved `D#`, and cited requirement ID has a task or explicit
  disposition.
- Dependencies and task order are feasible.
- Unit and runtime testing follow the rules below.
- No task silently changes the approved API or design.

## Testing

Unit tests are required for testable production behavior except view-only code. Plan dedicated,
coherently batched `T#` tasks after the behavior they cover and follow
[`../Test/unit-testing-guide.md`](../Test/unit-testing-guide.md). If a later test task is the only direct
proof, the behavior task names it in Verification and may be checked on its own build/runtime result;
a later failure invalidates it.

For user-visible behavior, run the app in an available simulator, emulator, browser, or runtime and
record what was observed. This is the primary verification for view-only changes. Do not create an
automated UI test suite unless the approved design requires one.

### Planned handoffs

Track externally owned work once as a `Disposition handoff` task. Run every independent owned task,
then stop when none can advance:

`⏳ GATE: Blocked: <T#> requires <external result> for <scenario>. Provide the result to continue.`

Known human testing is one final handoff task stating the scenario, expected result, and evidence:

`⏳ GATE: Blocked: <T#> requires human test evidence for <scenario>. Provide the result to continue.`

Record a passing result, check the handoff, and resume; on failure keep it unchecked and return to the
affected task.

### Unexpected human testing

If agent tooling unexpectedly cannot establish a required result, leave the current task unchecked
and block immediately, naming the smallest scenario, expected result, and evidence needed. Do not
weaken verification or silently defer it.

## Implement continuously

After Build approval, execute the first unchecked owned task whose dependencies are met. Skip an
unsupplied handoff until no owned task can advance. An invoked sibling workflow retains its own gates;
resume continuous outer execution when that workflow completes. For each task:

1. Read its Realizes, Done when, Work, and Verification entries and the referenced sources.
2. Apply the minimum complete change.
3. Run its verification on the current code.
4. Record evidence.
5. Check the task only when every completion and verification condition passes. A later `T#` named
   under *Testing* is a revocation condition, not a precondition.

Record evidence on the task's Verification line:

```text
[evidence: <command>; exit 0]
[evidence: simulator image-load flow; observed the requested image without a runtime error]
```

Always name the command/check and an exit code or observed result. On failure, persist full output under
`skai/working-docs/<branch-path>/<spec-name>/evidence/` and link it. A success log is
optional when the inline result is sufficient. Evidence predating the latest relevant mutation is
stale and must be rerun. When a checked task's evidence becomes stale or a later verification fails,
uncheck the task. Keep the earlier bracket as history, append fresh evidence after the fix, and check
the task again only when the rerun passes.

### Local fixes and design returns

Fix obvious identifier mistakes, missing imports, formatting, and clear local compilation errors
caused by the current task without stopping. The same applies to implementation-detail mismatches
that do not change behavior, API, architecture, scope, persistence, compatibility, or an explicit
constraint.

Stop at a blocked gate when:

- A viable implementation would change the approved API or a material design decision.
- The design and repository evidence disagree about intended behavior.
- An unsettled choice would change behavior, architecture, scope, persistence, compatibility, or
  another production interaction surface.
- A required tool or integration is missing or broken.
- Verification contradicts task completion.
- The next action is destructive, irreversible, or outside the workflow's authority.

Leave the current task unchecked and identify the smallest decision or external change needed. For a
non-design blocker, record `[evidence: blocked — needs <result>]` on the task before waiting, then
record the supervisor's resolution there before resuming. A
design/API problem transfers control to Work Spec Design in the same response; do not emit a separate
implementation-side blocked gate first. Once active, Design reopens the artifact, records the problem
as a new `D#`, and ends at its Discussion gate. When the design returns ready, re-audit, revise the
work spec without renumbering surviving tasks, and stop at the implementation-plan gate again.

Do not remove, weaken, or defer a requirement, completion criterion, test, or design decision to make
a task pass. Do not edit the design from this skill.

## Completion

For Plan, complete after supervisor approval with all implementation tasks still unchecked:

`🏁 Complete. The implementation plan is approved for handoff.`

Before Build completion, compare task evidence with later mutations and rerun only checks those
mutations may have invalidated. Do not add a blanket rerun when all relevant evidence remains current.

For Build, complete when every task is checked, required evidence is current, and no handoff remains:

`🏁 Complete. The work spec is implemented and verified.`

If any task remains unchecked, use the appropriate blocked or requested-boundary gate instead of a
completion line.
