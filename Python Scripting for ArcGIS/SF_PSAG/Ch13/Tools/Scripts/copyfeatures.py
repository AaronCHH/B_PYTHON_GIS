import arcpy
import os
from arcpy import env
env.workspace = arcpy.GetParameterAsText(0)
outworkspace = arcpy.GetParameterAsText(1)
fclist = arcpy.ListFeatureClasses()
fcount = len(fclist)
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase", 0, fcount, 1)
for fc in fclist:
    arcpy.SetProgressorLabel("Copying" + fc + "...")
    fcdesc = arcpy.Describe(fc)
    outfc = os.path.join(outworkspace, fcdesc.baseName)
    arcpy.CopyFeatures_management(fc, outfc)
    arcpy.SetProgressorPosition()
arcpy.ResetProgressor()