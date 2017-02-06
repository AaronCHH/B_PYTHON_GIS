# whereClauseWithVar.py
# Purpose: Use a SQL query to select specific records based on user arguments.
# Example: C:/gispy/data/ch17/fires.shp FID FireName
import arcpy, sys, traceback

fc = sys.argv[1]
numericField = sys.argv[2]
fieldToPrint = sys.argv[3]

query = '{0} > 6'.format(numericField)  # String formatting.

try:
    with arcpy.da.SearchCursor(fc, [fieldToPrint], query) as cursor:
        recordList = [row[0] for row in cursor]
    del cursor

    print recordList
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor
