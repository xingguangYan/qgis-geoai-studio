from setuptools import setup, find_packages
setup(
    name="qgis-geoai-studio",
    version="1.0.0",
    description="QGIS GeoAI Studio - Remote Sensing & SCI Figure Generation",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "geopandas", "rasterio", "shapely", "matplotlib",
        "scikit-learn", "scipy", "numpy", "pandas",
    ],
    entry_points={
        "console_scripts": [
            "geoai=scripts.geoai:main",
        ],
    },
)
