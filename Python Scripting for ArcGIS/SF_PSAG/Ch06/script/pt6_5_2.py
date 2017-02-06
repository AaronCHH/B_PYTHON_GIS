import arcpy
from arcpy import env

env.workspace = "../DATA"
fieldlist = arcpy.ListFields("roads.shp")

for field in fieldlist:
	print "{0} is a type of {1} with a length of {2}".format(field.name, field.type, field.length)
