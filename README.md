<picture>
  <source media="(prefers-color-scheme: dark)" srcset="internal/branding/skai-logo-dark.svg">
  <img src="internal/branding/skai-logo.svg" alt="SKAI" width="420">
</picture>

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
- [Project guide addenda](#project-guide-addenda)
  - [Shared context and platform overrides](#shared-context-and-platform-overrides)
- [IDE clutter / autocomplete](#ide-clutter--autocomplete-recommended)
- [Usage](#usage)
  - [How all workflows work](#how-all-workflows-work)
  - [Work spec design](#work-spec-design-skill-skai-work-spec-creation)
  - [Work spec implementation](#work-spec-implementation-skill-skai-work-spec-implementation)
  - [UI Map architecture](#ui-map-architecture-skill-skai-ui-map-architecture)
  - [UI Map implementation](#ui-map-implementation-skill-skai-ui-map-implementation)
  - [Product specs authoring](#product-specs-authoring-skill-skai-product-specs-authoring)
  - [Product specs promotion](#product-specs-promotion-skill-skai-product-specs-promotion)
  - [Design authoring](#design-authoring-skill-skai-design-authoring)
  - [Design promotion](#design-promotion-skill-skai-design-promotion)
  - [Design specs authoring](#design-specs-authoring-skill-skai-design-specs-authoring)
  - [Design specs promotion](#design-specs-promotion-skill-skai-design-specs-promotion)
  - [Unit testing](#unit-testing-skill-skai-unit-testing)
  - [Debugging](#debugging-skill-skai-debugging)
  - [Dev retro](#dev-retro-skill-skai-dev-retro)
  - [Suggestion](#suggestion-skill-skai-suggestion)
  - [Configure SKAI](#configure-skai-skill-skai-configure)
  - [Update installation](#update-installation-skill-skai-update-installation)
  - [Working documents](#working-documents)
  - [Figma designs](#figma-designs)
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

Paste this into your agent chat, from the host repo root. The agent asks which adapters (Claude
Code, Cursor, Codex) to install before writing anything.

> Install/update `skai` in this repo by following `Submodules/skai/Install/install-update.md` ([`Install/install-update.md`](Install/install-update.md)).

The adapter runbooks work with any IDE (JetBrains, Xcode, Android Studio, VS Code, etc.) or standalone agent environment. Stack-aware runbooks auto-detect the project stack and apply the appropriate guidance.

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
- **Managed blocks**: project-owned files (ignore files, agent instruction files) are updated only inside a delimited block, so a project's own content around it survives updates.
- **Instruction files**: Claude Code uses [`CLAUDE.md`](CLAUDE.md); Codex uses root [`AGENTS.md`](AGENTS.md). Their dated managed blocks share [composition guidance](Install/agent-instructions-install-update.md) and inline applicable policies; your own instructions stay outside the block.
- **Shared artifacts**: product spec, design-spec and UI Map change packages live in the repo holding their canonical artifact, including a shared submodule. The project README links each canonical artifact; agents resolve the repo from that link.
- **Change packages**: related work shares a change ID, with independent active folders `skai/changes/<change-id>/product-specs/` and `skai/changes/<change-id>/ui-map/`. Promotion moves only the selected type to `skai/promoted/<change-id>/<type>/` and repairs affected links; sibling types can promote in either order. The promoted UI Map artifact may retain unchecked Plan work for downstream implementation.
- **Legacy installs**: lookalike files without the header are treated as **legacy candidates** and are not overwritten by default (see [`Install/conflict-precedence-policy.md`](Install/conflict-precedence-policy.md)).

## Integration document (how to use it)

The Integration doc ([`skai/integration.md`](skai/integration.md)) is the **project-owned** place where `skai` workflows get the concrete, copy/pasteable details they need to run deterministically (build/test commands, destinations, artifact paths, evidence expectations).

Why it matters:
- It prevents agents from guessing project-specific constants (like `xcodebuild -destination` strings, scheme/test plan conventions, or where `.xcresult` / logs are stored).
- It makes install/update migrations safe: the installer can preserve your filled values while updating the managed template structure around them.

How the project owner fills it:
- **🟡 means "required project-specific value is missing."**
- Under a 🟡 item you may see one or more `INSTRUCTION:` lines. Those are **not part of the long-term document**; they exist only to explain what to fill in.
- When you fill a value:
  - remove the 🟡 marker
  - delete the `INSTRUCTION:` line(s) under it
- If a future install/update can't infer a required value with high confidence, the installer may **restore** 🟡 + `INSTRUCTION:` prompts so the doc remains a complete, reliable source of truth.

> **Note on `🟡`:** The Integration doc's `🟡` (missing project-specific value) is a separate concept from the workflow-progress `🟡` used in source files by skai workflows (see [Agent note-taking and progress tracking](#how-all-workflows-work) below). Both share the emoji; their lifecycles differ.

## Project guide addenda

Customize a guide with a project-owned, freeform Markdown file at
`skai/addenda/<guide-name>-addendum.md`. Each guide's final **Project Addendum** section gives its
exact filename. The agent prints the guide line on opening the guide, reads it fully, then reads the
addendum if it exists and prints an indented line the moment it has:

```text
📖 SKAI guide: product-specs-promotion
  - 📎 Addendum loaded
```

A guide line on its own means the project has no addendum for that guide. The addendum's rules
are part of the guide and win any conflict with it. These lines are not an approval gate.

Addenda may add rules or override guide defaults. Current task instructions and project-wide policies
retain authority. No required template, headings, frontmatter, schema or managed header applies;
SKAI updates preserve these files. Integration remains global operational settings, loaded by the
base guide when needed. Addendum authors need not repeat that dependency.

For example, `skai/addenda/product-specs-promotion-addendum.md` could contain:

```markdown
Include a short evidence summary naming the requirement files checked.
For this guide, replace the default completion sentence with:
“Product specs are promoted and archived.”
```

### Shared context and platform overrides

For iOS and Android projects sharing product specs, a UI Map or common conventions, keep the common
addendum in the shared repository. Each platform's conventional addendum points to it and can add
local rules. The conventional project file is the discovery entry point; the referenced content
may live elsewhere. A task performed directly in the shared repository uses that repository as its
active project.

Copy this optional boilerplate into the platform project's
`skai/addenda/product-specs-promotion-addendum.md`, adjusting the shared path:

```markdown
First read and apply the [shared addendum](../../Submodules/shared-context/skai/addenda/product-specs-promotion-addendum.md).

Then apply these project-specific additions and overrides:
- Include the iOS verification results in the evidence summary.
```

This example assumes the shared repository is checked out at `Submodules/shared-context/` under the
platform project. Relative links resolve from the file containing them, so `../../` leads from
`skai/addenda/` back to the project root. Use the actual checkout path for a sibling repository or
another layout.

- **Shared only:** the project addendum just instructs reading the shared file.
- **Local only:** it contains the project's rules directly.
- **Both:** read shared rules first, then apply local additions or overrides. Put explicit local
  replacements in the project file so the intended precedence is clear.

Required shared references must be read before proceeding; missing or unreadable references stop
rather than count as an absent project addendum. These references do not produce additional
addendum lines. Neither Integration nor README needs an inventory of addendum files.

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

- In **process artifacts** (markdown workflow documents — work specs, planning docs, retro outputs, ticket drafts, etc.): the agent uses `- [ ]` / `- [x]` markdown checkboxes with stable letter-led IDs (`D01`, `T01`, `F01`, `S01`, etc.) on each item. Completion is checking the box — the artifact keeps a record of every resolved item.
- In **source files** (test code, application code) written or planned by a skai workflow: the agent uses a **🟡** emoji on lines/functions/sections that are TODO. Completion is *removal* of the marker — the file's remaining work is read by which 🟡s remain. The canonical example is the unit test planning workflow, where section MARKs and test functions are seeded with 🟡 and the markers come off as tests are implemented and pass.
- Markers are cleared only when items are resolved and you give approval at the relevant gate.

> **Note on `🟡`:** This is the workflow-progress `🟡`, distinct from the [Integration document](#integration-document-how-to-use-it) `🟡` (which marks missing project-specific values needing supervisor input). Both share the emoji; their lifecycles differ.

**Project customization.** [Project guide addenda](#project-guide-addenda) add or override a guide's rules, including shared instructions and platform-local overrides.

**Retros on demand.** At any point you can ask the agent to **"retro"** to check for gaps, update documents, backfill requirements, and reflect on process.

### Work spec design (skill `skai-work-spec-creation`)

Turn open-ended feature input into a technical design whose primary review surface is a complete diff of changed production APIs. The agent fills gaps with proposals, keeps the design and API Sketch current through discussion, and invokes UI Map architecture or product specs authoring when their owned artifacts are needed. It does not write the implementation task list or code.

- Guide [`Guides/Spec/work-spec-creation.md`](Guides/Spec/work-spec-creation.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when an input carries a gap, or an item cannot be resolved because something outside the work is not yet known

**Prerequisites:** Any useful input: a discussion, design, ticket, requirements, another specification, source code, or a combination.

**Phases:**

1. **Draft and discuss.** Agent writes the design and API Sketch from the available inputs, filling gaps with recommended `D<n>` proposals. The sketch remains current while the supervisor resolves material decisions. Gate: supervisor approves the resolved design direction and API.
2. **Complete design.** Agent writes the remaining implementation-relevant design, invokes required sibling workflows, and completes for handoff or transitions directly into Work Spec Implementation. Optional delivery slicing appears only when the scope outgrows one iteration.

### Work spec implementation (skill `skai-work-spec-implementation`)

Audit an approved work-spec design against the codebase, create its concrete task list, then implement and verify it continuously after one plan approval. Supports plan-only architect/developer handoff and same-agent design-to-build flow.

- Guide [`Guides/Spec/work-spec-implementation.md`](Guides/Spec/work-spec-implementation.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when an input carries a gap, or an item cannot be resolved because something outside the work is not yet known

**Prerequisites:** A ready work-spec design and project build/test/runtime commands in [`skai/integration.md`](skai/integration.md).

**Phases:**

1. **Audit and plan.** Agent inspects the design, code, tests, and required sibling artifacts, then writes the whole implementation task list with observable completion and verification. Gate: supervisor approves the completed design and implementation plan.
2. **Implement continuously.** Agent executes owned tasks, records fresh evidence, and updates known-difference notes for verified fixes. It invokes Unit Testing and UI Map Implementation when applicable and blocks on unresolved design, missing tooling, handoffs, or required manual testing.

### UI Map architecture (skill `skai-ui-map-architecture`)

Create or change the app's UI Map as an architecture artifact. Produces a change package under `skai/changes/<change-id>/ui-map/` containing the architecture artifact, `proposed-ui-map.yaml`, and `proposed-ui-map.html`; the official map stays frozen during architecture.

- Guide [`Guides/UIMap/ui-map-architecture.md`](Guides/UIMap/ui-map-architecture.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when an input carries a gap, or an item cannot be resolved because something outside the work is not yet known
- Hosting [`Guides/Core/artifact-hosting.md`](Guides/Core/artifact-hosting.md) — read when the artifact does not exist yet: which repository it goes in, and the README link
- Example [`Guides/UIMap/ui-map-demo.md`](Guides/UIMap/ui-map-demo.md) -- a complete UI Map in YAML with its rendered diagram

**Prerequisites:** Product/design/story inputs for a baseline map or scoped map change. Existing maps live at `skai/ui-map/ui-map.yaml`; architecture change artifacts live under `skai/changes/<change-id>/ui-map/`.

**Phases:**

1. **Discussion.** Agent digests the inputs, drafts topic-organized map decisions with inline `- [ ]` items (questions, proposals, tradeoffs), and maintains a provisional proposed map and render as soon as there is enough structure to review. The preview reflects the agent's current recommendations and is updated as decisions change. Gate: supervisor resolves every discussion item.
2. **Map changes.** Agent diffs the frozen official map against the reviewed proposal, records the differences as typed map-change items, finalizes deferrals and assumptions/TODOs, and validates and renders the finished proposal. Ends with `🏁 Complete.` once the valid architecture package is in place.

### UI Map implementation (skill `skai-ui-map-implementation`)

Execute or specify the structural code work needed to conform to the target UI Map. The target is the proposed map when an architecture change package exists, or the official map for a no-package conformance run. The guide covers the audit, alignment discussion, checkbox-tracked code changes and their ownership dispositions, placeholder scaffolding, build verification, change requests back to architecture, and promotion of an approved proposed map.

- Guide [`Guides/UIMap/ui-map-implementation.md`](Guides/UIMap/ui-map-implementation.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when an input carries a gap, or an item cannot be resolved because something outside the work is not yet known

**Prerequisites:** The app codebase and an identifiable target map: either a ready change package at `skai/changes/<change-id>/ui-map/` (proposed map + render + architecture artifact) or the official `skai/ui-map/ui-map.yaml` for conformance work. Run mode (Plan vs Build) is inferred from context.

**Stages:**

1. **Audit.** Agent compares the codebase to the target map within the change's scope and separates UI-map-owned work, concrete handoffs, and map-level change requests.
2. **Discussion.** Agent resolves the non-mechanical decisions the audit raises. Gate: discussion complete.
3. **Code Changes.** Agent writes typed, unchecked items with stable IDs and a Disposition (`implement` / `placeholder` / `planned` / `handoff`), ending with a terminal promote item when a proposed map exists. The checkbox records completion; Disposition records ownership. Gate: Code Changes ready.
4. **Implement.** In Build, the agent executes owned items, verifies a fresh green build, and blocks before completion or promotion while any handoff remains unchecked. In Plan, owned code work remains unchecked as `planned`; the reviewed specification is the deliverable. When a proposed map exists, Plan promotes it after specification approval, while Build promotes it only after code conformance is green. After successful map promotion, the agent archives the UI Map type folder and repairs links and its preview. Pending Plan work continues at the promoted path. A conformance run without a proposed map uses a working-doc session. Click-through QA is downstream, not a gate.

### Product specs authoring (skill `skai-product-specs-authoring`)

Draft requirements into a change package under `skai/changes/<change-id>/product-specs/` against the product specs, resolve the questions they raise, and leave the package ready to promote. The canonical catalog stays unchanged during authoring; the rendered review page in the package is how the supervisor reads it. Sources are open-ended -- designs, an existing implementation, a product brief, a planning document, or a change request -- and the mode (baseline vs. scoped change) is inferred from the catalog rather than declared.

- Guide [`Guides/ProductSpecs/product-specs-authoring.md`](Guides/ProductSpecs/product-specs-authoring.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when an input carries a gap, or an item cannot be resolved because something outside the work is not yet known
- Baseline [`Guides/ProductSpecs/product-specs-baseline.md`](Guides/ProductSpecs/product-specs-baseline.md) — read when authoring infers Baseline mode
- Hosting [`Guides/Core/artifact-hosting.md`](Guides/Core/artifact-hosting.md) — read when the artifact does not exist yet: which repository it goes in, and the README link
- Content rules [`Guides/ProductSpecs/product-specs-catalog.md`](Guides/ProductSpecs/product-specs-catalog.md) -- scopes, layout, indexes and glossary, IDs, writing style
- Shape [`Guides/Core/spec-file-shape.md`](Guides/Core/spec-file-shape.md) — the file shape product specs and design specs share, and the `Bin/spec-tool.py` commands that validate, cross-reference and render it (cited by the content, authoring and promotion guides)
- Formats [`Guides/ProductSpecs/product-specs-artifacts.md`](Guides/ProductSpecs/product-specs-artifacts.md) -- the package and its rendered review page, requirement change items, change requests

**Prerequisites:** Sources describing the behavior to capture. An existing catalog, linked from the project README, or the intent to start one.

**Phases:**

1. **Discussion.** Agent digests the inputs, infers the mode, inventories the concepts the change touches (new or changed concepts are confirmed by the supervisor before app behavior is drafted on them), drafts the requirement files, and seeds topic-organized `- [ ]` items for the decisions it cannot settle -- two sources disagreeing, behavior that looks like a defect rather than intent, an undefined boundary. Requirements are drafted under the agent's recommended reading; Discussion items link to affected drafts, keeping the catalog complete and decisions discoverable. The typed change list is kept current as the drafts change, and the package is validated and re-rendered on every material change; change requests filed by downstream consumers are triaged on the request. Before the gate the agent runs the tool's validation, promotion's `C1`–`C5` and `check-changes`, recording evidence. Gate: supervisor resolves each item.
2. **Completion.** Agent brings assumptions and out-of-scope current, renders once more, and ends with `🏁 Complete.` once the package is ready to promote.

### Product specs promotion (skill `skai-product-specs-promotion`)

Write an approved change package into the canonical catalog, checking IDs and content and preparing
links for their canonical destinations. Shipping behavior and approved contracts with confirmed
known-difference notes may promote on approval; other future behavior waits until shipment.
Work-spec implementation may later update or remove those notes after verifying a fix, while
requirement text and IDs remain unchanged.

- Guide [`Guides/ProductSpecs/product-specs-promotion.md`](Guides/ProductSpecs/product-specs-promotion.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when readiness finds an open gap; the package returns to authoring to resolve it

**Prerequisites:** A change package at `skai/changes/<change-id>/product-specs/` whose discussion is fully resolved and whose requirement change items match its drafts.

**Phases:**

1. **Promotion checks.** Agent screens the package for readiness, then writes an unchecked checklist covering ID stability, prefix collisions, cross-reference resolution, writing style, catalog traversability, and destination link preparation, followed by the canonical write (C7) and package archival (C8). Gate: supervisor reviews what will become canon.
2. **Execute.** Agent runs each check in order, records evidence, writes the catalog, then moves the product specs package to its promoted path and repairs references. An archival failure resumes only that step; the canonical write is not repeated. A failing verifying check blocks and returns the package to authoring -- promotion never rewrites a requirement's prose. When the catalog itself is the problem, the agent raises a change request instead.

### Design authoring (skill `skai-design-authoring`)

Take a design change from an idea to approved mockups in a change package under `skai/changes/<change-id>/design/`, drafted on a change page named `<change-id>` in the project's design file. The production designs stay unchanged during authoring. Sources are open-ended -- an idea, sketches, a brief, a product spec package, an existing app to backfill from. The process guide is tool-agnostic and loads the conventions guide for the project's design tool (Figma today).

- Guide [`Guides/Design/design-authoring.md`](Guides/Design/design-authoring.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when an input carries a gap, or an item cannot be resolved because something outside the work is not yet known
- Tool guide, loaded by the process guide: [`Guides/Design/figma-designer-guide.md`](Guides/Design/figma-designer-guide.md) for Figma (and [`figma-designer-guide-multiple-sizes.md`](Guides/Design/figma-designer-guide-multiple-sizes.md) for several target sizes)

**Prerequisites:** The project README links the Figma file. Something to design from.

**Phases** (alternating; never both at once):

1. **Discussion.** Agent seeds topic-organized `- [ ]` items for the decisions it needs -- a proposed departure from the current app, something that looks like a defect, an open product question -- each with a written recommendation. Nothing is drawn. A decision that changes or adds a product spec is filed as a change request against the change's product spec package, never by editing it. Gate: supervisor resolves each item.
2. **Mockups.** Agent draws the resolved items on the change page and, before the review gate, traces every drawn state to a product spec and every package spec to a drawing, filing change requests for the gaps; supervisor reviews the designs there. Feedback goes into the designs; anything needing a decision is parked and opens the next Discussion phase. Gate: supervisor says "approved", after which the agent writes the Design Changes inventory. Ends with `🏁 Complete.`, naming any request still awaiting triage.

### Design promotion (skill `skai-design-promotion`)

Move an approved package's drafts from its change page into the production designs, have the supervisor confirm the result, delete the page, and archive the package to `skai/promoted/<change-id>/design/`. Promotion refactors production to absorb the drafts; a draft that needs changing returns the package to authoring. Implementing designs in code is out of scope.

- Guide [`Guides/Design/design-promotion.md`](Guides/Design/design-promotion.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when readiness finds an open gap; the package returns to authoring to resolve it

**Prerequisites:** A change package whose discussion is resolved, whose Design Changes inventory is written, and whose change requests against the product spec package are triaged.

**Phases:**

1. **Promotion checks.** Agent screens the package for readiness, then writes an unchecked checklist: drafts meet the conventions, inventory matches the page, production absorbs the page, links repoint, page deleted. Gate: supervisor reviews what will land.
2. **Execute.** Agent verifies and applies, then stops for the supervisor to review production in the design file. Gate: supervisor confirms; the change page is deleted and the package archived.

### Design specs authoring (skill `skai-design-specs-authoring`)

Draft design specs -- the rules joining a screen's design to the requirements: which drawn state shows under which condition, how data is formatted, what each control does, where the screen leads -- into a change package under `skai/changes/<change-id>/design-specs/`, resolve the questions they raise, and leave the package ready to promote. The canonical specs stay unchanged during authoring; the rendered review page in the package is how the supervisor reads it. An existing open package can be audited against the guides, the checks running over every draft before any edit. Sources are open-ended -- a story, a requirements or design change, designer notes, an existing app to backfill from -- and the mode (baseline vs. scoped change) is inferred from the specs rather than declared. Specs speak product language only: no frame, component or node names, no appearance words, no platform names outside a known-difference note.

- Guide [`Guides/DesignSpecs/design-specs-authoring.md`](Guides/DesignSpecs/design-specs-authoring.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when an input carries a gap, or an item cannot be resolved because something outside the work is not yet known
- Shape [`Guides/Core/spec-file-shape.md`](Guides/Core/spec-file-shape.md) — the file shape product specs and design specs share, and the `Bin/spec-tool.py` commands that validate, cross-reference and render it (cited by the content, authoring and promotion guides)
- Hosting [`Guides/Core/artifact-hosting.md`](Guides/Core/artifact-hosting.md) — read when the artifact does not exist yet: which repository it goes in, and the README link
- Content rules [`Guides/DesignSpecs/design-specs.md`](Guides/DesignSpecs/design-specs.md) -- layout, items, IDs, writing style, the ten verification checks
- Formats [`Guides/DesignSpecs/design-specs-artifacts.md`](Guides/DesignSpecs/design-specs-artifacts.md) -- the package and its rendered review page, spec change items, change requests

**Prerequisites:** The project README links the design file. The requirements the specs will cite.

**Phases:**

1. **Discussion.** Agent reads the drawings, the requirements and (in a backfill) the app, drafts the spec files screen by screen, and seeds topic-organized `- [ ]` items for what needs the supervisor -- a difference between the design and the app, a state the design does not draw, a product question. Specs are drafted under the recommended reading; an item whose answer is a drawing stays open until the drawing exists. A requirements gap is filed as a change request against the change's product spec package (or the catalog) rather than specified quietly, and stays open until triaged. The typed change list is kept current as the drafts change, and the package is validated and re-rendered on every material change; change requests received are triaged on the request. Before the gate the agent runs the tool's validation, the ten verification checks and `check-changes`, recording evidence. Gate: supervisor resolves each item.
2. **Completion.** Agent brings assumptions and out-of-scope current, renders once more, and ends with `🏁 Complete.` once the package is ready to promote.

### Design specs promotion (skill `skai-design-specs-promotion`)

Write an approved design-spec package into the canonical specs and archive it to `skai/promoted/<change-id>/design-specs/`. Promotion verifies; it never rewrites a spec's prose. A spec promotes on the supervisor's approval, whatever the state of the implementation.

- Guide [`Guides/DesignSpecs/design-specs-promotion.md`](Guides/DesignSpecs/design-specs-promotion.md)
- Gaps [`Guides/Core/known-gaps.md`](Guides/Core/known-gaps.md) — read when readiness finds an open gap; the package returns to authoring to resolve it

**Prerequisites:** A package whose Discussion is resolved and whose Spec Changes are written, citing only canonical requirements.

**Phases:**

1. **Promotion checks.** Agent screens the package for readiness, then writes an unchecked checklist: the ten verification checks, destination link preparation, the write, archival. Gate: supervisor reviews what will become canon.
2. **Execute.** Agent runs the checks with evidence, writes the specs, moves the package to its promoted path and repairs references. A failing check returns the package to authoring; when the existing specs are the problem, the agent raises a change request instead.

### Unit testing (skill `skai-unit-testing`)

Plan-first testing workflow. The agent creates an orchestration document for the overall testing session, plans all tests upfront, runs one infrastructure pass across all planned tests, and then implements tests one logical section at a time (e.g. "Success Tests", "Error Handling Tests"). Handles new test suites, additions to existing suites, and fixing failing tests.

- Guides [`Guides/Test/unit-testing-guide.md`](Guides/Test/unit-testing-guide.md), [`Guides/Test/unit-test-planning-guide.md`](Guides/Test/unit-test-planning-guide.md), [`Guides/Test/unit-test-infrastructure-guide.md`](Guides/Test/unit-test-infrastructure-guide.md), [`Guides/Test/unit-test-writing-guide.md`](Guides/Test/unit-test-writing-guide.md)

**Prerequisites:** Source code to test. Often triggered by a work spec task, but can be used independently.

**Phases:**

1. **Planning.** Agent chooses a session name for the current testing effort and creates `skai/working-docs/<branch-path>/<session-name>/testing/unit-testing.md` (following [`Guides/Core/working-doc-conventions.md`](Guides/Core/working-doc-conventions.md)) with a checklist of the three phases, Planning, Infrastructure and Writing, in the form the unit-testing guide gives, and creates test files organized into sections with test stubs in each. Test files use `🟡` on section MARKs and `@Test` functions (in-code progress markers). Doc comments on every stub serve as the test plan. At the planning gate, `Planning` remains unchecked until the supervisor approves advancing to infrastructure.
2. **Infrastructure.** Agent identifies required test infrastructure across all planned tests in the testing session (stubs, fixtures, production code abstractions) and proposes additions. The orchestration document keeps `Infrastructure` unchecked until the supervisor approves advancing to writing. Related infrastructure docs and artifacts live under the same `skai/working-docs/<branch-path>/<session-name>/...` session folder.
3. **Writing** (per section, file-by-file). Agent implements tests and then runs them section-by-section, finishing the current file before moving to the next. Gates: agent stops after writing (before running tests), and stops after test results to confirm conclusions and next steps (including any proposed production-code fixes). As tests pass and the supervisor approves, the agent removes `🟡` from those test functions and section MARKs in the test files. The orchestration document keeps `Writing` unchecked until all sections in the testing session are approved complete. If a test requires infrastructure that wasn't identified in Phase 2, it is skipped, the missing infrastructure is documented, and the supervisor can decide at the next planned gate whether to re-enter the infrastructure phase or defer that skipped work.

Phase 3 repeats for each section until none remain.

### Debugging (skill `skai-debugging`)

Evidence-first problem resolution. Prevents "guessing fixes" loops by requiring observable evidence before drawing conclusions. The process defines a toolkit of effective strategies (targeted logging, possibility-space partitioning, minimal reproducers, bisection, invariant assertions) that guide the agent's debugging approach.

- Guides [`Guides/Core/debugging-guide.md`](Guides/Core/debugging-guide.md), [`Policies/debugging-process-rule.md`](Policies/debugging-process-rule.md)

**Prerequisites:** A bug, crash, or unexpected behavior to investigate. Provide whatever evidence you have (error messages, logs, screenshots, steps to reproduce).

**Phases (repeating):**

1. **Hypothesize and experiment.** Agent states the current possibility space, chooses a tactic, and proposes the smallest discriminating experiment. Gates: pre-experiment and post-experiment during iteration, then hard gates for root cause, fix, and verify/close.

Repeats until the root cause is isolated.

### Dev retro (skill `skai-dev-retro`)

Completeness backstop that can be used at any point during any workflow. Reviews what has transpired since the last retro (or since session start), identifies gaps, reconciles plan drift, updates documentation, captures behavior the product specs do not yet reflect, and reflects on process.

- Guide [`Guides/Process/dev-retro.md`](Guides/Process/dev-retro.md)

**Prerequisites:** Work to review. The agent reads work specs, planning docs, evidence artifacts, the product specs, and any open product spec change package.

**Phases:**

1. **Retro.** Agent performs the full checklist, reports findings, and completes immediately if neither a product specs finding nor a process suggestion was generated.
2. **Product specs follow-up (optional).** If the session revealed behavior the catalog does not reflect, the agent seeds a change package -- draft requirements plus `- [ ] D<n>` items for what it could not settle -- and stops at a handoff gate. It never writes the catalog itself. On `next`, the agent enters [`Guides/ProductSpecs/product-specs-authoring.md`](Guides/ProductSpecs/product-specs-authoring.md), which owns resolving the items and, in turn, promotion.
3. **Process improvement follow-up (optional).** After all six retro steps, process suggestions remain as unchecked `S<n>` items. The ticket-drafting gate is used only when there is no product specs handoff. When both exist, product specs goes first and exits retro; the supervisor later invokes [`Guides/Process/ticket-filing.md`](Guides/Process/ticket-filing.md) from the retained suggestions. Ticket filing owns draft review and filing approval.

### Process refinement (skill `skai-process-refinement`)

Hardens a process guide against a cold review. A fresh, no-context session reads the guide set and attacks it; the refining session triages the findings, repairs one cluster at a time, scores the round, and decides whether to run another.

- Guide [`Guides/Process/process-refinement-guide.md`](Guides/Process/process-refinement-guide.md)
- Template [`Guides/Process/cold-review-prompt-template.md`](Guides/Process/cold-review-prompt-template.md)

**Prerequisites:** The guide document(s) to refine, and a design spec to judge them against. Without a spec, close that gap first -- the spec is the standard every finding is weighed against.

**Phases:**

1. **Commission the review.** Fill the template's slots and hand the filled prompt to a fresh session. The reviewer must not see the refinement guide or the template itself -- both are refiner-facing and would bias it.
2. **Triage.** Classify every finding `accept` / `log only` / `reject` / `supervisor decision` against the codification bar, consulting the target's findings log so settled ground is not relitigated. Collapse findings that name one defect into a single row.
3. **Score the round.** Before the first repair, record the round's score, defect counts, and noise count in the working document.
4. **Repair.** One cluster at a time, with a written self-check after each, then verify the repairs before handing the guide back.
5. **Stop or iterate.** Terminal is a fresh round over the current text with no new live findings, or the supervisor approving the unimplemented ledger. Close the pass and append every disposition to the findings log.

### Suggestion (skill `skai-suggestion`)

The suggestion box for skai itself. A developer has an idea, request, or complaint about the skai dev process; the agent helps articulate it, captures it as a ticket draft, and optionally files it as a GitHub issue on the skai repo. It does not change any guide's content — that is [Process refinement](#process-refinement-skill-skai-process-refinement).

- Guide [`Guides/Process/ticket-filing.md`](Guides/Process/ticket-filing.md)

**Prerequisites:** None -- can be triggered at any point during a session.

**Phases:**

1. **Understand and draft.** Agent asks clarifying questions to understand the suggestion (skipped if the developer provides enough detail up front). Once it has enough context, it stops at a ready-to-draft gate. On `next`, it chooses a session name, writes one or more `- [ ] T<n> Ticket: ...` drafts (with bold sub-bullet body fields) to `skai/working-docs/<branch-path>/<session-name>/process-tickets.md`, and presents them for review.
2. **Review and file (optional).** The draft-review gate is the main filing gate: the supervisor can revise drafts or move them to a `## Skipped` subsection, or say `next` to file the remaining unchecked `- [ ] T<n> Ticket: ...` entries as GitHub issues on `skai`. On filing, the entry is checked (`- [x]`) and a `- **Filed** #<n>` sub-bullet is appended.

### Configure SKAI (skill `skai-configure`)

Say **“configure SKAI”** in your project chat. The agent launches the bundled Mac app with a
categorized checklist with descriptions for both parent categories and individual skills/policies. Project settings define the
shared selection in **Project**; the **User** tab overrides components just for your working copy.

Agent launches use **Save and Apply**: saving closes the app immediately and the waiting agent
updates the installation. When opened independently, the app uses **Save**, remains open and shows
a dialog explaining how to ask an agent to apply the saved choices. OK returns to the checklist;
Save becomes available again after another edit. Closing discards unsaved edits and preserves saves.
A double-click launch finds the owning host repository when SKAI is installed as a submodule,
including under nested folders such as `Submodules/skai`. Otherwise, it asks you to choose a host.

- Guide [Configure SKAI](Guides/Core/configure-skai.md)
- App [SKAIConfigure.app](Bin/SKAIConfigure.app)
- Selection contract [Component configuration](Install/component-selection.md)

**Prerequisites:** An Apple Silicon Mac running macOS 13 or later and a harness that can launch
a local command and wait for its completion. The bundled app needs no browser automation, server or runtime Xcode installation.
The compiled app ships inside the SKAI checkout; users do not build it or install it separately. It
uses **Project** and **User** tabs. Bulk actions such as Select all, Clear and Use project
settings are in the compact **⋯** menu beside the tabs.

**Phases:**

1. **Choose components.** Agent opens the app for the active host project. Edit Project or User; Configure SKAI is always available and cannot be deselected.
2. **Save and Apply.** In agent mode the app writes changed config layers, closes without confirmation and returns the saved result. The agent runs each installed adapter's runbook against the current checkout. Standalone Save keeps the app open and gives the manual apply prompt instead.
3. **Verify.** Installer checks actual managed collateral against current config before recording success, even when selections or SKAI SHA are unchanged. Unmanaged conflicts and unrelated migrations retain their own approval requirements.

Project selections live in `skai/config.json`. Private overrides live in gitignored
`skai/config.local.json`, containing only explicit overrides:

```json
{
  "schemaVersion": 1,
  "overrides": {
    "skill.skai-debugging": true,
    "skill.skai-ui-map-architecture": false
  }
}
```

In the User tab, each component has a menu in the checkbox's place: **Project** omits the key,
**On** writes `true` and **Off** writes `false`. Categories have no control on User.
The User tab shows the override count. An overridden component's name is blue on both tabs, as is
the name of any category containing one; on Project the row also shows a blue **User: On/Off**
label with the user's value. On User, inherited component names and categories without overrides
are subtly dimmed.
Local settings take precedence; local-only edits leave project config untouched. The installer
also ignores `skai/install-state.local.json`, where local effective installation history is recorded.
Turning on a component locally can require migration of shared collateral under normal installation
rules; the user owns that choice.

Without either config file, every applicable component is installed. Once saved, the config is an explicit
selection: unchecked components and newly introduced optional components remain disabled until
selected. An empty selection retains configuration support. Guides and the app remain in the SKAI
checkout; the installer controls host-installed skills/policies and preserves project-owned content,
Integration values and addenda. If installation is interrupted, the saved desired config remains
available for the next install/update. Component history starts with customization or any managed
component removal, retaining each component’s last applied SHA through disable/re-enable.
Unchanged default installs need no component ledger; returning to defaults never discards history once recorded. On re-enablement, migrations are
checked from that component's version, even when the overall SKAI SHA hasn't changed. See
[Component history and migrations](Install/component-history.md).

### Update installation (skill `skai-update-installation`)

Update `skai` to the latest release (or a target you name), review what changed, and re-run adapter runbooks.

- Guide [`Guides/Core/update-installation-guide.md`](Guides/Core/update-installation-guide.md)

**Prerequisites:** An existing installation ([`skai/install-state.json`](skai/install-state.json), or the gitignored local state, must exist from the initial install).

**Phases:**

1. **Pick target, update, and report.** Agent updates the submodule to the latest release (`v<N>` tag) by default — or to a target you name (head of current branch, head of main, or a specific commit) — and reads every release document (`Releases/release-<n>.md`) between your installed release and the target, plus `Releases/unreleased.md` for a commit or branch-head target, reporting what they require. Gate: supervisor acknowledges before any runbooks are re-run.
2. **Re-run adapters.** Agent re-runs each installed adapter's install/update runbook to pick up new or changed assets.

### Working documents

- Working documents (plans, specs, progress logs) live under [`skai/working-docs/`](skai/working-docs/) and are organized by your current git branch.
- `<branch-path>` is the current branch name, with `/` decomposed into nested folders (so `feature/foo` becomes `feature/foo/`).
- Working docs are ephemeral and typically git-ignored.
- One exception: the refinement **findings log** at [`skai/refinement-reviews/`](skai/refinement-reviews/) is committed, one file per refined target. It carries what earlier refinement passes decided, so a later pass does not re-argue settled ground.

### Figma designs

- A project's Figma design file follows [`Guides/Design/figma-designer-guide.md`](Guides/Design/figma-designer-guide.md): page roles, conventions, canvas layout, frames, color and dimension variables, components, copy, and backfilling; a file with several target sizes also follows [`figma-designer-guide-multiple-sizes.md`](Guides/Design/figma-designer-guide-multiple-sizes.md).
- The project README links each main page of the file (`Production`, `Components`, `Design System`).
- Changing the designs follows [Design authoring](#design-authoring-skill-skai-design-authoring) and [Design promotion](#design-promotion-skill-skai-design-promotion).

## Development guide (for contributors)

This repo is typically maintained with an LLM. When you ask an LLM to make changes, point it at:
- [`README.md`](README.md) (this file)
- [`internal/maintain-skai.md`](internal/maintain-skai.md) (LLM maintainer entry point: common rules and a descriptive routing table for specialized references under [`internal/maintenance/`](internal/maintenance/))
- [`internal/maintain-retro.md`](internal/maintain-retro.md) (post-change checklist to ensure nothing was forgotten)
- [`internal/maintain-tickets.md`](internal/maintain-tickets.md) (work through process improvement tickets labeled `agent ready`)
- [`Releases/`](Releases/) (one technical document per release, read by the installing agent; [`CHANGELOG.md`](CHANGELOG.md) holds the human release notes)

### LLM-assisted change workflow (recommended)

- Ask the LLM to:
  - propose a small plan,
  - make the minimal edits,
  - then report exactly which files changed and why.
- Require safety defaults (unless you explicitly override):
  - no commits
  - no deletions
  - no dependency changes

### App and branding development

Maintainer-only app sources, tests and build tooling live under
[internal/apps/ConfigureSKAI](internal/apps/ConfigureSKAI). Rebuild the bundled app with
`bash internal/apps/ConfigureSKAI/build.sh` from the repository root; the
[build script](internal/apps/ConfigureSKAI/build.sh) produces the Apple Silicon app bundle in
[Bin/SKAIConfigure.app](Bin/SKAIConfigure.app). The repo-bundled app uses an ad hoc signature. Developer ID signing/notarization is a separate
packaging choice, not a prerequisite for the Git-based SKAI release.

Run the [configuration tests](internal/apps/ConfigureSKAI/test.sh) with
`bash internal/apps/ConfigureSKAI/test.sh`. They cover native config editing/host discovery, migration
history and agreement between the packaged Mac resolver and portable Python resolver. Rebuild the
app before testing changes to its source. UI appearance and interactions are checked manually.

Logo sources, exports and regeneration instructions live under
[internal/branding](internal/branding/README.md). The main README references those exports directly.
Host runtime tools stay in [Bin](Bin); app source and branding tooling are not installed into projects.

### Contributor rules

- Keep sources in this repo **IDE-neutral** (`.md`). IDE-specific outputs are generated into host repos by install/update runbooks.
- If you add/move/rename an asset, update:
  - [`assets.manifest.json`](assets.manifest.json)
  - [`README.md`](README.md) Usage section (developer-facing guides should be documented at file level)
- For a host-affecting change, update both [`Releases/unreleased.md`](Releases/unreleased.md) (the technical document the installing agent reads) and [`CHANGELOG.md`](CHANGELOG.md) (release notes for people).
- Installed collateral is changed by LLM-runbook-driven installers following [`Policies/`](Policies/). The configuration app writes only the project-owned desired config on explicit Save; it does not install or remove components. Other scripts must not mutate host repos.
