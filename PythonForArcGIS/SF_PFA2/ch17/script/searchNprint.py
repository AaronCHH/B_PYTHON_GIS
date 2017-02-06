# searchNprint.py
# Purpose: Print each fire name in a file.
# Usage: No script arguments needed.
import arcpy, traceback
try:
    cursor = arcpy.da.SearchCursor('C:/gispy/data/ch17/fires.shp', ['FireName'])
    for row in cursor:
        print row[0]
    del cursor
except:
    print 'An error occurred'
    traceback.print_exc()
    del cursor
