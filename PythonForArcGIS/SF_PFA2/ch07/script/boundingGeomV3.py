# boundingGeomV3.py (soft-coded using sys)
# Purpose: Find the minimum bounding geometry of a set of features.
# Usage: workspace, input_features, output_features
# Example: C:/gispy/data/ch07 park.shp C:/gispy/scratch/boundingBoxes.shp
import arcpy, sys

arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteOutput = True

inputFeatures = sys.argv[2]
outputFeatures = sys.argv[3]

arcpy.MinimumBoundingGeometry_management(inputFeatures, outputFeatures)
