# Provenance and Claim Boundaries

## Development provenance

This project was scaffolded with AI assistance to create a focused practice exercise around CAD/manufacturing evaluation and Python-based engineering workflows.

The current repository artifact should not be described as independently authored end-to-end Python software by Amr unless he personally completes and can defend the implementation.

## Minimum personal-validation gate before CV use

Before this project is promoted to CV/portfolio evidence, Amr should personally:

1. Run both provided examples and the unit-test suite.
2. Explain what every benchmark check does and why it passes or fails.
3. Review every threshold in `rules.json` and confirm that it is a configurable benchmark criterion, not a universal manufacturing rule.
4. Change at least one benchmark rule or weight intentionally and predict the output before running it.
5. Add at least one new candidate example of his own and explain the expected result.
6. Make at least one meaningful code or documentation change himself and record the reason.
7. Be able to explain the limitations of metadata-only evaluation versus inspection of actual CAD geometry, drawings, tolerances, materials, tooling, and supplier/process constraints.

## Safe claims after the validation gate

If the steps above are completed and documented, safe wording may include:

- "Built and validated a Python-based CAD/manufacturing evaluation benchmark with configurable engineering criteria and regression tests, using AI-assisted development." 
- "Used Python to automate structured PASS/FAIL evaluation of CAD/manufacturing metadata and documented rule limitations."
- "Worked with an AI coding assistant while personally reviewing engineering criteria, tests, outputs, and limitations."

## Claims to avoid without stronger evidence

Do not claim:

- advanced Python expertise;
- professional software-engineering ownership;
- production-ready DFM automation;
- automated validation of real CAD geometry unless geometry parsing is actually implemented and verified;
- CAM/CNC process expertise solely from this project;
- universal manufacturing-rule compliance;
- independent authorship of AI-generated code without disclosure.
