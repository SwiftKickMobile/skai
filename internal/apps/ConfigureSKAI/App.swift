import AppKit
import SwiftUI

/// App lifecycle, the JSON event protocol and the window. Everything inside the window is SwiftUI.
@MainActor
final class ConfigureApp: NSObject, NSApplicationDelegate, NSWindowDelegate {
    var model: ConfigureModel?
    var window: NSWindow!
    var hosting: NSHostingView<ConfigureView>!
    let agentSession: Bool
    var finished = false
    var savedResult: [String: Any]?
    let skaiRoot: URL
    let initialProject: URL?

    init(project: URL?, skaiRoot: URL, agentSession: Bool = false) {
        self.agentSession = agentSession
        self.initialProject = project
        self.skaiRoot = skaiRoot
    }

    func applicationDidFinishLaunching(_ notification: Notification) {
        // The bundle's icon as the system draws it: the Icon Composer version where supported, else the ICNS.
        if Bundle.main.bundleURL.pathExtension == "app" {
            NSApp.applicationIconImage = NSWorkspace.shared.icon(forFile: Bundle.main.bundlePath)
        }
        NSApp.setActivationPolicy(.regular)
        NSApp.activate(ignoringOtherApps: true)
        let mainMenu = NSMenu()
        let appMenu = NSMenu()
        let item = NSMenuItem()
        item.submenu = appMenu
        appMenu.addItem(withTitle: "Quit Configure SKAI", action: #selector(NSApplication.terminate(_:)), keyEquivalent: "q")
        mainMenu.addItem(item)
        NSApp.mainMenu = mainMenu
        var project = initialProject ?? HostProjectDiscovery.host(skaiRoot: skaiRoot)
        if project == nil {
            let panel = NSOpenPanel()
            panel.title = "Choose the project to configure"
            panel.message = "Select the host project that uses SKAI."
            panel.canChooseDirectories = true
            panel.canChooseFiles = false
            panel.allowsMultipleSelection = false
            guard panel.runModal() == .OK, let url = panel.url else { finish(["status": "cancelled"]); return }
            project = url
        }
        do {
            let configuration = try Configuration(project: project!, skaiRoot: skaiRoot)
            makeWindow(ConfigureModel(configuration: configuration, agentSession: agentSession))
            emit(["status": "ready", "project": configuration.project.path, "configPath": configuration.configURL.path,
                  "localConfigPath": configuration.localConfigURL.path, "launchMode": agentSession ? "agent" : "standalone"])
        } catch {
            showError(error)
            finish(["status": "error", "error": error.localizedDescription], code: 2)
        }
    }

    func makeWindow(_ model: ConfigureModel) {
        self.model = model
        window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 750, height: 770),
                          styleMask: [.titled, .closable, .miniaturizable, .resizable], backing: .buffered, defer: false)
        window.title = "Configure SKAI"
        window.minSize = NSSize(width: 650, height: 520)
        window.delegate = self
        window.isReleasedWhenClosed = false
        hosting = NSHostingView(rootView: view(for: model))
        hosting.sizingOptions = []
        window.contentView = hosting
        window.center()
        window.makeKeyAndOrderFront(nil)
    }

    func view(for model: ConfigureModel) -> ConfigureView {
        ConfigureView(model: model, onSave: { [weak self] in self?.save() }, onCancel: { [weak self] in self?.cancel() })
    }

    func save() {
        guard let model, model.canSave else { return }
        do {
            var result = try model.configuration.save()
            result["launchMode"] = agentSession ? "agent" : "standalone"
            result["reconcile"] = agentSession
            savedResult = result
            if agentSession {
                finish(result)
                return
            }
            emit(result)
            // Rebase on the committed files so standalone users can edit and save repeatedly.
            // A reload error must not misreport an already successful save as a failed write.
            var reloadMessage = ""
            do {
                let reloaded = ConfigureModel(configuration: try Configuration(project: model.configuration.project, skaiRoot: skaiRoot),
                                              agentSession: agentSession)
                reloaded.editingLocal = model.editingLocal
                reloaded.expanded = model.expanded
                self.model = reloaded
                hosting.rootView = view(for: reloaded)
            } catch {
                model.requiresReload = true
                reloadMessage = "\n\nThe configuration was saved, but couldn’t be reloaded. Close and reopen the app before further edits.\n" + error.localizedDescription
            }
            let alert = NSAlert()
            alert.messageText = "Configuration saved"
            alert.informativeText = "To apply these changes, ask your agent:\n\n“Apply the saved SKAI configuration for this project.”" + reloadMessage
            alert.alertStyle = .informational
            alert.addButton(withTitle: "OK")
            alert.runModal()
        } catch { showError(error) }
    }

    func cancel() {
        if agentSession { finish(["status": "cancelled", "launchMode": "agent"]) }
        else { finish(["status": "closed", "launchMode": "standalone", "saved": savedResult != nil]) }
    }
    func windowShouldClose(_ sender: NSWindow) -> Bool { cancel(); return false }
    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply { cancel(); return .terminateCancel }
    func showError(_ error: Error) {
        let alert = NSAlert()
        alert.messageText = "Configure SKAI needs attention"
        alert.informativeText = error.localizedDescription
        alert.alertStyle = .warning
        alert.addButton(withTitle: "OK")
        alert.runModal()
    }
    func finish(_ result: [String: Any], code: Int32 = 0) {
        guard !finished else { return }
        finished = true
        window?.orderOut(nil)
        emit(result)
        exit(code)
    }
}

// MARK: - Window content

/// Leading edge shared by the header, the section title and every checkbox.
private let contentLeading: CGFloat = 24
/// Width of the column left of a category checkbox that holds its disclosure chevron.
private let disclosureGutter: CGFloat = 16
/// Indent from a checkbox to its title text, so descriptions align under titles.
private let checkboxTitleIndent: CGFloat = 21
/// Width of the User tab's override menu, fixed so titles and descriptions align across rows.
private let overrideMenuWidth: CGFloat = 92

struct ConfigureView: View {
    @ObservedObject var model: ConfigureModel
    let onSave: () -> Void
    let onCancel: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            header
            ScrollView {
                VStack(alignment: .leading, spacing: 16) {
                    if !model.newSections.isEmpty {
                        Text("New 🔥 — configure to use")
                            .font(.system(size: 18, weight: .bold))
                            .padding(.leading, disclosureGutter)
                        ForEach(model.newSections) { CategorySection(model: model, section: $0) }
                        Divider().padding(.leading, disclosureGutter)
                    }
                    ForEach(model.mainSections) { CategorySection(model: model, section: $0) }
                }
                .padding(.leading, contentLeading - disclosureGutter)
                .padding(.trailing, contentLeading)
                .padding(.vertical, 12)
                .frame(maxWidth: .infinity, alignment: .leading)
            }
            footer
        }
        .frame(minWidth: 650, minHeight: 520)
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 0) {
            Text("Configure SKAI").font(.system(size: 26, weight: .bold))
            Text(model.projectPath)
                .font(.system(size: 12)).foregroundColor(.secondary)
                .textSelection(.enabled)
                .padding(.top, 5)
            Text("Set project components or override them just for you.")
                .font(.system(size: 13))
                .padding(.top, 14)
            HStack(spacing: 8) {
                Picker("Scope", selection: $model.editingLocal) {
                    Text("Project").tag(false)
                    Text("User (\(model.overrideCount))").tag(true)
                }
                .pickerStyle(.segmented)
                .labelsHidden()
                .fixedSize()
                Menu {
                    Button(model.editingLocal ? "Turn all on" : "Select all") { model.selectAll() }
                    Button(model.editingLocal ? "Turn all off" : "Clear optional") { model.clearOptional() }
                    if model.editingLocal {
                        Divider()
                        Button("Use project settings") { model.useProjectSettings() }
                    }
                } label: {
                    Image(systemName: "ellipsis")
                }
                .menuStyle(.borderlessButton)
                .menuIndicator(.hidden)
                .fixedSize()
                .help("More actions")
            }
            .padding(.top, 12)
        }
        .padding(.horizontal, contentLeading)
        .padding(.top, 22)
        .padding(.bottom, 8)
    }

    private var footer: some View {
        HStack(spacing: 8) {
            Text(model.summary).font(.system(size: 12)).foregroundColor(.secondary)
            Spacer()
            Button(model.agentSession ? "Cancel" : "Close", action: onCancel)
                .keyboardShortcut(.cancelAction)
            // Blue like a default button, but with no Return binding: saving always takes a click.
            Button(model.agentSession ? "Save and Apply" : "Save", action: onSave)
                .buttonStyle(.borderedProminent)
                .disabled(!model.canSave)
        }
        .padding(.horizontal, contentLeading)
        .padding(.top, 15)
        .padding(.bottom, 18)
    }
}

/// A category: chevron in the gutter, checkbox aligned with the window title, its description, and
/// (when expanded) its components. Collapsed by default; expanding grows the list downward, so
/// nothing above it moves.
struct CategorySection: View {
    @ObservedObject var model: ConfigureModel
    let section: ConfigureModel.Section

    var body: some View {
        let expanded = model.expanded.contains(section.id)
        VStack(alignment: .leading, spacing: 0) {
            HStack(alignment: .center, spacing: 0) {
                Button {
                    withAnimation(.easeInOut(duration: 0.2)) { model.toggleExpanded(section) }
                } label: {
                    Image(systemName: "chevron.right")
                        .font(.system(size: 10, weight: .bold))
                        .foregroundColor(.secondary)
                        .rotationEffect(.degrees(expanded ? 90 : 0))
                        .frame(width: disclosureGutter, height: 18)
                        .contentShape(Rectangle())
                }
                .buttonStyle(.plain)
                .accessibilityLabel((expanded ? "Hide " : "Show ") + section.name)
                if model.editingLocal {
                    // No category control on User: overrides are set per component.
                    Text(section.name)
                        .font(.system(size: 15, weight: .bold))
                        .foregroundColor(model.hasOverrides(section) ? .accentColor : .secondary)
                } else {
                    TriStateCheckbox(state: model.state(of: section), action: { model.click(section) }) {
                        Text(section.name)
                            .font(.system(size: 15, weight: .bold))
                            .foregroundColor(!model.isEnabled(section) ? Color(nsColor: .disabledControlTextColor)
                                             : model.hasOverrides(section) ? .accentColor : .primary)
                    }
                    .disabled(!model.isEnabled(section))
                }
            }
            if let description = section.description, !description.isEmpty {
                Text(description)
                    .font(.system(size: 12)).foregroundColor(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
                    .padding(.leading, disclosureGutter + (model.editingLocal ? 0 : checkboxTitleIndent))
                    .padding(.top, 3)
            }
            if expanded {
                VStack(alignment: .leading, spacing: 10) {
                    ForEach(section.members, id: \.id) { ComponentRow(model: model, component: $0) }
                }
                .padding(.leading, disclosureGutter + checkboxTitleIndent)
                .padding(.top, 10)
                .transition(.opacity)
            }
        }
    }
}

struct ComponentRow: View {
    @ObservedObject var model: ConfigureModel
    let component: Component

    var body: some View {
        VStack(alignment: .leading, spacing: 3) {
            HStack(spacing: 12) {
                if model.editingLocal {
                    // The override menu sits where the Project tab's checkbox is; required components get
                    // an empty slot of the same width so titles line up.
                    Group {
                        if component.required {
                            Color.clear
                        } else {
                            Picker("Override", selection: Binding(get: { model.overrideChoice(of: component) },
                                                                  set: { model.setOverride(component, to: $0) })) {
                                ForEach(OverrideChoice.allCases, id: \.self) { Text($0.title).tag($0) }
                            }
                            .pickerStyle(.menu)
                            .labelsHidden()
                        }
                    }
                    .frame(width: overrideMenuWidth, height: 20)
                    Text(component.title + (component.required ? " · Always installed" : ""))
                        .font(.system(size: 13))
                        .foregroundColor(component.required ? Color(nsColor: .disabledControlTextColor)
                                         : model.isOverridden(component) ? .accentColor : .secondary)
                        .help(component.id)
                } else {
                    TriStateCheckbox(state: model.state(of: component), action: { model.click(component) }) {
                        Text(component.title + (component.required ? " · Always installed" : ""))
                            .font(.system(size: 13))
                            .foregroundColor(component.required ? Color(nsColor: .disabledControlTextColor)
                                             : model.isOverridden(component) ? .accentColor : .primary)
                    }
                    .disabled(component.required)
                    .help(component.id)
                    if let badge = model.badge(for: component) {
                        Text(badge).font(.system(size: 11, weight: .semibold)).foregroundColor(.accentColor)
                    }
                }
            }
            if let description = component.description, !description.isEmpty {
                Text(description)
                    .font(.system(size: 12)).foregroundColor(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
                    .padding(.leading, model.editingLocal ? overrideMenuWidth + 12 : checkboxTitleIndent)
            }
        }
    }
}

/// A SwiftUI checkbox that can show a dash. SwiftUI draws a dash when a toggle's sources disagree,
/// so the mixed state is two sources, one on and one off; any click goes to the model, which owns
/// what the next state is.
struct TriStateCheckbox<Label: View>: View {
    let state: CheckState
    let action: () -> Void
    @ViewBuilder let label: () -> Label

    private struct Source { let isOn: Binding<Bool> }

    var body: some View {
        let sources = [0, 1].map { index in
            Source(isOn: Binding(get: { state == .on || (state == .mixed && index == 0) },
                                 set: { _ in if index == 0 { action() } }))
        }
        Toggle(sources: sources, isOn: \.isOn, label: label)
            .toggleStyle(.checkbox)
    }
}

@main
struct Main {
    @MainActor static func main() {
        let args = Array(CommandLine.arguments.dropFirst())
        func argument(_ flag: String) -> String? {
            guard let index = args.firstIndex(of: flag), index + 1 < args.count else { return nil }
            return args[index + 1]
        }
        if args.contains("--help") {
            print("SKAIConfigure [--project-root PATH] [--skai-root PATH] [--agent-session] [--resolve --adapter codex|cursor|claude-code --stack generic|swift|android] [--enable ID[,ID] --decline ID[,ID] [--target-sha SHA] [--date YYYY-MM-DD]]")
            return
        }
        let root = argument("--skai-root").map { URL(fileURLWithPath: $0) } ?? Bundle.main.bundleURL.deletingLastPathComponent().deletingLastPathComponent()
        let project = argument("--project-root").map { URL(fileURLWithPath: $0) }
        if args.contains("--resolve") {
            do {
                guard let project else { throw ConfigurationFailure(message: "--project-root is required for --resolve.") }
                let config = try Configuration(project: project, skaiRoot: root)
                emit(try config.resolve(adapter: argument("--adapter") ?? "codex", stack: argument("--stack") ?? "generic"))
            } catch {
                emit(["status": "error", "error": error.localizedDescription], to: .standardError)
                exit(2)
            }
            return
        }
        if args.contains("--enable") || args.contains("--decline") {
            do {
                guard let project else { throw ConfigurationFailure(message: "--project-root is required for --enable/--decline.") }
                let config = try Configuration(project: project, skaiRoot: root)
                func ids(_ flag: String) -> Set<String> { Set((argument(flag) ?? "").split(separator: ",").map(String.init).filter { !$0.isEmpty }) }
                var result: [String: Any] = ["status": "saved"]
                let enabled = ids("--enable"), declined = ids("--decline")
                guard enabled.isDisjoint(with: declined) else { throw ConfigurationFailure(message: "A component cannot be both enabled and declined.") }
                if !enabled.isEmpty { result.merge(try config.enable(enabled)) { _, new in new } }
                if !declined.isEmpty {
                    result.merge(try config.decline(declined, sha: argument("--target-sha") ?? Configuration.checkoutSHA(skaiRoot: root), date: argument("--date") ?? Configuration.today())) { _, new in new }
                }
                emit(result)
            } catch {
                emit(["status": "error", "error": error.localizedDescription], to: .standardError)
                exit(2)
            }
            return
        }
        let delegate = ConfigureApp(project: project, skaiRoot: root, agentSession: args.contains("--agent-session"))
        NSApplication.shared.delegate = delegate
        withExtendedLifetime(delegate) { NSApplication.shared.run() }
    }
}
