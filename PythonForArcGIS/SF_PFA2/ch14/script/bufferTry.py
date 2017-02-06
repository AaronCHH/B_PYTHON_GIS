# bufferTry.py
# Purpose: Buffer the input dataset.
# Usage: Fullpath_filename outDir
# Example input: C:/gispy/data/ch14/parkLines.shp outputWorkspace
import arcpy, sys, os
arcpy.env.overwriteOutput = True
try:
    inFile = sys.argv[1]
    outDir = sys.argv[2]
    buffer = outDir + '/' + os.path.splitext(inFile)[0] + 'Buff.shp'
    arcpy.Buffer_analysis(inFile, buffer, '1 mile')
    print '{0} created.'.format(buffer)
except arcpy.ExecuteError:
    print arcpy.GetMessages()
except IndexError:
    print 'Usage: <full path shapefile name>'
