from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class CheckResult:
    check: str
    passed: bool
    score: float
    max_score: float
    message: str


def load_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def evaluate_candidate(candidate: dict, rules: dict) -> dict:
    checks: list[CheckResult] = []

    def add(name: str, passed: bool, weight: float, message: str) -> None:
        checks.append(
            CheckResult(
                check=name,
                passed=bool(passed),
                score=weight if passed else 0.0,
                max_score=weight,
                message=message,
            )
        )

    criteria = rules["benchmark_criteria"]
    thickness = float(candidate["thickness_mm"])
    bend_radius = float(candidate["inside_bend_radius_mm"])
    min_web = float(candidate["min_web_width_mm"])
    holes = [float(x) for x in candidate.get("hole_diameters_mm", [])]
    min_edge = float(candidate["min_hole_edge_distance_mm"])

    add(
        "thickness_range",
        criteria["min_thickness_mm"] <= thickness <= criteria["max_thickness_mm"],
        criteria["weights"]["thickness_range"],
        f"Thickness {thickness:.2f} mm within benchmark range.",
    )

    required_bend_radius = criteria["min_bend_radius_to_thickness"] * thickness
    add(
        "bend_radius",
        bend_radius >= required_bend_radius,
        criteria["weights"]["bend_radius"],
        f"Bend radius {bend_radius:.2f} mm >= {required_bend_radius:.2f} mm benchmark.",
    )

    required_web = criteria["min_web_to_thickness"] * thickness
    add(
        "web_width",
        min_web >= required_web,
        criteria["weights"]["web_width"],
        f"Web {min_web:.2f} mm >= {required_web:.2f} mm benchmark.",
    )

    if holes:
        required_edge = criteria["min_hole_edge_to_diameter"] * max(holes)
        add(
            "hole_edge_distance",
            min_edge >= required_edge,
            criteria["weights"]["hole_edge_distance"],
            f"Edge distance {min_edge:.2f} mm >= {required_edge:.2f} mm benchmark.",
        )
    else:
        add(
            "hole_edge_distance",
            True,
            criteria["weights"]["hole_edge_distance"],
            "No holes declared.",
        )

    drawing_complete = all(
        bool(candidate.get(key, False))
        for key in [
            "drawing_has_units",
            "drawing_has_material",
            "drawing_has_thickness",
        ]
    )
    add(
        "drawing_completeness",
        drawing_complete,
        criteria["weights"]["drawing_completeness"],
        "Drawing includes units, material and thickness.",
    )

    add(
        "bom_completeness",
        bool(candidate.get("bom_complete", False)),
        criteria["weights"]["bom_completeness"],
        "BOM completeness flag.",
    )

    total = sum(item.score for item in checks)
    maximum = sum(item.max_score for item in checks)
    score_percent = 100.0 * total / maximum if maximum else 0.0

    mandatory_checks = set(criteria["mandatory_checks"])
    mandatory_pass = all(
        item.passed for item in checks if item.check in mandatory_checks
    )
    status = (
        "PASS"
        if score_percent >= criteria["pass_threshold_percent"] and mandatory_pass
        else "FAIL"
    )

    return {
        "candidate_id": candidate.get("candidate_id", "unknown"),
        "benchmark": rules["name"],
        "status": status,
        "score_percent": round(score_percent, 1),
        "checks": [asdict(item) for item in checks],
        "note": (
            "Configurable portfolio benchmark criteria only; not universal "
            "manufacturing standards or production-release rules."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate CAD/manufacturing candidate metadata against configurable benchmark criteria."
    )
    parser.add_argument("candidate", help="Path to candidate JSON")
    parser.add_argument("--rules", default="rules.json", help="Path to rules JSON")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    report = evaluate_candidate(load_json(args.candidate), load_json(args.rules))
    rendered = json.dumps(report, indent=2)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
