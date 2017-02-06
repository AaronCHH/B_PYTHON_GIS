import os
from arcpy import env
env.workspace = os.getcwd()

in_features = "bike_routes"
clip_features = "zip"
out_features = "Results/bike_Clip.shp"
xy_tolerance = ""

arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)