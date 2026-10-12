import AppKit

@MainActor
final class ConfigureApp: NSObject, NSApplicationDelegate, NSWindowDelegate {
    var configuration: Configuration?
    var window: NSWindow!
    var buttons: [String: NSButton] = [:]
    var categories: [String: NSButton] = [:]
    var newCategories: [String: NSButton] = [:]
    var overrideBadges: [String: NSTextField] = [:]
    let agentSession: Bool
    var scopeControl: NSSegmentedControl!
    var actionsButton: NSButton!
    var actionsMenu: NSMenu!
    var allAction: NSMenuItem!
    var noneAction: NSMenuItem!
    var resetAction: NSMenuItem!
    var resetSeparator: NSMenuItem!
    var editingLocal: Bool { scopeControl?.selectedSegment == 1 }
    var countLabel = NSTextField(labelWithString: "")
    var saveButton: NSButton!
    var finished = false
    var savedResult: [String: Any]?
    var requiresReload = false
    let skaiRoot: URL
    let initialProject: URL?

    init(project: URL?, skaiRoot: URL, agentSession: Bool = false) {
        self.agentSession = agentSession
        self.initialProject = project
        self.skaiRoot = skaiRoot
    }

    func applicationDidFinishLaunching(_ notification: Notification) {
        if let icon = Bundle.main.url(forResource: "SKAIConfigure", withExtension: "icns"),
           let image = NSImage(contentsOf: icon) { NSApp.applicationIconImage = image }
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
            configuration = try Configuration(project: project!, skaiRoot: skaiRoot)
            makeWindow()
            emit(["status": "ready", "project": configuration!.project.path, "configPath": configuration!.configURL.path, "localConfigPath": configuration!.localConfigURL.path, "launchMode": agentSession ? "agent" : "standalone"])
        } catch {
            showError(error)
            finish(["status": "error", "error": error.localizedDescription], code: 2)
        }
    }

    func text(_ value: String, size: CGFloat = 13, color: NSColor = .labelColor) -> NSTextField {
        let field = NSTextField(wrappingLabelWithString: value)
        field.font = .systemFont(ofSize: size)
        field.textColor = color
        field.isSelectable = true
        field.translatesAutoresizingMaskIntoConstraints = false
        return field
    }

    func makeWindow() {
        let config = configuration!
        window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 750, height: 770),
                          styleMask: [.titled, .closable, .miniaturizable, .resizable], backing: .buffered, defer: false)
        window.title = "Configure SKAI"
        window.minSize = NSSize(width: 650, height: 520)
        window.delegate = self
        window.isReleasedWhenClosed = false
        let content = window.contentView!
        let title = text("Configure SKAI", size: 26)
        title.font = .boldSystemFont(ofSize: 26)
        let project = text(config.project.path, size: 12, color: .secondaryLabelColor)
        let intro = text("Set project components or override them just for you.")
        scopeControl = NSSegmentedControl(labels: ["Project", "User"], trackingMode: .selectOne, target: self, action: #selector(scopeChanged(_:)))
        scopeControl.selectedSegment = 0
        let actions = NSButton(image: NSImage(systemSymbolName: "ellipsis", accessibilityDescription: "More actions")!,
                               target: self, action: #selector(showActions(_:)))
        actions.setButtonType(.momentaryChange)
        actions.isBordered = false
        actions.imagePosition = .imageOnly
        actions.imageScaling = .scaleProportionallyDown
        actions.focusRingType = .none
        actions.toolTip = "More actions"
        actions.setAccessibilityLabel("More actions")
        actions.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            actions.widthAnchor.constraint(equalToConstant: 28),
            actions.heightAnchor.constraint(equalToConstant: 24)
        ])
        let menu = NSMenu()
        menu.autoenablesItems = false
        allAction = NSMenuItem(title: "Select all", action: #selector(selectAll(_:)), keyEquivalent: "")
        noneAction = NSMenuItem(title: "Clear optional", action: #selector(clearOptional(_:)), keyEquivalent: "")
        resetAction = NSMenuItem(title: "Use project settings", action: #selector(resetOverrides(_:)), keyEquivalent: "")
        for item in [allAction!, noneAction!] { item.target = self; menu.addItem(item) }
        resetSeparator = .separator()
        menu.addItem(resetSeparator)
        resetAction.target = self
        menu.addItem(resetAction)
        actionsMenu = menu
        actionsButton = actions
        let tools = NSStackView(views: [scopeControl, actions])
        tools.spacing = 8
        tools.translatesAutoresizingMaskIntoConstraints = false
        let scroll = NSScrollView()
        scroll.hasVerticalScroller = true
        scroll.autohidesScrollers = true
        scroll.drawsBackground = false
        scroll.translatesAutoresizingMaskIntoConstraints = false
        let list = NSStackView()
        list.orientation = .vertical
        list.alignment = .leading
        list.spacing = 6
        list.edgeInsets = NSEdgeInsets(top: 12, left: 12, bottom: 16, right: 12)
        list.translatesAutoresizingMaskIntoConstraints = false
        scroll.documentView = list
        NSLayoutConstraint.activate([list.widthAnchor.constraint(equalTo: scroll.contentView.widthAnchor)])
        let newIDs = config.newComponentIDs
        // New components open checked, so a plain Save installs them; unchecking one declines it.
        config.selected.formUnion(newIDs)
        func componentRow(_ component: Component, badgeText: String? = nil) -> NSStackView {
            let checkbox = NSButton(checkboxWithTitle: component.title + (component.required ? " · Always installed" : ""), target: self, action: #selector(componentChanged(_:)))
            checkbox.identifier = NSUserInterfaceItemIdentifier(component.id)
            checkbox.isEnabled = !component.required
            checkbox.toolTip = component.id
            buttons[component.id] = checkbox
            let detail = text(component.description ?? "", size: 12, color: .secondaryLabelColor)
            let badge = text("", size: 11, color: .controlAccentColor)
            badge.font = .systemFont(ofSize: 11, weight: .semibold)
            badge.setContentCompressionResistancePriority(.required, for: .horizontal)
            overrideBadges[component.id] = badge
            var controlViews: [NSView] = [checkbox, badge]
            if let badgeText {
                let category = text(badgeText, size: 11, color: .tertiaryLabelColor)
                category.setContentCompressionResistancePriority(.required, for: .horizontal)
                controlViews.append(category)
            }
            let controls = NSStackView(views: controlViews)
            controls.spacing = 12
            let row = NSStackView(views: [controls, detail])
            row.orientation = .vertical
            row.alignment = .leading
            row.spacing = 3
            row.edgeInsets = NSEdgeInsets(top: 3, left: 18, bottom: 7, right: 10)
            list.addArrangedSubview(row)
            row.widthAnchor.constraint(equalTo: list.widthAnchor, constant: -24).isActive = true
            detail.widthAnchor.constraint(equalTo: row.widthAnchor, constant: -28).isActive = true
            return row
        }
        // Category headers look identical in both lists; only the action and registry differ.
        func categoryHeader(_ group: String, members: [Component], inNewSection: Bool) {
            let header = NSButton(checkboxWithTitle: group, target: self, action: inNewSection ? #selector(newCategoryChanged(_:)) : #selector(categoryChanged(_:)))
            header.identifier = NSUserInterfaceItemIdentifier((inNewSection ? "new:" : "") + group)
            header.allowsMixedState = true
            header.font = .boldSystemFont(ofSize: 15)
            header.isEnabled = members.contains { !$0.required }
            if inNewSection { newCategories[group] = header } else { categories[group] = header }
            let headerRow = NSStackView(views: [header])
            headerRow.orientation = .vertical
            headerRow.alignment = .leading
            headerRow.spacing = 3
            headerRow.edgeInsets = NSEdgeInsets(top: 12, left: 0, bottom: 4, right: 0)
            list.addArrangedSubview(headerRow)
            headerRow.widthAnchor.constraint(equalTo: list.widthAnchor, constant: -24).isActive = true
            if let description = config.componentCategories.first(where: { $0.name == group })?.description, !description.isEmpty {
                let detail = text(description, size: 12, color: .secondaryLabelColor)
                let descriptionRow = NSStackView(views: [detail])
                descriptionRow.edgeInsets = NSEdgeInsets(top: 0, left: 18, bottom: 0, right: 0)
                headerRow.addArrangedSubview(descriptionRow)
                descriptionRow.widthAnchor.constraint(equalTo: headerRow.widthAnchor).isActive = true
                detail.widthAnchor.constraint(equalTo: descriptionRow.widthAnchor, constant: -18).isActive = true
            }
            for component in members { _ = componentRow(component) }
        }
        func groupOrder(_ names: Set<String>) -> [String] {
            let preferred = config.componentCategories.map(\.name)
            return preferred.filter { names.contains($0) } + names.subtracting(preferred).sorted()
        }
        if !newIDs.isEmpty {
            // New in this SKAI version and never chosen: listed first until Save, then in their categories.
            let title = text("New 🔥 — configure to use", size: 18)
            title.font = .boldSystemFont(ofSize: 18)
            let titleRow = NSStackView(views: [title])
            titleRow.edgeInsets = NSEdgeInsets(top: 8, left: 0, bottom: 0, right: 0)
            list.addArrangedSubview(titleRow)
            titleRow.widthAnchor.constraint(equalTo: list.widthAnchor, constant: -24).isActive = true
            let fresh = config.components.filter { newIDs.contains($0.id) }
            for group in groupOrder(Set(fresh.map(\.group))) {
                categoryHeader(group, members: fresh.filter { $0.group == group }, inNewSection: true)
            }
            let divider = NSBox()
            divider.boxType = .separator
            divider.translatesAutoresizingMaskIntoConstraints = false
            // Measured: 17 after the last row and 12 after the line give equal 22pt gaps around it.
            if let above = list.arrangedSubviews.last { list.setCustomSpacing(17, after: above) }
            list.addArrangedSubview(divider)
            divider.widthAnchor.constraint(equalTo: list.widthAnchor, constant: -24).isActive = true
            list.setCustomSpacing(12, after: divider)
        }
        let rest = config.components.filter { !newIDs.contains($0.id) }
        for group in groupOrder(Set(rest.map(\.group))) {
            categoryHeader(group, members: rest.filter { $0.group == group }, inNewSection: false)
        }
        countLabel.textColor = .secondaryLabelColor
        countLabel.font = .systemFont(ofSize: 12)
        countLabel.translatesAutoresizingMaskIntoConstraints = false
        let cancel = NSButton(title: agentSession ? "Cancel" : "Close", target: self, action: #selector(cancel(_:)))
        cancel.keyEquivalent = "\u{1b}"
        let save = NSButton(title: agentSession ? "Save and Apply" : "Save", target: self, action: #selector(save(_:)))
        saveButton = save
        // Looks like the default action but has no Return binding: saving takes a click, so a
        // keystroke meant for another app cannot save.
        save.bezelColor = .controlAccentColor
        let footer = NSStackView(views: [cancel, save])
        footer.spacing = 8
        footer.translatesAutoresizingMaskIntoConstraints = false
        for view in [title, project, intro, scroll, countLabel, footer] { content.addSubview(view) }
        content.addSubview(tools)
        NSLayoutConstraint.activate([
            tools.topAnchor.constraint(equalTo: intro.bottomAnchor, constant: 12),
            tools.leadingAnchor.constraint(equalTo: title.leadingAnchor),
            scroll.topAnchor.constraint(equalTo: tools.bottomAnchor, constant: 8)
        ])
        NSLayoutConstraint.activate([
            title.topAnchor.constraint(equalTo: content.topAnchor, constant: 22), title.leadingAnchor.constraint(equalTo: content.leadingAnchor, constant: 24),
            project.topAnchor.constraint(equalTo: title.bottomAnchor, constant: 5), project.leadingAnchor.constraint(equalTo: title.leadingAnchor), project.trailingAnchor.constraint(equalTo: content.trailingAnchor, constant: -24),
            intro.topAnchor.constraint(equalTo: project.bottomAnchor, constant: 14), intro.leadingAnchor.constraint(equalTo: title.leadingAnchor), intro.trailingAnchor.constraint(equalTo: project.trailingAnchor),
            scroll.leadingAnchor.constraint(equalTo: content.leadingAnchor, constant: 12), scroll.trailingAnchor.constraint(equalTo: content.trailingAnchor, constant: -12),
            scroll.bottomAnchor.constraint(equalTo: footer.topAnchor, constant: -15),
            footer.trailingAnchor.constraint(equalTo: content.trailingAnchor, constant: -24), footer.bottomAnchor.constraint(equalTo: content.bottomAnchor, constant: -18),
            countLabel.leadingAnchor.constraint(equalTo: title.leadingAnchor), countLabel.centerYAnchor.constraint(equalTo: footer.centerYAnchor),
            countLabel.trailingAnchor.constraint(lessThanOrEqualTo: footer.leadingAnchor, constant: -12)
        ])
        refresh()
        // Start with the window itself as responder: no focus ring or row-induced scrolling.
        window.initialFirstResponder = nil
        window.center()
        window.makeKeyAndOrderFront(nil)
        window.makeFirstResponder(nil)
        // A non-flipped document's origin is its bottom. Scroll only after layout resolves its height.
        func showBeginning() {
            content.layoutSubtreeIfNeeded()
            list.layoutSubtreeIfNeeded()
            let bounds = list.bounds
            let top = list.isFlipped ? bounds.minY : max(bounds.minY, bounds.maxY - scroll.contentView.bounds.height)
            scroll.contentView.scroll(to: NSPoint(x: bounds.minX, y: top))
            scroll.reflectScrolledClipView(scroll.contentView)
        }
        showBeginning()
        DispatchQueue.main.async { showBeginning() }
    }

    func refresh() {
        let config = configuration!
        for component in config.components {
            let id = component.id
            buttons[id]?.allowsMixedState = editingLocal && !component.required
            buttons[id]?.state = component.required ? .on : (editingLocal ? config.overrides[id].map { $0 ? .on : .off } ?? .mixed : (config.selected.contains(id) ? .on : .off))
            buttons[id]?.toolTip = editingLocal && !component.required ? "Checked: Turn on. Unchecked: Turn off. Dash: Use project setting. Click to cycle." : component.id
            overrideBadges[id]?.stringValue = config.overrides[id].map { userValue in
                let scope = editingLocal ? "Project" : "User"
                let value = editingLocal ? config.selected.contains(id) : userValue
                return scope + ": " + (value ? "On" : "Off")
            } ?? ""
            overrideBadges[id]?.isHidden = config.overrides[id] == nil
            if let button = buttons[id] {
                let titleColor: NSColor = component.required ? .disabledControlTextColor :
                    (editingLocal && config.overrides[id] == nil ? .secondaryLabelColor : .labelColor)
                button.attributedTitle = NSAttributedString(string: component.title + (component.required ? " · Always installed" : ""),
                    attributes: [.foregroundColor: titleColor, .font: button.font ?? NSFont.systemFont(ofSize: NSFont.systemFontSize)])
            }
        }
        scopeControl.setLabel("User (\(config.overrides.count))", forSegment: 1)
        allAction.title = editingLocal ? "Turn all on" : "Select all"
        noneAction.title = editingLocal ? "Turn all off" : "Clear optional"
        resetAction.isHidden = !editingLocal
        resetSeparator.isHidden = resetAction.isHidden

        let newIDs = config.newComponentIDs
        for (group, button) in categories {
            let ids = Set(config.components.filter { $0.group == group && !$0.required && !newIDs.contains($0.id) }.map(\.id))
            let count = ids.intersection(config.selected).count
            let hasOverride = ids.contains { config.overrides[$0] != nil }
            let titleColor: NSColor = !button.isEnabled ? .disabledControlTextColor :
                (editingLocal && !hasOverride ? .secondaryLabelColor : .labelColor)
            button.attributedTitle = NSAttributedString(string: group,
                attributes: [.foregroundColor: titleColor, .font: button.font ?? NSFont.boldSystemFont(ofSize: 15)])
            if editingLocal && !ids.isEmpty {
                let values = Set(ids.map { config.overrides[$0] })
                button.state = values == Set([Optional(true)]) ? .on : (values == Set([Optional(false)]) ? .off : .mixed)
                button.toolTip = "Checked: Turn all on. Unchecked: Turn all off. Dash: use project settings (also shown for a mixed group)."
            } else {
                button.state = ids.isEmpty || count == ids.count ? .on : (count == 0 ? .off : .mixed)
                button.toolTip = nil
            }
        }
        for (group, button) in newCategories {
            let ids = Set(config.components.filter { $0.group == group && newIDs.contains($0.id) }.map(\.id))
            if editingLocal {
                let values = Set(ids.map { config.overrides[$0] })
                button.state = values == Set([Optional(true)]) ? .on : (values == Set([Optional(false)]) ? .off : .mixed)
            } else {
                let count = ids.intersection(config.selected).count
                button.state = count == ids.count ? .on : (count == 0 ? .off : .mixed)
            }
        }
        countLabel.stringValue = "\(config.effectiveSelection.count) of \(config.optionalIDs.count) effective · \(config.overrides.count) overrides"
        saveButton.isEnabled = config.hasChanges && !requiresReload
    }

    @objc func showActions(_ sender: NSButton) {
        let point = NSPoint(x: sender.bounds.minX, y: sender.isFlipped ? sender.bounds.maxY : sender.bounds.minY)
        actionsMenu.popUp(positioning: nil, at: point, in: sender)
    }

    @objc func componentChanged(_ sender: NSButton) {
        guard let id = sender.identifier?.rawValue else { return }
        if editingLocal {
            if sender.state == .mixed { configuration!.overrides.removeValue(forKey: id) }
            else { configuration!.overrides[id] = sender.state == .on }
        } else {
            if sender.state == .on { configuration!.selected.insert(id) } else { configuration!.selected.remove(id) }
        }
        refresh()
    }
    @objc func categoryChanged(_ sender: NSButton) {
        let newIDs = configuration!.newComponentIDs
        let ids = Set(configuration!.components.filter { $0.group == sender.identifier?.rawValue && !$0.required && !newIDs.contains($0.id) }.map(\.id))
        if editingLocal {
            for id in ids {
                if sender.state == .mixed { configuration!.overrides.removeValue(forKey: id) }
                else { configuration!.overrides[id] = sender.state == .on }
            }
        } else {
            if ids.isSubset(of: configuration!.selected) { configuration!.selected.subtract(ids) } else { configuration!.selected.formUnion(ids) }
        }
        refresh()
    }
    @objc func newCategoryChanged(_ sender: NSButton) {
        let group = String((sender.identifier?.rawValue ?? "").dropFirst(4))
        let newIDs = configuration!.newComponentIDs
        let ids = Set(configuration!.components.filter { $0.group == group && newIDs.contains($0.id) }.map(\.id))
        if editingLocal {
            for id in ids {
                if sender.state == .mixed { configuration!.overrides.removeValue(forKey: id) }
                else { configuration!.overrides[id] = sender.state == .on }
            }
        } else {
            if ids.isSubset(of: configuration!.selected) { configuration!.selected.subtract(ids) } else { configuration!.selected.formUnion(ids) }
        }
        refresh()
    }
    @objc func selectAll(_ sender: Any?) {
        if editingLocal { configuration!.overrides = Dictionary(uniqueKeysWithValues: configuration!.optionalIDs.map { ($0, true) }) }
        else { configuration!.selected = configuration!.optionalIDs }
        refresh()
    }
    @objc func clearOptional(_ sender: Any?) {
        if editingLocal { configuration!.overrides = Dictionary(uniqueKeysWithValues: configuration!.optionalIDs.map { ($0, false) }) }
        else { configuration!.selected = [] }
        refresh()
    }
    @objc func scopeChanged(_ sender: Any?) { refresh() }
    @objc func resetOverrides(_ sender: Any?) { configuration!.overrides = [:]; refresh() }
    @objc func save(_ sender: Any?) {
        guard !requiresReload, configuration!.hasChanges else { return }
        do {
            var result = try configuration!.save()
            result["launchMode"] = agentSession ? "agent" : "standalone"
            result["reconcile"] = agentSession
            savedResult = result
            if agentSession {
                finish(result)
                return
            }
            emit(result)
            // Rebase on committed files so standalone users can edit and save repeatedly.
            // A reload error must not misreport an already successful save as a failed write.
            let current = configuration!
            var reloadMessage = ""
            do {
                configuration = try Configuration(project: current.project, skaiRoot: current.skaiRoot)
            } catch {
                requiresReload = true
                reloadMessage = "\n\nThe configuration was saved, but couldn’t be reloaded. Close and reopen the app before further edits.\n" + error.localizedDescription
            }
            refresh()
            let alert = NSAlert()
            alert.messageText = "Configuration saved"
            alert.informativeText = "To apply these changes, ask your agent:\n\n“Apply the saved SKAI configuration for this project.”" + reloadMessage
            alert.alertStyle = .informational
            alert.addButton(withTitle: "OK")
            alert.runModal()
        } catch { showError(error) }
    }
    @objc func cancel(_ sender: Any?) {
        if agentSession { finish(["status": "cancelled", "launchMode": "agent"]) }
        else { finish(["status": "closed", "launchMode": "standalone", "saved": savedResult != nil]) }
    }
    func windowShouldClose(_ sender: NSWindow) -> Bool { cancel(nil); return false }
    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply { cancel(nil); return .terminateCancel }
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
