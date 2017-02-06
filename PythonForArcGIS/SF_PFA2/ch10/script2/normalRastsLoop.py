# normalRastsLoop.py
# Purpose: Create 3 raster containing random values with a normal (gaussian) distribution.

import arcpy
arcpy.env.workspace = 'ch10/data'
outDir = 'ch10/scratch'
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension('Spatial')

n = 1
while n < 4:
  outputName = 'out{0}'.format(n)
  tempRast = arcpy.sa.CreateNormalRaster()
  tempRast.save(outDir + outputName)
  print '{0}{1} created.'.format(outDir, outputName)
  n = n + 1
del tempRast
print 'Normal raster creation complete.'
