Managed-By: skai
Managed-Id: guide.dev-specs-implementation
Managed-Source: Guides/DevSpecs/dev-specs-implementation.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-31

# Dev Specs Implementation

Print `📖 SKAI guide: dev-specs-implementation` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

## Purpose

Turn a ready design into a task list; get one approval, then implement continuously. Write the
artifact, code and evidence. The approved design, requirement contracts, `skai/integration.md` and sibling
artifacts are read-only except sibling task-state updates under *Audit and plan* and verified
known-difference cleanup under *Completion*.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## Inputs and initiation

Start from the exact design path from [`dev-specs-authoring.md`](dev-specs-authoring.md).
Without a design, load Dev Specs Authoring; return on completion if the request also asks for
planning or implementation. Readiness requires:

- `## Discussion` has no unchecked non-gap items. A gap on an input you rely on, or an item of yours that cannot be resolved because something outside this work is not yet known, is handled per [`known-gaps.md`](../Core/known-gaps.md).
- `## API Sketch` and `## Implementation Design` are present.
- No assumption or TODO blocks implementation planning.
- Every required sibling architecture artifact is ready.

An assumption or TODO blocks if being wrong would change a resolved discussion decision (`D#`) or the
API Sketch; otherwise record a non-blocking note.

If the design fails readiness, load Dev Specs Authoring to reopen it and end at its Discussion gate.
Missing external inputs block. Never infer approval from chat history or repair the design in the task list.

Before auditing or writing the artifact, require `skai/integration.md` to define needed build, test,
and runtime commands. Block on missing or unfilled commands; the supervisor establishes them through
normal SKAI install/update, then resumes planning. This includes greenfield work; commands may name
the project structure its setup tasks will create.

The supervisor's request sets the endpoint; do not store a mode:

- **Plan**: create the artifact, obtain approval, and finish for handoff without changing code.
- **Build**: create the artifact, obtain approval, and implement it.

A request that asks only for an implementation plan is Plan.

On initiation, reopen an existing artifact in place—including after Plan handoff, interruption, a
bounded stop, or a design return. Re-audit current code and design. Preserve task IDs and checked tasks with current
evidence; update only changed or stale content. Stop at the implementation-plan gate again before
changing code. Return material design conflicts to Dev Specs Authoring.

## Implementation artifact

Create beside the authoring artifact:

```text
skai/working-docs/<spec-name>/<spec-name>-impl.md
```

For an activated delivery slice, use the design's declared `<spec-name>-<slice-name>-impl.md`. In
`## Inputs`, record the exact design path, every sibling artifact a task realizes, and key implementation
or convention sources a fresh agent must read. If `## Delivery Slices` does not declare the requested
slice current, load Dev Specs Authoring to make it current, then return. Omit broad file inventories.

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
- [ ] T01 **<coherent outcome>**
  - **Realizes** <API area, D#, requirement ID, sibling item, or named input>
  - **Disposition** handoff <!-- only when another operator owns completion -->
  - **Done when** <observable completion criteria>
  - **Work** <concise changes; nested bullets only when sequence matters>
  - **Touches** <paths or components> <!-- optional -->
  - **Verification** <command or runtime check and pass condition> [evidence: pending]
```

Omit `Disposition` for owned work and `Touches` or detailed `Work` when they add no useful precision.
Do not force a subtask count. Order tasks by dependency with stable `T#` IDs; never renumber them.
Removing a task retires its ID.

Map every in-scope design obligation to a task or explicit deferral/handoff. Each task names what it
realizes, with observable completion criteria beyond code existing or the project building.
Verification proves those outcomes as directly as available tooling permits.

`## Deferrals` lists only in-scope obligations the supervisor approves leaving undone at the
implementation-plan gate. Later deferrals change scope and block for renewed plan approval. Keep
handoffs as tasks with a Disposition; do not duplicate them here.

After plan approval, you may add, split, or reorder tasks without another gate if approved design,
scope, outcomes, and verification standards stay unchanged; record the reason in the artifact.
Changes to scope, `Done when`, required Verification, or a deferral require proposing the exact edit
at the implementation-plan gate and applying it only after approval. Changes to approved design/API
return to Design. Checkbox and evidence updates are ordinary execution, not plan changes.

Each task should leave the repository buildable and completed behavior verifiable. If a change
cannot sensibly pass in smaller pieces, keep one coherent task instead of intentionally broken tasks.

Example:

```markdown
- [ ] T01 **Integrate the service-backed image provider**
  - **Realizes** Design API Sketch — `ImageProviding`; D01
  - **Done when** A note's thumbnail and full-size image load through the image service, and a failed
    load reaches the caller as an error, not a missing image.
  - **Work** Add `ServiceImageProvider` and make it the app's `ImageProviding`.
  - **Verification** Run `<build command>` from `skai/integration.md`; launch the app and confirm a
    requested image loads through the provider without a runtime error. The unit tests prove that
    failures reach the caller (T02). [evidence: pending]
- [ ] T02 **Test image-provider behavior**
  - **Realizes** Design API Sketch — `ImageProviding`
  - **Done when** Tests show a loaded image comes back sized for display and a service failure comes
    back as an error, deterministically; no 🟡 markers.
  - **Work** One test scope for the image provider.
  - **Verification** Run `<targeted test command>` from `skai/integration.md`; all image-provider
    tests pass. [evidence: pending]
```

## Gates

While waiting on the supervisor, end every response with the active gate line verbatim until it
changes. Name the artifact path and what awaits review; for planned gates, state what approval does.
Do not invent intermediate gates. Completion is not a gate.

Unexpected blockers use:

- Blocked: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Once the task list and evidence plan are ready, briefly describe what will be built, its verification,
deferrals, and handoffs. Link the design and tasks, then use this skill's only approval gate:

- Build request: `⏳ GATE: Next: Design and implementation plan ready. Say "next" to approve them and begin implementation, or what to change.`
- Plan request: `⏳ GATE: Next: Design and implementation plan ready. Say "next" to approve them for handoff, or what to change.`

At a supervisor-requested run boundary, reuse this gate category:

`⏳ GATE: Next: Stopped as requested before <T#>, <what that task delivers>. Say "next" to continue implementation, or what to change.`

Advance intent resumes a bounded run without another audit; a re-initiated skill follows
*Inputs and initiation*.

The supervisor is an outside human or authorized agent who resolves this workflow's discussion items
and reviews its gates. The executing agent cannot resolve or approve its own. This guide prescribes
neither delegation nor escalation.

While an invoked sibling is active, end responses with only its gate line; resume after its completion line.

## Advance intent and task markers

Advance intent ("next", "continue", "go ahead", "do it") advances a planned gate only after that
gate is emitted. "We should" and "let's" are discussion. There is no `auto` mode.

At a blocked gate, the supervisor resolves the cause; the agent re-evaluates and emits the appropriate
gate on its next response. Bare advance intent while unresolved re-emits the blocked gate.

Tasks use `T#` checkboxes. At the implementation-plan gate, every unverified task stays unchecked.
Advance intent approves the plan and authorizes checking tasks as their Done when and Verification
pass; blocked, failed, handoff, and unverified tasks stay unchecked. No per-task approval is required.

For Plan, advance intent approves the artifact for handoff and completes the skill with every
implementation task unchecked.

## Audit and plan

Read the design and all required inputs. Inspect actual declarations, callers, tests, project structure,
and integration commands needed to make the design executable. Reference the design without copying it.

If the design links a UI Map change package, invoke [`../UIMap/ui-map-implementation.md`](../UIMap/ui-map-implementation.md) during the audit in the larger-feature context; it owns map conformance planning and gates. After completion, carry each
`planned` and `handoff` item as an outer task, using the returned artifact path under
`skai/promoted/<change-id>/ui-map/` after promotion. If the design already links a promoted Plan,
consume its pending items there without promoting again; check the current official map for later
changes before relying on the plan. For a no-proposal conformance run, use its working-doc session path. In both
cases, Realizes names the sibling artifact path and item ID. Give the outer task `Disposition handoff`
only if this workflow also does not own the work. The sibling owns map promotion. When an outer task
realizes a sibling item, update its checkbox and clear its in-code scaffold markers as its guide
requires, preserving its Disposition.

Write the whole task list in one pass. Include dependency or service adoption, migration, and
documentation only as the design or repository requires. Use commands from `skai/integration.md`; never invent project-specific variants when it
defines them.

For material design or API problems found during audit, follow *Local fixes and design returns*;
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

Require unit tests for testable production behavior except view-only code. Plan batched test tasks (`T#`) after the behavior they cover; follow [`../Test/unit-testing-guide.md`](../Test/unit-testing-guide.md). If a later test task is the only direct
proof, name it in the behavior task's Verification. That task may be checked on its own build/runtime
result; a later failure invalidates it.

For user-visible behavior, run the app in an available simulator, emulator, browser, or runtime and
record observations. This is the primary verification for view-only changes. Create a UI test suite only if the approved design requires one.

### Planned handoffs

Track externally owned work once as a `Disposition handoff` task. Run all independent owned tasks,
then stop when none can advance:

`⏳ GATE: Blocked: <T#> requires <external result> for <scenario>. Provide the result to continue.`

Known manual testing is one final handoff task stating the scenario, expected result, and evidence:

`⏳ GATE: Blocked: <T#> requires manual test evidence for <scenario>. Provide the result to continue.`

On a pass, record the result, check the handoff, and resume. On failure, leave it unchecked and return
to the affected task.

### Unexpected manual testing

If agent tooling unexpectedly cannot establish a required result, leave the current task unchecked
and block immediately. Name the smallest scenario, expected result, and needed evidence. Do not
weaken or silently defer verification.

## Implement continuously

After Build approval, execute the first unchecked owned task with met dependencies. Skip unsupplied
handoffs until no owned task can advance. Invoked siblings retain their gates; resume continuous
outer execution when they complete. For each task:

1. Read its Realizes, Done when, Work, and Verification entries and the referenced sources.
2. Apply the minimum complete change.
3. Run its verification on the current code.
4. Record evidence.
5. Check the task only when every completion and verification condition passes. A later `T#` named
   under *Testing* is a revocation condition, not a precondition.

Record evidence on the task's Verification line:

```text
The provider build fails on a missing import. [evidence: <command>; exit 65; output: <scratch path>]
The requested image loads with no runtime error. [evidence: simulator image-load flow]
```

Say what the run established, then the command or check, the exit code or observed result, and any
captured output's path under the scratch root `skai/integration.md` names (default `/tmp/skai/<spec-name>/`). Output is not kept; reruns
reproduce it. Evidence predating the latest relevant mutation is stale and must be rerun. Uncheck
tasks with stale evidence or later verification failures. Keep earlier brackets as history, append
fresh evidence after the fix, and recheck only when the rerun passes.

### Local fixes and design returns

Without stopping, fix obvious identifier mistakes, missing imports, formatting, and clear local
compilation errors caused by the current task. Also fix implementation-detail mismatches that change
no behavior, API, architecture, scope, persistence, compatibility, or explicit constraint.

Stop at a blocked gate when:

- A viable implementation would change the approved API or a material design decision.
- The design and repository evidence disagree about intended behavior.
- An unsettled choice would change behavior, architecture, scope, persistence, compatibility, or
  another production interaction surface.
- A required tool or integration is missing or broken.
- Verification contradicts task completion.
- The next action is destructive, irreversible, or outside the workflow's authority.

Leave the current task unchecked; identify the smallest needed decision or external change. For
non-design blockers, record `[evidence: blocked — needs <result>]` on the task before waiting and
the supervisor's resolution there before resuming. Transfer design/API problems to Dev Specs Authoring in the
same response without a separate implementation-side blocked gate. Authoring reopens its artifact,
records the problem (reopening or adding a `D#`), and ends at its Discussion gate. When the design
returns ready, re-audit, revise the task list, and stop at the
implementation-plan gate again.

Do not remove, weaken, or defer a requirement, completion criterion, test, or design decision to make
a task pass.

## Completion

For Plan:

`🏁 Complete. The implementation plan is approved for handoff.`

Before Build completion, compare task evidence with later mutations. Rerun only checks they may have
invalidated; do not add a blanket rerun when all relevant evidence is current.

After verifying implemented behavior, update or remove known-difference notes for addressed
requirements. Preserve remaining differences, including on other platforms. Change only those notes
and their now-unused link definitions, never requirement text or IDs. Issue closure alone is not verification.

For Build, complete when every task is checked, required evidence is current, and no handoff remains:

`🏁 Complete. The change is implemented and verified.`

If any task is unchecked, use the appropriate blocked or requested-boundary gate instead of a completion line.

## Project Addendum

If `<active-project-root>/skai/addenda/dev-specs-implementation-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
