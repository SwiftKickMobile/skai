package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.ui.graphics.Color

/**
 * Shared color palette for placeholder scenes.
 *
 * The domain colors mirror the UI Map render's `DOMAIN_PALETTE`
 * (`Bin/ui-map-render.py`) in declaration order, so a scaffolded scene's tint
 * matches its node color in the rendered map. `composite` is the light-gray
 * fill the render uses for composite wrappers.
 *
 * This mirrors SKAISwiftUI's `Colors`. Values are duplicated from the render
 * script's palette for now; deduplication is a later concern.
 */
object PlaceholderColors {
    private val palette = listOf(
        Color(0xFF8AD1FA),
        Color(0xFFEFD74E),
        Color(0xFFFE9CA8),
        Color(0xFF78DB85),
        Color(0xFFD39AE7),
        Color(0xFFFFB677),
        Color(0xFF87AFFF),
        Color(0xFF37D8CB),
        Color(0xFFF277D5),
    )

    /**
     * The tint for the domain at [index] in UI Map declaration order.
     * Wraps when a map has more domains than the renderer palette.
     */
    fun domain(index: Int): Color {
        require(index >= 0) { "Domain index must be non-negative" }
        return palette[index % palette.size]
    }

    /** Light-gray fill for composite scenes (mirrors the render's `#f0f0f0`). */
    val composite = Color(0xFFF0F0F0)
}
