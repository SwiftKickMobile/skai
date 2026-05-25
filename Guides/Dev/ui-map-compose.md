Managed-By: skai
Managed-Id: guide.ui-map-compose
Managed-Source: Guides/Dev/ui-map-compose.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-05-24

# UI Map — Jetpack Compose Reference

Platform reference for implementing a UI Map in Jetpack Compose. Companion to [`ui-map-guide.md`](ui-map-guide.md), which defines the platform-agnostic YAML format.

Each scene's routing is implemented locally: the view model emits one-shot navigation effects, and the screen subscribes and dispatches each effect to a Compose Navigation `NavController` scoped to that scene. There is no central router.

## Scene file layout

For a scene named `Foo`:

```
foo/
  FooScreen.kt          // @Composable fun FooScreen(viewModel: FooViewModel = hiltViewModel())
  FooViewModel.kt       // route enums at the top, then @HiltViewModel class FooViewModel : ViewModel()
  FooViewState.kt       // data class for observable scene state
  FooViewEvent.kt       // sealed interface — UI inputs to the view model
  FooViewEffect.kt      // sealed interface — one-shot outputs (navigation, toasts, etc.)
  views/                // optional — Foo's own subviews
```

All of the scene's route enums live at the top of `FooViewModel.kt`, above the view-model class. A non-routing scene with no state to manage may omit the view model, view state, event, and effect files entirely — the composable stands alone.

A scene's package may contain a `views/` subpackage for the scene's own subviews — small composables split out to keep `FooScreen.kt` uncluttered. `views/` holds subviews only: never a scene (every scene gets its own package), and never another scene's subviews.

Package nesting mirrors the map's domain structure — the package tree reads as the `domains:` tree, not as routing parentage. Each domain is a package directly under the scenes root, and a scene's package is placed where the map *defines* it (a collapsed domain at the domain package itself; an inline-defined scene inside its container's owning scene's package; a scene in a non-collapsed domain's `scenes:` list directly under the domain package). Every other appearance of a scene is a reference: the referencing scene calls the composable directly — a reference (cross-domain or `primary_parent`) never creates or moves a package.

Scenes in the YAML's top-level `common:` group are domain-agnostic. They live in the shared UI module under its own top-level `Scenes/` package — one package per scene, following the same per-scene layout as any other scene.

## Route enums

Sealed classes implementing a `Route` marker interface, with `@Serializable` cases for type-safe Compose Navigation. Cases carry whatever associated values the destination needs as `data class` fields.

```kotlin
sealed class DashboardNavRoute : Route {
    @Serializable data object Detail : DashboardNavRoute()
    @Serializable data class Item(val id: String) : DashboardNavRoute()
}
```

## Scene state, events, and effects

Every scene exposes three sealed types alongside its view model:

- `FooViewState` — a `data class` of observable state; exposed as `StateFlow<FooViewState>`.
- `FooViewEvent` — a `sealed interface` of UI inputs; the screen calls `viewModel.processEvent(event)`.
- `FooViewEffect` — a `sealed interface` of one-shot outputs (navigation, toast, etc.); exposed as `Flow<FooViewEffect>` from a `Channel`.

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

The view model emits a `Navigate(route)` effect; the screen dispatches it to the local `NavController`.

```kotlin
sealed class DashboardNavRoute : Route {
    @Serializable data object Detail : DashboardNavRoute()
}

data class Navigate(val route: DashboardNavRoute) : DashboardViewEffect

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

One `ModalRoute` enum per scene. The presentation style (dialog, bottom sheet, full-screen composable) is chosen at the `NavHost` declaration site, not in the route enum:

```kotlin
sealed class DashboardModalRoute : Route {
    @Serializable data object Profile : DashboardModalRoute()
    @Serializable data class MediaCapture(val id: String) : DashboardModalRoute()
    @Serializable data object RecordWarning : DashboardModalRoute()
}

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
    composable<DashboardModalRoute.MediaCapture>        { MediaCaptureScreen() }
    dialog<DashboardModalRoute.RecordWarning>           { RecordWarningDialog() }
}
```

## Child routing

Child routes replace what the scene renders. The start destination lives on the view state; transitions use `navigateReplace` instead of `navigatePush`.

```kotlin
sealed class AppChildRoute : Route {
    @Serializable data object Login : AppChildRoute()
    @Serializable data object Main : AppChildRoute()
}

data class AppViewState(val startDestination: AppChildRoute = AppChildRoute.Login)

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

The view state carries `currentTabRoute`. The screen uses a pager and tab row, syncing the pager's position to the route via events.

```kotlin
sealed class MainTabRoute : Route {
    @Serializable data object Home    : MainTabRoute()
    @Serializable data object Library : MainTabRoute()
    @Serializable data object Settings: MainTabRoute()
}

data class MainViewState(val currentTabRoute: MainTabRoute = MainTabRoute.Home)
```

## Composite scenes

A composite parent has no route enum for its composite children — they're called directly as composables in the parent's body.

```kotlin
@Composable
fun DetailScreen(viewModel: DetailViewModel = hiltViewModel()) {
    Column {
        HeaderView(/* … */)
        PlayerView(/* … */)
    }
}
```

The composite wrapper in the diagram is a grouping; no Kotlin artifact corresponds to it.

## Reused scenes

A reused scene is a `@Composable` function called from multiple parents. It may itself be a full scene with its own routes — e.g. a `PlayerScreen` used as a composite child in several parents, with its own modal route to a fullscreen variant.

## Implements

An `Implements: A, B, C` annotation means a single composable renders multiple variants, parameterized at call site. The variant is typically carried as a field on the route case that targets it:

```kotlin
sealed class ProfileNavRoute : Route {
    @Serializable data class Web(val resource: Resource) : ProfileNavRoute()
}
```

`WebScreen(resource = …)` renders the page for the given `Resource` (e.g. `PrivacyPolicy`, `TermsAndConditions`). One composable, one view model, multiple instances.

## Placeholder scenes

Scaffolding placeholder scenes — the placeholder library API, the per-route-kind patterns, the each-scene-owns-its-navigation-hosts rule, and the dismiss/breadcrumb behavior — is covered in its own doc, read only when implementing: [`ui-map-compose-placeholders.md`](ui-map-compose-placeholders.md).

## State ownership

Routes are owned by the local `NavController`, not the view model. The view model expresses *intent* to route via one-shot effects (`Navigate`, `NavigateModal`, `CloseModal`); the screen dispatches each effect to the appropriate `NavController`. The screen never reads the current route from the view model — Compose Navigation is the source of truth.

Effects come from:

- `processEvent` handlers called by the screen, e.g. a click handler that sends `Navigate(…)` to the effect channel.
- External flows observed in the view model's `init`, e.g. an auth flow that sends `Navigate(AppChildRoute.Login)` when the user logs out.
- Compose Navigation itself handles dismissal: system back press, drag-to-dismiss, and outside-tap pop the back stack automatically. The view model can pop programmatically via `CloseModal`.
