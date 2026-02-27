# Ticket planning (buckets)
#
# Goal: group overlapping "agent ready" tickets into thematic buckets so we can design and implement cohesive improvements (not one ticket at a time).
#
# Scope: all OPEN issues currently labeled `agent ready` in `SwiftKickMobile/ai-dev-process` (20 total).
#
# Notes:
# - Buckets are a planning tool. We are not committing to implementing each ticket's suggested solution verbatim.
# - Each ticket has a "Primary bucket" plus possible "Overlaps" to show where combined solutions should be coordinated.
# - 🟡 marks open discussion topics / undecided decisions (TODO).
# - 🟡 also covers "pending approval": work may be implemented, but the 🟡 cannot be removed until the human approves.
#
# Planning protocol (see `Guides/Spec/work-spec-creation.md`):
# - Keep 🟡 markers on open questions / undecided topics.
# - When the human explicitly approves an item, replace it inline by removing 🟡 and rewriting it as a requirement (no separate Decisions section).
# - Do not remove 🟡 preemptively.

## Bucket A: Checkpoints, consent gates, and "do not improvise"

Theme: Make "stop and ask" behavior explicit, consistent, and hard to accidentally skip. This includes gates for: moving between workflow phases, deviating from a spec, transitioning from diagnosis to fix, and following explicit human instructions literally.

Primary tickets:
- #12 "Align all guides with README process flow principles + standardized gate line"
- #14 "Agent should stop immediately when a required tool is missing or broken"
- #19 "Follow explicit instructions literally -- do not substitute a 'better' action"
- #21 "Mandatory stop-and-ask before deviating from a work spec"

Related/overlapping tickets:
- #18 "Explicit consent gate before implementing fixes" (debugging-specific instance of this theme)
- #13 "Global 🟡 lifecycle rule to prevent premature resolution" (gate/approval semantics for progress markers)

🟡 Open topics

- 🟡 Policy vs guide boundary (universal invariants vs workflow-specific gates)
  - Policies are LLM-facing rules and should cover universal invariants that must hold even when no ai-dev-process workflow is being followed.
  - `Policies/unauthorized-changes.md`: no code changes during discussion/troubleshooting without explicit authorization.
  - `Policies/safe-operations.md`: no commit/push/delete/add dependencies/revert unless explicitly asked.
  - Universal "STOP and ask" / "no substitution" / "no silent deviation" invariants belong in policies (with bright-line language + examples).
    - Proposal: define explicit STOP-and-ask bright lines in policy (part of the universal STOP-and-ask invariant).
      - STOP immediately (no workaround substitution) when:
        - A required tool/integration for the requested workflow is missing/broken.
        - Spec/requirements are ambiguous and product intent is needed.
        - You are about to do not-X where the spec/plan/instruction says X.
        - You are about to run a destructive/irreversible operation.
      - Allow exactly one small bounded self-fix for trivial mechanical issues (obvious typos, missing imports, straightforward compile errors with a clear fix); otherwise STOP.
      - STOP whenever required evidence/artifacts are unavailable or new evidence contradicts the current hypothesis.
  - Guides should cover workflow-specific gate points (what to stop after/before in that workflow) and should reference shared mechanics rather than restating universal invariants.
    - Guide "house style" for checkpoints + references (so the guide edits plan can be applied consistently).
      - Each workflow guide gets a short, consistent section near the top: `## Checkpoints` (or `## Process flow and checkpoints`).
      - That section:
        - Links to `Guides/Core/process-flow.md` for shared mechanics (what a gate is, how "next"/"auto" behave, standard gate line).
        - Lists the workflow's gate points as a short ordered list (e.g., "STOP after planning output", "STOP before applying fix", etc.).
        - States: "End every checkpoint output with the standard gate line" (do not restate the full gate-line variants in every guide).
      - Within the main body of the guide:
        - When a phase ends in a STOP, label it as `Checkpoint:` and ensure it maps to one of the gate points listed above.
    - What to remove from guides vs keep (avoid duplication but preserve workflow clarity).
      - Remove from guides:
        - Universal safety rules that are already covered by policies (commit/push/delete, unauthorized changes, no workaround substitution, destructive git prohibitions, etc.).
      - Keep in guides:
        - Workflow-scoped mechanics (e.g., "after Phase 1, STOP and wait", "this phase is complete when...") and any workflow-specific failure-mode callouts.
      - Replace removed content with a short reference sentence (e.g., "Universal safety rules are enforced by policies; see `Policies/safe-operations.md` and `Policies/unauthorized-changes.md`.").
  - Extend/strengthen existing policies (do NOT add a consolidated "process-flow / human-in-the-loop" policy).
    - `Policies/safe-operations.md` should own:
      - destructive/irreversible operations bright lines (esp. git discard/reset/checkout paths/clean/force push)
      - safe defaults (no commit/push/delete/add deps/revert unless explicitly asked)
      - STOP-and-ask bright lines for destructive operations + missing required tool/integration (when relevant)
    - `Policies/unauthorized-changes.md` should own:
      - the "discussion/troubleshooting => no code changes without explicit authorization" boundary (including debug logging as a code change)
      - authorization semantics examples (what counts as explicit authorization vs discussion)
      - "no workaround substitution" / "follow explicit instructions literally" (where it is about change execution rather than git safety)
    - `Policies/debugging-process-rule.md` should own:
      - enforcing "read + follow `Guides/Core/debugging-guide.md`" and its evidence-first loop
      - hard gate before declaring root cause / applying fixes (explicit approval)
      - prohibitions against speculative/shotgun fixes
  - The debugging guide must be followed reliably (this is a top pain point):
    - Suggestion: keep both `Policies/debugging-process-rule.md` (enforcement) and `Guides/Core/debugging-guide.md` (tactics), but make the policy explicitly enforce guide usage:
      - When debugging (bugs, flaky behavior, failing tests, unexpected runtime outcomes), the agent MUST read and follow the guide.
      - Each iteration MUST present the possibility-space partition + chosen tactic (by name, from the guide) + proposed discriminating experiment for human approval before proceeding (unless the human uses `auto` to bypass this checkpoint).
      - Add a hard STOP gate before declaring root cause / applying fixes (with explicit human approval).
      - Proposal: define "root cause" and forbid declaring a partition path as root cause prematurely.
        - "Root cause" means the most specific, testable statement that explains the observed symptom and is supported by discriminating evidence (or direct code proof for truly local inspection-only bugs).
        - A top-level partition bucket (or a chosen path through the possibility space) is not a root cause if it can be further partitioned into multiple plausible sub-causes.
        - Before declaring "this bucket/path is the root cause" or "this bucket/path cannot be partitioned further", the agent must inspect the relevant code within the current best-explanation path and attempt at least one further partition based on concrete code structure/branches/contracts.
        - If the current best explanation is still a category ("it's in module X", "it's caching", "it's concurrency"), STOP and either:
          - propose the next partition within that category, or
          - propose the smallest experiment that will partition it further,
          - but do not declare root cause yet.
      - Proposal: prevent "false partitioning" and "fix-as-experiment" (common failure mode).
        - Partition quality bar:
          - A possibility-space partition must list 2-4 plausible causes; "X vs not X" is not acceptable unless the "not X" bucket is further partitioned into concrete alternatives.
          - Partitions must be phrased so evidence can actually eliminate buckets (no hand-wavy buckets).
        - Experiment quality bar:
          - Testing a hypothesis means running a discriminating experiment (logging, bisection, unit-test repro, minimal harness, etc.).
          - It does NOT mean "implement the fix and see if it helps."
        - Inspection-only exception (narrow):
          - Only treat something as "obvious by inspection" when you can point to a specific, local code fact that directly implies incorrect behavior (e.g., typo, wrong variable used, off-by-one, missing guard).
          - If the proposed change is non-local, architectural, or depends on runtime behavior, it is not "obvious by inspection" -- require evidence first.
      - Put experiment-level checkpoints in the *guide* (process), not the policy:
        - In the debugging guide, STOP after each experiment to present conclusions and get approval before proceeding (unless the human uses `auto` to bypass checkpoints).
        - In the debugging guide, define a "not going well / stalled progress" stop condition that triggers STOP even in `auto` mode.

- "No workaround substitution" scope (global invariant)
  - No substituting tools/workflows/architectures without explicit approval (examples: `gh` for MCP; in-memory filtering for predicate-based filtering).
  - Recommendation: keep this as ONE invariant ("no substitution without explicit approval"), but explicitly enumerate two classes inside it:
    - tool substitution (MCP vs CLI, different runner/tooling)
    - approach/architecture substitution (predicate filtering vs in-memory, changing data model/flow)
  - Rationale: without approval, the same category of failure will keep recurring; with approval, the human can either provide the missing input, adjust the process/spec, or change/repair tooling so the workflow can run smoothly going forward.

- Authorization semantics (policy-level contract)
  - "Explicit authorization" should be treated as an unambiguous instruction to implement/change, not inferred from curiosity/questions. When unclear, STOP and ask.
  - Proposal: define "explicit authorization" using bright-line language + examples (encode in `Policies/unauthorized-changes.md`).
    - Definition:
      - "Explicit authorization" means the human clearly instructs the agent to make code changes now (an imperative request to implement/modify), not merely to analyze, explain, or suggest.
      - If the user intent could plausibly be interpreted as discussion/troubleshooting, treat it as NOT authorized and STOP to ask: "Do you want me to implement this change?"
    - Authorized examples (code changes allowed):
      - "Fix this."
      - "Implement X."
      - "Make the change."
      - "Go ahead and apply that fix."
      - "Update the code to do Y."
      - "Proceed with the changes."
    - Not authorized examples (discussion/troubleshooting; no code changes):
      - "Why is this happening?"
      - "What do you think is wrong?"
      - "How would you fix this?"
      - "What are my options?"
      - "Can you take a look?"
      - "What does this code do?"
    - Ambiguous examples (MUST STOP and ask which mode the user wants):
      - "Can you try X?"
      - "Maybe change Y?"
      - "Should we do Z?"
      - "Let's do X next." (without a clear "implement" instruction)
    - Special case: debugging/logging and other "small" edits:
      - Adding/removing debug logs, changing test assertions, and "quick refactors" are still code changes and require explicit authorization when in discussion/troubleshooting mode.

- 🟡 semantics (workflow-scoped mechanics; no leakage)
  - 🟡 semantics belong in shared workflow mechanics (core process-flow guide + referenced by workflow guides), not as a global policy rule.
  - 🟡 means TODO; 🟡 can also mean "implemented but pending approval" and must not be cleared until the human approves.
  - Do NOT require a "(pending approval)" suffix by default (too much file churn). Treat "pending approval" as an implicit 🟡 state, and surface it in checkpoint outputs / working docs instead of rewriting many 🟡 markers.
    - Optional fast-path (if we ever want the explicit suffix): use editor/project search + replace to add/remove the suffix in bulk for the current working document only (not across arbitrary project files), so it stays feasible.
  - Require every 🟡 marker to be individually updatable via a stable identifier on the same line (so tools can target one item reliably).
    - Principle: do not rely on line numbers; rely on stable IDs that survive edits.
    - Allowed stable identifiers (choose the best fit per artifact):
      - Work specs: task number + title line (e.g., `3. **Do thing** 🟡`) -- update by editing that one line.
      - Unit tests: function name (e.g., `@Test func testFoo() ... // 🟡`) or MARK section title -- update by editing that one symbol-bearing line.
      - Planning/working docs: explicit IDs (e.g., `🟡 [Q-03] ...`, `🟡 [DEC-02] ...`) -- update by searching for the bracketed ID.
    - Tooling expectation:
      - Individual updates can be done by searching for the stable identifier and removing/replacing the 🟡 on that same line.
        - Tools: editor search (scoped to the current working document), or CLI ripgrep (`rg`) to locate the identifier quickly before editing.
      - Bulk updates (optional) should be constrained to a single working document or a clearly scoped section, never repo-wide.

- Core process-flow guide scope (shared mechanics)
  - Create `Guides/Core/process-flow.md` to define: what a gate is, STOP-and-wait semantics, what "next" means, what to do when blocked, and the standard gate line.
  - README carries the human-facing contract (what you will see + how to respond).
  - Standard gate-line convention belongs in `README.md` (human contract) and in the shared core process-flow guide (canonical mechanics). Guides should reference it rather than re-stating inconsistently.
  - Standard gate line wording:
    - Continue: `⏳ GATE: Next: <thing>. Say "next" or what to change.`
    - Complete: `⏳ GATE: Complete. Say "next" or what to change.`
    - Blocked: `⏳ GATE: Blocked. Say "next" or what to change.`
  - Proposal: put only shared mechanics in `Guides/Core/process-flow.md`; keep workflow-specific gates and steps in each workflow guide.
    - `Guides/Core/process-flow.md` should define:
      - What a checkpoint/gate is, what "STOP and wait" means, and that the human controls progression.
      - The standard gate line convention (Continue/Complete/Blocked variants).
      - Shared command semantics:
        - "Advance intent" advances past the current checkpoint once a workflow is active. Common examples: `"begin" | "next" | "continue"`, plus natural language equivalents like "go for it", "proceed", "do it", etc.
        - Separate concept: context-setting phrases (e.g., "start implementation", "start debugging") primarily select/activate the relevant workflow/skill; once active, "advance intent" moves through that workflow's checkpoints.
        - `auto` means "advance intent, but bypass checkpoints" -- it does not bypass universal STOP conditions (blocked/missing tool/destructive/etc.).
      - Workflow-scoped 🟡 semantics:
        - 🟡 means TODO; may include "implemented but pending approval"; do not clear until approved.
        - Marker update protocol: stable identifiers; individual updates; bulk updates scoped to a single working document/section.
      - What to do when blocked:
        - how to ask for missing evidence/tooling/clarification
        - use the `⏳ GATE: Blocked...` line when waiting
      - Guide structure expectation:
        - each workflow guide has a `## Checkpoints` section near the top that links to this doc for mechanics
    - Each workflow guide should define:
      - its workflow-specific gate points (the "when to STOP" list) and any workflow-specific `auto` behavior
      - its phases/steps, prerequisites, artifacts, and workflow-specific failure modes

- 🟡 Workflow-specific gates (per workflow guide)
  - 🟡 Each workflow guide must enumerate its gate points and end checkpoint outputs with the standard gate line.
  - 🟡 Guides can call out workflow-specific failure modes, but should reference (not restate) universal invariants.

- Literal instruction compliance (execution-level invariant; distinct from deviation gates)
  - Context: sometimes the human specifies *how* to make a change (comment out vs delete, exact format/wording, "use this commit hash in the comment", etc.). Agents often "improve" the instruction instead of following it.
  - Distinction:
    - Deviation gate = "spec/plan says X, you are about to do not-X" (architectural/requirements-level).
    - Literal-instruction compliance = within an approved approach, do X *the way the human said*.
  - Proposal wording (encode as a universal invariant in an existing policy, likely `Policies/unauthorized-changes.md`):
    - If the human gives an explicit instruction about *how* to perform a change, follow it literally.
    - If you believe the instruction is suboptimal, STOP and ask before acting -- do not substitute your preferred approach.

### Bucket A implementation plan (reliability-first)

Goal: improve *reliable compliance* with existing safety/process rules by putting universal invariants into "always-on" surfaces (policies -> generated Cursor rules) and consolidating process-flow mechanics so guides can be consistent.

Keep process-flow mechanics in `README.md` (human contract) + `Guides/Core/process-flow.md` (LLM procedure) only. Do not add a new always-on policy / generated `.mdc` rule for process-flow mechanics.

Guide-edit discipline (to avoid slop / drift)

- Before editing a guide:
  - Provide a short assessment of that specific guide (what’s missing vs `Guides/Core/process-flow.md`, what is workflow-specific vs shared).
  - Wait for human green light before making changes to that guide.
- After editing a guide:
  - Quick self-check on that file:
    - No duplicated process-flow mechanics that are already defined in `Guides/Core/process-flow.md`.
    - Uses `## Checkpoints` house style and references `Guides/Core/process-flow.md`.
    - Checkpoint outputs are instructed to end with the standard `⏳ GATE:` line (by reference to the core guide).
    - Terminology: "advance intent" (no "Next Command").
- Periodically during the sweep:
  - Search for terminology drift (e.g., "Next Command") and remove it.
  - Search for duplicated `auto` definitions outside `Guides/Core/process-flow.md` and collapse to references.

Implementation tasks (not discussion topics):
- 🟡 Policy hardening (universal invariants):
  - 🟡 Strengthen `Policies/safe-operations.md` with bright-line prohibitions + explicit STOP/ask language for destructive operations (esp. git) and other irreversible actions.
  - 🟡 Strengthen/clarify `Policies/unauthorized-changes.md` so "discussion/troubleshooting" mode is unambiguous and includes common failure modes (e.g., adding debug logs is still a code change).
  - 🟡 Add explicit "tool missing/broken => STOP" + "no workaround substitution" invariants (either in an existing policy or a new core policy -- depends on the open decision above).
  - 🟡 Ensure 🟡 semantics are described in a way that matches actual usage: TODO, and "implemented but pending approval" still counts as TODO until approved.
  - 🟡 Tighten `Policies/debugging-process-rule.md` so it enforces "read + follow `Guides/Core/debugging-guide.md`" and makes tactic selection observable (name the tactic each iteration).
- 🟡 Rule-template / activation pass (Cursor):
  - 🟡 Ensure the Cursor adapter continues to generate managed `.mdc` rules for all universal policies (already done for safe-operations/unauthorized-changes/debugging, etc.).
  - 🟡 If a new policy is added, update `Install/Cursor/install-update-cursor.md` recommended generated rules list and `assets.manifest.json` accordingly.
- 🟡 Shared process-flow core guide + guide audit + README update (ordered):
  - 🟡 Create `Guides/Core/process-flow.md` first (canonical mechanics: what gates are, STOP-and-wait semantics, advance intent vs context-setting, `auto` semantics, what to do when blocked, standard gate line, 🟡 marker protocol + update tooling).
  - 🟡 Audit/update ALL workflow guides next:
    - 🟡 Add `## Checkpoints` sections per the approved house style.
    - 🟡 Convert any "phase complete when..." descriptions into explicit STOP gate points where needed.
    - 🟡 Ensure debugging + unit-testing guides align with the approved approval gates (no fix without approval; experiment-level checkpoints; etc.).
  - 🟡 Update `README.md` last:
    - 🟡 Human-facing process-flow contract (what gates look like, how to respond, standard gate line, "Complete"/"Blocked" meaning).

🟡 Guide edits plan (where we plan the actual guide changes)

Purpose: list the concrete edits required in each guide to achieve: (1) explicit workflow-specific gate points, (2) consistent gate semantics via `Guides/Core/process-flow.md`, and (3) consistent human-visible checkpoints via the standard gate line.

- Target pattern for each workflow guide:
  - Add a short "Process flow" / "Checkpoints" section that:
    - links to `Guides/Core/process-flow.md` for shared mechanics
    - enumerates this guide's workflow-specific gate points
    - ends each checkpoint output with the standard gate line
  - Remove duplicate restatements of universal invariants (keep them in policy; reference if needed).

- Guides to update (Bucket A scope):
  - `Guides/Spec/work-spec-creation.md`
    - Add explicit STOP/checkpoints after each stage (it currently has “complete when…” language in places).
    - Reference `Guides/Core/process-flow.md` and use the standard gate line.
  - `Guides/Spec/work-spec-implementation.md`
    - Align checkpoint language with the standard gate line (it already has strong STOP semantics).
    - Ensure deviation/ambiguity STOP points end with the standard gate line.
  - `Guides/Core/debugging-guide.md`
    - Add explicit experiment-level checkpoints (stop after experiment to present conclusions; `auto` bypass; “stalled progress” stop condition even in `auto`), consistent with the process-flow contract.
    - Ensure “diagnosis -> propose fix -> wait for approval -> apply fix” is a hard gate.
  - `Guides/Test/unit-testing-guide.md` and sub-guides:
    - `Guides/Test/unit-test-planning-guide.md`
    - `Guides/Test/unit-test-infrastructure-guide.md`
    - `Guides/Test/unit-test-writing-guide.md`
    - Make checkpoint outputs consistently end with the standard gate line.
    - Remove any duplicated universal invariant phrasing and replace with references.
  - `Guides/Process/dev-retro.md`
    - Ensure any “STOP and ask” conditions end with the standard gate line (it already uses STOP directives).
  - `Guides/Process/report-process-problem.md`
    - Ensure the “write entry -> present for review -> iterate” points have explicit gates with the standard gate line.
  - `Guides/Process/process-improvement-tickets.md`
    - Ensure MCP-missing behavior is expressed as an explicit STOP gate (and ends with standard gate line).
  - `Guides/Core/update-installation-guide.md`
    - Align “STOP” points (missing install-state, human acknowledgement before proceeding) with standard gate line.

## Bucket B: Debugging guide - evidence-first mechanics (reduce speculative fixes)

Theme: Tighten the debugging loop so "testing a hypothesis" means "run a discriminating experiment", and add concrete tactics (bisection, unit-test repros, prior-art search, log cleanup). Several of these also require explicit consent gates (overlap with Bucket A).

Primary tickets (all target `Guides/Core/debugging-guide.md` unless we decide to factor into a policy):
- #3 "Debugging guide should distinguish 'test hypothesis' from 'apply fix'"
- #5 "Debugging guide should define 'code bisection' concretely"
- #6 "Debugging guide should add a hard gate before declaring root cause"
- #15 "Proactive log cleanup after hypothesis narrowing"
- #16 "Propose reproducing bugs in unit tests as a discriminating experiment"
- #17 "Research prior art in forums and related projects before proposing fixes"
- #18 "Explicit consent gate before implementing fixes"

Key overlaps:
- Overlaps Bucket A on: explicit stop gates, consent gates, and phase checkpointing conventions.

Design questions this bucket raises:
- 🟡 What are the exact "gate boundaries" in debugging? (e.g., hypothesis -> experiment, narrowed space -> next experiment, root cause -> propose fix, propose fix -> implement fix)
- 🟡 Where do we draw the line between "can be proven by inspection" vs "requires runtime evidence"?

## Bucket C: Work spec workflow rigor (creation + implementation)

Theme: Strengthen spec workflows so agents do not silently deviate, and so implementation quality checks (like building) are represented as explicit subtasks rather than optional best-effort reminders.

Primary tickets:
- #9 "Work spec creation guide should require build verification subtasks"
- #21 "Mandatory stop-and-ask before deviating from a work spec"
- #19 "Follow explicit instructions literally -- do not substitute a 'better' action" (applies within tasks)
- #13 "Global 🟡 lifecycle rule to prevent premature resolution" (applies to task-level completion signaling)

Key overlaps:
- Overlaps Bucket A on: deviation gates and checkpoint conventions.
- Overlaps Bucket D (safety operations) if build/test verification guidance implies new "safe command" constraints.

Design questions this bucket raises:
- 🟡 Should "build verification" be a required subtask template in work specs, a rule in the creation guide, or both?
- 🟡 How do we enforce "do not edit the spec to match a deviation" procedurally (and, if applicable, structurally in templates)?

## Bucket D: Safety and irreversible operations (especially git)

Theme: Hard safety rails around destructive operations, with explicit human approval gates, and explicit prohibition language (not just "be careful").

Primary tickets:
- #20 "Hard prohibition on destructive git operations without explicit human approval"

Related/overlapping tickets:
- #14 "Agent should stop immediately when a required tool is missing or broken" (same "do not improvise" safety posture)

Design questions this bucket raises:
- 🟡 Where should this rule live for maximum effectiveness: a policy doc, a core guide, a Cursor rule, or multiple?
- 🟡 Do we want a general "destructive operations" checklist beyond git (file deletion, data resets, etc.), or keep it narrowly scoped?

## Bucket E: Process improvement system hygiene (tickets + retros)

Theme: Improve the meta-workflows that generate and implement process tickets: ensure the retro outputs are high quality and that ticket tooling guidance matches tool reality.

Primary tickets:
- #11 "Retro process reflection should include evaluation criteria for suggestions"
- #4 "Process ticket guide should include explicit label options"
- #7 "Process ticket guide should include explicit label options"

Notes:
- 🟡 #4 and #7 appear to be duplicates (same title and body). We should decide whether to close one as duplicate after we implement the combined fix.

Design questions this bucket raises:
- 🟡 Where should label options live: embedded list in the guide vs a referenced file in-repo (so it can be updated without needing GitHub label discovery)?
- 🟡 What criteria will meaningfully improve suggestion quality (vs re-stating rules that already exist)?

## Bucket F: Repo documentation and working-doc structure

Theme: Make the repository's docs and working-doc conventions clearer and easier to follow.

Primary tickets:
- #1 "Improve working document organization"
- #2 "Skill documentation"

Design questions this bucket raises:
- 🟡 Are working-doc conventions defined in one authoritative place today, or scattered across guides?
- 🟡 For skill documentation: what information belongs in `README.md` vs a dedicated doc (keeping README readable)?

## Cross-bucket consolidation candidates (to reduce churn)

These topics show up in multiple buckets; we should design them once and then apply consistently:

- 🟡 Standardized gate line + explicit STOP checkpoints (Buckets A, B, C, D)
- 🟡 Consent gate before applying fixes (Buckets A, B)
- 🟡 Stop immediately when a required tool/integration is missing or broken; ask the human how to proceed (global invariant; Buckets A, D)
- 🟡 Do not substitute tools or invent workarounds without explicit human approval (global invariant; Buckets A, D)
- 🟡 Always stop and ask for help when something goes wrong / an unexpected condition arises (global invariant; all buckets)
- 🟡 `🟡` lifecycle rules and when they can be cleared (Buckets A, C)

## Likely files impacted (hypothesis, not a commitment)

- `README.md` (process flow principles; possibly gate line convention)
- `Guides/Core/debugging-guide.md`
- `Guides/Spec/work-spec-creation.md`
- `Guides/Process/work-spec-implementation.md`
- `Guides/Process/dev-retro.md`
- `Guides/Process/process-improvement-tickets.md`
- `Policies/swift-code-organization.md`
- (Maybe new) `Guides/Core/process-flow.md` or similar, if we choose to centralize shared gate conventions
- (Maybe new) `Guides/Process/safe-operations.md` or policy equivalent for destructive git rules

