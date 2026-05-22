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

All of the scene's route enums live at the top of `FooViewModel.swift`, above the view-model class. A non-routing scene with no state to manage may omit `FooViewModel.swift` entirely — the view stands alone.

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

A single scene can expose several at once — one enum and one route property per presentation style:

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

The implementation skill scaffolds each new scene as a **placeholder** — skeleton + navigation, no feature content. Placeholders are built from the `PlaceholderScene` view shipped by the `SKAISwiftUI` package (the host depends on it via a local path through the skai submodule).

**Build philosophy.** Follow this guide for the standard patterns; defer to the project's `README.md` for overrides and for patterns this guide doesn't cover (e.g. a project's custom modal styles). A project `README.md` is only needed when a scene uses a non-standard pattern or override; with standard route kinds and modal styles, this guide alone suffices — no README required. If a scaffold needs a non-standard pattern that neither the guide nor the README supplies, STOP at a blocked gate citing the missing piece — do not invent one.

**Scene structure.** A scaffolded scene follows the standard Scene file layout above: its own per-scene folder under `Scenes/`, **placed by domain per that layout** (not flat), with `FooView.swift` plus `FooViewModel.swift` when it routes. The view's `body` is a single `PlaceholderScene(...)` invocation declaring the scene's title, outgoing routes, tabs, and embedded children. Every `PlaceholderScene` draws its own inset border and shows the scene name, so a click-through can confirm which scene was reached.

**Per route kind.** The scaffolded scene wires the actual native routing from the route-kind sections above (Nav routing, Modal routing, Child routing, Tab routing, Composite scenes) and uses `PlaceholderScene` as the content those modifiers wrap. `PlaceholderScene` supplies the visible identity, the Routes menu, and dismiss — it does not itself present destinations. The Routes menu's `action` closures set the route properties — driving the native presentation (nav/modal) or swapping the embedded child (child routes).

- **nav** → standard route enum + `navRoute` property; the view wraps `PlaceholderScene` in a `NavigationStack` and applies `.navigationDestination(item:)`. A scene that owns a nav route owns its own `NavigationStack` — including when it is rendered as a tab child. A Routes menu item sets `navRoute`.
- **modal** → standard route enum + a route property for the destination's declared `modal_style`. The `modal_style` lives on the *destination* scene in the map; the *presenting parent* reads it to choose its modifier. The view applies the matching native modifier on `PlaceholderScene`: `sheet` → `.sheet(item:)`, `full_screen` → `.fullScreenCover(item:)`, `popover` → `.popover(item:)` (also apply `.presentationCompactAdaptation(.popover)` to the destination, or it becomes a sheet on iPhone). A Routes menu item sets the route property. (Non-standard project modal styles come from the project `README.md` — see Build philosophy.)
- **child** → standard child route enum + a **non-optional** `childRoute` property defaulting to the **first child listed in the map** (per Child routing). The children appear in the **Routes menu**; selecting one sets `childRoute`. The `embedded` ViewBuilder shows exactly one child at a time by switching on `childRoute`. (Contrast composite: composite shows *all* its children at once; child shows *one*, swapped via the menu.)
- **composite** → all composite children instantiated directly in the parent's `embedded` ViewBuilder (shown together).
- **tab** → `PlaceholderScene`'s `tabs` render a real `TabView` (the native tab UI); one `PlaceholderTab` per tab child. Tabs compose with embedded content.

**Dismiss.** `PlaceholderScene` shows a dismiss "✕" top-right, driven by `@Environment(\.dismiss)`. No presentation context is passed in; the environment resolves the correct dismissal for nav / sheet / cover / popover and is a no-op where dismissal doesn't apply.

**New-scene inputs — none.** A newly scaffolded scene models no inputs: no variant enum for `implements`, no initializer parameters, and its incoming route case carries no associated value. (Wiring inputs — inspecting an existing destination's initializer, modeling them on the route enum, asking for a fixture — is the existing-scene case, handled separately.)

**Boundary.** Placeholders are skeleton + navigation only. If a scaffold seems to require feature content (real UI, business logic, data), the scene is being over-built — stop. Feature work belongs to a separate work spec.

```swift
// A leaf destination with no onward routes:
struct ShareSheetView: View {
    var body: some View { PlaceholderScene(title: "Share Sheet") }
}

// Native modal routing wired around PlaceholderScene, plus a composite child.
// Route enums + view-model route properties follow the Route enums / State ownership sections.
struct NoteView: View {
    @State private var viewModel = NoteViewModel()
    var body: some View {
        PlaceholderScene(
            title: "Note",
            routes: [
                PlaceholderRoute(label: "Share Sheet") { viewModel.sheetRoute = .shareSheet },
                PlaceholderRoute(label: "Tag Picker") { viewModel.popoverRoute = .tagPicker },
            ]
        ) {
            EditorView()   // composite child (its own PlaceholderScene)
        }
        .sheet(item: $viewModel.sheetRoute) { route in
            switch route { case .shareSheet: ShareSheetView() }
        }
        .popover(item: $viewModel.popoverRoute) { route in
            switch route { case .tagPicker: TagPickerView().presentationCompactAdaptation(.popover) }
        }
    }
}

// Child routing: children sit in the Routes menu; exactly one is embedded at a time.
// `childRoute` is non-optional with a default (per Child routing).
struct AppView: View {
    @State private var viewModel = AppViewModel()
    var body: some View {
        PlaceholderScene(
            title: "App",
            routes: [
                PlaceholderRoute(label: "Library") { viewModel.childRoute = .library },
                PlaceholderRoute(label: "Login") { viewModel.childRoute = .login },
            ]
        ) {
            switch viewModel.childRoute {
            case .library: LibraryView()
            case .login: LoginView()
            }
        }
    }
}
```
