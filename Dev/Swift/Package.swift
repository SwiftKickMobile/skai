// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "SKAI",
    platforms: [
        .iOS(.v18),
        .macOS(.v15),
    ],
    products: [
        .library(name: "SKAISwiftUI", targets: ["SKAISwiftUI"]),
    ],
    targets: [
        .target(name: "SKAISwiftUI"),
    ]
)
