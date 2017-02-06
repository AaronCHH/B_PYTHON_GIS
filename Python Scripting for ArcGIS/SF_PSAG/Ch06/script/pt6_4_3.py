import arcpy
from arcpy import env

env.workspace = "../DATA"

fclist = arcpy.ListFeatureClasses("", "point")

print fclist