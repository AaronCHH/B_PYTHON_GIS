# wildcards.py
# Purpose: Use a wildcard to selectively list files.

import arcpy
arcpy.env.workspace = 'ch11/data/rastTester.gdb'

# a. Use '*' or empty parentheses to list ALL the rasters in the workspace.
rasts = arcpy.ListRasters('*')
print 'a. All the rasters:'
print rasts
print

# b. List the rasters whose names START with 'elev'.
rasts = arcpy.ListRasters('elev*')
print 'b. elev* rasters:'
print rasts
print

# c. List a raster whose name is exactly 'elev'.
rasts = arcpy.ListRasters('elev')
print 'c. elev raster:'
print rasts
