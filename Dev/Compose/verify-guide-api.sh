#!/usr/bin/env bash
set -euo pipefail

compose_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
skai_root="$(cd "$compose_dir/../.." && pwd)"
compose_guide="$skai_root/Guides/UIMap/ui-map-compose.md"
placeholder_guide="$skai_root/Guides/UIMap/ui-map-compose-placeholders.md"

stale_pattern='com\.example\.compose|ModalBottomSheetNavHost|bottomSheetFullScreen<|BottomSheetScope|dismissBottomSheet|SKAI does not currently distribute|SlideNavHost\(navController,|PlaceholderRouteKind\.(Sheet|FullScreen|Popover)|PlaceholderRouteKind\.entries|PlaceholderTab\(label, icon\)|currentTabRoute|mutableIntStateOf\(0\)'
if rg -n --pcre2 --glob '!verify-guide-api.sh' "$stale_pattern" "$compose_dir" "$compose_guide" "$placeholder_guide"; then
    echo "Compose guide/API verification failed: stale contract text remains." >&2
    exit 1
fi

rg -q 'group = "com.swiftkickmobile.skai"' "$compose_dir/skai-compose-kmp/build.gradle.kts"
rg -q 'fun ModalNavHost\(' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'NavGraphBuilder\.bottomSheetFullScreenModal\(' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'NavGraphBuilder\.bottomSheetModal\(' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'NavController\.navigateToTab\(' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'navigateToTab\(tab\.route\)' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'val route: Route,' "$compose_dir/skai-compose-android/src/main/java/com/swiftkickmobile/skai/compose/placeholder/PlaceholderTab.kt"
rg -q 'fun domain\(index: Int\)' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'data class PlaceholderModalStyle\(' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'data class Modal\(val style: PlaceholderModalStyle\)' "$compose_dir/skai-compose-android/src/main/java"
rg -q 'com\.swiftkickmobile\.skai:skai-compose-kmp' "$compose_guide"
rg -q 'com\.swiftkickmobile\.skai:skai-compose-android' "$compose_guide"
rg -q 'commonMain\.dependencies' "$compose_guide"
rg -q '^    jvm()' "$compose_dir/skai-compose-kmp/build.gradle.kts"
rg -q 'ModalNavHost' "$compose_guide" "$placeholder_guide"
rg -q 'bottomSheetFullScreenModal' "$compose_guide"
rg -q 'bottomSheetModal<Route>' "$compose_guide"
rg -q 'navigateToTab' "$compose_guide"
rg -q 'navigateToTab' "$placeholder_guide"
rg -q 'PlaceholderTab\(label, route, icon\)' "$placeholder_guide"
rg -q 'PlaceholderColors\.domain\(index\)' "$placeholder_guide"
rg -q 'PlaceholderRouteKind\.Modal' "$placeholder_guide"

echo "Compose guide/API verification passed."
