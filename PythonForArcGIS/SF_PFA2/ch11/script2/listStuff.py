# listStuff.py
# Purpose: Use arcpy to list workspaces and tables.
import arcpy

arcpy.env.workspace = 'ch11/data'

print '---Workspaces---'
workspaces = arcpy.ListWorkspaces()
for wspace in workspaces:
    print wspace

print '\n---Tables---'

tables = arcpy.ListTables()
for table in tables:
    print table
