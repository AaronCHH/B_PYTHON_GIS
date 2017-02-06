# addLengthField.py
# Purpose: Add a field containing polygon lengths to the shapefile.
# Usage: No arguments needed.
import arcpy
arcpy.env.workspace = 'ch06/data'

inputFile = 'special_regions.shp'
fieldName = 'Length'
arcpy.AddField_management(inputFile, fieldName, 'FLOAT')
arcpy.CalculateField_management(inputFile, fieldName, '!shape.length!', 'PYTHON')

print 'done!'