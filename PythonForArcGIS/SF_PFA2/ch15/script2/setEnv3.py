# setEnv3.py
# Purpose: Set arcpy environment properties.
# Usage: workspace overwrite_output_value
# Example input: C:/gispy/data/ch15/scratch True
import arcpy, sys

wSpace = sys.argv[1]
overwrite = sys.argv[2]


def setEnviron3(workspace, overwriteVal):
    '''Set arcpy workspace and overwriteOutput properties
    based on function arguments.'''
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = overwriteVal

setEnviron3(wSpace, overwrite)
