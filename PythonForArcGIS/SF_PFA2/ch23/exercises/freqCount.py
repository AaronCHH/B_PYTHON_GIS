# freqCount.py
# Purpose: Count the number of occurrances of a given value within a field.
# Input: data_file fieldname field_value
# Sample input: C:/gispy/data/ch23/tester.gdb/park COVER woods
import arcpy, sys, traceback


def printArc(message):
    print message
    arcpy.AddMessage(message)

# Check incoming arguments.
for index, value in enumerate(sys.argv):
    m = 'Arg {0} = {1}'.format(index, value)
    print m
print

# Set input variables.
datafile = sys.argv[1]
fieldname = sys.argv[2]
fieldvalue = sys.argv[3]

# Get count.
whereClause = "{0} = \'{1}\'".format(fieldname, fieldvalue)
try:
    sc = arcpy.da.SearchCursor(datafile, [fieldname], whereClause)
    count = 0
    for row in sc:
        count = count + 1
    del sc
    # Print results.
    m = 'The {0} field in {1} contains {2} occurances of {3}.'.format(
        fieldname, datafile, count, fieldvalue)
    print m
except:
    print 'An error occurred.'
    traceback.print_exc()
    del sc
