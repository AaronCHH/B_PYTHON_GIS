# oops.py
# Purpose: Count the number records in an intersections
#             between two datasets and delete the intersection file 
#             (but the intersection output is not deleted since this line
#              of code is placed after the 'return' statement).
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch15/tester.gdb'
arcpy.env.overwriteOutput = True


def countIntersection(dataList):
    '''Calculate the number of features in the intersection.'''
    tempData = 'intersectOut'
    arcpy.Intersect_analysis(dataList, tempData)
    res = arcpy.GetCount_management(tempData)
    print '{0} created.'.format(tempData)
    return int(res.getOutput(0))
    # uh-oh! The delection is not going to happen.
    arcpy.Delete_management(tempData)
    print '{0} deleted.'.format(tempData)

inputData = ['schools', 'workzones']
count = countIntersection(inputData)
print 'There are {0} intersections.'.format(count)
