# scriptWithFunction.py
# Purpose: Call three tools (to find avg. nearest neighbor, intersection, and get count)
#          Print the results from avg. nearest neighbor and get count without using a function.
# Usage: No script arguments needed.

import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch15/tester.gdb'
arcpy.env.overwriteOutput = True

res = arcpy.AverageNearestNeighbor_stats('schools')
resList = res.getMessages().split('\n')
for message in resList:
    if '...' not in message and 'Time:' not in message:
        print message

arcpy.Intersect_analysis(['schools', 'workzones'], 'intersectOutput')

res = arcpy.GetCount_management('intersectOutput')
resList = res.getMessages().split('\n')
for message in resList:
    if '...' not in message and 'Time:' not in message:
        print message
