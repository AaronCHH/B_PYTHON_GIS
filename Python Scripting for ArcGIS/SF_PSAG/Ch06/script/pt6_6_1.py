import arcpy
from arcpy import env

env.workspace = "../DATA.gdb"

fcs = arcpy.ListFeatureClasses()

print len(fcs)