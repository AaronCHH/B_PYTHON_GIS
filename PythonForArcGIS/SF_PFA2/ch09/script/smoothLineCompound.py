# smoothLineCompound.py
# Usage: workspace, features_with_line_geometry
# Example 1: C:/gispy/data/ch09 trails.shp
# Example 2: C:/gispy/data/ch09 park.shp

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
outFile = 'C:/gispy/scratch/smoothOut'
desc = arcpy.Describe(data)
if desc.dataType in ['FeatureClass', 'ShapeFile'] and desc.shapeType == 'Polyline':
    result = arcpy.SmoothLine_cartography(data, outFile, \
                                          'BEZIER_INTERPOLATION')
    print 'Smooth line created {0}.'.format(result.getOutput(0))
