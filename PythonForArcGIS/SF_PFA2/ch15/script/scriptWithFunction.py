# scriptWithFunction.py (compare to scriptWithoutFunction.py)
# Purpose: Call three tools (to find avg. nearest neighbor, intersection, and get count)
#          Print the results from avg. nearest neighbor and get count using a function.
# Usage: No script arguments needed.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch15/tester.gdb'
arcpy.env.overwriteOutput = True


def reportResults(resultObj):
    '''Print selected result messages.'''
    resList = resultObj.getMessages().split('\n')
    arcpy.env.overwriteOutput = True
    for message in resList:
        if '...' not in message and 'Time:' not in message:
            print message

res = arcpy.AverageNearestNeighbor_stats('schools')
reportResults(res)  # Call the function.

arcpy.Intersect_analysis(['schools', 'workzones'], 'intersectOutput')

res = arcpy.GetCount_management('intersectOutput')
reportResults(res)  # Call the function.
