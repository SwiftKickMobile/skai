## Android/Gradle

Provide copy/pasteable, non-interactive `./gradlew` commands.

Placeholders like `<Variant>`, `<ModulePath>`, and `<TestNamePattern>` are **variables** the agent fills per task context (and asks the human only if unclear).

### Build / compile

```bash
./gradlew <AssembleTask> --no-daemon --stacktrace 2>&1 | tee <output-path>.txt
```

Examples for `<AssembleTask>` (pick based on the repo's modules/variants):
- `assemble`
- `assembleDebug`
- `:app:assembleDebug`

### Unit tests (all)

```bash
./gradlew test --no-daemon --stacktrace 2>&1 | tee <output-path>.txt
```

### Unit tests (single module / variant)

```bash
./gradlew <ModulePath>:test<Variant>UnitTest --no-daemon --stacktrace 2>&1 | tee <output-path>.txt
```

Examples:
- `<ModulePath>`: `:app`, `:core`, `:feature:notes`
- `<Variant>`: `Debug`, `Release`, `FreeDebug`

### Unit tests (subset)

Prefer a repo-supported mechanism (varies by test framework and Gradle config). Common patterns include:

```bash
./gradlew <ModulePath>:test<Variant>UnitTest --tests '<TestNamePattern>' --no-daemon --stacktrace 2>&1 | tee <output-path>.txt
```

### Instrumentation / UI tests (if applicable)

```bash
./gradlew <AndroidTestTask> --no-daemon --stacktrace 2>&1 | tee <output-path>.txt
```

Examples for `<AndroidTestTask>`:
- `connectedAndroidTest`
- `<ModulePath>:connected<Variant>AndroidTest`

### Reports / results (typical locations; repo may differ)

- Unit test reports: `**/build/reports/tests/**`
- Unit test results: `**/build/test-results/**`
- Android test reports/results: `**/build/reports/androidTests/**` / `**/build/outputs/androidTest-results/**`

### Mandatory when tests fail: capture structured results artifacts

In addition to the full console output log (`<output-path>.txt`), capture the structured test results artifacts produced by the repo.

Typical artifacts include:
- JUnit XML results: `**/build/test-results/**`
- HTML reports: `**/build/reports/tests/**`

Evidence contract: when tests fail, provide:
- `<output-path>.txt` (full output)
- the JUnit XML results path(s) for the failing run (or the closest equivalent in this repo)
- the HTML report path(s) for the failing run (if generated)

If the repo does not generate structured artifacts, state that explicitly and fall back to the console output log.

