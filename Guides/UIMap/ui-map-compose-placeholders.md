Managed-By: skai
Managed-Id: guide.ui-map-compose-placeholders
Managed-Source: Guides/UIMap/ui-map-compose-placeholders.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-11

# UI Map — Compose Multiplatform Placeholder Scenes

Print `📖 SKAI guide: ui-map-compose-placeholders` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

How the UI Map **implementation** skill scaffolds scenes in Compose Multiplatform or Android-only Jetpack Compose: skeleton + navigation, no feature content. It builds on [`ui-map-compose.md`](ui-map-compose.md) — read its **SKAI Compose library** (which also supplies the placeholder APIs below), **Scene file layout**, **Route enums**, **Scene state, events, and effects** and **Modal routing** first. Load this guide while auditing, planning, or building whenever placeholder work is in scope, and only then.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## Build philosophy

Follow this guide for the standard patterns — with standard route kinds and modal styles it alone suffices — and the project `README.md` for overrides and patterns not covered here (e.g. custom modal styles). If a scaffold needs a pattern neither supplies, STOP at a blocked gate citing the missing piece; never invent one.

## The one rule: each scene owns its navigation hosts

Compose has no ambient stack: **each scene that navigates owns its host(s)**:

- **nav push** — the scene wraps itself in a `SlideNavHost` whose start destination (`NavStart`) is the scene's own body, with the pushed scenes as sibling destinations.
- **modal** — the scene overlays a `ModalNavHost` (its own `modalNavController`), placed as in *Modal routing*.
- **child** — the scene hosts a plain `NavHost` inside a `PlaceholderChildHost`, swapping children with `navigateReplace`.
- **leaf / tabbed-only / composite-only** — no host; the scene is just a `PlaceholderScene`.

A scene that both pushes and presents modals owns both hosts; a pushed or modally-presented destination that itself navigates owns its own in turn (nested hosts are expected).

## API (placeholder library)

- `PlaceholderScene(title, domainColor, routes, tabs)` or `PlaceholderScene(title, domainColor, routes, embedded = listOf({ … }))` — the scene body; `title` is the scene name from its map ID, `embedded` lists composite children (never with `tabs`: see *composite*).
- `PlaceholderRoute(label, kind, isCurrent = false) { action }` — one menu route; `kind` is `PlaceholderRouteKind.Nav`, `.Modal(style)` or `.Child`; `isCurrent = true` omits it from the menu (the **active child**).
- `PlaceholderModalStyle(id, title, index)` — one entry of the map's top-level `modal_styles`; it only labels and orders the breadcrumb section, never presents the modal (see *Modal style descriptors*).
- `PlaceholderTab(label, route, icon) { content }` — one tab; `route` is its `<Scene>TabRoute` case; `icon` is an `ImageVector`; see *tab*.
- `PlaceholderChildHost(title, domainColor, routes) { content }` — hosts a child-routed scene full-bleed, passing the parent's breadcrumb to the selected child.

Two presentation helpers wire the breadcrumb + dismiss/back context on destinations:

- `PlaceholderPushedScene(presenterTitle, presenterColor, onBack, presenterRoutes) { destination }` — on a **nav** destination: appends the presenting scene and its routes to the breadcrumb, hides the dismiss control, and supplies `onBack` (`navController::popBackStack`) for the top-app-bar back arrow.
- `PlaceholderModalScene(presenterTitle, presenterColor, presenterRoutes, onDismiss) { destination }` — on a **modal** destination: appends the presenting scene to the breadcrumb, shows the dismiss control (✕), wires `onDismiss`, and clears any inherited back arrow (a modal never shows one).

Define a presenter's `routes` list once and pass it to its `PlaceholderScene` and every destination helper, so the presenter's breadcrumb segment always shows its full route menu.

## Domain colors

Scaffolded scenes are tinted to match the rendered map. The render colors domains by **declaration order**; `PlaceholderColors.domain(index)` returns the tint for an index.

Generate one file, `DomainColors.kt`, mapping each domain to its slot:

```kotlin
// 🟡 UI Map scaffold <change-id>
object DomainColors {
    val app = PlaceholderColors.domain(0)
    val library = PlaceholderColors.domain(1)
    val note = PlaceholderColors.domain(2)
    val common = PlaceholderColors.domain(3) // when top-level `common:` exists
}
```

Each scene sets `domainColor` to its domain's slot; a scene in a sub-domain uses its domain's color. `DomainColors` lists every key in `domains`, in declaration order, then `common` when the map has a top-level `common:` group — never only the domains that currently have placeholders. It is temporary placeholder infrastructure: the production skill deletes it once no `UI Map scaffold` markers remain. The SKAI Compose dependency stays until no placeholder or routing symbol from it remains.

## Modal style descriptors

Generate one `ModalStyles.kt` from the map's complete top-level `modal_styles` list: each style ID as a Kotlin property name, keeping its exact map ID, with a readable title and its declaration index.

```kotlin
// 🟡 UI Map scaffold <change-id>
object ModalStyles {
    val sheet = PlaceholderModalStyle(id = "sheet", title = "Sheet", index = 0)
    val fullScreen = PlaceholderModalStyle(id = "full_screen", title = "Full Screen", index = 1)
    val popover = PlaceholderModalStyle(id = "popover", title = "Popover", index = 2)
}
```

Every modal `PlaceholderRoute` uses `PlaceholderRouteKind.Modal` with the shared descriptor for its destination's declared style; never recreate one at a call site or substitute another style. Like `DomainColors`, `ModalStyles` is temporary.

## What the library renders for you — don't hand-build these

You declare only `title` / `domainColor` / `routes` / `tabs` / `embedded` and wire the destinations. `PlaceholderScene` handles:

- **Top app bar** — on full-bleed scenes (never embedded composite boxes), a centered title (the scene name) plus a back arrow on pushed scenes (wired via `PlaceholderPushedScene`'s `onBack`); it also insets content below the status bar.
- **Breadcrumb** — below the app bar: ancestors + this scene; each segment is a menu of that scene's routes in sections: Nav, the modal styles in map declaration order, then Child. Routeless segments render dimmed; the **active child** is omitted; the row scrolls horizontally, pinned to the current (trailing) segment.
- **Dismiss control** — the ✕, beside the breadcrumb, shown only when presented modally (via `PlaceholderModalScene`).
- **Layout** — full-bleed (no border) for everything except **embedded composite content**, which gets a light-gray fill and is greedy: each embedded child takes an equal share of the available height. A crumb-less root or `NavStart` scene is still full-bleed.
- **Tabs** — a bottom tab bar (`NavigationBar`); the breadcrumb, and the ✕ when presented modally, carry into each tab's content. Each tab takes an `ImageVector`.

## Route enums

Follow the route-type contract and route file layout in [`ui-map-compose.md`](ui-map-compose.md): `NoteModalRoute` below is `NoteModalRoute.kt`.

```kotlin
// 🟡 UI Map scaffold <change-id>
sealed class NoteModalRoute : Route {
    @Serializable data object TagPicker : NoteModalRoute()
    @Serializable data object ShareSheet : NoteModalRoute()
}
```

## View models and DI

Every new placeholder file, `<Scene>Screen.kt` and `<Scene>ViewModel.kt` included, starts with exactly one file-level `// 🟡 UI Map scaffold <change-id>` marker, as the implementation guide requires; the examples keep it even where imports are omitted.

Placeholder-only: every scaffolded scene gets a **minimal** view model (`class FooViewModel : ViewModel()`), empty until it needs state. Obtain it per *Scene state, events, and effects* (examples use plain `viewModel()`). Placeholders skip the state/event/effect triad and call `navigatePush` directly from the route action.

## Per route kind

### child

`PlaceholderChildHost` + a plain `NavHost` + `navigateReplace`. Each child route is `PlaceholderRouteKind.Child` and marks `isCurrent` (read from the nav controller). Children swap without a push animation, hence the plain `NavHost`, not `SlideNavHost`.

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

Declare a `<Scene>TabRoute` (one case per tab) and pass `tabs` to `PlaceholderScene`, each with its route. Each tab's content is the child scene's composable called directly (it owns its own hosts if it navigates — no wrapping at the tab). Tab labels and icons are final: use the ones the inputs give; otherwise pick a reasonable label, and for an icon not given or without an `ImageVector`, a fitting `ImageVector`. The library's bar is the bar: styling it, adding to it, or custom bars aren't scaffold work. A tab added to a real screen's bar is a real-screen route (see *Reaching a scene from a real screen*), not a `tabs` entry. Modal routes ride alongside in the `Box` with the scene's `ModalNavHost` (see modal).

```kotlin
// LibraryTabRoute.kt
// 🟡 UI Map scaffold <change-id>
sealed class LibraryTabRoute : Route {
    @Serializable data object Notes : LibraryTabRoute()
    @Serializable data object Folders : LibraryTabRoute()
    @Serializable data object Trash : LibraryTabRoute()
}

// LibraryScreen.kt
// 🟡 UI Map scaffold <change-id>
PlaceholderScene(
    title = "Library",
    domainColor = DomainColors.library,
    routes = listOf(
        PlaceholderRoute("Profile", PlaceholderRouteKind.Modal(ModalStyles.sheet)) { modalNavController.navigatePush(LibraryModalRoute.Profile) },
        PlaceholderRoute("Search", PlaceholderRouteKind.Modal(ModalStyles.fullScreen)) { modalNavController.navigatePush(LibraryModalRoute.Search) },
    ),
    tabs = listOf( // labels and icons from the inputs
        PlaceholderTab("All Notes", LibraryTabRoute.Notes, Icons.Default.Edit) { NotesScreen() },
        PlaceholderTab("Folders", LibraryTabRoute.Folders, Icons.Default.Menu) { FoldersScreen() },
        PlaceholderTab("Trash", LibraryTabRoute.Trash, Icons.Default.Delete) { TrashScreen() },
    ),
)
```

### nav

The scene owns a `SlideNavHost`: `composable<NavStart>` is its own body; each pushed scene is a sibling destination wrapped in `PlaceholderPushedScene`. The route action calls `navController.navigatePush(route)`.

```kotlin
// 🟡 UI Map scaffold <change-id>
@Composable
fun NotesScreen(viewModel: NotesViewModel = viewModel()) {
    val navController = rememberNavController()
    val routes = listOf(
        PlaceholderRoute("Note", PlaceholderRouteKind.Nav) { navController.navigatePush(NotesNavRoute.Note) },
    )
    SlideNavHost(navController = navController) {
        composable<NavStart> {
            PlaceholderScene(title = "Notes", domainColor = DomainColors.library, routes = routes)
        }
        composable<NotesNavRoute.Note> {
            PlaceholderPushedScene("Notes", DomainColors.library, onBack = navController::popBackStack, presenterRoutes = routes) {
                NoteScreen()
            }
        }
    }
}
```

### modal

The scene sets up its `modalNavController` and `ModalNavHost` as in *Modal routing*. Each destination is wrapped in `PlaceholderModalScene`. Use the `modal_style` → builder mapping in [`ui-map-compose.md`](ui-map-compose.md), passing `modalNavController::popBackStack` as `onDismiss`; gestures, outside taps and system back keep the destination's own dismissal.

```kotlin
// 🟡 UI Map scaffold <change-id>
@Composable
fun NoteScreen(viewModel: NoteViewModel = viewModel()) {
    val modalNavController = rememberNavController(rememberBottomSheetNavigator())
    val routes = listOf(
        PlaceholderRoute("Tag Picker", PlaceholderRouteKind.Modal(ModalStyles.popover)) { modalNavController.navigatePush(NoteModalRoute.TagPicker) },
        PlaceholderRoute("Share Sheet", PlaceholderRouteKind.Modal(ModalStyles.sheet)) { modalNavController.navigatePush(NoteModalRoute.ShareSheet) },
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
                PlaceholderModalScene("Note", DomainColors.note, presenterRoutes = routes, onDismiss = modalNavController::popBackStack) {
                    TagPickerScreen()
                }
            }
            bottomSheetModal<NoteModalRoute.ShareSheet>(navHostController = modalNavController) {
                PlaceholderModalScene("Note", DomainColors.note, presenterRoutes = routes, onDismiss = modalNavController::popBackStack) {
                    ShareSheetScreen()
                }
            }
        }
    }
}
```

### composite

Composite children are listed in `embedded` (shown together, each as its own gray-filled `PlaceholderScene`, sharing the available height equally). No route enum and no host for them — see `embedded = listOf({ EditorScreen() })` in the modal example above. A scene with both tabs and composite children has no placeholder shape: STOP in Discussion under the implementation guide's *Finding disposition*.

### leaf

No routes, tabs or embedded — but, under the placeholder-only convention above, a minimal view model.

```kotlin
// ShareSheetViewModel.kt
// 🟡 UI Map scaffold <change-id>
class ShareSheetViewModel : ViewModel()

// ShareSheetScreen.kt
// 🟡 UI Map scaffold <change-id>
@Composable
fun ShareSheetScreen(viewModel: ShareSheetViewModel = viewModel()) {
    PlaceholderScene(title = "Share Sheet", domainColor = DomainColors.note)
}
```

## New-scene inputs — none

A newly scaffolded scene models no inputs: no variant for `implements`, no parameters, and its incoming route case carries no associated value. A new route to an existing destination inspects and preserves its parameter contract: when the codebase or project conventions already define every required value's source, model those values on the route declaration and pass them through; otherwise STOP in Discussion. Never invent fixture data, value sources, or feature behavior.

## Reaching a scene from a real screen

> **TODO (deferred).** The real-screen entry trigger for Compose is deferred to separate work; none is built yet.

Until it lands or project conventions provide a compatible trigger, routing a new scene from an existing **real** screen, a tab added to a real screen's bar included, has no defined code mapping: STOP in Discussion before Code Changes under the implementation guide's *Finding disposition*. Do not hand-roll or omit the trigger.

## Boundary

Placeholders are skeleton + navigation only: a scaffold that seems to require feature content (real UI, business logic, data) is over-built — stop; feature work belongs to a separate dev spec.

## Project Addendum

If `<active-project-root>/skai/addenda/ui-map-compose-placeholders-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
