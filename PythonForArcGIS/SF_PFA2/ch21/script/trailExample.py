# trailExample.py
# Purpose: Create a Trail class and use it to store and
#          explore a land trail dataset ('trails.txt').
# Usage: No arguments required.  Data full path is hard-coded.


class Trail:
    '''Pedestrian path.

       Attributes:
         ID      A unique identifier
         length:  Estimated trail length
         vegetation: Plant growth on the trail
    '''
    def __init__(self, tid, theLength, theVegetation):
        '''Initialize trail properties.'''
        self.ID = tid
        self.length = theLength
        self.vegetation = theVegetation

    def calculateCost(self):
        '''Calculate maintenance costs based on vegetation and length.'''
        rate = 1000
        if self.vegetation == 'barren':
            rate = 800
        elif self.vegetation == 'some bare ground':
            rate = 900
        cost = self.length*rate
        return cost

    def reportInfo(self):
        '''Print trail properties'''
        print 'ID: {0}'.format(self.ID)
        print 'Length: {0}'.format(self.length)
        print 'Vegetation: {0}'.format(self.vegetation)

    def calculateCrowding(self, visits, track):
        '''Calculate number of visitors/100 m (count double for narrow trails)'''
        if track == 'single':
            val = 2*visits/(self.length*10)
        else:  # The default unit is square meters.
            val = visits/(self.length*10)
        return round(val, 2)

data = 'C:/gispy/data/ch21/trails.txt'

trailDict = {}
with open(data, 'r') as f:
    # Read each line.
    for line in f:
        # Strip the \n from the end and split the line.
        line = line.strip()
        lineList = line.split(',')
        tID = int(lineList[0])
        tLength = float(lineList[1])
        tVeg = lineList[2]
        # Create a trail object.
        theTrail = Trail(tID, tLength, tVeg)
        # Add the trail object to the dictionary.
        trailDict[tID] = theTrail

print 'The dictionary keys are trail ids:'
print trailDict.keys()

print '\nThe dictionary values are objects:'
print trailDict.values()

print '\nThe reportInfo method prints the object properties'
for t in trailDict.values():
    t.reportInfo()

print '\nDelete an entry based on its key:'
del trailDict[5]
for t in trailDict.values():
    t.reportInfo()

print '\nModify entries based on a property:'
# Increase trail length by 1.2km.
for t in trailDict.values():
    if t.vegetation == 'barren':
        t.length = t.length + 1.2
for t in trailDict.values():
    t.reportInfo()
print

print 'Delete entries based on a property:'
# Delete trails whose length exceeds 10 km.
for t in trailDict.values():
    if t.length > 10:
        del trailDict[t.ID]
for t in trailDict.values():
    t.reportInfo()
