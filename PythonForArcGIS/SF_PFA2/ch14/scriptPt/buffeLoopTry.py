# bufferLoopTry.py
# Purpose: Buffer the feature classes in a workspace.
# Usage: No arguments needed.
import arcpy, os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'data'
outDir = 'scratch/'
fcs = arcpy.ListFeatureClasses()
distance = '500 meters'

for fc in fcs:
    outFile = outDir + os.path.splitext(fc)[0] + 'Buff.shp'
    try:
        arcpy.Buffer_analysis(fc, outFile, distance)
        print 'Created: {0}'.format(outFile)
    except arcpy.ExecuteError:
        print arcpy.GetMessage(2)
