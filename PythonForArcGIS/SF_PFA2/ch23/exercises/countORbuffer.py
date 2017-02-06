# countORbuffer.py
# Purpose: Process input shapefile based on the user specified tool.
# Arguments:  Input feature class, tool name (buffer or get count), {buffer distance}.
# Example input1: C:/gispy/data/ch23/training/COVER4.shp "get count"
# Example input2: C:/gispy/data/ch23/smallDir/trails.shp "buffer" "1 mile"
import arcpy, os, sys


def printArc(message):
    print message
    arcpy.AddMessage(message)

arcpy.env.overwriteOutput = True
inputFile = sys.argv[1]
toolName = sys.argv[2]
arcpy.env.workspace = os.path.dirname(inputFile)

if toolName == 'buffer':
    distance = sys.argv[3]
    if distance == '#':
        distance = '2 Miles'
    outputFile = 'C:/gispy/scratch/outBuff'

    try:
        arcpy.Buffer_analysis(inputFile, outputFile, distance)
        m = '{0} called. {1} created'.format(toolName, outputFile)
        # Return the results to the tool.
        arcpy.SetParameterAsText(3, outputFile)
    except arcpy.ExecuteError:
        m = arcpy.GetMessages()
elif toolName == 'get count':
    try:
        count = arcpy.GetCount_management(inputFile)
        m = '{0} returned {1} records.'.format(toolName, count)
    except arcpy.ExecuteError:
        m = arcpy.GetMessages()
else:
    m = 'Tool {0} not called.'.format(toolName)

# Report success/failure.
printArc(m)
