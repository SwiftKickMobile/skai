package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Star
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.vector.ImageVector

/**
 * One tab in a tabbed placeholder scene.
 *
 * Each tab hosts a child scene's placeholder, so click-through exercises real
 * tab switching rather than a faked stack.
 *
 * @param label Tab label — the child scene's name.
 * @param icon Icon for the tab item; defaults to a generic placeholder glyph.
 * @param content The tab's hosted child-scene placeholder.
 */
data class PlaceholderTab(
    val label: String,
    val icon: ImageVector = Icons.Default.Star,
    val content: @Composable () -> Unit,
)
