# batchBufferv2.py
# Purpose: Buffer each feature class in the workspace and
#          place output in a different workspace.
import arcpy, os
arcpy.env.overwriteOutput = True
# SET workspaces
arcpy.env.workspace = 'ch11/data'
outDir = 'ch11/scratch/buffers/'
if not os.path.exists(outDir):
    os.mkdir(outDir)
# GET a list of feature classes
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    # SET the output variable
    outName = os.path.splitext(fc)[0] + '_buffer.shp'
    fcBuffer = os.path.join(outDir, outName)
    # Call buffer tool
    arcpy.Buffer_analysis(fc, fcBuffer, '1 mile')
    print '{0} created in {1}.'.format(fcBuffer, outDir)
