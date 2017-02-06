import arcpy

fc = "./DATA.gdb/roads"
# cursor = arcpy.da.SearchCursor(fc, ["NAME"])
with arcpy.da.SearchCursor(fc, ["NAME"]) as cursor:
	for row in cursor:
		print "Streetname = {0}".format(row[0])