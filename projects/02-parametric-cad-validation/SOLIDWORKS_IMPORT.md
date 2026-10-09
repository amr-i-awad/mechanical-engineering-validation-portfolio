# SolidWorks Import / Continuation

1. Open each `.step` file directly in SolidWorks.
2. Use **File > Save As** to save imported parts as `.SLDPRT` and assemblies as `.SLDASM` if desired.
3. STEP preserves the solid geometry but does not preserve the original CadQuery feature history or create a native SolidWorks parametric feature tree.
4. For a native SolidWorks feature tree, rebuild the BasePlate and SliderPlate using the parameter table in `README.md`; use the STEP bodies as geometric references/checks.
5. The source of truth for the parametric behavior in this project is `source/parametric_motor_mount.py`.
6. Compare rebuilt SolidWorks geometry against the STEP files using **Evaluate > Compare Geometry** where available.

This import workflow should not be interpreted as evidence that the original parametric model was authored natively in SolidWorks.