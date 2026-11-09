# Component configuration and reconciliation

Read this shared installer contract on every install, update or reconfiguration. The installer is
responsible for matching SKAI-owned installed collateral to the **current** project configuration.
The bundled Mac app writes configuration only; it does not install or remove collateral.

## Desired components

The active host project's `skai/config.json` is project-owned desired state:

```json
{
  "schemaVersion": 1,
  "components": ["skill.skai-debugging", "policy.error-handling"]
}
```

`components` is an explicit list of optional skill/policy asset IDs from `assets.manifest.json`.
An empty list selects none. Unlisted optional components, including future additions, are disabled.
**Only an absent file selects everything**, preserving the previous adapter/stack eligibility rules.
Known retired IDs listed in the manifest are ignored, not offered in the checklist; drop them when
next saving that config scope. All other unknown IDs block. Invalid JSON, unsupported schema,
unknown/duplicate IDs or an unreadable configuration block;
never treat them as absence or fall back to installing everything.

## Local user overrides

`skai/config.local.json` is gitignored, per-user desired state for this working copy:

```json
{
  "schemaVersion": 1,
  "overrides": {
    "skill.skai-debugging": true,
    "skill.skai-ui-map-architecture": false
  }
}
```

Only explicit overrides are stored. Missing key means **Use project setting**, `true` means **Turn on**,
`false` means **Turn off**. Never generate inherited keys or write null/default entries. The app has
Project and User tabs; Save commits only layers whose settings changed, preserving
unrelated JSON keys. Local-only edits never rewrite/create project config. Empty overrides restore
project choices; a missing project config still supplies all applicable defaults.

Effective selection is project/default choice, then explicit local on/off, then required support
always included and adapter/stack eligibility applied. Required components cannot be overridden.
Invalid/unreadable local config blocks, just like project config. Local settings may enable work on
shared collateral; that is the user's chosen configuration, with existing ownership/collision rules.

All adapters put `/skai/config.local.json`, `/skai/install-state.local.json` and `skai/working-docs/` in their
SKAI-managed `.gitignore` block; session working documents are not committed. Configure ensures the two local entries before launch so local files stay ignored even
if installation after Save fails. Preserve surrounding ignore content; don't add local files to
agent-ignore files (the installer must read them). Existing accidentally tracked local files need
an explicit untracking decision; ignore rules alone cannot untrack a file.

Read [Component history and migrations](component-history.md) on every reconciliation, including
removals without custom configuration. Use the resolver's `historyStatePath`; local effective installation
history remains gitignored, while project state describes the project configuration.

Manifest `label`, `description` and `category` fields describe checklist entries. Assets with
`installRole: required` are administration support, always installed for their adapter so the
project can be reconfigured even with no optional skills selected. The bundled app is read from the
SKAI checkout and is never a deselection candidate. Integration, instruction-block
structure, install state and ignore-block support also remain installer infrastructure. Guides in
the SKAI checkout remain available as references; component selection controls host-installed
wrappers/policies, not access to source guides or project artifacts.

Resolve the effective selection with the current checkout, established project stack and adapter.
On macOS, use the bundled executable in read-only mode (it opens no UI):

```sh
"<skai-root>/Bin/SKAIConfigure.app/Contents/MacOS/SKAIConfigure" --project-root "<host-project-root>" --skai-root "<skai-root>" --resolve --adapter <codex|cursor|claude-code> --stack <generic|swift|android>
```

On other platforms, the read-only standard-library helper returns the same effective sets:

```sh
python3 "<skai-root>/Bin/skai-configuration.py" --project-root "<host-project-root>" --resolve --adapter <codex|cursor|claude-code> --stack <generic|swift|android>
```

Exit 0 returns `skills` and `policies` with stable IDs/source paths, plus `newComponents` (see
below). Exit 2 is a configuration/catalog failure. Required administrator skills are included;
policies use existing core/Swift applicability. Use these resolved sets rather than installing every
adapter-tagged skill or every policy.

## New components

A component is **new** to a host when it is in the manifest, eligible for the adapter and stack,
not listed in `skai/config.json`, and absent from the adapter's component history (never installed,
disabled or declined; see [`component-history.md`](component-history.md)). Both resolvers return
them as `newComponents`. With no project config nothing is new in this sense: defaults select
everything eligible, so an update installs additions and the installer reports them at completion.

With a project config, the installer never enables a new component silently. Under `auto` it
enables every new component and reports them at completion; otherwise it stops at the update
guide's new-components gate, where the supervisor opens the configure app or answers inline. Either
way the choice is written through the configuration tool, not by editing JSON:

```sh
"<skai-root>/Bin/SKAIConfigure.app/Contents/MacOS/SKAIConfigure" --project-root "<host-project-root>" --skai-root "<skai-root>" --enable <id>[,<id>] --decline <id>[,<id>]
python3 "<skai-root>/Bin/skai-configuration.py" --project-root "<host-project-root>" --enable <id>[,<id>] --decline <id>[,<id>]
```

`--enable` appends the IDs to the project config's `components`, preserving unrelated keys; it never
creates a config on a default host. `--decline` records the IDs as declined in the adapter's
component history so they stop counting as new. Unknown or ineligible IDs exit 2. In the app, new
components appear in a **New** section at the top of the list until Save, which moves selected ones
into the config and records the rest as declined.

## Installed wrapper paths

Shared skill templates use the default `Submodules/skai/` prefix. When copying a resolved skill,
substitute the discovered checkout path, relative to the host root, for that prefix throughout
its references. Stamp `Managed-Source` using the same actual checkout and sourcePath. Keep source
templates, stable skill IDs and adapter markers unchanged. Do not create a second checkout just
to satisfy the template's default path.

## Reconcile, do not assume

1. Read both actual configuration layers and prior install history before advancing any SHA. Read the actual configuration and inventory the current adapter's SKAI-managed files/blocks.
   Do this on every invocation, even when source SHA, config selections or recorded install state
   appear unchanged. State is a record, not proof that installed files still match.
2. Use `component-history.md` to snapshot/persist known component versions before removal and
   identify enabled components' migration ranges, including re-enablement at the same global SHA.
   Prepare a concrete plan: create missing selected outputs, refresh changed selected outputs,
   remove deselected or retired managed skill/rule outputs, and recompose managed policy blocks with only the
   selected/applicable policies. Keep the fixed infrastructure. Read source dependencies as needed;
   do not silently enable optional components the user did not select.
3. Present the reconciliation plan. The Mac app's **Save and Apply** authorizes reconciliation
   of its selected components, including deselected SKAI-managed collateral; it does not authorize
   deleting unmarked lookalikes, custom content, project addenda, Integration values, canonical
   product specs/maps, or whole project-owned instruction files. Report conflicts and obtain their
   separate resolution. For a verified agent Save and Apply or explicit request to apply saved configuration, proceed
   with component reconciliation; do not ask the supervisor to approve that same work again. Reuse the established project stack if repo
   signals agree. Ordinary install/update requests retain their existing plan approval.
4. Execute each adapter within its ownership scope. Delete a deselected skill's managed SKILL.md
   or managed Cursor rule only after verifying SKAI's marker/id/adapter. Remove only empty managed
   directories; retain other files/custom resources and report any conflict. Recompose AGENTS/CLAUDE
   content only inside the existing SKAI block, preserving all surrounding project text.
5. Complete relevant component artifact migrations, re-read both config layers, then verify the
   actual managed inventory/content matches its
   resolved skills/policies and required infrastructure. If config changed during execution,
   resolve and report the changed plan; continue only work covered by the existing approval and
   use the existing approval/blocker route for changes outside that scope. Do not record success
   against stale configuration. On failure report what remains; don't mark
   that adapter successfully reconciled. Record verified history/fingerprint under `component-history.md`;
   retain disabled component records. Preserve other adapters' state entries.

Reconfiguration runs every installed adapter in the active install state, sequentially. Follow
`component-history.md` discovery: local state, shared state, then legacy `docs/skai/install-state.json`.
Malformed/unreadable state blocks; it is not an absent installation. Legacy relocation follows
`conflict-precedence-policy.md`; discovery does not move or merge files.
Without an installation state, enter the existing initial-install adapter selection flow. Config
never causes another adapter's files to be inventoried/deleted by the wrong adapter.

## Updates and local data

No host config is generated automatically by installation. The Mac app or project owner creates it.
Preserve both config files, unrelated config keys, disabled component history, project-owned
instructions/Integration and all `skai/addenda/`
content. An older host without config keeps the full eligible installation. A config-only change,
missing selected output or leftover deselected output requires reconciliation without a new SKAI
commit. Do not skip because `lastSHA` already equals the selected update target.

The compiled Mac app ships in the SKAI repo at `Bin/SKAIConfigure.app`; agents launch that bundle
directly from the installed checkout. Users do not build or install a separate app. Maintain the
prebuilt bundle alongside its source. Developer ID signing/notarization is a separate packaging
choice, not a prerequisite for the Git-based SKAI release. Existing hosts without config need no
config migration and retain all eligible optional components plus configuration support.

Agent launch uses `--agent-session`. Save and Apply closes immediately and returns saved with
`launchMode: agent` and `reconcile: true`. No acknowledgement dialog delays reconciliation.
Without the flag, standalone Save stays open, reloads the saved baseline and displays a dialog asking
the user to tell an agent to apply the choices. Its saved events carry `reconcile: false`; a later
explicit apply request authorizes reconciliation without reopening the picker or changing version.
