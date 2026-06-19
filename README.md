# QGIS GeoAI Studio

[![QGIS](https://img.shields.io/badge/QGIS-3.44-green)](https://qgis.org)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**QGIS GeoAI Studio** is a comprehensive geospatial remote sensing data processing and SCI paper figure generation system. It integrates QGIS processing capabilities with Python geospatial libraries to enable natural-language-driven spatial analysis and publication-ready figure creation.

---

## Features

### Part 1: Geospatial Data Management & Analysis
- **Data Management**: Shapefile, GeoJSON, GPKG, KML, KMZ, CSV, XLSX, GeoTIFF, NetCDF, HDF, LAS/LAZ
- **Vector Analysis**: Buffer, Clip, Union, Intersect, Dissolve, Spatial Join, Voronoi, Delaunay, Network Analysis
- **Raster Analysis**: Terrain (slope/aspect/hillshade), Focal/Zonal statistics, Resampling, Mosaic, Interpolation
- **Spatial Statistics**: Getis-Ord Gi* Hotspot, Moran's I, LISA Cluster Analysis, Kernel Density

### Part 2: Environment Awareness
- Auto-detect QGIS version, GDAL, GRASS, SAGA, Python packages
- Scan and discover local geospatial data
- Data quality checks (missing values, duplicates, topology errors)

### Part 3: Remote Sensing Research
- **60+ Spectral Indices**: NDVI, EVI, SAVI, NDWI, MNDWI, NDBI, NBR, BAI and more
- **8 Classification Algorithms**: Random Forest, SVM, XGBoost, LightGBM, CatBoost, KNN, CART, GBDT
- **Time Series**: Mann-Kendall, Sen's Slope, Theil-Sen, Breakpoint Detection
- **Change Detection**: Image Difference, CVA, Post-Classification Comparison

### Part 4: SCI Paper Figure Factory
Generate publication-ready figures:

| Figure | Description | Specification |
|--------|-------------|---------------|
| Figure 1 | Study Area Map | Location insets, scale bar, north arrow |
| Figure 2 | Land Cover | Multi-temporal comparison |
| Figure 3 | Accuracy Assessment | Confusion matrix + metrics |
| Figure 4 | Change Detection | Change map + transition matrix |
| Figure 5 | Spatial Pattern | Hotspot + LISA + Moran scatter |
| Figure 6 | Driver Analysis | Variable importance |
| Figure 7 | Uncertainty Analysis | Prediction uncertainty |
| Figure 8 | Methodology Framework | Workflow diagram |
| GA | Graphical Abstract | Workflow + key result (1296x765) |
| TOC | Table of Contents | Mini thumbnail |

### Part 5: Auto Journal Adaptation
Automatically adapt figures to journal requirements:

| Journal | Width | Font |
|---------|-------|------|
| Nature | 8.9/18.3 cm | Arial 7pt |
| Science | 5.7/17.8 cm | Arial 7pt |
| Remote Sensing (MDPI) | 17.2 cm | Arial 8pt |
| ISPRS JPRS (Elsevier) | 19.0 cm | Arial 8pt |
| IJAEOG / JAG | 18.0 cm | Arial 8pt |
| RSE | 21.0 cm | Arial 8pt |
| Ecological Indicators | 21.0 cm | Arial 8pt |

### Part 6: Paper Submission Agent
- **Journal Recommendation**: Aspiration / Medium / Safe tiers
- **Acceptance Prediction**: Based on novelty, methods, scope match
- **Cover Letter Generation**: Auto-generated submission letters
- **Reviewer Response**: Structured response templates

### Part 7: Workflow Pipelines
- Urban Expansion Analysis
- Forest Disturbance Monitoring
- Carbon Stock Estimation
- Water Body Monitoring
- Ecological Quality (RSEI) Assessment
- Land Use/Land Cover Change

### Part 8: Research Report Generator
- Complete scientific reports (markdown / Word)
- SCI paper frameworks (Introduction-Discussion)
- Thesis frameworks (Master / PhD)
- Export to Markdown, Word, LaTeX

---

## Quick Start

### 1. With QGIS Python (Recommended)

```powershell
# Set up QGIS environment
set PYTHONHOME=D:\QGIS\apps\Python312
set PYTHONPATH=D:\QGIS\apps\qgis\python
set PATH=D:\QGIS\bin;D:\QGIS\apps\qgis\bin;%PATH%

# Run the studio
D:\QGIS\bin\python.exe scripts\\geoai.py env
```

### 2. With Conda / System Python

```bash
# Install dependencies
pip install geopandas rasterio shapely matplotlib scikit-learn scipy numpy pandas

# Check environment
python scripts/geoai.py env
```

### 3. With QGIS Bootstrap

```python
from scripts.geoai_qgis_bootstrap import init_qgis
qgs = init_qgis()
# Now use all 747 QGIS processing algorithms
```

### Complete Workflow Example

```python
# 1. Initialize
from scripts.geoai_qgis_bootstrap import init_qgis
qgs = init_qgis()

# 2. Load data
from scripts.geoai_data_manager import DataManager
dm = DataManager("analysis")
gdf = dm.read_vector("study_area.shp")

# 3. Compute indices
from scripts.geoai_remote_sensing import RemoteSensing
rs = RemoteSensing()
ndvi = rs.compute_index({"N": nir, "R": red}, "NDVI")

# 4. Classify
metrics = rs.train(X, y, algorithm="rf")

# 5. Generate figures
from scripts.geoai_sci_figure import SCIFigures
sf = SCIFigures(journal="Remote_Sensing")
sf.figure1_study_area(sat_img, boundary)
sf.figure2_land_cover([lc_2010, lc_2020], ["2010", "2020"])

# 6. Journal recommendation
from scripts.geoai_paper_agent import PaperSubmissionAgent
agent = PaperSubmissionAgent()
recs = agent.recommend(target_if=5.0)

qgs.exitQgis()
```

---

## Project Structure

```
qgis-geoai-studio/
├── SKILL.md                          # Main skill instructions
├── agents/openai.yaml                # UI metadata
├── scripts/
│   ├── geoai.py                      # Unified CLI
│   ├── geoai_data_manager.py         # Data management
│   ├── geoai_vector_analysis.py      # Vector analysis
│   ├── geoai_raster_analysis.py      # Raster analysis
│   ├── geoai_remote_sensing.py       # Remote sensing indices & ML
│   ├── geoai_sci_figure.py           # SCI figure factory
│   ├── geoai_paper_agent.py          # Paper submission agent
│   ├── geoai_report.py               # Research report generator
│   ├── geoai_pipeline.py             # Workflow engine
│   ├── geoai_env_setup.py            # Environment detection
│   ├── geoai_qgis_bootstrap.py       # QGIS bootstrap
│   ├── geoai_gee_bridge.py           # Earth Engine bridge
├── references/
│   ├── qgis_api_cheatsheet.md        # PyQGIS API reference
│   ├── remote_sensing_indices.md     # Spectral indices formulas
│   ├── sci_figure_templates.md       # Figure templates
│   └── journal_requirements.md       # Journal database
├── assets/templates/                 # Figure templates
├── install.bat                       # Windows installer
├── setup.py                          # pip installer
├── LICENSE                           # MIT license
└── .gitignore
```

---

## Requirements

- **QGIS 3.x** (recommended: 3.44+)
- **Python 3.8+** (QGIS bundled Python 3.12 or conda)
- **Packages**: geopandas, rasterio, shapely, matplotlib, scikit-learn, numpy, pandas

Optional:
- Google Earth Engine: `earthengine-api`, `geemap`
- Word export: `python-docx`
- Deep Learning: `tensorflow`, `torch`

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Citation

If you use QGIS GeoAI Studio in your research, please cite:

```bibtex
@software{qgis_geoai_studio,
  title = {QGIS GeoAI Studio},
  version = {1.0.0},
  year = {2026},
  url = {https://github.com/xingguangYan/qgis-geoai-studio}
}
```
