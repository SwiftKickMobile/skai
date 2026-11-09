Managed-By: skai
Managed-Id: guide.ui-map-compose-placeholders
Managed-Source: Guides/UIMap/ui-map-compose-placeholders.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-07

# UI Map — Jetpack Compose Placeholder Scenes

Print `📖 SKAI guide: ui-map-compose-placeholders` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

How the UI Map **implementation** skill scaffolds scenes in Jetpack Compose: skeleton + navigation, no feature content. It builds on [`ui-map-compose.md`](ui-map-compose.md) — read its **Scene file layout** and **Route enums** first. Load this guide while auditing, planning, or building whenever placeholder work is in scope, and only then.

Placeholders need two project-vendored libraries SKAI does not distribute yet: the **placeholder library** (the `PlaceholderScene` family — the Compose counterpart to `SKAISwiftUI`) and the **routing library** (`SlideNavHost`, `ModalBottomSheetNavHost`, the `bottomSheet` / `bottomSheetFullScreen` / `dialog` modal builders, the `navigate*` extensions). Before Code Changes, confirm the project provides compatible implementations of the APIs below; if either is absent or incompatible, STOP in Discussion under the implementation guide's *Finding disposition* — never hand-roll a substitute.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

## Build philosophy

Follow this guide for the standard patterns — with standard route kinds and modal styles it alone suffices — and the project `README.md` for overrides and patterns not covered here (e.g. custom modal styles). If a scaffold needs a pattern neither supplies, STOP at a blocked gate citing the missing piece; never invent one.

## The one rule: each scene owns its navigation hosts

Unlike SwiftUI, which keeps **one** `NavigationStack` at the presentation boundary and lets scenes declare destinations into that ambient stack, Compose has no ambient stack — **each scene that navigates owns its host(s)**:

- **nav push** — the scene wraps itself in a `SlideNavHost` whose start destination (`NavStart`) is the scene's own body, with the pushed scenes as sibling destinations.
- **modal** — the scene overlays a `ModalBottomSheetNavHost` (its own `modalNavController`) beside its body in a `Box`.
- **child** — the scene hosts a plain `NavHost` inside a `PlaceholderChildHost`, swapping children with `navigateReplace`.
- **leaf / tabbed-only / composite-only** — no host; the scene is just a `PlaceholderScene`.

A scene that both pushes and presents modals owns both hosts; a pushed or modally-presented destination that itself navigates owns its own in turn (nested hosts are expected).

## API (placeholder library)

- `PlaceholderScene(title, domainColor, routes, tabs)` and `PlaceholderScene(title, domainColor, routes, tabs, embedded = listOf({ … }))` — the scene body; `title` is the scene name from its map ID, `embedded` lists composite children.
- `PlaceholderRoute(label, kind, isCurrent = false) { action }` — one menu route; `kind` is `PlaceholderRouteKind.{Nav, Sheet, FullScreen, Popover, Child}`; `isCurrent = true` omits it from the menu (the **active child**).
- `PlaceholderTab(label, icon) { content }` — one tab; `icon` is an `ImageVector`; see *tab*.
- `PlaceholderChildHost(title, domainColor, routes) { content }` — hosts a child-routed scene full-bleed, passing the parent's breadcrumb to the selected child.
- `PlaceholderColors.domain(index)` — the domain palette by index, matched to the rendered map (mirrors `Bin/ui-map-render.py`).

Two presentation helpers wire the breadcrumb + dismiss/back context on destinations:

- `PlaceholderPushedScene(presenterTitle, presenterColor, onBack) { destination }` — on a **nav** destination: appends the presenting scene to the breadcrumb, hides the dismiss control, and supplies `onBack` (`navController::popBackStack`) for the top-app-bar back arrow.
- `PlaceholderModalScene(presenterTitle, presenterColor, onDismiss) { destination }` — on a **modal** destination: shows the dismiss control (✕), wires `onDismiss`, resets the breadcrumb to the presenter, and clears any inherited back arrow (a modal never shows one). For a sheet, `onDismiss` is the `BottomSheetScope`'s `dismissBottomSheet` (animated); for a `dialog`, it's `navController::popBackStack`.

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

Each scene sets `domainColor` to its domain's slot; a scene in a sub-domain uses its domain's color. `DomainColors` lists every key in `domains`, in declaration order, then `common` when the map has a top-level `common:` group — never only the domains that currently have placeholders. It is shared placeholder infrastructure, like the placeholder library itself: the production skill deletes it once no `UI Map scaffold` markers remain.

## What the library renders for you — don't hand-build these

You declare only `title` / `domainColor` / `routes` / `tabs` / `embedded` and wire the destinations. `PlaceholderScene` handles:

- **Top app bar** — on full-bleed scenes (never embedded composite boxes), a centered title (the scene name) plus a back arrow on pushed scenes (wired via `PlaceholderPushedScene`'s `onBack`); it also insets content below the status bar — the Compose stand-in for SwiftUI's `NavigationStack` nav bar.
- **Breadcrumb** — below the app bar: ancestors + this scene; each segment is a menu of that scene's routes in title-case sections by kind (Nav / Sheet / Full Screen / Popover / Child). Routeless segments render dimmed; the **active child** is omitted; the row scrolls horizontally.
- **Dismiss control** — the ✕, beside the breadcrumb, shown only when presented modally (via `PlaceholderModalScene`).
- **Layout** — full-bleed (no border) for everything except **embedded composite content**, which gets a light-gray fill and is greedy: each embedded child takes an equal share of the available height (mirrors SwiftUI's maxHeight-infinity children).
- **Tabs** — a bottom tab bar (`NavigationBar`); the breadcrumb is accumulated into each tab's content. Each tab takes an `ImageVector`.

## Route enums

Follow the route-type contract and route file layout in [`ui-map-compose.md`](ui-map-compose.md): `NoteModalRoute` below is `NoteModalRoute.kt`.

```kotlin
sealed class NoteModalRoute : Route {
    @Serializable data object TagPicker : NoteModalRoute()
    @Serializable data object ShareSheet : NoteModalRoute()
}
```

## View models and DI

As a placeholder-only convention, every scaffolded scene gets a **minimal** view model (`class FooViewModel : ViewModel()`), empty until it needs state; the canonical guide still lets production stateless leaves omit one. The file holds nothing else; route declarations stay in their own files. Obtain it with plain `viewModel()`, not `hiltViewModel()`: a skeleton should not need Hilt wiring. Production scenes follow `ui-map-compose.md`; placeholders skip the state/event/effect triad and call `navigatePush` directly from the route action.

## Per route kind

### child

`PlaceholderChildHost` + a plain `NavHost` + `navigateReplace`. Each child route is `PlaceholderRouteKind.Child` and marks `isCurrent` (read from the nav controller). Children swap without a push animation, hence the plain `NavHost`, not `SlideNavHost`.

```kotlin
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

`tabs` on `PlaceholderScene`; each tab's content is the child scene's composable called directly (it owns its own hosts if it navigates — no wrapping at the tab). Tab labels and icons are final: use the ones the inputs give; otherwise pick a reasonable label, and for an icon not given or without an `ImageVector`, a fitting `ImageVector`. The library's bar is the bar: styling it, adding to it, or custom bars aren't scaffold work. A tab added to a real screen's bar is a real-screen route (see *Reaching a scene from a real screen*), not a `tabs` entry. Modal routes ride alongside in the same `Box` (see modal).

```kotlin
PlaceholderScene(
    title = "Library",
    domainColor = DomainColors.library,
    routes = listOf(
        PlaceholderRoute("Profile", PlaceholderRouteKind.Sheet) { modalNavController.navigatePush(LibraryModalRoute.Profile) },
        PlaceholderRoute("Search", PlaceholderRouteKind.FullScreen) { modalNavController.navigatePush(LibraryModalRoute.Search) },
    ),
    tabs = listOf( // from the inputs
        PlaceholderTab("All Notes", Icons.Default.Edit) { NotesScreen() },
        PlaceholderTab("Folders", Icons.Default.Menu) { FoldersScreen() },
        PlaceholderTab("Trash", Icons.Default.Delete) { TrashScreen() },
    ),
)
```

### nav

The scene owns a `SlideNavHost`: `composable<NavStart>` is its own body; each pushed scene is a sibling destination wrapped in `PlaceholderPushedScene`. The route action calls `navController.navigatePush(route)`.

```kotlin
@Composable
fun NotesScreen(viewModel: NotesViewModel = viewModel()) {
    val navController = rememberNavController()
    SlideNavHost(navController, startDestination = NavStart) {
        composable<NavStart> {
            PlaceholderScene(
                title = "Notes",
                domainColor = DomainColors.library,
                routes = listOf(
                    PlaceholderRoute("Note", PlaceholderRouteKind.Nav) { navController.navigatePush(NotesNavRoute.Note) },
                ),
            )
        }
        composable<NotesNavRoute.Note> {
            PlaceholderPushedScene("Notes", DomainColors.library, onBack = navController::popBackStack) {
                NoteScreen()
            }
        }
    }
}
```

### modal

The scene overlays a `ModalBottomSheetNavHost` (its own `modalNavController = rememberNavController(rememberBottomSheetNavigator())`) beside its body in a `Box`. Each destination is wrapped in `PlaceholderModalScene`. Use the `modal_style` → builder mapping in [`ui-map-compose.md`](ui-map-compose.md); the dismiss callback is:

| Builder | Dismiss passed to `PlaceholderModalScene` |
| --- | --- |
| `bottomSheet<Route>(navHostController = modalNavController) { … }` | `{ dismissBottomSheet() }` |
| `bottomSheetFullScreen<Route>(navHostController = modalNavController) { … }` | `{ dismissBottomSheet() }` |
| `dialog<Route> { … }` | `modalNavController::popBackStack` |

`bottomSheet` / `bottomSheetFullScreen` are the routing library's opaque material3 sheets. Both open **full-height**, skipping the partial detent; the sheet has a rounded top + status-bar gap, the full-screen variant is square edge-to-edge (the difference is cosmetic). Their content runs in a `BottomSheetScope` exposing `dismissBottomSheet()`, an animated close (slide down, then pop); a `dialog` has no slide animation, so it dismisses with a plain `popBackStack`.

```kotlin
@Composable
fun NoteScreen(viewModel: NoteViewModel = viewModel()) {
    val modalNavController = rememberNavController(rememberBottomSheetNavigator())
    Box(Modifier.fillMaxSize()) {
        PlaceholderScene(
            title = "Note",
            domainColor = DomainColors.note,
            routes = listOf(
                PlaceholderRoute("Tag Picker", PlaceholderRouteKind.Popover) { modalNavController.navigatePush(NoteModalRoute.TagPicker) },
                PlaceholderRoute("Share Sheet", PlaceholderRouteKind.Sheet) { modalNavController.navigatePush(NoteModalRoute.ShareSheet) },
            ),
            embedded = listOf({ EditorScreen() }),
        )
        ModalBottomSheetNavHost(navController = modalNavController) {
            dialog<NoteModalRoute.TagPicker> {
                PlaceholderModalScene("Note", DomainColors.note, onDismiss = modalNavController::popBackStack) {
                    TagPickerScreen()
                }
            }
            bottomSheet<NoteModalRoute.ShareSheet>(navHostController = modalNavController) {
                PlaceholderModalScene("Note", DomainColors.note, onDismiss = { dismissBottomSheet() }) {
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
