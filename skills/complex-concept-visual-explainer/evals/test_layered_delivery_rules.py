"""Smoke-check the editable, novice-facing diagram contract.

This checks skill instructions only. It cannot judge a rendered figure.
"""

from pathlib import Path
import unittest


SKILL = Path(__file__).resolve().parents[1] / "SKILL.md"


class LayeredDeliveryRulesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.instructions = SKILL.read_text(encoding="utf-8").casefold()

    def test_text_and_illustration_have_separate_owners(self):
        self.assertIn("text-free", self.instructions)
        self.assertIn("native editable objects", self.instructions)
        self.assertIn("opaque strip", self.instructions)

    def test_novice_reading_order_and_editability(self):
        self.assertIn("what enters", self.instructions)
        self.assertIn("what changes it", self.instructions)
        self.assertIn("what comes out", self.instructions)
        self.assertIn("save, reopen and inspect", self.instructions)
        self.assertIn("full name and abbreviation together", self.instructions)
        self.assertIn("do not show the abbreviation alone", self.instructions)
        self.assertIn("must answer a distinct reader question", self.instructions)
        self.assertIn("separate generated artwork", self.instructions)

    def test_old_new_display_review_precedes_replacement(self):
        self.assertIn("matched old/new comparison", self.instructions)
        self.assertIn("every actual delivery scale", self.instructions)
        self.assertIn("user has approved replacement", self.instructions)


if __name__ == "__main__":
    unittest.main()
