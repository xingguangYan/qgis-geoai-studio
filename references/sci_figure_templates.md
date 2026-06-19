# SCI Figure Templates & Layout Standards

## Common Journal Page Sizes

| Journal | Single Column (mm) | Full Page (mm) | DPI |
|---------|-------------------|----------------|-----|
| Nature | 89 x 246 | 183 x 246 | 300+ |
| Science | 57 x 247 | 178 x 247 | 300+ |
| Remote Sensing | 172 x 254 | 172 x 254 | 300 |
| ISPRS JPRS | 190 x 254 | 190 x 254 | 300 |
| IJAEOG/JAG | 180 x 260 | 180 x 260 | 300 |
| Ecological Indicators | 210 x 280 | 210 x 280 | 300 |
| RSE | 210 x 280 | 210 x 280 | 300 |
| PNAS | 87 x 236 | 183 x 236 | 300 |
| IEEE TGRS | 89 x 241 | 183 x 241 | 300 |

## Standard Figure Types & Specifications

### Figure 1: Study Area
```
Layout: Full page width
Components:
┌─────────────────────────────────────┐
│  (a) National Location              │
│  ┌─────────┐  ┌─────────────────┐  │
│  │ China   │  │ Provincial      │  │
│  │ Inset   │  │ Location        │  │
│  └─────────┘  └─────────────────┘  │
│                                     │
│  (b) Study Area Details             │
│  ┌─────────────────────────────┐   │
│  │ DEM/Imagery + Boundaries    │   │
│  │ Scale Bar + North Arrow     │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
Required: Scale bar, north arrow, legend, graticule,
          data source note, CRS annotation
```

### Figure 2: Land Cover
```
Layout: Full page width, timeline format
┌─────────┐  ┌─────────┐  ┌─────────┐
│ 2010    │  │ 2015    │  │ 2020    │
│ LC Map  │  │ LC Map  │  │ LC Map  │
└─────────┘  └─────────┘  └─────────┘
┌─────────────────────────────────────┐
│ Legend (shared across all maps)     │
└─────────────────────────────────────┘
Required: Unified legend, color consistency,
          area statistics inset
```

### Figure 3: Accuracy Assessment
```
Layout: Half page or column width
Components:
┌─────────────────┐  ┌───────────────┐
│ Confusion Matrix│  │ Accuracy      │
│ (Heatmap)       │  │ Bar Chart     │
└─────────────────┘  └───────────────┘
┌─────────────────────────────────────┐
│ ROC Curve / Kappa Statistics        │
└─────────────────────────────────────┘
Required: Overall accuracy, Kappa, class-wise
          producer/user accuracy
```

### Figure 4: Change Detection
```
Layout: Full page
┌──────────────┐  ┌──────────────────┐
│ Change Map   │  │ Change Matrix    │
│ (Gain/Loss)  │  │ (Sankey/Alluvial)│
└──────────────┘  └──────────────────┘
┌─────────────────────────────────────┐
│ Change Statistics (Stacked Bar)     │
└─────────────────────────────────────┘
```

### Figure 5: Spatial Pattern
```
Layout: Full page or half page
┌─────────────┐  ┌──────────────────┐
│ Hotspot Map │  │ LISA Cluster Map │
│ (Getis-Ord) │  │ (Moran I)        │
└─────────────┘  └──────────────────┘
┌─────────────────────────────────────┐
│ Moran Scatter Plot                  │
└─────────────────────────────────────┘
```

### Figure 6: Driver Analysis
```
Layout: Half page
┌─────────────────────────────────────┐
│ Variable Importance (Bar)           │
├─────────────────────────────────────┤
│ Partial Dependence Plots (2x3 grid) │
├─────────────────────────────────────┤
│ SHAP Summary Plot                   │
└─────────────────────────────────────┘
```

### Figure 7: Uncertainty Analysis
```
Layout: Half page
┌──────────────┐  ┌──────────────────┐
│ Uncertainty  │  │ Confidence       │
│ Map (StdDev) │  │ Interval Plot    │
└──────────────┘  └──────────────────┘
```

### Figure 8: Methodology Framework
```
Layout: Full page
┌─────────────────────────────────────┐
│ Data Acquisition → Preprocessing → │
│ ┌────┐   ┌────┐   ┌────┐   ┌────┐ │
│ │S1  │   │S2  │   │LS  │   │DEM │ │
│ └────┘   └────┘   └────┘   └────┘ │
│                                     │
│ Analysis → Classification →         │
│ Post-processing → Validation →      │
│                                     │
│ Result → Figures → Publication       │
└─────────────────────────────────────┘
```

### Graphical Abstract
```
Layout: Single landscape panel
Size: 1296 x 765 px (typical Elsevier)
Content: Workflow summary + key result
Style: Simplified icons, clean arrows,
       minimal text, 3-5 color palette
```

### TOC Figure
```
Size: Mini thumbnail
Content: Single compelling result image
        or simplified workflow
```

## Color Schemes for Journals

### Remote Sensing (MDPI)
```python
LC_COLORS_MDPI = {
    'Cropland':     '#FFFF64',
    'Forest':       '#006400',
    'Grassland':    '#00A000',
    'Shrubland':    '#A6CE39',
    'Water':        '#0064FF',
    'Wetland':      '#966400',
    'Built-up':     '#FF0000',
    'Bareland':     '#E6E6A0',
    'Ice/Snow':     '#E6FFFF',
}
```

### Nature/Science
```python
NATURE_COLORS = ['#E69F00', '#56B4E9', '#009E73',
                 '#F0E442', '#0072B2', '#D55E00',
                 '#CC79A7', '#999999']
```

### Elsevier Journals
```python
ELSEVIER_COLORS = ['#4477AA', '#CC6677', '#DDCC77',
                   '#117733', '#AA4499', '#88CCEE',
                   '#332288', '#44AA99']
```

## Font Requirements by Journal

| Journal | Body Font | Figure Font | Min Size |
|---------|-----------|-------------|----------|
| Nature | Arial | Arial/Helvetica | 6pt |
| Science | Arial | Arial/Helvetica | 5pt |
| Remote Sensing | Times New Roman | Arial | 7pt |
| ISPRS | Times New Roman | Arial/Helvetica | 6pt |
| RSE | Times New Roman | Arial/Helvetica | 6pt |
| IEEE | Times New Roman | Arial/Helvetica | 8pt |
| Elsevier | Any standard | Arial/Helvetica | 6pt |
| AGU (JGR) | Times New Roman | Arial/Helvetica | 6pt |

## Cartographic Elements Checklist
- [ ] Scale bar (with units)
- [ ] North arrow (true north)
- [ ] Legend (clear labels, no technical codes)
- [ ] Graticule/Graticule labels
- [ ] CRS annotation (e.g., "WGS 84 / UTM zone 50N")
- [ ] Data source note
- [ ] Author credit line if applicable
- [ ] Base map attribution (if using OSM, ESRI, etc.)
- [ ] DOI or citation for data reuse
