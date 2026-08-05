"""Run every dependency-free skill fixture.

Usage from the repository root:
    python skills/complex-concept-visual-explainer/evals/run_all.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from evaluate_outputs import evaluate_text


ROOT = Path(__file__).resolve().parent
EVALS_PATH = ROOT / "evals.json"
FIXTURES_DIR = ROOT / "fixtures"
NEGATIVE_FIXTURES_DIR = ROOT / "negative_fixtures"


def main() -> int:
    data = json.loads(EVALS_PATH.read_text(encoding="utf-8"))
    results = []
    for evaluation in data["evals"]:
        fixture = FIXTURES_DIR / f"{evaluation['id']}.txt"
        if not fixture.exists():
            results.append(
                {
                    "eval_id": evaluation["id"],
                    "status": "failed",
                    "missing": [f"fixture:{fixture.name}"],
                    "forbidden": [],
                }
            )
            continue
        results.append(
            evaluate_text(evaluation, fixture.read_text(encoding="utf-8"))
        )

    negative_results = []
    for evaluation in data["evals"]:
        fixture = NEGATIVE_FIXTURES_DIR / f"{evaluation['id']}.txt"
        if not fixture.exists():
            continue
        check = evaluate_text(evaluation, fixture.read_text(encoding="utf-8"))
        negative_results.append(
            {
                "eval_id": evaluation["id"],
                "status": "passed" if check["status"] == "failed" else "failed",
                "expected": "failed",
                "observed": check["status"],
                "missing": check["missing"],
                "forbidden": check["forbidden"],
            }
        )

    print(json.dumps({"positive": results, "negative": negative_results}, ensure_ascii=False, indent=2))
    all_passed = all(result["status"] == "passed" for result in results + negative_results)
    return 0 if all_passed and negative_results else 1


if __name__ == "__main__":
    sys.exit(main())
