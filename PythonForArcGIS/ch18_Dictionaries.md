# 18 Dictionaries

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [18 Dictionaries](#18-dictionaries)
  * [18.1 Dictionary Terms and Syntax](#181-dictionary-terms-and-syntax)
    * [18.1.1 Access by Key, Not by Index](#1811-access-by-key-not-by-index)
    * [18.1.2 Conditional Construct vs. Dictionary](#1812-conditional-construct-vs-dictionary)
    * [18.1.3 How to Modify: Update/Add/Delete Items](#1813-how-to-modify-updateadddelete-items)
  * [18.2 Dictionary Operations and Methods](#182-dictionary-operations-and-methods)
    * [18.2.1 Does It Have That Key?](#1821-does-it-have-that-key)
    * [18.2.2 Listing Keys, Values, and Items](#1822-listing-keys-values-and-items)
    * [18.2.3 Looping Through Dictionaries](#1823-looping-through-dictionaries)
  * [18.3 Populating a Dictionary](#183-populating-a-dictionary)
    * [18.3.1 Dictionaries and Cursors](#1831-dictionaries-and-cursors)
  * [18.4 Discussion](#184-discussion)
  * [18.5 Key Terms](#185-key-terms)
  * [18.6 Exercises](#186-exercises)

<!-- tocstop -->


## 18.1 Dictionary Terms and Syntax


```python
zipcodeDictionary = {27522 : 'Granville', 28736 : 'Jackson', 27953:'Dare',
                     27511: 'Wake', 27607: 'Wake'}
```


```python
 flickDict = {8.5:1963, 'oceans':[11,12], 'up' : 'dog'}
```


```python
 newVocab = {'mouse potato': 'a frequent computer user',
             'wasband' : 'former husband',
             'himbo': 'an attractive but vacuous man'}
```


```python
type(newVocab)
```




    dict



### 18.1.1 Access by Key, Not by Index


```python
roomDict = {'cslewis': 4139, 'emforste': 4118,
            'jkrowlin': 4098, 'jrtolkie': 4259, 'pgwodeho': 4118,
            'jrtolkie': 4259, 'vmhugo': 2121, 'vwoolf': 3145}
```


```python
roomDict['emforste']
```




    4118




```python
roomDict[1]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-8-9af2b3fb97ec> in <module>()
    ----> 1 roomDict[1]


    KeyError: 1


### 18.1.2 Conditional Construct vs. Dictionary


```python
if num == 0:
    day = 'Monday'
    print 'Weekday: {0}'.format(day)
elif num == 1:
    day = 'Tuesday'
    print 'Weekday: {0}'.format(day)
elif num == 2:
    day = 'Wednesday'
    print 'Weekday: {0}'.format(day)
elif num == 3:
    day = 'Thursday'
    print 'Weekday: {0}'.format(day)
elif num == 4:
    day = 'Friday'
    print 'Weekday: {0}'.format(day)
```

* **Example 18.1 weekdays.py**


```python
# %load ch18/script2/weekdays.py
# weekdays.py
# Purpose: Print the day of the week, based on a number.
#          Contrast using ELIF branching (15 lines of code)
#          with using a dictionary (3 lines of code)
# Usage: Integer between 0 and 4.
# Example 3


import sys
code = int(sys.argv[1])
if code == 0:
    day = 'Monday'
    print 'Weekday: {0}'.format(day)
elif code == 1:
    day = 'Tuesday'
    print 'Weekday: {0}'.format(day)
elif code == 2:
    day = 'Wednesday'
    print 'Weekday: {0}'.format(day)
elif code == 3:
    day = 'Thursday'
    print 'Weekday: {0}'.format(day)
elif code == 4:
    day = 'Friday'
    print 'Weekday: {0}'.format(day)

#################################### Dictionary equivalent

weekdayDict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}

day = weekdayDict[code]
print 'Weekday: {0}'.format(day)

```

### 18.1.3 How to Modify: Update/Add/Delete Items


```python
# Modify the room number for 'emforste'.
roomDict['emforste'] = 4139
roomDict # The dictionary is updated.
len(roomDict)
```


```python
# Add 'lcarroll' in room 2121 to the dictionary.
roomDict['lcarroll'] = 2121
roomDict # A new item is added to the dictionary.
len(roomDict) # The length of the dictionary becomes 8.
```


```python
weather = {'S1' : [15,20],'S2' : [25,30,40]}
```


```python
weather['S3'] = [33,40]
weather
```


```python
weather['S2'].append(36)
weather
```


```python
update = [i + 1for i in weather['S1']]
weather['S1'] = update
weather
```


```python
delroomDict['jrtolkie']
roomDict
```


```python
len(roomDict)
```


```python
del roomDict['cslouis']
```

## 18.2 Dictionary Operations and Methods

### 18.2.1 Does It Have That Key?


```python
'cslewis' in roomDict
```


```python
'cslouis' in roomDict
```


```python
key = 'cslouis'
if key in roomDict:
    print roomDict[key]
else:
    'No {0} key found.'.format(key)
```

### 18.2.2 Listing Keys, Values, and Items


```python
roomDict.keys()
```


```python
roomDict.values()
```


```python
roomDict.items()
```

### 18.2.3 Looping Through Dictionaries


```python
for k in newVocab.keys():
    print k
```


```python
for v in newVocab.values():
    print v
```


```python
for k, v in newVocab.items():
    print k, ':', v
```


```python
for k in weather.keys():
    weather[k].append(0)
weather
```


```python
for v in weather.values():
print sum(v)/len(v),
```


```python
for k, v in roomDict.items():
    room = str(v)
    if room.startswith('4'):
        print'{0}, room {1}'.format(k,v)
```

## 18.3 Populating a Dictionary

* **Example 18.2 healthyLiving.py**


```python
# %load ch18/script2/healthyLiving.py
# healthyLiving.py
# Purpose: Populate a dictionary based on user responses.
#          Inquires about fruit and veg multiple times to
#          but only keeps the last response.
# Usage: No arguments required to start the script running.
choiceList = ['fruit', 'fruit', 'fruit', 'veg', 'veg', 'veg', 'exercise', 'park']
favDict = {}  # Create empty dictionary
for c in choiceList:
    question = "What is your favorite {0}?".format(c)
    answer = raw_input(question)
    favDict[c] = answer  # Add or update item
print 'favDict {0}'.format(favDict)

```

* **Example 18.3 healthyLivingV2.py**


```python
# %load ch18/script2/healthyLivingV2.py
# healthyLivingV2.py
# Purpose: Populate a dictionary based on user responses.
#          Inquires about fruit and veg multiple times to
#          and collects ALL of the responses.
# Usage: No arguments required to start the script running.
choiceList = ['fruit', 'fruit', 'fruit', 'veg', 'veg', 'veg', 'exercise', 'park']
topDict = {}  # Create empty dictionary
for c in choiceList:
    question = "What is your favorite {0}?".format(c)
    answer = raw_input(question)
    if not c in topDict:
        topDict[c] = [answer]  # Add a new item to the dictionary.
    else:
        topDict[c].append(answer)  # Update an item by adding to an item's list.

print 'topDict {0}'.format(topDict)

```

* **Example 18.4 fileDates.py**


```python
# %load ch18/script2/fileDates.py
# fileDates.py
# Purpose: Collect filenames and modification dates in a dictionary.
# Usage: No arguments needed.
import os, time

inputDir = 'data/smallDir'

fileList = os.listdir(inputDir)

fileDict = {}
for f in fileList:
    epochNum = os.path.getmtime(inputDir + '/' + f)
    modTime = time.ctime(epochNum)
    fileDict[f] = modTime

print fileDict

```

### 18.3.1 Dictionaries and Cursors

* **Example 18.5 areaMedian.py**


```python
# %load ch18/script2/areaMedian.py
# areaMedian.py
# Purpose: Find the polygon median area and identify polygons
#          with areas in this range.
# Usage: No arguments needed.
import arcpy, numpy

fc = 'data/parkAreas.shp'
idField = 'FID'
areaField = 'F_AREA'
areasDict = {}

# User search cursor to populate id:area dictionary items.
sc = arcpy.da.SearchCursor(fc, [idField, areaField])
for row in sc:
    id = row[0]
    area = row[1]
    areasDict[id] = area
del sc

# Find the median area.
areas = areasDict.values()
medianArea = numpy.median(areas)
print 'Median area: {0}'.format(medianArea)

# Find the polygons with values close to median.
sqft = 400
print 'Polygons close to median:'
for k, v in areasDict.items():
    if medianArea - sqft < v < medianArea + sqft:
        print '{0}: {1}, {2}: {3}'.format(idField, k, areaField, v)

```

* **Example 18.6 coverMedianArea.py**


```python
# %load ch18/script2/coverMedianArea.py
# coverMedianArea.py
# Purpose: Find the median area of polygons of each cover type.
# Usage: No arguments needed.
import arcpy, numpy

arcpy.env.workspace = 'data'
fc = 'parkAreas.shp'

# Populate the dictionary,
# accumulate a list of areas for each cover type.
d = {}
sc = arcpy.da.SearchCursor(fc, ['COVER', 'F_AREA'])
for row in sc:
    cover = row[0]
    area = row[1]
    if cover in d:
        d[cover].append(area)
    else:
        d[cover] = [area]
del sc

#Calculate the median area for each cover type.
for k, v in d.items():
    median = numpy.median(v)
    print "Polygons with cover '{0}' have median area {1}".format(k, median)


##>>> Polygons with cover woods have median area 83095.3479504
##Polygons with cover other have median area 55491.6260843
##Polygons with cover orch have median area 83477.7527484

```

## 18.4 Discussion


```python

```

## 18.5 Key Terms

* 'dict' data type  
* Key  
* Value  
* Item  
* Access by key vs. indexing multi-way conditional construct  
* Dictionary methods (keys, values, items)  
* numpy module  

## 18.6 Exercises
