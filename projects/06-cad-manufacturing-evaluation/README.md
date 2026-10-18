# CAD Manufacturing Evaluation Benchmark

A small Python-based benchmark for reviewing CAD/manufacturing candidate metadata against configurable engineering-evaluation criteria.

## Why this project exists

The goal is to practice a workflow that combines **CAD review, manufacturing reasoning, structured evaluation criteria, and Python-based automation**. It is intentionally designed as an engineering-evaluation exercise rather than a production-release tool.

The benchmark accepts JSON metadata for a candidate sheet-metal part and evaluates items such as:

- material thickness range;
- bend-radius-to-thickness relationship;
- minimum web width;
- hole-to-edge distance;
- drawing metadata completeness;
- BOM completeness.

The checks are scored and reported as structured PASS/FAIL output.

## Important scope limitation

The numerical criteria in `rules.json` are **configurable portfolio benchmark criteria only**. They are not universal DFM rules, supplier standards, code requirements, or production-release limits. Real manufacturing decisions must be based on the actual material, process, supplier capability, tooling, tolerance stack, loading, and applicable standards.

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

From this project folder:

```bash
python evaluator.py examples/pass_bracket.json --rules rules.json
```

To save a report:

```bash
python evaluator.py examples/pass_bracket.json --rules rules.json --output report.json
```

Run the regression tests with:

```bash
python -m unittest discover -s tests -v
```

## Expected behavior

- `examples/pass_bracket.json` should return `PASS`.
- `examples/fail_bracket.json` should return `FAIL`.
- Removing required drawing metadata from the pass case should cause a failure because drawing completeness is configured as a mandatory check.

## Skills demonstrated when personally reviewed and executed

- structured CAD/manufacturing review logic;
- DFM-oriented reasoning;
- converting evaluation criteria into machine-readable rules;
- Python scripting for engineering workflows;
- JSON input/output;
- deterministic scoring and PASS/FAIL reporting;
- basic regression testing;
- engineering documentation and scope control.

## Current evidence status

This project was scaffolded with AI assistance. It should **not** be used as evidence of independent Python authorship merely because it exists in the repository. Before using it in a CV or interview, Amr should personally run the code, review every benchmark rule, explain the logic, verify the sample outputs, and document any corrections or changes he makes. See `PROVENANCE.md`.
