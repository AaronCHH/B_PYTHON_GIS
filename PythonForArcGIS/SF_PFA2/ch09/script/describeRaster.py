# describeRaster.py
# Purpose: Report the format of raster input file.
# Usage: workspace, raster_dataset
# Example: C:/gispy/data/ch09 getty.tif

import arcpy
arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
desc = arcpy.Describe(data)
if desc.dataType == 'RasterDataset':
    print 'Image format: {0}'.format(desc.format)
