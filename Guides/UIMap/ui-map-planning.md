Managed-By: skai
Managed-Id: guide.ui-map-planning
Managed-Source: Guides/UIMap/ui-map-planning.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-09

# UI Map Planning (Deprecated)

Before using this guide, complete [Project addendum](#project-addendum) loading below.

This compatibility guide has been replaced by the UI Map architecture/implementation split:

- Use [`ui-map-architecture.md`](ui-map-architecture.md) when the work creates or changes the `ui-map.yaml` architecture artifact.
- Use [`ui-map-implementation.md`](ui-map-implementation.md) when the work aligns app code to an approved `ui-map.yaml`, scaffolds placeholder navigation, records checklisted planned/handoff work, or raises a UI Map change request.

New installations should use the `skai-ui-map-architecture` and `skai-ui-map-implementation` skills. Existing references to UI Map planning should be routed to UI Map Architecture unless the request is explicitly about code alignment or scaffolding.

## Project addendum

Read this guide fully; check `<host-project-root>/skai/addenda/ui-map-planning-addendum.md` before use.
Host root means the active project. Read a present addendum and required shared addenda fully; resolve links
from their containing file. Apply shared rules, then local additions/overrides to guide defaults,
subject to task instructions/project policies. This guide owns Integration lookup. Unknown root,
lookup/read errors or missing required references stop; never infer absence. Before work, report
`📎 ADDENDUM: <resolved path> — loaded` for each file, or `📎 ADDENDUM: <resolved path> — none present`
for an absent host entry. Receipt is not a gate; keep GATE lines last.
