import Foundation

@main struct ConfigurationTests {
    static func main() throws {
        let skaiRoot = URL(fileURLWithPath: CommandLine.arguments[1])
        let temporary = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)
        try FileManager.default.createDirectory(at: temporary, withIntermediateDirectories: true)
        defer { try? FileManager.default.removeItem(at: temporary) }
        // Real local repositories exercise Git's actual submodule/worktree metadata.
        func git(_ args: [String]) throws {
            let process = Process()
            process.executableURL = URL(fileURLWithPath: "/usr/bin/env")
            process.arguments = ["git", "-c", "protocol.file.allow=always"] + args
            process.standardOutput = FileHandle.nullDevice
            let errors = Pipe()
            process.standardError = errors
            try process.run()
            let output = errors.fileHandleForReading.readDataToEndOfFile()
            process.waitUntilExit()
            guard process.terminationStatus == 0 else {
                throw ConfigurationFailure(message: "Git fixture failed: " + String(decoding: output, as: UTF8.self))
            }
        }
        func repository(_ url: URL) throws {
            try git(["init", "--quiet", "--initial-branch=main", url.path])
            try git(["-C", url.path, "-c", "user.name=SKAI Test", "-c", "user.email=test@example.invalid", "commit", "--quiet", "--allow-empty", "-m", "Fixture"])
        }
        func commit(_ url: URL) throws {
            try git(["-C", url.path, "-c", "user.name=SKAI Test", "-c", "user.email=test@example.invalid", "commit", "--quiet", "-am", "Submodule fixture"])
        }
        let source = temporary.appendingPathComponent("source project")
        let host = temporary.appendingPathComponent("host project")
        try repository(source)
        try repository(host)
        try git(["-C", host.path, "submodule", "add", "--quiet", source.path, "Vendor tools/skai"])
        let module = host.appendingPathComponent("Vendor tools/skai")
        precondition(HostProjectDiscovery.host(skaiRoot: module)?.path == host.resolvingSymlinksInPath().path)
        precondition(HostProjectDiscovery.host(skaiRoot: source) == nil)
        precondition(HostProjectDiscovery.host(skaiRoot: temporary) == nil)
        let alias = temporary.appendingPathComponent("module alias")
        try FileManager.default.createSymbolicLink(at: alias, withDestinationURL: module)
        precondition(HostProjectDiscovery.host(skaiRoot: alias)?.path == host.resolvingSymlinksInPath().path)
        let copied = host.appendingPathComponent("copied pointer")
        try FileManager.default.createDirectory(at: copied, withIntermediateDirectories: true)
        // An absolute copied pointer must not redirect this unrelated directory to the host.
        let moduleGit = HostProjectDiscovery.gitDirectory(at: module)!
        try Data("gitdir: \(moduleGit.path)\n".utf8).write(to: copied.appendingPathComponent(".git"))
        precondition(HostProjectDiscovery.host(skaiRoot: copied) == nil)
        try commit(host)
        let linkedHost = temporary.appendingPathComponent("linked host")
        try git(["-C", host.path, "worktree", "add", "--quiet", "-b", "linked", linkedHost.path])
        try git(["-C", linkedHost.path, "submodule", "update", "--init", "--quiet"])
        precondition(HostProjectDiscovery.host(skaiRoot: linkedHost.appendingPathComponent("Vendor tools/skai"))?.path == linkedHost.resolvingSymlinksInPath().path)
        let outerHost = temporary.appendingPathComponent("outer host")
        try repository(outerHost)
        try git(["-C", outerHost.path, "submodule", "add", "--quiet", host.path, "Shared"])
        try git(["-C", outerHost.path, "submodule", "update", "--init", "--recursive", "--quiet"])
        let nestedOwner = outerHost.appendingPathComponent("Shared")
        precondition(HostProjectDiscovery.host(skaiRoot: nestedOwner.appendingPathComponent("Vendor tools/skai"))?.path == nestedOwner.resolvingSymlinksInPath().path)
        print("PASS host discovery: submodule with spaces/nested folders, symlink, linked host worktree, nested superproject, standalone/missing/copied-pointer fallback")
        let configPath = temporary.appendingPathComponent("skai/config.json")
        func write(_ object: [String: Any]) throws {
            try FileManager.default.createDirectory(at: configPath.deletingLastPathComponent(), withIntermediateDirectories: true)
            try JSONSerialization.data(withJSONObject: object).write(to: configPath)
        }
        func reject(_ name: String, _ operation: () throws -> Void) throws {
            do { try operation() } catch { print("PASS \(name)"); return }
            fatalError("Expected rejection: \(name)")
        }
        let initial = try Configuration(project: temporary, skaiRoot: skaiRoot)
        precondition(initial.defaultAll && initial.selected == initial.optionalIDs)
        precondition(Set(initial.componentCategories.map(\.name)) == Set(initial.components.map(\.group)))
        precondition(initial.componentCategories.allSatisfy { !$0.description.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty })
        print("PASS every component category has a parent description")
        precondition(!initial.hasChanges)
        initial.selected.remove("skill.skai-debugging")
        precondition(initial.hasChanges)
        initial.selected = initial.optionalIDs
        precondition(!initial.hasChanges)
        print("PASS selection changes enable Save; reverting disables it")
        precondition(!FileManager.default.fileExists(atPath: configPath.path))
        print("PASS absent config selects all; opening does not write")
        initial.selected = []
        let emptySave = try initial.save()
        precondition(emptySave["status"] as? String == "saved")
        let empty = try Configuration(project: temporary, skaiRoot: skaiRoot)
        let resolved = try empty.resolve(adapter: "codex", stack: "swift")
        precondition((resolved["skills"] as! [[String: Any]]).map { $0["id"] as! String } == ["skill.skai-configure"])
        precondition((resolved["policies"] as! [[String: Any]]).isEmpty)
        print("PASS empty selection preserves Configure SKAI only")
        try write(["schemaVersion": 1, "components": [], "projectNote": "preserve me"])
        let edit = try Configuration(project: temporary, skaiRoot: skaiRoot)
        edit.selected = ["skill.skai-debugging", "policy.swift-code-organization", "policy.error-handling"]
        _ = try edit.save()
        let saved = try JSONSerialization.jsonObject(with: Data(contentsOf: configPath)) as! [String: Any]
        precondition(saved["projectNote"] as? String == "preserve me")
        let loaded = try Configuration(project: temporary, skaiRoot: skaiRoot)
        for adapter in ["codex", "cursor", "claude-code"] {
            let generic = try loaded.resolve(adapter: adapter, stack: "generic")
            let swift = try loaded.resolve(adapter: adapter, stack: "swift")
            precondition((generic["skills"] as! [[String: Any]]).count == 2)
            precondition((generic["policies"] as! [[String: Any]]).count == 1)
            precondition((swift["policies"] as! [[String: Any]]).count == 2)
        }
        print("PASS save/reopen, extra-key preservation and all adapter/stack selections")
        let same = try loaded.save()
        precondition(same["changed"] as? Bool == false && same["reconcile"] as? Bool == true)
        print("PASS unchanged Save still requests reconciliation")
        let localPath = temporary.appendingPathComponent("skai/config.local.json")
        let projectBytes = try Data(contentsOf: configPath)
        let localEdit = try Configuration(project: temporary, skaiRoot: skaiRoot)
        localEdit.overrides = ["skill.skai-debugging": false, "skill.skai-ui-map-architecture": true]
        _ = try localEdit.save()
        let unchangedProject = try Data(contentsOf: configPath)
        precondition(unchangedProject == projectBytes)
        let localObject = try JSONSerialization.jsonObject(with: Data(contentsOf: localPath)) as! [String: Any]
        precondition((localObject["overrides"] as! [String: Bool]).count == 2)
        let overridden = try Configuration(project: temporary, skaiRoot: skaiRoot)
        precondition(!overridden.effectiveSelection.contains("skill.skai-debugging"))
        precondition(overridden.effectiveSelection.contains("skill.skai-ui-map-architecture"))
        precondition(overridden.historyScope == "local" && !overridden.hasChanges)
        overridden.overrides.removeValue(forKey: "skill.skai-debugging")
        _ = try overridden.save()
        let inherited = try Configuration(project: temporary, skaiRoot: skaiRoot)
        precondition(inherited.effectiveSelection.contains("skill.skai-debugging"))
        let inheritedObject = try JSONSerialization.jsonObject(with: Data(contentsOf: localPath)) as! [String: Any]
        precondition((inheritedObject["overrides"] as! [String: Bool])["skill.skai-debugging"] == nil)
        print("PASS local on/off precedence, inherited key omitted, project bytes untouched")
        inherited.overrides = [:]
        _ = try inherited.save()
        let reset = try Configuration(project: temporary, skaiRoot: skaiRoot)
        precondition(reset.overrides.isEmpty && reset.effectiveSelection == reset.selected)
        print("PASS reset overrides restores project selection")
        let staleLocal = try Configuration(project: temporary, skaiRoot: skaiRoot)
        staleLocal.selected = []
        let beforeBlockedSave = try Data(contentsOf: configPath)
        try JSONSerialization.data(withJSONObject: ["schemaVersion": 1, "overrides": ["skill.skai-debugging": true]]).write(to: localPath)
        try reject("external local edit blocks project Save", { _ = try staleLocal.save() })
        let afterBlockedSave = try Data(contentsOf: configPath)
        precondition(beforeBlockedSave == afterBlockedSave)
        for values: [String: Any] in [["skill.skai-debugging": 1], ["skill.skai-debugging": NSNull()], ["skill.skai-configure": false], ["unknown": true]] {
            try JSONSerialization.data(withJSONObject: ["schemaVersion": 1, "overrides": values]).write(to: localPath)
            try reject("invalid local override blocks", { _ = try Configuration(project: temporary, skaiRoot: skaiRoot) })
        }
        try FileManager.default.removeItem(at: localPath)
        try reject("stale window cannot overwrite", { _ = try edit.save() })
        for invalid: [String: Any] in [[:], ["schemaVersion": true, "components": []], ["schemaVersion": 2, "components": []], ["schemaVersion": 1, "components": ["unknown"]], ["schemaVersion": 1, "components": ["skill.skai-debugging", "skill.skai-debugging"]]] {
            try write(invalid)
            try reject("invalid config blocks", { _ = try Configuration(project: temporary, skaiRoot: skaiRoot) })
        }
        try Data("{invalid".utf8).write(to: configPath)
        try reject("malformed JSON blocks", { _ = try Configuration(project: temporary, skaiRoot: skaiRoot) })
        try FileManager.default.removeItem(at: configPath)
        let target = temporary.appendingPathComponent("outside.json")
        try Data("{}".utf8).write(to: target)
        try FileManager.default.createSymbolicLink(at: configPath, withDestinationURL: target)
        try reject("symlink config blocked", { _ = try Configuration(project: temporary, skaiRoot: skaiRoot) })
        let targetBytes = try Data(contentsOf: target)
        precondition(targetBytes == Data("{}".utf8))
        let unignored = try Configuration(project: host, skaiRoot: skaiRoot)
        unignored.overrides = ["skill.skai-debugging": false]
        try reject("Git project blocks local Save until private files are ignored", { _ = try unignored.save() })
        let hostLocal = host.appendingPathComponent("skai/config.local.json")
        precondition(!FileManager.default.fileExists(atPath: hostLocal.path))
        try Data("/skai/config.local.json\n/skai/install-state.local.json\n".utf8).write(to: host.appendingPathComponent(".gitignore"))
        _ = try unignored.save()
        precondition(FileManager.default.fileExists(atPath: hostLocal.path))
        try git(["-C", host.path, "add", "--force", "skai/config.local.json"])
        let tracked = try Configuration(project: host, skaiRoot: skaiRoot)
        tracked.overrides = ["skill.skai-debugging": true]
        let beforeTrackedSave = try Data(contentsOf: hostLocal)
        try reject("tracked private settings require explicit untracking", { _ = try tracked.save() })
        let afterTrackedSave = try Data(contentsOf: hostLocal)
        precondition(beforeTrackedSave == afterTrackedSave)
        print("PASS Git ignore enforcement preserves private config on rejected Save")
        print("All native configuration checks passed.")
    }
}
