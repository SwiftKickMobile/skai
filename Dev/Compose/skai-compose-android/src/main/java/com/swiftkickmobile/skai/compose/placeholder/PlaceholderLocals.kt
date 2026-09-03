package com.swiftkickmobile.skai.compose.placeholder

import androidx.compose.runtime.compositionLocalOf

/**
 * Composition locals that replace SKAISwiftUI's placeholder environment values.
 * The scene reads these to decide its layout (full-bleed vs boxed) and whether
 * to draw a dismiss control; hosts and parents provide them down the tree.
 */

/** Inherited breadcrumb chain. Non-empty means this scene is rendered full-bleed. */
val LocalPlaceholderCrumbs = compositionLocalOf<List<PlaceholderCrumb>> { emptyList() }

/** True only while a scene is rendered directly as embedded composite content. */
val LocalPlaceholderIsEmbedded = compositionLocalOf { false }

/**
 * Whether a placeholder scene should show its dismiss control.
 *
 * Default false: roots, full-bleed children, and composites have nothing to
 * dismiss. A modal host sets it true on the presented scene, and tab content
 * inherits that presentation context. `PlaceholderScene` resets it only for
 * embedded composite content.
 */
val LocalPlaceholderShowsDismiss = compositionLocalOf { false }

/** The dismiss action for a modally-presented scene (e.g. pop the modal nav stack). */
val LocalPlaceholderDismiss = compositionLocalOf<() -> Unit> { {} }

/**
 * The back action for a pushed scene (e.g. pop the push nav stack). Non-null only
 * on pushed destinations; drives the top app bar's back arrow.
 */
val LocalPlaceholderBack = compositionLocalOf<(() -> Unit)?> { null }
