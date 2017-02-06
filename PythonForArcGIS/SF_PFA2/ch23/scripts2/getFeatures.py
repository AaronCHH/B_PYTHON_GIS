# getFeatures.py
# Purpose: Copy the digitized feature set input into a shapefile
#          and send this to the script tool as output.

import arcpy, sys
arcpy.env.overwriteOutput = True
fs = sys.argv[1]
outputFeat = 'C:/gispy/scratch/getFeaturesOutput.shp'
arcpy.CopyFeatures_management(fs, outputFeat)
arcpy.SetParameterAsText(1, outputFeat)
