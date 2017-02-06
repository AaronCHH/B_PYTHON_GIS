import arcpy
import os
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise11"
fclist = arcpy.ListFeatureclasses()
for fc in fclist:
    desc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, os.path.join("Results/study.mdb", desc.basename))