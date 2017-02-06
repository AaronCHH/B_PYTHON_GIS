import arcpy

arcpy.env.workspace = "../DATA"
arcpy.env.overwriteOutput = True

infc = "rivers.shp"
clipfc = "basin.shp"
outfc = "rivers_clip.shp"
desc = arcpy.Describe(clipfc)
type = desc.shapeType

if type == "Polygon":
	arcpy.Clip_analysis(infc, clipfc, outfc)
else:
	print "The clip features are not polygon"

raw_input("done")