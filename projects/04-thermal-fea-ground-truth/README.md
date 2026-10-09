# Thermal FEA Ground-Truth Benchmark

A thermal-validation study of an aluminum cooling fin, comparing a transparent numerical finite-element model with a closed-form fin solution and an energy-balance check.

![Temperature validation](renders/Temperature_Profile_Validation.png)

## Problem

- Fin: 200 × 30 × 4 mm
- Thermal conductivity: 205 W/m·K
- Base temperature: 100 °C
- Ambient temperature: 25 °C
- Convection coefficient: 15 W/m²·K

## Numerical Benchmark Results

- Analytical tip temperature: **63.0819 °C**
- Numerical FE tip temperature: **63.0815 °C**
- Tip-temperature error: **0.0012%**
- Analytical heat input: **10.23513 W**
- Numerical FE heat input: **10.23529 W**
- Heat-flow error: **0.0015%**
- Energy-balance error: approximately **0%**

The included model is a transparent **1D thermal finite-element benchmark**. The `ansys_replication/` material explains how to reproduce the same physics using the supplied 3D STEP geometry.

## ANSYS Work

Amr has separately performed hands-on Thermal FEA work in ANSYS, including model setup, material and thermal-boundary-condition definition, meshing, and temperature/thermal-result review.

## Result Provenance

The documented **0.0012% tip-temperature error** and **0.0015% heat-flow error** belong to the transparent numerical benchmark contained in this project.

They are **not presented as ANSYS accuracy results**. The ANSYS replication material is a reproduction workflow, while Amr's hands-on ANSYS Thermal FEA experience is stated separately from these benchmark-specific numerical values.

## Scope

This project is a numerical portfolio validation benchmark. It does not represent experimental or physical thermal validation, product qualification, or certification.