# combineFields.py
# Purpose: Create a new field that is the sum of two existing fields.
import arcpy, sys

dataset = sys.argv[1]
field1 = sys.argv[2]
field2 = sys.argv[3]
newfield = sys.argv[4]

arcpy.AddField_management(dataset, newfield)
expression = '!{0}!+!{1}!'.format(field1, field2)
arcpy.CalculateField_management(dataset, newfield, expression, 'PYTHON')

arcpy.SetParameterAsText(4, dataset)
