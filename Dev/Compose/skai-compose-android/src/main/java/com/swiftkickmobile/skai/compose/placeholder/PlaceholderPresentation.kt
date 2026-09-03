package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.ui.graphics.Color

/**
 * Presents [content] as a modally-presented scene: shows the dismiss control,
 * wires the dismiss action, and appends the presenter's identity to the
 * inherited breadcrumb. Mirrors SKAISwiftUI's
 * `.environment(\.placeholderShowsDismiss, true)` + `.placeholderCrumb(presenter)`.
 *
 * @param presenterTitle The presenting scene's name (appended to the breadcrumb).
 * @param presenterColor The presenting scene's domain color.
 * @param presenterRoutes The presenter's routes, surfaced under its breadcrumb pill.
 * @param onDismiss Pops the modal (e.g. `modalNavController::popBackStack`).
 */
@Composable
fun PlaceholderModalScene(
    presenterTitle: String,
    presenterColor: Color,
    presenterRoutes: List<PlaceholderRoute> = emptyList(),
    onDismiss: () -> Unit,
    content: @Composable () -> Unit,
) {
    val crumbs = LocalPlaceholderCrumbs.current
    CompositionLocalProvider(
        LocalPlaceholderCrumbs provides crumbs + PlaceholderCrumb(presenterTitle, presenterColor, presenterRoutes),
        LocalPlaceholderIsEmbedded provides false,
        LocalPlaceholderShowsDismiss provides true,
        LocalPlaceholderDismiss provides onDismiss,
        // A modal has the dismiss control, never a back arrow — clear any back
        // action inherited from a pushed presenter (e.g. a modal opened from Note).
        LocalPlaceholderBack provides null,
    ) {
        content()
    }
}

/**
 * Presents [content] as a pushed (nav) destination: appends the presenter to the
 * inherited breadcrumb, hides the dismiss control, and supplies the back action
 * for the destination's top-app-bar back arrow. Mirrors `.placeholderCrumb(presenter)`
 * + `.environment(\.placeholderShowsDismiss, false)` + the `NavigationStack` back button.
 *
 * @param presenterTitle The presenting scene's name (appended to the breadcrumb).
 * @param presenterColor The presenting scene's domain color.
 * @param onBack Pops the push stack (e.g. `navController::popBackStack`); shown as
 *   the back arrow.
 * @param presenterRoutes The presenter's routes, surfaced under its breadcrumb pill.
 */
@Composable
fun PlaceholderPushedScene(
    presenterTitle: String,
    presenterColor: Color,
    onBack: () -> Unit,
    presenterRoutes: List<PlaceholderRoute> = emptyList(),
    content: @Composable () -> Unit,
) {
    val crumbs = LocalPlaceholderCrumbs.current
    CompositionLocalProvider(
        LocalPlaceholderCrumbs provides crumbs + PlaceholderCrumb(presenterTitle, presenterColor, presenterRoutes),
        LocalPlaceholderIsEmbedded provides false,
        LocalPlaceholderShowsDismiss provides false,
        LocalPlaceholderBack provides onBack,
    ) {
        content()
    }
}
