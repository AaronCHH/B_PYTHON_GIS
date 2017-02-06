import arcpy
fc = "../DATA/rivers.shp"
desc = arcpy.Describe(fc)
sr = desc.spatialReference
print "Dataset type: " + desc.datasetType
print "spatial reference: " + sr.name