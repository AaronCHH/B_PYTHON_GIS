# pt2.py
import arcpy
from arcpy import env
env.workspace = "./Exercise09/"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
print desc.dataType
print desc.bandCount
print desc.compressionType

raw_input()