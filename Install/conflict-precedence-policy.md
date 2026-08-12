# Install/Update Conflict & Precedence Policy

This policy defines how installers and update runbooks must behave in the presence of existing files.

## File classes

- **Managed file**: contains the managed header (`Managed-By: skai`).
- **Managed skill file**: a skill file at `.cursor/skills/**/SKILL.md`, `.claude/skills/**/SKILL.md`, or `.agents/skills/**/SKILL.md` that contains the managed marker comment described in `Install/managed-header.md`.
- **Managed symlink**: a symlink created by the installer that points at the expected repo-owned target path.
- **Managed block file**: a project-owned file that contains a delimited managed block (begin/end markers) that the installer may update in-place (e.g., ignore files).
- **Legacy candidate**: appears to be an older copy of a managed asset but lacks the managed header.
- **Project-owned file**: anything else (custom project content).

## Core rules

- Never overwrite project-owned files.
- Managed files may be overwritten deterministically.
- Managed skill files may be overwritten deterministically when the managed marker is present.
- Managed symlinks may be overwritten deterministically if they already point to an `skai` target.
- Managed block files may be updated deterministically, but only within the managed block.
- Deprecated install artifacts should be identified during discovery and proposed for cleanup (permission-gated).
- Legacy candidates must not be overwritten by default.
  - Migrate by generating new managed outputs in the current target locations.
  - Default migration plan should propose a cleanup action for any legacy candidates that are known install artifacts (delete or replace-with-symlink), but never execute without explicit human approval.

## When destination path already exists

- If destination does not exist: create it.
- If destination exists and is managed: overwrite/update it.
- If destination exists and is a symlink:
  - If it points to the expected `skai` target: treat as managed symlink → update/replace as needed.
  - Otherwise: treat as project-owned → do not overwrite.
- If destination exists and contains a managed block: treat as managed block file → update only the block.
- If destination exists and is not managed:
  - Treat it as project-owned by default.
  - If it looks like a legacy candidate, classify it as legacy candidate and do not overwrite.
  - Create the new managed output in the current canonical location (e.g., `.cursor/rules/skai/`) with a non-conflicting name only if needed.

## Cleanup step (always explicit)

Cleanup of legacy candidates is always a separate step:
- Present the list of legacy candidates.
- Ask whether to delete, keep, replace with a symlink, or strip overlapping content.
- Do not delete or strip without explicit approval.

## Canonical project-artifact path migration

The first update that adopts the top-level `skai/` layout must discover and plan these known moves:

| Legacy path | Canonical path |
|---|---|
| `docs/skai/integration.md` | `skai/integration.md` |
| `docs/skai/install-state.json` | `skai/install-state.json` |
| `docs/skai/ui-map/` | `skai/ui-map/` |
| `docs/skai/changes/` | `skai/changes/` |
| `working-docs/` | `skai/working-docs/` |

- Inventory both sides during discovery and list each applicable move in the plan. `working-documents/` is not part of this migration.
- The confirm gate must explicitly approve the listed moves. A move preserves the artifact; it is not legacy cleanup.
- If a destination is absent, move the source there after approval. Use `git mv` for tracked paths and `mv` for untracked paths.
- If both source and destination exist, do not overwrite or silently merge them. Report the collision and STOP for a project-specific merge decision.
- Leave unrelated content under `docs/skai/` or top-level `working-docs/` untouched.
