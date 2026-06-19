---
name: qgis-geoai-studio
description: >-
  Professional QGIS-integrated GeoAI Studio for natural-language geospatial remote sensing
  data processing, analysis, and SCI paper figure generation. Use when users request:
  (1) QGIS-based vector/raster spatial analysis and data management,
  (2) Remote sensing index computation and time series analysis,
  (3) Land cover classification using ML/DL algorithms,
  (4) Change detection and spatial pattern (hotspot/LISA) analysis,
  (5) SCI journal publication-ready Figure 1-8 generation,
  (6) Graphical abstract, TOC figure, and academic poster creation,
  (7) Automatic figure adaptation to journal requirements,
  (8) Paper submission support with journal recommendation and acceptance prediction,
  (9) Research report generation,
  (10) Complete workflow pipelines for geospatial analysis.
---

# QGIS GeoAI Studio

QGIS GeoAI Studio is a comprehensive remote sensing spatial data processing
and SCI paper figure generation system that integrates QGIS with Python geospatial libraries.


## QGIS Environment (Detected)

Your QGIS 3.44.2 is installed at **D:\QGIS** via OSGeo4W.

**Detected configuration:**
- QGIS version: 3.44.2 Solothurn
- Python: 3.12.11
- GDAL: 3.11.3
- GRASS: 8.4.1 (307 algorithms)
- Processing: 747 total algorithms (321 Native, 57 GDAL, 307 GRASS, 44 QGIS, 17 PDAL)

### Using QGIS Python (Recommended)

Run scripts using QGIS\'s bundled Python interpreter:

```powershell
$env:PYTHONHOME = "D:\QGIS\apps\Python312"
$env:PYTHONPATH = "D:\QGIS\apps\qgis\python"
$env:PATH = "D:\QGIS\bin;D:\QGIS\apps\qgis\bin;D:\QGIS\apps\Python312;$env:PATH"
& "D:\QGIS\bin\python.exe" your_script.py
```

### Initialize PyQGIS in Scripts

```python
import sys
sys.path.insert(0, r"D:\QGIS\apps\qgis\python")
sys.path.insert(0, r"D:\QGIS\apps\qgis\python\plugins")

from qgis.core import QgsApplication
from processing.core.Processing import Processing
import processing

QgsApplication.setPrefixPath(r"D:\QGIS\apps\qgis", True)
qgs = QgsApplication([], False)
qgs.initQgis()
Processing.initialize()

# Now all 747 algorithms are available
result = processing.run("native:buffer", {
    "INPUT": layer, "DISTANCE": 100, "OUTPUT": "output.shp"
})
qgs.exitQgis()
```

### Running a QGIS Algorithm

```python
from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY
import processing

# Create memory layer
layer = QgsVectorLayer("Point?crs=EPSG:4326", "pts", "memory")
dp = layer.dataProvider()
f = QgsFeature()
f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(114.3, 30.6)))
dp.addFeatures([f])

# Run buffer
result = processing.run("native:buffer", {
    "INPUT": layer, "DISTANCE": 0.1, "SEGMENTS": 5,
    "DISSOLVE": False, "OUTPUT": "buffer.gpkg"
})
print("Buffer: OK")
```

## Quick Start

User says: "Analyze urban expansion in Wuhan 2010-2025 and generate SCI figures"

```python
from geoai_data_manager import DataManager
from geoai_remote_sensing import RemoteSensing
from geoai_vector_analysis import VectorAnalysis
from geoai_sci_figure import SCIFigures
from geoai_paper_agent import PaperSubmissionAgent

dm = DataManager("wuhan_urban")
rs = RemoteSensing()
va = VectorAnalysis()
sf = SCIFigures(journal="Remote_Sensing")
agent = PaperSubmissionAgent()

# Generate all 8 figures
sf.figure1_study_area(sat_img, boundary)
sf.figure2_land_cover([lc2010, lc2020], ["2010", "2020"])
sf.figure3_accuracy(cm, class_names, {"OA": 0.92, "Kappa": 0.89})
sf.figure4_change_detection(change_map, transition_matrix)
sf.figure5_spatial_pattern(hotspot_map, lisa_map)
sf.figure6_driver_analysis(importance, feat_names)
sf.figure7_uncertainty(uncertainty_map)
sf.figure8_framework(["Data", "Classify", "Analyze", "Map"])
sf.graphical_abstract(["Data", "Method", "Result"], result_img)
```

## Part 1: Basic Capabilities

### Data Management (DataManager)

Support: Shapefile, GeoJSON, GPKG, KML, KMZ, CSV, XLSX, GeoTIFF, NetCDF, HDF, LAS/LAZ

```python
dm = DataManager("workspace")

# Scan directory for all geospatial data
found = dm.scan_directory()

# Read data
gdf = dm.read_vector("data.shp")
data, meta = dm.read_raster("image.tif")
gdf_csv = dm.read_csv_as_gdf("points.csv", x_col="lon", y_col="lat")

# Write data
dm.write_vector(gdf, "output.gpkg")

# Data quality check
report = dm.data_quality_report(gdf)
print(report["quality_issues"])

# CRS operations
reprojected = dm.reproject(gdf, "EPSG:32650")
clipped = dm.clip_by_extent(gdf, 114, 30, 115, 31)
merged = dm.merge_layers(["layer1", "layer2"])

# Raster metadata
info = dm.raster_info("landsat.tif")
```

### Vector Analysis (VectorAnalysis)

Full native spatial analysis tools:

```python
va = VectorAnalysis()

# Buffer
buf = va.buffer(gdf, 100, dissolve=True)

# Overlay operations
clip = va.clip(target, clip_layer)
inter = va.intersection(a, b)
union = va.union(a, b)
erase = va.erase(target, erase_layer)
sym_diff = va.symmetrical_difference(a, b)

# Spatial operations
dissolved = va.dissolve(gdf, by="class")
joined = va.spatial_join(target, join_layer)
selected = va.select_by_location(target, select_layer)

# Advanced analysis
kde, transform, crs = va.kernel_density(pts)
voronoi = va.voronoi(pts)
delaunay = va.delaunay_triangulation(pts)
nearest = va.nearest_neighbor_analysis(gdf, k=5)

# Spatial statistics (requires esda, libpysal)
hotspots = va.hotspot_analysis_getis_ord(gdf, "value")
mi = va.morans_i(gdf, "value")
lisa = va.lisa(gdf, "value")

# Network analysis
path = va.shortest_path(network, src, dst)
service = va.service_area(network, src, max_dist=1000)
centrality = va.centrality_analysis(gdf)
```

### Raster Analysis (RasterAnalysis)

```python
ra = RasterAnalysis()
data, meta = ra.read("dem.tif")

# Terrain
slope = ra.slope(data[0], cellsize=30)
aspect = ra.aspect(data[0], cellsize=30)
hillshade = ra.hillshade(data[0], cellsize=30)
curvature = ra.curvature(data[0], cellsize=30)
tpi = ra.tpi(data[0], cellsize=30)
tri = ra.tri(data[0], cellsize=30)
roughness = ra.terrain_roughness(data[0], cellsize=30)

# Focal/Zonal
smoothed = ra.focal_stats(data[0], size=5, stat="mean")
zonal = ra.zonal_stats(data[0], zones, ["mean","std","sum"])

# Resample/Mosaic/Reclassify
resampled, new_meta = ra.resample(data, meta, target_res=[10,10])
mosaic_data, m_meta = ra.mosaic([file1, file2])
reclass = ra.reclassify(data[0], [0,0.2,0.5,1], [1,2,3])

# Interpolation
grid = ra.idw_interpolation(points, values, (100,100))
```


## Part 2: Environment Awareness System

### Auto Environment Detection

```python
from geoai_env_setup import generate_env_report
report = generate_env_report()
if report["qgis"]:
    for q in report["qgis"]:
        v = q.get("version","?")
        print(f"QGIS {v} at {q['path']}")
for pkg, ver in report["python_packages"].items():
    s = f"v{ver}" if ver else "missing"
    print(f"  {pkg}: {s}")
```

### QGIS Bootstrap

```python
from geoai_qgis_bootstrap import init_qgis
qgs = init_qgis()
```

### Data Discovery and Quality

```python
from geoai_data_manager import DataManager
dm = DataManager("project")
found = dm.scan_directory("./data")
gdf = dm.read_vector("data.shp")
quality = dm.data_quality_report(gdf)
if quality["quality_issues"]["empty_geometries"]:
    print("WARNING: Empty geometries found")
if quality["crs"] == "Not set":
    print("WARNING: CRS missing")
```


## Part 3: Remote Sensing Research Capabilities

### Spectral Indices (60+)

Vegetation: NDVI, EVI, EVI2, SAVI, OSAVI, MSAVI2, ARVI, GCVI, NDRE, CVI, RVI, DVI
Water: NDWI, MNDWI, AWEI_sh, AWEI_nsh, WRI
Built-up: NDBI, BUI, IBI
Burn: NBR, dNBR, BAI
Moisture: NDMI, MSI
Snow: NDSI
Soil: BI, CI

```python
rs = RemoteSensing()

# Define bands
bands = {"B": blue, "G": green, "R": red, "N": nir,
         "S1": swir1, "S2": swir2, "RE1": rededge1}

# Single index
ndvi = rs.compute_index(bands, "NDVI")

# Multiple indices
all_idx = rs.compute_multiple_indices(bands,
    ["NDVI", "EVI", "SAVI", "MNDWI", "NDBI", "NBR"])

# All indices
all = rs.compute_all_indices(bands)
```

### Classification Algorithms

Supported: Random Forest, SVM, CART, XGBoost, LightGBM, GBDT, CatBoost, KNN

```python
# Train
metrics = rs.train(X, y, algorithm="rf",
    n_estimators=200, max_depth=15)
print(f"OA={metrics[accuracy]:.3f}, Kappa={metrics[kappa]:.3f}")

# Cross-validation
cv = rs.cross_validate(X, y, algorithm="rf", cv=10)

# Apply to raster
classified = rs.classify_raster(raster_data, "rf")

# Feature importance
imp = rs.feature_importance("rf")
```

### Time Series Analysis

```python
# Mann-Kendall trend test
mk = rs.mann_kendall_test(ndvi_series)
print(f"Trend: {mk[trend]}, p={mk[p_value]:.4f}")

# Sen slope estimator
slope = rs.sen_slope(ndvi_series)

# Theil-Sen robust regression
ts = rs.theil_sen_regression(years, values)

# Breakpoint detection
bp = rs.breakpoint_detection(values)
```

### Change Detection

```python
# Image difference
diff = rs.image_difference(img1, img2)

# Change Vector Analysis
mag, angle = rs.change_vector_analysis(bands1, bands2)

# Post-classification comparison
change_map, stats = rs.post_classification_comparison(c1, c2)
print(f"Change: {stats[change_percentage]:.1f}%")
```

## Part 4: SCI Paper Figure Factory

### Figure Types

| Figure | Description | Method |
|--------|-------------|--------|
| Figure 1 | Study Area | `figure1_study_area()` |
| Figure 2 | Land Cover | `figure2_land_cover()` |
| Figure 3 | Accuracy Assessment | `figure3_accuracy()` |
| Figure 4 | Change Detection | `figure4_change_detection()` |
| Figure 5 | Spatial Pattern | `figure5_spatial_pattern()` |
| Figure 6 | Driver Analysis | `figure6_driver_analysis()` |
| Figure 7 | Uncertainty Analysis | `figure7_uncertainty()` |
| Figure 8 | Framework | `figure8_framework()` |
| - | Graphical Abstract | `graphical_abstract()` |
| - | TOC Figure | `toc_figure()` |
| - | Academic Poster | `academic_poster()` |

### Journal-Specific Adaptation

```python
sf = SCIFigures(journal="Remote_Sensing")  # MDPI format
sf_nature = SCIFigures(journal="Nature")    # Nature format
sf_science = SCIFigures(journal="Science")  # Science format
sf_rse = SCIFigures(journal="RSE")          # RSE format
sf_elsevier = SCIFigures(journal="ISPRS_JPRS")  # Elsevier
```

Adaptation includes: page width, font, font size, color palette, line width, DPI

## Part 5: Auto Journal Adaptation

Supported journals:
- Remote Sensing (MDPI) - 17.2cm, Arial 8pt
- Nature - 8.9cm single-column, Arial 7pt
- Science - 5.7cm single-column, Arial 7pt
- ISPRS JPRS (Elsevier) - 19.0cm, Arial 8pt
- IJAEOG/JAG (Elsevier) - 18.0cm, Arial 8pt
- RSE (Elsevier) - 21.0cm, Arial 8pt
- Ecological Indicators (Elsevier) - 21.0cm, Arial 8pt
- IEEE TGRS - Arial 8pt

Auto-optimized: fonts, color schemes, legends, layout, line widths, output dimensions

## Part 6: Paper Submission Agent

```python
agent = PaperSubmissionAgent()

# Journal recommendation
recs = agent.recommend(topic="urban expansion", target_if=5.0)
for tier, js in recs.items():
    for j in js:
        print(f"  [{tier}] {j[name]} (IF={j[if]})")

# Acceptance prediction
pred = agent.predict("Remote_Sensing", novelty=7, methods=8, scope=9)
print(f"Accept: {pred[accept_prob]}%")

# Cover letter
letter = agent.cover_letter("Title", ["Author A"], "RS", "significance")
```

## Part 7: Workflow Engine

```python
pipeline = GeoAIPipeline(workspace=".")

# Urban expansion
pipeline.urban_expansion_workflow("Wuhan", [2010,2015,2020,2025])

# Forest disturbance
pipeline.forest_disturbance_workflow("Amazon", [2000,2025])

# Carbon stock
pipeline.carbon_stock_workflow("Region", 2020)

# Water monitoring
pipeline.water_monitoring_workflow("Poyang Lake", ["2023-01","2023-07"])

# Eco-quality (RSEI)
pipeline.eco_quality_workflow("Region", 2023)

# LULC change
pipeline.lulc_change_workflow("Region", [2010,2020])
```

## Part 8: Research Report Generator

### Free Features (All Open)

```python
report = ResearchReport(output_dir="report")

sections = [
    report.generate_title("Title", "Authors", "Affiliation"),
    report.section_introduction("Background", "Gap", "Objectives"),
    report.section_study_area("Location", "Extent", "Climate", "Sources"),
    report.section_data("Table", "Preprocessing"),
    report.section_methods("Methods", "Workflow"),
    report.section_results("Results", "Findings"),
    report.section_discussion("Discussion", "Limits"),
    report.section_conclusion("Conclusion"),
]
full = report.build_report(sections)

# Export formats
report.save_markdown(full, "paper.md")
report.save_word(full, "paper.docx")

# SCI framework
sci_sections = report.sci_framework("Title")

# Thesis framework
master = report.thesis_framework("master")
phd = report.thesis_framework("phd")
```

### Paid Feature: Research Report Generator

Price: 9.9 yuan (one-time, lifetime use)
When user requests "generate complete research report",
prompt that this is a premium feature.

Includes: Full research report, SCI framework, grant report,
thesis framework, Word/PDF export.

All other features are permanently free.
