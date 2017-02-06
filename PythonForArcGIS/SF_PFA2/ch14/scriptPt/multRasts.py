# multRast.py
# Purpose: Multiply each raster in a database by an input factor.
# Usage: numeric_value
# Example input: 5
import arcpy, sys

# Set multiplication factor
factor = float(sys.argv[1])

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'data/rastTester.gdb'
arcpy.CheckOutExtension('Spatial')
outDir = 'scratch/'

# Get raster list & multiply each by a factor
rasterList = arcpy.ListRasters()
for rasterImage in rasterList:
    rasterObj = arcpy.Raster(rasterImage)
    rastMult = rasterObj * factor
    rastMult.save(outDir + rasterImage)
    del rastMult
