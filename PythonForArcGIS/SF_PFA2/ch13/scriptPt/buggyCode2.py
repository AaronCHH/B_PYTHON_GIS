# buggyCode2.py
import arcpy, sys, os
arcpy.env.workspace = sys.argv[1]
fc = arcpy.ListFeatureClasses()
for fc in fcs:
    # Append Buffer to the output name?
    fcBuffer = os.path.splitext(fc)[0] + 'Buffer.shp'
    # Call buffer tool with required input, output, and distance arguments.
    arcpy.Buffer_analysis(fc, fcBuffer, '1 elephant')
