import arcpy
from arcpy import env

env.workspace = "../DATA"

fclist = arcpy.ListFeatureClasses("w*")

print fclist