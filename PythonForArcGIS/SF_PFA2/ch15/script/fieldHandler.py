# fieldHandler.py
# Purpose: Work with field names.
# Usage: No script arguments need.
import arcpy


def getFieldNames(data):
    '''Get a list of field names.'''
    fields = arcpy.ListFields(data)
    fnames = [f.name for f in fields]
    return fnames


def fieldExists(data, name):
    '''Check if a given field name already exists.'''
    fieldNames = getFieldNames(data)
    isThere = name in fieldNames
    return isThere

inputF = 'C:/gispy/data/ch15/park.shp'
names = getFieldNames(inputF)
fieldName = 'COVER'
result = fieldExists(inputF, fieldName)
print 'Does field "{0}" exist? {1}'.format(fieldName, result)
result = fieldExists(inputF, 'Value')
print 'Does field "Value" exist? {0}'.format(result)
