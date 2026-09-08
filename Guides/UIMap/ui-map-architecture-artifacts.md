Managed-By: skai
Managed-Id: guide.ui-map-architecture-artifacts
Managed-Source: Guides/UIMap/ui-map-architecture-artifacts.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-06

# UI Map Architecture Artifact Formats

The typed formats the architecture skill produces and consumes. This is the consumer-facing layer: a downstream reader resolves any field or value here without reading the authoring method ([`ui-map-architecture.md`](ui-map-architecture.md)). For the YAML map format itself, see [`ui-map-guide.md`](ui-map-guide.md).

A change package lives at `skai/changes/<change-id>/`. It holds the proposed map (`proposed-ui-map.yaml`), its render (`proposed-ui-map.svg`), and the architecture artifact (`ui-map-architecture.md`) — whose `## Map Changes` section lists **map change items**. The architecture skill also consumes **change requests** raised by downstream implementation. Both formats are defined below.

Implementation-side artifact formats (code change items, build evidence) live in `ui-map-implementation-artifacts.md`; the architecture skill does not need them. Implementation reads both references — it consumes map change items and raises change requests defined here, and authors its own formats defined there.

## Map change items

`## Map Changes` in the architecture artifact lists exactly the differences between the frozen official map and the proposed map, one typed entry per difference. Each entry:

```
- M<n> <Type>: <identity>
  - **Description** what changes. Single operation: 1-2 lines.
    Multiple operations of the same kind under one identity: a sub-list,
    one bullet per operation. Avoid prose that buries per-operation detail.
  - **Justification** <Source>: <reference or rationale>
  - **Touches** scenes / routes / map areas affected
```

- **ID** — `M1`, `M2`, ... assigned sequentially in document order and never renumbered or reused, so cross-references stay stable across revisions. The ID identifies; it does not order.
- **Type** — `<operation> <element>`.
  - operations: `add` | `remove` | `move` | `modify`
  - map elements: `domain` | `scene` | `route` | `scene-attribute`
- **Source** (the leading token of Justification) — one of: `Upstream requirement` | `Human spec` | `Resolved decision` | `Agent proposal` | `Guide convention` | `Project convention` | `Map` | `Migration mapping` | `Change request`. When the source is a spec, requirement, or change request, the Justification is just the citation. `Resolved decision: D#` cites a resolved Discussion item — the `D#` item's Decision line shows whether the outcome was operator-directed, approved as proposed, or revised. `Agent proposal` is an agent-originated map choice that did not go through Discussion, and carries a real rationale. `Project convention` means the project's README or equivalent project-conventions doc is the authority.

Entries are written top-down in structural order — domain-level changes first, then scenes, then routes — mirroring the map and the rendered diagram. Items carry no checkbox: the change is realized by the proposed map and render that accompany the section.

## Change requests

A change request is the artifact downstream implementation raises when code reality shows the approved map is wrong, incomplete, infeasible, or underspecified at the map-architecture level; architecture consumes it on reopen. Missing implementation guidance or an undefined map-to-code convention is not map underspecification and blocks in implementation Discussion instead. One markdown file per request:

`skai/changes/<change-id>/change-requests/ui-map-<nnn>.md`

It carries two fields as inline `Label: value` lines — a `Change Request Status` (exactly one of `Proposed | Incorporated | Rejected | Superseded`) and a `Reviewer Response` — above the free-form body that states the concern and the requested change:

```
Change Request Status: Proposed
Reviewer Response: <filled by architecture on reopen>
```

Lifecycle: the request opens `Proposed`; architecture's reviewer fills `Reviewer Response` and moves the status to `Incorporated` (only once the adjustment is applied in the proposed map in Map Changes), `Rejected`, or `Superseded`.
