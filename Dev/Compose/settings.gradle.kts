pluginManagement {
    repositories {
        google {
            content {
                includeGroupByRegex("com\\.android.*")
                includeGroupByRegex("com\\.google.*")
                includeGroupByRegex("androidx.*")
            }
        }
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

// Must not camel-case to the same accessor as any module name: host builds with
// TYPESAFE_PROJECT_ACCESSORS generate colliding accessors otherwise.
rootProject.name = "skai-compose"
include(":skai-compose-android")
include(":skai-compose-kmp")
