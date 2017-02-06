# insertPolygon.py
# Insert cursor polygon example
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys

# Create 3 point objects for the triangle.
a = arcpy.Point(2134000, 179643)
b = arcpy.Point(2147000, 163267)
c = arcpy.Point(2131327, 167339)

# Create an array, needed for creating a polygon.
myArray = arcpy.Array([a, b, c])

# Create a polygon.
poly = arcpy.Polygon(myArray)

fcOrig = sys.argv[1]
fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)
try:
    # Create an insert cursor.
    cursor = arcpy.da.InsertCursor(fc, ['SHAPE@', 'Id'])

    # Create row list.
    newRow = [poly, 333]

    # Insert the new row.
    # It's automatically given an FID one greater
    # than the largest existing one.
    cursor.insertRow(newRow)
    print 'Polygon inserted.'
    del cursor
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor
