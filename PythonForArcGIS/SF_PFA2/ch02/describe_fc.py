# describe_fc.py
# Purpose: Print information about each feature class in a workspace.
# Usage: Workspace
# Example input: C:/gispy/data/ch02
# Output: A list of basic information about each feature class.
# Author: Lou Lou Who 7/20/2055

import arcpy, sys

# GET the input workspace from the user.
arcpy.env.workspace = sys.argv[1]

# GET a list of the feature classes in the workspace.
fcs = arcpy.ListFeatureClasses()

# PRINT basic information about each feature class in the folder.
print 'Feature classes in folder {0}:'.format(arcpy.env.workspace)
for fc in fcs:
    desc = arcpy.Describe(fc)
    print 'Name:        {0}'.format(fc)
    print 'Data type:   {0}'.format(desc.dataType)
    print 'Data class:  {0}'.format(desc.dataSetType)
    print 'Type:        {0}'.format(desc.featureType)
    print 'Shape type:  {0}'.format(desc.shapeType)
    print 'Has M:       {0}'.format(desc.hasM)
    print 'Has Z:       {0}'.format(desc.hasZ)
    print
print 'Feature class list complete.'
