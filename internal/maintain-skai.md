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
   - repo metadata change (manifest/release documents/changelog/readme)
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
- `Releases/unreleased.md` and `CHANGELOG.md` — two documents, two audiences; every host-affecting change writes both, an internal-only change writes neither
  - **`Releases/unreleased.md` is the technical document for the installing agent.** Add a dated entry (`YYYY-MM-DD`) for every change that affects a host installation. When proposing a host-affecting change, assess its impact on existing artifacts as well as future outputs; this assessment does not require access to a host checkout. Entries must give the updating agent what it needs to migrate: asset renames/moves (old path → new path), additions/removals, managed-content changes, required reruns, and existing-artifact transformations. For a transformation, state what to discover, how to transform it, what to preserve, and how to verify it. Write every step so it is safe to re-run (a move of an already-moved path or a conversion of an already-converted file is a no-op); a step that cannot be made re-runnable says so and states its guard. A migration the supervisor should review rather than merely run is written as the stops the agent makes. If execution is uncertain, inspect `Guides/Core/update-installation-guide.md` and the relevant adapter runbook before proposing installer changes. Omit pure-internal changes that don't touch a host (working-doc edits, test-harness tweaks, refactors with no asset effect).
  - **`CHANGELOG.md` is release notes for people.** Add one short line under its `## Unreleased` section saying what changed and why it matters; a reader decides from it whether to look at the technical document. No migration mechanics here.
  - **Unreleased is a staging log, not finished notes.** Entries stack up across sessions as work lands — that is expected. Within your own session, write the *net* entry for your change; don't narrate your own back-and-forth (no "add X" then "rename X to Y" in the same batch). Do not rewrite or reconcile earlier sessions' Unreleased entries as you go — you may lack their context. Cross-session overlaps are merged later, at the cut (see [Releases](maintenance/releases.md#cutting-release-n)).
  - released documents are frozen: `Releases/release-<N>.md` and the matching `## Release <N>` section are append-only history — fix an outright error, but never rewrite shipped scope.
  - always determine the date by running `date +%Y-%m-%d` in the terminal (see `Install/managed-header.md`, "Determining today's date")
  - format entries for fast scanning: prefer multiple short bullets over one giant "mega-entry"; short bold headline + 1-2 sentences max; group by theme when many files change (core mechanics, policies, spec guides, test guides, templates, etc.)
- Tool tests: each tool under `Bin/` and `internal/apps/` has one self-contained automated test in `internal/tests/tools/<tool-name>/` (`test.py`, or `test.sh` when it must compile code first). Run it after changing that tool, and extend it when the tool's behavior changes; the tool's docstring stays its documentation, so the test folder has no README. There is no top-level runner.
- `Bin/spec-tool.py`
  - `Bin/spec-review.v<n>.css` and `Bin/spec-review.v<n>.js` are the review pages' stylesheet and script, loaded by every rendered page from the SKAI checkout by relative path. Versioning rule (both for these and for the UI Map viewer): a change that leaves every page already rendered against the current version working as before is made in place and reaches them all; a change that would break or alter such a page (markup, the classes and attributes the script reads, the script's behaviour) is a new version: new files, the renderer links them, and every old version stays beside the tool untouched. The unversioned `ui-map-viewer.css` / `.js` are frozen copies for maps rendered before versioning.
- `Bin/ui-map-render.py`
  - its docstring ("RENDER CONVENTIONS") is the canonical render spec: update it in the same edit as the code
  - when the render output changes, regenerate the Mermaid block in `Guides/UIMap/ui-map-demo.md` from that guide's own YAML (`uv run Bin/ui-map-render.py <demo yaml> -o <file>`) and update the guide's notes; never hand-edit the block
  - `Bin/ui-map-viewer.v<n>.js` and `Bin/ui-map-viewer.v<n>.css` are the `--html` output's viewer, loaded by every rendered page from the SKAI checkout by relative path: a behaviour change there is a render change (docstring rule 12, release documents) and follows the versioning rule above
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
| Guide addendum loading, overrides, receipts, lookup-name compatibility, wrapper routing or installer preservation | [Guide addenda](maintenance/guide-addenda.md) | The reviewed entry/footer boilerplate, host-root lookup, precedence and project ownership; applies to every registered guide, including references and handoffs. |
| A workflow that waits for supervisor decisions or approval; discussion items; gates, advance intent, auto, marker lifecycles, or handoffs | [Gated workflows](maintenance/gated-workflows.md) and the [process-flow definitions](../Guides/Core/process-flow.md) | The standard inline runtime template, discussion schema, pre-edit workflow modeling, post-edit simulations, and rules for propagating process-flow changes. |
| Creating, finding, reopening, consuming, promoting, or moving change packages; adding a new package type | [Change packages](maintenance/change-packages.md) | Repository ownership, change-ID grouping, independent type folders, active/promoted lifecycle, link repair, completion evidence, and migration checks. Applies to product specs and UI Map workflows and their callers. |
| Adapter installers, managed files/blocks, Integration templates, install state, or upgrade execution | [Installation](maintenance/installation.md) | Idempotency, overwrite/deletion rules, install-state ownership, Integration block/marker conventions, and installer-specific checks. Consult the affected runbook under `Install/` for execution details. |
| Preparing release notes, cutting a release, or creating its commit/tag | [Releases](maintenance/releases.md) | The two release documents and their audiences, consolidating the unreleased document and writing the human notes, frozen release history, release numbering, verification, commit/tag authorization, and push boundaries. |
| Completing a significant multi-file, path, installer, or workflow change | [Maintenance retro](maintain-retro.md) | The final bookkeeping and consistency backstop, applicable house-style checks, and process reflection. |

## Maintainer-only code and artwork

Keep app source and build scripts under `internal/apps/`, tests under `internal/tests/` (tool tests
in `tools/`, skill tests in `skills/`), and branding sources and exports under `internal/branding/`.
Intermediate build output goes to the scratch root (`/tmp/skai/<session-name>/`), never into the repository; a shipped deliverable (the app bundle in `Bin/`) is not output. Host runtime executables and their dependencies stay in `Bin/`.
Document contributor tooling in the README Development guide, rather than skill Usage entries.

## Common house style

These rules apply to Guides, internal runbooks and maintenance references, and skill entry points.

- Keep skill templates as thin wrappers; substantive runtime instructions live in their Guides.
- Use "advance intent" and "supervisor" for workflow control. An operator is the agent executing the workflow; the supervisor is the human or authorized agent reviewing it.
- Keep guides concise and route specialized material through descriptive links. Inline the runtime gate and marker mechanics the executing agent needs; maintainer references are authoring inputs, not runtime dependencies.
- Registered assets require the managed header and a `Managed-Id` matching the manifest. This meta-runbook and its references under `internal/maintenance/` are not manifest assets and need no managed header.
- Use IDE-neutral Markdown; IDE-specific outputs are generated by installer runbooks under `Install/`. Use project-agnostic examples (the shared fictional theme is LumenNotes).
- Working docs follow `Guides/Core/working-doc-conventions.md` in host repositories. skai's own working docs are not committed (`skai/working-docs/` is ignored here: every host checks this library out whole); the one record kept is a refinement target's working document, tracked at `skai/refinement-reviews/<target>-refinement.md` beside its design spec and findings log; change packages use the distinct lifecycle in [Change packages](maintenance/change-packages.md).
- After each guide edit, run and record the applicable [sanity scan](maintenance/guide-authoring.md#sanity-scan-after-every-guide-edit). For gated workflows also model before editing and simulate after editing as described in [Gated workflows](maintenance/gated-workflows.md).

## After changes (retro)

After making changes, run the post-change checklist in `internal/maintain-retro.md`.

## How to guide an LLM (prompt template)

Use this as a starting prompt when maintaining this repo:

> You are updating the `skai` repo.
> Follow `README.md` and `internal/maintain-skai.md`.
> Make minimal changes.
> Update `assets.manifest.json`, `README.md` (asset inventory), `Releases/unreleased.md` and `CHANGELOG.md` as needed.
> Do not commit or delete files unless I explicitly ask.
> After edits, summarize exactly what changed and list touched files.
