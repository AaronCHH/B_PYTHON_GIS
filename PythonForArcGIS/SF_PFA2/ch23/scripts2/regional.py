# regional.py
# Purpose: Print the names of states in the input region.
# Usage: region
# Example input: Mountain

import arcpy, reportSTargs, sys

region = sys.argv[1]

inf = 'C:/gispy/data/ch23/USA/USA_States_Generalized.shp'

fields = ['SUB_REGION', 'STATE_NAME']

sc = arcpy.da.SearchCursor(inf, fields)

reportSTargs.printArc('\n--States in {0}--'.format(region))

for row in sc:
    if row[0] == region:
        reportSTargs.printArc(row[1])

reportSTargs.printArc('\n')
del sc
