Managed-By: skai
Managed-Id: guide.ui-map-compose-placeholders
Managed-Source: Guides/UIMap/ui-map-compose-placeholders.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-05-24

# UI Map — Jetpack Compose Placeholder Scenes

How the UI Map **implementation** skill scaffolds scenes in Jetpack Compose: skeleton + navigation, no feature content. Companion to [`ui-map-compose.md`](ui-map-compose.md) — read its **Scene file layout** and **Route enums** sections first; this doc builds on them. Read this doc only when scaffolding placeholders (not for audit or planning).

Placeholders use two copy-in libraries: the **placeholder library** (the `PlaceholderScene` family — the Compose counterpart to `SKAISwiftUI`) and the **routing library** (`SlideNavHost`, `ModalBottomSheetNavHost`, the `bottomSheet` / `bottomSheetFullScreen` / `dialog` modal builders, the `navigate*` extensions). Both are vendored into the app; distribution is a project concern, not a scaffolding one.

## Build philosophy

Follow this guide for the standard patterns; defer to the project `README.md` for overrides and for patterns not covered here (e.g. custom modal styles). With standard route kinds and modal styles, this guide alone suffices — no README required. If a scaffold needs a pattern neither the guide nor the README supplies, STOP at a blocked gate citing the missing piece — do not invent one.

## The one rule: each scene owns its navigation hosts

This is the key difference from SwiftUI. SwiftUI keeps **one** `NavigationStack` at the presentation boundary and scenes declare destinations into that ambient stack. Compose has no ambient stack — **each scene that navigates owns its host(s)**:

- **nav push** — the scene wraps itself in a `SlideNavHost` whose start destination (`NavStart`) is the scene's own body, with the pushed scenes as sibling destinations.
- **modal** — the scene overlays a `ModalBottomSheetNavHost` (its own `modalNavController`) beside its body in a `Box`.
- **child** — the scene hosts a plain `NavHost` inside a `PlaceholderChildHost`, swapping children with `navigateReplace`.
- **leaf / tabbed-only / composite-only** — no host; the scene is just a `PlaceholderScene`.

A scene that both pushes and presents modals owns both hosts. A pushed or modally-presented destination that itself navigates owns its own host in turn (nested hosts are expected and fine).

## API (placeholder library)

- `PlaceholderScene(title, domainColor, routes, tabs)` and `PlaceholderScene(title, domainColor, routes, tabs, embedded = listOf({ … }))` — the scene body. `embedded` is a list of composite children.
- `PlaceholderRoute(label, kind, isCurrent = false) { action }` — one menu route. `kind` is `PlaceholderRouteKind.{Nav, Sheet, FullScreen, Popover, Child}`. `isCurrent = true` omits it from the menu (used for the **active child**).
- `PlaceholderTab(label, icon) { content }` — one tab. `icon` is an `ImageVector`.
- `PlaceholderChildHost(title, domainColor, routes) { content }` — hosts a child-routed scene full-bleed and contributes the parent's breadcrumb to the selected child.
- `PlaceholderColors.{app, library, note, other, common}` — domain tints, matched to the rendered map.

Two presentation helpers wire the breadcrumb + dismiss/back context on destinations:

- `PlaceholderPushedScene(presenterTitle, presenterColor, onBack) { destination }` — on a **nav** destination: appends the presenting scene to the breadcrumb, hides the dismiss control, and supplies `onBack` (`navController::popBackStack`) for the top-app-bar back arrow.
- `PlaceholderModalScene(presenterTitle, presenterColor, onDismiss) { destination }` — on a **modal** destination: shows the dismiss control (✕), wires `onDismiss`, resets the breadcrumb to the presenter, and clears any inherited back arrow (a modal never shows one). For a sheet, `onDismiss` is the `BottomSheetScope`'s `dismissBottomSheet` (animated); for a `dialog`, it's `navController::popBackStack`.

## What the library renders for you — don't hand-build these

You declare only `title` / `domainColor` / `routes` / `tabs` / `embedded` and wire the destinations. `PlaceholderScene` handles:

- **Top app bar** — on full-bleed scenes, a centered title (the scene name) plus a back arrow on pushed scenes (wired via `PlaceholderPushedScene`'s `onBack`). It also insets content below the status bar — the Compose stand-in for SwiftUI's `NavigationStack` nav bar. Embedded composite boxes get no app bar.
- **Breadcrumb** — below the app bar: ancestors + this scene; each segment is a menu of that scene's routes, grouped into title-case sections by kind (Nav / Sheet / Full Screen / Popover / Child). Routeless segments render dimmed; the **active child** is omitted; the row scrolls horizontally.
- **Dismiss control** — the ✕, beside the breadcrumb, shown only when presented modally (via `PlaceholderModalScene`).
- **Layout** — full-bleed (no border) for everything except **embedded composite content**, which gets a light-gray fill and is greedy: each embedded child takes an equal share of the available height (mirrors SwiftUI's maxHeight-infinity children).
- **Tabs** — a bottom tab bar (`NavigationBar`); the breadcrumb is accumulated into each tab's content. Each tab takes an `ImageVector`.

## Route enums

Per `ui-map-compose.md`: a `sealed interface` implementing the `Route` marker, with `@Serializable data object` (or `data class`) cases, for type-safe Compose Navigation. Route enums live at the top of `<Scene>ViewModel.kt`.

```kotlin
sealed interface NoteModalRoute : Route {
    @Serializable data object TagPicker : NoteModalRoute
    @Serializable data object ShareSheet : NoteModalRoute
}
```

## View models and DI

Every scene gets a view model, like every scene in `ui-map-compose.md` — but a placeholder's is **minimal** (`class FooViewModel : ViewModel()`), empty until it needs state. The route enums in the view model file are the only required content. Obtain it with plain `viewModel()`, not `hiltViewModel()`: a skeleton should not require Hilt wiring. (Production scenes use `hiltViewModel()` and the full `ViewState` / `ViewEvent` / `ViewEffect` triad per `ui-map-compose.md`; placeholders skip all of that and call `navigatePush` directly from the route action.)

## Per route kind

### child

`PlaceholderChildHost` + a plain `NavHost` + `navigateReplace`. Each child route is `PlaceholderRouteKind.Child` and marks `isCurrent` (read from the nav controller) so the active one drops out of the menu. Children swap with `navigateReplace` (no push animation), so use the plain `NavHost`, not `SlideNavHost`.

```kotlin
@Composable
fun AppScreen(viewModel: AppViewModel = viewModel()) {
    val navController = rememberNavController()
    val destination = navController.currentBackStackEntryAsState().value?.destination
    PlaceholderChildHost(
        title = "App",
        domainColor = PlaceholderColors.app,
        routes = listOf(
            PlaceholderRoute("Library", PlaceholderRouteKind.Child, isCurrent = destination?.hasRoute(AppChildRoute.Library::class) != false) {
                navController.navigateReplace(AppChildRoute.Library)
            },
            PlaceholderRoute("Login", PlaceholderRouteKind.Child, isCurrent = destination?.hasRoute(AppChildRoute.Login::class) == true) {
                navController.navigateReplace(AppChildRoute.Login)
            },
        ),
    ) {
        NavHost(navController, startDestination = AppChildRoute.Library) {
            composable<AppChildRoute.Library> { LibraryScreen() }
            composable<AppChildRoute.Login> { LoginScreen() }
        }
    }
}
```

### tab

`tabs` on `PlaceholderScene`; each tab's content is the child scene's composable called directly (it owns its own hosts if it navigates — no wrapping at the tab). Give each tab a fitting `ImageVector`. Modal routes (if any) ride alongside in the same `Box` (see modal).

```kotlin
PlaceholderScene(
    title = "Library",
    domainColor = PlaceholderColors.library,
    routes = listOf(
        PlaceholderRoute("Profile", PlaceholderRouteKind.Sheet) { modalNavController.navigatePush(LibraryModalRoute.Profile) },
        PlaceholderRoute("Search", PlaceholderRouteKind.FullScreen) { modalNavController.navigatePush(LibraryModalRoute.Search) },
    ),
    tabs = listOf(
        PlaceholderTab("Notes", Icons.Default.Edit) { NotesScreen() },
        PlaceholderTab("Folders", Icons.Default.Menu) { FoldersScreen() },
        PlaceholderTab("Trash", Icons.Default.Delete) { TrashScreen() },
    ),
)
```

### nav

The scene owns a `SlideNavHost`: `composable<NavStart>` is the scene's own body; each pushed scene is a sibling destination wrapped in `PlaceholderPushedScene`. The route action calls `navController.navigatePush(route)`.

```kotlin
@Composable
fun NotesScreen(viewModel: NotesViewModel = viewModel()) {
    val navController = rememberNavController()
    SlideNavHost(navController, startDestination = NavStart) {
        composable<NavStart> {
            PlaceholderScene(
                title = "Notes",
                domainColor = PlaceholderColors.library,
                routes = listOf(
                    PlaceholderRoute("Note", PlaceholderRouteKind.Nav) { navController.navigatePush(NotesNavRoute.Note) },
                ),
            )
        }
        composable<NotesNavRoute.Note> {
            PlaceholderPushedScene("Notes", PlaceholderColors.library, onBack = navController::popBackStack) {
                NoteScreen()
            }
        }
    }
}
```

### modal

The scene overlays a `ModalBottomSheetNavHost` (its own `modalNavController = rememberNavController(rememberBottomSheetNavigator())`) beside its body in a `Box`. Each destination is wrapped in `PlaceholderModalScene`. The presentation style maps to the builder, chosen at the host (not on the route enum):

| modal style | builder | dismiss passed to `PlaceholderModalScene` |
| --- | --- | --- |
| sheet | `bottomSheet<Route>(navHostController = modalNavController) { … }` | `{ dismissBottomSheet() }` |
| full_screen | `bottomSheetFullScreen<Route>(navHostController = modalNavController) { … }` | `{ dismissBottomSheet() }` |
| popover | `dialog<Route> { … }` | `modalNavController::popBackStack` |

`bottomSheet` / `bottomSheetFullScreen` are the routing library's opaque material3 sheets. Both open **full-height**, skipping the partial detent — matching SalesPro and HomeStory; the sheet has a rounded top + status-bar gap, the full-screen variant is square edge-to-edge (height is the same; the difference is cosmetic). Their content runs in a `BottomSheetScope` that exposes `dismissBottomSheet()` — an animated close (slide down, then pop) — which you pass as the modal's `onDismiss`. A `dialog` has no slide animation, so it dismisses with a plain `popBackStack`.

```kotlin
@Composable
fun NoteScreen(viewModel: NoteViewModel = viewModel()) {
    val modalNavController = rememberNavController(rememberBottomSheetNavigator())
    Box(Modifier.fillMaxSize()) {
        PlaceholderScene(
            title = "Note",
            domainColor = PlaceholderColors.note,
            routes = listOf(
                PlaceholderRoute("Tag Picker", PlaceholderRouteKind.Popover) { modalNavController.navigatePush(NoteModalRoute.TagPicker) },
                PlaceholderRoute("Share Sheet", PlaceholderRouteKind.Sheet) { modalNavController.navigatePush(NoteModalRoute.ShareSheet) },
            ),
            embedded = listOf({ EditorScreen() }),
        )
        ModalBottomSheetNavHost(navController = modalNavController) {
            dialog<NoteModalRoute.TagPicker> {
                PlaceholderModalScene("Note", PlaceholderColors.note, onDismiss = modalNavController::popBackStack) {
                    TagPickerScreen()
                }
            }
            bottomSheet<NoteModalRoute.ShareSheet>(navHostController = modalNavController) {
                PlaceholderModalScene("Note", PlaceholderColors.note, onDismiss = { dismissBottomSheet() }) {
                    ShareSheetScreen()
                }
            }
        }
    }
}
```

### composite

Composite children are listed in `embedded` (shown together, each as its own gray-filled `PlaceholderScene`, sharing the available height equally). No route enum and no host for them — see `embedded = listOf({ EditorScreen() })` in the modal example above.

### leaf

No routes, no tabs, no embedded — but still gets a minimal view model, like every scene.

```kotlin
class ShareSheetViewModel : ViewModel()

@Composable
fun ShareSheetScreen(viewModel: ShareSheetViewModel = viewModel()) {
    PlaceholderScene(title = "Share Sheet", domainColor = PlaceholderColors.note)
}
```

## New-scene inputs — none

A newly scaffolded scene models no inputs: no variant for `implements`, no parameters, and its incoming route case carries no associated value. (Wiring inputs — modeling them on the route enum, asking for a fixture — is the existing-scene case, handled separately.)

## Boundary

Placeholders are skeleton + navigation only. If a scaffold seems to require feature content (real UI, business logic, data), the scene is being over-built — stop. Feature work belongs to a separate work spec.
