# askWorkspaceRaw.py
# Purpose: Get a workspace with the raw_input function.
# Usage: No script arguments needed.
# raw_input DOES NOT restrict the user to valid workspaces.
# Use tkFileDialog askDirectory or a script tool instead.
import arcpy
arcpy.env.workspace = raw_input('Enter a workspace:')
print arcpy.env.workspace
