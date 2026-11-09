import Foundation
import Combine

/// A Project-tab checkbox's displayed state. `mixed` is the dash: a category with some members on.
enum CheckState { case on, off, mixed }

/// A User-tab component's override, chosen from a menu: Project (keep the project setting), On or Off.
enum OverrideChoice: Hashable, CaseIterable {
    case inherit, on, off
    var title: String {
        switch self {
        case .inherit: "Project"
        case .on: "On"
        case .off: "Off"
        }
    }
}

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

    /// The Project tab's checkbox for a component.
    func state(of component: Component) -> CheckState {
        if component.required { return .on }
        return configuration.selected.contains(component.id) ? .on : .off
    }

    /// Project tab: toggles the component's project selection.
    func click(_ component: Component) {
        guard !component.required else { return }
        objectWillChange.send()
        if configuration.selected.contains(component.id) {
            configuration.selected.remove(component.id)
        } else {
            configuration.selected.insert(component.id)
        }
    }

    /// The User tab's menu value for a component.
    func overrideChoice(of component: Component) -> OverrideChoice {
        switch configuration.overrides[component.id] {
        case nil: .inherit
        case true?: .on
        case false?: .off
        }
    }

    /// User tab: Project removes the key; On and Off write explicit booleans.
    func setOverride(_ component: Component, to choice: OverrideChoice) {
        guard !component.required else { return }
        objectWillChange.send()
        switch choice {
        case .inherit: configuration.overrides.removeValue(forKey: component.id)
        case .on: configuration.overrides[component.id] = true
        case .off: configuration.overrides[component.id] = false
        }
    }

    func isDimmed(_ component: Component) -> Bool {
        editingLocal && !component.required && configuration.overrides[component.id] == nil
    }

    /// On Project, the user's value for an overridden component, shown beside it. User has no badge:
    /// an overridden row's title is drawn in the accent color instead.
    func badge(for component: Component) -> String? {
        guard !editingLocal, let userValue = configuration.overrides[component.id] else { return nil }
        return "User: " + (userValue ? "On" : "Off")
    }

    func isOverridden(_ component: Component) -> Bool { configuration.overrides[component.id] != nil }

    // MARK: Categories

    private func optionalIDs(_ section: Section) -> [String] { section.members.filter { !$0.required }.map(\.id) }

    func isEnabled(_ section: Section) -> Bool { !optionalIDs(section).isEmpty }

    /// The Project tab's checkbox for a category. The User tab has no category control.
    func state(of section: Section) -> CheckState {
        let ids = optionalIDs(section)
        guard !ids.isEmpty else { return .on }
        let count = ids.filter { configuration.selected.contains($0) }.count
        return count == ids.count ? .on : (count == 0 ? .off : .mixed)
    }

    /// Project tab: select all, or clear all when all are selected.
    func click(_ section: Section) {
        let ids = optionalIDs(section)
        guard !ids.isEmpty, !editingLocal else { return }
        objectWillChange.send()
        if ids.allSatisfy({ configuration.selected.contains($0) }) {
            configuration.selected.subtract(ids)
        } else {
            configuration.selected.formUnion(ids)
        }
    }

    /// A category with any overridden member is drawn in the accent color on both tabs, so overrides
    /// can be found without expanding.
    func hasOverrides(_ section: Section) -> Bool { optionalIDs(section).contains { configuration.overrides[$0] != nil } }

    func isDimmed(_ section: Section) -> Bool { editingLocal && !hasOverrides(section) }

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
