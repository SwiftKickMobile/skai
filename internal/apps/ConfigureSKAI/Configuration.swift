import Foundation
import CoreFoundation
import CryptoKit

struct ConfigurationFailure: LocalizedError {
    let message: String
    var errorDescription: String? { message }
}

// Read local Git metadata; standalone launches need no Git executable or Xcode.
enum HostProjectDiscovery {
    static func gitDirectory(at root: URL) -> URL? {
        let marker = root.appendingPathComponent(".git")
        var isDirectory: ObjCBool = false
        guard FileManager.default.fileExists(atPath: marker.path, isDirectory: &isDirectory) else { return nil }
        if isDirectory.boolValue { return marker.resolvingSymlinksInPath() }
        guard let contents = try? String(contentsOf: marker, encoding: .utf8) else { return nil }
        let line = contents.trimmingCharacters(in: .whitespacesAndNewlines)
        guard line.hasPrefix("gitdir:"), !line.contains("\n") else { return nil }
        let path = String(line.dropFirst(7)).trimmingCharacters(in: .whitespaces)
        guard !path.isEmpty else { return nil }
        let directory = (path.hasPrefix("/") ? URL(fileURLWithPath: path, isDirectory: true) : root.appendingPathComponent(path, isDirectory: true))
            .standardizedFileURL.resolvingSymlinksInPath()
        guard FileManager.default.fileExists(atPath: directory.path, isDirectory: &isDirectory), isDirectory.boolValue else { return nil }
        return directory
    }

    static func host(skaiRoot: URL) -> URL? {
        let root = skaiRoot.standardizedFileURL.resolvingSymlinksInPath()
        var markerIsDirectory: ObjCBool = false
        guard FileManager.default.fileExists(atPath: root.appendingPathComponent(".git").path, isDirectory: &markerIsDirectory),
              !markerIsDirectory.boolValue, let moduleGit = gitDirectory(at: root),
              let config = try? String(contentsOf: moduleGit.appendingPathComponent("config"), encoding: .utf8) else { return nil }
        // Confirm this metadata belongs to this checkout, rather than a copied .git pointer.
        var inCore = false
        var worktree: String?
        for raw in config.components(separatedBy: .newlines) {
            let line = raw.trimmingCharacters(in: .whitespaces)
            if line.hasPrefix("[") { inCore = line.lowercased() == "[core]"; continue }
            guard inCore, let separator = line.firstIndex(of: "="),
                  line[..<separator].trimmingCharacters(in: .whitespaces).lowercased() == "worktree" else { continue }
            let value = String(line[line.index(after: separator)...]).trimmingCharacters(in: .whitespaces)
            if value.hasPrefix("\"") {
                worktree = (try? JSONSerialization.jsonObject(with: Data(value.utf8), options: [.fragmentsAllowed])) as? String
            } else { worktree = value }
        }
        guard let worktree, !worktree.isEmpty else { return nil }
        let actualRoot = (worktree.hasPrefix("/") ? URL(fileURLWithPath: worktree, isDirectory: true) : moduleGit.appendingPathComponent(worktree, isDirectory: true))
            .standardizedFileURL.resolvingSymlinksInPath()
        guard actualRoot.path == root.path else { return nil }
        var ancestor = root.deletingLastPathComponent()
        while ancestor.path != "/" {
            if let ownerGit = gitDirectory(at: ancestor),
               moduleGit.pathComponents.starts(with: ownerGit.appendingPathComponent("modules").pathComponents) {
                return ancestor
            }
            ancestor.deleteLastPathComponent()
        }
        return nil
    }
}

struct Component: Decodable {
    let id: String
    let type: String
    let sourcePath: String
    let tags: [String]
    let label: String?
    let category: String?
    let description: String?
    let installRole: String?
    var required: Bool { installRole == "required" }
    var title: String { label ?? id }
    var group: String { category ?? "Other" }
}

struct ComponentCategory: Decodable {
    let name: String
    let description: String
}

struct Catalog: Decodable {
    let assets: [Component]
    let retiredComponents: [String]?
    let componentCategories: [ComponentCategory]?
}

final class Configuration {
    let project: URL
    let skaiRoot: URL
    let components: [Component]
    let componentCategories: [ComponentCategory]
    let catalogData: Data
    let originalData: Data?
    let originalLocalData: Data?
    let original: [String: Any]?
    let originalLocal: [String: Any]?
    let originalSelection: Set<String>
    let originalOverrides: [String: Bool]
    var selected: Set<String>
    var overrides: [String: Bool]
    var projectChanged: Bool { selected != originalSelection }
    var localChanged: Bool { overrides != originalOverrides }
    var hasChanges: Bool { projectChanged || localChanged }
    var defaultAll: Bool { originalData == nil }
    var configURL: URL { project.appendingPathComponent("skai/config.json") }
    var localConfigURL: URL { project.appendingPathComponent("skai/config.local.json") }
    var optionalIDs: Set<String> { Set(components.filter { !$0.required }.map(\.id)) }
    var effectiveSelection: Set<String> {
        var result = selected
        for (id, enabled) in overrides {
            if enabled { result.insert(id) } else { result.remove(id) }
        }
        return result
    }
    var historyScope: String {
        originalLocalData != nil || !overrides.isEmpty || FileManager.default.fileExists(atPath: project.appendingPathComponent("skai/install-state.local.json").path) ? "local" : "project"
    }
    var configurationFingerprint: String {
        // Same semantic representation as the portable installer resolver. Extra JSON keys don't affect selection.
        let base = originalData == nil && !projectChanged ? "all" : selected.sorted().joined(separator: ",")
        let local = overrides.keys.sorted().map { $0 + ":" + (overrides[$0]! ? "on" : "off") }.joined(separator: ",")
        return SHA256.hash(data: Data("project=\(base)\noverrides=\(local)\n".utf8)).map { String(format: "%02x", $0) }.joined()
    }

    init(project: URL, skaiRoot: URL) throws {
        self.project = project.standardizedFileURL.resolvingSymlinksInPath()
        self.skaiRoot = skaiRoot.standardizedFileURL.resolvingSymlinksInPath()
        var isDirectory: ObjCBool = false
        guard FileManager.default.fileExists(atPath: self.project.path, isDirectory: &isDirectory), isDirectory.boolValue else {
            throw ConfigurationFailure(message: "The host project directory does not exist.")
        }
        catalogData = try Data(contentsOf: self.skaiRoot.appendingPathComponent("assets.manifest.json"))
        let catalog = try JSONDecoder().decode(Catalog.self, from: catalogData)
        guard Set(catalog.assets.map(\.id)).count == catalog.assets.count else {
            throw ConfigurationFailure(message: "The component catalog contains duplicate IDs.")
        }
        componentCategories = catalog.componentCategories ?? []
        guard Set(componentCategories.map(\.name)).count == componentCategories.count else {
            throw ConfigurationFailure(message: "The component catalog contains duplicate category names.")
        }
        components = catalog.assets.filter { ["skill", "policy"].contains($0.type) }
        originalData = try Self.readConfigBytes(project: self.project)
        originalLocalData = try Self.readConfigBytes(project: self.project, name: "config.local.json")
        let optional = Set(components.filter { !$0.required }.map(\.id))
        let retired = Set(catalog.retiredComponents ?? [])
        if let bytes = originalData {
            let (object, selection) = try Self.parse(bytes, optional: optional, retired: retired)
            original = object
            originalSelection = selection
            selected = selection
        } else {
            original = nil
            originalSelection = optional
            selected = optional
        }
        if let bytes = originalLocalData {
            let object = try Self.parseObject(bytes)
            guard let values = object["overrides"] as? [String: Any] else {
                throw ConfigurationFailure(message: "Local config must have an overrides object: omit a key to inherit, or use true/false.")
            }
            var result: [String: Bool] = [:]
            for (id, value) in values {
                guard optional.contains(id) || retired.contains(id), let number = value as? NSNumber,
                      CFGetTypeID(number) == CFBooleanGetTypeID() else {
                    throw ConfigurationFailure(message: "Local overrides must be true/false for known optional component IDs.")
                }
                if optional.contains(id) { result[id] = number.boolValue }
            }
            originalLocal = object
            originalOverrides = result
            overrides = result
        } else {
            originalLocal = nil
            originalOverrides = [:]
            overrides = [:]
        }
    }

    static func readConfigBytes(project: URL, name: String = "config.json") throws -> Data? {
        let path = project.appendingPathComponent("skai/" + name)
        let resolved = path.resolvingSymlinksInPath().standardizedFileURL.path
        guard resolved.hasPrefix(project.path + "/") else {
            throw ConfigurationFailure(message: "skai/\(name) must stay inside the host project.")
        }
        do {
            let attributes = try FileManager.default.attributesOfItem(atPath: path.path)
            guard attributes[.type] as? FileAttributeType == .typeRegular else {
                throw ConfigurationFailure(message: "skai/\(name) must be a regular file, not a symlink or directory.")
            }
            return try Data(contentsOf: path)
        } catch let error as NSError where error.domain == NSCocoaErrorDomain && error.code == NSFileReadNoSuchFileError {
            return nil
        }
    }

    static func parseObject(_ bytes: Data) throws -> [String: Any] {
        guard let object = try JSONSerialization.jsonObject(with: bytes) as? [String: Any],
              let version = object["schemaVersion"] as? NSNumber,
              CFGetTypeID(version) != CFBooleanGetTypeID(),
              !["f", "d"].contains(String(cString: version.objCType)), version.doubleValue == 1 else {
            throw ConfigurationFailure(message: "Configuration must be a JSON object with schemaVersion: 1.")
        }
        return object
    }

    static func parse(_ bytes: Data, optional: Set<String>, retired: Set<String> = []) throws -> ([String: Any], Set<String>) {
        let object = try parseObject(bytes)
        guard let ids = object["components"] as? [String], ids.count == Set(ids).count,
              Set(ids).isSubset(of: optional.union(retired)) else {
            throw ConfigurationFailure(message: "components must list unique, known optional skill/policy IDs.")
        }
        return (object, Set(ids).intersection(optional))
    }

    func save() throws -> [String: Any] {
        guard selected.isSubset(of: optionalIDs), Set(overrides.keys).isSubset(of: optionalIDs) else {
            throw ConfigurationFailure(message: "The selection contains unknown or required component IDs.")
        }
        guard try Data(contentsOf: skaiRoot.appendingPathComponent("assets.manifest.json")) == catalogData else {
            throw ConfigurationFailure(message: "The SKAI catalog changed. Cancel and reopen Configure SKAI.")
        }
        guard try Self.readConfigBytes(project: project) == originalData,
              try Self.readConfigBytes(project: project, name: "config.local.json") == originalLocalData else {
            throw ConfigurationFailure(message: "Project or local config changed outside this window. Cancel and reopen Configure SKAI.")
        }
        if localChanged {
            func gitStatus(_ args: [String]) throws -> Int32 {
                let process = Process()
                process.executableURL = URL(fileURLWithPath: "/usr/bin/env")
                process.arguments = ["git", "-C", project.path] + args
                process.standardOutput = FileHandle.nullDevice
                process.standardError = FileHandle.nullDevice
                try process.run()
                process.waitUntilExit()
                return process.terminationStatus
            }
            if try gitStatus(["rev-parse", "--is-inside-work-tree"]) == 0 {
                for name in ["config.local.json", "install-state.local.json"] {
                    guard try gitStatus(["check-ignore", "--quiet", "--", project.appendingPathComponent("skai/" + name).path]) == 0 else {
                        throw ConfigurationFailure(message: "skai/\(name) must be gitignored before saving local overrides. Ask your agent to refresh SKAI's ignore entries; already tracked local files need explicit untracking.")
                    }
                }
            }
        }
        func encode(_ object: [String: Any]) throws -> Data {
            var bytes = try JSONSerialization.data(withJSONObject: object, options: [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes])
            bytes.append(0x0a)
            return bytes
        }
        var writes: [(URL, Data, Data?)] = []
        if projectChanged {
            var object = original ?? [:]
            object["schemaVersion"] = 1
            object["components"] = selected.sorted()
            writes.append((configURL, try encode(object), originalData))
        }
        if localChanged {
            var object = originalLocal ?? [:]
            object["schemaVersion"] = 1
            object["overrides"] = overrides
            writes.append((localConfigURL, try encode(object), originalLocalData))
        }
        if !writes.isEmpty { try FileManager.default.createDirectory(at: configURL.deletingLastPathComponent(), withIntermediateDirectories: true) }
        var completed: [(URL, Data, Data?)] = []
        do {
            for write in writes { try write.1.write(to: write.0, options: .atomic); completed.append(write) }
        } catch {
            // Restore only our own successful writes if the second layer failed; never overwrite an external edit.
            for write in completed.reversed() {
                if (try? Data(contentsOf: write.0)) == write.1 {
                    if let previous = write.2 { try previous.write(to: write.0, options: .atomic) }
                    else { try FileManager.default.removeItem(at: write.0) }
                }
            }
            throw error
        }
        return ["status": "saved", "project": project.path, "configPath": configURL.path,
                "localConfigPath": localConfigURL.path, "components": effectiveSelection.sorted(),
                "projectChanged": projectChanged, "localChanged": localChanged,
                "changed": hasChanges, "reconcile": true]
    }

    func resolve(adapter: String, stack: String) throws -> [String: Any] {
        guard ["codex", "cursor", "claude-code"].contains(adapter), ["generic", "swift", "android"].contains(stack) else {
            throw ConfigurationFailure(message: "Unknown adapter or stack.")
        }
        let effective = effectiveSelection
        let enabled = components.filter { $0.required || effective.contains($0.id) }
        let stateName = historyScope == "local" ? "install-state.local.json" : "install-state.json"
        _ = try Self.readConfigBytes(project: project, name: stateName)
        func asset(_ c: Component) -> [String: Any] {
            ["id": c.id, "type": c.type, "sourcePath": c.sourcePath, "tags": c.tags]
        }
        return ["configPath": configURL.path, "localConfigPath": localConfigURL.path,
                "defaultAll": defaultAll, "configurationFingerprint": configurationFingerprint,
                "trackComponents": originalData != nil || !overrides.isEmpty || projectChanged,
                "historyScope": historyScope,
                "historyStatePath": project.appendingPathComponent(historyScope == "local" ? "skai/install-state.local.json" : "skai/install-state.json").path,
                "skills": enabled.filter { $0.type == "skill" && $0.tags.contains("adapter:" + adapter) }.map(asset),
                "policies": enabled.filter { $0.type == "policy" && ($0.tags.contains("core") || (stack == "swift" && $0.tags.contains("swift"))) }.map(asset)]
    }
}

func emit(_ object: [String: Any], to handle: FileHandle = .standardOutput) {
    if var bytes = try? JSONSerialization.data(withJSONObject: object, options: [.sortedKeys, .withoutEscapingSlashes]) {
        bytes.append(0x0a)
        try? handle.write(contentsOf: bytes)
    }
}
