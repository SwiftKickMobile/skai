Managed-By: skai
Managed-Id: guide.ui-map-implementation-artifacts
Managed-Source: Guides/UIMap/ui-map-implementation-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-06

# UI Map Implementation Artifact Formats

The typed formats the implementation skill produces. Read an artifact with [`ui-map-implementation.md`](ui-map-implementation.md) for Mode and control flow, the platform guide named in its `## Inputs`, and [`ui-map-guide.md`](ui-map-guide.md) for the YAML map. The architecture-side formats the implementation skill *consumes* (map change items) and *raises* (change requests) live in [`ui-map-architecture-artifacts.md`](ui-map-architecture-artifacts.md).

The implementation artifact (`ui-map-implementation.md`) sits in the change package at `skai/changes/<change-id>/`, parallel to the architecture artifact. Its `## Code Changes` section lists **code change items**; its `## Evidence` section holds **verification evidence**.

## Code change items

`## Code Changes` lists one entry per source unit under `Realizes`: one applicable `M#`, one `D#`, or one audit finding without an ID. Do not split one source unit across multiple `T#` items or merge multiple source units into one item. When a source unit describes several operations, keep them together in the Description and leave its checkbox unchecked until every operation is complete. The terminal promote item is the sole exception: it realizes the approved change as a whole. Each entry:

```
- [ ] T<n> <identity>
  - **Description** what changes in the code.
  - **Disposition** implement | placeholder | planned | handoff
  - **Realizes** <what this item carries out — see below>
  - **Touches** files / folders / types affected
```

- **ID** — `T1`, `T2`, ... assigned in document order, never renumbered or reused, so the production skill can cite an item by a stable handle.
- **Checkbox** — actual completion state. Write every item unchecked (`- [ ]`) at the Code Changes-ready gate. Check it (`- [x]`) only when the code or artifact state described by the item is true. A later workflow may check a `planned` or `handoff` item after completing or verifying it; it preserves the item's ID and Disposition.
- **Disposition** — who owns the item and how it is treated; it does not change when the checkbox changes:
  - `implement` — UI Map implementation owns the item: either a mechanical, non-placeholder code change executed in Build, or the terminal promotion executed when a proposed map exists.
  - `placeholder` — UI Map implementation owns placeholder or navigation scaffolding and executes it in Build. Check the item when the scaffold is complete; later productionization is separate work.
  - `planned` — UI-map-owned work intentionally not executed because the run is Plan; the receiving workflow should implement and check it using the UI Map and platform guides.
  - `handoff` — concrete, verifiable work outside UI Map implementation ownership that directly affects UI Map conformance; the required outcome is already defined, and another workflow, skill, person, or PR owns and checks it. Missing guidance or an unmapped value is not a handoff; it blocks before Code Changes.
- **Description for `planned` / `handoff`** — include what remains, why this run is not doing it, and the relevant UI Map/platform guidance or constraints the receiving workflow must preserve. A `handoff` Description must define enough of the expected outcome to decide when its checkbox is true.
- **Realizes** — what this item carries out, so each code change traces back to the map: an `M#` from the architecture change list, a `D#` discussion decision, a short description of the audit finding when it has no ID, or — for the terminal promote item — the approved change as a whole rather than a single `M#`.

There is no `Type` field: the identity and Description convey the kind at a glance (e.g. `T3 move pantry/ → inventory/`, `T5 scaffold edit_item`). Items are written top-down in structural order: any shared, cross-scene item (e.g. a generated `DomainColors`) **first**, then per domain → scene → route, mirroring the map.

## Verification evidence

`## Evidence` records the verification trail: build checks at chunk boundaries and completion, plus the official render performed by a terminal promote item. One bracket per check:

```
[evidence: <command>; exit <code>; output: <path when persisted>]
```

On failure, persist and link the full output, so `output` is required. On success, `output` is optional when no output was persisted. The evidence brackets are the durable record that conformance and promotion were verified, not asserted.
