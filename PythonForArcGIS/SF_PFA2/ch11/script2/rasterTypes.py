# rasterTypes.py
# Purpose: Use a wildcard to selectively list files.
import arcpy
arcpy.env.workspace = 'ch11/data'

# a. Use empty parenthesis to list ALL the rasters in the current workspace.
rasts = arcpy.ListRasters()
print 'a. All the rasters:'
print rasts
print

# b. List ALL the GIF type rasters.
rasts = arcpy.ListRasters('*', 'GIF')
print 'b. GIF rasters:'
print rasts
print

# c. List the raster whose name is GIF
rasts = arcpy.ListRasters('GIF')
print 'c. raster named GIF:'
print rasts
print

# d. List the rasters whose names start with 'tree'.
rasts = arcpy.ListRasters('tree*')
print 'd. tree* rasters:'
print rasts
print

# e. List the rasters whose names start with 'tree' which are GIF type files.
rasts = arcpy.ListRasters('tree*', 'GIF')
print 'e. tree* GIF type rasters:'
print rasts
print
