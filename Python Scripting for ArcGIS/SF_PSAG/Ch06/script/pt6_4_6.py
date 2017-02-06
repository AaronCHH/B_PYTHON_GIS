import arcpy
from arcpy import env

env.workspace = "../DATA"
fieldlist = arcpy.ListFields("roads.shp", "", "String")

for field in fieldlist:
	print field.name + " " + str(field.length) 