# setEnv1.py
# Purpose: Set arcpy environment properties.
# Usage: No script arguments needed.
import arcpy


def setEnviron1():
    '''Set arcpy workspace and overwriteOutput properties
    to hard-coded values.'''
    arcpy.env.workspace = 'C:/gispy/data/ch15'
    arcpy.env.overwriteOutput = True
setEnviron1()
