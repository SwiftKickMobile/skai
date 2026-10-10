# Install/update `skai` (entry runbook)

One entry point for installing or updating `skai` in a host repo, whichever agent is running it.

## Steps

1. Read `Install/component-selection.md` and resolve the active host's current component configuration. An absent config keeps the full eligible set; invalid/unreadable config blocks.
2. Ask the supervisor which adapters to install or update, and wait for the answer. Offer:
   - Claude Code — `Install/ClaudeCode/install-update-claudecode.md`
   - Cursor — `Install/Cursor/install-update-cursor.md`
   - Codex — `Install/Codex/install-update-codex.md`

   Default to the adapter you are running in. If `skai/install-state.local.json`, `skai/install-state.json` (or legacy `docs/skai/install-state.json`) exists, present its
   installed adapters as already selected.
3. Run each selected adapter's runbook in turn, in full. Each discovers, plans, and waits for
   approval before writing; a saved configure selection supplies the component-reconciliation approval described in the shared contract. Unmanaged conflicts and unrelated cleanup keep their separate gates.

Everything about what may be overwritten, how the Integration doc is migrated, and what counts as a
legacy candidate lives in the adapter runbooks and `Install/managed-header.md`.
