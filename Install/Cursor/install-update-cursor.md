# Cursor adapter: install/update (LLM runbook)

This document is the canonical Cursor install/update runbook.

## Inputs (required reading)

- `assets.manifest.json`
- `Install/component-selection.md`
- `Install/managed-header.md`
- `Install/conflict-precedence-policy.md`
- `Policies/safe-operations.md`
- `Templates/docs/skai/integration.md`

Key responsibilities:
- Detect existing installs (including legacy copies of guides/rules) and plan a safe migration.
- Create/update `skai/integration.md` (and migrate any legacy integration command notes into it).
- Generate managed Cursor `.mdc` rule files into `.cursor/rules/skai/`.
- Install `skai` Cursor skills into `.cursor/skills/` (no symlinks; wrappers point at `Submodules/skai/...` sources).
- Update `.cursorignore` (and, if present, `.claudeignore`) via managed blocks so Cursor and Claude installs can coexist without clutter.
- Never overwrite project-owned files; only overwrite managed files; treat lookalike files as legacy candidates.

## Migration-capable algorithm (required)

Follow the discover → classify → plan → confirm → execute workflow.

### 1) Discover (read-only)

- Read the current host `skai/config.json` and resolve effective skills/policies for this adapter
  using `Install/component-selection.md`. Inventory actual managed collateral every time, regardless
  of unchanged SHA/config/state; invalid configuration blocks before writing. Read prior component
  history under `Install/component-history.md` before any removal or SHA advancement.

- Identify whether `skai` is already present as a submodule (and where).
- If this is an update, record the current submodule commit SHA (pre-update) and the intended new SHA (post-update).
- Inventory existing install artifacts:
  - `.cursor/rules/**`, `.cursor/**`
  - specifically scan for prior `skai` install targets under `.cursor/**` (do not assume current targets only):
    - `.cursor/skills/**`
    - `.cursor/agent/**` (deprecated install target; see cleanup guidance below)
  - Root `AGENTS.md` for awareness only; do not write into it from this adapter
  - `docs/**`
  - the known legacy and canonical SKAI project-artifact paths in `Install/conflict-precedence-policy.md`
  - any "integration glue" docs/notes (build/test commands, destinations, artifact paths), wherever they live (README, docs, CI scripts, etc.)
- Inventory any existing Integration doc candidates and existing rule/policy docs (do not assume specific filenames).

### 2) Classify

Classify each discovered artifact:
- **Managed file**: carries the managed header, or the marker comment after frontmatter (`Install/managed-header.md`) → overwrite.
- **Managed block**: contains `BEGIN`/`END` managed-block markers → replace only the block.
- **Not managed**: neither → do not overwrite (a managed block may be inserted, permission-gated). If it looks like an old install artifact (a stale copy of a managed asset, a symlink into `Submodules/skai/...`), propose cleanup; never act without approval.

### 3) Plan (no changes yet)

Prepare a concrete plan:
- Reconcile the resolved component set: selected missing/changed outputs, deselected managed
  outputs to remove, and managed policy blocks to recompose. Preserve all infrastructure and
  project-owned content. Follow `Install/component-selection.md` for ownership and approval.

- Files to create
- Files to update (managed only)
- Legacy candidates to supersede (create new managed files in canonical locations)
- Integration doc migration items (move legacy integration glue into `skai/integration.md`)
- Canonical SKAI project-artifact path migrations and any destination conflicts
- Legacy cleanup proposals (explicitly permission-gated):
  - delete legacy candidates
 - Deprecated install artifact cleanup proposals (explicitly permission-gated):
   - remove managed outputs that were installed by older versions of this runbook but are no longer part of the current install targets

Required gray-area checks (ask the supervisor, then reflect the decision in the plan):
- Search for legacy debugging rule candidates (common examples: `.cursor/rules/debugging*.mdc`, `.cursor/rules/*debug*.mdc`, or other Cursor rules that encode project-specific logging/API conventions).
  - If found, propose:
    1) migrating any project-specific logging/API conventions they contain into `skai/integration.md`, then
    2) deleting those legacy debugging rule files (only with explicit approval).
  - When reporting discovery, list the candidates you found; do not emit "not found" lines for example filenames you didn't find.

### 4) Confirm (supervisor gate)

Present the plan. A verified agent **Save and Apply**, or an explicit request to apply saved SKAI
configuration, supplies component-reconciliation approval: proceed with that scoped plan under
`Install/component-selection.md`. A standalone saved event alone does not authorize installation.
Ordinary install/update plans still wait for supervisor approval before writing.
Unmanaged conflicts, unrelated migrations and legacy cleanup still require their own resolution.

If updating the submodule, include an "update review" section:
- Summarize changes between the old SHA and new SHA for relevant paths:
  - `Guides/`, `Policies/`, `Templates/`, `Install/`, `assets.manifest.json`, `README.md`
- If you cannot compute the diff yourself, STOP and ask the supervisor to provide the diff output.
- State what the release documents require of this adapter (`Releases/release-<n>.md` after the host's release, and `Releases/unreleased.md` for a commit target); when the update-installation guide has already reported them at its release-documents gate, cite that report rather than re-reading.

### 5) Execute (safe order)

1. Ensure submodule is present/updated.
2. Perform the approved canonical project-artifact path migrations from `Install/conflict-precedence-policy.md`; STOP on any source/destination collision.
3. Create/update `skai/integration.md` (migrate legacy command docs into it; do not delete legacy docs by default).
   - If you cannot find the required integration information in-repo:
     - Create/seed the Integration doc from `Templates/docs/skai/integration.md`.
     - Fill only what you can source with high confidence.
     - Add explicit 🟡 placeholders for missing items.
     - STOP and ask the supervisor for the missing items before proceeding with the rest of the install.
   - When filling "Build / compile" and "Unit tests", prefer non-interactive command-line commands (e.g., `xcodebuild ...`) over GUI instructions ("open Xcode…"). If you can't produce command-line commands with high confidence, leave 🟡 placeholders and ask.
   - For Xcode projects: never invent a simulator/device model. If a canonical `xcodebuild -destination` string is not already established in-repo, propose one and ask the supervisor to confirm before writing it.
   - Follow `Install/integration-doc-install-update.md` for how to update the Integration doc safely (managed blocks + supervisor overrides).
3.5 Create/update ignore files (permission-gated if the files already exist and are project-owned):
   - Update `.gitignore` by inserting/updating a managed block:
     - Add `skai/working-docs/` so ephemeral working documents are not committed.
     - Add `/skai/config.local.json` and `/skai/install-state.local.json` for private user settings/history.
   - Update `.cursorignore` by inserting/updating a managed block:
     - Exclude `.claude/**` so Cursor sessions don't ingest Claude-specific assets by default.
     - Do NOT exclude `Submodules/skai/**` here; use editor UI excludes for autocomplete/search clutter instead.
   - If `.claudeignore` exists, propose inserting/updating an equivalent managed block to exclude `.cursor/**` (ask approval before changing).
4. Generate selected/applicable managed policy `.mdc` files into `.cursor/rules/skai/`; remove deselected managed rules under `Install/component-selection.md`. Configuration remains discoverable through the required skai-configure skill.
5. Install `skai` Cursor skills into `.cursor/skills/`.
6. If approved, perform legacy cleanup (delete).
7. Write/update the resolver's `historyStatePath` (see "Install state file" below).

Required Integration doc fields to request (minimum set):
- Build/compile command(s)
- Unit test command(s): run all + run a single test/subset
- How to capture full output (paths/artifacts the supervisor should paste back)
- Simulator/device destination conventions (if applicable)
- Known evidence-capture limitations (if any)

## Cursor install targets

Create these directories in the host repo:
- `.cursor/rules/skai/`
- `.cursor/skills/`

## Generating Cursor rule files (`.mdc`)

The Cursor adapter writes `.mdc` files directly into the host repo.

Rules:
- Each generated `.mdc` starts with YAML frontmatter (`description`, `globs`, `alwaysApply`), then the managed marker comment immediately after its closing `---` (see `Install/managed-header.md`). Nothing precedes the frontmatter.
- For updates, overwrite only when the destination is missing or already has a managed header or marker comment. Convert an older header-first managed rule to frontmatter-first form; preserve its managed id and adapter.
- Determine stack (Swift/Xcode vs Android/Kotlin, etc.) by inspecting the host repo, then confirm on initial installation or ambiguity. Reconfiguration reuses the established stack when repo signals agree.

Initial supported stacks:
- Swift/Xcode: generate `.mdc` with `globs: ["**/*.swift"]`.
- Android/Kotlin: generate `.mdc` with `globs: ["**/*.kt", "**/*.kts"]`.

Policy rule destinations (filenames are stable; generate only the selected/applicable resolved policies):
- `.cursor/rules/skai/coding-patterns.mdc` ← `Policies/coding-patterns.md`
- `.cursor/rules/skai/debugging-process.mdc` ← `Policies/debugging-process-rule.md`
- `.cursor/rules/skai/error-handling.mdc` ← `Policies/error-handling.md`
- `.cursor/rules/skai/unauthorized-changes.mdc` ← `Policies/unauthorized-changes.md`
- `.cursor/rules/skai/safe-operations.mdc` ← `Policies/safe-operations.md`
- `.cursor/rules/skai/universal-stop-conditions.mdc` ← `Policies/universal-stop-conditions.md`
- `.cursor/rules/skai/swift-code-organization.mdc` ← `Policies/swift-code-organization.md` (Swift stack only)

## Installing Cursor skills (recommended; no symlinks)

Create these skills in the host repo under `.cursor/skills/` by copying the shared templates from the submodule and inserting the managed marker comment immediately after the YAML frontmatter (see `Install/managed-header.md`).

Before stamping, apply the shared checkout-path rule in `Install/component-selection.md`:
rewrite copied wrapper references to use the discovered SKAI checkout location.

Use `Managed-Adapter: cursor` and `Managed-Id: skill.<skill-name>` (e.g., `skill.skai-debugging`).

Rules:
- Each destination `SKILL.md` is considered managed only if it contains the managed marker comment described in `Install/managed-header.md`.
- Overwrite only if destination is missing or already contains the managed marker.

Which skills to install is decided by the manifest **and current host config**, resolved under
`Install/component-selection.md`. Install each returned `skills` asset for this adapter using its
stable id/sourcePath and the stamping rules above. No config returns the full adapter-tagged set;
an explicit config installs only selected optional skills plus required configuration support.

During discovery compare actual managed skills with that resolved set. Deselected SKAI-managed
outputs are reconciliation removals under the shared contract; verify marker/id/adapter before
removing their managed file, retain custom resources, and remove directories only if empty.
Retired `skill.skai-ui-map-planning` is a managed retirement removal after plan approval or Save;
its template/guide no longer exist. Every ID in the manifest's `retiredComponents` is the same kind
of removal; when a retired component has a replacement, the release document that retired it says
how a host carries its selection and component history to the new ID. Verify managed markers before
removal and preserve project addenda/artifacts. Other unmarked lookalikes and obsolete artifacts remain separate
permission-gated legacy candidates. Never remove project addenda or canonical data.

## Install state file

Read `Install/component-history.md` on every reconciliation. Persist known baseline
versions before removing outputs; re-enabling a component uses its retained last applied SHA for
artifact migration even if the checkout/global SHA is unchanged. Keep local state/choices out of
shared state. Record this adapter’s `lastSHA` on success even for defaults. A full ledger starts
on customization or any managed removal; retain it thereafter under the shared history contract.

Before recording success, verify the actual skill/policy inventory against a fresh config resolution
under `Install/component-selection.md`. Config drift or incomplete reconciliation prevents recording
success; report the outstanding work and preserve the other adapters' entries.


After a successful install or update, write/update the resolver's `historyStatePath` so the `update-installation` skill can detect changes and re-run the appropriate adapters.

Format:

```json
{
  "managedBy": "skai",
  "submodulePath": "Submodules/skai",
  "lastSHA": "<current submodule HEAD SHA>",
  "lastRelease": "<latest v<N> release tag that is an ancestor of submodule HEAD>",
  "lastUpdatedAt": "<yyyy-mm-dd>",
  "installedAdapters": [
    {
      "adapter": "<adapter-id>",
      "runbook": "<submodule-relative runbook path>",
      "lastRunAt": "<yyyy-mm-dd>",
      "lastSHA": "<current submodule HEAD SHA>"
    }
  ]
}
```

Rules:
- Resolve the state path under `Install/component-history.md`. If local state is new, seed from
  shared state before merging; never overwrite shared state with local effective choices.
- If the file does not exist, create it with this adapter's entry.
- If the file already exists, **merge**: upsert this adapter's entry in `installedAdapters` and its component history (preserve entries from other adapters). Do not advance the top-level `lastSHA`, `lastRelease` or `lastUpdatedAt`: the update-installation guide writes them in its step 7 after every adapter has completed, so a retry after a partial multi-adapter update reports the same release range.
- When creating the file, determine `lastRelease` from the submodule's current HEAD: `git -C <submodulePath> tag --list 'v[0-9]*' --merged HEAD --sort=-v:refname | head -1` — the latest `v<N>` tag that is an ancestor of HEAD. Never write null; omit the field when no tag is an ancestor.
- The adapter ID for this runbook is `cursor`; the runbook path is `Install/Cursor/install-update-cursor.md`.

Follow `Install/component-history.md` for configuration fingerprints, retained component records,
migration ranges and failure recovery. Merge only verified applied state after reconciliation.

## Legacy artifact cleanup (permission-gated)

During discovery, if you find artifacts that appear to be from older installations (symlinks pointing into the submodule, guide/rule copies without managed headers, skills that have been renamed or replaced), propose a cleanup plan:

- **Symlinks** into `Submodules/skai/...`: an abandoned install mechanism; propose deleting them (only with explicit approval).
- **Legacy candidates** (look like managed assets but lack the managed header): do not overwrite. Propose deletion or replacement, but only with explicit approval. If they contain project-specific content (e.g., logging conventions, custom rules), propose migrating that content into `skai/integration.md` first.
- **Non-symlink or project-authored content**: treat as project-owned and STOP to ask the supervisor what to do.

Rationale: leaving legacy copies in place increases the chance that people/agents keep reading the wrong file out of habit.
