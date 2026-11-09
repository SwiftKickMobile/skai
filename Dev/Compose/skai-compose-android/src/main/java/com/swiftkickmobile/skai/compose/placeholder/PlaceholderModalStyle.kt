package com.swiftkickmobile.skai.compose.placeholder

/**
 * One project-defined modal presentation from the UI Map's top-level
 * `modal_styles` vocabulary.
 *
 * [index] is the style's declaration order in the map. The placeholder library
 * uses it only to order breadcrumb-menu sections; the host owns the actual
 * presentation modifier or navigation builder.
 */
data class PlaceholderModalStyle(
    val id: String,
    val title: String,
    val index: Int,
) {
    init {
        require(id.isNotBlank()) { "Modal style id must not be blank" }
        require(title.isNotBlank()) { "Modal style title must not be blank" }
        require(index >= 0) { "Modal style index must be non-negative" }
    }
}
