# Name: avgNearNeighbor.py
# Purpose: Analyze crime data to determine if spatial patterns are
#         statistically significant.

import arcpy

arcpy.env.workspace = 'C:/gispy/data/ch06'

annResult = arcpy.AverageNearestNeighbor_stats('points.shp', 'Euclidean Distance')

print 'Average Nearest Neighbor Output'
print 'Nearest neighbor ratio: {0}'.format(annResult.getOutput(0))
print 'z-score: {0}'.format(annResult.getOutput(1))
print 'p-value: {0}'.format(annResult.getOutput(2))
print 'Expected Mean Distance: {0}'.format(annResult.getOutput(3))
print 'Observed Mean Distance: {0}'.format(annResult.getOutput(4))
