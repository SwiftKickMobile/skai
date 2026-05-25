Managed-By: skai
Managed-Id: guide.ui-map-figjam
Managed-Source: Guides/Dev/ui-map-figjam.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-05-24

# UI Map — FigJam Format & Migration (deprecated)

The FigJam diagram is the **deprecated** predecessor to the YAML UI Map format. This document is needed only when **migrating** an existing FigJam-based project onto the YAML system — it is not loaded for ordinary planning or implementation work. Companion to [`ui-map-guide.md`](ui-map-guide.md).

## FigJam diagram format

Each app has its own UI Map in FigJam. The diagram uses a fixed vocabulary of shapes, colors, and connector labels.

### Scenes

A scene is a discrete unit of UI that owns its own state and routes. A scene is usually a full screen, but it can also be a subview that owns routes of its own (e.g. a reusable player that can present its own modal).

A scene is drawn as a **rounded rectangle** labeled with the scene name, with two shape exceptions for reused and TODO scenes (see below). Color is used redundantly with shape, both as a visual hint for human readers.

- **Rounded rectangle, solid blue fill** — a scene that handles routing (has one or more outgoing routes).
- **Rounded rectangle, light blue fill** — a scene with no outgoing routes.
- **Hexagon, gray fill** — a scene defined elsewhere in the map and reused here. Hexagons are pointers; the canonical definition is wherever the scene is drawn as a rounded rectangle.
- **Octagon, pink fill** — a scene whose routing is a TODO (future scene, incomplete mapping, or pending routing refactor).

### Routes

A route is a **connector** between two scenes, labeled with the route kind:

| Label | Meaning |
|---|---|
| `Nav` | Parent pushes the child onto a navigation stack. |
| `Modal` | Parent presents the child modally. The diagram does not specify the modal presentation style; see [`ui-map-swiftui.md`](ui-map-swiftui.md). |
| `Child` | Parent embeds the child as its primary content. Switching child routes replaces what the parent renders. |
| `Tab` | Parent embeds the child as one tab in a tab container. |
| `Composite` | Parent embeds the child as a subview. The child is part of the parent screen, not a separate destination. |

### Wrappers

A wrapper drawn around one or more scenes is itself meaningful, not just visual grouping. Shape distinguishes the two wrapper kinds; stroke style is used redundantly as a visual hint.

- **Rounded rectangle, dashed stroke** — a set of *mutually-exclusive routes*. A connector terminating on the wrapper routes to exactly one scene inside at a time.
- **Manual-input shape, solid stroke** — a *composite parent*. The wrapper itself is never the target of a route; its children compose a single screen.

### Annotations

A right-leaning parallelogram attached to a scene carries one of:

- `Implements: A, B, C` — the scene is a single class with multiple concrete instances. Each name is an instance, distinguished by a construction-time parameter. For example, a `Web` scene annotated `Implements: Privacy Policy, Terms and Conditions` is one reusable web component; "Privacy Policy" and "Terms and Conditions" are two concrete instances distinguished by URL.
- `<Platform> only` (e.g. `Android only`) — the scene exists only on the named platform.
- Free text — a designer or developer note.

Sticky notes mark TODOs and known divergences between the map and the current implementation.

## Migration to the YAML format

A one-time, per-project conversion of a deprecated FigJam diagram into a valid `ui-map.yaml`. The human points the agent at this doc to run it; it is not part of ordinary planning or implementation. Migration produces the **map only** — it does not modify code or scaffold placeholders. It *reads* the code freely, though: the diagram is the structural source, and the code fills what the diagram can't carry (e.g. modal styles). A full code-vs-map conformance pass is a separate, later audit (`ui-map-planning.md`), not part of migration.

The hard part is **domains**: FigJam has no concept of them, but the YAML is organized around them (and the code folders mirror them). So migration is not a mechanical transcription — it pivots on a human-reviewed domain design. Everything else maps element-for-element.

### Process

Four steps, gated twice:

1. **Read the FigJam and understand the app.** Pull the diagram with the Figma MCP (`get_figjam`). Inventory every scene, connector (with its route-kind label), wrapper, and annotation. Read for *meaning* — you need to know what the app does to group it well, not just match name prefixes.
2. **Propose domains.** The design step FigJam can't supply (see *Designing domains*). Present the proposed grouping with a rationale per domain, then STOP.
   `⏳ GATE: Next: Domain proposal above. Say "next" to write the map, or tell me what to regroup.`
3. **Write the map.** With the approved domains, translate the rest element-for-element (see *Element mapping*) and read the code for what the diagram can't carry (see *Filling what the diagram omits*), then render and validate the map (the render and validate commands ship with the UI Map tooling). Fix until valid; never present an invalid map. Then STOP.
   `⏳ GATE: Next: Map drafted — map at <path>, render at <path>. Review both; say "next" to finish, or what to change.`
4. **Finish.** On approval: `🏁 Complete. <app> is migrated to the YAML UI Map.`

If the FigJam can't be read or is ambiguous — any scene, connector, wrapper, or annotation whose meaning isn't clear from `get_figjam` — a required command is missing, or any value the map needs can't be settled from the diagram or the code, STOP at a blocked gate; the human fixes the FigJam (or supplies the missing value) before you continue. Do not visually guess or infer past the ambiguity. `⏳ GATE: Blocked: <reason>. Resolve and say "next" to continue.`

**Advance intent** — "next" (also "continue" / "go ahead") moves past a planned gate, recognized only after a `⏳ GATE:` line; "we should…" / "let's…" is discussion, not authorization. Migration has no `auto`: both planned gates (the domain design and the final map) are mandatory human checkpoints and are never auto-bypassed, and a blocked gate always requires explicit human resolution.

### Designing domains

FigJam draws the routing graph from a root; the YAML re-roots it into domains. A domain is a top-level grouping serving three goals that pull against each other:

- **Logical cohesion** — scenes in the same functional area.
- **Shallow tree** — without domains, scenes nest by routing parentage and the tree (and folders) get deep; promoting a subtree to its own domain flattens it.
- **Reach for hot scenes** — the most-edited scenes should sit near the top, not buried inside another scene's routing.

They conflict (strict cohesion buries a hot scene; flattening for reach splits a group), so the proposal is a judgment call — hence the gate. Give the rationale per domain, and flag any call where the goals traded off.

Two domain shapes (see `ui-map-guide.md`):

- **Collapsed** — named for its single root scene (`app:`, `library:`); the root scene's fields sit directly on the domain. Use when one scene clearly owns the group.
- **Non-collapsed** — no single root: a `scenes:` list of peers under a domain id that names the area (e.g. `other:`).

Domain-agnostic reusable scenes (e.g. a shared Web view) go under top-level `common:`, not a domain.

A scene is **defined once** at its canonical home (the domain you assign it) and referenced by id everywhere else. In FigJam the canonical instance is the **rounded rectangle**; hexagons are pointers. When a scene has more than one inbound route, set `primary_parent` to the parent under which FigJam drew the rounded rectangle, so the render places it there.

### Element mapping

| FigJam | YAML |
| --- | --- |
| Rounded rectangle (solid or light-blue) | a scene, *defined* (`foo: { … }`) at its canonical home |
| Hexagon (gray) | a *reference* to that scene by id (`- foo`); its definition lives elsewhere |
| Octagon (pink) | a scene with `todo: true` |
| Connector label `Nav` / `Modal` / `Child` / `Tab` / `Composite` | a route container of that kind on the source scene (`nav:` / `modal:` / `child:` / `tab:` / `composite:`) |
| Dashed rounded-rect wrapper | the destination list of a `nav` / `modal` / `tab` / `child` container — members are mutually exclusive |
| Manual-input solid wrapper | a `composite:` container — members compose one screen |
| `Implements: A, B, C` parallelogram | `implements: [a, b, c]` on the scene |
| `<Platform> only` parallelogram | `platform: <platform>` |
| Free-text parallelogram / sticky note | `note:` on the scene (or `notes:` with `at:` for a route container); cross-cutting notes → top-level `todos:` |

Take `version: 1` and `app:` from the diagram title. Scene ids are the lowercased, snake_cased scene names, globally unique.

### Filling what the diagram omits

FigJam captures less than the schema allows — but the codebase is right there. Read it to fill what the diagram can't carry; don't omit, and don't guess.

- **Modal styles.** A FigJam `Modal` connector says a scene is presented modally but never *how*. The style lives in the code: find the presentation modifier (SwiftUI) or builder (Compose) bound to each modal route and map it back to a `modal_style` per the platform reference (`ui-map-swiftui.md` / `ui-map-compose.md`), then declare the resulting `modal_styles` vocabulary at the top of the map.
- **Anything else the diagram can't express** — derive it from the code where the code is authoritative. If neither the diagram nor the code settles it, **STOP at a blocked gate** and ask the human — never fabricate, and never silently drop it.

Structure comes from the FigJam (and the human-designed domains); the code supplies the details the diagram can't hold. Reconciling any remaining code↔map drift is a later pass (`ui-map-planning.md`), not migration. After approval the project is on the YAML system; subsequent changes use `ui-map-planning.md` / `ui-map-implementation.md`.
