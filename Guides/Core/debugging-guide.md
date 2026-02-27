Managed-By: ai-dev-process
Managed-Id: guide.debugging-core
Managed-Source: Guides/Core/debugging-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-02-27

# Debugging / Problem-Resolution Guide (Core)

Goal: prevent "guessing fixes" loops by using evidence, clear tactics, and explicit stopping conditions.

## Checkpoints

This guide follows the shared process-flow mechanics in `Guides/Core/process-flow.md` (checkpoints, advance intent, `auto`, and the standard gate line).

Workflow-specific gate points (this guide must STOP and wait at these checkpoints):
- Before running an experiment: present facts + possibility-space partition + chosen tactic + proposed discriminating experiment for approval.
- After an experiment: present conclusions and updated possibility space for approval before proceeding.
- Before declaring a root cause and before applying a fix: present the root cause and proposed fix and get explicit approval.

## Required mindset

- **Facts over speculation**: conclusions must be backed by observable evidence.
- **Hypotheses guide experiments**: use hypotheses to decide what to measure, not as conclusions.
- **One change per experiment**: avoid bundling multiple changes that confuse causality.

## Human-in-the-loop contract

In most projects the agent cannot run the app or observe runtime behavior directly.

- The **agent** proposes the smallest next experiment and explains what it will prove/disprove.
- The **human** runs the experiment and provides outputs (logs, test output, screenshots, traces, crash reports).

## Pick a tactic, justify it, reassess

For each iteration:
1. State the current best explanation space (2-4 possibilities).
2. Pick a tactic and justify why it's the best next step.
3. Design the smallest discriminating experiment.
4. Run (human) → report evidence → update the possibility space.
5. If the tactic isn't producing new discriminating evidence quickly, switch tactics.

Checkpoint: STOP for approval before proceeding to the next iteration (use the standard gate line; see `Guides/Core/process-flow.md`). The human may use `auto` to bypass iteration checkpoints, but `auto` does not bypass universal STOP conditions or the hard gates below.

## Debugging toolbox (core)

- **Facts-first logging/instrumentation**
  - Purpose: produce evidence that eliminates possibilities (not "log everything").
  - Log at:
    - decision points (branches, retries, state changes)
    - function/module boundaries (inputs + outputs)
    - sequencing points (start/end markers, ordering)
    - identity/lifecycle points (object instance identity when relevant)
  - Log format:
    - use `AIDEV:` as the debug log prefix unless explicitly overridden
    - include key values needed to differentiate paths
  - Workflow:
    1. write a hypothesis
    2. add the smallest log(s) that will confirm/refute it
    3. have the human run and paste the output
    4. state *facts* from the output (no "probably/maybe")

- **Partition the possibility space**
  - Example structure: A/B/C → B1/B2/B3.
  - Prefer partitions with a clear discriminating observation.
  - Use *logically valid* partitions:
    - cover the space well enough that the true cause must be in one bucket (no "holes")
    - allow some overlap in practice (both can be true), but still be useful for elimination
    - if overlap is likely, add an explicit "both / interaction" or "other / unknown" bucket
  - Examples:
    - **Location**: server-side vs client-side vs integration/contract mismatch
    - **Call boundary**: bug is in this function vs in a function it calls (or in the contract between them)
    - **Timing**: ordering/race vs stale state/caching vs deterministic logic bug
    - **Data**: bad input vs transformation bug vs persistence/serialization bug

Partition quality bar:
- A possibility-space partition must list 2-4 plausible causes. "X vs not X" is not acceptable unless the "not X" bucket is further partitioned into concrete alternatives.
- Partitions must be phrased so evidence can actually eliminate buckets (no hand-wavy buckets).

- **Minimal working implementation → move toward real until it breaks**
  - Start with a small implementation that works.
  - Change one dimension at a time toward the real implementation.
  - Identify the first change that introduces the issue.

- **Bisection**
  - Runtime bisection using feature flags/config toggles.
  - `git bisect` when the bug is a regression with a known commit range.

- **Minimal harness**
  - Create a deterministic reproducer (unit test, small harness, or minimal sample).
  - Goal: "repro on demand" so experiments are cheap.

- **Invariants & assertions**
  - Define what must be true; add temporary asserts/guards to fail at the first invalid state.

## Testing a hypothesis is not applying a fix

Testing a hypothesis means running a discriminating experiment (logging, bisection, unit-test repro, minimal harness, etc.).

It does NOT mean "implement the fix and see if it helps."

Inspection-only exception (narrow):
- Only treat something as "obvious by inspection" when you can point to a specific, local code fact that directly implies incorrect behavior (e.g., typo, wrong variable used, off-by-one, missing guard).
- If the proposed change is non-local, architectural, or depends on runtime behavior, it is not "obvious by inspection" -- require evidence first.

## Investigation loop (logging-heavy default)

1. **Observe the symptom**: actual vs expected.
2. **Form a hypothesis**: keep it tentative.
3. **Collect evidence**: often via the Facts-first logging tactic.
4. **Wait for evidence**: the human runs and provides output.
5. **State facts**: report what the evidence shows.
6. **Repeat** until the root cause statement is isolated.

### Root cause (definition + hard gate)

"Root cause" means the most specific, testable statement that explains the observed symptom and is supported by discriminating evidence (or direct code proof for truly local inspection-only bugs).

Do not declare a root cause prematurely:
- A top-level partition bucket (or a chosen path through the possibility space) is not a root cause if it can be further partitioned into multiple plausible sub-causes.
- Before declaring "this bucket/path is the root cause" or "this bucket/path cannot be partitioned further", inspect the relevant code within the current best-explanation path and attempt at least one further partition based on concrete code structure/branches/contracts.
- If the current best explanation is still a category ("it's in module X", "it's caching", "it's concurrency"), STOP and propose the next partition or the smallest experiment that will partition it further.

Checkpoint: STOP and get explicit approval before declaring a root cause or applying a fix (use the standard gate line; see `Guides/Core/process-flow.md`).

## Log hygiene

- Remove or disable temporary logs once the investigation is complete.
- Keep logs focused on the current hypothesis.
- Avoid log spam: prefer logging state changes, not every read.

## Stop conditions (consult human)

Stop and consult the human when:
- Expected behavior is ambiguous (product intent required).
- Required evidence is missing (human hasn't provided output needed to proceed).
- The next change is large/destructive/wide-reaching.
- You've iterated without gaining discriminating evidence.

If progress stalls:
- STOP and ask the human for a direction change (e.g., choose a different tactic, broaden/narrow the possibility space, provide missing evidence, or accept a workaround).
- This stop condition applies even in `auto`.

## Adapter notes (minimal)

Adapters should only cover:
- Logging APIs and how to capture/share evidence for a stack
- Known tooling limitations that affect evidence collection

