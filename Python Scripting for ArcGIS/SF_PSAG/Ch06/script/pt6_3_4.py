import arcpy
element = "../DATA.gdb roads"
desc = arcpy.Describe(element)
print "Dataset type: " + desc.datasetType