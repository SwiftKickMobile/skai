#!/bin/bash
set -euo pipefail
task_root="$(cd "$(dirname "$0")/../../.." && pwd)"
task_build="/tmp/skai/component-configuration/build"
task_app="$task_root/Bin/SKAIConfigure.app"
mkdir -p "$task_build/module-cache" "$task_app/Contents/MacOS" "$task_app/Contents/Resources"
# Icon Composer source: actool emits Assets.car (the system-drawn icon, macOS 26+) and an ICNS fallback
# for older macOS. Both are named SKAIConfigure, matching Info.plist.
xcrun actool "$task_root/internal/branding/SKAIConfigure.icon" --compile "$task_app/Contents/Resources" --platform macosx \
    --minimum-deployment-target 13.0 --app-icon SKAIConfigure \
    --output-partial-info-plist "$task_build/icon-info.plist" --output-format human-readable-text >/dev/null
task_sdk="$(xcrun --sdk macosx --show-sdk-path)"
xcrun swiftc -parse-as-library -O -sdk "$task_sdk" -target "arm64-apple-macosx13.0" \
    -module-cache-path "$task_build/module-cache" \
    "$task_root/internal/apps/ConfigureSKAI/Configuration.swift" "$task_root/internal/apps/ConfigureSKAI/ConfigureModel.swift" "$task_root/internal/apps/ConfigureSKAI/App.swift" \
    -o "$task_build/SKAIConfigure-arm64"
cp "$task_build/SKAIConfigure-arm64" "$task_app/Contents/MacOS/SKAIConfigure"
cp "$task_root/internal/apps/ConfigureSKAI/Info.plist" "$task_app/Contents/Info.plist"
# Ad hoc signature for the repo-bundled app; Developer ID/notarization is a separate packaging choice.
codesign --force --sign - "$task_app"
printf '%s\n' "$task_app"
