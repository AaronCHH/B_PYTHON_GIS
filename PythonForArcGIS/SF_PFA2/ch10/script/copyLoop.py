# copyLoop.py
# Purpose: Make a copy of each ASCII .txt extension file.

import arcpy, os

arcpy.env.workspace = 'C:/gispy/data/ch10'
outDir = 'C:/gispy/scratch/'
theFiles = os.listdir(arcpy.env.workspace)
for fileName in theFiles:
    if fileName.endswith('.txt'):
        outName = outDir + fileName[:-4] + 'V2.txt'
        arcpy.Copy_management(fileName, outName)
        print '{0} created.'.format(outName)
