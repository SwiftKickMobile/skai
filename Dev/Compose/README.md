# SKAI Compose

SKAI's local Compose library for UI Map routing and placeholder scaffolding. It supports
both Compose Multiplatform projects and Android-only Jetpack Compose projects.

## Structure

```
skai-compose/
├── settings.gradle.kts        # Standalone build: repositories + module includes
├── build.gradle.kts           # Root build: plugin declarations (apply false)
├── gradle/libs.versions.toml  # Version catalog (Android + KMP equivalents)
├── skai-compose-android/      # Android library module (owns the sources)
│   └── src/main/java/com/swiftkickmobile/skai/compose/
│       ├── navigation/        # SlideNavHost, ModalNavHost, Route, ...
│       └── placeholder/       # Placeholder scene/scaffolding
└── skai-compose-kmp/          # KMP module (android + iOS); compiles the same
                               # sources from commonMain — no copies
```

## Building

This folder is a self-contained Gradle build with its own wrapper:

```
./gradlew :skai-compose-android:assembleRelease  # Android library
./gradlew :skai-compose-kmp:assemble             # KMP module (all targets)
./gradlew :skai-compose-kmp:compileKotlinIosArm64
./gradlew :skai-compose-kmp:jvmTest
./verify-guide-api.sh                             # guide/source API drift
```

## Consuming from a host project (composite build)

In the host project's `settings.gradle.kts`:

```kotlin
includeBuild("Submodules/skai/Dev/Compose")
```

Then depend on the library by its coordinates — Gradle substitutes the included build
automatically:

```kotlin
dependencies {
    implementation("com.swiftkickmobile.skai:skai-compose-kmp") // KMP (primary)
    // or, for the plain Android build:
    implementation("com.swiftkickmobile.skai:skai-compose-android")
}
```

Use exactly one artifact in a consuming module. The KMP artifact supports Android,
JVM, `iosArm64`, and `iosSimulatorArm64`; use the Android artifact only when the
consuming code is Android-only.

## Kotlin Multiplatform

`:skai-compose-kmp` is the primary module: its `commonMain` points at the Android
module's sources (the multiplatform artifacts keep the `androidx.*` package names, so
the exact same files compile on both) and it builds for `androidTarget` plus the iOS
targets. `:skai-compose-android` is the plain-Android backup, compiled against the androidx
Compose BOM. Pick one — they ship the same classes.

The catalog's KMP equivalents (marked as such in `libs.versions.toml`):

- Plugins: `kotlin-multiplatform`, `compose-multiplatform`, `android-kotlin-multiplatform-library`
- Libraries: the `org.jetbrains.*` multiplatform ports of material, material3,
  navigation-compose, material-navigation, and material-icons-extended

Toolchain notes: AGP 9+ has built-in Kotlin, so the Android module applies no
`kotlin-android` plugin, and the KMP module uses `com.android.kotlin.multiplatform.library`
(`androidLibrary {}` inside `kotlin {}`). There is no `iosX64` target — Compose
Multiplatform 1.11+ no longer ships Intel-simulator artifacts.

The checked-in build uses Gradle 9.6.1, AGP 9.1.1, Kotlin 2.4.10, Compose
Multiplatform 1.11.1, Android compile SDK 37, and Android minimum SDK 29. An
included build is configured by the host's Gradle process rather than by this
folder's wrapper, so the host must meet the same Gradle/AGP/compile-SDK floor.
Android Studio must also support AGP 9.1.1; use Panda 3 or newer rather than Otter 3.

Note that `org.jetbrains.compose.material3:material3` is versioned on its own release
train, decoupled from the `compose-multiplatform` plugin version.

The routing APIs may remain in production code. Placeholder APIs and project-generated
`DomainColors` scaffolds are temporary; removing the last placeholder does not by itself
mean the SKAI Compose dependency is unused.
