# Install/update `skai` (entry runbook)

One entry point for installing or updating `skai` in a host repo, whichever agent is running it.

## Steps

1. Ask the supervisor which adapters to install or update, and wait for the answer. Offer:
   - Claude Code — `Install/ClaudeCode/install-update-claudecode.md`
   - Cursor — `Install/Cursor/install-update-cursor.md`
   - Codex — `Install/Codex/install-update-codex.md`

   Default to the adapter you are running in. If `skai/install-state.json` (or its legacy path, `docs/skai/install-state.json`) exists, present its
   installed adapters as already selected.
2. Run each selected adapter's runbook in turn, in full. Each discovers, plans, and waits for
   approval before writing; the second and later adapters get the same gate, not a pass-through.

Everything about what may be overwritten, how the Integration doc is migrated, and what counts as a
legacy candidate lives in the adapter runbooks and `Install/managed-header.md`.
