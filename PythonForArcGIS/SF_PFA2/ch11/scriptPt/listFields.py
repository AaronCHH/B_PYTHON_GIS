# listFields.py
# Purpose: List attribute table field properties.
import arcpy
arcpy.env.workspace = 'data'

fields = arcpy.ListFields('park.shp')
for fieldObject in fields:
    print 'Name: {0}'.format(fieldObject.name)
    print 'Length: {0}'.format(fieldObject.length)
    print 'Type: {0}'.format(fieldObject.type)
    print 'Editable: {0}'.format(fieldObject.editable)
    print 'Required: {0}\n'.format(fieldObject.required)
