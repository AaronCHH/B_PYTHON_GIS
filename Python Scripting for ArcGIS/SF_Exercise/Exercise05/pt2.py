import os
from arcpy import env
env.workspace = os.getcwd()

arcpy.Buffer_analysis("facilities", "Results/facilities_buffer.shp", "500 METERS")