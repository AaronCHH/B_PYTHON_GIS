# simpleBuffer.py
import arcpy

# Buffer park.shp by 0.25 miles around each feature exterior.
# Buffers ends are rounded & all buffers are dissolved into a single feature.
arcpy.Buffer_analysis('C:/gispy/data/ch01/park.shp',
                      'C:/gispy/scratch/parkBuffer.shp',
                      '0.25 miles', 'OUTSIDE_ONLY', 'ROUND', 'ALL')
