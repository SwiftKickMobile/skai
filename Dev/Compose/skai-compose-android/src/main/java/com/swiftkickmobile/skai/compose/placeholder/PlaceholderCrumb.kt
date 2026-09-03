package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.ui.graphics.Color

/**
 * One ancestor entry in a placeholder breadcrumb: a scene's title plus its
 * routes (surfaced as that title's menu).
 *
 * Crumbs accumulate across child-routing, tab, push, and modal boundaries —
 * where the child renders full-bleed and the presenter's identity would
 * otherwise disappear. Embedded/composite content resets the chain, since its
 * nesting is already shown by the surrounding fill.
 */
data class PlaceholderCrumb(
    val title: String,
    val color: Color,
    val routes: List<PlaceholderRoute> = emptyList(),
)
