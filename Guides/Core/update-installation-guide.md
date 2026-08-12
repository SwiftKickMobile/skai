Managed-By: skai
Managed-Id: guide.update-installation
Managed-Source: Guides/Core/update-installation-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-12

# Update Installation Guide

Updates the `skai` submodule and re-runs installed adapter runbooks.

## Gates

Core rule: every time the agent is waiting on the human, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the human.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the human gives advance intent. If the gate is non-standard, make it describe the exact human response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the human resolves it.

Planned gates for this workflow:
- After reporting what changed (changelog summary or `git log` fallback), but before running the adapter install/update runbooks.

Workflow-specific blocked gates:
- Both `skai/install-state.json` and the legacy `docs/skai/install-state.json` are missing, so the update workflow does not know what was previously installed.
- The default (latest release) target is requested but the submodule has no `v<N>` release tag.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-step rules below. Do not use them to skip required prerequisite checks.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit human resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking:
- This workflow currently uses inline discussion rather than a required work document.
- The active state lives in the conversation plus the discovered install-state file; adapter migration writes the canonical `skai/install-state.json`.
- At the changelog-review gate, STOP after summarizing what changed and wait for approval before re-running adapter runbooks.

Workflow-specific advance behavior:
- `auto` may bypass the changelog-review gate and continue directly into the adapter runbooks.
- `auto` does not bypass the blocked missing-install-state or no-release-tag cases.
- Use `runbooks` as the stable bounded-auto target for this guide.

## Prerequisites

- `skai/install-state.json` or the legacy `docs/skai/install-state.json` must exist (created by the initial install).
  - If both are missing, STOP and tell the human to run the initial install/update runbook for each adapter first.

## Procedure

### 1. Read the install state file

Read `skai/install-state.json`; if it is absent and `docs/skai/install-state.json` exists, read that legacy file and record the canonical path migration for each adapter's plan. Extract:
- `submodulePath` (default: `Submodules/skai`)
- `lastSHA`
- `lastRelease` (the `v<N>` the host is currently on; may be absent on installs that predate release targeting)
- `lastUpdatedAt`
- `installedAdapters` (list of adapter entries with `runbook` paths)

### 2. Choose the update target

Default to the **latest release** -- the highest `v<N>` tag. Use a different target only when the human names one:

| Human says | Target |
|---|---|
| (nothing) | latest `v<N>` release tag -- the default |
| "head of current branch" | HEAD of the submodule's checked-out branch |
| "head of main" | `origin/main` HEAD |
| "commit <hash>" | that commit |

```
cd <submodulePath>
git fetch --tags
```

Resolve the target to a SHA. For the default, the latest release tag is:

```
git tag --list 'v*' --sort=-v:refname | head -1
```

If the default is requested but no `v<N>` tag exists, STOP with a blocked gate -- there is no release to target yet (the human can re-run naming a branch head or commit).

### 3. Check whether an update is needed

Compare `lastSHA` (from step 1) to the resolved target SHA. If they match, report "skai is already at `<target>`" and stop. Otherwise record the old SHA and continue.

### 4. Update the submodule

Check out the target in the submodule:

```
git -C <submodulePath> checkout <target-sha>
```

The host repo's submodule pointer now references the target; the human commits that pointer change as usual.

### 5. Report what changed

- Read `<submodulePath>/CHANGELOG.md`.
- For a release target: show every `## Release <N>` section newer than the host's installed release (`lastRelease` from state; if absent, fall back to entries dated **after** `lastUpdatedAt`). These sections are written for this step -- they state the asset renames/moves, additions/removals, and re-run needs the adapters must apply.
- For a branch-head or commit target: show `## Unreleased` plus any `## Release <N>` sections in the `<oldSHA>..<newSHA>` range; if none apply, show `git log --oneline <oldSHA>..<newSHA>`.
- Gate: STOP after reporting what changed and end with `⏳ GATE: Next: Run the installed adapter update runbooks. Say "next" or what to change.`

### 6. Run adapter install/update runbooks

For each entry in `installedAdapters`:
- Read the runbook at `<submodulePath>/<runbook>` and execute it.
- Run them sequentially (one adapter at a time).
- Each runbook's migration-capable algorithm handles any necessary updates (new skills, changed policies, deprecated artifacts, etc.).

### 7. Update install state

Update `skai/install-state.json` with:
- The new submodule HEAD SHA
- `lastRelease`: the `v<N>` tag updated to (leave null for a branch-head or commit target)
- Today's date (run `date +%Y-%m-%d` -- see `Install/managed-header.md`)
- Per-adapter `lastRunAt` timestamps

Then complete the workflow.
