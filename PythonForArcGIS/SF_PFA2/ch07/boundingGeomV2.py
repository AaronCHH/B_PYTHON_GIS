# boundingGeomV2.py (soft-coded using arcpy)
# Purpose: Find the minimum bounding geometry of a set of features.
# Usage: workspace, input_features, output_features
# Example: C:/gispy/data/ch07 park.shp C:/gispy/scratch/boundingBoxes.shp
import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

inputFeatures = arcpy.GetParameterAsText(1)
outputFeatures = arcpy.GetParameterAsText(2)

arcpy.MinimumBoundingGeometry_management(inputFeatures, outputFeatures)
