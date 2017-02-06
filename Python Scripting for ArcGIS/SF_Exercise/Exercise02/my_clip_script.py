import arcpy
arcpy.env.workspace = "./DATA/"
arcpy.Clip_analysis("soils.shp","basin.shp","./Results/soils_Clip2")