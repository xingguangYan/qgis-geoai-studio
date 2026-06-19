@echo off
REM QGIS GeoAI Studio Installer
echo Installing QGIS GeoAI Studio...
echo.
REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

REM Install dependencies
echo Installing Python packages...
pip install geopandas rasterio shapely matplotlib scikit-learn scipy numpy pandas
pip install seaborn plotly openpyxl python-docx pillow requests

REM Optional
pip install earthengine-api geemap xarray rioxarray netCDF4 h5py

echo.
echo ====================================
echo QGIS GeoAI Studio installed!
echo ====================================
echo.
echo To use with QGIS Python:
echo   set PYTHONHOME=D:\QGIS\apps\Python312
echo   set PYTHONPATH=D:\QGIS\apps\qgis\python
echo   D:\QGIS\bin\python.exe scripts\\geoai.py env
echo.
pause
