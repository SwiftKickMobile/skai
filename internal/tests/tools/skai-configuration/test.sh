#!/bin/bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
task_root="$(cd "$(dirname "$0")/../../../.." && pwd)"
task_tests="$task_root/internal/tests/tools/skai-configuration"
task_app_source="$task_root/internal/apps/ConfigureSKAI"
task_build="/tmp/skai/component-configuration/build"
mkdir -p "$task_build/module-cache"
python3 "$task_tests/test_history.py"
xcrun swiftc -parse-as-library -module-cache-path "$task_build/module-cache" \
    "$task_app_source/Configuration.swift" "$task_app_source/ConfigureModel.swift" \
    "$task_tests/Tests.swift" -o "$task_build/configuration-tests"
"$task_build/configuration-tests" "$task_root"
python3 "$task_tests/test_resolver_parity.py"
