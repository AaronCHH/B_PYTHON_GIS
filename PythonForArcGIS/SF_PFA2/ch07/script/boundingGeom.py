# boundingGeom.py
# Purpose: Find the minimum bounding geometry of a set of features.
# Usage: No arguments required.

import arcpy

arcpy.env.workspace = 'C:/gispy/data/ch07'
arcpy.env.overwriteOutput = True

inputFeatures = 'park.shp'
outputFeatures = 'C:/gispy/scratch/boundingBoxes.shp'

arcpy.MinimumBoundingGeometry_management(inputFeatures, outputFeatures)
