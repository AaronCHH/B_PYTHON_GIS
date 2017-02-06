import arcpy

fc = "./DATA.gdb/roads"
cursor = arcpy.da.SearchCursor(fc, ["NAME"])

for row in cursor:
	print "Streetname = {0}".format(row[0])