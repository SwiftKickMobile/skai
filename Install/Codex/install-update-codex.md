# Codex adapter: install/update (LLM runbook)

Purpose: install/update `skai` into any repo using Codex.

This adapter is **stack-aware** (Xcode/Swift, Android/Kotlin, etc.). It detects the project stack from repo signals, then applies stack-specific guidance from addenda files.

## Assumptions (stop if false)

Assume the following, unless the host repo already establishes a different working convention:

- Codex instructions live at root `AGENTS.md`; `.agents/` holds skills. The instruction file is project-owned, with a dated SKAI block.
- Agent-facing skills live at `.agents/skills/skai-*/` (managed skill wrappers pointing to submodule sources).
- Mixed-agent repos may also contain `.cursor/**` or `.claude/**`; those belong to their own adapters and are out of scope for Codex install/update.

If any assumption is false in the host repo's setup, STOP and ask the supervisor what file/path/convention to use.

## Inputs (required reading)

- `assets.manifest.json`
- `Install/component-selection.md`
- `Install/managed-header.md`
- `Install/conflict-precedence-policy.md`
- `Install/agent-instructions-install-update.md`
- `Templates/agents/instructions-block.md`
- `Policies/safe-operations.md`
- `Policies/universal-stop-conditions.md`
- `Templates/docs/skai/integration.md`
- `Templates/agents/codex/AGENTS.md`

## Migration-capable algorithm (required)

Follow the discover -> classify -> plan -> confirm -> execute workflow.

### 1) Discover (read-only)

- Read the current host `skai/config.json` and resolve effective skills/policies for this adapter
  using `Install/component-selection.md`. Inventory actual managed collateral every time, regardless
  of unchanged SHA/config/state; invalid configuration blocks before writing. Read prior component
  history under `Install/component-history.md` before any removal or SHA advancement.

- Identify whether `skai` is already present as a submodule (and where).
- If this is an update, record the current submodule commit SHA (pre-update) and the intended new SHA (post-update).
- **Detect stack** from project signals:
  - Xcode/Swift: `.xcodeproj`, `.xcworkspace`, `Package.swift`, `*.swift`
  - Android/Kotlin: `build.gradle`, `settings.gradle`, `*.kt`, `*.kts`
  - Otherwise: generic (no stack addendum needed)
  - Confirm the detected stack with the developer on initial installation or if ambiguous. During reconfiguration, reuse the established Integration/installed stack when repo signals agree; do not add a routine confirmation after Save.
- **Detect other agent context** (for coexistence rules):
  - Note whether `.cursor/` exists (for optional `.cursorignore` setup).
  - Note whether `.claude/` exists (for optional `.claudeignore` setup).
  - Do **not** inventory or classify other agents' contents -- those belong to other adapters and are out of scope.
- Inventory existing install artifacts:
  - Root `AGENTS.md` and old `.agents/AGENTS.md`; follow the shared instruction migration procedure to preserve custom content and plan permission-gated cleanup of the old path
  - Codex skill files (`.agents/skills/**`)
  - `docs/**`
  - the known legacy and canonical SKAI project-artifact paths in `Install/conflict-precedence-policy.md`
- Identify any existing docs containing integration details (to migrate into Integration doc).

### 2) Classify

Classify each discovered artifact:
- **Managed file**: carries the managed header, or the marker comment after frontmatter (`Install/managed-header.md`) -> overwrite.
- **Managed block**: contains `BEGIN`/`END` managed-block markers -> replace only the block.
- **Not managed**: neither -> do not overwrite (a managed block may be inserted, permission-gated). If it looks like an old install artifact (a stale copy of a managed asset, a symlink into `Submodules/skai/...`), propose cleanup; never act without approval.

### 3) Plan (no changes yet)

Prepare a concrete plan:
- Reconcile the resolved component set: selected missing/changed outputs, deselected managed
  outputs to remove, and managed policy blocks to recompose. Preserve all infrastructure and
  project-owned content. Follow `Install/component-selection.md` for ownership and approval.

- Files to create
- Files to update (managed only)
- Legacy candidates to supersede (create new canonical outputs)
- Integration doc migration items
- Canonical SKAI project-artifact path migrations and any destination conflicts
- Legacy cleanup proposals (permission-gated)

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
     - STOP and ask the supervisor for the missing items before proceeding.
   - Prefer non-interactive command-line commands over GUI instructions. If you can't produce command-line commands with high confidence, leave 🟡 placeholders and ask.
   - **Stack-specific integration doc guidance**: if a stack was detected, read the corresponding addendum for additional rules:
     - Xcode/Swift -> `Install/Codex/stack-xcode.md`
     - Android/Kotlin -> `Install/Codex/stack-android.md`
   - Follow `Install/integration-doc-install-update.md` for how to update the Integration doc safely (managed blocks + supervisor overrides).
4. Create/update root `AGENTS.md` by following `Install/agent-instructions-install-update.md`; use the existing Codex template for the dated block markers and the shared block interior plus applicable policies.
5. Install Codex skills into `.agents/skills/` (see "Installing Codex skills" below).
6. Create/update ignore files (permission-gated if they already exist and are project-owned):
   - Update `.gitignore` by inserting/updating a managed block:
     - Add `/skai/config.local.json` and `/skai/install-state.local.json` for private user settings/history.
     - Remove a `skai/working-docs/` line left in the block by an earlier install; working documents are committed.
   - If `.cursorignore` exists, propose inserting/updating a managed block to exclude `.agents/**` so Cursor sessions don't ingest Codex-specific assets by default (ask approval before changing).
   - If `.claudeignore` exists, propose inserting/updating a managed block to exclude `.agents/**` so Claude sessions don't ingest Codex-specific assets by default (ask approval before changing).
   - Do NOT exclude `Submodules/skai/**` here; use editor UI excludes for autocomplete/search clutter instead.
7. Optionally propose cleanup of legacy candidates as a separate explicit step.
8. Write/update the resolver's `historyStatePath` (see "Install state file" below).

Required Integration doc fields to request (minimum set):
- Build/compile command(s)
- Unit test command(s): run all + run a single test/subset
- How to capture full output (paths/artifacts the supervisor should paste back)
- Device/simulator/emulator conventions (if applicable)
- Known evidence-capture limitations (if any)

## Installing Codex skills

Create these skills in the host repo under `.agents/skills/` by copying the shared templates from the submodule and inserting the managed marker comment immediately after the YAML frontmatter (see `Install/managed-header.md`).

Before stamping, apply the shared checkout-path rule in `Install/component-selection.md`:
rewrite copied wrapper references to use the discovered SKAI checkout location.

Use `Managed-Adapter: codex` and `Managed-Id: skill.<skill-name>` (e.g., `skill.skai-debugging`).

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
- The adapter ID for this runbook is `codex`; the runbook path is `Install/Codex/install-update-codex.md`.

Follow `Install/component-history.md` for configuration fingerprints, retained component records,
migration ranges and failure recovery. Merge only verified applied state after reconciliation.

## Legacy artifact cleanup (permission-gated)

During discovery, if you find artifacts that appear to be from older installations (symlinks pointing into the submodule, guide copies without managed headers, skills that have been renamed or replaced), propose a cleanup plan:

- **Symlinks** into `Submodules/skai/...`: an abandoned install mechanism; propose deleting them (only with explicit approval). Remove the containing directory if empty after cleanup.
- **Non-symlink or project-authored content**: treat as project-owned and STOP to ask the supervisor what to do.
