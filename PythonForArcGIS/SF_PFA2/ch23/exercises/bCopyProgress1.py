# bCopy.py
# Purpose: Copy the raster or feature class datasets
#          from the source workspace to the destination workspace.
# Input:  source workspace, destination workspace, dataset type
# Sample input1: C:/gispy/data/ch17/tester.gdb C:/gispy/data/ch23/out.gdb "feature class"
# Sample input2: C:/gispy/data/ch17/testRaster.gdb C:/gispy/data/ch23/out.gdb raster
# Sample input3: C:/gispy/data/ch17/tester.gdb C:/gispy/data/ch23/out.mdb raster
import arcpy, os, sys


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)

arcpy.env.workspace = sys.argv[1]
outputWorkspace = sys.argv[2]
dType = sys.argv[3]

outPath = os.path.dirname(outputWorkspace)
outName = os.path.basename(outputWorkspace)
if not arcpy.Exists(outputWorkspace):
    if outName.endswith('gdb'):
        arcpy.CreateFileGDB_management(outPath, outName)
    else:
        arcpy.CreatePersonalGDB_management(outPath, outName)

if dType == 'raster':
    datasets = arcpy.ListRasters()
else:
    datasets = arcpy.ListFeatureClasses()

for d in datasets:
    dout = outputWorkspace + '/' + d
    try:
        arcpy.Copy_management(d, dout)
        message = '{0}/{1} was copied to {2}'.format(
            arcpy.env.workspace, d, dout)
    except arcpy.ExecuteError:
        message = arcpy.GetMessages()
    printArc(message)
