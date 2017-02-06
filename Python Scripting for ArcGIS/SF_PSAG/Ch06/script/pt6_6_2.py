import arcpy
from arcpy import env

env.workspace = "../DATA.gdb"
fcs = arcpy.ListFeatureClasses()

fcs.sort()
print fcs

fcs.sort(reverse = True)
print fcs