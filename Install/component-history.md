# Component history and migrations

Read on every reconciliation. Installations with no project config, no explicit overrides,
no previous history and no component removals need no component ledger. Customization or any
managed component removal starts a full ledger, including default, eligibility or retirement changes.
An empty local overrides map alone does not start a ledger, but retains one already recorded.
The resolver’s `trackComponents` flag signals customization; it never permits skipping history
before a managed removal. The planner also starts tracking whenever actual inventory loses a component.
Keep existing installation metadata; record each adapter's `lastSHA` on successful installation so a later customization has a reliable
version baseline. A top-level SHA alone is insufficient after independent adapter updates.

## State ownership

Use the selection resolver's `historyStatePath`:

- Project config only, or defaults never customized: `skai/install-state.json`.
- A local config/state exists: gitignored `skai/install-state.local.json`. On first local use, seed
  from shared install state, preserving adapter entries and component version evidence. All subsequent
  actual effective-installation records go to local state; do not publish the user's effective choices
  or overwrite the shared state with them. An empty local overrides map still retains local history.

Discovery reads local state first when present, then shared state (then the old `docs/skai` path).
Malformed/unreadable state blocks; it is not an absent installation. Preserve unrelated state keys
and other adapters. Config is desired state; history describes successfully applied work.

## Adapter record

When tracking starts, extend that adapter's existing record:

```json
{
  "adapter": "codex",
  "runbook": "Install/Codex/install-update-codex.md",
  "lastRunAt": "2026-10-09",
  "lastSHA": "<current-checkout-sha>",
  "configurationFingerprint": "<resolver-fingerprint>",
  "componentHistory": {
    "skill.skai-debugging": {
      "installed": false,
      "lastAppliedSHA": "<version-N-sha>",
      "lastAppliedAt": "2026-10-08",
      "lastDisabledSHA": "<version-N-plus-1-sha>",
      "lastDisabledAt": "2026-10-09"
    }
  }
}
```

The fingerprint covers project selection/default mode and explicit local overrides, excluding
unrelated config keys. Store it only after that exact effective selection is successfully applied.
Retain disabled and retired records indefinitely. Do not replace `lastAppliedSHA` with the version
at which a component was disabled. Returning to defaults does not erase existing history.

## Discover, migrate, record

1. **Capture before removal or state advancement.** Read previous state before updating its SHA.
   At first customization or any removal, snapshot every verified installed optional component into history using
   that adapter's prior `lastSHA`/`lastRunAt`. For a legacy install whose sole recorded adapter matches the
   adapter being reconciled, the existing global `lastSHA` and `lastUpdatedAt` may supply missing
   adapter version/date evidence. A sole different adapter
   or missing adapter attribution cannot prove that baseline. If mixed-adapter legacy state cannot prove a component version, record
   `lastAppliedSHA: null` and audit its artifacts; never invent a version or substitute the current
   checkout. Required configure infrastructure needs no optional-component record.
   Persist this baseline snapshot before removing any managed output, including when transitioning
   from defaults. This records prior evidence, not current success: leave prior version/fingerprint
   intact. A later failure must not erase the only record of a now-removed component.
2. **Find component migration work.** For every enabled applicable component, compare its own
   `lastAppliedSHA` with the target checkout, even if the global SHA/fingerprint is unchanged or its
   wrapper is missing. Read changelog upgrade instructions across that range and the affected guides;
   discover their existing artifacts in the host and any shared repositories. Apply relevant changes
   to existing artifacts, not just wrapper updates. Respect recorded completion evidence and verify
   already-applied transformations instead of repeating them. Unknown versions require an artifact
   audit against current conventions; being absent from history does not prove artifacts are new.
3. **Reconcile.** Apply desired wrappers/policies under the shared ownership rules. Disabling removes
   managed install outputs, preserves canonical/project artifacts and retains prior applied version
   evidence. A local override may enable migration of shared collateral: this is the user's chosen
   scope, with the same artifact ownership and collision rules as any installation. Do not add a
   separate approval solely because the enablement came from a local override.
4. **Record only verified success.** After relevant migrations and actual inventory checks succeed,
   set enabled components' `installed: true`, `lastAppliedSHA` to target, and `lastAppliedAt` to today.
   On an enabled-to-disabled transition, set `installed: false`, `lastDisabledSHA`/`lastDisabledAt`
   while preserving last applied fields. Advance this adapter's `lastSHA` and fingerprint only for
   successful reconciliation. On failure, retain baseline evidence and report incomplete work;
   migration completion evidence belongs in its owning artifacts, not fabricated success state.

Thus A installed at N, disabled at N+1, then re-enabled at N+1 still requires the N → N+1 migration
check. A disabled for several releases catches up from its last applied version. Selected components
with known current versions still undergo actual inventory/content verification.

## Optional read-only planning helper

Prepare an inventory JSON from the adapter's verified pre-reconciliation managed outputs:

```json
{"components": ["skill.skai-debugging", "policy.error-handling"]}
```

The portable resolver can calculate migration ranges and **proposed** adapter history without writes.

The helper accepts current adapter identities only. For legacy Claude IDs (`jetbrains-claudecode`,
`xcode-claudecode`, `androidstudio-claudecode`), use the direct procedure above and the Claude
runbook's identity migration instead; the helper rejects those records. Preserve their evidence
through baseline capture and convert persisted identity only after verified success.

```sh
python3 "<skai-root>/Bin/skai-configuration.py" --project-root "<host-root>" --plan-history --adapter <adapter> --stack <stack> --inventory "<inventory.json>" --target-sha <checkout-sha> --date <today>
```

With `tracking: true`, `migrations` names enabled components with a version gap or unknown baseline.
With `tracking: false`, unchanged defaults use adapter-level provenance and the list is empty;
it does not establish that no artifact migration is needed. Still check the adapter’s prior version
against the target changelog and apply its relevant artifact migrations before recording success.
`baselineAdapterState` captures prior evidence; merge it before removals when new history is seeded.
`nextAdapterState` is a proposal, not evidence that migration happened. Merge it only after step 4;
preserve all other state fields/adapters. Without Python, apply the same schema/procedure directly.
