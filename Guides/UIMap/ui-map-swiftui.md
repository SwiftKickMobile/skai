Managed-By: skai
Managed-Id: guide.ui-map-swiftui
Managed-Source: Guides/UIMap/ui-map-swiftui.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-07

# UI Map — SwiftUI Reference

Print `📖 SKAI guide: ui-map-swiftui` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Platform reference for implementing a UI Map in SwiftUI; companion to [`ui-map-guide.md`](ui-map-guide.md), the platform-agnostic YAML format.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

Routing is local, with no central router: the view model owns the outgoing route state as properties and the view applies SwiftUI modifiers driven by them. Deliberate overrides of any pattern here go in the project's `README.md` or an equivalent conventions doc — what README means here and in the placeholder guide.

## Scene file layout

Map scene IDs are lower snake case; each word becomes UpperCamelCase for scene folders and code types: `trail_detail` becomes `TrailDetail`, so its standard layout is:

```
TrailDetail/
  TrailDetailView.swift          // struct TrailDetailView: View
  TrailDetailViewModel.swift     // @Observable class TrailDetailViewModel
  TrailDetailNavRoute.swift      // enum TrailDetailNavRoute — one file per nav, tab or child route kind
  TrailDetailModalRoute.swift    // the scene's modal route enums, together
  Views/                         // optional — TrailDetail's own subviews
```

Every scene, even a leaf with no routes or state, gets a `<Scene>ViewModel`, so layouts are identical and state has a home the moment any is needed.

An optional `Views/` subfolder holds the scene's own small presentational subviews, split out to keep `<Scene>View.swift` uncluttered — never a scene (every scene gets its own folder) or another scene's subviews.

Scenes live under a top-level `Scenes/` folder (root overridable in `README.md`); each domain is a folder directly under it, and a scene's folder sits where the map *defines* it inside `domains:` — never where a reference, `primary_parent`, or other inbound route names it:

- a collapsed domain (domain id == its root scene) → the domain folder is the root scene's folder (e.g. `Library/LibraryView.swift`);
- a scene defined inline under a route container → nests inside the container's owning scene's folder (e.g. `App/Login/Welcome/`);
- a scene defined in a non-collapsed domain's `scenes:` list → sits directly under the domain folder.

Every other appearance is a reference — the referencing scene imports and instantiates it — and **never** creates or moves a folder: a cross-domain reference does not pull the scene into the referrer's domain, and `primary_parent` is a render-only hint. Never place scenes flat.

The YAML's top-level `common:` scenes are domain-agnostic and live in the shared UI module under its own top-level `Scenes/` folder, one folder per scene with the same layout. Scaffolding them applies the `SKAISwiftUI` package-linkage rule in [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md) to the shared module; with no SwiftUI-capable shared module, STOP at a blocked gate rather than relocating the scene into another target to make it build.

## Route enums

One enum per route kind, or per modal style, named `<Scene><Kind>Route`; each case maps to a destination scene by name and carries the associated values the destination needs at construction. It lives in a file of that name beside the view model, not inside it (modal enums share `<Scene>ModalRoute.swift`), keeping the view model to state and logic and a navigation change out of its diff. Enums bound with `item:` (nav and modal) are `Identifiable, Hashable` with a stable string `id`; a tab enum is `Hashable`:

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
// DashboardNavRoute.swift
enum DashboardNavRoute: Identifiable, Hashable {
    case detail
    var id: String { "detail" }
}

// DashboardViewModel.swift
@Observable
class DashboardViewModel {
    var navRoute: DashboardNavRoute?
}

// DashboardView.swift
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

The map's required `modal_style` on every modal destination selects the native modifier; never infer or substitute a style:

| `modal_style` | Enum suffix | Property | Modifier |
|---|---|---|---|
| `sheet` | `SheetRoute` | `sheetRoute` | `.sheet(item:)` |
| `full_screen` | `CoverRoute` | `coverRoute` | `.fullScreenCover(item:)` |
| `popover` | `PopoverRoute` | `popoverRoute` | `.popover(item:)` — also apply `.presentationCompactAdaptation(.popover)` to the content, or iPhone (compact width) shows a sheet instead |

A scene can expose several at once - one enum and one route property per style:

```swift
// DashboardModalRoute.swift
enum DashboardSheetRoute: Identifiable, Hashable { /* ... */ }
enum DashboardCoverRoute: Identifiable, Hashable { /* ... */ }
enum DashboardPopoverRoute: Identifiable, Hashable { /* ... */ }

// DashboardViewModel.swift
@Observable
class DashboardViewModel {
    var navRoute: DashboardNavRoute?
    var sheetRoute: DashboardSheetRoute?
    var coverRoute: DashboardCoverRoute?
    var popoverRoute: DashboardPopoverRoute?
}

// DashboardView.swift
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

Non-standard modal styles (third-party libraries, project-specific overlays) the project declares in its `modal_styles` YAML vocabulary and documents, each with its modifier signature and enum-suffix convention, under a **Modal Styles** section of `README.md`.

## Child routing

Child routes are mutually-exclusive root views; the enum is non-optional with a default case.

```swift
// AppChildRoute.swift
enum AppChildRoute {
    case login
    case main
}

// AppViewModel.swift
@Observable
class AppViewModel {
    var childRoute: AppChildRoute = .login
}

// AppView.swift
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
// MainTabRoute.swift
enum MainTabRoute: Hashable {
    case home
    case library
    case settings
}

// MainViewModel.swift
@Observable
class MainViewModel {
    var currentTabRoute: MainTabRoute = .home
}
```

The view binds `currentTabRoute` to the tab container in use (`TabView`, a custom material tab bar, etc.).

## Composite scenes

A composite parent has no route enum for its composite children — its body embeds them directly.

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

The diagram's composite wrapper is a grouping; no Swift artifact corresponds to it.

## Reused scenes

A reused scene is a `View` struct instantiated from several parents, possibly a full scene with its own routes — e.g. a `PlayerView` composite child of several parents with its own modal route to a fullscreen presentation.

## Implements

An `Implements: A, B, C` annotation means one Swift type renders several variants, parameterized at construction; the variant typically rides as an associated value on the route case that targets it:

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

`WebView(resource:)` renders the page for its `Resource` (e.g. `.privacyPolicy`, `.termsAndConditions`). One view, one view model, multiple instances.

## State ownership

Route state lives on the view model; the view never owns or mutates it. Mutations come from:

- View-model methods the view calls, e.g. `viewModel.detailTapped()` sets `navRoute = .detail`.
- External publishers observed in the view model's `init`, e.g. an auth service publisher flipping `childRoute` between `.login` and `.main`.
- SwiftUI itself: any `item:`-bound modifier (nav, sheet, cover, popover) clears the route to `nil` on user dismissal (back button, swipe-back, sheet drag-down, etc.).

The view model can also set or clear any route programmatically at any time: `nil` dismisses, a new value moves to a different destination.

## Placeholder scenes

Placeholder scaffolding (the `SKAISwiftUI` package, per-route-kind patterns, the NavigationStack-at-the-presentation-boundary rule, dismiss/breadcrumb/nav-title behavior) has its own doc, read only when implementing: [`ui-map-swiftui-placeholders.md`](ui-map-swiftui-placeholders.md).

## Project Addendum

If `<active-project-root>/skai/addenda/ui-map-swiftui-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
