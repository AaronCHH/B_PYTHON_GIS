# point2Line.py
# Purpose: Create a set of line features from a set of point features in a list.
import arcpy
arcpy.env.workspace = 'data'
outDir = 'scratch/'
arcpy.env.overwriteOutput = True

theFiles = ['data1.shp', 'data2.shp', 'data3.shp', 'data4.shp']
for currentFile in theFiles:
    # Remove file extension from the current name.
    baseName = currentFile[:-4]
    # Create unique output name. E.g., 'data1Line.shp'.
    outName = outDir + baseName + 'Line.shp'
    arcpy.PointsToLine_management(currentFile, outName)
    print '{0}{1} created.'.format(outDir, outName)
