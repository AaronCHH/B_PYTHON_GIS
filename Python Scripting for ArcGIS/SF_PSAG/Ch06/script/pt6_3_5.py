import arcpy
arcpy.env.workspace = "../DATA.gdb"
element = "roads"
desc = arcpy.Describe(element)
print "Data type: " + desc.dataType 
print "File path: " + desc.path 
print "Catalog path: " + desc.catalogPath 
print "File name: " + desc.file 
print "Base name: " + desc.baseName 
print "Name: " + desc.name 