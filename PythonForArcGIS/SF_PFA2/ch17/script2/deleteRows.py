# deleteRows.py
# Purpose: Delete the first x rows.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys

fcOrig = sys.argv[1]
fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)

field = 'FID'
x = 7
try:
    cursor = arcpy.da.UpdateCursor(fc, [field])
    # Delete the first x rows.
    for row in cursor:
        if row[0] < x:
            # Delete this row.
            cursor.deleteRow()
            print 'Deleted row {0}'.format(row[0])
    del cursor
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor
