"""Run dependency-free token checks against a generated skill response.

Usage:
    python evaluate_outputs.py evals.json 1 output.txt

The evaluator is intentionally small. It provides repeatable smoke checks for
structured expectations; it does not judge visual quality or replace human
review.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def evaluate_text(evaluation: dict[str, Any], text: str) -> dict[str, Any]:
    """Return the token-check result for one evaluation and response text."""

    normalized = text.casefold()
    missing = [
        term
        for term in evaluation.get("must_include", [])
        if term.casefold() not in normalized
    ]
    forbidden = [
        term
        for term in evaluation.get("must_not_include", [])
        if term.casefold() in normalized
    ]
    return {
        "eval_id": evaluation["id"],
        "status": "passed" if not missing and not forbidden else "failed",
        "missing": missing,
        "forbidden": forbidden,
    }


def load_evaluation(evals_path: Path, eval_id: int) -> dict[str, Any]:
    data = json.loads(evals_path.read_text(encoding="utf-8"))
    matches = [item for item in data["evals"] if item["id"] == eval_id]
    if not matches:
        valid_ids = ", ".join(str(item["id"]) for item in data["evals"])
        raise ValueError(f"Unknown eval_id {eval_id}; valid ids: {valid_ids}")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evals_json", type=Path)
    parser.add_argument("eval_id", type=int)
    parser.add_argument("output_text", type=Path)
    args = parser.parse_args()

    try:
        evaluation = load_evaluation(args.evals_json, args.eval_id)
    except ValueError as exc:
        parser.error(str(exc))
    result = evaluate_text(
        evaluation, args.output_text.read_text(encoding="utf-8")
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
