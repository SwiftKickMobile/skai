Managed-By: skai
Managed-Id: guide.ui-map-compose
Managed-Source: Guides/UIMap/ui-map-compose.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-07

# UI Map — Jetpack Compose Reference

Print `📖 SKAI guide: ui-map-compose` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Platform reference for implementing a UI Map in Jetpack Compose; companion to [`ui-map-guide.md`](ui-map-guide.md), the platform-agnostic YAML format.

Everything you write for a person follows [`writing-style.md`](../Core/writing-style.md); read it before writing.

Routing is local, with no central router: the view model emits one-shot navigation effects and the screen dispatches them to a Compose Navigation `NavController` scoped to the scene. Deliberate overrides of any pattern here go in the project's `README.md` or an equivalent conventions doc; "README" here and in the placeholder guide means either.

## Scene file layout

Map scene IDs are lower snake case; the package name drops the underscores and each word becomes UpperCamelCase in code types: `trail_detail` becomes:

```
traildetail/
  TrailDetailScreen.kt          // @Composable fun TrailDetailScreen(viewModel: TrailDetailViewModel = hiltViewModel())
  TrailDetailViewModel.kt       // @HiltViewModel class TrailDetailViewModel : ViewModel()
  TrailDetailNavRoute.kt        // sealed class TrailDetailNavRoute — one file per nav, tab or child route kind
  TrailDetailModalRoute.kt      // sealed class TrailDetailModalRoute — all of the scene's modal destinations
  TrailDetailViewState.kt       // data class for observable scene state
  TrailDetailViewEvent.kt       // sealed interface — UI inputs to the view model
  TrailDetailViewEffect.kt      // sealed interface — one-shot outputs (navigation, toasts, etc.)
  views/                        // optional — TrailDetail's own subviews
```

A non-routing, stateless scene may omit the view model, view state, event and effect files; the composable stands alone.

An optional `views/` subpackage holds the scene's own small composables, keeping `<Scene>Screen.kt` uncluttered — never a scene (each gets its own package) or another scene's subviews.

Package nesting mirrors where the map *defines* each scene inside `domains:`, never references, `primary_parent`, or other inbound routes. Each domain is a package directly under the top-level `scenes/` package; within it, a collapsed domain's root scene is the domain package itself, an inline-defined scene nests in its container's owning scene's package, and a scene listed in a non-collapsed domain's `scenes:` sits directly under the domain package. Every other appearance is a reference — the referencing scene calls the composable directly — and creates or moves nothing.

The YAML's top-level `common:` scenes are domain-agnostic and live in the shared UI module's own top-level `scenes/` package, one package per scene with the same layout.

## Route enums

Sealed classes implementing a `Route` marker interface, with `@Serializable` cases for type-safe Compose Navigation that carry the values the destination needs as `data class` fields. One `<Scene><Kind>Route.kt` per kind sits beside the view model, not inside it, keeping it to state and logic and a navigation change out of its diff.

```kotlin
sealed class DashboardNavRoute : Route {
    @Serializable data object Detail : DashboardNavRoute()
    @Serializable data class Item(val id: String) : DashboardNavRoute()
}
```

## Scene state, events, and effects

Every scene with a view model exposes three sealed types beside it:

- `FooViewState` — a `data class` of observable state, exposed as `StateFlow<FooViewState>`.
- `FooViewEvent` — a `sealed interface` of UI inputs the screen sends via `viewModel.processEvent(event)`.
- `FooViewEffect` — a `sealed interface` of one-shot outputs (navigation, toast, etc.), exposed as `Flow<FooViewEffect>` from a `Channel`.

```kotlin
@HiltViewModel
class DashboardViewModel @Inject constructor() : ViewModel() {

    private val _viewState = MutableStateFlow(DashboardViewState())
    val viewState: StateFlow<DashboardViewState> = _viewState.asStateFlow()

    private val _viewEffects = Channel<DashboardViewEffect>(Channel.BUFFERED)
    val viewEffects: Flow<DashboardViewEffect> = _viewEffects.receiveAsFlow()

    fun processEvent(event: DashboardViewEvent) { /* … */ }
}
```

## Nav routing

The view model emits a `Navigate(route)` effect; the screen hands it to the local `NavController`.

```kotlin
// DashboardNavRoute.kt
sealed class DashboardNavRoute : Route {
    @Serializable data object Detail : DashboardNavRoute()
}

// DashboardViewEffect.kt
data class Navigate(val route: DashboardNavRoute) : DashboardViewEffect

// DashboardScreen.kt
@Composable
fun DashboardScreen(viewModel: DashboardViewModel = hiltViewModel()) {
    val viewState by viewModel.viewState.collectAsStateWithLifecycle()
    val navController = rememberNavController()

    LaunchedEffect(Unit) {
        viewModel.viewEffects.collect { effect ->
            when (effect) {
                is Navigate -> navController.navigatePush(effect.route)
            }
        }
    }

    SlideNavHost(navController = navController) {
        composable<NavStart> { DashboardContent(viewState, viewModel::processEvent) }
        composable<DashboardNavRoute.Detail> { DetailScreen() }
    }
}
```

## Modal routing

One `ModalRoute` enum per scene; each destination's required map `modal_style` selects the builder at the `NavHost` declaration site, not the route enum — never infer or substitute one:

| `modal_style` | Builder |
|---|---|
| `sheet` | `bottomSheet<Route>` |
| `full_screen` | `bottomSheetFullScreen<Route>` |
| `popover` | `dialog<Route>` |

Projects document non-standard styles in `README.md`, each with its builder and the `NavHost` it belongs in.

```kotlin
// DashboardModalRoute.kt
sealed class DashboardModalRoute : Route {
    @Serializable data object Profile : DashboardModalRoute()
    @Serializable data class MediaCapture(val id: String) : DashboardModalRoute()
    @Serializable data object RecordWarning : DashboardModalRoute()
}

// DashboardViewEffect.kt
data class NavigateModal(val route: DashboardModalRoute) : DashboardViewEffect
data object CloseModal : DashboardViewEffect
```

```kotlin
val modalNavController = rememberNavController(rememberBottomSheetNavigator())

LaunchedEffect(Unit) {
    viewModel.viewEffects.collect { effect ->
        when (effect) {
            is NavigateModal -> modalNavController.navigatePush(effect.route)
            is CloseModal    -> modalNavController.popBackStack()
        }
    }
}

ModalBottomSheetNavHost(navController = modalNavController) {
    bottomSheet<DashboardModalRoute.Profile>            { ProfileScreen() }
    bottomSheetFullScreen<DashboardModalRoute.MediaCapture> { MediaCaptureScreen() }
    dialog<DashboardModalRoute.RecordWarning>           { RecordWarningDialog() }
}
```

## Child routing

Child routes replace what the scene renders: the view state holds the start destination; transitions use `navigateReplace`, not `navigatePush`.

```kotlin
// AppChildRoute.kt
sealed class AppChildRoute : Route {
    @Serializable data object Login : AppChildRoute()
    @Serializable data object Main : AppChildRoute()
}

// AppViewState.kt
data class AppViewState(val startDestination: AppChildRoute = AppChildRoute.Login)

// AppViewEffect.kt
data class Navigate(val route: AppChildRoute) : AppViewEffect
```

```kotlin
LaunchedEffect(Unit) {
    viewModel.viewEffects.collect { effect ->
        when (effect) {
            is Navigate -> navController.navigateReplace(effect.route)
        }
    }
}

NavHost(navController = navController, startDestination = viewState.startDestination) {
    composable<AppChildRoute.Login> { LoginScreen() }
    composable<AppChildRoute.Main>  { MainScreen() }
}
```

## Tab routing

The view state carries `currentTabRoute`; the screen binds the tab container in use (`NavigationBar`, `TabRow` + pager, etc.) to it via events.

```kotlin
// MainTabRoute.kt
sealed class MainTabRoute : Route {
    @Serializable data object Home    : MainTabRoute()
    @Serializable data object Library : MainTabRoute()
    @Serializable data object Settings: MainTabRoute()
}

// MainViewState.kt
data class MainViewState(val currentTabRoute: MainTabRoute = MainTabRoute.Home)
```

## Composite scenes

A composite parent has no route enum for its composite children; its body calls them directly.

```kotlin
@Composable
fun DetailScreen(viewModel: DetailViewModel = hiltViewModel()) {
    Column {
        HeaderView(/* … */)
        PlayerView(/* … */)
    }
}
```

The diagram's composite wrapper is a grouping; no Kotlin artifact corresponds to it.

## Reused scenes

A reused scene is a `@Composable` function called from several parents, possibly a full scene with its own routes — e.g. a `PlayerScreen` composite child of several parents with a modal route to a fullscreen variant.

## Implements

An `Implements: A, B, C` annotation means one composable renders several variants, parameterized at call site; the variant typically rides as a field on the targeting route case:

```kotlin
sealed class ProfileNavRoute : Route {
    @Serializable data class Web(val resource: Resource) : ProfileNavRoute()
}
```

`WebScreen(resource = …)` renders the page for its `Resource` (e.g. `PrivacyPolicy`, `TermsAndConditions`): one composable, one view model, many instances.

## Placeholder scenes

Placeholder scaffolding (placeholder library API, per-route-kind patterns, the each-scene-owns-its-navigation-hosts rule, dismiss/breadcrumb behavior) has its own doc, read only when implementing: [`ui-map-compose-placeholders.md`](ui-map-compose-placeholders.md).

## State ownership

Route state lives in the local `NavController`: Compose Navigation is the source of truth; the screen never reads the current route from the view model, which only signals *intent* via one-shot effects (`Navigate`, `NavigateModal`, `CloseModal`) the screen dispatches to the right `NavController`.

Effects come from:

- `processEvent` handlers the screen calls, e.g. a click handler sending `Navigate(…)` to the effect channel.
- External flows the view model's `init` observes, e.g. an auth flow sending `Navigate(AppChildRoute.Login)` on logout.
- Compose Navigation handles dismissal itself: system back, drag-to-dismiss and outside-tap pop the back stack; the view model pops programmatically via `CloseModal`.

## Project Addendum

If `<active-project-root>/skai/addenda/ui-map-compose-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
