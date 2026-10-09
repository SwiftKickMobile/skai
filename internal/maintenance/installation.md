# Installer and integration maintenance

This is a maintainer reference, read only when the routing table in [`../maintain-skai.md`](../maintain-skai.md) applies. It is not an installed asset or a runtime dependency of host workflows.

## Install state

- All adapter runbooks write `skai/install-state.json` on successful completion.
- The `update-installation` skill reads this file to determine which adapters to re-run and what SHA was last applied.
- If you add a new adapter runbook, ensure it writes/merges its entry into this file.

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
  - **Managed blocks**: some project-owned files (e.g., ignore files, Integration doc, agent instruction files) are updated only inside delimited managed blocks.
- **Legacy candidates are permission-gated**:
  - Identify legacy candidates.
  - Propose deletion, but do not execute without explicit approval.
- **Gray areas must be surfaced**:
  - Example: legacy `.cursor/rules/debugging.mdc` should be flagged and deletion should be proposed only after migrating any project-specific logging conventions into the Integration doc and getting approval.

## Integration doc architecture (do not regress)

The Integration doc is project-owned at `skai/integration.md`, but is structured to support safe automation.

**Note on `🟡` semantics in this section.** The `🟡` convention used in the Integration doc (and its templates / installer guide) is a **separate concept** from the workflow-progress `🟡` defined in `Guides/Core/process-flow.md` § "Progress markers." Both share the emoji but serve different lifecycles:

| Convention | Where it appears | Semantics |
|---|---|---|
| Workflow-progress `🟡` | Source files (test code, app code) seeded by a skai workflow | TODO marker; completion is removal as the agent's work is approved (see `Guides/Core/process-flow.md` § Progress markers). |
| Integration-doc `🟡` | `Templates/docs/skai/integration.md` and host-installed `skai/integration.md` | "Required project-specific value is missing"; completion is supervisor filling the value AND removing the marker (see rules below). |

Do not conflate them. The workflow-progress rule does not apply to Integration-doc fields, and vice versa.

Format rules:
- `Templates/docs/skai/integration.md` must be **minimal** and must not contain "meta" guidance.
  - No instructions to the installer/LLM (those belong in `Install/integration-doc-install-update.md`).
  - No instructions to supervisors about how to clear 🟡 markers (those belong in `README.md`).

Ownership rules:
- The project owner fills prompted values and clears their associated 🟡/INSTRUCTION prompts as described in README. Freeform edits are limited to **Special instructions / overrides**; form and managed-section structure remain installer-owned.
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
  - no "installer/supervisor instructions" (those belong in `README.md` and `Install/integration-doc-install-update.md`)
  - include copy/pasteable CLI command templates with `<...>` variables
- Ensure `Install/integration-doc-install-update.md` remains the canonical installer guidance for:
  - managed block merge/update/remove behavior
  - `{supervisor response}` placeholders + `INSTRUCTION:` formatting and restoration rules

## If you change install/runbooks

After editing anything under `Install/`:
- Ensure `Install/conflict-precedence-policy.md` still matches the runbooks (managed file vs managed block behavior).
- Ensure `assets.manifest.json` includes any new policy/guide/runbook IDs referenced by the installer.
- Ensure `README.md` Quick start prompts still point at the correct submodule path (`Submodules/skai/...`).
- Ensure ignore-file behavior remains safe: update `.cursorignore` / `.claudeignore` via managed blocks and do not hide the submodule via agent ignore (use editor UI excludes instead).
