# tableLister.py
# Purpose: Create shapefiles from 'stations*' xy tables, connect the points,
#          and then find then intersection of the lines.
# Usage:  workspace_containing_tables
# Example: C:/gispy/data/ch11/trains
import arcpy, os, sys
arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteOutput = True
tables = arcpy.ListTables('stations*', 'dBASE')

tempPoints = 'temporaryPointLayer'

for table in tables:
    # SET the output variable.
    lineFile = os.path.splitext(table)[0] + 'Line'
    # CALL geoprocessing tools.
    arcpy.MakeXYEventLayer_management(table, 'POINT_X', 'POINT_Y', tempPoints)
    arcpy.PointsToLine_management(tempPoints, lineFile)
    print '\t{0}/{1} created.'.format(arcpy.env.workspace, lineFile)

# GET the list of lines and intersect the lines.
lineList = arcpy.ListFeatureClasses('stations*Line*')
arcpy.Intersect_analysis(lineList, 'hubs', '#', '0.5 mile', 'POINT')
print '{0}/hubs created.'.format(arcpy.env.workspace)
