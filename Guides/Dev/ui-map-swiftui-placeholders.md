# UI Map — SwiftUI Placeholder Scenes

How the UI Map **implementation** skill scaffolds scenes in SwiftUI: skeleton + navigation, no feature content. Companion to [`ui-map-swiftui.md`](ui-map-swiftui.md) — read its **Scene file layout**, **Route enums**, and **Modal routing** sections first; this doc builds on them. Read this doc only when scaffolding placeholders (not for audit or planning).

Placeholders are built from the `SKAISwiftUI` package (the host depends on it via a local path through the skai submodule). **Requires iOS 18 / macOS 15** (uses `ScrollPosition`).

## Build philosophy

Follow this guide for the standard patterns; defer to the project `README.md` for overrides and for patterns not covered here (e.g. custom modal styles). With standard route kinds and modal styles, this guide alone suffices — no README required. If a scaffold needs a pattern neither the guide nor the README supplies, STOP at a blocked gate citing the missing piece — do not invent one.

## The one rule: NavigationStack lives at the presentation boundary

A scene **never wraps itself** in a `NavigationStack`. Exactly one stack is supplied by whatever presents the scene:

- **modal** — the `.sheet` / `.fullScreenCover` wraps its content in a `NavigationStack` (popover does **not**).
- **tab** — each `PlaceholderTab`'s content is wrapped in a `NavigationStack`.
- **child** — the child slot wraps a **non-tab** child in a `NavigationStack`; a **tabbed** child (its body is a `TabView`) is **not** wrapped (each tab carries its own).
- **nav push** — reuses the ambient stack; the destination adds none.

This gives every scene a nav bar (for its title) without nested stacks, for any graph.

## API (`SKAISwiftUI`)

- `PlaceholderScene(title:routes:tabs:)` and `PlaceholderScene(title:routes:tabs:) { embedded }` — the scene body.
- `PlaceholderRoute(label:kind:isCurrent:) { action }` — one menu route. `kind` ∈ `.nav .sheet .fullScreen .popover .child`. `isCurrent: true` omits it from the menu (used for the **active child**).
- `PlaceholderTab(label:) { content }` — one tab.
- `PlaceholderChildHost(title:routes:) { content }` — hosts a child-routed scene full-bleed and contributes the parent's breadcrumb to the selected child.
- `.placeholderCrumb("Owner")` — on a nav/modal destination, adds the presenting scene to the destination's breadcrumb.
- `\.placeholderShowsDismiss` (environment `Bool`) — `true` on modal destinations (shows the ✕), `false` on nav destinations.

## What the package renders for you — don't hand-build these

You declare only `title` / `routes` / `tabs` / `embedded` and wire the destinations. `PlaceholderScene` handles:

- **Breadcrumb title bar** — ancestors + this scene; each segment is a menu of that scene's routes, grouped into title-case sections by kind (Nav / Sheet / Full Screen / Popover / Child). Routeless segments render in secondary color; the **active child** is omitted; the row scrolls horizontally and is pinned to the trailing (current) node.
- **Dismiss ✕** — inline beside the breadcrumb, shown only when `placeholderShowsDismiss` (i.e. presented modally).
- **Nav-bar title** — inline `navigationTitle`, on full-bleed scenes only (embedded content doesn't set one).
- **Layout** — full-bleed (no border) for everything except **embedded composite content**, which gets a light-gray fill (no border).
- **Tabs** — a real full-bleed `TabView` with a default tab symbol; the breadcrumb is delegated to (accumulated into) each tab.

## Destination markers (nav + modal only)

Every destination a scene presents gets two annotations so the destination inherits the right breadcrumb + dismiss context:

- `.placeholderCrumb("<this scene's own title>")` — so the destination's breadcrumb includes this (the presenting) scene.
- `.environment(\.placeholderShowsDismiss, <true for modal, false for nav>)`.

Child and tab content need **no** markers — `PlaceholderChildHost` and the tab wrapping carry the crumb automatically.

## Per route kind

### child

`PlaceholderChildHost` + a `switch` over the child route. Each child route is `kind: .child` and marks `isCurrent` so the active one drops out of the menu. In the switch, wrap a **non-tab** child in a `NavigationStack`; leave a **tabbed** child unwrapped.

```swift
struct AppView: View {
    @State private var viewModel = AppViewModel()
    var body: some View {
        PlaceholderChildHost(
            title: "App",
            routes: [
                PlaceholderRoute(label: "Library", kind: .child, isCurrent: viewModel.childRoute == .library) { viewModel.childRoute = .library },
                PlaceholderRoute(label: "Login", kind: .child, isCurrent: viewModel.childRoute == .login) { viewModel.childRoute = .login },
            ]
        ) {
            switch viewModel.childRoute {
            case .library: LibraryView()                  // tabbed child → not wrapped
            case .login: NavigationStack { LoginView() }  // non-tab child → wrapped
            }
        }
    }
}
```

### tab

`tabs:` on `PlaceholderScene`; each tab's content is wrapped in a `NavigationStack`. Modal routes (if any) ride alongside as `.sheet` / `.fullScreenCover` (see modal).

```swift
PlaceholderScene(
    title: "Library",
    routes: [
        PlaceholderRoute(label: "Profile", kind: .sheet) { viewModel.sheetRoute = .profile },
        PlaceholderRoute(label: "Search", kind: .fullScreen) { viewModel.coverRoute = .search },
    ],
    tabs: [
        PlaceholderTab(label: "Notes") { NavigationStack { NotesView() } },
        PlaceholderTab(label: "Folders") { NavigationStack { FoldersView() } },
        PlaceholderTab(label: "Trash") { NavigationStack { TrashView() } },
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
        PlaceholderScene(
            title: "Notes",
            routes: [PlaceholderRoute(label: "Note", kind: .nav) { viewModel.navRoute = .note }]
        )
        .navigationDestination(item: $viewModel.navRoute) { route in
            switch route {
            case .note: NoteView()
                .environment(\.placeholderShowsDismiss, false)
                .placeholderCrumb("Notes")
            }
        }
    }
}
```

### modal

`.sheet` / `.fullScreenCover` **wrap their content in a `NavigationStack`**; `.popover` does not (and adds `.presentationCompactAdaptation(.popover)`). Every modal destination gets `showsDismiss = true` and the presenter's crumb. Use the modal-style → modifier mapping in `ui-map-swiftui.md`.

```swift
.sheet(item: $viewModel.sheetRoute) { route in
    NavigationStack {
        switch route {
        case .shareSheet: ShareSheetView()
            .environment(\.placeholderShowsDismiss, true)
            .placeholderCrumb("Note")
        }
    }
}
.fullScreenCover(item: $viewModel.coverRoute) { route in
    NavigationStack {
        switch route {
        case .attachmentViewer: AttachmentViewerView()
            .environment(\.placeholderShowsDismiss, true)
            .placeholderCrumb("Note")
        }
    }
}
.popover(item: $viewModel.popoverRoute) { route in
    switch route {
    case .tagPicker: TagPickerView()
        .presentationCompactAdaptation(.popover)
        .environment(\.placeholderShowsDismiss, true)
        .placeholderCrumb("Note")
    }
}
```

### composite

Composite children are instantiated directly in the `embedded` ViewBuilder (shown together, each as its own gray-filled `PlaceholderScene`).

```swift
PlaceholderScene(
    title: "Note",
    routes: [ /* modal routes, wired as above */ ]
) {
    EditorView()
}
```

### leaf

No routes, no embedded, no tabs.

```swift
struct ShareSheetView: View {
    var body: some View { PlaceholderScene(title: "Share Sheet") }
}
```

## New-scene inputs — none

A newly scaffolded scene models no inputs: no variant enum for `implements`, no initializer parameters, and its incoming route case carries no associated value. (Wiring inputs — inspecting an existing destination's initializer, modeling them on the route enum, asking for a fixture — is the existing-scene case, handled separately.)

## Boundary

Placeholders are skeleton + navigation only. If a scaffold seems to require feature content (real UI, business logic, data), the scene is being over-built — stop. Feature work belongs to a separate work spec.
