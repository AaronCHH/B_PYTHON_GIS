import arcpy

arcpy.env.workspace = "../DATA.gdb"
arcpy.env.overwriteOutput = True

arcpy.Buffer_analysis("roads", "buffer", "100 METERS")

raw_input("done")