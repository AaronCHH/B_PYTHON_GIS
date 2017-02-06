# where_clause2.py
# Purpose: Extract raster features by attributes based on user input.
# Usage: fieldName fieldValue
# Example: COUNT 6000

import arcpy, sys

arcpy.env.workspace = 'C:/gispy/data/ch09'
arcpy.CheckOutExtension('Spatial')

inputRast = 'getty_rast'

fieldName = sys.argv[1]
fieldValue = sys.argv[2]

whereClause = '{0} > {1}'.format(fieldName, fieldValue)

outputRast = arcpy.sa.ExtractByAttributes(inputRast, whereClause)
outputRast.save('C:/gispy/scratch/attextract')
del outputRast
