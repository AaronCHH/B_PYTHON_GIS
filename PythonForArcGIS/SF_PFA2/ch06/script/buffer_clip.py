# buffer_clip.py (hard-coded version)
# Purpose: Buffer a zone and use it to clip another file
# Input: No arguments needed.

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch06'
outDir = 'C:/gispy/scratch/'

# Set buffer params
fireDamage = 'special_regions.shp'
fireBuffer = outDir + fireDamage[:-4] + 'Buffer.shp'
bufferDist = '1 mile'

# Set clip params
park = 'park.shp'
clipOutput = outDir + park[:-4] + 'DamageBuffer.shp'

arcpy.Buffer_analysis(fireDamage, fireBuffer, bufferDist)
print '{0} created.'.format(fireBuffer)
arcpy.Clip_analysis(park, fireBuffer, clipOutput)
print '{0} created.'.format(clipOutput)
