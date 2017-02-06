# point2LineV2.py (a modification of 'points2Line.py' from Chapter 10.)
# Purpose: V2 one uses the 'enumerate' function in the loop to
#     create a unique output name based on a number.
# Usage: No arguments needed.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch12'
arcpy.env.overwriteOutput = True
outDir = 'C:/gispy/scratch/'

myFiles = ['data1.shp', 'data2.shp', 'data3.shp', 'data4.shp']
for index, currentFile in enumerate(myFiles):
    # Create a unique output names, 'Line1.shp,', 'Line2.shp'...
    outputName = 'Line{0}.shp'.format(index)
    arcpy.PointsToLine_management(currentFile, outDir + outputName)
    print outputName,
