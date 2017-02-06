# pt3
import arcpy
from arcpy import env
# env.workspace = "C:/raster"
# rasterband = "img.tif/Band_1"
env.workspace = "./Exercise09/"
rasterband = "landcover.tif/Band_1"
desc = arcpy.Describe(rasterband)
print desc.meanCellHeight
print desc.meanCellWidth
print desc.pixelType

raw_input()