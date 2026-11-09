package com.swiftkickmobile.skai.compose.navigation

import androidx.compose.animation.core.AnimationSpec
import androidx.compose.animation.core.SpringSpec
import androidx.compose.foundation.layout.requiredSize
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.ModalBottomSheetValue
import androidx.compose.material.navigation.BottomSheetNavigator
import androidx.compose.material.navigation.ModalBottomSheetLayout
import androidx.compose.material.navigation.bottomSheet
import androidx.compose.material.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.navigation.NavGraphBuilder
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.ComposeNavigator
import androidx.navigation.compose.ComposeNavigatorDestinationBuilder
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.dialog
import androidx.navigation.get
import kotlin.reflect.KClass
import kotlin.reflect.KType

/**
 * The one NavHost for a scene's modal group — hosts every modal flavor:
 * M2 [bottomSheet] destinations, [dialog] destinations, [bottomSheetModal] destinations and
 * [bottomSheetFullScreenModal] destinations. Idles on [EmptyRoute] internally;
 * callers never declare it.
 *
 * NOTE: M3 [bottomSheetModal] should be favoured over M2 [bottomSheet] destinations.
 *
 * The [navController] must have been created with the navigator from
 * [rememberBottomSheetNavigator] attached (pass it to `rememberNavController`).
 *
 * @param navController The NavHostController to use for navigation
 * @param modifier The modifier to apply to the NavHost
 * @param route The route to use for the NavGraph
 * @param typeMap The type map to use for the NavGraph
 * @param isComposite Whether the NavHost is hosted in a composite view
 * @param sheetGesturesEnabled Whether the sheet itself takes drags. Off for a
 * host whose sheet wraps a platform view (the web view) — the sheet's drag
 * wins over an interop child's own scroll, so the page cannot move; scrim tap
 * and back still dismiss
 * @param builder The builder for the NavGraph
 */
@Composable
fun ModalNavHost(
    navController: NavHostController,
    modifier: Modifier = Modifier,
    route: KClass<*>? = null,
    typeMap: Map<KType, NavType<*>> = emptyMap(),
    isComposite: Boolean = false,
    sheetGesturesEnabled: Boolean = true,
    builder: NavGraphBuilder.() -> Unit,
) {
    val startDestination = EmptyRoute

    // Create an empty composable screen destination
    val emptyDestination = ComposeNavigatorDestinationBuilder(
        navigator = navController.navigatorProvider[ComposeNavigator::class],
        route = startDestination::class,
        typeMap = emptyMap(),
        content = {},
    ).build()

    // Build the NavGraph
    val navGraph = remember(route, startDestination, builder) {
        NavGraphBuilder(
            provider = navController.navigatorProvider,
            startDestination = startDestination,
            route = route,
            typeMap = typeMap,
        ).apply { addDestination(emptyDestination) }.apply(builder).build()
    }

    // Create the Modal Bottom Sheet Layout with the provided BottomSheetNavigator
    ModalBottomSheetLayout(
        modifier = if (isComposite) Modifier.requiredSize(0.dp) else Modifier,
        bottomSheetNavigator = navController.navigatorProvider[BottomSheetNavigator::class],
        sheetGesturesEnabled = sheetGesturesEnabled,
        sheetShape = RoundedCornerShape(topStart = 12.dp, topEnd = 12.dp),
        sheetBackgroundColor = Color.Transparent, // Avoids the strange white line on the rounded corners
    ) {
        NavHost(
            modifier = modifier,
            navController = navController,
            graph = navGraph,
        )
    }
}

@Composable
fun rememberBottomSheetNavigator(
    animationSpec: AnimationSpec<Float> = SpringSpec(),
    skipHalfExpanded: Boolean = false,
): BottomSheetNavigator {
    val sheetState = rememberModalBottomSheetState(
        ModalBottomSheetValue.Hidden,
        animationSpec = animationSpec,
        skipHalfExpanded = skipHalfExpanded,
    )
    return remember(sheetState) { BottomSheetNavigator(sheetState) }
}
