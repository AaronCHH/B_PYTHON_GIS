# askDirectory.py
# Purpose: Get a directory from the user and set the workspace.
# Usage: No script arguments required.
import tkFileDialog, arcpy

arcpy.env.workspace = tkFileDialog.askdirectory(initialdir="./",
                                                title='Select the FOLDER containing Landuse RASTERS')

print 'Workspace = {0}'.format(arcpy.env.workspace)
