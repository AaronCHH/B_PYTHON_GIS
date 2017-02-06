# handleHighways.py
# Purpose: Demonstrates using a class defined in a separate user-defined module.
# Input:  No arguments needed, but highwayInfo.py must be in the same directory.
import highwayInfo
myHwy = highwayInfo.Highway('Pacific Highway', 496, 5)

spdLimit = myHwy.calculateAvgSpeed()
print 'Avg travel speed: {0} km/hr'.format(spdLimit)

orient = myHwy.getOrientation(5)
print 'Orientation: {0}'.format(orient)
