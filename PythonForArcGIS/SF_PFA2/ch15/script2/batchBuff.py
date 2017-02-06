# batchBuff.py
# Purpose: Buffer specific sets of feature classes in a workspace.
# Usage: No script arguments needed.
import arcpy, os


# Define the function.
def batchBuffer(workspace, featType, outSuffix, buffDistance):
    '''For a given workspace, buffer each feature class of a given feature type.'''
    arcpy.env.workspace = workspace
    fcs = arcpy.ListFeatureClasses('*', featType)
    for fc in fcs:
        fcParts = os.path.splitext(fc)
        outputName = fcParts[0] + outSuffix + fcParts[1]
        try:
            arcpy.Buffer_analysis(fc, outputName, buffDistance)
            print '{0} created.'.format(outputName)
        except:
            print 'Buffering {0} failed.'.format(fc)

# Call the function.
batchBuffer('ch15/data', 'Polygon', 'Buff', '1 mile')

# Set argument variables.
wSpace = 'ch15/data/tester.gdb'
featureType = 'Point'
outputSuffix = 'Ring'
distance = '0.5 kilometers'

# Call the function again.
batchBuffer(wSpace, featureType, outputSuffix, distance)

# Call the function and get TypeError.
batchBuffer('C:/gispy/data/ch15', 'Polygon', 5, '1 mile')
