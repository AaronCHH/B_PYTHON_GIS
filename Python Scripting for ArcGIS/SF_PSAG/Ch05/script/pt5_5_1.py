import arcpy

arcpy.env.workspace = "../DATA"
arcpy.env.overwriteOutput = True

arcpy.Clip_analysis("rivers.shp", "basin.shp", "result.shp")

raw_input("done")