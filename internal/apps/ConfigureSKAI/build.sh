#!/bin/bash
set -euo pipefail
task_root="$(cd "$(dirname "$0")/../../.." && pwd)"
task_branch="$(git -C "$task_root" symbolic-ref --short HEAD 2>/dev/null || printf '%s' detached)"
task_build="$task_root/skai/working-docs/$task_branch/component-configuration/build"
task_app="$task_root/Bin/SKAIConfigure.app"
task_iconset="$task_build/SKAIConfigure.iconset"
mkdir -p "$task_build/module-cache" "$task_app/Contents/MacOS" "$task_app/Contents/Resources" "$task_iconset"
for task_size in 16 32 128 256 512; do
    sips -z "$task_size" "$task_size" "$task_root/internal/branding/skai-app-icon.png" --out "$task_iconset/icon_${task_size}x${task_size}.png" >/dev/null
    task_retina=$((task_size * 2))
    sips -z "$task_retina" "$task_retina" "$task_root/internal/branding/skai-app-icon.png" --out "$task_iconset/icon_${task_size}x${task_size}@2x.png" >/dev/null
done
iconutil -c icns "$task_iconset" -o "$task_app/Contents/Resources/SKAIConfigure.icns"
task_sdk="$(xcrun --sdk macosx --show-sdk-path)"
xcrun swiftc -parse-as-library -O -sdk "$task_sdk" -target "arm64-apple-macosx13.0" \
    -module-cache-path "$task_build/module-cache" \
    "$task_root/internal/apps/ConfigureSKAI/Configuration.swift" "$task_root/internal/apps/ConfigureSKAI/App.swift" \
    -o "$task_build/SKAIConfigure-arm64"
cp "$task_build/SKAIConfigure-arm64" "$task_app/Contents/MacOS/SKAIConfigure"
cp "$task_root/internal/apps/ConfigureSKAI/Info.plist" "$task_app/Contents/Info.plist"
# Ad hoc signature for the repo-bundled app; Developer ID/notarization is a separate packaging choice.
codesign --force --sign - "$task_app"
printf '%s\n' "$task_app"
