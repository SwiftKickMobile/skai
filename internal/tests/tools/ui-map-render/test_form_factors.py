"""Tests for form-factor marking in Bin/ui-map-render.py (skai#67) and the identifier rule.

Run after any change to ui-map-render.py or ui-map.schema.json:
    python3 internal/tests/tools/ui-map-render/test_form_factors.py
Each case renders a small map with `uv run` and checks it renders, or fails with the expected message.
"""
from pathlib import Path
import json
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
RENDERER = ROOT / "Bin/ui-map-render.py"

# The three cases from skai#67 plus a tablet-only chain: Log is pushed on a phone and a card on a
# tablet; the panels switch one at a time on a phone and sit side by side on a tablet; settings
# opens full screen on a phone and as a card on a tablet; rounds and its detail exist only on a tablet.
VALID = """\
version: 1
app: Darts
modal_styles: [full_screen, card]
form_factors: [phone, tablet]
domains:
  game:
    nav:
      - to: log
        form_factor: [phone]
    modal:
      - to: log
        form_factor: [tablet]
        scene:
          modal_style: card
      - settings:
          modal_style: { phone: full_screen, tablet: card }
      - rounds:
          form_factor: [tablet]
          modal_style: card
          nav:
            - rounds_detail:
                form_factor: [tablet]
    child:
      - to: panel_a
        form_factor: [phone]
        scene: {}
      - to: panel_b
        form_factor: [phone]
        scene: {}
    composite:
      - to: panel_a
        form_factor: [tablet]
      - to: panel_b
        form_factor: [tablet]
"""


def render(text, *extra):
    with tempfile.TemporaryDirectory() as directory:
        source = Path(directory) / "map.yaml"
        page = Path(directory) / "map.html"
        source.write_text(text)
        result = subprocess.run(
            ["uv", "run", "--quiet", str(RENDERER), str(source), "-o", str(Path(directory) / "map.mmd"),
             "--html", str(page), *extra],
            capture_output=True, text=True,
        )
        model = None
        if result.returncode == 0:
            model = json.loads(re.search(r"window\.UI_MAP = (.*);</script>", page.read_text()).group(1))
        return result, model


class FormFactors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if shutil.which("uv") is None:
            raise unittest.SkipTest("uv is required to run the renderer")

    def assertFails(self, text, message):
        result, _ = render(text)
        self.assertNotEqual(result.returncode, 0, "expected the map to be rejected")
        self.assertIn(message, result.stderr + result.stdout)

    def test_the_issue_examples_render(self):
        result, model = render(VALID)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(model["formFactors"], ["phone", "tablet"])
        self.assertEqual(model["scenes"]["rounds"]["formFactors"], ["tablet"])
        self.assertIsNone(model["scenes"]["settings"]["formFactors"])
        nav = next(r for r in model["scenes"]["game"]["routes"] if r["kind"] == "nav")
        self.assertEqual(nav["formFactors"], [["phone"]])
        modal = next(r for r in model["scenes"]["game"]["routes"] if r["kind"] == "modal")
        self.assertEqual(modal["formFactors"], [["tablet"], None, None])

    def test_several_routes_from_one_parent_need_no_primary_parent(self):
        _, model = render(VALID)
        self.assertEqual((model["scenes"]["log"]["parent"], model["scenes"]["log"]["parentKind"]), ("game", "modal"))
        self.assertEqual((model["scenes"]["panel_a"]["parent"], model["scenes"]["panel_a"]["parentKind"]), ("game", "child"))

    def test_marking_without_a_vocabulary(self):
        self.assertFails(VALID.replace("form_factors: [phone, tablet]\n", ""), "no top-level 'form_factors' vocabulary")

    def test_value_outside_the_vocabulary(self):
        self.assertFails(VALID.replace("- to: log\n        form_factor: [phone]", "- to: log\n        form_factor: [watch]"),
                         "form_factor [watch] is not in form_factors")

    def test_route_marked_where_its_destination_does_not_exist(self):
        text = VALID.replace("      - rounds:\n", "      - to: rounds\n        form_factor: [phone]\n        scene:\n")
        self.assertFails(text, "but 'rounds' exists only on [tablet]")

    def test_undeclared_screen_reachable_on_some_form_factors(self):
        text = VALID.replace("            - rounds_detail:\n                form_factor: [tablet]", "            - rounds_detail: {}")
        self.assertFails(text, "Scene 'rounds_detail' is reachable only on [tablet]; declare form_factor: [tablet]")

    def test_declared_form_factor_no_route_reaches(self):
        text = VALID.replace("                form_factor: [tablet]", "                form_factor: [phone, tablet]")
        self.assertFails(text, "no route reaches it on [phone]")

    def test_scene_reachable_on_no_form_factor(self):
        # detail is defined (and checked) before its parent, rounds. rounds declares phone and tablet but
        # is reached only on a tablet, so the phone-only route into detail is never usable.
        text = """\
version: 1
app: Darts
modal_styles: [card]
form_factors: [phone, tablet]
domains:
  history:
    scenes:
      - detail: {}
  game:
    modal:
      - to: rounds
        form_factor: [tablet]
        scene:
          form_factor: [phone, tablet]
          modal_style: card
          nav:
            - to: detail
              form_factor: [phone]
"""
        self.assertFails(text, "Scene 'detail' can't be reached on any form factor")

    def test_modal_style_map_missing_a_form_factor(self):
        self.assertFails(VALID.replace("{ phone: full_screen, tablet: card }", "{ phone: full_screen }"),
                         "presented modally on [tablet] but has no modal_style for it")

    def test_modal_style_map_for_a_form_factor_never_presented(self):
        text = VALID.replace("        scene:\n          modal_style: card", "        scene:\n          modal_style: { phone: card, tablet: card }")
        self.assertFails(text, "has a modal_style for [phone], but no modal route presents it there")

    def test_scene_listed_twice_in_one_container(self):
        self.assertFails(VALID.replace("    modal:\n", "    modal:\n      - settings\n"), "'settings' is listed twice in 'game.modal'")

    def test_identifiers_are_lower_snake_case(self):
        self.assertFails(VALID.replace("rounds_detail", "RoundsDetail"), "'RoundsDetail' is not lower snake case")

    def test_map_without_form_factors_is_unchanged(self):
        result, model = render("version: 1\napp: Notes\ndomains:\n  home:\n    nav:\n      - detail: {}\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(model["formFactors"], [])


if __name__ == "__main__":
    unittest.main()
