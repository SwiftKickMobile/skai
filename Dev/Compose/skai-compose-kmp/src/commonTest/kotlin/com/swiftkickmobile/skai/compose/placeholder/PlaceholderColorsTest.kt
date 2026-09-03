package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.ui.graphics.Color
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith

class PlaceholderColorsTest {
    @Test
    fun domainColorsMatchRendererPaletteAndWrap() {
        val expected = listOf(
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

        expected.forEachIndexed { index, color ->
            assertEquals(color, PlaceholderColors.domain(index))
        }
        assertEquals(expected.first(), PlaceholderColors.domain(expected.size))
    }

    @Test
    fun domainRejectsNegativeIndexes() {
        assertFailsWith<IllegalArgumentException> {
            PlaceholderColors.domain(-1)
        }
    }
}
