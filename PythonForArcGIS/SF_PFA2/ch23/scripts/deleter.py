# deleter.py
# Purpose: Delete files from a workspace based on their type and name.
# Usage: workspace datatype(raster, feature class, or other) wildcard
# Sample input: C:/gispy/data/ch23/rastTester.gdb raster _out

import arcpy, os, sys


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
for d in data:
    try:
        arcpy.Delete_management(d)
        printArc('{0}/{1} deleted.'.format(arcpy.env.workspace, d))
    except arcpy.ExecuteError:
        printArc(arcpy.GetMessages())
