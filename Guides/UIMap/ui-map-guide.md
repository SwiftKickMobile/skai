Managed-By: skai
Managed-Id: guide.ui-map-guide
Managed-Source: Guides/UIMap/ui-map-guide.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-02

# UI Map Guide

A UI Map is a YAML document that defines every scene in an app and the routing relationships between them. The map is the single source of truth for the app's UI architecture; implementation should mirror it directly. A render script produces a visual diagram from the YAML for human review.

This guide defines the platform-agnostic YAML format. Platform implementation patterns live in companion references:

- [`ui-map-swiftui.md`](ui-map-swiftui.md) — implementing a UI Map in SwiftUI
- [`ui-map-compose.md`](ui-map-compose.md) — implementing a UI Map in Compose Multiplatform or Android-only Jetpack Compose
- [`ui-map-figjam.md`](ui-map-figjam.md) — the deprecated FigJam diagram format, for migrating existing projects

## Rendering and validation

SKAI owns the default UI Map renderer. Use `Bin/ui-map-render.py` from the current SKAI checkout unless the project provides an explicit override.

For an installed project, look first for the SKAI checkout at `Submodules/skai`. If SKAI is installed elsewhere, use that root instead. The renderer takes the map to render and the SVG to write; for the official map:

```
uv run <skai-root>/Bin/ui-map-render.py skai/ui-map/ui-map.yaml --svg skai/ui-map/ui-map.svg
```

`skai/integration.md` may override this command or add project-specific evidence-capture requirements. It does not need to repeat the SKAI default. If no override exists, use the default renderer and block only when the SKAI root, renderer, runtime dependency, SVG dependency, or validation result prevents a valid render.

## YAML format

A UI Map is a YAML document with a fixed schema. The schema is formally defined in [`ui-map.schema.json`](../../Bin/ui-map.schema.json); this section is the conceptual reference.

### Top-level structure

```yaml
version: 1
app: <name>

modal_styles:              # required when modal routes exist
  - <style>

domains:
  <domain-id>:
    ...

common:                    # optional
  - <scene>

todos:                     # optional
  - scope: <scene-id>
    note: "..."
```

- `version`: integer, currently always `1`.
- `app`: human-readable app name.
- `modal_styles`: project vocabulary of valid modal presentation styles (see [Modal styles](#modal-styles)). Required whenever the map contains a modal route.
- `domains`: top-level grouping. Each key is a domain ID; each value is either a *collapsed* or *non-collapsed* domain (see below).
- `common`: optional list of domain-agnostic scenes (e.g. a reusable Web component) shared across the app.
- `todos`: optional list of cross-cutting TODOs not tied to a single scene.

### Domains

A domain is a top-level grouping of related scenes, and the code's folder tree mirrors the map: each domain is a top-level folder, and a scene's folder lives where the map *defines* it (its canonical home) — under that domain, nested by the route containers it sits in. Every other appearance of a scene is a reference, not a definition: references (cross-domain or repeated) are pointers — they import and instantiate the scene from where it's rooted and never move its folder. `primary_parent` likewise affects only the rendered diagram, not the folder tree. (See the platform reference for the concrete layout.)

Domains do two jobs at once: they keep conceptually related scenes together, and they cap nesting depth — a self-contained subtree can be promoted to its own domain (reached by a reference from its entry point) so no single tree grows unboundedly deep.

**Collapsed**: domain ID matches its single root scene. The domain entry carries scene-level fields directly:

```yaml
app:                       # the App scene IS the domain root
  child:
    - login: {}
    - main                 # cross-domain ref
```

**Non-collapsed**: no single root scene. Contains a `scenes:` list of top-level entries:

```yaml
assessment:                # no scene named "assessment" exists
  scenes:
    - question_set: {}
    - media_capture: {}
```

Rule for collapsing: if domain ID == root scene ID, collapse.

### Scenes

Scenes appear inside route containers or directly under a non-collapsed domain's `scenes:` list. Each scene appears in two forms:

- **Reference** — bare string: `- foo`
- **Definition** — single-key mapping: `- foo: { ...body... }`

A scene is *defined* exactly once (its canonical home). All other appearances are references by ID.

Scene body fields (optional unless the route context requires them):

| Field | Meaning |
|---|---|
| `nav`, `modal`, `composite`, `tab`, `child` | Route containers — lists of destinations |
| `modal_style` | Presentation style when reached by a modal route (one of the project's `modal_styles`) |
| `implements` | Variant identifiers for an abstract scene |
| `platform` | Platform scoping (`android`, `ios`, …) |
| `todo` | Boolean — scene is unimplemented |
| `note` | Single free-text annotation |
| `notes` | Multiple annotations (with optional `at:` for container attachment) |
| `primary_parent` | Visual canonical parent (for reused scenes with multiple inbound routes) |

A leaf scene with no body is written as `foo: {}`.

### Route containers

Each route kind is a list of destinations. The list represents a mutually-exclusive group (for nav/modal/tab/child) or the set of children for composite.

```yaml
appointment_details:
  nav:
    - question_set         # cross-domain ref
  composite:
    - thumbnail_slider     # cross-domain ref
  modal:
    - media_capture        # cross-domain ref
    - appointment_submitted: {}   # in-domain definition
    - record_warning: {}
```

Route kinds:

| Kind | Meaning |
|---|---|
| `nav` | Push onto a navigation stack |
| `modal` | Present modally using the destination scene's required `modal_style` |
| `composite` | Embed as a subview |
| `tab` | Embed as a tab in a tab container |
| `child` | Replace primary content (mutually exclusive root-view selection) |

### Modal styles

A `modal` route says a scene is presented modally. The destination's `modal_style` says exactly how, using the project's vocabulary of modal presentations (sheet, full-screen, card, popover, …).

Declare the project vocabulary once at the top level:

```yaml
modal_styles: [sheet, full_screen, card, popover]
```

Then tag a scene with `modal_style` wherever it is *defined* (its canonical home). The value must be one of the declared `modal_styles`:

```yaml
appointment_details:
  modal:
    - media_capture                # cross-domain ref — style lives at its definition
    - appointment_submitted:
        modal_style: card
    - record_warning:
        modal_style: card

media_capture:                     # canonical home
  modal_style: full_screen
```

`modal_style` belongs to the scene, not the route — a scene presented modally from several parents carries one agreed presentation style, and implementation must use it. Every scene reached through a `modal` route must declare `modal_style`, and the map must declare that value in its top-level `modal_styles` vocabulary. The renderer rejects a modal destination with no style or a style outside that vocabulary. A map with no modal routes may omit `modal_styles`.

In the render, each modal wrapper gets a callout listing its destinations and required styles.

### Cross-domain references

Scenes can be referenced across domain boundaries by ID. References use the scene ID alone; the scene's body lives at its canonical home elsewhere in the document.

```yaml
domains:
  pipeline:
    tab:
      - appointments_stage:
          nav:
            - appointment_details   # cross-domain ref

  appointment_details:              # canonical home
    nav: [...]
```

Scene IDs are globally unique across the whole document.

### Reused scenes and `primary_parent`

A scene referenced from multiple places renders with one canonical visual instance and pointers everywhere else. When there are multiple inbound references, `primary_parent` picks the visual home:

```yaml
thumbnail_slider:
  primary_parent: appointment_details   # canonical instance renders here
  modal:
    - gallery: {}
```

With a single inbound reference, `primary_parent` is unnecessary — the only parent is implicitly primary.

### Annotations

Four annotation types, all optional and independent:

**`implements`** — Concrete variants of an abstract scene:

```yaml
web:
  implements: [privacy_policy, terms_of_service]
```

**`todo`** — Boolean flag: the scene's routing or feature work is incomplete. The scene is still part of the map and is still built (scaffolded) — `todo` flags the unfinished routing/feature, not exclusion. Build what's defined.

```yaml
verify:
  todo: true
```

**`note` / `notes`** — Free-text annotations. Single shorthand or list of items:

```yaml
verify:
  todo: true
  note: "iOS implementation missing"

library:
  notes:
    - "Subfolder support planned for v2"
    - at: modal
      text: "Both surfaced from the library toolbar"
```

A note item can be:

- A bare string (attaches to the scene)
- An object `{ text: "...", at: <route-kind> }` (attaches to a route container of that kind instead of the scene)

> Note: the field is `at:` (not `on:`) because YAML 1.1 — which PyYAML uses — treats bare `on` as the boolean `true`. `at:` avoids the trap.

**`platform`** — Platform scoping:

```yaml
demo_mode_loading:
  platform: android
```

### Common scenes

Scenes that are domain-agnostic — typically reusable UI primitives used across features — live under top-level `common:` rather than inside a domain.

```yaml
common:
  - web:
      implements: [privacy_policy, terms_of_service]
```

References to common scenes from inside domains work the same as cross-domain references: by ID.

### Top-level `todos:`

For TODOs that don't naturally attach to a single scene (e.g., architectural concerns, cross-cutting refactors), use the top-level `todos:` list:

```yaml
todos:
  - scope: folders_tab
    note: "Subfolder navigation planned for v2"
  - note: "Migrate analytics tracking to new framework"
```

`scope` is optional. For scene-specific TODOs, prefer the scene-level `todo: true` flag with an accompanying `note:`.

### Schema reference

The formal contract is in [`ui-map.schema.json`](../../Bin/ui-map.schema.json) (JSON Schema, draft 2020-12). Validate a UI Map with:

```
pipx run check-jsonschema --schemafile ui-map.schema.json <your-map>.yaml
```

The schema catches structural errors (missing required fields, invalid route kinds, malformed notes, etc.). Semantic errors (dangling cross-references, duplicate canonical homes) are validated by the render script.

## Authoring a UI Map

The sections above define the format; these are the conventions that make a map *good* — the structure the code mirrors, and the surface a reviewer reads. They are platform-agnostic, and they apply whether you are creating a baseline from scratch or editing an existing map. [`ui-map-demo.md`](ui-map-demo.md) is the worked example.

- **Draw domain boundaries by meaning, then depth.** Group conceptually related scenes into a domain. Promote a self-contained or deeply-nesting subtree to its own domain (referenced from its entry point) to keep trees shallow — but don't spawn a domain mechanically the moment nesting reaches some depth, and don't force unrelated scenes together to fill one.
- **Weigh whether a feature earns its own domain.** A domain should be a substantial feature area; a small or secondary feature doesn't justify a dedicated domain — group small/secondary features together under one shared domain rather than giving each its own.
- **Collapse single-root domains.** A feature area with one root scene is one collapsed domain: domain id == root scene id, scene fields written directly, no `scenes:` wrapper. Prefer the concise feature name (`tickets`, not a `tickets` domain wrapping a `tickets_home` scene). Use the non-collapsed `scenes:` form only when a domain genuinely has several top-level scenes with no single root (a multi-root bucket like `assessment`). Don't wrap a lone root scene in `scenes:`, and don't force a multi-root bucket to collapse.
- **Define each scene where it's reached.** A scene reached by a single route is defined *nested inside that route container*, under its parent, so the folder tree mirrors the navigation. Don't flatten a single-parent scene into a sibling of its parent.

  Wrong — `ticket_detail` is reached only from `tickets_home`, yet defined as its sibling under `scenes:`:

  ```yaml
  tickets:
    scenes:
      - tickets_home:
          nav:
            - ticket_detail        # reference out
      - ticket_detail:             # wrong: a single-parent scene flattened to a domain sibling
          modal:
            - reassign: { modal_style: sheet }
  ```

  Right — defined nested under the parent that reaches it; the single-root domain also collapses:

  ```yaml
  tickets:                         # collapsed: one root scene (was tickets_home)
    nav:
      - ticket_detail:
          modal:
            - reassign: { modal_style: sheet }
  ```

- **Reused scenes have one home.** A scene reached from more than one parent is defined once — at a domain's top-level `scenes:` list or in `common:` — and referenced by id from each parent; set `primary_parent` to choose its visual home. Never copy a scene's body to a second place.
- **`common:` is only for domain-agnostic scenes.** Use `common:` for a scene with no feature identity — one that could render anything, like a web view that displays any URL. A *feature* scene that happens to be reused across domains stays in a domain with `primary_parent`; it does not belong in `common:`.
- **Display and data states are notes, not structure.** Empty, populated, loading, and error are states of one scene — not separate scenes, routes, or `implements` variants. Capture them with `note`/`notes` (or a map TODO); reserve `implements` for genuinely distinct variants of an abstract scene.
- **Route kind reflects the actual presentation.** Read `nav`/`modal`/`composite`/`tab`/`child` from how a destination is really presented — not from vague wording ("appears", "available from", "can access") and not from an enum's name. Use `modal` when the source says modal/sheet/dialog/popover/full-screen; use `nav` when it says pushed/opens detail/drills in/links to. When the basis is genuinely ambiguous, treat it as a decision to raise, not a guess to bury.
- **Every modal destination has a `modal_style`, on the scene.** A scene presented modally carries one required `modal_style` at its canonical home — it describes the destination, not the route — and implementation must use it.
