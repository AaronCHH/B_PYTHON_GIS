# sqlQueryCursor.py
# Purpose: Use a SQL query to select specific records.
# Usage: No script arguments needed.
import arcpy, traceback
fc = 'data/fires.shp'

# Create the where_clause.
query = "SizeClass = 'A'"
try:
    sc = arcpy.da.SearchCursor(fc, ['CalendarYe'], query)

    for row in sc:
        print row[0],
    del sc
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor
