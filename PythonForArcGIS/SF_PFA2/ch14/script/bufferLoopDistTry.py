# bufferLoopDistTry.py
# Purpose: Buffer the input file by the given distance.
# Usage: input_filename numeric_distance (using the default unit of measure)
# Example input: C:/gispy/data/ch14/cover.shp 3

import arcpy, sys, os
arcpy.env.workspace = os.path.dirname(sys.argv[1])
fc = os.path.basename(sys.argv[1])
outDir = 'C:/gispy/scratch/'
arcpy.env.overwriteOutput = False
maxDist = float(sys.argv[2])
i = 1
while i <= maxDist:
    try:
        outFile = outDir + os.path.splitext(fc)[0] + str(i) + 'Buff.shp'
        distance = str(i) + ' miles'
        arcpy.Buffer_analysis(fc, outFile, distance)
        print 'Created: ', outFile
    except arcpy.ExecuteError:
        print arcpy.GetMessage(3)
    i = i + 1
