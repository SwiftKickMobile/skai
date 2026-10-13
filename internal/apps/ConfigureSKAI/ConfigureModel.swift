import Foundation
import Combine

/// A checkbox's displayed state. `mixed` is the dash: a category with mixed members, or (User tab)
/// a component that uses the project setting.
enum CheckState { case on, off, mixed }

/// The window's state and every user action, kept free of view code so it can be tested directly.
@MainActor
final class ConfigureModel: ObservableObject {
    struct Section: Identifiable {
        let id: String
        let name: String
        let description: String?
        let members: [Component]
    }

    let configuration: Configuration
    let agentSession: Bool
    /// Components this host has never chosen: listed first, checked, until Save.
    let newIDs: Set<String>
    @Published var editingLocal = false
    @Published var expanded: Set<String> = []
    @Published var requiresReload = false

    init(configuration: Configuration, agentSession: Bool) {
        self.configuration = configuration
        self.agentSession = agentSession
        newIDs = configuration.newComponentIDs
        // New components open checked, so a plain Save installs them; unchecking one declines it.
        configuration.selected.formUnion(newIDs)
    }

    var projectPath: String { configuration.project.path }
    var newSections: [Section] { sections(configuration.components.filter { newIDs.contains($0.id) }, prefix: "new:") }
    var mainSections: [Section] { sections(configuration.components.filter { !newIDs.contains($0.id) }, prefix: "") }

    private func sections(_ components: [Component], prefix: String) -> [Section] {
        let preferred = configuration.componentCategories.map(\.name)
        let names = Set(components.map(\.group))
        let order = preferred.filter { names.contains($0) } + names.subtracting(preferred).sorted()
        return order.map { group in
            Section(id: prefix + group, name: group,
                    description: configuration.componentCategories.first { $0.name == group }?.description,
                    members: components.filter { $0.group == group })
        }
    }

    // MARK: Components

    func state(of component: Component) -> CheckState {
        if component.required { return .on }
        if editingLocal { return configuration.overrides[component.id].map { $0 ? .on : .off } ?? .mixed }
        return configuration.selected.contains(component.id) ? .on : .off
    }

    /// Project tab: on/off. User tab: use project setting → turn on → turn off → use project setting.
    func click(_ component: Component) {
        guard !component.required else { return }
        objectWillChange.send()
        if editingLocal {
            switch configuration.overrides[component.id] {
            case nil: configuration.overrides[component.id] = true
            case true?: configuration.overrides[component.id] = false
            case false?: configuration.overrides.removeValue(forKey: component.id)
            }
        } else if configuration.selected.contains(component.id) {
            configuration.selected.remove(component.id)
        } else {
            configuration.selected.insert(component.id)
        }
    }

    func isDimmed(_ component: Component) -> Bool {
        editingLocal && !component.required && configuration.overrides[component.id] == nil
    }

    /// The other tab's value for an overridden component, shown beside it.
    func badge(for component: Component) -> String? {
        guard let userValue = configuration.overrides[component.id] else { return nil }
        let value = editingLocal ? configuration.selected.contains(component.id) : userValue
        return (editingLocal ? "Project" : "User") + ": " + (value ? "On" : "Off")
    }

    // MARK: Categories

    private func optionalIDs(_ section: Section) -> [String] { section.members.filter { !$0.required }.map(\.id) }

    func isEnabled(_ section: Section) -> Bool { !optionalIDs(section).isEmpty }

    func state(of section: Section) -> CheckState {
        let ids = optionalIDs(section)
        guard !ids.isEmpty else { return .on }
        if editingLocal {
            let values = Set(ids.map { configuration.overrides[$0] })
            return values == [true] ? .on : (values == [false] ? .off : .mixed)
        }
        let count = ids.filter { configuration.selected.contains($0) }.count
        return count == ids.count ? .on : (count == 0 ? .off : .mixed)
    }

    /// Project tab: select all, or clear all when all are selected. User tab: cycles the whole group
    /// through turn on → turn off → use project settings.
    func click(_ section: Section) {
        let ids = optionalIDs(section)
        guard !ids.isEmpty else { return }
        objectWillChange.send()
        if editingLocal {
            switch state(of: section) {
            case .mixed: ids.forEach { configuration.overrides[$0] = true }
            case .on: ids.forEach { configuration.overrides[$0] = false }
            case .off: ids.forEach { configuration.overrides.removeValue(forKey: $0) }
            }
        } else if ids.allSatisfy({ configuration.selected.contains($0) }) {
            configuration.selected.subtract(ids)
        } else {
            configuration.selected.formUnion(ids)
        }
    }

    func isDimmed(_ section: Section) -> Bool {
        editingLocal && !optionalIDs(section).contains { configuration.overrides[$0] != nil }
    }

    func toggleExpanded(_ section: Section) {
        if expanded.contains(section.id) { expanded.remove(section.id) } else { expanded.insert(section.id) }
    }

    // MARK: Bulk actions and status

    func selectAll() {
        objectWillChange.send()
        if editingLocal { configuration.overrides = Dictionary(uniqueKeysWithValues: configuration.optionalIDs.map { ($0, true) }) }
        else { configuration.selected = configuration.optionalIDs }
    }

    func clearOptional() {
        objectWillChange.send()
        if editingLocal { configuration.overrides = Dictionary(uniqueKeysWithValues: configuration.optionalIDs.map { ($0, false) }) }
        else { configuration.selected = [] }
    }

    func useProjectSettings() {
        objectWillChange.send()
        configuration.overrides = [:]
    }

    var overrideCount: Int { configuration.overrides.count }
    var summary: String {
        "\(configuration.effectiveSelection.count) of \(configuration.optionalIDs.count) effective · \(overrideCount) override\(overrideCount == 1 ? "" : "s")"
    }
    /// New components always need a decision, so Save stays available while any are listed: saving
    /// installs the checked ones and records the rest as declined.
    var canSave: Bool { (configuration.hasChanges || !newIDs.isEmpty) && !requiresReload }
}
