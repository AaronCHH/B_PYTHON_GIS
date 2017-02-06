# scriptPathOptionalv2.py
# Purpose: List the files in the given directory or the current directory.
# Usage: {directory path}
import arcpy, os

if arcpy.GetParameterAsText(0):
    workingDir = arcpy.GetParameterAsText(0)
else:
    # Get the script location
    scriptPath = os.path.abspath(__file__)
    workingDir = os.path.dirname(scriptPath)

print '{0} contains the following files:'.format(workingDir)
print os.listdir(workingDir)
