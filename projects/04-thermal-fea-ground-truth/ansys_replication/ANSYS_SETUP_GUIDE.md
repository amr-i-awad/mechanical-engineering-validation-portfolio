# ANSYS Steady-State Thermal Replication Guide

## Geometry
Import `../cad/Aluminum_Cooling_Fin.step`.

Dimensions:
- 200 mm length
- 30 mm width
- 4 mm thickness

## Material
Use aluminum with thermal conductivity **205 W/m·K**. Density and specific heat are not required for steady-state analysis; values 2700 kg/m³ and 900 J/kg·K may be used if material completeness is desired.

## Boundary Conditions
1. Base face at x = 0: **Temperature = 100 °C**.
2. Four long faces: **Convection h = 15 W/m²·K, ambient = 25 °C**.
3. Tip face at x = 200 mm: **Convection h = 15 W/m²·K, ambient = 25 °C**.
4. Do not apply convection to the fixed-temperature base face.

## Mesh
Run at least three meshes. Suggested global element sizes:
- Coarse: 20 mm
- Medium: 10 mm
- Fine: 5 mm or finer

Because the thickness-based Biot number is very small (0.000146), the analytical model assumes temperature is nearly uniform through each cross-section.

## Results to Request
- Temperature distribution
- Total heat flux
- Directional heat flux in X
- Reaction heat flow at the 100 °C base

## Analytical Targets
- Tip temperature ≈ **63.0819 °C**
- Base heat input ≈ **10.23513 W**

A consistent 3D ANSYS replication should approach the analytical targets as the mesh is refined. Small differences can occur because the analytical model uses a one-dimensional fin assumption.

## Result Provenance

This file is a **replication workflow**, not a record of benchmark-specific ANSYS accuracy results. The documented **0.0012% tip-temperature error** and **0.0015% heat-flow error** in this repository belong to the transparent numerical thermal benchmark, not to an ANSYS result set documented by this guide.