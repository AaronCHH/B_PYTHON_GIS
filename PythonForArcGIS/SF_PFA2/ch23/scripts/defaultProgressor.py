# defaultProgressor.py
# Purpose: Delete files from a workspace based on their type and name and
#          use the default progressor to show progress.
# Arguments: workspace datatype(raster, feature class, or other) wildcard
# Sample input: C:/gispy/data/ch23/rastTester.gdb raster _out

import arcpy, os, sys, time


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)

arcpy.env.workspace = sys.argv[1]
fType = sys.argv[2]
wildcard = sys.argv[3]
substring = '*{0}*'.format(wildcard)

if fType == 'raster':
    data = arcpy.ListRasters(substring)
elif fType == 'feature class':
    data = arcpy.ListFeatureClasses(substring)
else:
    entireDir = os.listdir(arcpy.env.workspace)
    data = []
    for d in entireDir:
        if d.endswith(wildcard):
            data.append(d)

message = "Delete '{0}' files from {1}".format(wildcard, arcpy.env.workspace)
arcpy.SetProgressor('default', message)
time.sleep(1)
printArc(message)
for d in data:
    try:
        arcpy.SetProgressorLabel('Deleting {0}'.format(d))
        arcpy.Delete_management(d)
        printArc('{0}/{1} deleted'.format(arcpy.env.workspace, d))
        time.sleep(3)
    except arcpy.ExecuteError:
        printArc(arcpy.GetMessages())
