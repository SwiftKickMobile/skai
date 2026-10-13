Managed-By: skai
Managed-Id: guide.update-installation
Managed-Source: Guides/Core/update-installation-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-13

# Update Installation Guide

Before using this guide, complete [Project addendum](#project-addendum) loading below.

Updates the `skai` submodule and re-runs installed adapter runbooks.

## Gates

Core rule: every time the agent is waiting on the supervisor, the message must end with a `⏳ GATE:` line. The only normal exception is full workflow completion, which uses `🏁 Complete. Let me know if anything needs adjustment.`

The supervisor is the human or authorized agent outside this workflow that resolves its discussion items and reviews its gates; the executing agent does not resolve or approve its own.

**Gate persistence.** Once a `⏳ GATE:` line is emitted, every subsequent response — including discussion, clarifications, and refinements — must end with the *same* gate line, verbatim, until the gate actually moves. The gate stays "on" between turns; re-emitting it is mandatory, not optional. Update the line only when the gate's content actually changes (e.g., a blocker emerges, or `Next` has to be revised); when updating, emit the new line in full at the end of that response. Do not paraphrase, shorten, or silently mutate the line across turns.

**No fabricated gates.** `⏳ GATE:` lines only appear at gates this `## Gates` section defines or at a properly emitted blocked gate. Do not invent new gate categories or labels to describe discussion state, partial completion, or intermediate review. If a `⏳ GATE:` line is needed that this guide doesn't define, that's a signal the guide is missing a gate — file it as a process improvement.

Use these standard gate lines:
- Planned gate: `⏳ GATE: Next: <what happens after your response>. Say "next" or what to change.`
- Blocked gate: `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

Planned gates are the expected review points of this workflow. At each planned gate:
1. Summarize what you did and what should happen next.
2. End with the planned gate line.
3. STOP and wait for the supervisor.

In the planned gate line, `<what happens after your response>` should describe what the agent will do after the supervisor gives advance intent. If the gate is non-standard, make it describe the exact supervisor response or handoff needed to resume the workflow.

If an unexpected blocker prevents continued work, use the blocked gate line and STOP until the supervisor resolves it.

Planned gates for this workflow:
- After reporting what changed (changelog summary or `git log` fallback), but before running the adapter install/update runbooks.
- New components gate: when the host has a project config and the target adds optional components it
  has never seen (`newComponents` from the resolver), after the changelog gate and before the
  runbooks. `Next` opens the configure app; the supervisor may instead answer inline, naming which
  to enable and which to skip, and the installer records that through the configuration tool
  without opening the app.
  - `⏳ GATE: Next: Open the configure app to choose among <N> new components (<labels>). Or say which to enable or skip.`

Workflow-specific blocked gates:
- All of `skai/install-state.local.json`, `skai/install-state.json` and legacy `docs/skai/install-state.json` are missing, so the update workflow does not know what was previously installed.
- The default (latest release) target is requested but the submodule has no `v<N>` release tag.

## Advance intent

Advance intent moves past the current gate. Common signals: "next", "continue", "go ahead", "do it".

Rules:
- Recognized as approval to move past a gate only after you output a `⏳ GATE:` line.
- "we should...", "let's..." = discussion/context-setting, NOT authorization.
- Outside a gate, interpret "begin"/"next"/"continue" using the workflow's active-step rules below. Do not use them to skip required prerequisite checks.

`auto` = advance intent that bypasses planned gates only. Blocked gates always require explicit supervisor resolution.
`auto to <milestone>` = auto-advance but STOP before the named planned gate. Use stable, workflow-specific milestone names.

Progress tracking:
- This workflow currently uses inline discussion rather than a required work document.
- The active state lives in the conversation plus the discovered install-state file; adapter migration writes its resolved project or local state path.
- At the changelog-review gate, STOP after summarizing what changed and wait for approval before re-running adapter runbooks.

Workflow-specific advance behavior:
- `auto` may bypass the changelog-review gate and continue directly into the adapter runbooks.
- `auto` bypasses the new-components gate by enabling every new component (through the
  configuration tool) and naming them in the completion message. A default host (no project config)
  has no such gate: additions install as defaults, and are named at completion the same way.
- `auto` does not bypass the blocked missing-install-state or no-release-tag cases.
- Use `runbooks` as the stable bounded-auto target for this guide.

## Prerequisites

- Local `skai/install-state.local.json`, project `skai/install-state.json` or legacy `docs/skai/install-state.json` must exist (created by the initial install).
  - If all are missing, STOP and tell the supervisor to run the initial install/update runbook for each adapter first.

## Procedure

### 1. Read the install state file

Read `skai/install-state.local.json` when present; otherwise `skai/install-state.json`, otherwise
legacy `docs/skai/install-state.json` and record its canonical path migration. Malformed/unreadable
state blocks rather than implying absence. Preserve the chosen state path for later writes. Extract:
- `submodulePath` (default: `Submodules/skai`)
- `lastSHA`
- `lastRelease` (the `v<N>` the host is currently on; may be absent on installs that predate release targeting)
- `lastUpdatedAt`
- `installedAdapters` (list of adapter entries with `runbook` paths)

### 2. Choose the update target

Default to the **latest release** -- the highest `v<N>` tag. Use a different target only when the supervisor names one:

| Supervisor says | Target |
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

If the default is requested but no `v<N>` tag exists, STOP with a blocked gate -- there is no release to target yet (the supervisor can re-run naming a branch head or commit).

### 3. Check whether an update is needed

Keep recorded `lastSHA` as the prior installation/migration baseline; it does not prove the
checkout's current version. Read the actual checkout HEAD:

```sh
git -C "<submodulePath>" rev-parse HEAD
```

Compare that HEAD to the target SHA. Skip only step 4's checkout when they match. A failed update
may have changed HEAD without advancing installation state, so use the recorded version separately
for changelog/artifact migration checks. Continue actual component reconciliation regardless of
SHA equality. Use `Install/component-history.md` on every reconciliation; component baselines may
be older than the recorded adapter/global SHA. Never advance install state merely from a checkout.

### 4. Update the submodule

Check out the target in the submodule:

```
git -C <submodulePath> checkout <target-sha>
```

The host repo's submodule pointer now references the target; the supervisor commits that pointer change as usual.

### 5. Report what changed

- Read `<submodulePath>/CHANGELOG.md`.
- For a release target: show every `## Release <N>` section newer than the host's installed release (`lastRelease` from state; if absent, fall back to entries dated **after** `lastUpdatedAt`). These sections are written for this step -- they state the asset renames/moves, additions/removals, and re-run needs the adapters must apply.
- For a branch-head or commit target: show `## Unreleased` plus any `## Release <N>` sections in the `<oldSHA>..<newSHA>` range; if none apply, show `git log --oneline <oldSHA>..<newSHA>`.
- Gate: STOP after reporting what changed and end with `⏳ GATE: Next: Run the installed adapter update runbooks. Say "next" or what to change.`

### 5b. Offer new components

Resolve each installed adapter's effective selection with the current checkout
(`Install/component-selection.md`) and collect `newComponents`. If the host has a project config and
the list is not empty, STOP at the new-components gate above. On `next`, launch the configure app in
agent mode as `Guides/Core/configure-skai.md` describes; on an inline answer, write the choices with
the configuration tool's `--enable` / `--decline` flags. Under `auto`, enable them all. Then
continue; the runbooks install whatever the config now selects.

### 6. Run adapter install/update runbooks

For each entry in `installedAdapters`:
- Read `Install/component-selection.md` from that checkout, resolve the active host's current config, then read the adapter runbook at `<submodulePath>/<runbook>` and execute it, including actual inventory/reconciliation.
- Run them sequentially (one adapter at a time).
- Each runbook's migration-capable algorithm handles any necessary updates (new skills, changed policies, deprecated artifacts, etc.).

### 7. Update install state

Update the resolver's active `historyStatePath` with:
- The new submodule HEAD SHA
- `lastRelease`: the `v<N>` tag updated to (leave null for a branch-head or commit target)
- Today's date (run `date +%Y-%m-%d` -- see `Install/managed-header.md`)
- Per-adapter `lastRunAt` timestamps and `lastSHA` provenance
- Verified config fingerprint and component history under `Install/component-history.md` when
  tracking applies; retain disabled components' last applied versions. Keep local effective
  history in gitignored local state, preserving shared state and other adapter entries.

Before the completion line, name every optional component this update installed that was not
installed before (new to the catalog or newly enabled), and any the supervisor declined, so the
change in what the agent can do is visible in the transcript. Then complete the workflow.

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/update-installation-guide-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Once the lookup is done
and before work, report `- 📖 SKAI guide: update-installation-guide`, nesting `- 📎 Addendum loaded` under it only if one
loaded. If the lookup fails, nest `- ⛔ Addendum lookup failed: <what failed>` and stop. Report each guide
once per task; one addendum line covers referenced documents. Not a gate; keep GATE lines last.
