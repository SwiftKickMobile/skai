#!/bin/bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
task_root="$(cd "$(dirname "$0")/../../.." && pwd)"
task_branch="$(git -C "$task_root" symbolic-ref --short HEAD 2>/dev/null || printf '%s' detached)"
task_build="$task_root/skai/working-docs/$task_branch/component-configuration/build"
mkdir -p "$task_build/module-cache"
python3 "$task_root/internal/apps/ConfigureSKAI/test_history.py"
xcrun swiftc -parse-as-library -module-cache-path "$task_build/module-cache" \
    "$task_root/internal/apps/ConfigureSKAI/Configuration.swift" \
    "$task_root/internal/apps/ConfigureSKAI/Tests.swift" -o "$task_build/configuration-tests"
"$task_build/configuration-tests" "$task_root"
python3 "$task_root/internal/apps/ConfigureSKAI/test_resolver_parity.py"
