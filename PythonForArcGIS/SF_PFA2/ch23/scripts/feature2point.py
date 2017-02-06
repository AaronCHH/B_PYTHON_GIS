# feature2point.py
# Purpose: Find the centroids of the input polygons.

import arcpy, sys

arcpy.env.overwriteOutput = True
inputFile = sys.argv[1]
outputFile = 'C:/gispy/scratch/Points.shp'

# Find points based on the input.
arcpy.FeatureToPoint_management(inputFile, outputFile)

# Return the results to the tool.
arcpy.SetParameterAsText(1, outputFile)
