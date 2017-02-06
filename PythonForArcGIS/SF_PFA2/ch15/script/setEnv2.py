# setEnv2.py
# Purpose: Set arcpy environment properties.
# Usage: No script arguments needed.
import arcpy


def setEnviron2(workspace, overwriteVal):
    '''Set arcpy workspace and overwriteOutput properties
    based on function arguments.'''
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = overwriteVal

wSpace = 'C:/gispy/data/ch15/tester.gdb'
overwrite = False
setEnviron2(wSpace, overwrite)
