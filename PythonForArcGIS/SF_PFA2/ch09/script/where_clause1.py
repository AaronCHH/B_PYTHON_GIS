# where_clause1.py
# Purpose: Select features with high reclassification numbers.
# Usage: No arguments needed.

import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch09'
inputFile = 'park.shp'
whereClause = 'RECNO >= 400'
arcpy.Select_analysis(inputFile, 'C:/gispy/scratch/out.shp', whereClause)
