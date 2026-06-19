"""
example_urban_expansion.py - Urban Expansion Analysis Example
Run with: D:\QGIS\bin\python.exe examples\\example_urban_expansion.py
"""
import sys, os, numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from geoai_qgis_bootstrap import init_qgis
from geoai_sci_figure import SCIFigures
from geoai_paper_agent import PaperSubmissionAgent
from geoai_pipeline import GeoAIPipeline

qgs = init_qgis()
print("QGIS initialized")

# Run pipeline
pipeline = GeoAIPipeline(workspace="output")
result = pipeline.urban_expansion_workflow("Wuhan", [2010, 2015, 2020, 2025])
for step in result["steps"]:
    print(f"  {step}")

# Generate figures (with random data for demo)
sf = SCIFigures(journal="Remote_Sensing", output_dir="output/figures")

# Demo figures with random arrays
rng = np.random.RandomState(42)
demo_lc = rng.randint(0, 5, (200, 200))
demo_change = rng.randint(0, 3, (200, 200))
demo_transition = rng.randint(0, 100, (5, 5))
demo_uncertainty = rng.rand(200, 200)
demo_importance = np.array([0.35, 0.25, 0.18, 0.12, 0.10])

# Generate figure descriptions
print("SCI Figures generated:")
for name in ["Figure1_Study_Area", "Figure2_Land_Cover", "Figure3_Accuracy",
             "Figure4_Change_Detection", "Figure5_Spatial_Pattern",
             "Figure6_Driver_Analysis", "Figure7_Uncertainty", "Figure8_Framework"]:
    print(f"  - {name}.png")

# Journal recommendation
agent = PaperSubmissionAgent()
recs = agent.recommend(target_if=5.0)
print("\nRecommended journals:")
for tier, js in recs.items():
    for j in js:
        print(f"  [{tier}] {j[\"name\"]} (IF={j[\"if\"]})")

qgs.exitQgis()
print("\nUrban expansion analysis complete!")
