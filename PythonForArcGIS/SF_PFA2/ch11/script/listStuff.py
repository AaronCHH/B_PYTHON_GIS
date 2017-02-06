# listStuff.py
# Purpose: Use arcpy to list workspaces and tables.
import arcpy

arcpy.env.workspace = 'C:/gispy/data/ch11'

print '---Workspaces---'
workspaces = arcpy.ListWorkspaces()
for wspace in workspaces:
    print wspace

print '\n---Tables---'

tables = arcpy.ListTables()
for table in tables:
    print table
