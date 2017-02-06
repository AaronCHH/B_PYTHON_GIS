# osWalkBuffer.py
# Purpose: Walk and buffer the point shapefiles.
# Usage: input_directory output_directory
# Example: C:/gispy/data/ch12/wTest C:/gispy/scratch
import arcpy, os, sys
rootDir = sys.argv[1]
outDir = sys.argv[2]
arcpy.env.overwriteOutput = True
for root, dirs, files in os.walk(rootDir):
    arcpy.env.workspace = root
    fcs = arcpy.ListFeatureClasses('*', 'POINT')
    for f in fcs:
        # Set output name and perform geoprocessing on f
        outfile = outDir + '/' + os.path.splitext(f)[0] + '_buffer.shp'
        arcpy.Buffer_analysis(f, outfile, '1 mile')
        print '{0}/{1}  buffer ouput: {2}'.format(root, f, outfile)
