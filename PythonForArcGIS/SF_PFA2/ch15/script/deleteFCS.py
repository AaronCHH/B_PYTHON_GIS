# deleteFCS.py
# Purpose: Clear workspace of unwanted files.
# Usage: No arguments needed.
import arcpy

arcpy.env.workspace = 'C:/gispy/data/ch15/scratch'


def delBuffFCS():
    '''Delete feature classes with names containing "Buff".'''
    fcs = arcpy.ListFeatureClasses('*Buff*')
    for fc in fcs:
        arcpy.Delete_management(fc)
        print '{0} deleted.'.format(fc)


def delNamedFCS(delString):
    '''Delete feature classes with names containing delString.'''
    wildcard = '*{0}*'.format(delString)
    fcs = arcpy.ListFeatureClasses(wildcard)
    for fc in fcs:
        arcpy.Delete_management(fc)
        print '{0} deleted.'.format(fc)

delBuffFCS()
delNamedFCS('Out')
