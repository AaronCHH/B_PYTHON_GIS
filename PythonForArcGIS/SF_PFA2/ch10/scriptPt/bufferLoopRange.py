# bufferLoopRange.py
# Purpose: Buffer a park varying buffer distances from 1 to 5 miles.

import arcpy
arcpy.env.workspace = 'data'
outDir = 'scratch/'
arcpy.env.overwriteOutput = True
inName = 'park.shp'
for num in range(1, 6):
    # Set the buffer distance based on num ('1 miles', '2 miles', ...).
    distance = '{0} miles'.format(num)
    # Set the output name based on num ('buffer1.shp', 'buffer2.shp', ...)
    outName = outDir + 'buffer{0}.shp'.format(num)
    arcpy.Buffer_analysis(inName, outName, distance)
    print '{0}{1} created.'.format(outDir, outName)
