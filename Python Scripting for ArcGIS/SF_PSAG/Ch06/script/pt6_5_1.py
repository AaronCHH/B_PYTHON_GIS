import arcpy
from arcpy import env

env.workspace = "../DATA"
tifflist = arcpy.ListRasters("","TIF")

for tiff in tifflist:
	arcpy.BuildPyramids_management(tiff)