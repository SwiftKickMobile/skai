package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Star
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.vector.ImageVector
import com.swiftkickmobile.skai.compose.navigation.Route

/**
 * One tab in a tabbed placeholder scene.
 *
 * Each tab is a destination in the scene's tab `NavHost`, switched with
 * `navigateToTab`, so click-through exercises real tab navigation (per-tab
 * state saved and restored, back from any tab root returning to the primary
 * tab) rather than a faked stack.
 *
 * @param label Tab label — the child scene's name.
 * @param route The tab's typed route case. The first tab's route is the primary
 *   tab and the tab host's start destination.
 * @param icon Icon for the tab item; defaults to a generic placeholder glyph.
 * @param content The tab's hosted child-scene placeholder.
 */
data class PlaceholderTab(
    val label: String,
    val route: Route,
    val icon: ImageVector = Icons.Default.Star,
    val content: @Composable () -> Unit,
)
