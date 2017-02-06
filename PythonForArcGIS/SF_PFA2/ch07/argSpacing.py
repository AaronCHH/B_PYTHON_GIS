# argSpacing.py
# Purpose: Print the number of incoming user arguments
# and the first 2 arguments.
import arcpy

numArgs = arcpy.GetArgumentCount()
print 'Number of user arguments: {0}'.format(numArgs)
print 'The first argument: {0}'.format(arcpy.GetParameterAsText(0))
print 'The second argument: {0}'.format(arcpy.GetParameterAsText(1))
