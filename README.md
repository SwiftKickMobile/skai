# `skai`

Reusable, mostly IDE-agnostic **agentic coding guides** and **policies** you can vendor into any repo.

This repo is designed to be installed as a **git submodule** and activated by an **LLM-runbook-driven installer** that:
- inspects the host repo (including legacy installs),
- proposes a migration plan,
- writes **managed files** only (safe updates),
- installs agent-facing assets into the host repo's expected directories (IDE/agent-specific),
- generates IDE-specific artifacts (e.g., Cursor `.mdc`) into the host repo.
- updates agent ignore files using managed blocks so multi-agent installs can coexist cleanly (permission-gated if the ignore files already exist).

Recommended host locations for agent-facing docs:
- Cursor: `.cursor/skills/skai-*/`
- Claude Code: `.claude/skills/skai-*/`
- Codex: `.agents/skills/skai-*/`

## Contents

- [Quick start](#quick-start-recommended)
- [How installs stay safe](#how-installs-stay-safe)
- [Integration document](#integration-document-how-to-use-it)
- [IDE clutter / autocomplete](#ide-clutter--autocomplete-recommended)
- [Usage](#usage)
  - [How all workflows work](#how-all-workflows-work)
  - [Work spec design](#work-spec-design-skill-skai-work-spec-creation)
  - [Work spec implementation](#work-spec-implementation-skill-skai-work-spec-implementation)
  - [UI Map architecture](#ui-map-architecture-skill-skai-ui-map-architecture)
  - [UI Map implementation](#ui-map-implementation-skill-skai-ui-map-implementation)
  - [Requirements authoring](#requirements-authoring-skill-skai-requirements-authoring)
  - [Requirements promotion](#requirements-promotion-skill-skai-requirements-promotion)
  - [Unit testing](#unit-testing-skill-skai-unit-testing)
  - [Debugging](#debugging-skill-skai-debugging)
  - [Dev retro](#dev-retro-skill-skai-dev-retro)
  - [Suggestion](#suggestion-skill-skai-suggestion)
  - [Update installation](#update-installation-skill-skai-update-installation)
  - [Working documents](#working-documents)
- [Development guide](#development-guide-for-contributors)

## Quick start (recommended)

### 1) Add the submodule (one-time)

From your host repo root:

```bash
git submodule add <REPO_URL> Submodules/skai
git submodule update --init --recursive
```

If you already have the submodule installed, just run:

```bash
git submodule update --init --recursive
```

### 2) Ask your agent to install/update (copy/paste)

Paste ONE of these prompts into your agent chat (from the host repo root).

#### Cursor prompt

> Install/update `skai` in this repo by following `Submodules/skai/Install/Cursor/install-update-cursor.md` ([`Install/Cursor/install-update-cursor.md`](Install/Cursor/install-update-cursor.md)).
>
> - If the `Submodules/skai` submodule is missing, add it there.
> - Do a discovery pass first, then propose a migration plan, then WAIT for approval before writing.
> - Use `skai/integration.md` ([`skai/integration.md`](skai/integration.md)) as the project-owned Integration doc and migrate any legacy build/test command notes into it (do not delete legacy files unless I explicitly approve).
> - Only overwrite files that contain the managed header (`Managed-By: skai`). Treat lookalike files without the header as legacy candidates.

#### Claude Code prompt

> Install/update `skai` in this repo by following `Submodules/skai/Install/ClaudeCode/install-update-claudecode.md` ([`Install/ClaudeCode/install-update-claudecode.md`](Install/ClaudeCode/install-update-claudecode.md)).
>
> - If the `Submodules/skai` submodule is missing, add it there.
> - Do a discovery pass first, then propose a migration plan, then WAIT for approval before writing.
> - Use `skai/integration.md` ([`skai/integration.md`](skai/integration.md)) as the project-owned Integration doc and migrate any legacy build/test command notes into it (do not delete legacy files unless I explicitly approve).
> - Only overwrite files that contain the managed header (`Managed-By: skai`). Treat lookalike files without the header as legacy candidates.

#### Codex prompt

> Install/update `skai` in this repo by following `Submodules/skai/Install/Codex/install-update-codex.md` ([`Install/Codex/install-update-codex.md`](Install/Codex/install-update-codex.md)).
>
> - If the `Submodules/skai` submodule is missing, add it there.
> - Do a discovery pass first, then propose a migration plan, then WAIT for approval before writing.
> - Use `skai/integration.md` ([`skai/integration.md`](skai/integration.md)) as the project-owned Integration doc and migrate any legacy build/test command notes into it (do not delete legacy files unless I explicitly approve).
> - Use `.agents/AGENTS.md` as the Codex instruction file.
> - Only overwrite files that contain the managed header (`Managed-By: skai`). Treat lookalike files without the header as legacy candidates.

These runbooks work with any IDE (JetBrains, Xcode, Android Studio, VS Code, etc.) or standalone agent environment. Stack-aware runbooks auto-detect the project stack and apply the appropriate guidance.

### 3) Set up a GitHub MCP server (optional)

Some workflows (process improvement ticket filing, ticket implementation) require a GitHub MCP server to create and manage GitHub issues. If you don't need these workflows, skip this step.

Add a GitHub MCP server to your IDE's MCP configuration with a personal access token that has repo issue permissions. The JSON format is the same across IDEs:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<your-token>"
      }
    }
  }
}
```

**Config file locations:**
- Cursor: `.cursor/mcp.json` (project-level) or `~/.cursor/mcp.json` (global)
- Claude Code: `~/.claude.json`
- Codex: use the MCP configuration location supported by your Codex environment.

## How installs stay safe

- **Integration doc (project-owned)**: [`skai/integration.md`](skai/integration.md) is the single source of truth for project-specific commands/paths (build/test/lint/etc). Templates live in [`Templates/`](Templates/).
- **Managed files**: host-project files written by the installer have a required header (see [`Install/managed-header.md`](Install/managed-header.md)). The installer overwrites only files that already contain this header.
- **Legacy installs**: lookalike files without the header are treated as **legacy candidates** and are not overwritten by default (see [`Install/conflict-precedence-policy.md`](Install/conflict-precedence-policy.md)).

## Integration document (how to use it)

The Integration doc ([`skai/integration.md`](skai/integration.md)) is the **project-owned** place where `skai` workflows get the concrete, copy/pasteable details they need to run deterministically (build/test commands, destinations, artifact paths, evidence expectations).

Why it matters:
- It prevents agents from guessing project-specific constants (like `xcodebuild -destination` strings, scheme/test plan conventions, or where `.xcresult` / logs are stored).
- It makes install/update migrations safe: the installer can preserve your filled values while updating the managed template structure around them.

How humans should fill it:
- **🟡 means "required project-specific value is missing."**
- Under a 🟡 item you may see one or more `INSTRUCTION:` lines. Those are **not part of the long-term document**; they exist only to explain what to fill in.
- When you fill a value:
  - remove the 🟡 marker
  - delete the `INSTRUCTION:` line(s) under it
- If a future install/update can't infer a required value with high confidence, the installer may **restore** 🟡 + `INSTRUCTION:` prompts so the doc remains a complete, reliable source of truth.

> **Note on `🟡`:** The Integration doc's `🟡` (missing project-specific value) is a separate concept from the workflow-progress `🟡` used in source files by skai workflows (see [Agent note-taking and progress tracking](#how-all-workflows-work) below). Both share the emoji; their lifecycles differ.

## IDE clutter / autocomplete (recommended)

To reduce duplicate autocomplete/search results (submodule sources + installed assets), hide the submodule in your editor UI while keeping the submodule [`README.md`](README.md) visible.

Example for Cursor/VS Code workspace settings (`.vscode/settings.json`):

```json
{
  "files.exclude": {
    "**/Submodules/skai/**": true,
    "**/Submodules/skai/README.md": false
  },
  "search.exclude": {
    "**/Submodules/skai/**": true,
    "**/Submodules/skai/README.md": false
  }
}
```

Android Studio (JetBrains):
- In the Project tool window, right-click `Submodules/skai` → **Mark Directory as** → **Excluded**.
- Optionally also exclude `.claude/skills/skai-*` or `.agents/skills/skai-*` if you don't want the skill install artifacts in search results.
- Prefer local IDE excludes over committing `.idea` changes unless your repo explicitly versions IDE config.

## Usage

After installation, workflows are available as **skills** that your agent activates automatically based on conversational context.

### How all workflows work

**Minimal command structure.** You don't need to memorize strict commands:

1. Start with context that activates a skill/workflow (e.g. "Write a work spec", "Start unit testing", "Start debugging").
2. Progress through steps using **advance intent** (e.g. "begin", "next", "continue", "go ahead").
3. At certain steps the agent will **stop and wait** at a checkpoint (gate). At checkpoints, the agent ends its output with exactly one of these lines:
   - `⏳ GATE: Next: <thing>. Say "next" or what to change.`
   - `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`
   - `🏁 Complete. Let me know if anything needs adjustment.` (not a gate -- workflow finished)
4. Saying "next" (or similar) at a checkpoint counts as approval to proceed.
5. Some workflows support **"auto"** and **"auto to <milestone>"** to bypass planned gates. The work-spec skills intentionally do not: their reduced gate set is advanced by a supervisor, which may be a human or an authorized agent.

**Agent note-taking and progress tracking.** The agent keeps structured notes so you can pick up where you left off. Two marker conventions coexist:

- In **process artifacts** (markdown workflow documents — work specs, planning docs, retro outputs, ticket drafts, etc.): the agent uses `- [ ]` / `- [x]` markdown checkboxes with stable letter-led IDs (`D1`, `T1`, `F1`, `S1`, etc.) on each item. Completion is checking the box — the artifact keeps a record of every resolved item.
- In **source files** (test code, application code) written or planned by a skai workflow: the agent uses a **🟡** emoji on lines/functions/sections that are TODO. Completion is *removal* of the marker — the file's remaining work is read by which 🟡s remain. The canonical example is the unit test planning workflow, where section MARKs and test functions are seeded with 🟡 and the markers come off as tests are implemented and pass.
- Markers are cleared only when items are resolved and you give approval at the relevant gate.

> **Note on `🟡`:** This is the workflow-progress `🟡`, distinct from the [Integration document](#integration-document-how-to-use-it) `🟡` (which marks missing project-specific values needing human input). Both share the emoji; their lifecycles differ.

**Retros on demand.** At any point you can ask the agent to **"retro"** to check for gaps, update documents, backfill requirements, and reflect on process.

### Work spec design (skill `skai-work-spec-creation`)

Turn open-ended feature input into a technical design whose primary review surface is a complete diff of changed production APIs. The agent fills gaps with proposals, keeps the design and API Sketch current through discussion, and invokes UI Map Architecture or requirements backfill when their owned artifacts are needed. It does not write the implementation task list or code.

- Guide [`Guides/Spec/work-spec-creation.md`](Guides/Spec/work-spec-creation.md)

**Prerequisites:** Any useful input: a discussion, design, ticket, requirements, another specification, source code, or a combination.

**Phases:**

1. **Draft and discuss.** Agent writes the design and API Sketch from the available inputs, filling gaps with recommended `D<n>` proposals. The sketch remains current while the supervisor resolves material decisions. Gate: supervisor approves the resolved design direction and API.
2. **Complete design.** Agent writes the remaining implementation-relevant design, invokes required sibling workflows, and completes for handoff or transitions directly into Work Spec Implementation. Optional delivery slicing appears only when the scope outgrows one iteration.

### Work spec implementation (skill `skai-work-spec-implementation`)

Audit an approved work-spec design against the codebase, create its concrete task list, then implement and verify it continuously after one plan approval. Supports plan-only architect/developer handoff and same-agent design-to-build flow.

- Guide [`Guides/Spec/work-spec-implementation.md`](Guides/Spec/work-spec-implementation.md)

**Prerequisites:** A ready work-spec design and project build/test/runtime commands in [`skai/integration.md`](skai/integration.md).

**Phases:**

1. **Audit and plan.** Agent inspects the design, code, tests, and required sibling artifacts, then writes the whole implementation task list with observable completion and verification. Gate: supervisor approves the completed design and implementation plan.
2. **Implement continuously.** Agent executes all runnable owned tasks without per-task gates, records fresh evidence, invokes the Unit Testing and UI Map Implementation workflows when applicable, and blocks only on unresolved design, missing tooling, handoffs, or required human testing.

### UI Map architecture (skill `skai-ui-map-architecture`)

Create or change the app's UI Map as an architecture artifact. Produces a change package under `skai/changes/<change-id>/` containing the architecture artifact, `proposed-ui-map.yaml`, and `proposed-ui-map.svg`; the official map stays frozen during architecture.

- Guide [`Guides/UIMap/ui-map-architecture.md`](Guides/UIMap/ui-map-architecture.md)
- Example [`Guides/UIMap/ui-map-demo.md`](Guides/UIMap/ui-map-demo.md) -- a complete UI Map in YAML with its rendered diagram

**Prerequisites:** Product/design/story inputs for a baseline map or scoped map change. Existing maps live at `skai/ui-map/ui-map.yaml`; architecture change artifacts live under `skai/changes/<change-id>/`.

**Phases:**

1. **Discussion.** Agent digests the inputs, drafts topic-organized map decisions with inline `- [ ]` items (questions, proposals, tradeoffs), and maintains a provisional proposed map and render as soon as there is enough structure to review. The preview reflects the agent's current recommendations and is updated as decisions change. Gate: human resolves every discussion item.
2. **Map changes.** Agent diffs the frozen official map against the reviewed proposal, records the differences as typed map-change items, finalizes deferrals and assumptions/TODOs, and validates and renders the finished proposal. Ends with `🏁 Complete.` once the valid architecture package is in place.

### UI Map implementation (skill `skai-ui-map-implementation`)

Execute or specify the structural code work needed to conform to the target UI Map. The target is the proposed map when an architecture change package exists, or the official map for a no-package conformance run. The guide covers the audit, alignment discussion, checkbox-tracked code changes and their ownership dispositions, placeholder scaffolding, build verification, change requests back to architecture, and promotion of an approved proposed map.

- Guide [`Guides/UIMap/ui-map-implementation.md`](Guides/UIMap/ui-map-implementation.md)

**Prerequisites:** The app codebase and an identifiable target map: either a ready change package at `skai/changes/<change-id>/` (proposed map + render + architecture artifact) or the official `skai/ui-map/ui-map.yaml` for conformance work. Run mode (Plan vs Build) is inferred from context.

**Stages:**

1. **Audit.** Agent compares the codebase to the target map within the change's scope and separates UI-map-owned work, concrete handoffs, and map-level change requests.
2. **Discussion.** Agent resolves the non-mechanical decisions the audit raises. Gate: discussion complete.
3. **Code Changes.** Agent writes typed, unchecked items with stable IDs and a Disposition (`implement` / `placeholder` / `planned` / `handoff`), ending with a terminal promote item when a proposed map exists. The checkbox records completion; Disposition records ownership. Gate: Code Changes ready.
4. **Implement.** In Build, the agent executes owned items, verifies a fresh green build, and blocks before completion or promotion while any handoff remains unchecked. In Plan, owned code work remains unchecked as `planned`; the reviewed specification is the deliverable. When a proposed map exists, Plan promotes it after specification approval, while Build promotes it only after code conformance is green. Click-through QA is downstream, not a gate.

### Requirements authoring (skill `skai-requirements-authoring`)

Draft behavioral requirements into a change package under `skai/changes/<change-id>/`, resolve the questions they raise, and leave the package ready to promote. The canonical local catalog defaults to `skai/requirements/**` and stays frozen during authoring; the Integration block may name another local or shared root. Sources are open-ended -- designs, an existing implementation, a product brief, a planning document, or a change request -- and the mode (baseline vs. scoped change) is inferred from the catalog rather than declared.

- Guide [`Guides/Requirements/requirements-authoring.md`](Guides/Requirements/requirements-authoring.md)
- Content rules [`Guides/Requirements/requirements-catalog.md`](Guides/Requirements/requirements-catalog.md) -- scopes, layout, requirement format, IDs, writing style
- Formats [`Guides/Requirements/requirements-artifacts.md`](Guides/Requirements/requirements-artifacts.md) -- requirement change items and change requests

**Prerequisites:** Sources describing the behavior to capture. An existing catalog at the Integration block's root, or the intent to start one.

**Phases:**

1. **Discussion.** Agent digests the inputs, infers the mode, drafts the requirement files, and seeds topic-organized `- [ ]` items for the decisions it cannot settle -- two sources disagreeing, behavior that looks like a defect rather than intent, an undefined boundary. Requirements are drafted under the agent's recommended reading and cite their open item, so the drafts always read as a complete catalog. Gate: human resolves each item.
2. **Requirement changes.** Agent writes typed change items describing exactly the difference between the frozen catalog and the drafts, each naming its source. Ends with `🏁 Complete.` once the package is ready to promote.

### Requirements promotion (skill `skai-requirements-promotion`)

Write an approved change package into the canonical catalog. Promotion is the only writer of the Integration block's requirements root (normally `skai/requirements/**` for a local catalog), and it is a transformation rather than a copy: drafting scaffolding is stripped, IDs are checked against what the catalog already holds, and the writing-style rules get their last enforcement on the exact text about to become permanent. A package recording behavior that already ships promotes on approval; one recording behavior still to come promotes when the change ships.

- Guide [`Guides/Requirements/requirements-promotion.md`](Guides/Requirements/requirements-promotion.md)

**Prerequisites:** A change package at `skai/changes/<change-id>/` whose discussion is fully resolved and whose requirement change items match its drafts.

**Phases:**

1. **Promotion checks.** Agent screens the package for readiness, then writes an unchecked checklist covering ID stability, prefix collisions, cross-reference resolution, writing style, catalog traversability, and scaffolding removal, ending with the terminal write. Gate: human reviews what will become canon.
2. **Execute.** Agent runs each check in order, records evidence, and writes the catalog. A failing check blocks and returns the package to authoring -- promotion never rewrites a requirement's prose. When the catalog itself is the problem, the agent raises a change request instead.

### Unit testing (skill `skai-unit-testing`)

Plan-first testing workflow. The agent creates an orchestration document for the overall testing session, plans all tests upfront, runs one infrastructure pass across all planned tests, and then implements tests one logical section at a time (e.g. "Success Tests", "Error Handling Tests"). Handles new test suites, additions to existing suites, and fixing failing tests.

- Guides [`Guides/Test/unit-testing-guide.md`](Guides/Test/unit-testing-guide.md), [`Guides/Test/unit-test-planning-guide.md`](Guides/Test/unit-test-planning-guide.md), [`Guides/Test/unit-test-infrastructure-guide.md`](Guides/Test/unit-test-infrastructure-guide.md), [`Guides/Test/unit-test-writing-guide.md`](Guides/Test/unit-test-writing-guide.md)

**Prerequisites:** Source code to test. Often triggered by a work spec task, but can be used independently.

**Phases:**

1. **Planning.** Agent chooses a session name for the current testing effort and creates `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md` (following [`Guides/Core/working-doc-conventions.md`](Guides/Core/working-doc-conventions.md)) with a `- [ ] Planning` / `- [ ] Infrastructure` / `- [ ] Writing` checklist, and creates test files organized into sections with test stubs in each. Test files use `🟡` on section MARKs and `@Test` functions (in-code progress markers). Doc comments on every stub serve as the test plan. At the planning gate, `Planning` remains unchecked until the human approves advancing to infrastructure.
2. **Infrastructure.** Agent identifies required test infrastructure across all planned tests in the testing session (stubs, fixtures, production code abstractions) and proposes additions. The orchestration document keeps `Infrastructure` unchecked until the human approves advancing to writing. Related infrastructure docs and artifacts live under the same `skai/working-docs/<branch-path>/<session-name>/...` session folder.
3. **Writing** (per section, file-by-file). Agent implements tests and then runs them section-by-section, finishing the current file before moving to the next. Gates: agent stops after writing (before running tests), and stops after test results to confirm conclusions and next steps (including any proposed production-code fixes). As tests pass and the human approves, the agent removes `🟡` from those test functions and section MARKs in the test files. The orchestration document keeps `Writing` unchecked until all sections in the testing session are approved complete. If a test requires infrastructure that wasn't identified in Phase 2, it is skipped, the missing infrastructure is documented, and the human can decide at the next planned gate whether to re-enter the infrastructure phase or defer that skipped work.

Phase 3 repeats for each section until none remain.

### Debugging (skill `skai-debugging`)

Evidence-first problem resolution. Prevents "guessing fixes" loops by requiring observable evidence before drawing conclusions. The process defines a toolkit of effective strategies (targeted logging, possibility-space partitioning, minimal reproducers, bisection, invariant assertions) that guide the agent's debugging approach.

- Guides [`Guides/Core/debugging-guide.md`](Guides/Core/debugging-guide.md), [`Policies/debugging-process-rule.md`](Policies/debugging-process-rule.md)

**Prerequisites:** A bug, crash, or unexpected behavior to investigate. Provide whatever evidence you have (error messages, logs, screenshots, steps to reproduce).

**Phases (repeating):**

1. **Hypothesize and experiment.** Agent states the current possibility space, chooses a tactic, and proposes the smallest discriminating experiment. Gates: pre-experiment and post-experiment during iteration, then hard gates for root cause, fix, and verify/close.

Repeats until the root cause is isolated.

### Dev retro (skill `skai-dev-retro`)

Completeness backstop that can be used at any point during any workflow. Reviews what has transpired since the last retro (or since session start), identifies gaps, reconciles plan drift, updates documentation, captures behavior the requirements catalog does not yet reflect, and reflects on process.

- Guide [`Guides/Process/dev-retro.md`](Guides/Process/dev-retro.md)

**Prerequisites:** Work to review. The agent reads work specs, planning docs, evidence artifacts, the requirements catalog, and any open requirements change package.

**Phases:**

1. **Retro.** Agent performs the full checklist, reports findings, and completes immediately if neither a requirements finding nor a process suggestion was generated.
2. **Requirements follow-up (optional).** If the session revealed behavior the catalog does not reflect, the agent seeds a change package -- draft requirements plus `- [ ] D<n>` items for what it could not settle -- and stops at a handoff gate. It never writes the catalog itself. On `next`, the agent enters [`Guides/Requirements/requirements-authoring.md`](Guides/Requirements/requirements-authoring.md), which owns resolving the items and, in turn, promotion.
3. **Process improvement follow-up (optional).** If the retro identifies process improvements, agent lists them in the retro output as `- [ ] S<n>` items and stops at a handoff gate. On `next`, the agent enters [`Guides/Process/ticket-filing.md`](Guides/Process/ticket-filing.md), which drafts `process-tickets.md`, lets the human review/edit the resulting `- [ ] T<n> Ticket: ...` entries, and files the remaining ones on `next`.

### Process refinement (skill `skai-process-refinement`)

Hardens a process guide against a cold review. A fresh, no-context session reads the guide set and attacks it; the refining session triages the findings, repairs one cluster at a time, scores the round, and decides whether to run another.

- Guide [`Guides/Process/process-refinement-guide.md`](Guides/Process/process-refinement-guide.md)
- Template [`Guides/Process/cold-review-prompt-template.md`](Guides/Process/cold-review-prompt-template.md)

**Prerequisites:** The guide document(s) to refine, and a design spec to judge them against. Without a spec, close that gap first -- the spec is the standard every finding is weighed against.

**Phases:**

1. **Commission the review.** Fill the template's slots and hand the filled prompt to a fresh session. The reviewer must not see the refinement guide or the template itself -- both are refiner-facing and would bias it.
2. **Triage.** Classify every finding `accept` / `log only` / `reject` / `human decision` against the codification bar, consulting the target's findings log so settled ground is not relitigated. Collapse findings that name one defect into a single row.
3. **Score the round.** Before the first repair, record the round's score, defect counts, and noise count in the working document.
4. **Repair.** One cluster at a time, with a written self-check after each, then verify the repairs before handing the guide back.
5. **Stop or iterate.** Terminal is a fresh round over the current text with no new live findings, or the human approving the unimplemented ledger. Close the pass and append every disposition to the findings log.

### Suggestion (skill `skai-suggestion`)

The suggestion box for skai itself. A developer has an idea, request, or complaint about the skai dev process; the agent helps articulate it, captures it as a ticket draft, and optionally files it as a GitHub issue on the skai repo. It does not change any guide's content — that is [Process refinement](#process-refinement-skill-skai-process-refinement).

- Guide [`Guides/Process/ticket-filing.md`](Guides/Process/ticket-filing.md)

**Prerequisites:** None -- can be triggered at any point during a session.

**Phases:**

1. **Understand and draft.** Agent asks clarifying questions to understand the suggestion (skipped if the developer provides enough detail up front). Once it has enough context, it stops at a ready-to-draft gate. On `next`, it chooses a session name, writes one or more `- [ ] T<n> Ticket: ...` drafts (with bold sub-bullet body fields) to `skai/working-docs/<branch-path>/<session-name>/process-tickets.md`, and presents them for review.
2. **Review and file (optional).** The draft-review gate is the main filing gate: the human can revise drafts or move them to a `## Skipped` subsection, or say `next` to file the remaining unchecked `- [ ] T<n> Ticket: ...` entries as GitHub issues on `skai`. On filing, the entry is checked (`- [x]`) and a `- **Filed** #<n>` sub-bullet is appended.

### Update installation (skill `skai-update-installation`)

Update `skai` to the latest release (or a target you name), review what changed, and re-run adapter runbooks.

- Guide [`Guides/Core/update-installation-guide.md`](Guides/Core/update-installation-guide.md)

**Prerequisites:** An existing installation ([`skai/install-state.json`](skai/install-state.json) must exist from the initial install).

**Phases:**

1. **Pick target, update, and report.** Agent updates the submodule to the latest release (`v<N>` tag) by default — or to a target you name (head of current branch, head of main, or a specific commit) — and presents the `## Release <N>` notes between your installed and target releases. Gate: human acknowledges before any runbooks are re-run.
2. **Re-run adapters.** Agent re-runs each installed adapter's install/update runbook to pick up new or changed assets.

### Working documents

- Working documents (plans, specs, progress logs) live under [`skai/working-docs/`](skai/working-docs/) in the target-owning repository and are organized by that repository's current git branch.
- `<branch-path>` is the current branch name, with `/` decomposed into nested folders (so `feature/foo` becomes `feature/foo/`).
- Working docs are ephemeral and typically git-ignored.
- One exception: the refinement **findings log** at [`refinement-reviews/`](refinement-reviews/) in the target repository is committed, one file per refined target. It carries what earlier refinement passes decided, so a later pass does not re-argue settled ground.

## Development guide (for contributors)

This repo is typically maintained with an LLM. When you ask an LLM to make changes, point it at:
- [`README.md`](README.md) (this file)
- [`maintain-skai.md`](maintain-skai.md) (LLM maintainer runbook)
- [`maintain-retro.md`](maintain-retro.md) (post-change checklist to ensure nothing was forgotten)
- [`maintain-tickets.md`](maintain-tickets.md) (work through process improvement tickets labeled `agent ready`)

### LLM-assisted change workflow (recommended)

- Ask the LLM to:
  - propose a small plan,
  - make the minimal edits,
  - then report exactly which files changed and why.
- Require safety defaults (unless you explicitly override):
  - no commits
  - no deletions
  - no dependency changes

### Contributor rules

- Keep sources in this repo **IDE-neutral** (`.md`). IDE-specific outputs are generated into host repos by install/update runbooks.
- If you add/move/rename an asset, update:
  - [`assets.manifest.json`](assets.manifest.json)
  - [`README.md`](README.md) Usage section (developer-facing guides should be documented at file level)
- Update [`CHANGELOG.md`](CHANGELOG.md) for user-visible changes.
- Do not introduce scripts that mutate host repos; installers are LLM-runbook-driven and must follow the safety policies in [`Policies/`](Policies/).
