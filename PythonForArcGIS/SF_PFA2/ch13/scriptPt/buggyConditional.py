# buggyConditional.py
# Purpose: Calculate the value of a field based on the values of three input parameters.
# Usage: full_path_featureclass_filename Z_value AF_value T_value output_fieldname
# Example input: C:/gispy/data/ch13/tester.gdb/c1 -2 3 6 veld
import arcpy

fc = arcpy.GetParameterAsText(0)
Z = arcpy.GetParameterAsText(1)
AF = arcpy.GetParameterAsText(2)
T = arcpy.GetParameterAsText(3)
outFieldName = arcpy.GetParameterAsText(4)

# Add output field, if it doesn't already exist
fields = arcpy.ListFields(fc)
fieldNames = [field.name for field in fields]
if field.name in fieldNames:
    arcpy.AddField_management(fc, outFieldName)

if (Z > 0) and (AF > 0):
    value = T + Z + AF    # or = sum([T, Z, AF])
elif (Z > 0) and (AF < 0):
    value = T + Z         # or = sum([T, Z ])
elif (Z < 0) and (AF > 0):
    value = T + AF        # or = sum([T, AF])
else:
    value = T

print "Value: {0}".format(value)

# Set the new field to the output value
results = arcpy.CalculateField_management(fc, outFieldName, T)

print results.getMessages()
