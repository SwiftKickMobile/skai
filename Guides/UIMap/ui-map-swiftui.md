Managed-By: skai
Managed-Id: guide.ui-map-swiftui
Managed-Source: Guides/UIMap/ui-map-swiftui.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-05-24

# UI Map — SwiftUI Reference

Platform reference for implementing a UI Map in SwiftUI. Companion to [`ui-map-guide.md`](ui-map-guide.md), which defines the platform-agnostic YAML format.

Each scene's routing is implemented locally: the view model owns the outgoing route state as `@Published` properties, and the view applies SwiftUI modifiers driven by those properties. There is no central router.

## Scene file layout

For a scene named `Foo`:

```
Foo/
  FooView.swift          // struct FooView: View
  FooViewModel.swift     // route enums at the top, then @Observable class FooViewModel
  Views/                 // optional — Foo's own subviews
```

All of the scene's route enums live at the top of `FooViewModel.swift`, above the view-model class. Every scene gets a `FooViewModel` — even a leaf with no routes or state — so each scene's file layout is identical and there is always a consistent home for state the moment any is needed.

A scene's folder may contain a `Views/` subfolder for the scene's own subviews — small presentational views split out to keep `FooView.swift` uncluttered. `Views/` holds subviews only: never a scene (every scene gets its own folder), and never another scene's subviews.

Scenes live under a top-level `Scenes/` folder (a project may override the root in its `README.md`), organized to mirror the map's domain structure — **the folder tree reads as the `domains:` tree, not as routing parentage.** Each domain is a folder directly under `Scenes/`, and a scene's folder is placed where the map *defines* it:

- a collapsed domain (domain id == its root scene) → the domain folder is that root scene's folder (e.g. `Library/LibraryView.swift`);
- a scene defined inline under a route container → nests inside that container's owning scene's folder (e.g. `App/Login/Welcome/`);
- a scene defined in a non-collapsed domain's `scenes:` list → sits directly under the domain folder.

Every other appearance of a scene is a reference: the referencing scene imports and instantiates it, and a reference **never** creates or moves a folder. This includes a cross-domain reference (it does not pull the scene into the referrer's domain) and `primary_parent` (a render-only hint, never a folder move). Do not place scenes flat — the folder tree must mirror the map's domain structure.

Scenes in the YAML's top-level `common:` group are domain-agnostic. They live in the shared UI module under its own top-level `Scenes/` folder — one folder per scene, following the same per-scene layout as any other scene. The shared UI module must link the placeholder package (`SKAISwiftUI`) to host these scenes. If it doesn't — or the project has no SwiftUI-capable shared module — that is a **blocked gate**: STOP and ask for the dependency to be added. (The symptom is a *link* error — undefined `SKAISwiftUI` symbols — not a missing-module compile error, since SwiftPM exposes the module at the project level.) Do not relocate the scene into another target to make it build.

## Route enums

One enum per route kind. The enum is named `<Scene><Kind>Route` and each case maps to a destination scene by name. Cases carry whatever associated values the destination needs at construction. Modal-style enums are `Identifiable, Hashable` with a stable string `id`:

```swift
enum DashboardNavRoute: Identifiable, Hashable {
    case detail(itemID: String)

    var id: String {
        switch self {
        case .detail: "detail"
        }
    }
}
```

## Nav routing

```swift
enum DashboardNavRoute: Identifiable, Hashable {
    case detail
    var id: String { "detail" }
}

@Observable
class DashboardViewModel {
    var navRoute: DashboardNavRoute?
}

struct DashboardView: View {
    @State private var viewModel = DashboardViewModel()

    var body: some View {
        @Bindable var viewModel = viewModel
        NavigationStack {
            content
                .navigationDestination(item: $viewModel.navRoute) { route in
                    switch route {
                    case .detail: DetailView()
                    }
                }
        }
    }
}
```

The view model sets `navRoute` to navigate; SwiftUI clears it when the user pops or swipes back.

## Modal routing

A `Modal` connector in the diagram doesn't specify *how* the modal is presented — the map's `modal_style` value selects the native modifier:

| `modal_style` | Enum suffix | Property | Modifier |
|---|---|---|---|
| `sheet` | `SheetRoute` | `sheetRoute` | `.sheet(item:)` |
| `full_screen` | `CoverRoute` | `coverRoute` | `.fullScreenCover(item:)` |
| `popover` | `PopoverRoute` | `popoverRoute` | `.popover(item:)` — also apply `.presentationCompactAdaptation(.popover)` to the content, or it falls back to a sheet on iPhone (compact width) |

A single scene can expose several at once - one enum and one route property per presentation style:

```swift
@Observable
class DashboardViewModel {
    var navRoute: DashboardNavRoute?
    var sheetRoute: DashboardSheetRoute?
    var coverRoute: DashboardCoverRoute?
    var popoverRoute: DashboardPopoverRoute?
}

struct DashboardView: View {
    @State private var viewModel = DashboardViewModel()

    var body: some View {
        @Bindable var viewModel = viewModel
        content
            .navigationDestination(item: $viewModel.navRoute) { route in /* ... */ }
            .sheet(item: $viewModel.sheetRoute) { route in /* ... */ }
            .fullScreenCover(item: $viewModel.coverRoute) { route in /* ... */ }
            .popover(item: $viewModel.popoverRoute) { route in /* ... */ }
    }
}
```

For modal styles beyond the standard set above (third-party libraries, project-specific overlay patterns), the project declares them in its `modal_styles` YAML vocabulary and documents the implementations in `README.md` under a **Modal Styles** section — each non-standard style paired with its modifier signature and enum-suffix convention. The project's `README.md` is also where projects declare deliberate overrides of other patterns in this guide.

The choice of presentation style is informal and not encoded in the diagram.

## Child routing

Child routes are mutually-exclusive root views. The enum is non-optional and has a default case.

```swift
enum AppChildRoute {
    case login
    case main
}

@Observable
class AppViewModel {
    var childRoute: AppChildRoute = .login
}

struct AppView: View {
    @State private var viewModel = AppViewModel()

    var body: some View {
        switch viewModel.childRoute {
        case .login: LoginView()
        case .main: MainView()
        }
    }
}
```

## Tab routing

```swift
enum MainTabRoute: Hashable {
    case home
    case library
    case settings
}

@Observable
class MainViewModel {
    var currentTabRoute: MainTabRoute = .home
}
```

The view binds `currentTabRoute` to whatever tab container is in use (`TabView`, a custom material tab bar, etc.).

## Composite scenes

A composite parent has no route enum for its composite children — they're embedded directly in the parent's body.

```swift
struct DetailView: View {
    @State private var viewModel = DetailViewModel()

    var body: some View {
        ScrollView {
            HeaderView(...)
            PlayerView(...)
            // ...
        }
    }
}
```

The composite wrapper in the diagram is a grouping; no Swift artifact corresponds to it.

## Reused scenes

A reused scene is a `View` struct instantiated from multiple parents. It may itself be a full scene with its own routes — e.g. a `PlayerView` used as a composite child in several parents, with its own modal route to a fullscreen presentation.

## Implements

An `Implements: A, B, C` annotation means a single Swift type renders multiple variants, parameterized at construction. The variant is typically carried as an associated value on the route case that targets it:

```swift
enum ProfileNavRoute: Identifiable, Hashable {
    case web(Resource)

    var id: String {
        switch self {
        case .web: "web"
        }
    }
}
```

`WebView(resource:)` renders the page for the given `Resource` (e.g. `.privacyPolicy`, `.termsAndConditions`). One view, one view model, multiple instances.

## State ownership

Routes live on the view model. The view never owns or mutates route state. Mutations come from:

- View-model methods called by the view, e.g. `viewModel.detailTapped()` sets `navRoute = .detail`.
- External publishers observed in the view model's `init`, e.g. an auth service publisher flipping `childRoute` between `.login` and `.main`.
- SwiftUI itself: any modifier bound with `item:` (Nav, Sheet, Cover, Modal, Message, Popover) clears the route back to `nil` when the user dismisses the destination (back button, swipe-back, sheet drag-down, etc.).

The view model can also set or clear any route programmatically at any time — assign `nil` to dismiss, or assign a new value to transition to a different destination.

## Placeholder scenes

Scaffolding placeholder scenes — the `SKAISwiftUI` package, the per-route-kind patterns, the NavigationStack-at-the-presentation-boundary rule, and the dismiss/breadcrumb/nav-title behavior — is covered in its own doc, read only when implementing: [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md).
