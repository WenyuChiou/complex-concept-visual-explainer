"""Run the skill eval token checks against a generated text file.

Usage:
    python evaluate_outputs.py evals.json 1 output.txt

The evaluator is intentionally small and dependency-free. It provides a
repeatable smoke test for the structured expectations in evals.json; it does
not judge visual quality or replace human review.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evals_json", type=Path)
    parser.add_argument("eval_id", type=int)
    parser.add_argument("output_text", type=Path)
    args = parser.parse_args()

    data = json.loads(args.evals_json.read_text(encoding="utf-8"))
    evaluation = next(item for item in data["evals"] if item["id"] == args.eval_id)
    text = args.output_text.read_text(encoding="utf-8").casefold()
    missing = [term for term in evaluation["must_include"] if term.casefold() not in text]
    forbidden = [term for term in evaluation["must_not_include"] if term.casefold() in text]

    result = {
        "eval_id": args.eval_id,
        "status": "passed" if not missing and not forbidden else "failed",
        "missing": missing,
        "forbidden": forbidden,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
