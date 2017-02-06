# circles.py
# Purpose: Calculate circle statistics and create circle feature classes.
# Usage: No script arguments needed.
import arcpy, os, math


def arcLength(angle, radius, mode='degrees'):
    '''Find the length of an arc'''
    if mode == 'degrees':
        angle = angle*math.pi/180
    length = angle*radius
    return length
    print 'The length is {0}'.format(length)


def isCircle(majorSemiAxis, minorSemiAxis):
    '''Check if circle or ellipse'''
    if majorSemiAxis == minorSemiAxis:
        ans = True
    else:
        ans = False
    return ans


def createCircles(workspace, outDir):
    '''Buffer the points in each point
    feature class in the workspace.'''
    arcpy.env.workspace = workspace
    fcs = arcpy.ListFeatureClasses('', 'Point')
    for fc in fcs:
        outName = outDir + os.path.splitext(fc)[0] + 'Circles.shp'
        try:
            arcpy.Buffer_analysis(fc, outName, '50 meters')
        except arcpy.ExecuteError:
            print arcpy.GetMessages()

print arcLength(45, 1)
length = arcLength(3.14, 1, 'radians')
print isCircle(5, 4)
print createCircles('C:/gispy/data/ch15/tester.gdb', 'C:/gispy/scratch/')
