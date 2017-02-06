# bufferAll.py
# Purpose: Buffer all the feature classes in an input folder by the input distance and
#          send the output file names to script tool.
# Arguments: working_directory linear_unit
# Sample input: C:/gispy/data/ch23/smallDir "0.2 miles"

import arcpy, reportSTargs, sys

arcpy.env.overwriteOutput = True
arcpy.env.workspace = sys.argv[1]
distance = sys.argv[2]

fcs = arcpy.ListFeatureClasses()
outList = []
for fc in fcs:
    reportSTargs.printArc('Processing: {0}'.format(fc))
    outputFile = 'C:/gispy/scratch/' + fc[:-4] + 'Out.shp'
    try:
        arcpy.Buffer_analysis(fc, outputFile, distance)
        reportSTargs.printArc('Created {0}'.format(outputFile))
        outList.append(outputFile)
    except arcpy.ExecuteError:
        reportSTargs.printArc(arcpy.GetMessages())

results = ";".join(outList)

reportSTargs.printArc(results)

arcpy.SetParameterAsText(2, results)
