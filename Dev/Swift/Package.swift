// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "SKAI",
    platforms: [
        .iOS(.v17),
        .macOS(.v14),
    ],
    products: [
        .library(name: "SKAISwiftUI", targets: ["SKAISwiftUI"]),
    ],
    targets: [
        .target(name: "SKAISwiftUI"),
    ]
)
