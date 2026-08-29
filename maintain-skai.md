# Maintain `skai` (LLM maintainer runbook)

This file is instructions for an LLM making changes **to the `skai` repo itself** (not installing into a host project).

## Safety defaults

- Do not commit unless explicitly asked.
- Do not delete files unless explicitly asked.
- Do not add dependencies unless explicitly asked.
- Keep edits minimal and reversible.

## Before you change anything

1. Read `README.md` to understand the intended system.
2. Identify what kind of change this is:
   - guide/policy content change
   - installer/runbook change
   - template change
   - repo metadata change (manifest/changelog/readme)
3. Propose a short plan and then proceed.
4. After significant edits (multi-file changes, path moves, installer behavior changes), run `maintain-retro.md` and fix straightforward misses immediately.

## Required bookkeeping (most common misses)

When you change assets, keep these in sync:
- `assets.manifest.json`
  - add/move/rename assets here
  - keep `id` stable when possible
- `README.md`
  - update the Usage section for developer-facing skills (see "README Usage section conventions" below)
- `CHANGELOG.md`
  - add an entry under the top `## Unreleased` section for changes that affect a host installation (prefix each line item with the date, `YYYY-MM-DD`)
  - **Audience: the installing agent, not a human reader.** Entries are consumed by the agent updating an existing host installation. Each must give that agent what it needs to migrate: assets renamed or moved (state old path → new path), assets added or removed, managed-block / managed-header changes, and anything that must be re-run. Omit pure-internal changes that don't touch a host (working-doc edits, test-harness tweaks, refactors with no asset effect).
  - **`## Unreleased` is a staging log, not finished notes.** Entries stack up across sessions as work lands — that is expected. Within your own session, write the *net* entry for your change; don't narrate your own back-and-forth (no "add X" then "rename X to Y" in the same batch). Do not rewrite or reconcile earlier sessions' Unreleased entries as you go — you may lack their context. Cross-session overlaps are merged later, at the cut (see `## Release planning` below).
  - released sections are frozen: below a `## Release <N>` heading (or the legacy `## Released` bucket), entries are append-only history — fix an outright error, but never rewrite shipped scope.
  - always determine the date by running `date +%Y-%m-%d` in the terminal (see `Install/managed-header.md`, "Determining today's date")
  - format entries for fast scanning: prefer multiple short bullets over one giant "mega-entry"; short bold headline + 1-2 sentences max; group by theme when many files change (core mechanics, policies, spec guides, test guides, templates, etc.)
 - Skills (if you add/change them):
   - shared templates live at `Templates/skills/skai-*/SKILL.md`
   - Cursor installer installs them into host repos at `.cursor/skills/`
   - Claude Code installer installs them into host repos at `.claude/skills/`
   - Codex installer installs them into host repos at `.agents/skills/`
   - **Wrapper pattern (invariant)**: skill templates must be thin wrappers -- a few lines that point the LLM at the corresponding Guide(s) in `Guides/`. All substantive logic lives in the Guide, not in the skill template. This keeps the files copied into host projects small and ensures the Guide is the single source of truth.
   - When adding a new skill: start by writing the Guide under `Guides/`, then create the skill wrapper that references it. This order prevents accidentally inlining logic into the skill template.
 - Install state file:
   - All adapter runbooks write `skai/install-state.json` on successful completion.
   - The `update-installation` skill reads this file to determine which adapters to re-run and what SHA was last applied.
   - If you add a new adapter runbook, ensure it writes/merges its entry into this file.

## Release planning

Releases are cut by the human using normal git release mechanisms — a `v<N>` tag on the release commit. The human decides the scope and timing; the agent never cuts a release on its own. `CHANGELOG.md` mirrors this: a `## Unreleased` staging section at the top, frozen `## Release <N>` sections below it (newest first), and a legacy `## Released` bucket at the bottom for entries that predate release numbering.

**Default:** new changelog entries go under `## Unreleased`, which is a staging log (see the `CHANGELOG.md` rules above) — left to accumulate, not consolidated as you go.

**Cutting release `<N>`** (only when the human asks):

1. **Consolidate** the whole `## Unreleased` stack into clean notes for the installing agent — merge related entries, drop superseded intermediate steps, group by theme. Cross-check `git log` since the previous release so nothing host-affecting is missed.
2. **Convert** the `## Unreleased` heading to `## Release <N> — <YYYY-MM-DD>`; those bullets are now frozen.
3. **Open** a fresh empty `## Unreleased` at the top.

The human tags the release commit `v<N>` and pushes it. That tag is the anchor the update workflow targets by default; the `## Release <N>` heading and the `v<N>` tag name the same release.

## Guides/ subdirectory convention

All guides live under a topical subdirectory within `Guides/`. Do not place guides at the `Guides/` top level.

| Subdirectory | Purpose |
|---|---|
| `Core/` | Cross-cutting foundations: debugging, working-doc conventions, update installation |
| `Spec/` | Work spec creation and implementation |
| `Test/` | Unit testing (planning, infrastructure, writing) |
| `Process/` | Retro, process problem reporting, ticket creation |
| `UIMap/` | UI Map system: YAML format, platform references, planning/implementation methods, FigJam migration |

When adding a new guide, place it in the most appropriate existing subdirectory. If none fits, propose a new subdirectory and document it here.

## Guide house style

Applies to all workflow documents: files under `Guides/`, internal runbooks (`maintain-*.md`), and skill entry points (`SKILL.md` files under `Templates/skills/`, `.cursor/skills/`, `.claude/skills/`, and `.agents/skills/`). Follow these rules whenever adding or substantially editing any of them.

### Required elements

- **Managed header**: required on files that are registered assets in `assets.manifest.json` — everything under `Guides/`, installed skill/policy/template files, and the manifest-tracked runbooks `maintain-retro.md` and `maintain-tickets.md`. The header (`Managed-By`, `Managed-Id`, `Managed-Source`, `Managed-Adapter`, `Managed-Updated-At`) gates safe overwrites of host-installed files and must carry a `Managed-Id` matching its manifest entry. `maintain-skai.md` itself is the meta-runbook — not a manifest asset, never installed into a host — so it carries no header.
- **Terminology**: use "advance intent" (never "Next Command").
- **Lean core, deep links**: keep core guides concise; if a tactic/procedure is detailed and rarely used, place it in a dedicated guide/appendix and link to it from the core guide. **Exception — runtime process-flow mechanics** (gates, advance intent, marker conventions) are inlined verbatim per `Standard structure for guides with gates` below. Lean for content; inline for runtime mechanics. Agents skip indirect references for runtime behavior, so process-flow content must live in the guide the agent is executing.

### Examples vs. derivations

Agents copy the worked **example**, not the surrounding prose — an example outweighs any rule, and a missing or mismatched one misleads more than absent text. Two consequences for authoring:

- **Each distinct *path* a guide teaches needs its own faithful example.** With only one (e.g. only the audit case, or only the root case), it becomes the gravitational center and agents misapply it to the other paths.
- **Never enumerate *compositions*.** Route kinds, options, and states combine combinatorially — an example per combination bloats the guide and still leaves gaps. State the governing rule as a **decision procedure the agent applies** ("before X, ask Y; do Z only if…"), frame per-case recipes as *derivations* of it, and let the agent derive the combinations you didn't draw. Illustrate the bounded base set; derive the rest.

### Discussion-phase authoring (when applicable)

If the guide you're writing or editing includes a discussion phase (a phase where the agent proposes design items and the human refines, accepts, or rejects them), read `Guides/Core/process-flow.md` § "Structured discussion items" **before drafting the discussion content**. That section is canonical for:

- the item-line shape (`- [ ] <ID> [Kind] <summary>`)
- the Kind taxonomy (`[Question]` / `[Proposal]` / `[Tradeoff]`)
- the sub-bullet labels (`Concern` / `Proposal` / `Options` / `Detail` / `Why` / `Decision`)
- the resolution mechanic (check the box + append `- **Decision** <resolution>.`)
- the discussion-phase gate cycle (blocked while items remain, planned the moment they're all resolved — the *first planned gate* of a discussion-based workflow)

Treat it as an authoring input, not a runtime read. Once the discussion phase is drafted per the canonical, the standardized gates template (below) still applies to the workflow's gate behavior overall.

### Standard structure for guides with gates

If the guide is a gated workflow — one where the agent waits on the human and emits `⏳ GATE:` lines — inline the process-flow operational template in both sections. A bare "STOP" inside a method guide (stop and run the self-check; stop and present a tradeoff) is not a gate and needs neither section. Do not reference `Guides/Core/process-flow.md` as a runtime dependency -- agents skip indirect references.

```
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

Workflow-specific gate notes (optional):
- If a planned gate has workflow-specific semantics rather than the default "review complete, say `next` to advance" behavior, state the exact gate response and what `Next` means there.
- Review/handoff gates are one common example, but not the only allowed variation.
- Recognition test for a non-standard planned gate:
  - If the human response needed there is not simply "review complete; `next` means approve-and-advance", treat it as non-standard.
  - If leaving the gate standard would misdescribe what the human should do next, clear progress markers too early, or advance to the wrong phase, treat it as non-standard.
  - For any non-standard planned gate, document the exact `⏳ GATE: Next: ...` response, what kind of human response resumes the workflow, what `Next` means there, and how progress markers track that gate.
- For any non-standard planned gate, use progress markers in the most natural workflow artifact to show what remains open for that gate (marker convention defined in the Progress tracking block of the Advance intent template below).
- Make the marker lifecycle explicit:
  - which markers track gate/phase state vs local working state
  - what specific human intent approves clearing them
  - that the agent clears them only after that human intent is received
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

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit human resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking (**authoritative marker convention for skai workflow guides** — sanity scan enforces the same rule at `## Sanity scan` → "Marker convention compliance" below; canonical reference in `Guides/Core/process-flow.md` § "Progress markers"):

- **Two conventions, by artifact type:**
  - **`- [ ]` / `- [x]` in process artifacts** (markdown workflow docs: work specs, planning docs, working docs, retro outputs, ticket drafts, etc.). Completion is checking the box — the artifact preserves the audit trail of resolved items.
  - **`🟡` in source files** (test code, application code) seeded or planned by a skai workflow. Completion is **removal** of the marker — the file's remaining work is read by which `🟡`s remain. Canonical in-code case: `Guides/Test/unit-test-planning-guide.md`.
- Default rule: a progress marker means TODO or pending approval. Do not clear it without human approval.
- At a planned gate, advance intent is the approval signal for clearing the guide-owned progress markers completed by the phase that just finished.
- Ordering rule: the agent first stops and waits at the gate, then clears the approved markers (`- [ ]` → `- [x]` in a process artifact; remove `🟡` in code) only after the human gives advance intent.
- If a workflow needs a custom marker lifecycle (for example, inline discussion items resolved during a human-led discussion loop), define that exception explicitly and narrowly below.
- If a workflow uses both gate/phase markers and local working markers, keep them distinct: local approvals clear local working markers; advance intent clears the gate/phase marker.
- For any custom marker lifecycle, specify both:
  - the artifact where the markers live
  - the exact human intent that authorizes clearing them

**Not workflow progress:** the `🟡` convention in `Templates/docs/skai/integration.md` and `Install/integration-doc-install-update.md` (project-specific missing constants needing human input during host install) is a separate concept, scoped to that section's rules. Don't conflate the two.

<workflow-specific advance behavior>
```

**Gates section rules:**
- Copy the standardized gates template verbatim, then add workflow-specific planned gates.
- If the guide has a custom review/handoff gate, explicitly state the exact `⏳ GATE: Next: ...` response and what human action resumes the workflow.
- Keep blocked-gate behavior generic unless the workflow has concrete blocker cases discovered through retros.
- Every place the guide says the agent must STOP and wait on the human must correspond to a `⏳ GATE:` line in the runtime behavior.
- After the template block, list this guide's workflow-specific gates.

**Advance intent section rules:**
- Copy the standardized advance intent template verbatim (the block above starting "Advance intent moves past").
- After the template block, add workflow-specific behavior (if any): custom advance actions, `auto` milestone names, custom marker-lifecycle exceptions, hard gates that `auto` does not bypass.

### Process-flow house style

`Guides/Core/process-flow.md` is the **house style reference** for process-flow mechanics. It is the canonical definition used by maintainers to ensure consistency across guides. It is NOT a runtime reference that agents read during workflow execution.

The operational core is inlined in each guide using the standard template above. When process-flow house style changes:
1. Update `Guides/Core/process-flow.md` (the canonical definition).
2. Update the standard template in this section.
3. Propagate the template changes to all workflow guides.

**What guides should contain (inline):**
- The standardized gates and advance intent template (copied verbatim)
- Workflow-specific gate descriptions, phase sequencing, `auto` skip/fix rules
- Workflow-specific procedures, examples, and reference material

**What guides should NOT contain.** Most of these are enforced by a corresponding sanity-scan check (`## Sanity scan` below); where a sanity-scan reference is given on a bullet, the authoritative rule phrasing lives there. The list here is for awareness during authoring.

- References to `Guides/Core/process-flow.md` as a required runtime read — sanity scan: "Process-flow template compliance" / "References to `Guides/Core/process-flow.md` that imply it is a required runtime read."
- "Flow" or "Process Overview" subsections that embed checkpoint behavior or marker-clearing steps alongside phase sequencing — state only which phases exist and their order.
- Standalone "Progress Tracking" or "Emoji System" sections that redefine the canonical marker conventions — sanity scan: "Process-flow template compliance" / "Standalone 'Progress Tracking' or 'Emoji System' sections that redefine the canonical marker conventions."
- Inline restatements of marker-clearing timing unless gated on advance intent — sanity scan: "Flow control integrity" / "Any 'remove 🟡' or 'check the box' language…"
- Discussion items in aggregator sections (`## Questions`, `## Decisions`, etc.) instead of inline with their topic — sanity scan: "Marker convention compliance" / "Discussion items in aggregator sections…"

### Flow reflection (required for guides with gates)

After editing a guide with gates, imagine a fresh agent using it from the start of the workflow and mentally step through the first few human/agent exchanges plus each gate transition.

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
- what human response resumes the workflow
- whether that response is advance intent, local approval, or some other workflow-specific action
- which workflow-owned artifact is tracking that gate or phase
- which specific progress marker is still present while waiting (the unchecked `- [ ]`, or the `🟡` in code)
- what marker changes on resolution, and only after what human intent
- what exact artifact change happens after that human intent

Look specifically for:
- waits on the human that do not end with a `⏳ GATE:` line
- gates where `Next` is unclear or misleading
- planned gates that have no workflow-owned artifact or no gate/phase marker to clear
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

### Sanity scan (after every edit)

Run this scan after *each* guide edit, not just at the end of a batch. Deferring the scan to the end of a batch is the proven failure mode -- violations introduced early in the batch survive unchecked.

**Record the result of every check, even when clean.** For each check below, write down either `0 occurrences` (with the search / inspection used — file paths, `grep` / `rg` pattern, or "visual review of section X") or a list of occurrences classified per-check (e.g., `<path>:<line>` → `false positive (intentional per …)` / `to fix` / `to revisit`). Reading the check and self-certifying "done" without a recorded result is the failure mode this rule prevents — a `0 occurrences` line with the search used is the minimum evidence. This matches the recording discipline already required for flow-reflection simulations (see `## Flow reflection` above).

Checks:

**Structure:**
- Missing `## Gates` section (if the guide has gates)
- Missing `## Advance intent` section (if the guide has gates)
- Inconsistent terms ("Next Command" instead of "advance intent")
- Mixed gate terminology ("checkpoint" and "gate" used interchangeably without a workflow-specific reason)
- Stack-mismatched references (e.g., Xcode terms in Android-only sections)
- If the guide creates working docs or artifacts, stale path layouts that skip the required `session-name` folder

**Process-flow template compliance:**
- Gates section missing the standardized gates template (the block starting "Core rule: every time the agent is waiting on the human...")
- Advance intent section missing the standardized advance intent template (the block starting "Advance intent moves past the current gate.")
- References to `Guides/Core/process-flow.md` that imply it is a required runtime read (e.g., "This guide follows the shared process-flow mechanics in...")
- Standalone "Progress Tracking" or "Emoji System" sections that redefine the canonical marker conventions (`- [ ]` / `🟡`).

**Marker convention compliance:**
- `🟡` used in process artifacts (markdown workflow docs) — should be `- [ ]` / `- [x]` instead. `🟡` is reserved for in-code progress (test files, source files) where completion = removal. Canonical in-code case: `Guides/Test/unit-test-planning-guide.md`.
- `- [ ]` items missing a stable letter-led ID on the same line (e.g., `- [ ] Do thing` instead of `- [ ] T1 Do thing`). Letter-led so a leading digit isn't misparsed as an ordered-list item.
- Loose `- [ ]` lists under the same heading (blank lines between sibling items) — pushes the checkbox onto its own line in some renderers. Use tight lists for sibling checkbox items.
- `- [ ]` inside a heading line (`## - [ ] Foo`) — markdown task lists are scoped to list items; this renders as plain text.
- Discussion items in aggregator sections (`## Questions`, `## Decisions`, `## Tradeoffs`, `## Open Items`) instead of inline with their topic.
- Discussion items missing the `[Kind]` label (`[Question]` / `[Proposal]` / `[Tradeoff]`) — every item should declare its shape.
- Discussion phases that do not use the canonical gate pattern: blocked gate while `- [ ]` items remain, planned gate the moment they're all resolved (the *first planned gate* of the workflow). See `Guides/Core/process-flow.md` "Discussion-phase gate behavior".
- Discussion phases with a separate "draft is ready, please review" planned gate before the discussion begins — this duplicates the blocked/planned gate cycle. The drafting response itself should end with the blocked or planned gate per item state.

**Flow control integrity:**
- Any place where the guide says the agent waits for the human but does not end with a `⏳ GATE:` line in the described runtime behavior.
- Walkthroughs or examples that show multi-turn back-and-forth at a gate but only display the `⏳ GATE:` line on the first turn. Every turn that ends with the agent still waiting on the human should re-emit the gate line verbatim.
- Guide-defined ad-hoc `⏳ GATE:` lines that don't correspond to gates listed in the guide's `## Gates` section (the "fabricated gates" anti-pattern). Each `⏳ GATE:` template in the guide should trace back to a named gate.
- Any planned gate that does not have a workflow-owned artifact and a gate/phase marker that remains while waiting for advance intent.
- Any "remove 🟡" or "check the box" language that is not explicitly gated on advance intent or a documented workflow-specific exception. Search for `remove 🟡`, `Remove 🟡`, `check the box`, `mark `…` complete`, and `- [x]` walkthroughs, and verify each occurrence is tied either to a gate/advance-intent step or to an explicitly documented custom lifecycle.
- Any guide where the planned gate exists but the post-approval artifact change is not explicit (for example, no statement of which marker is cleared after advance intent).
- Flow/sequence descriptions where marker clearing appears before a STOP/gate (wrong order -- the STOP comes first, marker clearing happens on the subsequent advance intent unless a documented local exception applies).
- Examples or walkthroughs that show markers cleared without a preceding gate + advance intent step, unless the guide explicitly documents a narrower exception (for example, inline discussion items resolved during human-approved discussion).
- `auto` sections that list gates bypassed by `auto` without labeling which gates are hard (not bypassed). If a guide has both soft and hard gates, the `## Gates` section should label the hard ones.
- Inline "Gate:" signposts that add mechanics not present in the `## Gates` section (acceptable to say "Gate: STOP"; not acceptable to add new rules about what happens at the gate unless they are already defined in the gate model).
- If the guide defines working-doc paths, any examples or artifact paths that place files directly under `skai/working-docs/<branch-path>/...` instead of `skai/working-docs/<branch-path>/<session-name>/...`.

## README Usage section conventions

The Usage section documents each **skill** (not sub-processes or internal maintenance workflows). Each entry follows this format:

1. Heading: `### <Human-readable name> (skill <skill-name>)` (no colon)
2. One-paragraph description of what the workflow does.
3. **Prerequisites:** what's needed before starting.
4. **Phases:** numbered list of the workflow's phases. Each phase is one line: `<number>. **<Phase name>.** <What happens>.`
   - If a phase has sub-steps, use a numbered sub-list under the phase.
   - If an entire phase is optional, mark it `(optional)` in the phase name.

Formatting rule:
- When referencing a file or directory path within this repo in `README.md`, use a markdown link so humans can click it in the browser (do not leave bare backticked paths).

Do not add entries for:
- Sub-processes that are invoked by other skills (e.g., the filing phase of the ticket-filing guide is invoked by the retro -- it appears as a phase within that entry, not as its own heading).
- Internal maintenance workflows (e.g., `maintain-tickets.md` -- these belong in the Development guide section).

## Content rules (project goals)

- Prefer IDE-neutral `.md` sources in this repo.
- IDE-specific outputs (e.g., Cursor `.mdc`) are generated into host repos by installer runbooks under `Install/`.
- Keep examples project-agnostic (use the shared fictional theme, currently "LumenNotes").

## Installer invariants (do not regress)

The install/update runbooks must remain robust across:
- returning to a host repo later,
- updating the submodule,
- starting a fresh LLM session,
- running install/update again.

To preserve that:

- **Idempotency**: re-running install/update should converge to the same end state without manual cleanup.
- **Managed overwrites only**:
  - Generated host files are overwriteable only if they contain the managed header (`Install/managed-header.md`).
  - **Symlinks** are overwriteable only if they point at the expected `Submodules/skai/...` targets (symlinks cannot contain headers).
  - **Managed blocks**: some project-owned files (e.g., ignore files, Integration doc) are updated only inside delimited managed blocks.
- **Legacy candidates are permission-gated**:
  - Identify legacy candidates.
  - Propose delete/replace (often replace-with-symlink), but do not execute without explicit approval.
- **Gray areas must be surfaced**:
  - Example: legacy `.cursor/rules/debugging.mdc` should be flagged and deletion should be proposed only after migrating any project-specific logging conventions into the Integration doc and getting approval.

## Integration doc architecture (do not regress)

The Integration doc is project-owned at `skai/integration.md`, but is structured to support safe automation.

**Note on `🟡` semantics in this section.** The `🟡` convention used in the Integration doc (and its templates / installer guide) is a **separate concept** from the workflow-progress `🟡` defined in `Guides/Core/process-flow.md` § "Progress markers." Both share the emoji but serve different lifecycles:

| Convention | Where it appears | Semantics |
|---|---|---|
| Workflow-progress `🟡` | Source files (test code, app code) seeded by a skai workflow | TODO marker; completion is removal as the agent's work is approved (see `## Guide house style` above). |
| Integration-doc `🟡` | `Templates/docs/skai/integration.md` and host-installed `skai/integration.md` | "Required project-specific value is missing"; completion is human filling the value AND removing the marker (see rules below). |

Do not conflate them. The workflow-progress rule does not apply to Integration-doc fields, and vice versa.

Format rules:
- `Templates/docs/skai/integration.md` must be **minimal** and must not contain "meta" guidance.
  - No instructions to the installer/LLM (those belong in `Install/integration-doc-install-update.md`).
  - No instructions to humans about how to clear 🟡 markers (those belong in `README.md`).

Ownership rules:
- Humans may edit only the **Special instructions / overrides** section (freeform).
- The installer owns:
  - the `required-values` "form" block (structure + restoration of missing fields)
  - stack-specific sections inside `BEGIN/END Managed-By: skai` blocks.
- Stack-specific templates live under:
  - `Templates/docs/skai/integration-sections/`

When changing Integration templates/sections:
- Keep managed block markers minimal and stable:
  - `<!-- BEGIN Managed-By: skai | Section: <id> -->`
  - `<!-- END Managed-By: skai | Section: <id> -->`
- Keep 🟡 markers only for true project-specific missing constants/mappings.
  - Do not mark variables (e.g., `<Scheme>`, `<TestPlan>`, `<TestTarget>`) with 🟡.
  - Do not mark standard procedures/patterns with 🟡.
- Ensure section templates treat placeholders like `<Scheme>`, `<TestPlan>`, `<TestTarget>` as **variables** (agent-filled per task context).
- Ensure section templates are **integration-doc-ready** content:
  - no 🟡 TODO lists
  - no "installer/human instructions" (those belong in `README.md` and `Install/integration-doc-install-update.md`)
  - include copy/pasteable CLI command templates with `<...>` variables
- Ensure `Install/integration-doc-install-update.md` remains the canonical installer guidance for:
  - managed block merge/update/remove behavior
  - `{human response}` placeholders + `INSTRUCTION:` formatting and restoration rules

## If you change install/runbooks

After editing anything under `Install/`:
- Ensure `Install/conflict-precedence-policy.md` still matches the runbooks (managed header vs managed symlink behavior).
- Ensure `assets.manifest.json` includes any new policy/guide/runbook IDs referenced by the installer.
- Ensure `README.md` Quick start prompts still point at the correct submodule path (`Submodules/skai/...`).
- Ensure ignore-file behavior remains safe: update `.cursorignore` / `.claudeignore` via managed blocks and do not hide the submodule via agent ignore (use editor UI excludes instead).

## After changes (retro)

After making changes, run the post-change checklist in `maintain-retro.md`.

## How to guide an LLM (prompt template)

Use this as a starting prompt when maintaining this repo:

> You are updating the `skai` repo.
> Follow `README.md` and `maintain-skai.md`.
> Make minimal changes.
> Update `assets.manifest.json`, `README.md` (asset inventory), and `CHANGELOG.md` as needed.
> Do not commit or delete files unless I explicitly ask.
> After edits, summarize exactly what changed and list touched files.
