package com.swiftkickmobile.skai.compose.placeholder

/**
 * The structural kind of a route, used to group breadcrumb-menu items.
 * Modal routes carry the project's own UI Map style descriptor; the descriptor
 * does not choose or perform the presentation.
 */
sealed interface PlaceholderRouteKind {
    val title: String

    data object Nav : PlaceholderRouteKind {
        override val title = "Nav"
    }

    data class Modal(val style: PlaceholderModalStyle) : PlaceholderRouteKind {
        override val title: String = style.title
    }

    data object Child : PlaceholderRouteKind {
        override val title = "Child"
    }
}

/**
 * One entry in a placeholder scene's "Routes" menu.
 *
 * Each route maps to an outgoing destination. Selecting the menu item runs
 * [action], which fires the route (e.g. a navController call the host owns).
 *
 * @param label Menu-item label — the destination scene's name.
 * @param kind The route's presentation kind — groups the menu item into a section.
 * @param isCurrent When true, the route targets the currently-selected
 *   destination (e.g. the active child) and is omitted from the menu.
 * @param action Fires the route. The host owns whatever route state it uses
 *   (nav controller, etc.); this closure decouples the placeholder from that.
 */
data class PlaceholderRoute(
    val label: String,
    val kind: PlaceholderRouteKind,
    val isCurrent: Boolean = false,
    val action: () -> Unit,
)
