# addLengthField.py
# Purpose: Add a field containing polygon lengths to the shapefile.
# Usage: No arguments needed.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch06'

inputFile = 'special_regionsCopy.shp'
fieldName = 'Length'
arcpy.AddField_management(inputFile, fieldName, 'FLOAT')
arcpy.CalculateField_management(inputFile, fieldName, '!shape.length!', 'PYTHON')
