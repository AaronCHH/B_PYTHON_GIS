# insertLine.py
# Purpose: Find the centroids of two polygons in park.shp, then
#          create a line segment connecting these points
#          and add it to parkLines with left_fid set to 50.
# Solution is similar to the insertPolygon.py example

import arcpy, os, traceback

fcPoly = 'C:/gispy/data/ch17/park.shp'
origfcLine = 'C:/gispy/data/ch17/parkLines.shp'
fcLine = 'C:/gispy/scratch/' + os.path.basename(origfcLine)
arcpy.Copy_management(origfcLine, fcLine)
try:
    with arcpy.da.SearchCursor(fcPoly, ['SHAPE@XY']) as sc:
        # Get 2 centroids
        row = sc.next()
        point1 = arcpy.Point(row[0][0], row[0][1])
        print 'Point1: ({0},{1})'.format(row[0][0], row[0][1])
        row = sc.next()
        point2 = arcpy.Point(row[0][0], row[0][1])
        print 'Point2: ({0},{1})'.format(row[0][0], row[0][1])
    del sc
except:
    print 'An error occurred.'
    traceback.print_exc()
    del sc

### Create an array and then a polyline.  Then use an insert cursor.
