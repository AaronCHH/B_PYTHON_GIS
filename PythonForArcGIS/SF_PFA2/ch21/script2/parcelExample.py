# parcelExample.py
# Purpose: Create a Parcel class and use it to store and
#          explore a land parcel dataset ('land.txt').
# Usage: No arguments required.  Data full path is hard-coded.


class Parcel:
    '''Real estate plot.
    Attributes:
        ID      A unique identifier
        value   Estimated market value
        zoning  Permitted land use
    '''
    def __init__(self, pid, value, zoning):
        '''Initialize parcel properties.'''
        self.ID = pid
        self.value = value
        self.zoning = zoning

    def calculateTax(self):
        '''Calculate the taxes for a parcel based on zoning and property value.'''
        rate = 0.076
        if self.zoning == 'residential':
            rate = 0.075
        elif self.zoning == 'industrial':
            rate = 0.77
        tax = self.value*rate
        return tax

    def reportInfo(self):
        '''Print parcel properties.'''
        print 'ID: {0}'.format(self.ID)
        print 'Value: {0}'.format(self.value)
        print 'Zoning: {0}'.format(self.zoning)

##    def unitValue(self, area, unit):
##        '''Calculate the cost per acre.'''
##        if unit == 'acres':
##            val = self.value/area
##        else: # default unit is square meters
##            val = (self.value*4046.86)/area
##        return round(val,2)

data = 'C:/gispy/data/ch21/land.txt'

parcelDict = {}
with open(data, 'r') as f:
    # Read each line.
    for line in f:
        # Strip the \n from the end and split the line.
        line = line.strip()
        lineList = line.split(',')
        parcID = int(lineList[0])
        val = float(lineList[1])
        zoning = lineList[2]
        # Create a Parcel object.
        theParcel = Parcel(parcID, val, zoning)
        # Add the Parcel object to the dictionary.
        parcelDict[parcID] = theParcel

print 'The dictionary keys are parcel ids:'
print parcelDict.keys()

print '\nThe dictionary values are objects:'
print parcelDict.values()

print '\nThe reportInfo method prints the object properties'
for p in parcelDict.values():
    p.reportInfo()

print '\nDelete an entry based on its key:'
del parcelDict[5]
for p in parcelDict.values():
    p.reportInfo()

print '\nModify entries based on a property:'
# Increase residential property values by $5000.
for p in parcelDict.values():
    if p.zoning == 'residential':
        p.value = p.value + 5000
for p in parcelDict.values():
    p.reportInfo()
print

print 'Delete entries based on a property:'
# Delete parcels whose value exceeds a million.
for p in parcelDict.values():
    if p.value > 1000000:
        del parcelDict[p.ID]
for p in parcelDict.values():
    p.reportInfo()
