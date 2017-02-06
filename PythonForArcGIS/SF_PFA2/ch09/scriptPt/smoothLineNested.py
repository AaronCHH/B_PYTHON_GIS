# smoothLineNested.py
# Usage: workspace, features_with_line_geometry
# Example 1: C:/gispy/data/ch09 trails.shp
# Example 2: C:/gispy/data/ch09 park.shp
# Example 3: C:/gispy/data/ch09 getty.tif
import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
outFile = 'scratch/output'
desc = arcpy.Describe(data)

if desc.dataType in ['FeatureClass', 'ShapeFile']:
    if desc.shapeType == 'Polyline':
        result = arcpy.SmoothLine_cartography(data, outFile,
                                              'BEZIER_INTERPOLATION')
        print 'Smooth line created {0}.'.format(result.getOutput(0))
    else:
        print 'Warning: shape type is {0}. Smooth Line only works on Polyline \
shape types. '.format(desc.shapeType)
else:
    print "Warning: Input data type must be 'FeatureClass' or 'ShapeFile'."
    print 'Input dataType:', desc.dataType
