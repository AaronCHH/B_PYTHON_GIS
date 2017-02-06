# buffer1.py
# Purpose:  Buffer a file and send the result to a script tool.

import arcpy
arcpy.env.overwriteOutput = True

fileToBuffer = 'C:/gispy/data/ch23/smallDir/randpts.shp'
distance = '500 meters'
outputFile = 'C:/gispy/scratch/randptsBuffer.shp'

arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)

arcpy.SetParameterAsText(0, outputFile)
