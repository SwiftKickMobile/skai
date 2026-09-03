Managed-By: skai
Managed-Id: guide.ui-map-compose
Managed-Source: Guides/UIMap/ui-map-compose.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-02

# UI Map — Compose Multiplatform Reference

Platform reference for implementing a UI Map in Compose Multiplatform or Android-only Jetpack Compose. Companion to [`ui-map-guide.md`](ui-map-guide.md), which defines the platform-agnostic YAML format.

Each scene's routing is implemented locally: the view model emits one-shot navigation effects, and the screen subscribes and dispatches each effect to a Compose Navigation `NavController` scoped to that scene. There is no central router.

## SKAI Compose library

The route types, navigation hosts, navigation extensions, and placeholder UI in these Compose guides come from the local SKAI Compose build at `Submodules/skai/Dev/Compose`. Inspect the source set that will consume it before Code Changes:

- Shared Compose code in `commonMain` uses `com.swiftkickmobile.skai:skai-compose-kmp`.
- Android-only Compose code uses `com.swiftkickmobile.skai:skai-compose-android`.

Use exactly one artifact in a consuming module. When the matching dependency is absent, attaching the included build and artifact is mechanical setup owned by UI Map implementation in Build; Plan records the setup without changing project files. From a conventional repository root, the Gradle settings entry is:

```kotlin
includeBuild("Submodules/skai/Dev/Compose")
```

Select one artifact for the consuming module, then place that dependency where the scene sources can see it. A KMP module declares the KMP artifact in `commonMain`; its platform source sets inherit the same classes, so do not add the Android artifact again:

```kotlin
kotlin {
    sourceSets {
        commonMain.dependencies {
            implementation("com.swiftkickmobile.skai:skai-compose-kmp")
        }
    }
}
```

A plain Android module declares only the Android artifact in its module dependencies:

```kotlin
dependencies {
    implementation("com.swiftkickmobile.skai:skai-compose-android")
}
```

Do not copy the library sources or hand-roll substitutes. If the submodule path is unavailable, or the project's toolchain or target constraints cannot consume either artifact, STOP in Discussion under the implementation guide's missing-mapping rule.

Type-safe routes also require the Kotlin serialization compiler plugin on the **consuming module**; applying it inside the included library does not configure the host. Inspect the consuming module's plugins before Code Changes. When absent, adding `org.jetbrains.kotlin.plugin.serialization` at the Kotlin-compatible version established by the project is mechanical setup owned by UI Map implementation in Build; Plan records it without changing project files. If the project has no compatible plugin version or its conventions prohibit the plugin, STOP in Discussion under the same missing-mapping rule.

The KMP artifact currently targets Android (minimum SDK 29), JVM, `iosArm64`, and `iosSimulatorArm64`; it has no `iosX64` target. The library build's README and version catalog are the authority for its current Kotlin, AGP, Gradle, and Compose versions.

The library packages are `com.swiftkickmobile.skai.compose.navigation` and `com.swiftkickmobile.skai.compose.placeholder`.

## Scene file layout

Map scene IDs are lower snake case. Keep the map ID as the package name and convert each word to UpperCamelCase for code types: `trail_detail` becomes:

```
trail_detail/
  TrailDetailScreen.kt          // @Composable fun TrailDetailScreen(...)
  TrailDetailViewModel.kt       // route enums at the top, then the view-model class
  TrailDetailViewState.kt       // data class for observable scene state
  TrailDetailViewEvent.kt       // sealed interface — UI inputs to the view model
  TrailDetailViewEffect.kt      // sealed interface — one-shot outputs (navigation, toasts, etc.)
  views/                        // optional — TrailDetail's own subviews
```

Place shared Compose scenes under the project's `commonMain` scenes root; place Android-only scenes under its Android source set. The project's established module and source-root conventions choose the exact prefix, while the domain/scene nesting below remains the same.

All of a scene's route enums live at the top of its `<Scene>ViewModel.kt`, above the view-model class. A non-routing scene with no state to manage may omit the view model, view state, event, and effect files entirely — the composable stands alone.

A scene's package may contain a `views/` subpackage for the scene's own subviews — small composables split out to keep `<Scene>Screen.kt` uncluttered. `views/` holds subviews only: never a scene (every scene gets its own package), and never another scene's subviews.

Package nesting mirrors the map's canonical definition nesting inside `domains:` — not references, `primary_parent`, or other inbound routes. Each domain is a package directly under the scenes root, and a scene's package is placed where the map *defines* it (a collapsed domain at the domain package itself; an inline-defined scene inside its container's owning scene's package; a scene in a non-collapsed domain's `scenes:` list directly under the domain package). Every other appearance of a scene is a reference: the referencing scene calls the composable directly — a reference (cross-domain or `primary_parent`) never creates or moves a package.

Scenes in the YAML's top-level `common:` group are domain-agnostic. They live in the shared UI module under its own top-level `Scenes/` package — one package per scene, following the same per-scene layout as any other scene.

## Route enums

Sealed classes implementing a `Route` marker interface, with `@Serializable` cases for type-safe Compose Navigation. Before adding them, confirm the consuming-module serialization-plugin prerequisite in **SKAI Compose library** above. Cases carry whatever associated values the destination needs as `data class` fields.

```kotlin
sealed class DashboardNavRoute : Route {
    @Serializable data object Detail : DashboardNavRoute()
    @Serializable data class Item(val id: String) : DashboardNavRoute()
}
```

## Scene state, events, and effects

A scene with state-management responsibility exposes three types alongside its view model; the stateless, non-routing exemption above remains valid:

- `FooViewState` — a `data class` of observable state; exposed as `StateFlow<FooViewState>`.
- `FooViewEvent` — a `sealed interface` of UI inputs; the screen calls `viewModel.processEvent(event)`.
- `FooViewEffect` — a `sealed interface` of one-shot outputs (navigation, toast, etc.); exposed as `Flow<FooViewEffect>` from a `Channel`.

```kotlin
class DashboardViewModel : ViewModel() {

    private val _viewState = MutableStateFlow(DashboardViewState())
    val viewState: StateFlow<DashboardViewState> = _viewState.asStateFlow()

    private val _viewEffects = Channel<DashboardViewEffect>(Channel.BUFFERED)
    val viewEffects: Flow<DashboardViewEffect> = _viewEffects.receiveAsFlow()

    fun processEvent(event: DashboardViewEvent) { /* … */ }
}
```

The state/event/effect responsibilities are cross-platform; construction and dependency injection follow the consuming source set's project convention. Shared `commonMain` code uses the project's KMP-compatible ViewModel, lifecycle collection, and DI APIs. An Android-only module may use Hilt (`@HiltViewModel`, `@Inject`, and `hiltViewModel()`) when that is its established convention. If a scene needs a view model but the consuming source set has no defined compatible lifecycle/DI pattern, STOP in Discussion rather than introducing one during UI Map implementation.

## Nav routing

The view model emits a `Navigate(route)` effect; the screen dispatches it to the local `NavController`.

```kotlin
sealed class DashboardNavRoute : Route {
    @Serializable data object Detail : DashboardNavRoute()
}

data class Navigate(val route: DashboardNavRoute) : DashboardViewEffect

@Composable
fun DashboardScreen(viewModel: DashboardViewModel) {
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

One `ModalRoute` enum per scene. Every modal destination has a required `modal_style` in the map; that agreed value selects the builder at the `NavHost` declaration site, not in the route enum. Do not infer or substitute a style during implementation.

Every scene that presents a modal owns a `modalNavController` created with `rememberNavController(rememberBottomSheetNavigator())` and overlays one `ModalNavHost`. SKAI defines these standard mappings:

| `modal_style` | Destination builder | Owner and behavior |
|---|---|---|
| `sheet` | `bottomSheetModal<Route>(navHostController = modalNavController) { … }` | SKAI Compose; Material 3 modal bottom sheet, rounded top corners by default, sized to content with partial expansion allowed |
| `full_screen` | `bottomSheetFullScreenModal<Route>(navHostController = modalNavController) { … }` | SKAI Compose; full-size Material 3 sheet, rounded top corners by default, with partial expansion skipped |
| `popover` | `dialog<Route> { … }` | Navigation Compose dialog destination |

Projects may declare any other modal style. Their project-conventions document maps each non-standard style to the actual Compose destination builder or presentation mechanism; the scaffold writes that real project-defined routing call. If neither this table nor project conventions map a declared style, STOP in Discussion under the implementation guide's missing-mapping rule. The placeholder style descriptor records the map vocabulary for breadcrumb grouping but never chooses the builder. The M2 `bottomSheet` builder from `androidx.compose.material.navigation` is still hosted by `ModalNavHost` for legacy code only; new `sheet` destinations use `bottomSheetModal`.

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

ModalNavHost(navController = modalNavController) {
    bottomSheetModal<DashboardModalRoute.Profile>(
        navHostController = modalNavController,
    ) { ProfileScreen() }
    bottomSheetFullScreenModal<DashboardModalRoute.MediaCapture>(
        navHostController = modalNavController,
    ) { MediaCaptureScreen() }
    dialog<DashboardModalRoute.RecordWarning> { RecordWarningDialog() }
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
fun DetailScreen(viewModel: DetailViewModel) {
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
