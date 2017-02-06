# buffer2.py
# Purpose:  Buffer an input file by an input distance
#           and send the result to a script tool.

import arcpy, os, sys
arcpy.env.overwriteOutput = True

fileToBuffer = sys.argv[1]
distance = sys.argv[2]
arcpy.env.workspace = os.path.dirname(fileToBuffer)
outputFile = 'C:/gispy/scratch/Buff'

arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)

arcpy.SetParameterAsText(2, outputFile)
