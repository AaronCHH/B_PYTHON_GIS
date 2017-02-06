# printTableExclude.py
# Purpose: Print the names of the non-geometry non-OID type fields in the
#     input file and the value of these fields for each record.
# Usage: Full path file name
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, sys


def excludeFields(table, types=[]):
    '''Return a list of fields minus those with specified field types'''
    fieldNames = []
    fds = arcpy.ListFields(table)
    for f in fds:
        if f.type not in types:
            fieldNames.append(f.name)
    return fieldNames

fc = sys.argv[1]
excludeTypes = ['Geometry', 'OID']
fields = excludeFields(fc, excludeTypes)

with arcpy.da.SearchCursor(fc, fields) as cursor:
    print cursor.fields
    for row in cursor:
        print row
del cursor
