import json
import unittest
from pathlib import Path

from evaluator import evaluate_candidate

ROOT = Path(__file__).resolve().parents[1]
RULES = json.loads((ROOT / "rules.json").read_text(encoding="utf-8"))


class EvaluatorTests(unittest.TestCase):
    def load_candidate(self, name: str):
        return json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))

    def test_known_pass_case(self):
        report = evaluate_candidate(self.load_candidate("pass_bracket.json"), RULES)
        self.assertEqual(report["status"], "PASS")
        self.assertGreaterEqual(report["score_percent"], 80.0)

    def test_known_fail_case(self):
        report = evaluate_candidate(self.load_candidate("fail_bracket.json"), RULES)
        self.assertEqual(report["status"], "FAIL")

    def test_missing_required_drawing_metadata_fails(self):
        candidate = self.load_candidate("pass_bracket.json")
        candidate["drawing_has_material"] = False
        report = evaluate_candidate(candidate, RULES)
        self.assertEqual(report["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
