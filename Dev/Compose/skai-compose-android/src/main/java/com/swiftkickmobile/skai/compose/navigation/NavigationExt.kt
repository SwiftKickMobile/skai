package com.swiftkickmobile.skai.compose.navigation

import androidx.navigation.NavController
import androidx.navigation.NavDestination.Companion.hasRoute
import androidx.navigation.NavGraph.Companion.findStartDestination

/**
 * Navigates to the given destination screen.
 *
 * If [shouldReplace] is set to true, it replaces the current screen.
 * Otherwise, it pushes the new Route onto the stack.
 *
 * @param route The [Route] to navigate to.
 * @param shouldReplace Flag to replace the current screen or push
 */
fun <T : Route> NavController.navigateToRoute(route: T, shouldReplace: Boolean = false) {
    if (shouldReplace) {
        navigateReplace(route)
    } else {
        navigatePush(route)
    }
}

/**
 * Replaces the current screen with the given destination screen. The previous screen's state is
 * not saved or added to the backstack.
 *
 * This function does nothing if the [route] Route being navigated to is already the current Route.
 *
 * @param route The [Route] to replace the current screen with.
 */
fun <T : Route> NavController.navigateReplace(route: T) {
    val currentRoute = currentBackStackEntry?.destination
    val isCurrentRoute = currentRoute?.hasRoute(route::class) == true

    if (!isCurrentRoute) {
        navigate(route) {
            // Pop everything up to, and including, the current Route off
            // the back stack.
            // Then navigate to the route Route.
            popUpTo(requireNotNull(currentRoute?.route)) {
                inclusive = true
            }
        }
    }
}

/**
 * Pushes the given destination screen onto the navigation stack. The state of the previous screen
 * is saved and added to the backstack.
 *
 * This function does nothing if the Route's route type is the same as the current screen's.
 *
 * @param route The [Route] to be pushed onto the navigation stack.
 */
fun <T : Route> NavController.navigatePush(route: T) {
    val currentRoute = currentBackStackEntry?.destination
    val isCurrentRoute = currentRoute?.hasRoute(route::class) == true

    if (!isCurrentRoute) {
        navigate(route)
    }
}

/**
 * Pop everything off to the start Route (primary tab) before navigating to the destination [route].
 *
 * This should be used when navigating between tabs on the dashboard. It ensures that
 * all Routes would have a back reference to the start Route ensuring that a back press navigation
 * from the root of any tab navigates to the primary tab.
 *
 * All Routes that are popped will have their state saved, and the target Route's state
 * will be restored (if available) when performing navigation.
 *
 * @param resetState Clears any saved state associated with this [route] before navigation.
 *
 */
fun <T : Route> NavController.navigateToTab(route: T, resetState: Boolean = false) {
    if (resetState) clearBackStack(route)

    // Navigate to tab route
    navigate(route) {
        popUpTo(requireNotNull(graph.findStartDestination().route)) {
            this.saveState = true
        }
        // Avoid multiple copies of the same Route when
        // re-selecting the same item
        this.launchSingleTop = true
        // Restore state when re-selecting a previously selected item
        this.restoreState = true
    }
}
