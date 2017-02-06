# highwayInfo.py
# Purpose: Define a highway class to be used by other scripts.
#          Demonstrate defining a class within a user-defined module to be
#          called from another script.
# Usage: No arguments required.


class Highway:
    '''Major road.
    Attributes:
        name        None-numerical road name.
        length      Length based on a network dataset.
        travelTime  Estimated time it takes to travel the full length of this highway.
    '''
    def __init__(self, name, length, tTime):
        '''Initialize a Highway object.'''
        self.name = name
        self.length = length
        self.travelTime = tTime

    def calculateAvgSpeed(self):
        '''Calculate the average speed.'''
        avgSpeed = self.length/float(self.travelTime)
        return avgSpeed

    def getOrientation(self, number):
        '''Determine highway orientation based on the hwy number.'''
        if number % 2 == 1:  # If the number is odd...
            orientation = 'NS'
        else:  # Otherwise, the number is even.
            orientation = 'EW'
        return orientation

    def report(self):
        '''Print highway attributes.'''
        print
        print '''{0} Highway
-----------
{1} km long
{2} hours travel time
        '''.format(self.name, self.length, self.travelTime)

if __name__ == "__main__":
    hwy = Highway('Lincoln', 4946, 100)
    spdLimit = hwy.calculateAvgSpeed()
    print 'Avg speed limit: {0} km/hr'.format(spdLimit)
    orient = hwy.getOrientation(30)
    print 'Orientation: {0}'.format(orient)
    hwy.report()

# This code will be executed, even when this module is imported.
favoriteHighway = Highway('Blue Ridge Parkway', 755, 19)
favoriteHighway.report()
