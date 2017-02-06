# buffer_clipv2.py (soft-coded version)
# Purpose: Buffer a zone and use it to clip another file
# Usage: workspace output_directory file_to_buffer buffer_dist. file_to_clip
# Input example: C:/gispy/data/ch07/ C:/gispy/scratch/ special_regions.shp "1 mile" park.shp

import arcpy, sys

arcpy.env.overwriteOutput = 1
arcpy.env.workspace = sys.argv[1]
outDir = sys.argv[2]

# Set buffer params
fireDamage = sys.argv[3]
fireBuffer = outDir + fireDamage[:-4] + 'Buffer.shp'
bufferDist = sys.argv[4]

# Set clip params
park = sys.argv[5]
clipOutput = outDir + park[:-4] + 'DamageBuffer.shp'

# Call tools
arcpy.Buffer_analysis(fireDamage, fireBuffer, bufferDist)
print '{0} created.'.format(fireBuffer)
arcpy.Clip_analysis(park, fireBuffer, clipOutput)
print '{0} created.'.format(clipOutput)
