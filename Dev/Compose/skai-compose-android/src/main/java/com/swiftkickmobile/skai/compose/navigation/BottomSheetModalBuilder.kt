package com.swiftkickmobile.skai.compose.navigation

import androidx.compose.foundation.layout.ColumnScope
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.graphics.Shape
import androidx.compose.ui.util.fastForEach
import androidx.navigation.NamedNavArgument
import androidx.navigation.NavBackStackEntry
import androidx.navigation.NavDeepLink
import androidx.navigation.NavGraphBuilder
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.ComposeNavigator
import androidx.navigation.compose.ComposeNavigatorDestinationBuilder
import androidx.navigation.get
import kotlin.reflect.KType

/**
 * Add the [content] [Composable] as a bottom sheet full screen dialog content to the [NavGraphBuilder].
 *
 * Deliberately full-bleed — the sheet covers the whole screen, status bar
 * included; content handles its own insets. Declare inside [ModalNavHost].
 *
 * @param T route from a [KClass] for the destination
 * @param typeMap map of destination arguments' kotlin type [KType] to its respective custom
 *   [NavType]. May be empty if [T] does not use custom NavTypes.
 * @param arguments list of arguments to associate with destination
 * @param deepLinks list of deep links to associate with the destinations
 * @param content the sheet content at the given destination
 */
inline fun <reified T : Any> NavGraphBuilder.bottomSheetFullScreenModal(
    typeMap: Map<KType, NavType<*>> = emptyMap(),
    arguments: List<NamedNavArgument> = emptyList(),
    deepLinks: List<NavDeepLink> = emptyList(),
    navHostController: NavHostController,
    shape: Shape = RectangleShape,
    dragToDismissEnabled: Boolean = true,
    noinline content: @Composable ColumnScope.(backstackEntry: NavBackStackEntry) -> Unit,
) {
    destination(
        ComposeNavigatorDestinationBuilder(
            provider[ComposeNavigator::class],
            T::class,
            typeMap
        ) { backStackEntry ->
            ModalBottomSheetWrapper(
                navHostController,
                backStackEntry,
                shape,
                dragToDismissEnabled,
                content,
            )
        }
            .apply {
                arguments.fastForEach { (argumentName, argument) ->
                    argument(argumentName, argument)
                }
                deepLinks.forEach { deepLink -> deepLink(deepLink) }
            }
    )
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ModalBottomSheetWrapper(
    modalNavHostController: NavHostController,
    backStackEntry: NavBackStackEntry,
    shape: Shape,
    dragToDismissEnabled: Boolean,
    content: @Composable ColumnScope.(backstackEntry: NavBackStackEntry) -> Unit,
) {
    val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)

    var isVisible by rememberSaveable { mutableStateOf(true) }
    if (isVisible) {
        ModalBottomSheet(
            modifier = Modifier.fillMaxSize(),
            sheetState = sheetState,
            shape = shape,
            sheetGesturesEnabled = dragToDismissEnabled,
            scrimColor = Color.Black.copy(alpha = 0.32f),
            dragHandle = null,
            contentWindowInsets = { WindowInsets(0, 0, 0, 0) },
            onDismissRequest = {
                isVisible = false
                modalNavHostController.popBackStack()
            },
        ) {
            content(backStackEntry)
        }
    }
}
