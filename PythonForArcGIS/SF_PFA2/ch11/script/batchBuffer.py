# batchBuffer.py
# Purpose: Buffer each feature class in the workspace.
# Usage: No arguments required.

import arcpy, os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch11/'

# GET a list of feature classes.
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    # SET the output variable. 
    fcBuffer = os.path.splitext(fc)[0] + 'Buffer.shp'
    # Call Buffer (Analysis) tool.
    arcpy.Buffer_analysis(fc, fcBuffer, '1 mile')
    print '{0} created.'.format(fcBuffer)
