# updateValues.py
# Purpose: Modify the fire type value and the fire name in each record.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys

fcOrig = sys.argv[1]
fc = 'scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)
fields = ['FireType_P', 'FireName']
cursor = arcpy.da.UpdateCursor(fc, fields)
try:
    for row in cursor:
        # Make changes to the list of values in 'row'
        row[0] = row[0] + 2      # Example: 13->15
        row[1] = row[1].title()  # Example: LITTLE CRK->Little Crk
        # Update the table (otherwise the changes won't be saved)
        cursor.updateRow(row)
        print 'Updated {0} and {1}'.format(row[0], row[1])
    del cursor
except:
    print 'An error occurred'
    traceback.print_exc()
    del cursor
