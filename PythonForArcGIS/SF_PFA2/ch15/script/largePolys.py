# largePolys.py
# Purpose: Count the number of large polygons in the workspace.
# Usage: input_workspace
# Example input: C:/gispy/data/ch15/tester.gdb
import arcpy, sys


def countLargePolygons(data, threshold):
    '''Return the number of polygons in the data larger than the threshold.'''
    whereClause = 'Shape_Area > {0}'.format(threshold)
    arcpy.MakeFeatureLayer_management(data, 'lyr')
    arcpy.SelectLayerByAttribute_management('lyr', 'NEW_SELECTION', whereClause)
    res = arcpy.GetCount_management('lyr')
    # Get the first result (the count)
    strCount = res.getOutput(0)
    # getOutput returns a string; cast it to integer before returning it
    intCount = int(strCount)
    return intCount

arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteOutput = True
fcs = arcpy.ListFeatureClasses('', 'Polygon')
polyCount = 0
largeArea = 100000
for fc in fcs:
    fcLargeCount = countLargePolygons(fc, largeArea)
    polyCount = polyCount + fcLargeCount

print 'Total polygons in {0} with area > {1} = {2}'.format(arcpy.env.workspace, largeArea, polyCount)
