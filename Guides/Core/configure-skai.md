Managed-By: skai
Managed-Id: guide.configure-skai
Managed-Source: Guides/Core/configure-skai.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-10

# Configure SKAI

Before using this guide, complete [Project addendum](#project-addendum) loading below.

Launch the bundled Mac app to choose optional skills and policies for the active host project.
The app saves project-owned `skai/config.json` and sparse gitignored `skai/config.local.json`
overrides; the installer applies the effective selection and checks retained component migration history.
The configure skill and app remain available even when every optional component is disabled.
If the request explicitly asks to apply an already saved configuration, skip Launch and the UI gates;
use the explicit-request case under Reconcile after Save. Otherwise open the picker.

## Gates

The supervisor is the human or authorized agent outside this workflow who chooses components;
the executing agent never approves its own selection. Every response while waiting on the supervisor
ends with the same applicable `⏳ GATE:` line, verbatim, until the state changes. Do not invent gates.

The planned gate is a **hard UI choice gate**:
`⏳ GATE: Next: Choose components in the Mac app, then Save and Apply or Cancel.`

Here Next describes the supervisor's UI action, not a chat command. Project/User drafts are the
review artifact: agent-mode `ready` means pending choice, final `saved` means config committed
and app closed, and `cancelled` means abandoned before Save. These states replace process TODO
markers; checkboxes represent desired components. Save and Apply commits the selection and
authorizes component reconciliation; no additional confirmation or acknowledgement is required.

Blocked conditions use `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`
Stop until resolved; preserve separate installer gates for unmanaged conflicts and unrelated cleanup.
Completion uses `🏁 Complete. Let me know if anything needs adjustment.` after reconciliation succeeds,
or after an explicit Cancel (state clearly that configuration and installation are unchanged).

## Advance intent

Chat `next`, `continue`, `go ahead`, `auto` or `auto to` cannot select components or bypass the hard
UI choice gate. `auto` may continue authorized installer work after Save; blockers still require
resolution. While the app is open, keep the command session alive and wait for its final JSON event
using bounded tool waits. Stay in the active agent turn so Save and Apply automatically resumes installation;
show the UI gate line in waiting updates. If the harness interrupts or ends the turn, report that
resumption is needed rather than claiming automatic completion.

## Launch

Resolve the active host root and SKAI checkout from project context and install state using
[`component-history.md`](../../Install/component-history.md) discovery: local, shared, then legacy
`docs/skai/install-state.json`. Malformed/unreadable state blocks; it is not an absent installation.
Do not configure the dependency checkout merely because this guide lives there. Read
[`component-selection.md`](../../Install/component-selection.md) for selection and ownership rules.
Before launch, ensure `/skai/config.local.json` and `/skai/install-state.local.json` are ignored in
this host's SKAI-managed `.gitignore` block, preserving all surrounding text. This configuration
request authorizes that minimal ignore setup. If a local file is already tracked, obtain an explicit
untracking decision; never remove it from Git silently. The app refuses local Save in a Git repo if
these local paths are not ignored. Read local settings normally; do not put them in agent-ignore files.

This prototype requires an Apple Silicon Mac running macOS 13 or later and the bundled app.
An unavailable app/platform or
invalid/unreadable configuration blocks; never reset config or silently install everything.

Launch the executable directly through the harness's local command tool, with resolved paths:

```sh
"<skai-root>/Bin/SKAIConfigure.app/Contents/MacOS/SKAIConfigure" --project-root "<host-project-root>" --skai-root "<skai-root>" --agent-session
```

The app has **Project** and **User** tabs, with the explicit override count in the User
label. Bulk actions are in the compact **⋯** menu beside the tabs. No layout flag is needed.

The explicit `--agent-session` flag declares the agent launch contract; do not infer it from
parent process names. Verify the `ready` event has `launchMode: agent`. Without that flag the app
uses standalone mode, even when invoked from a terminal. An unexpected mode is a launch error;
resolve it rather than treating a standalone save as the automatic installer handoff.

Use a persistent command session (or equivalent) to capture output and exit status; do not launch
via `open`, detach the process, or infer completion from the window disappearing. Direct execution
opens the native window, prints a `ready` JSON event, and remains running while the supervisor chooses.
No browser, web server, custom URL scheme, Playwright, or runtime Xcode installation is needed.

No project config checks all optional entries; an existing project config checks only its selection.
The **Project** tab uses ordinary checkboxes. The **User** tab uses three-state checkboxes:
checked is Turn on, unchecked is Turn off, and dash is Use project setting. Click to cycle states;
a category dash also represents mixed member settings. Inherit omits the key; on/off are explicit
booleans in local config. Overridden rows have blue **User: On/Off** labels on Project and
**Project: On/Off** labels on User, showing the other setting’s value;
on User, inherited component names are subtly dimmed, as are categories with no overridden
components. A category retains normal contrast when any child is overridden on or off. Rows show
the component name, description and any override badge. Required Configure SKAI cannot be changed in either tab.
In the **⋯** menu, Select all/Clear optional affect project choices when Project is selected;
Turn all on/Turn all off affect User overrides when User is selected. Use project settings clears
User overrides. Drafts persist when switching tabs.

The agent-mode button is **Save and Apply**; standalone mode uses **Save**. Either is disabled until
its drafts differ from the opening/saved baseline and disables again when all edits are reverted.
Save writes only changed layers, preserving unrelated keys; local-only edits do not create/rewrite
project config. Saving checks both files and the catalog for outside changes and writes atomically
with rollback on a failed second-layer write. Errors keep the app open.

In agent mode, Save and Apply closes immediately and returns final `saved` with `launchMode: agent`
and `reconcile: true`. Cancel, window close and Quit before Save discard drafts without config/install
changes. No confirmation dialog intervenes between a successful Save and the agent handoff.

In standalone mode, Save commits config, reloads it as the new editing baseline and shows a dialog:
“Apply the saved SKAI configuration for this project.” The user must ask an agent to apply it. OK
returns to the checklist, with Save disabled until further edits. Standalone saved events have
`launchMode: standalone` and `reconcile: false`; they are not an automatic installation handoff.
Close/Quit preserve earlier successful saves and discard only later unsaved edits.

## Reconcile after Save

An agent-mode final `saved` event names the project/config and has `reconcile: true`. Verify it
matches the launched host, has `launchMode: agent`, and read both actual config layers. A local-only
Save may leave project config absent: that means all project defaults with explicit local overrides.
Do not treat `ready`, a standalone saved event, process interruption, a nonzero exit or window
disappearance as an agent-mode Save. On `cancelled`, stop without running the installer. An
interruption with no final event is unresolved; obtain supervisor resolution before applying.

After a standalone Save, wait for an explicit request to apply it. When the supervisor asks to apply an already saved configuration,
resolve/read the current host config and active history, then execute the same reconciliation below.
That explicit request approves the component changes; don't reopen the picker or invoke the
version-update skill merely to apply the saved choices.

For an existing installation, run every adapter in the state discovered above sequentially,
using its runbook from the **current checkout**, in full. Do not invoke the version-update skill,
fetch releases, switch the SKAI checkout or stop because SHA/selections are unchanged. Read
[`component-history.md`](../../Install/component-history.md) for per-component versions, pre-removal
baselines and migration checks on re-enablement, including at the same global SHA. Ordinary installation updates also reconcile actual collateral when config is unchanged. Without install state, use
[`install-update.md`](../../Install/install-update.md) to choose initial adapters.

Save and Apply supplies approval for selected/deselected SKAI-managed component reconciliation.
Report the concrete plan and proceed without another approval for that work; unrelated migrations,
unmanaged conflicts and custom-file cleanup retain their separate gates. The app does not own
installed collateral. If installation fails, retain saved desired state, report incomplete work,
and rerun reconciliation after resolution. Do not record successful state for a failed adapter.

Report the saved path, adapters reconciled and any remaining conflicts. Complete only after actual
inventory and required component migrations match effective config. User overrides can enable
migrations of shared collateral under the ordinary ownership/collision rules; no extra approval
is needed solely because the selection came from a local override. No commit, push or release is implied.

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/configure-skai-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Before work, report
`📎 ADDENDUM: <project-entry filename> — loaded` or `No project addendum found: <project-entry filename>.`
Report only the project entry, not each referenced document. Receipt is not a gate; keep GATE lines last.
