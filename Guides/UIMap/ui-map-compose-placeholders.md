Managed-By: skai
Managed-Id: guide.ui-map-compose-placeholders
Managed-Source: Guides/UIMap/ui-map-compose-placeholders.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-02

# UI Map — Compose Multiplatform Placeholder Scenes

How the UI Map **implementation** skill scaffolds scenes in Compose Multiplatform or Android-only Jetpack Compose: skeleton + navigation, no feature content. Companion to [`ui-map-compose.md`](ui-map-compose.md) — read its **SKAI Compose library**, **Scene file layout**, **Route enums**, and **Modal routing** sections first; this doc builds on them. Load this doc while auditing, planning, or building whenever placeholder work is in scope; omit it only when no placeholder work is in scope.

The official SKAI Compose library supplies both the routing and placeholder APIs. Follow the dependency-selection and missing-mapping rules in [`ui-map-compose.md`](ui-map-compose.md); do not install a second project-vendored implementation or hand-roll a substitute during scaffolding.

## Build philosophy

Follow this guide for the standard patterns; defer to the project `README.md` for overrides and for patterns not covered here (e.g. custom modal styles). With standard route kinds and modal styles, this guide alone suffices — no README required. If a scaffold needs a pattern neither the guide nor the README supplies, STOP at a blocked gate citing the missing piece — do not invent one.

## The one rule: each scene owns its navigation hosts

This is the key difference from SwiftUI. SwiftUI keeps **one** `NavigationStack` at the presentation boundary and scenes declare destinations into that ambient stack. Compose has no ambient stack — **each scene that navigates owns its host(s)**:

- **nav push** — the scene wraps itself in a `SlideNavHost` whose start destination (`NavStart`) is the scene's own body, with the pushed scenes as sibling destinations.
- **modal** — the scene overlays a `ModalNavHost` (its own `modalNavController`) beside its body in a `Box`.
- **child** — the scene hosts a plain `NavHost` inside a `PlaceholderChildHost`, swapping children with `navigateReplace`.
- **tab** — the scene declares typed tab routes and passes them to `PlaceholderScene`, which owns the tab `NavHost` (a plain `NavHost` whose start destination is the first tab) and switches tabs with `navigateToTab`.
- **leaf / composite-only** — no host; the scene is just a `PlaceholderScene`.

A scene that both pushes and presents modals owns both hosts. A pushed or modally-presented destination that itself navigates owns its own host in turn (nested hosts are expected and fine).

## API (placeholder library)

- `PlaceholderScene(title, domainColor, routes, tabs)` or `PlaceholderScene(title, domainColor, routes, embedded = listOf({ … }))` — the scene body. `embedded` is a list of composite children. The current placeholder renderer does not support nonempty `tabs` and `embedded` together.
- `PlaceholderRoute(label, kind, isCurrent = false) { action }` — one menu route. `kind` is `PlaceholderRouteKind.Nav`, `.Modal(style)`, or `.Child`. `isCurrent = true` omits it from the menu (used for the **active child**).
- `PlaceholderModalStyle(id, title, index)` — one project-defined entry from the map's top-level `modal_styles` vocabulary. It labels and orders the breadcrumb section only; host code owns the actual presentation.
- `PlaceholderTab(label, route, icon) { content }` — one tab. `route` is the tab's typed `Route` case (the first tab is the primary tab and the tab host's start destination); `icon` is an `ImageVector`.
- `PlaceholderChildHost(title, domainColor, routes) { content }` — hosts a child-routed scene full-bleed and contributes the parent's breadcrumb to the selected child.
- `PlaceholderColors.domain(index)` — the domain palette by index, matched to the rendered map (mirrors `Bin/ui-map-render.py`).

Two presentation helpers wire the breadcrumb + dismiss/back context on destinations:

- `PlaceholderPushedScene(presenterTitle, presenterColor, onBack, presenterRoutes) { destination }` — on a **nav** destination: appends the presenting scene and its routes to the breadcrumb, hides the dismiss control, and supplies `onBack` (`navController::popBackStack`) for the top-app-bar back arrow.
- `PlaceholderModalScene(presenterTitle, presenterColor, presenterRoutes, onDismiss) { destination }` — on a **modal** destination: appends the presenting scene to the breadcrumb, shows the dismiss control (✕), wires `onDismiss`, and clears any inherited back arrow (a modal never shows one).

Define a presenter's `routes` list once. Pass that same list to its `PlaceholderScene` and to every pushed or modal destination helper so the presenting breadcrumb segment always exposes the complete route menu.

**Unsupported combined shape.** A real product screen may combine tab and composite content, but the current placeholder renderer has no mapping for that layout. If one mapped scene contains both `tab` and `composite`, STOP in Discussion under the implementation guide's missing-mapping rule. Do not pass both lists, omit either set of mapped children, or invent their relative layout.

## Domain colors

Scaffolded scenes are tinted to match the rendered map. The render colors each domain by its **declaration order**; `PlaceholderColors.domain(index)` returns the tint for that index.

Generate one artifact, `DomainColors.kt`, mapping each domain to its slot in map declaration order:

```kotlin
// 🟡 UI Map scaffold <change-id>
object DomainColors {
    val app = PlaceholderColors.domain(0)
    val library = PlaceholderColors.domain(1)
    val note = PlaceholderColors.domain(2)
    val common = PlaceholderColors.domain(3) // when top-level `common:` exists
}
```

Each scene sets `domainColor` to its domain's slot; a scene in a sub-domain uses its domain's color. `DomainColors` follows the renderer's domain order: every key in `domains`, in declaration order, followed by `common` when the map has a top-level `common:` group. Never track only the domains that currently have placeholders. `DomainColors` is temporary placeholder infrastructure: productionization deletes it once no `UI Map scaffold` markers remain. The combined SKAI Compose dependency may remain for routing; remove it only when neither placeholder nor routing symbols from the library remain in use.

## Modal style descriptors

Generate one `ModalStyles.kt` artifact from the map's complete top-level `modal_styles` list. Convert each style ID to a Kotlin property name, preserve its exact map ID, give it a human-readable title, and assign its declaration index:

```kotlin
// 🟡 UI Map scaffold <change-id>
object ModalStyles {
    val sheet = PlaceholderModalStyle(id = "sheet", title = "Sheet", index = 0)
    val dialog = PlaceholderModalStyle(id = "dialog", title = "Dialog", index = 1)
}
```

Every modal `PlaceholderRoute` uses `PlaceholderRouteKind.Modal` with the shared descriptor for its destination's declared style. Never recreate a descriptor at individual call sites or substitute a different style. The agent still writes the actual builder from [`ui-map-compose.md`](ui-map-compose.md) or project conventions; `PlaceholderModalStyle` does not perform routing.

Like `DomainColors`, `ModalStyles` is temporary placeholder infrastructure and is removed once no `UI Map scaffold` markers remain. Removing it does not remove the production routing implementation or change the map's modal-style vocabulary.

## What the library renders for you — don't hand-build these

You declare only `title` / `domainColor` / `routes` / `tabs` / `embedded` and wire the destinations. `PlaceholderScene` handles:

- **Top app bar** — on full-bleed scenes, a centered title (the scene name) plus a back arrow on pushed scenes (wired via `PlaceholderPushedScene`'s `onBack`). It also insets content below the status bar — the Compose stand-in for SwiftUI's `NavigationStack` nav bar. Embedded composite boxes get no app bar.
- **Breadcrumb** — below the app bar: ancestors + this scene; each segment is a menu of that scene's routes. Sections appear as Nav, modal styles by their map declaration index, then Child. Routeless segments render dimmed; the **active child** is omitted; the row scrolls horizontally and opens on the trailing/current segment.
- **Dismiss control** — the ✕, beside the breadcrumb, shown only when presented modally (via `PlaceholderModalScene`).
- **Layout** — full-bleed (no border) for everything except **embedded composite content**, which gets a light-gray fill and is greedy: each embedded child takes an equal share of the available height (mirrors SwiftUI's maxHeight-infinity children). A crumb-less root or `NavStart` scene is still full-bleed.
- **Tabs** — a bottom tab bar (`NavigationBar`) over the scene's tab `NavHost`; tabs switch with `navigateToTab`, so each tab keeps its own nested stack and back from any tab's root returns to the primary (first) tab. The breadcrumb is accumulated into each tab's content. Each tab takes an `ImageVector`.

## Route enums

Follow the route-type contract in [`ui-map-compose.md`](ui-map-compose.md). Placeholder route declarations live at the top of `<Scene>ViewModel.kt`.

```kotlin
// 🟡 UI Map scaffold <change-id>
sealed class NoteModalRoute : Route {
    @Serializable data object TagPicker : NoteModalRoute()
    @Serializable data object ShareSheet : NoteModalRoute()
}
```

## View models and DI

Every new placeholder file starts with exactly one file-level `// 🟡 UI Map scaffold <change-id>` marker, as required by the implementation guide. This includes each new `<Scene>Screen.kt` and `<Scene>ViewModel.kt`; the examples below retain the marker even where imports are omitted.

As a placeholder-only convention, every scaffolded scene gets a **minimal** view model (`class FooViewModel : ViewModel()`), empty until it needs state; this does not change the canonical guide's allowance for production stateless leaves to omit one. Route declarations, when present, are the minimal view-model file's only required additional content. Use the consuming source set's existing KMP-compatible or Android ViewModel provider; the examples use plain `viewModel()`. Do not introduce Hilt wiring solely for a skeleton. If the source set has no compatible ViewModel/provider convention, STOP in Discussion instead of inventing one. Production scenes follow `ui-map-compose.md`; placeholders skip the production state/event/effect triad and call `navigatePush` directly from the route action.

## Per route kind

### child

`PlaceholderChildHost` + a plain `NavHost` + `navigateReplace`. Each child route is `PlaceholderRouteKind.Child` and marks `isCurrent` (read from the nav controller) so the active one drops out of the menu. Children swap with `navigateReplace` (no push animation), so use the plain `NavHost`, not `SlideNavHost`.

```kotlin
// 🟡 UI Map scaffold <change-id>
@Composable
fun AppScreen(viewModel: AppViewModel = viewModel()) {
    val navController = rememberNavController()
    val destination = navController.currentBackStackEntryAsState().value?.destination
    PlaceholderChildHost(
        title = "App",
        domainColor = DomainColors.app,
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

Declare a `<Scene>TabRoute` enum (one `@Serializable` case per tab, at the top of the scene's ViewModel file) and pass `tabs` to `PlaceholderScene` with each tab's route. `PlaceholderScene` owns the tab `NavHost` — the first tab is the start destination — and switches tabs with `navigateToTab`, so per-tab state is saved and restored and back from any tab's root returns to the first tab. Each tab's content is the child scene's composable called directly (it owns its own hosts if it navigates — no wrapping at the tab). Give each tab a fitting `ImageVector`. Modal routes (if any) ride alongside in the same `Box` (see modal). If the same mapped scene also has composite children, use the unsupported-combined-shape stop above.

```kotlin
// 🟡 UI Map scaffold <change-id>
sealed class LibraryTabRoute : Route {
    @Serializable data object Notes : LibraryTabRoute()
    @Serializable data object Folders : LibraryTabRoute()
    @Serializable data object Trash : LibraryTabRoute()
}
```

```kotlin
// 🟡 UI Map scaffold <change-id>
PlaceholderScene(
    title = "Library",
    domainColor = DomainColors.library,
    routes = listOf(
        PlaceholderRoute("Profile", PlaceholderRouteKind.Modal(ModalStyles.sheet)) { modalNavController.navigatePush(LibraryModalRoute.Profile) },
        PlaceholderRoute("Purchase Confirmation", PlaceholderRouteKind.Modal(ModalStyles.dialog)) { modalNavController.navigatePush(LibraryModalRoute.PurchaseConfirmation) },
    ),
    tabs = listOf(
        PlaceholderTab("Notes", LibraryTabRoute.Notes, Icons.Default.Edit) { NotesScreen() },
        PlaceholderTab("Folders", LibraryTabRoute.Folders, Icons.Default.Menu) { FoldersScreen() },
        PlaceholderTab("Trash", LibraryTabRoute.Trash, Icons.Default.Delete) { TrashScreen() },
    ),
)
```

### nav

The scene owns a `SlideNavHost`: `composable<NavStart>` is the scene's own body; each pushed scene is a sibling destination wrapped in `PlaceholderPushedScene`. The route action calls `navController.navigatePush(route)`.

```kotlin
// 🟡 UI Map scaffold <change-id>
@Composable
fun NotesScreen(viewModel: NotesViewModel = viewModel()) {
    val navController = rememberNavController()
    val routes = listOf(
        PlaceholderRoute("Note", PlaceholderRouteKind.Nav) {
            navController.navigatePush(NotesNavRoute.Note)
        },
    )
    SlideNavHost(navController = navController, startDestination = NavStart) {
        composable<NavStart> {
            PlaceholderScene(
                title = "Notes",
                domainColor = DomainColors.library,
                routes = routes,
            )
        }
        composable<NotesNavRoute.Note> {
            PlaceholderPushedScene(
                "Notes",
                DomainColors.library,
                onBack = navController::popBackStack,
                presenterRoutes = routes,
            ) {
                NoteScreen()
            }
        }
    }
}
```

### modal

The scene overlays a `ModalNavHost` (its own `modalNavController = rememberNavController(rememberBottomSheetNavigator())`) beside its body in a `Box`. Each destination is wrapped in `PlaceholderModalScene`. Use the sole `modal_style` → builder mapping in [`ui-map-compose.md`](ui-map-compose.md). Pass `modalNavController::popBackStack` as the placeholder dismiss action; gestures, outside taps, and system back continue to use the destination's normal navigation dismissal.

```kotlin
// 🟡 UI Map scaffold <change-id>
@Composable
fun NoteScreen(viewModel: NoteViewModel = viewModel()) {
    val modalNavController = rememberNavController(rememberBottomSheetNavigator())
    val routes = listOf(
        PlaceholderRoute("Tag Picker", PlaceholderRouteKind.Modal(ModalStyles.dialog)) {
            modalNavController.navigatePush(NoteModalRoute.TagPicker)
        },
        PlaceholderRoute("Share Sheet", PlaceholderRouteKind.Modal(ModalStyles.sheet)) {
            modalNavController.navigatePush(NoteModalRoute.ShareSheet)
        },
    )
    Box(Modifier.fillMaxSize()) {
        PlaceholderScene(
            title = "Note",
            domainColor = DomainColors.note,
            routes = routes,
            embedded = listOf({ EditorScreen() }),
        )
        ModalNavHost(navController = modalNavController) {
            dialog<NoteModalRoute.TagPicker> {
                PlaceholderModalScene(
                    "Note",
                    DomainColors.note,
                    presenterRoutes = routes,
                    onDismiss = modalNavController::popBackStack,
                ) {
                    TagPickerScreen()
                }
            }
            bottomSheetModal<NoteModalRoute.ShareSheet>(navHostController = modalNavController) {
                PlaceholderModalScene(
                    "Note",
                    DomainColors.note,
                    presenterRoutes = routes,
                    onDismiss = modalNavController::popBackStack,
                ) {
                    ShareSheetScreen()
                }
            }
        }
    }
}
```

### composite

Composite children are listed in `embedded` (shown together, each as its own gray-filled `PlaceholderScene`, sharing the available height equally). No route enum and no host for them — see `embedded = listOf({ EditorScreen() })` in the modal example above. If the same mapped scene also has tabs, use the unsupported-combined-shape stop above.

### leaf

No routes, no tabs, no embedded — but still gets a minimal view model under the placeholder-only convention above.

```kotlin
// 🟡 UI Map scaffold <change-id>
class ShareSheetViewModel : ViewModel()
```

```kotlin
// 🟡 UI Map scaffold <change-id>
@Composable
fun ShareSheetScreen(viewModel: ShareSheetViewModel = viewModel()) {
    PlaceholderScene(title = "Share Sheet", domainColor = DomainColors.note)
}
```

## New-scene inputs — none

A newly scaffolded scene models no inputs: no variant for `implements`, no parameters, and its incoming route case carries no associated value. For a new route to an existing destination, inspect and preserve that destination's parameter contract. When the codebase or project conventions already define the source of every required value, model those values on the route declaration and pass them through; otherwise STOP in Discussion under the implementation guide's missing-input rule. Do not invent fixture data, value sources, or feature behavior.

## Reaching a scene from a real screen

> **TODO (deferred).** The real-screen entry trigger for Compose is deferred to a separate work effort (rebuild-plan D12); no Compose trigger is built yet.

Until it lands or project conventions provide a compatible trigger, routing a new scene from an existing **real** screen has no defined code mapping: STOP in Discussion before Code Changes under the implementation guide's missing-mapping rule. Do not hand-roll or omit the trigger.

## Boundary

Placeholders are skeleton + navigation only. If a scaffold seems to require feature content (real UI, business logic, data), the scene is being over-built — stop. Feature work belongs to a separate work spec.
