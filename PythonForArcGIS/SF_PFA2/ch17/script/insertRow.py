# insertRow.py
# Purpose: Insert a new row without geometry.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys
fcOrig = sys.argv[1]
fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)
fields = ['FireId', 'CalendarYe']
# Create an insert cursor.
try:
    cursor = arcpy.da.InsertCursor(fc, fields)
    # Create a list with FireId=513180 & CalendarYr=2009.
    newRecord = [513180, 2009]
    # Insert the row (otherwise no change would occur).
    cursor.insertRow(newRecord)
    print 'Point inserted.'
    del cursor
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor
