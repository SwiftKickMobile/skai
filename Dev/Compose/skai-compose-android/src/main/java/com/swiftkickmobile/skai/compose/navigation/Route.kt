package com.swiftkickmobile.skai.compose.navigation

import kotlinx.serialization.Serializable

interface Route

@Serializable
data object NavStart: Route

@Serializable
data object EmptyRoute: Route
