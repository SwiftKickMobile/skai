Managed-By: skai
Managed-Id: guide.ui-map-swiftui-placeholders
Managed-Source: Guides/UIMap/ui-map-swiftui-placeholders.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-11

# UI Map — SwiftUI Placeholder Scenes

How the UI Map **implementation** skill scaffolds scenes in SwiftUI: skeleton + navigation, no feature content. Companion to [`ui-map-swiftui.md`](ui-map-swiftui.md) — read its **Scene file layout**, **Route enums**, and **Modal routing** sections first; this doc builds on them. Load this doc while auditing, planning, or building whenever placeholder work is in scope; omit it only when no placeholder work is in scope.

Placeholders are built from the `SKAISwiftUI` package. Inspect the app target first; when the local package product is absent, adding it from the skai submodule is mechanical scaffold setup owned by this skill in Build. If the package path is unavailable or project constraints prevent linking it, STOP at a blocked gate. **Requires iOS 18 / macOS 15** (uses `ScrollPosition`).

## Build philosophy

Follow this guide for the standard patterns; defer to the project `README.md` for overrides and for patterns not covered here (e.g. custom modal styles). With standard route kinds and modal styles, this guide alone suffices — no README required. If a scaffold needs a pattern neither the guide nor the README supplies, STOP at a blocked gate citing the missing piece — do not invent one.

## The one rule: NavigationStack lives at the presentation boundary

A scene **never wraps itself** in a `NavigationStack`. Exactly one stack sits on any root-to-leaf path, supplied by whatever first presents a scene on that path.

**The decision you run:** before rendering any slot or destination, ask *is a `NavigationStack` already on this path?* — add one only if not. That question resolves every graph. The per-kind cases below are it worked out for a **single** kind; read them as derivations of this rule, not independent commands. For a composition the cases don't draw (e.g. a `child` coordinator reached by a `nav` push), apply the rule rather than pattern-matching a case: the push already put a stack on the path, so the child slot adds none.

- **modal** — `.sheet` / `.fullScreenCover` supplies the stack (popover does **not**).
- **tab** — each `PlaceholderTab`'s content supplies its own stack.
- **child** — the child slot supplies the stack for a **non-tab** child **only when none is already on the path**; a **tabbed** child (its body is a `TabView`) supplies its own per tab.
- **nav push** — reuses the ambient stack; the destination adds none.

This gives every scene a nav bar (for its title) without nested stacks, for any graph.

## API (`SKAISwiftUI`)

- `PlaceholderScene(title:domainColor:routes:tabs:)` and `PlaceholderScene(title:domainColor:routes:tabs:) { embedded }` — the scene body.
- `PlaceholderRoute(label:kind:isCurrent:) { action }` — one menu route. `kind` ∈ `.nav .sheet .fullScreen .popover .child`. `isCurrent: true` omits it from the menu (used for the **active child**).
- `PlaceholderTab(label:) { content }` — one tab.
- `PlaceholderChildHost(title:domainColor:routes:) { content }` — hosts a child-routed scene full-bleed and contributes the parent's breadcrumb to the selected child.
- `.placeholderCrumb("Owner", color: ..., routes: ...)` — on a nav/modal destination, adds the presenting scene and its routes to the destination's breadcrumb.
- `\.placeholderShowsDismiss` (environment `Bool`) — `true` on modal destinations (shows the ✕), `false` on nav destinations.

## Domain colors

Scaffolded scenes are tinted to match the rendered map, so click-through reads against the diagram. The render colors each domain by its **declaration order** in the map; `Colors.domain(at:)` returns the tint for that index.

Generate one artifact, `DomainColors.swift`, mapping each domain to its slot in map declaration order:

```swift
// 🟡 UI Map scaffold <change-id>
import SKAISwiftUI

enum DomainColors {
    static let app     = Colors.domain(at: 0)
    static let trails  = Colors.domain(at: 1)
    static let profile = Colors.domain(at: 2)
    static let common  = Colors.domain(at: 3) // when top-level `common:` exists
}
```

Each scene then sets `domainColor` to its domain's slot. A scene in a sub-domain uses its domain's color — `trail_detail` and `log_hike` live in `trails`, so both use `DomainColors.trails`:

```swift
PlaceholderScene(title: "Trails", domainColor: DomainColors.trails, routes: [ /* ... */ ])
```

`DomainColors` follows the renderer's domain order: every key in `domains`, in declaration order, followed by `common` when the map has a top-level `common:` group. Never track only the domains that currently have placeholders. It is shared placeholder infrastructure, like the `SKAISwiftUI` dependency itself: the production skill deletes it once no `UI Map scaffold` markers remain in the project.

## What the package renders for you — don't hand-build these

You declare only `title` / `domainColor` / `routes` / `tabs` / `embedded` and wire the destinations. `PlaceholderScene` handles:

- **Breadcrumb title bar** — ancestors + this scene; each segment is a menu of that scene's routes, grouped into title-case sections by kind (Nav / Sheet / Full Screen / Popover / Child). Routeless segments render in secondary color; the **active child** is omitted; the row scrolls horizontally and is pinned to the trailing (current) node.
- **Dismiss ✕** — inline beside the breadcrumb, shown only when `placeholderShowsDismiss` (i.e. presented modally).
- **Nav-bar title** — inline `navigationTitle`, on full-bleed scenes only (embedded content doesn't set one).
- **Layout** — full-bleed (no border) for everything except **embedded composite content**, which gets a light-gray fill (no border).
- **Tabs** — a real full-bleed `TabView`; the breadcrumb is delegated to (accumulated into) each tab. Each tab takes a `systemImage` (see tab section); the package falls back to a default if it doesn't resolve.

## Destination markers (nav + modal only)

Every destination a scene presents gets two annotations so the destination inherits the right breadcrumb + dismiss context:

- `.placeholderCrumb("<this scene's own title>", color: <this scene's domain color>, routes: <this scene's routes>)` — so the destination's breadcrumb includes this presenting scene and exposes the same route menu. Reuse the route list passed to the presenter's `PlaceholderScene`; do not reconstruct a partial list at each destination.
- `.environment(\.placeholderShowsDismiss, <true for modal, false for nav>)`.

Child and tab content need **no** markers — `PlaceholderChildHost` and the tab wrapping carry the crumb automatically.

## Per route kind

### child

`PlaceholderChildHost` + a `switch` over the child route. Each child route is `kind: .child` and marks `isCurrent` so the active one drops out of the menu. In the switch, apply the one rule: wrap a **non-tab** child in a `NavigationStack` **only if no stack is already on the path** — i.e. this coordinator is itself the presentation boundary (the root, or reached by a modal/tab). A coordinator reached by a **nav push** already sits in the presenter's stack, so its non-tab children reuse it (no wrap). A **tabbed** child is never wrapped.

```swift
struct AppView: View {
    @State private var viewModel = AppViewModel()
    var body: some View {
        PlaceholderChildHost(
            title: "App",
            domainColor: DomainColors.app,
            routes: [
                PlaceholderRoute(label: "Library", kind: .child, isCurrent: viewModel.childRoute == .library) { viewModel.childRoute = .library },
                PlaceholderRoute(label: "Login", kind: .child, isCurrent: viewModel.childRoute == .login) { viewModel.childRoute = .login },
            ]
        ) {
            switch viewModel.childRoute {
            case .library: LibraryView()                  // tabbed child → not wrapped
            case .login: NavigationStack { LoginView() }  // non-tab child, App is root (no ambient stack) → wrap
            }
        }
    }
}
```

### tab

`tabs:` on `PlaceholderScene`; each tab's content is wrapped in a `NavigationStack`. Give each tab a fitting `systemImage` — a real SF Symbol, preferably a base name with a `.fill` variant so iOS solidifies it when selected (e.g. `note.text`, `folder`, `trash`). If the name doesn't resolve, the package falls back to a default, but pick a valid one. Modal routes (if any) ride alongside as `.sheet` / `.fullScreenCover` (see modal).

```swift
PlaceholderScene(
    title: "Library",
    domainColor: DomainColors.library,
    routes: [
        PlaceholderRoute(label: "Profile", kind: .sheet) { viewModel.sheetRoute = .profile },
        PlaceholderRoute(label: "Search", kind: .fullScreen) { viewModel.coverRoute = .search },
    ],
    tabs: [
        PlaceholderTab(label: "Notes", systemImage: "note.text") { NavigationStack { NotesView() } },
        PlaceholderTab(label: "Folders", systemImage: "folder") { NavigationStack { FoldersView() } },
        PlaceholderTab(label: "Trash", systemImage: "trash") { NavigationStack { TrashView() } },
    ]
)
.sheet(...) { ... }            // see modal
.fullScreenCover(...) { ... }
```

### nav

The scene declares `.navigationDestination` on its `PlaceholderScene` and owns **no** `NavigationStack` (the presenter/tab/child supplies it). The destination gets `showsDismiss = false` and the presenter's crumb.

```swift
struct NotesView: View {
    @State private var viewModel = NotesViewModel()
    var body: some View {
        @Bindable var viewModel = viewModel
        let routes = [PlaceholderRoute(label: "Note", kind: .nav) { viewModel.navRoute = .note }]
        PlaceholderScene(
            title: "Notes",
            domainColor: DomainColors.library,
            routes: routes
        )
        .navigationDestination(item: $viewModel.navRoute) { route in
            switch route {
            case .note: NoteView()
                .environment(\.placeholderShowsDismiss, false)
                .placeholderCrumb("Notes", color: DomainColors.library, routes: routes)
            }
        }
    }
}
```

### modal

`.sheet` / `.fullScreenCover` **wrap their content in a `NavigationStack`**; `.popover` does not (and adds `.presentationCompactAdaptation(.popover)`). Every modal destination gets `showsDismiss = true` and the presenter's crumb. Use the modal-style → modifier mapping in `ui-map-swiftui.md`.

In the modifier examples below, `routes` is the same array passed to the presenting `PlaceholderScene`.

```swift
.sheet(item: $viewModel.sheetRoute) { route in
    NavigationStack {
        switch route {
        case .shareSheet: ShareSheetView()
            .environment(\.placeholderShowsDismiss, true)
            .placeholderCrumb("Note", color: DomainColors.note, routes: routes)
        }
    }
}
.fullScreenCover(item: $viewModel.coverRoute) { route in
    NavigationStack {
        switch route {
        case .attachmentViewer: AttachmentViewerView()
            .environment(\.placeholderShowsDismiss, true)
            .placeholderCrumb("Note", color: DomainColors.note, routes: routes)
        }
    }
}
.popover(item: $viewModel.popoverRoute) { route in
    switch route {
    case .tagPicker: TagPickerView()
        .presentationCompactAdaptation(.popover)
        .environment(\.placeholderShowsDismiss, true)
        .placeholderCrumb("Note", color: DomainColors.note, routes: routes)
    }
}
```

### composite

Composite children are instantiated directly in the `embedded` ViewBuilder (shown together, each as its own gray-filled `PlaceholderScene`).

```swift
PlaceholderScene(
    title: "Note",
    domainColor: DomainColors.note,
    routes: [ /* modal routes, wired as above */ ]
) {
    EditorView()
}
```

### leaf

No routes, no embedded, no tabs — but still gets a view model, like every scene (empty until it needs state).

```swift
@Observable
class ShareSheetViewModel {}

struct ShareSheetView: View {
    @State private var viewModel = ShareSheetViewModel()

    var body: some View { PlaceholderScene(title: "Share Sheet", domainColor: DomainColors.note) }
}
```

## New-scene inputs — none

A newly scaffolded scene models no inputs: no variant enum for `implements`, no initializer parameters, and its incoming route case carries no associated value. For a new route to an existing destination, inspect and preserve that destination's initializer contract. When the codebase or project conventions already define the source of every required value, carry those values on the route enum and pass them through; otherwise STOP in Discussion under the implementation guide's missing-input rule. Do not invent fixture data, value sources, or feature behavior.

## Reaching a scene from a real screen

> **TODO (deferred).** The concrete entry-trigger API is not implemented yet (rebuild-plan D12). Until `SKAISwiftUI` or project conventions provide it, this route has no defined code mapping: STOP in Discussion before Code Changes under the implementation guide's missing-mapping rule. Do not hand-roll or omit the trigger.

Once that mapping exists, reaching a scaffolded scene from an existing **real** (non-placeholder) screen injects two pieces into that real file, each stamped with the change-id scaffold marker (`// 🟡 UI Map scaffold <change-id>`) so feature work can find and remove them:

1. **Destination registration** — register the new scene on the real screen's navigation host using the standard route pattern (see *Route enums* in [`ui-map-swiftui.md`](ui-map-swiftui.md) and *Per route kind* above).
2. **Entry trigger** — a temporary route-menu bar overlaid on the real screen via `safeAreaInset(edge: .top)`, so the new scene is reachable for click-through. Planned as a small `SKAISwiftUI` modifier reusing the placeholder breadcrumb menu; exact signature TBD in testing.

The trigger is throwaway — feature work replaces it with the real entry point and deletes the marked block.

## Boundary

Placeholders are skeleton + navigation only. If a scaffold seems to require feature content (real UI, business logic, data), the scene is being over-built — stop. Feature work belongs to a separate work spec.
