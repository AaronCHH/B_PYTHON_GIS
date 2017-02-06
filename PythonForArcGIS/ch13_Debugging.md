
# 13 Debugging

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [13 Debugging](#13-debugging)
  * [13.1 Syntax Errors](#131-syntax-errors)
    * [buggyCode1.py](#buggycode1py)
  * [13.2 Exceptions](#132-exceptions)
    * [buggyCode2.py](#buggycode2py)
  * [13.3 Logic Errors](#133-logic-errors)
    * [buggyCode3.py](#buggycode3py)
    * [buggyLoop.py](#buggylooppy)
    * [buggyFreq.py](#buggyfreqpy)
  * [13.4 PythonWin Debugging Toolbar](#134-pythonwin-debugging-toolbar)
    * [13.4.1 Using Breakpoints](#1341-using-breakpoints)
  * [13.5 Running in Debug Mode](#135-running-in-debug-mode)
  * [13.6 PyScripter Debugging Toolbar](#136-pyscripter-debugging-toolbar)
  * [13.7 Debugging Tips](#137-debugging-tips)
  * [13.8 Key Terms](#138-key-terms)
  * [13.9 Exercises](#139-exercises)

<!-- tocstop -->

## 13.1 Syntax Errors

### buggyCode1.py


```python
# %load ch13/script2/buggyCode1.py
# buggyCode1.py
import os, sys
outputDir = os.path.dirname(sys.argv[1]) + '\outputFiles/
if not os.path.exists(outputDir :
    os.mkdir(outputDir)

```

## 13.2 Exceptions

### buggyCode2.py


```python
# %load ch13/script2/buggyCode2.py
# buggyCode2.py
import arcpy, sys, os
arcpy.env.workspace = sys.argv[1]
fc = arcpy.ListFeatureClasses()
for fc in fcs:
    # Append Buffer to the output name?
    fcBuffer = os.path.splitext(fc)[0] + 'Buffer.shp'
    # Call buffer tool with required input, output, and distance arguments.
    arcpy.Buffer_analysis(fc, fcBuffer, '1 elephant')

```

## 13.3 Logic Errors

### buggyCode3.py


```python
# %load ch13/script2/buggyCode3.py
# buggyCode3.py
# Purpose: Normalize data time steps.
timeSteps = [2011, 2009, 2008, 2005, 2004, 2003, 2001, 1999]
# Normalize to values between 0 and 1.
maxv = max(timeSteps)
minv = min(timeSteps)
r = maxv - minv
normalizedList = [v - minv/r for v in timeSteps]
print normalizedList
```

    [1845, 1843, 1842, 1839, 1838, 1837, 1835, 1833]



```python
%run ch13/script2/buggyCode3.py
```

    [1845, 1843, 1842, 1839, 1838, 1837, 1835, 1833]



```python
normalizedList = [(v - minv)/r for v in timeSteps]
normalizedList
```




    [1, 0, 0, 0, 0, 0, 0, 0]




```python
normalizedList = [(v - minv)/float(r) for v in timeSteps]
normalizedList
```




    [1.0,
     0.8333333333333334,
     0.75,
     0.5,
     0.4166666666666667,
     0.3333333333333333,
     0.16666666666666666,
     0.0]



### buggyLoop.py


```python
# %load ch13/script2/buggyLoop.py
# buggyLoop.py
# Remove feature classes whose names do not contain the given tag
tag = 'zones'  #'data'
fcs = [u'data1', u'data2', u'data3', u'fireStations',
       u'park_data', u'PTdata4', u'schoolzones',
       u'regions1', u'regions2', u'workzones']

print 'Before loop: {0}'.format(fcs)
for fcName in fcs:
    if tag in fcName:
        fcs.remove(fcName)
print 'After loop: {0}'.format(fcs)


##print 'Before loop: {0}'.format(fcs)
##fcsOut = []
##for fcName in fcs:
##	if tag not in fcName:
##		fcsOut.append(fcName)
##print 'After loop: {0}'.format(fcsOut)

```


```python
%run ch13/script2/buggyLoop.py
```

    Before loop: [u'data1', u'data2', u'data3', u'fireStations', u'park_data', u'PTdata4', u'schoolzones', u'regions1', u'regions2', u'workzones']
    After loop: [u'data1', u'data2', u'data3', u'fireStations', u'park_data', u'PTdata4', u'regions1', u'regions2']


### buggyFreq.py


```python
# %load ch13/script2/buggyFreq.py
# buggyFreq.py
# Purpose: Find frequency of each value in each string field

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch13/smallTest.gdb'
featureList = arcpy.ListFeatureClasses()

for inputFile in featureList:
    fields = arcpy.ListFields(inputFile, '*', 'String')
    for field in fields:
        fieldName = field.name
    outTable = inputFile + fieldName + 'freq'
    arcpy.Frequency_analysis(inputFile, outTable, fieldName)
    print 'Output table created: {0}'.format(outTable)

```


```python

```


```python

```

## 13.4 PythonWin Debugging Toolbar

### 13.4.1 Using Breakpoints

## 13.5 Running in Debug Mode

## 13.6 PyScripter Debugging Toolbar

## 13.7 Debugging Tips

## 13.8 Key Terms

## 13.9 Exercises


```python

```
