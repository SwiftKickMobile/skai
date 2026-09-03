package com.swiftkickmobile.skai.compose.samples

// Illustrative host-project usage. This file is not compiled into either library artifact.

import androidx.compose.runtime.Composable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.ui.Modifier
import androidx.navigation.compose.rememberNavController
import com.swiftkickmobile.skai.compose.navigation.ModalNavHost
import com.swiftkickmobile.skai.compose.navigation.Route
import com.swiftkickmobile.skai.compose.navigation.bottomSheetFullScreenModal
import com.swiftkickmobile.skai.compose.navigation.navigatePush
import com.swiftkickmobile.skai.compose.navigation.rememberBottomSheetNavigator
import com.swiftkickmobile.skai.compose.placeholder.PlaceholderColors
import com.swiftkickmobile.skai.compose.placeholder.PlaceholderModalScene
import com.swiftkickmobile.skai.compose.placeholder.PlaceholderModalStyle
import com.swiftkickmobile.skai.compose.placeholder.PlaceholderRoute
import com.swiftkickmobile.skai.compose.placeholder.PlaceholderRouteKind
import com.swiftkickmobile.skai.compose.placeholder.PlaceholderScene
import kotlinx.serialization.Serializable

@Serializable
private data object SampleSheet : Route

@Composable
fun Sample() {
    val modalNavController = rememberNavController(rememberBottomSheetNavigator())
    val color = PlaceholderColors.domain(0)
    val fullScreen = PlaceholderModalStyle("full_screen", "Full Screen", 0)
    val routes = listOf(
        PlaceholderRoute(
            label = "Sample Sheet",
            kind = PlaceholderRouteKind.Modal(fullScreen),
            action = { modalNavController.navigatePush(SampleSheet) },
        ),
    )

    Box(Modifier.fillMaxSize()) {
        PlaceholderScene(title = "Sample", domainColor = color, routes = routes)
        ModalNavHost(navController = modalNavController) {
            bottomSheetFullScreenModal<SampleSheet>(navHostController = modalNavController) {
                PlaceholderModalScene(
                    presenterTitle = "Sample",
                    presenterColor = color,
                    presenterRoutes = routes,
                    onDismiss = modalNavController::popBackStack,
                ) {
                    PlaceholderScene(title = "Sample Sheet", domainColor = color)
                }
            }
        }
    }
}
