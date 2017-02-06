import arcpy
from arcpy import env

env.workspace = "../DATA"
fieldlist = arcpy.ListFields("roads.shp")

print fieldlist