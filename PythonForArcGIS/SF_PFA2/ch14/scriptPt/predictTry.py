import arcpy, sys
arcpy.env.overwriteOutput = False
arcpy.env.workspace = 'C:/gispy/data/ch14/predict'
try:
    inFile = sys.argv[1]
    print 'HURRAY'
    desc = arcpy.Describe(inFile)
    print 'WOOPEEE!'
    dataShapeType = desc.shapeType
    print 'FAB'
except IndexError:
    print 'DOH'
    sys.exit(0)
except IOError:
    print 'MEH'
    sys.exit(0)
    print 'AT LAST'
except AttributeError:
    print 'EWWW'
    sys.exit(0)
if dataShapeType == 'Polygon':
    try:
        outputFile = arcpy.PolygonToLine_management(inFile, 'parkLines.shp')
        print 'LOL'
    except arcpy.ExecuteError:
        print 'UH-OH'
        print arcpy.GetMessage(arcpy.GetMessageCount()-1)
elif dataShapeType == 'Point':
    try:
        outputFile = arcpy.PointsToLine_management(inFile, 'out.shp')
        print 'PHEW'
    except arcpy.ExecuteError:
        print 'UH-OH'
        print arcpy.GetMessages()
    print 'SHAZAM'
print 'TOODLES'

# The workspace contains coverPolygons.shp, firePoints.shp,
#    parkLines.shp, and treeRast.gif
# Predict what will be printed with these inputs:
# -----------------------------------------------------

# 1. no arguments

# 2. C:/gispy/data/ch14/predict/bogus.shp (a file that doesn't exist)

# 3. C:/gispy/data/ch14/predict/tree.gif

# 4. C:/gispy/data/ch14/predict/coverPolgons.shp (a Polygon file)

# 5. C:/gispy/data/ch14/predict/firePoints.shp (a Point file)

# 6. C:/gispy/data/ch14/predict/parkLines.shp (a Polyline file)
