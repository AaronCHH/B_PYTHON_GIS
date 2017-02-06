# arcpyWalkBuffer.py
# Purpose: Walk the point shapefiles.
# Usage: input_directory output_directory
# Example: C:/gispy/data/ch11/ C:/gispy/scratch
import arcpy, sys
rootDir = sys.argv[1]
outDir = sys.argv[2]
arcpy.env.overwriteOutput = True
for root, dirs, files in arcpy.da.Walk(rootDir,
                                       datatype='FeatureClass',
                                       type='POINT'):
    arcpy.env.workspace = root
    for f in files:
        print '{0}/{1}'.format(root, f)
