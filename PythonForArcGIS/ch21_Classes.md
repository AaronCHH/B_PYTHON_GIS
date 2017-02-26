
# 21 Classes

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [21 Classes](#21-classes)
  * [21.1 Why Use OOP?](#211-why-use-oop)
  * [21.2 Defining a Class](#212-defining-a-class)
  * [21.3 Object Initialization and Self](#213-object-initialization-and-self)
  * [21.4 Using Class Objects](#214-using-class-objects)
  * [21.5 Where to Define a Class](#215-where-to-define-a-class)
  * [21.6 Classes Within a Separate User-Defined Module](#216-classes-within-a-separate-user-defined-module)
  * [21.7 Discussion](#217-discussion)
  * [21.8 Key Terms](#218-key-terms)
  * [21.9 Exercises](#219-exercises)

<!-- tocstop -->

## 21.1 Why Use OOP?


```python
trailList = [1, 2, 5, 10, 15]
```


```python
trailList.append(16)
trailList
```


```python
trailList.remove(5)
trailList
```


```python
trailVegetation = {1: 'barren', 2: 'some bare ground', 5: 'stunted vegetation', 10: 'barren', 15: 'over-grown'}
```

* **Example 21.1**


```python
# %load ch21/script2/calculateCost.py
def calculateCost(trail_ID, vegetation, length):
    '''Calculate trail maintenance based on
    vegetation and length.'''
    rate = 1000
    if vegetation[trail_ID] == 'barren':
        rate = 800
    elif vegetation[trail_ID] == 'some bare ground':
        rate = 900
    cost = length[trail_ID]*rate
    return cost
```

## 21.2 Defining a Class

```python
class ClassName:
    '''Class docstring.
    '''
    code statement(s)
```

* **Example 21.2: A Trail class, created using the class keyword and indenting all of the contents**


```python
# %load ch21/script2/trailExample.py
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

data = 'ch21/data/trails.txt'

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

```


```python
%run ch21/script2/trailExample.py
```

## 21.3 Object Initialization and Self


```python
myTrail = Trail(1, 2.3, 'barren')
```

## 21.4 Using Class Objects


```python
myTrail2 = Trail(2, 5.0, 'some bare ground')
myTrail2.length
```


```python
myTrail2.vegetation
```


```python
myCost = myTrail2.calculateCost()
myCost
```


```python
myTrail2.length = 2.1
myTrail2.calculateCost()
```

* **Example 21.4: Read a dataset and createTrail objects**


```python
# %load ch21/script2/trailExample.py
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

data = 'ch21/data/trails.txt'

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

```


```python
trailDict.keys()
```


```python
trailDict.values()
```


```python
for t in trailDict.values():
    t.reportInfo()
```


```python
del trailDict[5]
```


```python
# Delete trails whose length exceeds 10 km.
for t in trailDict.values():
    if t.length > 10:
        del trailDict[t.ID]
```

* **functionalTrailDelete.py**


```python
# %load ch21/script2/functionalParcelDelete.py
# functionalParcelDelete.py
parcelList = [1, 2, 5, 10, 15] 
parcelZoning = {1: 'residential', 2: 'commerial', 5: 'industrial', 10: 'residential', 15: 'agricultural'}
parcelPricing = {1: 145000.0, 2: 400000.0, 15: 90005000.0, 10: 900000.0, 5: 8000000.0}

# Determine which parcels to delete.
highCost = []
for k, v in parcelPricing.items():
    if v > 1000000:
        highCost.append(k)
# Delete the high cost parcels and tcorresponding attributes.
for i in highCost:
    parcelList.remove(i)
    del parcelPricing[i]
    del parcelZoning[i]

```


```python
# Increase barren property lengths by $5000.
for t in trailDict.values():
    if t.vegetation == 'barren':
        t.length = t.length + 1.2
```


```python
def calculateCrowding(self, visits, track):
    '''Calculate number of visitors/100 m
    (count double for narrow trails).'''
    if track == 'single':
        val = 2*visits/(self.length*10)
    else:# default unit is square meters
        val = visits/(self.length*10)
    return round(val,2)
```


```python
t = Trail(11, 9.5, 'barren')
t.calculateCrowding(20, 'single')
```


```python
class Trail:
    def__init__(self, tid, length, vegetation, visits = 0):
        '''Initialize trail properties.'''
        self.ID = tid
        self.length = length
        self.vegetation = vegetation
        self.visits = visits
```


```python
t1 = Trail(1, 14.5, 'over-grown')
t2 = Trail(2, 3.4, 'some bare ground', 3.5)
```


```python
t1.visits
t2.visits
```


```python

```

## 21.5 Where to Define a Class

* **Example 21.5: Defi ning a class, creating an object instance, and using the object properties and methods**


```python
# %load ch21/script2/highwayInfo.py
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

```


```python
%run ch21/script2/highwayInfo.py
```


```python
import highwayInfo
myHwy = highwayInfo.Highway('Paci fic Highway', 496, 5)
```


```python
myHwy.report()
```

* **Example 21.6: Calling the Highway class in highwayInfo, from a separate script**


```python
# %load ch21/script2/handleHighways.py
# handleHighways.py
# Purpose: Demonstrates using a class defined in a separate user-defined module.
# Input:  No arguments needed, but highwayInfo.py must be in the same directory.
import highwayInfo
myHwy = highwayInfo.Highway('Pacific Highway', 496, 5)

spdLimit = myHwy.calculateAvgSpeed()
print 'Avg travel speed: {0} km/hr'.format(spdLimit)

orient = myHwy.getOrientation(5)
print 'Orientation: {0}'.format(orient)

```

## 21.6 Classes Within a Separate User-Defined Module

## 21.7 Discussion

## 21.8 Key Terms
* Theclass keyword
* Object-oriented programming
* Functional programming
* A class versus an object instance
* Instantiating an object instance
* Properties
* Methods
* Theself argument
* The ```__init__``` method  

## 21.9 Exercises


```python

```
