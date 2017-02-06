# simpleBuffer.py
import arcpy

# Buffer park.shp by 0.25 miles around each feature exterior.
# Buffers ends are rounded & all buffers are dissolved into a single feature.
arcpy.Buffer_analysis('./data/park.shp',
                      './scratch/parkBuffer.shp',
                      '0.25 miles', 'OUTSIDE_ONLY', 'ROUND', 'ALL')
