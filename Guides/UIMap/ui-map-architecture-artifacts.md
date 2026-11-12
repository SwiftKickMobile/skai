Managed-By: skai
Managed-Id: guide.ui-map-architecture-artifacts
Managed-Source: Guides/UIMap/ui-map-architecture-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-11

# UI Map Architecture Artifact Formats

Print `📖 SKAI guide: ui-map-architecture-artifacts` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

The typed formats the architecture skill produces and consumes. This is the consumer-facing layer: a downstream reader resolves any field or value here without reading the authoring method ([`ui-map-architecture.md`](ui-map-architecture.md)). For the YAML map format itself, see [`ui-map-guide.md`](ui-map-guide.md).

A change package lives at `skai/changes/<change-id>/ui-map/` in the repo that holds the production map. It holds the proposed map (`proposed-ui-map.yaml`), its render (`proposed-ui-map.html`), and the architecture artifact (`ui-map-architecture.md`) — whose `## Map Changes` section lists **map change items**. A **change request** against it is the `ui-map/` sub-package of a request folder, `skai/changes/<change-id>/changes/CR-<id>/ui-map/`, with the same files; its base and promotion are [`change-requests.md`](../Core/change-requests.md)'s. The type folder owns all map artifacts, evidence and working documents (`working-docs/`);
related product specs work stays in its independent sibling folder. After successful map promotion,
this complete package moves to its promoted destination (`skai/promoted/<change-id>/ui-map/` for a change's own), including any unchecked Plan
implementation work. Historical citations and downstream plan execution use that promoted path.
End the architecture artifact with append-only `## Decision Log`: `- <ID> decided|gap|reopened — <one line>` per Discussion state change. An open **Gap** item marks a placeholder in the proposed map, or that none exists ([`known-gaps.md`](../Core/known-gaps.md)).

Implementation-side artifact formats (code change items, build evidence) live in `ui-map-implementation-artifacts.md`; the architecture skill does not need them. Implementation reads both references — it consumes map change items defined here and authors its own formats defined there.

## Map change items

`## Map Changes` in the architecture artifact lists exactly the differences between the base (the frozen production map, or a request's base package's proposed map) and the proposed map, every difference, one entry per scene or domain, grouped under a `### <domain>` heading per domain in the map's order (`common:` scenes under `### common`, last), entries in the map's scene order:

```
### <domain>

- M<n> <Type>: <identity>
  - **Description** what changes, 1-2 lines.
  - **Justification** <why the change is needed>; <Source>: <reference>
```

- **Identity** — the one scene the entry changes, by ID (in backticks when it holds a space), or the domain for a domain's own change; a change to several scenes is several entries. A route entry's identity is the scene it starts from, and its text names the target. A moved scene sits under its new domain, and its text names the old one; a renamed scene's identity is its new ID, and its text names the old one. A removed scene sits under its old domain, with its former ID, after that domain's other entries.
- **One entry per scene.** Adding or removing a scene is its entry's whole change. A scene changed in several ways (moved and rerouted, or a route and an attribute) takes one entry whose numbered sub-changes replace Description and Justification, each a change and its reason, as Design Changes does; its type is `move scene` when it moved, else `modify scene`:

  ```
  - M04 modify scene: note_editor
    - **01** The Tag Picker opens as a sheet instead of a pushed screen — tags are a side task; Resolved decision: D02
    - **02** Its note says autosave runs on every edit — the design shows no Save button; Upstream requirement: [EDIT-03]
  ```
- **Gaps** — only inherited gaps get footnotes, one each, on the first entry or sub-change whose change rests on its placeholder ([`spec-file-gaps.md`](../Core/spec-file-gaps.md)); this package's own gaps are Discussion items.

- **ID** — `M1`, `M2`, ...: the first list's IDs run in document order; a later entry takes the next unused ID wherever map order places it. Never renumbered or reused, so cross-references stay stable across revisions. The ID identifies; it does not order.
- **Type** — `<operation> <element>`.
  - operations: `add` | `remove` | `move` | `modify`
  - map elements: `domain` | `scene` | `route` | `scene-attribute`
- **Source** (the token after the reason) — one of: `Upstream requirement` | `Supervisor input` | `Resolved decision` | `Agent proposal` | `Guide convention` | `Project convention` | `Map` | `Migration mapping` | `Change request`. A Justification is a reason a reader follows without opening anything, then its source. `Resolved decision: D#` cites a resolved Discussion item — the `D#` item's Decision line shows whether the outcome was supervisor-directed, approved as proposed, or revised. `Agent proposal` is an agent-originated map choice that did not go through Discussion. `Project convention` means the project's README or equivalent project-conventions doc is the authority.

  ❌ `- **Description** add scene share_sheet under notes` / `- **Justification** Resolved decision: D01`
  ✅ `- **Description** A note gains a Share sheet, opened from its toolbar and dismissed back to the note.` / `- **Justification** Sharing is a side task, not a place in the note's flow, so it opens as a sheet; Resolved decision: D01`

Items carry no checkbox: the change is realized by the proposed map and render that accompany the section. After a request folds into its base, the base's recomputed list cites the request on each difference it brought: `; Change request: CR-<id> M<n>`.

## Project Addendum

If `<active-project-root>/skai/addenda/ui-map-architecture-artifacts-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
