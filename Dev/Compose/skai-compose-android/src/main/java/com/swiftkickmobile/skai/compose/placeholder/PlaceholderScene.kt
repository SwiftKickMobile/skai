package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.navigation.NavDestination.Companion.hasRoute
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import com.swiftkickmobile.skai.compose.navigation.navigateToTab

/** Shared layout constants mirroring SKAISwiftUI's `PlaceholderScene`. */
private object PlaceholderDimens {
    val inset = 6.dp
    val content = 12.dp
    val corner = 10.dp
}

/**
 * The placeholder body for a UI Map scene. A scaffolded scene composable invokes
 * this. Mirrors SKAISwiftUI's `PlaceholderScene`.
 *
 * Embedded composite scenes draw their own inset gray fill so nesting remains
 * visible. Layout is inferred from what's declared and presentation context:
 * - Root / leaf: full-bleed with a breadcrumb row.
 * - Full-bleed (carries crumbs from a child host / tab / push, or is modal):
 *   fills edge-to-edge, breadcrumb accumulates ancestors.
 * - Tabbed: a real bottom-tab scaffold over a tab `NavHost` switched with
 *   `navigateToTab`; tab content accumulates this scene.
 *
 * @param title The scene's name (the visible identifier).
 * @param domainColor The scene's domain tint.
 * @param routes Outgoing routes for this scene's breadcrumb menu; empty hides it.
 * @param tabs Tab children rendered as a bottom-tab scaffold, each a typed
 *   destination in the scene's tab `NavHost`; empty for non-tabbed.
 * @param embedded Composite/child scene placeholders, each itself a
 *   `PlaceholderScene` carrying its own inset fill; empty for a leaf scene.
 */
@Composable
fun PlaceholderScene(
    title: String,
    domainColor: Color = PlaceholderColors.domain(0),
    routes: List<PlaceholderRoute> = emptyList(),
    tabs: List<PlaceholderTab> = emptyList(),
    embedded: List<@Composable () -> Unit> = emptyList(),
) {
    val crumbs = LocalPlaceholderCrumbs.current
    val isEmbedded = LocalPlaceholderIsEmbedded.current
    val showsDismiss = LocalPlaceholderShowsDismiss.current

    // Roots and presentation destinations are full-bleed. Only a scene invoked
    // directly as embedded composite content keeps the inset gray treatment;
    // presentation context takes precedence if that scene routes onward.
    val isFullBleed = !isEmbedded || crumbs.isNotEmpty() || showsDismiss

    when {
        tabs.isNotEmpty() -> TabScaffold(title, domainColor, routes, tabs, crumbs)
        isFullBleed -> FullBleedScene(title, domainColor, routes, crumbs, showsDismiss, embedded)
        else -> EmbeddedScene(title, domainColor, routes, crumbs, showsDismiss, embedded)
    }
}

// MARK: - Layout

/**
 * A full-bleed scene (child, pushed, or modal). Gets a top app bar carrying the
 * title (and a back arrow on pushed scenes) — the Compose stand-in for SwiftUI's
 * `NavigationStack` nav bar, which also pushes content clear of the status bar.
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun FullBleedScene(
    title: String,
    domainColor: Color,
    routes: List<PlaceholderRoute>,
    crumbs: List<PlaceholderCrumb>,
    showsDismiss: Boolean,
    embedded: List<@Composable () -> Unit>,
) {
    val onBack = LocalPlaceholderBack.current
    Column(Modifier.fillMaxSize()) {
        CenterAlignedTopAppBar(
            title = { Text(title) },
            navigationIcon = {
                if (onBack != null) {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")
                    }
                }
            },
        )
        SceneContent(
            title, domainColor, routes, crumbs, showsDismiss, embedded,
            Modifier.fillMaxSize(),
        )
    }
}

/** An embedded composite child — an inset, gray-filled box with no app bar. */
@Composable
private fun EmbeddedScene(
    title: String,
    domainColor: Color,
    routes: List<PlaceholderRoute>,
    crumbs: List<PlaceholderCrumb>,
    showsDismiss: Boolean,
    embedded: List<@Composable () -> Unit>,
) {
    SceneContent(
        title, domainColor, routes, crumbs, showsDismiss, embedded,
        Modifier
            .fillMaxSize()
            .padding(PlaceholderDimens.inset)
            .clip(RoundedCornerShape(PlaceholderDimens.corner))
            .background(PlaceholderColors.composite),
    )
}

/** Shared breadcrumb + body, used by both the full-bleed and embedded layouts. */
@Composable
private fun SceneContent(
    title: String,
    domainColor: Color,
    routes: List<PlaceholderRoute>,
    crumbs: List<PlaceholderCrumb>,
    showsDismiss: Boolean,
    embedded: List<@Composable () -> Unit>,
    modifier: Modifier,
) {
    Column(
        modifier = modifier.padding(PlaceholderDimens.content),
        verticalArrangement = Arrangement.spacedBy(16.dp),
    ) {
        Breadcrumb(title, domainColor, routes, crumbs, showsDismiss)
        // Embedded composites are greedy: each takes an equal share of the
        // remaining height (mirrors SwiftUI's maxHeight-infinity children). Their
        // nesting is shown by the box, so the breadcrumb chain resets.
        embedded.forEach { child ->
            Box(
                modifier = Modifier
                    .weight(1f)
                    .fillMaxWidth(),
            ) {
                CompositionLocalProvider(
                    LocalPlaceholderCrumbs provides emptyList(),
                    LocalPlaceholderIsEmbedded provides true,
                    LocalPlaceholderShowsDismiss provides false,
                ) {
                    child()
                }
            }
        }
    }
}

/**
 * Hosts a child-routed scene full-bleed.
 *
 * A child route replaces the parent's content entirely, so the parent draws no
 * box of its own. Instead it renders the selected child filling the available
 * space and appends its identity (title + child-switcher routes) to the
 * breadcrumb the child shows, so the parent stays reachable.
 */
@Composable
fun PlaceholderChildHost(
    title: String,
    domainColor: Color,
    routes: List<PlaceholderRoute> = emptyList(),
    content: @Composable () -> Unit,
) {
    val crumbs = LocalPlaceholderCrumbs.current
    CompositionLocalProvider(
        LocalPlaceholderCrumbs provides crumbs + PlaceholderCrumb(title, domainColor, routes),
    ) {
        Box(Modifier.fillMaxSize()) { content() }
    }
}

// MARK: - Tabs

/**
 * A bottom-tab scaffold over the scene's tab `NavHost`. The first tab is the
 * primary tab (start destination); switching goes through [navigateToTab], so
 * each tab keeps its own nested state and back from any tab's root returns to
 * the primary tab.
 */
@Composable
private fun TabScaffold(
    title: String,
    domainColor: Color,
    routes: List<PlaceholderRoute>,
    tabs: List<PlaceholderTab>,
    parentCrumbs: List<PlaceholderCrumb>,
) {
    val tabNavController = rememberNavController()
    val currentDestination = tabNavController.currentBackStackEntryAsState().value?.destination

    // Delegate the breadcrumb to the tab content: accumulate this scene into the
    // crumbs the selected tab renders under its own layout.
    val effectiveCrumbs = parentCrumbs + PlaceholderCrumb(title, domainColor, routes)

    Scaffold(
        bottomBar = {
            NavigationBar {
                tabs.forEach { tab ->
                    NavigationBarItem(
                        selected = currentDestination?.hasRoute(tab.route::class) == true,
                        onClick = { tabNavController.navigateToTab(tab.route) },
                        icon = { Icon(tab.icon, contentDescription = tab.label) },
                        label = {
                            Text(
                                text = tab.label,
                                maxLines = 1,
                                softWrap = false,
                                overflow = TextOverflow.Ellipsis,
                            )
                        },
                    )
                }
            }
        },
    ) { insets ->
        // Consume the insets so each tab's content (a full-bleed scene with its
        // own top app bar) doesn't re-apply the status-bar inset on top of these.
        Box(
            Modifier
                .padding(insets)
                .consumeWindowInsets(insets)
                .fillMaxSize(),
        ) {
            CompositionLocalProvider(
                LocalPlaceholderCrumbs provides effectiveCrumbs,
                LocalPlaceholderIsEmbedded provides false,
            ) {
                // Tabs swap in place — no push animation.
                NavHost(
                    navController = tabNavController,
                    startDestination = tabs.first().route,
                    enterTransition = { EnterTransition.None },
                    exitTransition = { ExitTransition.None },
                ) {
                    tabs.forEach { tab ->
                        composable(route = tab.route::class) { tab.content() }
                    }
                }
            }
        }
    }
}

// MARK: - Breadcrumb

@Composable
private fun Breadcrumb(
    title: String,
    domainColor: Color,
    routes: List<PlaceholderRoute>,
    crumbs: List<PlaceholderCrumb>,
    showsDismiss: Boolean,
) {
    val scrollState = rememberScrollState()
    val path = crumbs.map { it.title } + title

    LaunchedEffect(path, scrollState.maxValue) {
        scrollState.scrollTo(scrollState.maxValue)
    }

    Row(
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        Row(
            modifier = Modifier
                .weight(1f)
                .horizontalScroll(scrollState),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(6.dp),
        ) {
            crumbs.forEach { crumb ->
                TitleMenu(crumb.title, crumb.routes, crumb.color)
                Text(
                    "›",
                    style = MaterialTheme.typography.titleMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }
            TitleMenu(title, routes, domainColor)
        }
        if (showsDismiss) {
            DismissButton(domainColor)
        }
    }
}

@Composable
private fun TitleMenu(
    title: String,
    routes: List<PlaceholderRoute>,
    color: Color,
) {
    val visible = routes.filter { !it.isCurrent }
    var expanded by remember { mutableStateOf(false) }

    Box {
        Pill(
            title = title,
            color = color,
            dimmed = visible.isEmpty(),
            onClick = if (visible.isEmpty()) null else { -> expanded = true },
        )
        if (visible.isNotEmpty()) {
            DropdownMenu(expanded = expanded, onDismissRequest = { expanded = false }) {
                orderedRouteKinds(visible).forEach { kind ->
                    val kindRoutes = visible.filter { it.kind == kind }
                    if (kindRoutes.isNotEmpty()) {
                        Text(
                            kind.title,
                            style = MaterialTheme.typography.labelSmall,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                            modifier = Modifier.padding(horizontal = 12.dp, vertical = 4.dp),
                        )
                        kindRoutes.forEach { route ->
                            DropdownMenuItem(
                                text = { Text(route.label) },
                                onClick = {
                                    expanded = false
                                    route.action()
                                },
                            )
                        }
                    }
                }
            }
        }
    }
}

private fun orderedRouteKinds(routes: List<PlaceholderRoute>): List<PlaceholderRouteKind> =
    routes
        .map { it.kind }
        .distinct()
        .sortedWith(
            compareBy<PlaceholderRouteKind> { kind ->
                when (kind) {
                    PlaceholderRouteKind.Nav -> 0
                    is PlaceholderRouteKind.Modal -> 1
                    PlaceholderRouteKind.Child -> 2
                }
            }
                .thenBy { kind ->
                    when (kind) {
                        is PlaceholderRouteKind.Modal -> kind.style.index
                        else -> 0
                    }
                }
                .thenBy { it.title },
        )

@Composable
private fun Pill(
    title: String,
    color: Color,
    dimmed: Boolean,
    onClick: (() -> Unit)?,
) {
    Text(
        text = title,
        color = Color.Black,
        style = MaterialTheme.typography.bodyMedium,
        modifier = Modifier
            .alpha(if (dimmed) 0.5f else 1f)
            .clip(RoundedCornerShape(8.dp))
            .background(color)
            .then(if (onClick != null) Modifier.clickable { onClick() } else Modifier)
            .padding(horizontal = 8.dp, vertical = 3.dp),
    )
}

@Composable
private fun DismissButton(color: Color) {
    val dismiss = LocalPlaceholderDismiss.current
    Box(
        modifier = Modifier
            .clip(CircleShape)
            .background(color)
            .clickable { dismiss() }
            .padding(7.dp),
        contentAlignment = Alignment.Center,
    ) {
        Icon(
            Icons.Default.Close,
            contentDescription = "Dismiss",
            tint = Color.Black,
            modifier = Modifier.size(16.dp),
        )
    }
}
