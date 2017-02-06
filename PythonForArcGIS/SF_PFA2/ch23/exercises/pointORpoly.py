# pointORpoly.py
# Purpose: Process polygon or point input based on the user specified tool.
# Arguments:  Point or polygon feature class, tool name (Feature to point,
#             Minimum bounding box, Thiessen polygon, or Points to line).

import arcpy, os, sys


def printArc(message):
    print message
    arcpy.AddMessage(message)

arcpy.env.overwriteOutput = True
inputFile = sys.argv[1]
toolName = sys.argv[2]
arcpy.env.workspace = os.path.dirname(inputFile)
outputFile = 'C:/gispy/scratch/out.shp'

if toolName == 'Feature to point':
    try:
        arcpy.FeatureToPoint_management(inputFile, outputFile)
        m = '{0} called. {1} created'.format(toolName, outputFile)
    except arcpy.ExecuteError:
        m = arcpy.GetMessages()
elif toolName == 'Minimum bounding box':
    try:
        arcpy.MinimumBoundingGeometry_management(inputFile, outputFile)
        m = '{0} called. {1} created'.format(toolName, outputFile)
    except arcpy.ExecuteError:
        m = arcpy.GetMessages()
elif toolName == 'Thiessen polygon':
    try:
        arcpy.CreateThiessenPolygons_analysis(inputFile, outputFile)
        m = '{0} called. {1} created'.format(toolName, outputFile)
    except arcpy.ExecuteError:
        m = arcpy.GetMessages()
elif toolName == 'Points to line':
    try:
        arcpy.PointsToLine_management(inputFile, outputFile)
        m = '{0} called. {1} created'.format(toolName, outputFile)
    except arcpy.ExecuteError:
        m = arcpy.GetMessages()
else:
    m = 'Tool {0} not called.'.format(toolName)

# Report success and return the results to the tool.
printArc(m)
arcpy.SetParameterAsText(2, outputFile)
