# Maintain `skai` (LLM maintainer runbook)

This file is instructions for an LLM making changes **to the `skai` repo itself** (not installing into a host project).

## Safety defaults

- Do not commit unless explicitly asked. A request to cut a release explicitly authorizes the release commit and tag, but not a push.
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
3. Use the routing table below to read only the references relevant to this change. Propose a short plan and then proceed. For a host-affecting change, assess migration needs under `Required bookkeeping` while preparing that plan.
4. After significant edits (multi-file changes, path moves, installer behavior changes), run `internal/maintain-retro.md` and fix straightforward misses immediately.

## Required bookkeeping (most common misses)

When you change assets, keep these in sync:
- `Managed-Updated-At`: bump it in the same edit that changes a managed file's content, never as a separate step -- a separate step is the one that gets skipped
- `assets.manifest.json`
  - add/move/rename assets here
  - keep `id` stable when possible
  - edit it as text; serializing and rewriting the file (e.g. `json.dumps`) reformats every entry
- `README.md`
  - update the Usage section for developer-facing skills (see [Guide authoring](maintenance/guide-authoring.md#readme-usage-section-conventions))
- `CHANGELOG.md`
  - add an entry under the top `## Unreleased` section for changes that affect a host installation (prefix each line item with the date, `YYYY-MM-DD`)
  - **Audience: the installing agent, not a supervisor reader.** When proposing a host-affecting change, assess its impact on existing artifacts as well as future outputs; this assessment does not require access to a host checkout. Entries must give the updating agent what it needs to migrate: asset renames/moves (old path → new path), additions/removals, managed-content changes, required reruns, and existing-artifact transformations. For a transformation, state what to discover, how to transform it, what to preserve, and how to verify it. If execution is uncertain, inspect `Guides/Core/update-installation-guide.md` and the relevant adapter runbook before proposing installer changes. Omit pure-internal changes that don't touch a host (working-doc edits, test-harness tweaks, refactors with no asset effect).
  - **`## Unreleased` is a staging log, not finished notes.** Entries stack up across sessions as work lands — that is expected. Within your own session, write the *net* entry for your change; don't narrate your own back-and-forth (no "add X" then "rename X to Y" in the same batch). Do not rewrite or reconcile earlier sessions' Unreleased entries as you go — you may lack their context. Cross-session overlaps are merged later, at the cut (see [Releases](maintenance/releases.md#release-planning)).
  - released sections are frozen: below a `## Release <N>` heading (or the legacy `## Released` bucket), entries are append-only history — fix an outright error, but never rewrite shipped scope.
  - always determine the date by running `date +%Y-%m-%d` in the terminal (see `Install/managed-header.md`, "Determining today's date")
  - format entries for fast scanning: prefer multiple short bullets over one giant "mega-entry"; short bold headline + 1-2 sentences max; group by theme when many files change (core mechanics, policies, spec guides, test guides, templates, etc.)
- `Bin/ui-map-render.py`
  - its docstring ("RENDER CONVENTIONS") is the canonical render spec: update it in the same edit as the code
  - when the render output changes, regenerate the Mermaid block in `Guides/UIMap/ui-map-demo.md` from that guide's own YAML (`uv run Bin/ui-map-render.py <demo yaml> -o <file>`) and update the guide's notes; never hand-edit the block
  - `Bin/ui-map-viewer.js` and `Bin/ui-map-viewer.css` are the `--html` output's viewer, loaded by every rendered page from the SKAI checkout: a behaviour change there is a render change (docstring rule 12, changelog), and the two files must stay beside the renderer under their current names, since rendered pages link them by relative path
- Skills (if you add/change them):
   - shared templates live at `Templates/skills/skai-*/SKILL.md`
   - Cursor installer installs them into host repos at `.cursor/skills/`
   - Claude Code installer installs them into host repos at `.claude/skills/`
   - Codex installer installs them into host repos at `.agents/skills/`
   - **Wrapper pattern (invariant)**: skill templates must be thin wrappers -- a few lines that point the LLM at the corresponding Guide(s) in `Guides/`. All substantive logic lives in the Guide, not in the skill template. This keeps the files copied into host projects small and ensures the Guide is the single source of truth.
   - Adapter runbooks derive their skill set from manifest `adapter:` tags and `sourcePath`s. Keep those tags complete; do not duplicate a skill inventory in a runbook.
   - Agent instruction composition is shared in `Install/agent-instructions-install-update.md` and `Templates/agents/instructions-block.md`; preserve adapter template ids and dated block markers.
   - When adding a new skill: write its Guide first, then the thin wrapper that references it.

## Maintenance reference routing

Read the matching references before editing; several rows may apply. Do not load every reference for an unrelated maintenance task. Paths in this table are relative to this runbook.

| When your change involves… | Read | What you will find |
| --- | --- | --- |
| Adding or editing a guide, runbook, skill entry point, worked example, or README Usage entry | [Guide authoring](maintenance/guide-authoring.md) | Guide placement, faithful examples, README entry format, and the per-edit sanity scan. Gate-specific checks apply only to gated workflows. |
| A workflow that waits for supervisor decisions or approval; discussion items; gates, advance intent, auto, marker lifecycles, or handoffs | [Gated workflows](maintenance/gated-workflows.md) and the [process-flow definitions](../Guides/Core/process-flow.md) | The standard inline runtime template, discussion schema, pre-edit workflow modeling, post-edit simulations, and rules for propagating process-flow changes. |
| Creating, finding, reopening, consuming, promoting, or moving change packages; adding a new package type | [Change packages](maintenance/change-packages.md) | Repository ownership, change-ID grouping, independent type folders, active/promoted lifecycle, link repair, completion evidence, and migration checks. Applies to requirements and UI Map workflows and their callers. |
| Adapter installers, managed files/blocks, Integration templates, install state, or upgrade execution | [Installation](maintenance/installation.md) | Idempotency, overwrite/deletion rules, install-state ownership, Integration block/marker conventions, and installer-specific checks. Consult the affected runbook under `Install/` for execution details. |
| Preparing release notes, cutting a release, or creating its commit/tag | [Releases](maintenance/releases.md) | Consolidating Unreleased notes, frozen release history, release numbering, verification, commit/tag authorization, and push boundaries. |
| Completing a significant multi-file, path, installer, or workflow change | [Maintenance retro](maintain-retro.md) | The final bookkeeping and consistency backstop, applicable house-style checks, and process reflection. |

## Common house style

These rules apply to Guides, internal runbooks and maintenance references, and skill entry points.

- Keep skill templates as thin wrappers; substantive runtime instructions live in their Guides.
- Use "advance intent" and "supervisor" for workflow control. An operator is the agent executing the workflow; the supervisor is the human or authorized agent reviewing it.
- Keep guides concise and route specialized material through descriptive links. Inline the runtime gate and marker mechanics the executing agent needs; maintainer references are authoring inputs, not runtime dependencies.
- Registered assets require the managed header and a `Managed-Id` matching the manifest. This meta-runbook and its references under `internal/maintenance/` are not manifest assets and need no managed header.
- Use IDE-neutral Markdown; IDE-specific outputs are generated by installer runbooks under `Install/`. Use project-agnostic examples (the shared fictional theme is LumenNotes).
- Ephemeral working docs use `Guides/Core/working-doc-conventions.md`; change packages use the distinct lifecycle in [Change packages](maintenance/change-packages.md).
- After each guide edit, run and record the applicable [sanity scan](maintenance/guide-authoring.md#sanity-scan-after-every-guide-edit). For gated workflows also model before editing and simulate after editing as described in [Gated workflows](maintenance/gated-workflows.md).

## After changes (retro)

After making changes, run the post-change checklist in `internal/maintain-retro.md`.

## How to guide an LLM (prompt template)

Use this as a starting prompt when maintaining this repo:

> You are updating the `skai` repo.
> Follow `README.md` and `internal/maintain-skai.md`.
> Make minimal changes.
> Update `assets.manifest.json`, `README.md` (asset inventory), and `CHANGELOG.md` as needed.
> Do not commit or delete files unless I explicitly ask.
> After edits, summarize exactly what changed and list touched files.
