
# 15 User-Defined Functions

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [15 User-Defined Functions](#15-user-defined-functions)
  * [15.1 A Word About Function Words](#151-a-word-about-function-words)
    * [15.1.1 How It Works](#1511-how-it-works)
    * [15.1.2 The Docstring](#1512-the-docstring)
  * [15.2 Custom Functions with Arguments](#152-custom-functions-with-arguments)
    * [15.2.1 Script Arguments vs. Functions Arguments](#1521-script-arguments-vs-functions-arguments)
    * [15.2.2 Optional Arguments](#1522-optional-arguments)
  * [15.3 Returning Values](#153-returning-values)
    * [15.3.1 A Common Mistake: Where Did the None Come from?](#1531-a-common-mistake-where-did-the-none-come-from)
    * [15.3.2 Returning Multiple Values](#1532-returning-multiple-values)
  * [15.4 When to Write Functions](#154-when-to-write-functions)
    * [15.4.1 Where to Defi ne](#1541-where-to-defi-ne)
  * [15.5 Variables Inside and Outside of Functions](#155-variables-inside-and-outside-of-functions)
    * [15.5.1 Mutable Arguments Can Change](#1551-mutable-arguments-can-change)
    * [15.5.2 Pass in Outside Variables](#1552-pass-in-outside-variables)
  * [15.6 Key Terms](#156-key-terms)
  * [15.7 Exercises](#157-exercises)

<!-- tocstop -->

## 15.1 A Word About Function Words


```python
def printBird():
    print"""
    ,,, ::.
    <*~) ;;
    ( @}//
    ''
    """
```


```python
printBird()
```


        ,,, ::.
        <*~) ;;
        ( @}//
        ''



* **Example 15.1 reportArgs.py**  


```python
# %load ch15/script2/reportArgs.py
# reportArgs.py
# Purpose: Print the script arguments.
import sys


def printArgs():
    '''Print user arguments.'''
    for index, arg in enumerate(sys.argv):
        print 'Argument {0}: {1}'.format(index, arg)

printArgs()

```


```python
%run ch15/script2/reportArgs.py
```

    Argument 0: ch15/script2/reportArgs.py


### 15.1.1 How It Works

### 15.1.2 The Docstring


```python
help(printArgs)
```

    Help on function printArgs in module __main__:

    printArgs()
        Print user arguments.



## 15.2 Custom Functions with Arguments

* **Example 15.2 deleteFCS.py**  


```python
# %load ch15/script2/deleteFCS.py
# deleteFCS.py
# Purpose: Clear workspace of unwanted files.
# Usage: No arguments needed.
import arcpy

arcpy.env.workspace = 'ch15/scratch'


def delBuffFCS():
    '''Delete feature classes with names containing "Buff".'''
    fcs = arcpy.ListFeatureClasses('*Buff*')
    for fc in fcs:
        arcpy.Delete_management(fc)
        print '{0} deleted.'.format(fc)


def delNamedFCS(delString):
    '''Delete feature classes with names containing delString.'''
    wildcard = '*{0}*'.format(delString)
    fcs = arcpy.ListFeatureClasses(wildcard)
    for fc in fcs:
        arcpy.Delete_management(fc)
        print '{0} deleted.'.format(fc)

delBuffFCS()
delNamedFCS('Out')

```


```python
%run ch15/script2/deleteFCS.py
```

****excerpt from batchBuff.py**  **


```python
# %load ch15/script2/batchBuff.py
# batchBuff.py
# Purpose: Buffer specific sets of feature classes in a workspace.
# Usage: No script arguments needed.
import arcpy, os


# Define the function.
def batchBuffer(workspace, featType, outSuffix, buffDistance):
    '''For a given workspace, buffer each feature class of a given feature type.'''
    arcpy.env.workspace = workspace
    fcs = arcpy.ListFeatureClasses('*', featType)
    for fc in fcs:
        fcParts = os.path.splitext(fc)
        outputName = fcParts[0] + outSuffix + fcParts[1]
        try:
            arcpy.Buffer_analysis(fc, outputName, buffDistance)
            print '{0} created.'.format(outputName)
        except:
            print 'Buffering {0} failed.'.format(fc)

# Call the function.
batchBuffer('ch15/data', 'Polygon', 'Buff', '1 mile')

# Set argument variables.
wSpace = 'ch15/data/tester.gdb'
featureType = 'Point'
outputSuffix = 'Ring'
distance = '0.5 kilometers'

# Call the function again.
batchBuffer(wSpace, featureType, outputSuffix, distance)

# Call the function and get TypeError.
batchBuffer('C:/gispy/data/ch15', 'Polygon', 5, '1 mile')

```


```python
%run ch15/script2/batchBuff.py
```


```python
batchBuffer('ch15/data', 'Polygon', 'Buff', '1 mile')
```

    Buffering park.shp failed.
    Buffering parkBuff.shp failed.
    Buffering parkBuffBuff.shp failed.
    parkBuffBuffBuffBuff.shp created.



```python
batchBuffer('ch15/data', 'Polygon', 'Buff')
```


```python
wSpace = 'ch15/data/tester.gdb'
featureType = 'Point'
outputSuffix = 'Ring'
distance = '0.5 kilometers'
batchBuffer(wSpace, featureType, outputSuffix, distance)
```

    Buffering c1 failed.
    Buffering c2 failed.
    Buffering data1 failed.
    Buffering data2 failed.
    Buffering data3 failed.
    Buffering fireStations failed.
    Buffering ptdata4 failed.
    Buffering sample failed.
    Buffering scatter failed.
    Buffering schools failed.
    Buffering shp failed.
    Buffering intersectOut failed.
    Buffering intersectOutput failed.



```python

```

### 15.2.1 Script Arguments vs. Functions Arguments

* **Example 15.3 setEnv1.py**  


```python
# %load ch15/script2/setEnv1.py
# setEnv1.py
# Purpose: Set arcpy environment properties.
# Usage: No script arguments needed.
import arcpy


def setEnviron1():
    '''Set arcpy workspace and overwriteOutput properties
    to hard-coded values.'''
    arcpy.env.workspace = 'C:/gispy/data/ch15'
    arcpy.env.overwriteOutput = True
setEnviron1()

```


```python
# %load ch15/script2/setEnv2.py
# setEnv2.py
# Purpose: Set arcpy environment properties.
# Usage: No script arguments needed.
import arcpy


def setEnviron2(workspace, overwriteVal):
    '''Set arcpy workspace and overwriteOutput properties
    based on function arguments.'''
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = overwriteVal

wSpace = 'C:/gispy/data/ch15/tester.gdb'
overwrite = False
setEnviron2(wSpace, overwrite)

```


```python
# %load ch15/script2/setEnv3.py
# setEnv3.py
# Purpose: Set arcpy environment properties.
# Usage: workspace overwrite_output_value
# Example input: C:/gispy/data/ch15/scratch True
import arcpy, sys

wSpace = sys.argv[1]
overwrite = sys.argv[2]


def setEnviron3(workspace, overwriteVal):
    '''Set arcpy workspace and overwriteOutput properties
    based on function arguments.'''
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = overwriteVal

setEnviron3(wSpace, overwrite)

```

### 15.2.2 Optional Arguments


```python
def setEnviron4(workspace, overwriteVal = True):
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = overwriteVal
```


```python
setEnviron4('ch15/data', False)
```


```python
setEnviron4('ch15/data')
```


```python

```

## 15.3 Returning Values

* **excerpt from fieldHandler.py**


```python
# %load ch15/script2/fieldHandler.py
# fieldHandler.py
# Purpose: Work with field names.
# Usage: No script arguments need.
import arcpy


def getFieldNames(data):
    '''Get a list of field names.'''
    fields = arcpy.ListFields(data)
    fnames = [f.name for f in fields]
    return fnames


def fieldExists(data, name):
    '''Check if a given field name already exists.'''
    fieldNames = getFieldNames(data)
    isThere = name in fieldNames
    return isThere

inputF = 'C:/gispy/data/ch15/park.shp'
names = getFieldNames(inputF)
fieldName = 'COVER'
result = fieldExists(inputF, fieldName)
print 'Does field "{0}" exist? {1}'.format(fieldName, result)
result = fieldExists(inputF, 'Value')
print 'Does field "Value" exist? {0}'.format(result)

```


```python
names = getFieldNames('C:/gispy/data/ch15/park.shp')
```


```python
names
```


```python
def fieldExists(data, name):
    '''Check if a given field name already exists.'''
    fieldNames = getFieldNames(data)
    isThere = name in fieldNames
    return isThere
```


```python
result = fieldExists('C:/gispy/data/ch15/park.shp', 'COVER')
result
```

* **Example 15.4 oops.py**  


```python
# %load ch15/script2/oops.py
# oops.py
# Purpose: Count the number records in an intersections
#             between two datasets and delete the intersection file
#             (but the intersection output is not deleted since this line
#              of code is placed after the 'return' statement).
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch15/tester.gdb'
arcpy.env.overwriteOutput = True


def countIntersection(dataList):
    '''Calculate the number of features in the intersection.'''
    tempData = 'intersectOut'
    arcpy.Intersect_analysis(dataList, tempData)
    res = arcpy.GetCount_management(tempData)
    print '{0} created.'.format(tempData)
    return int(res.getOutput(0))
    # uh-oh! The delection is not going to happen.
    arcpy.Delete_management(tempData)
    print '{0} deleted.'.format(tempData)

inputData = ['schools', 'workzones']
count = countIntersection(inputData)
print 'There are {0} intersections.'.format(count)

```

* **Example 15.5 age.py**  


```python
# %load ch15/script2/age.py
# age.py
# Purpose: Calculate age.
# Usage: No script arguments needed.
import datetime


def calculateAge(yr, mo, day):
    '''Calculate age based on the given birth date.'''
    # Get datetime objects for birth date and today
    born = datetime.date(yr, mo, day)
    today = datetime.date.today()
    # Get this year's birthday and handle leap year exceptions
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day-1)
    # Return age
    if birthday < today:
        return today.year - born.year
    else:
        return today.year - born.year - 1

print calculateAge(2012, 4, 20)

```


```python
# Return age
if birthday < today:
    age = today.year - born.year
else:
    age = today.year - born.year - 1
return age
```

### 15.3.1 A Common Mistake: Where Did the None Come from?

* **except from returnVSprint.py**  


```python
# %load ch15/script2/returnVSprint.py
# returnVSprint.py
# Purpose: Demonstrate that the default return value is 'None'.
# Usage: No script arguments needed.


def positiveMinV1(numList):
    '''Find the minimum positive number in the list'''
    pos = []
    for val in numList:
        if val >= 0:
            pos.append(val)
    positiveMin = min(pos)
    print 'Min positive number = {0}'.format(positiveMin)

theList = [8, 2.5, 0, 12, 5]
print 'Run function 1...'
value = positiveMinV1(theList)
print 'positiveMinV1 returned: {0}'.format(value)


def positiveMinV2(numList):
    pos = []
    for val in numList:
        if val >= 0:
            pos.append(val)
    return min(pos)
print 'Run function 2...'
value = positiveMin(theList)
print 'positiveMinV2 returned: {0}'.format(value)

```


```python
def positiveMinV2(numList):
    '''Find the minimum positive number in the list'''
    pos = []
    for val in numList:
        if val >= 0:
            pos.append(val)
            return min(pos)
```

### 15.3.2 Returning Multiple Values

* **excerpt from returnMultVals.py**


```python
# %load ch15/script2/returnMultVals.py
# returnMultVals.py
# Purpose: Find the midpoints of two line segments.
# Usage: No arguments needed.


def midPoint(x1, y1, x2, y2):
    '''Calculate the midpoint of line segment (x1,y1), (x2,y2).'''
    xVal = (x1 + x2)/2.0
    yVal = (y1 + y2)/2.0
    return xVal, yVal
# Find the midpoint of the line from (3,5) to (2,1).
# Capture the return values with two variables.
x, y = midPoint(3, 5, 2, 1)
print 'Midpoint of line segment (3,5),(2,1):'
print 'x = {0}'.format(x)
print 'y = {0}'.format(y)

# Find the midpoint of the line from (1,1) to (3,5).
# Capture the return values with one variable.
t = midPoint(1, 1, 3, 5)
print 'Midpoint of line segment (1,1),(3,5):'
print 'x = {0}'.format(t[0])
print 'y = {0}'.format(t[1])

```

* **Example 15.6 walkCount.py**  


```python
# %load ch15/script2/walkCount.py
# walkCount.py
# Purpose: Walk and get the record count for each file, where possible.
# Usage: input_directory
# Example input: C:/gispy/data/ch15
import arcpy, datetime, sys
mydir = sys.argv[1]


def diffTime(start, end):
    '''Calculate the difference between two datetime objects'''
    difference = end - start
    weeks, days = divmod(difference.days, 7)
    minutes, seconds = divmod(difference.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return weeks, days, hours, minutes, seconds

before = datetime.datetime.now()
for root, dirs, files in arcpy.da.Walk(mydir):
    for f in files:
        try:
            count = arcpy.GetCount_management(root + "/" + f)
            print '{0}/{1}  Count = {2}'.format(root, f, count)
        except arcpy.ExecuteError:
            print arcpy.GetMessages()

after = datetime.datetime.now()

t = diffTime(before, after)

print 'Time elapsed: {0} weeks, {1} days, {2}:{3}:{4}'.format(t[0], t[1], t[2], t[3], t[4])

```

## 15.4 When to Write Functions

* **scriptWithoutFunction.py**  


```python
# %load ch15/script2/scriptWithOutFunction.py
# scriptWithFunction.py
# Purpose: Call three tools (to find avg. nearest neighbor, intersection, and get count)
#          Print the results from avg. nearest neighbor and get count without using a function.
# Usage: No script arguments needed.

import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch15/tester.gdb'
arcpy.env.overwriteOutput = True

res = arcpy.AverageNearestNeighbor_stats('schools')
resList = res.getMessages().split('\n')
for message in resList:
    if '...' not in message and 'Time:' not in message:
        print message

arcpy.Intersect_analysis(['schools', 'workzones'], 'intersectOutput')

res = arcpy.GetCount_management('intersectOutput')
resList = res.getMessages().split('\n')
for message in resList:
    if '...' not in message and 'Time:' not in message:
        print message

```

* **Example 15.7 scriptWithFunction.py**  


```python
# %load ch15/script2/scriptWithFunction.py
# scriptWithFunction.py (compare to scriptWithoutFunction.py)
# Purpose: Call three tools (to find avg. nearest neighbor, intersection, and get count)
#          Print the results from avg. nearest neighbor and get count using a function.
# Usage: No script arguments needed.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch15/tester.gdb'
arcpy.env.overwriteOutput = True


def reportResults(resultObj):
    '''Print selected result messages.'''
    resList = resultObj.getMessages().split('\n')
    arcpy.env.overwriteOutput = True
    for message in resList:
        if '...' not in message and 'Time:' not in message:
            print message

res = arcpy.AverageNearestNeighbor_stats('schools')
reportResults(res)  # Call the function.

arcpy.Intersect_analysis(['schools', 'workzones'], 'intersectOutput')

res = arcpy.GetCount_management('intersectOutput')
reportResults(res)  # Call the function.

```


```python

```

### 15.4.1 Where to Defi ne

## 15.5 Variables Inside and Outside of Functions

### 15.5.1 Mutable Arguments Can Change


```python
myList = ['a','b','c']
myList[0] = 'z'
myList
```




    ['z', 'b', 'c']




```python
myList.sort()
```


```python
myStr = 'abc'
myStr[0] = 'z'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-34-018bf378477a> in <module>()
          1 myStr = 'abc'
    ----> 2 myStr[0] = 'z'


    TypeError: 'str' object does not support item assignment



```python
myStr.replace('a','z')
```




    'zbc'




```python
myStr
```




    'abc'




```python
def augment(myList, myInt):
    myList.append('some value')
    myInt = myInt + 1
```


```python
aList = ['first entry']
num = 5
print aList
```

    ['first entry']



```python
print num
```

    5



```python
augment(aList, num)
```


```python
print aList
```

    ['first entry', 'some value']



```python
print num
```

    5



```python
def augmentList(list1):
    list2 = list(list1)
    list2.append('some value')
    return list2
```


```python
aList = ['first entry']
result = augmentList(aList)
```


```python
print aList
```

    ['first entry']



```python
print result
```

    ['first entry', 'some value']


### 15.5.2 Pass in Outside Variables

* **Example 15.8 passVars.py**  


```python
# %load ch15/script2/passVars.py
# passVars.py
# Purpose: Demonstrate 'UnboundLocalError'.
# Usage: No script arguments needed.
x = 5


def addOne():
    '''Add one to x and print x.'''
    x = x + 1
    print 'In here', x

print 'Out here', x
addOne()
```


```python
def appendNext():
    maxVal = max(myList)
    maxVal = maxVal + 1
    myList.append(maxVal)
    myList = [1,2,3]
    appendNext()
```


```python
myList
```




    ['b', 'c', 'z']



## 15.6 Key Terms

## 15.7 Exercises


```python

```
