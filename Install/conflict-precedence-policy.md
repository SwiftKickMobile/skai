# Install/Update Conflict & Precedence Policy

This policy defines how installers and update runbooks must behave in the presence of existing files.

## File classes

- **Managed file**: carries the managed header, or the marker comment after frontmatter (`Install/managed-header.md`). The installer owns the file.
- **Managed block**: contains `BEGIN`/`END` managed-block markers. The installer owns only the block.
- **Not managed**: neither. The installer owns nothing here. A file that looks like an old install artifact -- a stale copy of a managed asset, or a symlink into `Submodules/skai/...` -- is a **legacy candidate**: it may be proposed for cleanup, never acted on without approval.

## Core rules

- A managed file may be overwritten deterministically.
- A managed block may be updated deterministically, but only within the block.
- Anything not managed is never overwritten. Migrate by generating new managed outputs in the current canonical location; propose cleanup of legacy candidates as a separate, permission-gated step.

## When destination path already exists

- If the destination does not exist: create it.
- If it is a managed file: overwrite it.
- If it contains a managed block: update only the block.
- Otherwise: do not overwrite it; inserting a managed block into it is permitted, permission-gated. If it is a legacy candidate, propose cleanup. Create the new managed output in the canonical location with a non-conflicting name only if needed.

## Cleanup step (always explicit)

Cleanup of legacy candidates is always a separate step:
- Present the list of legacy candidates.
- Ask whether to delete, keep, or strip overlapping content.
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
