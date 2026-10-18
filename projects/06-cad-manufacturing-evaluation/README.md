# CAD Manufacturing Evaluation Benchmark

A Python-based portfolio benchmark for reviewing CAD/manufacturing candidate metadata against configurable engineering-evaluation criteria.

## Project focus

The project combines **CAD review, manufacturing reasoning, structured evaluation criteria, and Python-based automation**. It evaluates sheet-metal candidate metadata and produces deterministic PASS/FAIL results with a structured report.

Current checks include:

- material thickness range;
- bend-radius-to-thickness relationship;
- minimum web width;
- hole-to-edge distance;
- drawing metadata completeness;
- BOM completeness.

## Engineering scope

The thresholds in `rules.json` are configurable benchmark criteria for this portfolio exercise. They are not universal DFM rules, supplier standards, code requirements, or production-release limits. Real manufacturing decisions must account for material, process, supplier capability, tooling, tolerances, loading, and applicable standards.

## Project structure

```text
06-cad-manufacturing-evaluation/
├── README.md
├── PROVENANCE.md
├── evaluator.py
├── rules.json
├── examples/
│   ├── pass_bracket.json
│   └── fail_bracket.json
└── tests/
    └── test_evaluator.py
```

## Example usage

```bash
python evaluator.py examples/pass_bracket.json --rules rules.json
python evaluator.py examples/fail_bracket.json --rules rules.json
python -m unittest discover -s tests -v
```

To save a report:

```bash
python evaluator.py examples/pass_bracket.json --rules rules.json --output report.json
```

## Expected behavior

- `examples/pass_bracket.json` returns `PASS`.
- `examples/fail_bracket.json` returns `FAIL`.
- Removing mandatory drawing metadata from the pass case produces a failure.

## Capability areas represented

- CAD/manufacturing review logic;
- DFM-oriented reasoning;
- machine-readable evaluation criteria;
- Python scripting for engineering workflows;
- JSON input/output;
- deterministic scoring and PASS/FAIL reporting;
- basic regression testing;
- engineering documentation and scope control.

## Development and personal validation

The implementation used AI-assisted development. Amr personally reviewed the engineering criteria and Python logic, executed the provided examples and regression tests, modified the project, verified expected outputs, and validated the documented engineering limitations.

Accordingly, this project is evidence of a **personally validated AI-assisted engineering development workflow** involving Python, CAD/manufacturing evaluation logic, structured rules, testing, and engineering judgment. It should not be described as unaided end-to-end software authorship or as evidence of advanced professional Python development.

See `PROVENANCE.md` for the claim boundaries.
