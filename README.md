# Amr Awad — Mechanical Engineering Portfolio

Mechanical Engineering graduate portfolio focused on **mechanical design, parametric CAD, FEA validation, thermal analysis, and engineering documentation**.

This portfolio emphasizes a practical engineering principle: **CAD and simulation results should be checked against calculations, constraints, convergence behavior, or other independent evidence whenever possible.**

[LinkedIn](https://www.linkedin.com/in/amr-awad-16b2a7278/) · Email: amrawad0595@gmail.com · [Portfolio document status](docs/README.md)

## Featured Projects

### 1. Compact Scissor Lift — Mechanical Design Study

![Scissor lift](assets/scissor_lift.png)

A self-initiated virtual mechanical-design project developed from requirements through CAD, kinematic and analytical calculations, lead-screw concept sizing, BOM, manufacturing profiles, drawings, and concept-stage risk review.

**Design target:** 10 kg centered payload.

**Evidence includes:** CAD assembly and component models, kinematic and analytical load calculations, lead-screw force/torque/self-locking review, BOM, DXF manufacturing profiles, concept manufacturing drawings, validation plots, and a prototype test plan.

**Validation status:** This is a virtual design study. A physical prototype, proof-load testing, endurance testing, local FEA, and safety certification were not completed. It must not be interpreted as a manufactured or certified lifting device and is not intended for lifting people.

[Open project →](projects/05-compact-scissor-lift/)

### 2. Static FEA Ground-Truth Benchmark

![Static FEA](assets/static_fea.png)

A structural benchmark comparing a transparent numerical finite-element model with closed-form cantilever-beam calculations, including mesh convergence and equilibrium checks.

**Important:** the documented **0.52% tip-deflection error and approximately 0.33% sampled bending-stress error belong to the numerical Q4 benchmark**. They should not be described as ANSYS result errors unless corresponding ANSYS result artifacts are available.

Amr has separately performed hands-on Static Structural FEA work in ANSYS involving model setup, material definition, loads/supports, meshing, stress/deformation review, and analytical/convergence reasoning.

[Open project →](projects/03-static-fea-ground-truth/)

### 3. Parametric CAD Validation Benchmark — CadQuery / STEP

![Parametric CAD assembly](assets/parametric_cad.png)

A personally authored parametric adjustable motor-mount benchmark created to investigate **configuration robustness, mechanical clearances, travel constraints, geometry validity, and deterministic CAD validation**.

The project includes parametric CadQuery source, Compact/Standard/Extended configurations, STEP geometry, DXF profiles, validation CSV/JSON, multiple slider travel states, and intentionally invalid parameter cases.

STEP files can be opened in SolidWorks, but they do not preserve a native SolidWorks feature tree. The project therefore should not be described as native SolidWorks parametric modeling.

[Open project →](projects/02-parametric-cad-validation/)

### 4. Thermal FEA Ground-Truth Benchmark

![Thermal validation](assets/thermal_validation.png)

A thermal benchmark comparing a transparent numerical finite-element model with a closed-form analytical fin solution and energy-balance checks.

The documented numerical benchmark reports **0.0012% tip-temperature error** and **0.0015% heat-flow error**.

**Important:** these accuracy values belong to the documented numerical benchmark. They should not be presented as ANSYS result errors unless corresponding ANSYS result artifacts establish that connection.

Amr's hands-on Thermal FEA experience in ANSYS is separate from these benchmark-specific numerical values.

[Open project →](projects/04-thermal-fea-ground-truth/)

## Supporting Engineering Artifact

### Automated Engineering Evaluation Harness

![Evaluation score](assets/evaluation_score.png)

A deterministic Python-based evaluation pipeline that consumes validation outputs from the CAD, static-FEA, and thermal benchmarks and produces configurable PASS/FAIL decisions and structured reports.

**Ownership note:** This artifact was developed **with external assistance**. It is retained as supporting context for the validation portfolio, but it should not be used by itself as evidence that Amr independently designed and implemented the complete Python evaluation infrastructure.

The Parametric CAD Validation Benchmark is separate and was personally authored by Amr.

[Open supporting artifact →](projects/01-engineering-evaluation-harness/)

## Technical Evidence Areas

- **Mechanical design:** kinematics, analytical loading, lead-screw concept sizing, mechanical component reasoning, BOM preparation, engineering drawings, and concept-stage risk review
- **CAD:** SolidWorks 3D modeling, parametric CadQuery modeling, assemblies, STEP workflows, DXF profiles, configuration and clearance reasoning, and AutoCAD 2D
- **Engineering analysis:** Static Structural FEA, Thermal FEA, mesh-convergence reasoning, analytical comparison, equilibrium checks, and energy-balance checks
- **Engineering documentation:** calculations, BOMs, CAD deliverables, drawings, validation outputs, design limitations, and reproducible project organization

## Repository Map

```text
projects/
  01-engineering-evaluation-harness/
  02-parametric-cad-validation/
  03-static-fea-ground-truth/
  04-thermal-fea-ground-truth/
  05-compact-scissor-lift/
assets/
docs/
```

## Evidence and Ownership Policy

Projects in this portfolio distinguish between:

- **Designed** — original engineering design decisions made by Amr.
- **Modeled / Re-modeled** — CAD geometry created by Amr, including work based on an existing reference.
- **Calculated** — engineering calculations personally performed.
- **Simulated** — analysis personally executed using simulation software.
- **Numerically validated** — numerical or simulation results compared with analytical or independent numerical references.
- **Physically tested** — used only when actual physical-testing evidence exists.
- **Manufactured** — used only when hardware was actually fabricated.

Virtual projects are not described as manufactured, physically tested, certified, or production-ready without corresponding evidence.