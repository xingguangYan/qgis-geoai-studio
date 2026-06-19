# QGIS API Cheatsheet

## QGIS Installation & Setup

### Install QGIS via Conda (Recommended for Codex)
```bash
conda install -c conda-forge qgis
conda install -c conda-forge pyqgis
```

### Standalone Installer
Download from: https://qgis.org/download/
- Windows: OSGeo4W network installer or standalone .exe
- Typical path: `C:\Program Files\QGIS 3.x`

### Verify Installation
```python
import os
# For standalone QGIS on Windows:
os.environ['PATH'] += r';C:\Program Files\QGIS 3.34.11\bin'
os.environ['PATH'] += r';C:\Program Files\QGIS 3.34.11\apps\qgis\bin'
os.environ['PYTHONPATH'] = r'C:\Program Files\QGIS 3.34.11\apps\qgis\python'
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Program Files\QGIS 3.34.11\apps\Qt5\plugins'

from qgis.core import QgsApplication
QgsApplication.setPrefixPath(r'C:\Program Files\QGIS 3.34.11\apps\qgis', True)
qgs = QgsApplication([], False)
qgs.initQgis()
```

## Core PyQGIS Classes

### Data Management
| Class | Purpose |
|-------|---------|
| `QgsVectorLayer` | Vector data layer (Shapefile, GeoJSON, GPKG) |
| `QgsRasterLayer` | Raster data layer (GeoTIFF, NetCDF) |
| `QgsProject` | Manage project layers |
| `QgsMapLayerRegistry` | Legacy layer registry |
| `QgsVectorFileWriter` | Export vector layers |

### Vector Operations
```python
from qgis.core import (QgsVectorLayer, QgsProcessingFeedback,
                       QgsCoordinateReferenceSystem)
from qgis.analysis import QgsNativeAlgorithms
import processing

# Buffer
processing.run("native:buffer", {
    'INPUT': 'input.shp',
    'DISTANCE': 100,
    'SEGMENTS': 5,
    'END_CAP_STYLE': 0,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2,
    'DISSOLVE': False,
    'OUTPUT': 'output.shp'
})

# Clip
processing.run("native:clip", {
    'INPUT': 'input.shp',
    'OVERLAY': 'clip.shp',
    'OUTPUT': 'output.shp'
})

# Union
processing.run("native:union", {
    'INPUT': 'layer_a.shp',
    'OVERLAY': 'layer_b.shp',
    'OUTPUT': 'output.shp'
})

# Intersect
processing.run("native:intersection", {
    'INPUT': 'input.shp',
    'OVERLAY': 'overlay.shp',
    'OUTPUT': 'output.shp'
})

# Dissolve
processing.run("native:dissolve", {
    'INPUT': 'input.shp',
    'FIELD': ['category'],
    'OUTPUT': 'output.shp'
})

# Spatial Join
processing.run("native:joinattributesbylocation", {
    'INPUT': 'target.shp',
    'JOIN': 'join.shp',
    'PREDICATE': [0],  # 0=intersects, 1=contains, 2=equals
    'JOIN_FIELDS': ['field1'],
    'METHOD': 0,  # 0=one-to-one, 1=one-to-many
    'OUTPUT': 'output.shp'
})
```

### Raster Operations (GDAL)
```python
# Clip raster by extent
processing.run("gdal:cliprasterbyextent", {
    'INPUT': 'input.tif',
    'PROJWIN': 'xmin,ymin,xmax,ymax [CRS]',
    'OUTPUT': 'output.tif'
})

# Clip raster by mask layer
processing.run("gdal:cliprasterbymasklayer", {
    'INPUT': 'input.tif',
    'MASK': 'mask.shp',
    'OUTPUT': 'output.tif'
})

# Raster calculator
processing.run("gdal:rastercalculator", {
    'INPUT_A': 'band1.tif',
    'BAND_A': 1,
    'FORMULA': 'A*B',
    'INPUT_B': 'band2.tif',
    'BAND_B': 1,
    'OUTPUT': 'output.tif'
})

# Resampling
processing.run("gdal:warpreproject", {
    'INPUT': 'input.tif',
    'SOURCE_CRS': 'EPSG:4326',
    'TARGET_CRS': 'EPSG:32650',
    'RESAMPLING': 0,  # 0=nearest, 1=bilinear, 2=cubic
    'OUTPUT': 'output.tif'
})
```

### Processing Feedback
```python
class Feedback(QgsProcessingFeedback):
    def __init__(self):
        super().__init__()
    def pushInfo(self, info):
        print(f"[INFO] {info}")
    def reportError(self, error):
        print(f"[ERROR] {error}")
    def setProgress(self, progress):
        print(f"[PROGRESS] {progress:.1f}%")
```

## GRASS GIS Integration
```python
# GRASS raster tools
processing.run("grass7:r.slope.aspect", {
    'elevation': 'dem.tif',
    'slope': 'slope.tif',
    'aspect': 'aspect.tif',
    'format': 0  # degrees
})

processing.run("grass7:r.neighbors", {
    'input': 'input.tif',
    'output': 'output.tif',
    'method': 0,  # 0=average, 1=median, 2=mode
    'neighborhood': 3  # 3x3 window
})
```

## SAGA GIS Integration
```python
processing.run("saga:slopeaspectcurvature", {
    'ELEVATION': 'dem.tif',
    'SLOPE': 'slope.tif',
    'ASPECT': 'aspect.tif',
    'UNIT_SLOPE': 0,  # 0=degrees, 1=radians, 2=percent
    'METHOD': 6  # 6=maximum slope (Horn)
})
```

## WhiteboxTools Integration
```python
processing.run("whitebox:breachdepressions", {
    'dem': 'dem.tif',
    'output': 'filled_dem.tif'
})

processing.run("whitebox:d8pointer", {
    'dem': 'filled_dem.tif',
    'output': 'flow_dir.tif'
})

processing.run("whitebox:d8flowaccumulation", {
    'dem': 'filled_dem.tif',
    'output': 'flow_acc.tif'
})
```

## Map Rendering & Export
```python
from qgis.core import QgsMapSettings, QgsMapRendererParallelJob
from qgis.gui import QgsMapCanvas
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QSize

# Export map to image
def export_map(layers, extent, output_path, dpi=300, width=2100, height=1480):
    settings = QgsMapSettings()
    settings.setLayers(layers)
    settings.setExtent(extent)
    settings.setOutputSize(QSize(width, height))
    settings.setOutputDpi(dpi)

    image = QImage(settings.outputSize(), QImage.Format_ARGB32_Premultiplied)
    image.setDotsPerMeterX(dpi / 0.0254)
    image.setDotsPerMeterY(dpi / 0.0254)

    painter = QPainter(image)
    job = QgsMapRendererParallelJob(settings)
    job.start()
    job.waitForFinished()
    job.renderedImage().save(output_path)
    painter.end()
```

## Common CRS Definitions
```python
# WGS84
crs_wgs84 = QgsCoordinateReferenceSystem('EPSG:4326')
# Web Mercator
crs_web = QgsCoordinateReferenceSystem('EPSG:3857')
# UTM Zones (replace zone number)
crs_utm = QgsCoordinateReferenceSystem('EPSG:32650')  # Zone 50N
# China Geodetic Coordinate System 2000
crs_cgcs = QgsCoordinateReferenceSystem('EPSG:4490')
# Albers Equal Area (China)
crs_albers = QgsCoordinateReferenceSystem('EPSG:102025')
```

## Standalone PyQGIS Complete Setup
```python
import sys, os
from qgis.core import QgsApplication, QgsVectorLayer, QgsProject

def init_qgis(qgis_path=None):
    """Initialize QGIS in standalone mode."""
    if qgis_path is None:
        # Auto-detect common paths
        candidates = [
            r'C:\Program Files\QGIS 3.34.11',
            r'C:\Program Files\QGIS 3.34',
            r'C:\Program Files\QGIS 3.32',
            r'C:\Program Files\QGIS 3.30',
            r'C:\OSGeo4W\apps\qgis',
            r'C:\OSGeo4W64\apps\qgis',
        ]
        for p in candidates:
            if os.path.exists(p):
                qgis_path = p
                break

    prefix = os.path.join(qgis_path, 'apps', 'qgis')
    bin_path = os.path.join(qgis_path, 'bin')
    plugin_path = os.path.join(prefix, 'python', 'plugins')

    os.environ['PATH'] = bin_path + ';' + os.environ.get('PATH', '')
    sys.path.insert(0, os.path.join(prefix, 'python'))
    sys.path.insert(0, plugin_path)

    QgsApplication.setPrefixPath(prefix, True)
    qgs = QgsApplication([], False)
    qgs.initQgis()
    return qgs
```
