import arcpy
from arcpy import env

env.workspace = "C:/Data"
rasterlist = arcpy.ListRasters()

print rasterlist