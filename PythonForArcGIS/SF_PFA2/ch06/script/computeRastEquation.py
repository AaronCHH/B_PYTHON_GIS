# computeRastEquation.py
# Purpose: Calculate 5 * 'getty_rast' - 2

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch06/rastSmall.gdb'
arcpy.CheckOutExtension('Spatial')

outRast1 = arcpy.sa.Times(5, 'dataRast')
outRast2 = arcpy.sa.Minus(outRast1, 2)
outRast2.save('equationRast')

print 'Output raster written in {0}'.format(arcpy.env.workspace)
del outRast1, outRast2
