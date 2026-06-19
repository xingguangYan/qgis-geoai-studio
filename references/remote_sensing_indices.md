# Remote Sensing Indices Reference

## Vegetation Indices

| Index | Formula | Description | Sensor | Scale |
|-------|---------|-------------|--------|-------|
| NDVI | (NIR - Red) / (NIR + Red) | Normalized Difference Vegetation Index | All | [-1, 1] |
| EVI | 2.5 * (NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1) | Enhanced Vegetation Index | MODIS, Landsat | [-1, 1] |
| EVI2 | 2.5 * (NIR - Red) / (NIR + 2.4*Red + 1) | Two-band EVI | Sentinel-2 | [-1, 1] |
| SAVI | (NIR - Red) * 1.5 / (NIR + Red + 0.5) | Soil-Adjusted Vegetation Index | All | [-1, 1] |
| OSAVI | (NIR - Red) / (NIR + Red + 0.16) | Optimized SAVI | All | [-1, 1] |
| MSAVI2 | (2*NIR+1 - sqrt((2*NIR+1)^2 - 8*(NIR-Red)))/2 | Modified SAVI | All | [-1, 1] |
| ARVI | (NIR - (2*Red - Blue)) / (NIR + (2*Red - Blue)) | Atmospherically Resistant VI | Landsat | [-1, 1] |
| GCI | (NIR / Green) - 1 | Green Chlorophyll Index | All | 0+ |
| NDRE | (NIR - RE1) / (NIR + RE1) | Normalized Difference Red Edge | S2, WV | [-1, 1] |
| MCARI | ((RE1-Red)-0.2*(RE1-Green))*(RE1/Red) | Modified Chlorophyll Absorption | S2 | - |
| TCARI | 3*((RE1-Red)-0.2*(RE1-Green)*(RE1/Red)) | Transformed Chlorophyll Absorption | S2 | - |
| RECI | (NIR/RE1)-1 | Red Edge Chlorophyll Index | S2 | - |
| CVI | NIR * Red / Green^2 | Chlorophyll Vegetation Index | All | - |

## Water Indices

| Index | Formula | Description | Sensor |
|-------|---------|-------------|--------|
| NDWI | (Green - NIR) / (Green + NIR) | Normalized Difference Water Index | All |
| MNDWI | (Green - SWIR1) / (Green + SWIR1) | Modified NDWI | Landsat, S2 |
| AWEI_sh | Blue + 2.5*Green - 1.5*(NIR+SWIR1) - 0.25*SWIR2 | Automated Water Extraction Index (shadow) | Landsat |
| AWEI_nsh | 4*(Green-SWIR1) - (0.25*NIR+2.75*SWIR2) | AWEI (non-shadow) | Landsat |
| WI2015 | 1.7204 + 171*Green + 3*Red - 70*NIR - 45*SWIR1 - 71*SWIR2 | Water Index 2015 | Landsat |

## Built-up Indices

| Index | Formula | Description | Sensor |
|-------|---------|-------------|--------|
| NDBI | (SWIR1 - NIR) / (SWIR1 + NIR) | Normalized Difference Built-up Index | Landsat |
| BUI | NDBI - NDVI | Built-up Index | Landsat |
| IBI | (2*SWIR1/(SWIR1+NIR) - (NIR/(NIR+Red) + Green/(Green+SWIR1))) / (2*SWIR1/(SWIR1+NIR) + (NIR/(NIR+Red) + Green/(Green+SWIR1))) | Index-based Built-up Index | Landsat |
| UI | (SWIR2 - NIR) / (SWIR2 + NIR) | Urban Index | Landsat |

## Burn & Bare Indices

| Index | Formula | Description | Sensor |
|-------|---------|-------------|--------|
| NBR | (NIR - SWIR2) / (NIR + SWIR2) | Normalized Burn Ratio | All |
| dNBR | NBR_pre - NBR_post | Difference NBR | All |
| BAI | 1 / ((0.1-Red)^2 + (0.06-NIR)^2) | Burn Area Index | Landsat |
| BI | sqrt((Red^2+Green^2+NIR^2)/3) | Bareness Index | All |
| NDSI | (Green - SWIR1) / (Green + SWIR1) | Normalized Difference Snow Index | All |

## Moisture Indices

| Index | Formula | Description | Sensor |
|-------|---------|-------------|--------|
| NDMI | (NIR - SWIR1) / (NIR + SWIR1) | Normalized Difference Moisture Index | All |
| MNDMI | (Green - SWIR1) / (Green + SWIR1) | Modified NDMI | All |
| MSI | SWIR1 / NIR | Moisture Stress Index | Landsat |
| NDWI_Gao | (NIR - SWIR2) / (NIR + SWIR2) | NDWI (Gao, 1996) | All |

## Biophysical Parameters

| Parameter | Method | Description |
|-----------|--------|-------------|
| LAI | 3.618*EVI - 0.118 | Leaf Area Index (empirical) |
| FPAR | 1.2*(1-exp(-0.65*LAI)) | Fraction of PAR absorbed |
| fCover | 1 - (NDVI - NDVI_soil)/(NDVI_veg - NDVI_soil) | Fractional Vegetation Cover |
| GPP | PAR * fPAR * LUE | Gross Primary Productivity |
| NPP | GPP - R_auto | Net Primary Productivity |
| WUE | GPP / ET | Water Use Efficiency |
| LUE | 0.022 * T_scalar * W_scalar | Light Use Efficiency |
| AGB | a * NDVI^b (site-specific) | Above-Ground Biomass |
| Carbon | AGB * 0.47 | Carbon Stock |
| SOC | Regression from spectral bands | Soil Organic Carbon |

## Computation Helper (Python/NumPy)
```python
def compute_index(bands, index_name):
    """Compute remote sensing index from band dictionary."""
    import numpy as np

    # Band mapping (adjust for your sensor)
    B = bands.get('blue')
    G = bands.get('green')
    R = bands.get('red')
    N = bands.get('nir')
    S1 = bands.get('swir1')
    S2 = bands.get('swir2')
    RE1 = bands.get('rededge1')
    RE2 = bands.get('rededge2')

    eps = 1e-10

    indices = {
        'NDVI': (N - R) / (N + R + eps),
        'EVI': 2.5 * (N - R) / (N + 6*R - 7.5*B + 1 + eps),
        'EVI2': 2.5 * (N - R) / (N + 2.4*R + 1 + eps),
        'SAVI': (N - R) * 1.5 / (N + R + 0.5 + eps),
        'OSAVI': (N - R) / (N + R + 0.16 + eps),
        'NDWI': (G - N) / (G + N + eps),
        'MNDWI': (G - S1) / (G + S1 + eps),
        'NDBI': (S1 - N) / (S1 + N + eps),
        'NBR': (N - S2) / (N + S2 + eps),
        'NDMI': (N - S1) / (N + S1 + eps),
        'BAI': 1 / ((0.1-R)**2 + (0.06-N)**2 + eps),
        'AWEI_sh': B + 2.5*G - 1.5*(N+S1) - 0.25*S2,
        'AWEI_nsh': 4*(G-S1) - (0.25*N+2.75*S2),
        'IBI': (2*S1/(S1+N+eps) - (N/(N+R+eps) + G/(G+S1+eps))) /
               (2*S1/(S1+N+eps) + (N/(N+R+eps) + G/(G+S1+eps))),
    }
    return indices.get(index_name)

# Sentinel-2 band mapping
S2_BANDS = {
    'B1': 'coastal', 'B2': 'blue', 'B3': 'green', 'B4': 'red',
    'B5': 'rededge1', 'B6': 'rededge2', 'B7': 'rededge3',
    'B8': 'nir', 'B8A': 'nir2', 'B9': 'water_vapor',
    'B11': 'swir1', 'B12': 'swir2'
}

# Landsat band mapping (OLI)
LS_BANDS = {
    'B1': 'coastal', 'B2': 'blue', 'B3': 'green', 'B4': 'red',
    'B5': 'nir', 'B6': 'swir1', 'B7': 'swir2'
}
```

## Time Series Analysis

### LandTrendr (Landsat-based Detection of Trends)
- Purpose: Disturbance and recovery detection
- Algorithm: Temporal segmentation with vertex identification
- Key parameters: max_segments, spike_threshold, recovery_threshold
- Implementation: `pip install lt-gee` or QGIS plugin

### CCDC (Continuous Change Detection and Classification)
- Purpose: Continuous land cover change monitoring
- Algorithm: Time-series model fitting with harmonic terms
- Output: Change date, magnitude, classification
- Implementation: `ccdc` Python package

### BFAST (Breaks For Additive Seasonal and Trend)
- Purpose: Breakpoint detection in time series
- Algorithm: Iterative decomposition with structural change tests
- Implementation: `bfast` R package (via rpy2)
```python
import rpy2.robjects as ro
r_code = '''
library(bfast)
data <- ts(ndvi_values, frequency=23, start=c(2010,1))
fit <- bfast(data, h=0.15, season="harmonic", max.iter=5)
plot(fit)
'''
ro.r(r_code)
```

### Mann-Kendall Trend Test
```python
from scipy import stats
import numpy as np

def mann_kendall(series):
    """Mann-Kendall trend test."""
    n = len(series)
    s = 0
    for i in range(n-1):
        for j in range(i+1, n):
            s += np.sign(series[j] - series[i])
    return s

def sen_slope(series):
    """Sen"s slope estimator."""
    n = len(series)
    slopes = []
    for i in range(n-1):
        for j in range(i+1, n):
            slopes.append((series[j] - series[i]) / (j - i))
    return np.median(slopes)

# Example usage
years = np.arange(2010, 2025)
ndvi_values = np.array([0.3, 0.32, 0.28, 0.35, 0.31, 0.33, 0.36, 0.34, 0.38, 0.37, 0.40, 0.39, 0.42, 0.41, 0.45])
s = mann_kendall(ndvi_values)
slope = sen_slope(ndvi_values)
tau, p_value = stats.kendalltau(years, ndvi_values)
print(f"Mann-Kendall S={s}, tau={tau:.3f}, p={p_value:.4f}, Sen slope={slope:.4f}")
```
