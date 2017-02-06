# buggyCursor.py
# WARNING: This script contains BUGS!  Remove them if you can.
# Purpose:   Count the number of records in park.shp with 'COVER'
#           field value that is neither 'woods' and nor 'orch'
# Usage: No arguments needed.
import traceback

filename = 'C:/gispy/data/ch17/parkCopy3.shp'
fields = ['COVER', 'FID']

count = 0  # Initialize count to zero.

try:
    with cursor as arcpy.da.SearchCursor(fileName, fields):
        for row in cursor:
            cover = row[1]
            if cover != 'woods' or cover != 'orch':
                count = count + 1
            del cursor
    print 'Number of records with other cover types:', count
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor
