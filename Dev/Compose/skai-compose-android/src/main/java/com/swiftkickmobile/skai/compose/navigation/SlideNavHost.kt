package com.swiftkickmobile.skai.compose.navigation

import androidx.compose.animation.AnimatedContentTransitionScope
import androidx.compose.animation.EnterTransition
import androidx.compose.animation.ExitTransition
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.animation.slideInHorizontally
import androidx.compose.animation.slideOutHorizontally
import androidx.navigation.NavBackStackEntry
import androidx.navigation.NavGraphBuilder
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost

@Composable
fun SlideNavHost(
    modifier: Modifier = Modifier,
    navController: NavHostController,
    startDestination: Route = NavStart,
    enterTransition:
    (AnimatedContentTransitionScope<NavBackStackEntry>.() -> EnterTransition) = {
        slideInHorizontally { it }
    },
    exitTransition:
    (AnimatedContentTransitionScope<NavBackStackEntry>.() -> ExitTransition) = {
        slideOutHorizontally { -it / 2 }
    },
    popEnterTransition:
    (AnimatedContentTransitionScope<NavBackStackEntry>.() -> EnterTransition) = {
        slideInHorizontally { -it / 2 }
    },
    popExitTransition:
    (AnimatedContentTransitionScope<NavBackStackEntry>.() -> ExitTransition) = {
        slideOutHorizontally { it }
    },
    builder: NavGraphBuilder.() -> Unit,
) {
    NavHost(
        navController = navController,
        startDestination = startDestination,
        modifier = modifier,
        enterTransition = enterTransition,
        exitTransition = exitTransition,
        popEnterTransition = popEnterTransition,
        popExitTransition = popExitTransition,
        builder = builder,
    )
}
