# insertRows.py
# Purpose: Insert multiple rows without geometry.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, sys, traceback
fcOrig = sys.argv[1]
fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)

# Find the current fire numbers.
try:
    fields = ['FireNumber']
    cursor = arcpy.da.SearchCursor(fc, fields)
    fireNumbers = [row[0] for row in cursor]
    print '{0} fire numbers found.'.format(len(fireNumbers))
    del cursor
except:
    print 'An error occurred in the search.'
    traceback.print_exc()
    del cursor

# Insert 5 new fires for year 2015.
try:
    fields.append('CalendarYe')
    cursor = arcpy.da.InsertCursor(fc, fields)
    # Find the max value in list and increment by 1.
    fireNum = max(fireNumbers) + 1
    for i in range(5):
        # Create a row with unique fire number & year=2015.
        newRow = [fireNum, 2015]
        fireNum = fireNum + 1
        # Insert the row.
        cursor.insertRow(newRow)
        print 'New row created with fire# {0} and year = {1}.'.format(
                                newRow[0], newRow[1])
    del cursor
except:
    print 'An error occurred in the insertion.'
    traceback.print_exc()
    del cursor
