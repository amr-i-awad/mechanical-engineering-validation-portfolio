# Static FEA Ground-Truth Benchmark

A reproducible static-structural validation benchmark comparing a transparent numerical finite-element model with closed-form cantilever-beam calculations.

![Deformed shape](renders/FEA_Deformed_Shape.png)

## Problem

- Length: 250 mm
- Height: 30 mm
- Thickness: 10 mm
- Structural steel: E = 210 GPa, ν = 0.30
- Fixed left edge
- 600 N downward end load
- 2D plane-stress Q4 finite elements

## Analytical Reference

- Root bending stress: **100.000 MPa**
- Tip deflection: **0.661376 mm**
- Nominal yield factor of safety: **2.500**

## Numerical Benchmark Results

- Fine-mesh tip deflection: **0.664841 mm** → **0.52% error** relative to the analytical value
- Matching-section bending-stress error: approximately **0.33%**
- Vertical reaction equilibrium: approximately exact
- Reaction-moment equilibrium: approximately exact

The repository includes the transparent numerical solver, analytical calculation, convergence data, raw fine-mesh results, validation outputs, and an ANSYS replication guide.

## ANSYS Work

Amr has separately performed hands-on Static Structural FEA work in ANSYS for this type of benchmark, including:

- model/geometry setup
- material definition
- loads and supports
- boundary-condition setup
- meshing
- stress and deformation review
- mesh-convergence and analytical-validation reasoning

## Result Provenance

The documented **0.52% tip-deflection error** and approximately **0.33% sampled bending-stress error** are results from the transparent numerical Q4 benchmark contained in this project.

They are **not presented as ANSYS result errors**. The ANSYS replication material documents how the benchmark can be reproduced in ANSYS, while Amr's hands-on ANSYS experience is stated separately from the benchmark-specific numerical values.

## Scope

This project is a portfolio validation benchmark. It is not a certified production structural analysis, physical test, or safety approval.