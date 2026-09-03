plugins {
    alias(libs.plugins.kotlin.multiplatform)
    alias(libs.plugins.android.kotlin.multiplatform.library)
    alias(libs.plugins.compose.multiplatform)
    alias(libs.plugins.compose.compiler)
    alias(libs.plugins.kotlin.serialization)
}

group = "com.swiftkickmobile.skai"
version = "0.1.0"

kotlin {
    androidLibrary {
        namespace = "com.swiftkickmobile.skai.compose"
        compileSdk = 37
        minSdk = 29
    }
    jvm()
    iosArm64()
    iosSimulatorArm64()
    // No iosX64: Compose Multiplatform 1.11+ no longer ships Intel-simulator artifacts.

    sourceSets {
        commonMain {
            // Single source of truth: compiles the Android module's sources against the
            // multiplatform artifacts (same androidx.* package names).
            kotlin.srcDir("../skai-compose-android/src/main/java")
            dependencies {
                implementation(libs.compose.material)
                implementation(libs.compose.material3)
                implementation(libs.jetbrains.material.icons.extended)
                implementation(libs.jetbrains.material.navigation)
                implementation(libs.jetbrains.navigation.compose)
            }
        }
        commonTest.dependencies {
            implementation(kotlin("test"))
        }
    }
}
