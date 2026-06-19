"""
example_env_check.py - Check your QGIS GeoAI environment
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from geoai_env_setup import generate_env_report

report = generate_env_report()
print("=== System ===")
print(f"Platform: {report['system']['platform']}")
print(f"Python: {report['system']['python']}")

print("\n=== QGIS ===")
if report["qgis"]:
    for q in report["qgis"]:
        print(f"  Found: {q['path']} ({q['version']})")
else:
    print("  QGIS not detected")

print("\n=== Python GIS Packages ===")
for pkg, ver in sorted(report["python_packages"].items()):
    status = f"v{ver}" if ver else "MISSING"
    print(f"  {pkg}: {status}")
