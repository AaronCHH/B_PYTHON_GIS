import os
os.path
os.getcwd()
import arcpy
arcpy.Exists("./DATA/hospitals.shp")
from arcpy import env
env.workspace = os.getcwd()
arcpy.Usage("Clip_analysis")
arcpy.Usage("Clip")
prjFile = "./DATA/facilities.prj"
spatial_ref = arcpy.SpatialReference(prjFile)
arcpy.DefineProjection_management("hospitals", spatial_ref)
print spatial_ref.name
print spatial_ref.linearUnitName
print spatial_ref.XYResolution