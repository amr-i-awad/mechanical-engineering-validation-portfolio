# Automated Engineering Evaluation Harness

A deterministic Python pipeline that evaluates validation outputs from the CAD, static-FEA, and thermal benchmarks.

![Baseline score](outputs/Baseline/score_summary.png)

## Ownership Note

This artifact was developed **with external assistance**.

It is retained as a supporting portfolio artifact because it demonstrates a structured validation workflow, reproducible acceptance criteria, reporting, and failure-case handling. It should **not** be used by itself as evidence that Amr independently designed and implemented the complete Python evaluation infrastructure.

The Parametric CAD Validation Benchmark is a separate project and was personally authored by Amr.

## What It Does

- Reads CAD, structural, and thermal validation JSON files.
- Applies configurable acceptance rules and domain weights.
- Produces domain scores, an overall score, and PASS/FAIL status.
- Writes machine-readable JSON, compact CSV, and a Markdown engineering report.
- Stores SHA-256 fingerprints of the inputs and rule configuration.
- Includes intentionally corrupted inputs and unit tests for repeatability.

## Included Results

- **Baseline:** 99.3/100 — PASS
- **Failure cases:** 44.818/100 — FAIL

These scores are outputs from this portfolio evaluation configuration. They are not standardized engineering qualification or certification scores.

## Run

```bash
python source/evaluation_harness.py \
  --cad inputs/Baseline/cad_validation.json \
  --static inputs/Baseline/static_validation.json \
  --thermal inputs/Baseline/thermal_validation.json \
  --rules config/evaluation_rules.json \
  --outdir outputs/Baseline
```

## Test

```bash
python -m unittest discover tests -v
```

## Portfolio Role

The goal of this artifact is not to replace engineering judgment. Its value in the portfolio is as supporting evidence of **validation methodology, explicit criteria, reproducibility, cross-project organization, and auditable reporting**.

Any claim about Amr's personal Python-development capability should be supported by work for which his individual authorship is independently established, rather than inferred from this assisted artifact alone.