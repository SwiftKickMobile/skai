Managed-By: skai
Managed-Id: guide.ui-map-swiftui-placeholders
Managed-Source: Guides/UIMap/ui-map-swiftui-placeholders.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-07

# UI Map — SwiftUI Placeholder Scenes

Print `📖 SKAI guide: ui-map-swiftui-placeholders` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

How the UI Map **implementation** skill scaffolds SwiftUI scenes: skeleton + navigation, no feature content, building on [`ui-map-swiftui.md`](ui-map-swiftui.md) (read its **Scene file layout**, **Route enums** and **Modal routing** first). Load this guide while auditing, planning, or building whenever placeholder work is in scope, and only then. Placeholder route actions set view-model route properties directly, unlike production's *State ownership*.

Placeholders are built from the `SKAISwiftUI` package (**requires iOS 18 / macOS 15**; uses `ScrollPosition`). Inspect the app target first: a missing local package product is added from the skai submodule as mechanical scaffold setup this skill owns in Build; if its path is unavailable or project constraints prevent linking it, STOP at a blocked gate.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## Build philosophy

This guide covers the standard patterns — with standard route kinds and modal styles it alone suffices — and the project `README.md` covers overrides and patterns not here (e.g. custom modal styles); a pattern neither supplies means STOP at a blocked gate citing the missing piece, never inventing one.

## The one rule: NavigationStack lives at the presentation boundary

A scene **never wraps itself** in a `NavigationStack`: exactly one stack sits on any root-to-leaf path, supplied by whatever first presents a scene on it.

**The decision you run:** before rendering any slot or destination, ask *is a `NavigationStack` already on this path, or is what I'm presenting tabbed?* and add one only if neither; that resolves every graph. The per-kind cases below each derive it for a **single** kind — not independent commands — so for a composition they don't draw (e.g. a `child` coordinator reached by `nav` push), apply the rule, not a case: the push already put a stack on the path; the child slot adds none.

- **modal** — `.sheet` / `.fullScreenCover` supply the stack (a tabbed destination excepted: see **tab**); `.popover` does **not**.
- **tab** — a tabbed scene (its body is a `TabView`) takes no stack from its presenter; each tab's content supplies its own unless one is already on the path.
- **child** — the child slot supplies the stack for a **non-tab** child **only when none is already on the path**; a **tabbed** child is never wrapped (see **tab**).
- **nav push** — reuses the ambient stack; the destination adds none.

This gives every scene's title a nav bar without nested stacks, for any graph; a tabbed scene's title rides in its tabs' breadcrumbs instead.

## API (`SKAISwiftUI`)

- `PlaceholderScene(title:domainColor:routes:tabs:selection:)`, or with `{ embedded }` instead of tabs — the scene body; `title` is the scene name from its map ID.
- `PlaceholderRoute(label:kind:isCurrent:) { action }` — one menu route; `kind` ∈ `.nav .sheet .fullScreen .popover .child`; `isCurrent: true` hides it (the **active child**).
- `PlaceholderTab(label:systemImage:route:) { content }` — one tab; see *tab*.
- `PlaceholderChildHost(title:domainColor:routes:) { content }` — hosts a child-routed scene full-bleed, passing the parent's breadcrumb to the selected child.
- `.placeholderCrumb("Owner", color: ..., routes: ...)` — on a nav/modal destination, adds the presenting scene and its routes to its breadcrumb.
- `\.placeholderShowsDismiss` (environment `Bool`) — `true` on modal destinations (shows the ✕), `false` on nav ones.

## Domain colors

Scaffolded scenes are tinted like the rendered map, so click-through reads against the diagram; domains are colored in map **declaration order**, and `Colors.domain(at:)` returns an index's tint.

Generate one file, `DomainColors.swift`, with each domain's slot:

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

Each scene sets `domainColor` to its domain's slot, a sub-domain scene to its domain's color: `trail_detail` and `log_hike` live in `trails`, so both use `DomainColors.trails`:

```swift
PlaceholderScene(title: "Trails", domainColor: DomainColors.trails, routes: [ /* ... */ ])
```

`DomainColors` lists every key in `domains`, in declaration order, then `common` when the map has a top-level `common:` group — never only the domains with placeholders so far. Like the `SKAISwiftUI` dependency, it is shared placeholder infrastructure the production skill deletes once no `UI Map scaffold` markers remain.

## What the package renders for you — don't hand-build these

You declare only `title` / `domainColor` / `routes` / `tabs` / `selection` / `embedded` and wire the destinations; `PlaceholderScene` handles:

- **Breadcrumb title bar** — ancestors + this scene; each segment is a menu of its scene's routes in title-case sections by kind (Nav / Sheet / Full Screen / Popover / Child). Routeless segments are secondary-colored, the **active child** omitted; the row scrolls horizontally, pinned to the trailing (current) node.
- **Dismiss ✕** — inline beside the breadcrumb, only when `placeholderShowsDismiss` (i.e. modal).
- **Nav-bar title** — inline `navigationTitle`, full-bleed scenes only (embedded content sets none).
- **Layout** — full-bleed (no border) for all but **embedded composite content**, which gets a light-gray fill (no border).
- **Tabs** — a real full-bleed `TabView` and nothing else: the breadcrumb, and the ✕ when presented modally, move into each tab. Each tab takes a `systemImage` (see *tab*), defaulted if it doesn't resolve.

## Destination markers (nav + modal only)

Every destination a scene presents gets two annotations for breadcrumb + dismiss context:

- `.placeholderCrumb("<this scene's title>", color: <its domain color>, routes: <its routes>)` — puts this presenting scene and its route menu in the destination's breadcrumb; pass the presenter's `PlaceholderScene` route list, never a partial rebuild per destination.
- `.environment(\.placeholderShowsDismiss, <true for modal, false for nav>)`.

Child and tab content need **no** markers — `PlaceholderChildHost` and the tab wrapping carry the crumb.

## Per route kind

### child

`PlaceholderChildHost` + a `switch` over the child route; each child route is `kind: .child` marking `isCurrent`. In the switch, apply the one rule: wrap a **non-tab** child in a `NavigationStack` **only if no stack is already on the path**, i.e. this coordinator is the presentation boundary (the root, or presented by a popover; a sheet, cover, tab or nav push already put one on the path). A **tabbed** child is never wrapped.

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

`tabs:` on `PlaceholderScene`; each tab's content is wrapped in a `NavigationStack` unless one is already on the path (see the one rule). Tab labels and icons are final: use those the inputs give; otherwise a reasonable label, and for an icon not given or not an SF Symbol, a fitting `systemImage` — a valid name, not the package's fallback — ideally with a `.fill` variant so iOS fills it when selected (e.g. `text.document`, `folder`, `trash`). As in production the view model's `currentTabRoute` selects the tab: pass it as `selection:`, each tab's `<Scene>TabRoute` case as `route:`. The package's bar is the bar: styling or extending it, or custom bars, isn't scaffold work. A tab added to a real screen's bar is a real-screen route (see *Reaching a scene from a real screen*), not a `tabs:` entry. Modal routes ride alongside as `.sheet` / `.fullScreenCover` (see modal).

```swift
PlaceholderScene(
    title: "Library",
    domainColor: DomainColors.library,
    routes: [
        PlaceholderRoute(label: "Profile", kind: .sheet) { viewModel.sheetRoute = .profile },
        PlaceholderRoute(label: "Search", kind: .fullScreen) { viewModel.coverRoute = .search },
    ],
    tabs: [ // from the inputs
        PlaceholderTab(label: "All Notes", systemImage: "text.document", route: LibraryTabRoute.notes) { NavigationStack { NotesView() } },
        PlaceholderTab(label: "Folders", systemImage: "folder", route: LibraryTabRoute.folders) { NavigationStack { FoldersView() } },
        PlaceholderTab(label: "Trash", systemImage: "trash", route: LibraryTabRoute.trash) { NavigationStack { TrashView() } },
    ],
    selection: $viewModel.currentTabRoute
)
.sheet(...) { ... }            // see modal
.fullScreenCover(...) { ... }
```

### nav

The scene declares `.navigationDestination` on its `PlaceholderScene` and owns **no** `NavigationStack` (supplied by the presenter/tab/child).

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

`.sheet` / `.fullScreenCover` **wrap their content in a `NavigationStack`** unless it is tabbed; `.popover` does not (and adds `.presentationCompactAdaptation(.popover)`). Use the modal-style → modifier mapping in `ui-map-swiftui.md`.

Below, `routes` is the presenting `PlaceholderScene`'s array.

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

Composite children go directly in the `embedded` ViewBuilder (shown together, each a gray-filled `PlaceholderScene`). A scene with both tabs and composite children has no placeholder shape: STOP in Discussion under the implementation guide's *Finding disposition*.

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

No routes, embedded or tabs — but, like every scene, a view model (empty until it needs state).

```swift
// ShareSheetViewModel.swift
// 🟡 UI Map scaffold <change-id>
@Observable
class ShareSheetViewModel {}

// ShareSheetView.swift
// 🟡 UI Map scaffold <change-id>
struct ShareSheetView: View {
    @State private var viewModel = ShareSheetViewModel()

    var body: some View { PlaceholderScene(title: "Share Sheet", domainColor: DomainColors.note) }
}
```

## New-scene inputs — none

A newly scaffolded scene models no inputs: no variant enum for `implements`, no initializer parameters, no associated value on its incoming route case. A new route to an existing destination inspects and preserves its initializer contract: when the codebase or project conventions already define every required value's source, carry them on the route enum and pass them through; otherwise STOP in Discussion. Never invent fixture data, value sources, or feature behavior.

## Reaching a scene from a real screen

> **TODO (deferred).** No concrete entry-trigger API exists yet; until `SKAISwiftUI` or project conventions provide it, this whole route, a real screen's tab bar included, is deferred: STOP in Discussion before Code Changes under the implementation guide's *Finding disposition*. Never hand-roll or omit the trigger.

Once it exists, reaching a scaffolded scene from a **real** (non-placeholder) screen injects up to two pieces into that file, each stamped with the change-id scaffold marker (`// 🟡 UI Map scaffold <change-id>`) for feature work to find and remove:

1. **Destination registration** — the new scene on the real screen's navigation host or tab bar, in the standard route pattern (*Route enums* and *Tab routing* in [`ui-map-swiftui.md`](ui-map-swiftui.md); *Per route kind* above).
2. **Entry trigger** — unless the host is its own entry (a tab bar), a temporary route-menu bar over the real screen via `safeAreaInset(edge: .top)` so the new scene is click-through reachable; planned as a small `SKAISwiftUI` modifier reusing the placeholder breadcrumb menu, exact signature TBD in testing.

The trigger is throwaway — feature work replaces it with the real entry point and deletes the marked block.

## Boundary

Placeholders are skeleton + navigation only: a scaffold that seems to require feature content (real UI, business logic, data) is over-built — stop; feature work belongs to a separate dev spec.

## Project Addendum

If `<active-project-root>/skai/addenda/ui-map-swiftui-placeholders-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
