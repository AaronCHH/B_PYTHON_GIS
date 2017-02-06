import arcpy
from arcpy import env
env.workspace = "./Exercise09/"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
print desc.dataType

raw_input()