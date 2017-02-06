# boxes.py
# Usage: No arguments required
import arcpy, os

#############################
length = 3
width = 6

# Find the paremeter of a box
perimeter = 2*length + 2*width

# Check if the box is square
if length == width:
    ans = True
else:
    ans = False

print perimeter
print ans

#############################
# Set box
length = 5
width = 5

# Find the paremeter of a box
perimeter = 2*length + 2*width

# Check if the box is square
if length == width:
    ans = True
else:
    ans = False

print perimeter
print ans

#############################
# Create a minimum bounding box feature class
# for each polgon feature class in the workspace
workspace = 'C:/gispy/data/ch15'
outDir = 'C:/gispy/data/ch15/scratch'
arcpy.env.workspace = workspace
fcs = arcpy.ListFeatureClasses('', 'Polygon')
for fc in fcs:
    outName = outDir + os.path.splitext(fc)[0] + 'Box.shp'
    try:
        arcpy.MinimumBoundingGeometry_management(fc, outName)
        print '{0} created.'.format(outName)
    except arcpy.ExecuteError:
        print arcpy.GetMessages()

#############################
# Create a minimum bounding box feature class
# for each polgon feature class in the workspace
workspace = 'C:/gispy/data/ch15/tester.gdb'
outDir = 'C:/gispy/scratch/'
arcpy.env.workspace = workspace
fcs = arcpy.ListFeatureClasses('', 'Polygon')
for fc in fcs:
    outName = outDir + os.path.splitext(fc)[0] + 'Box.shp'
    try:
        arcpy.MinimumBoundingGeometry_management(fc, outName)
        print '{0} created.'.format(outName)
    except arcpy.ExecuteError:
        print arcpy.GetMessages()
