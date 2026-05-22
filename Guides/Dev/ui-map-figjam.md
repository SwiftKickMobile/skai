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

*Stub — the migration procedure will be authored here. See the UI Map skill build sequence, step 6.*
