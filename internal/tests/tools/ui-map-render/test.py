"""Automated test for Bin/ui-map-render.py against the worked example in Guides/UIMap/ui-map-demo.md.

Run after any change to ui-map-render.py: python3 internal/tests/tools/ui-map-render/test.py
Renders the guide's YAML block with `uv run` (the renderer declares its own dependencies) and checks
the Mermaid text matches the guide's Mermaid block exactly.
"""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
RENDERER = ROOT / "Bin/ui-map-render.py"
DEMO = ROOT / "Guides/UIMap/ui-map-demo.md"


def fenced_block(text, language):
    blocks = re.findall(rf"^```{language}\n(.*?)^```$", text, flags=re.S | re.M)
    if len(blocks) != 1:
        raise AssertionError(f"expected one ```{language} block in {DEMO.name}, found {len(blocks)}")
    return blocks[0]


class DemoRender(unittest.TestCase):
    def test_demo_yaml_renders_to_the_guide_mermaid_block(self):
        self.assertIsNotNone(shutil.which("uv"), "uv is required to run the renderer")
        guide = DEMO.read_text()
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "ui-map-demo.yaml"
            output = Path(directory) / "ui-map-demo.mmd"
            source.write_text(fenced_block(guide, "yaml"))
            result = subprocess.run(["uv", "run", "--quiet", str(RENDERER), str(source), "-o", str(output)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(output.read_text().rstrip("\n"), fenced_block(guide, "mermaid").rstrip("\n"))


if __name__ == "__main__":
    unittest.main()
