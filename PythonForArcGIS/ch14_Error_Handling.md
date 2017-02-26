
# 14 Error Handling

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [14 Error Handling](#14-error-handling)
    * [multRast.py](#multrastpy)
  * [14.1 try/except Structures](#141-tryexcept-structures)
    * [doubleMyNumber.py](#doublemynumberpy)
    * [14.1.1 Using Named Exceptions](#1411-using-named-exceptions)
    * [14.1.2 Multiple except Blocks](#1412-multiple-except-blocks)
    * [14.1.3 Error Handling Gotcha](#1413-error-handling-gotcha)
  * [14.2 Geoprocessing and Error Handling](#142-geoprocessing-and-error-handling)
    * [14.2.1 Getting Geoprocessing Messages](#1421-getting-geoprocessing-messages)
    * [14.2.2 The arcpy Named Exception](#1422-the-arcpy-named-exception)
  * [14.3 Catching Exceptions in Loops](#143-catching-exceptions-in-loops)
  * [14.4 Discussion](#144-discussion)
  * [14.5 Key Terms](#145-key-terms)
  * [14.6 Exercises](#146-exercises)

<!-- tocstop -->

### multRast.py


```python
# %load ch14/script2/multRasts.py
# multRast.py
# Purpose: Multiply each raster in a database by an input factor.
# Usage: numeric_value
# Example input: 5
import arcpy, sys

# Set multiplication factor
factor = float(sys.argv[1])

arcpy.env.overwriteOutput = True
arcpy.env.worspace = 'C:/gispy/data/ch14/rastTester.gdb'
arcpy.CheckOutExtension('Spatial')
outDir = 'C:/gispy/scratch/'

# Get raster list & multiply each by a factor
rasterList = arcpy.ListRasters()
for rasterImage in rasterList:
    rasterObj = arcpy.Raster(rasterImage)
    rastMult = rasterObj * factor
    rastMult.save(outDir + rasterImage)
    del rastMult

```

## 14.1 try/except Structures

### doubleMyNumber.py


```python
# %load ch14/script2/doubleMyNumber.py
# doubleMyNumber.py
# Purpose: Multiply input by 2.
# Usage: numeric_value
# Example input: 5
import sys

try:
    number = float(sys.argv[1])
    product = 2*number
    print 'The doubled number is {0}'.format(product)
except:
    print 'An error occurred.'
    print 'Please enter a numerical argument.'

print 'Good bye!'

```

### 14.1.1 Using Named Exceptions

* **doubleMyNumberV2.py**


```python
# %load ch14/script2/doubleMyNumberV2.py
# doubleMyNumberV2.py
# Purpose: Multiply input by 2
#          or catch value error.
# Usage: numeric_value
# Example input: 5
import sys

try:
    number = float(sys.argv[1])
    product = 2*number
    print 'The doubled number is {0}'.format(product)
except ValueError:
    print 'Input must be numerical.'
print 'Good bye!'

```

### 14.1.2 Multiple except Blocks

* **slopeTry.py**


```python
# %load ch14/script2/slopeTry.py
# slopeTry.py
# Purpose: Find the slope, given rise and run.
# Usage: slope_rise slope_run
# Example input: 1 3
import sys

rise = sys.argv[1]
run = sys.argv[2]

try:
    print 'Rise: {0} Run: {1}'.format(rise, run)
    slope = float(rise)/float(run)
    print 'Slope = rise/run'
except ZeroDivisionError:
    slope = 'Undefined (line is vertical)'
except ValueError:
    print 'Usage: <numeric rise> <numeric run>'
    slope = 'Not found'

print 'Slope:', slope

```

### 14.1.3 Error Handling Gotcha

* **cubeMyNumber.py**


```python
# %load ch14/script2/cubeMyNumber.py
# cubeMyNumber.py
# Purpose: Cube input value.
# Usage: numeric_value
# Example input: 5
import sys
try:
    number = float(sys.argv[1])
    cube = number**3
    print 'The cubed number is {0}'.format()  # missing arg
except:
    print 'Input must be numerical.'
print 'Good bye!'

```

* **cubeMyNumberV2.py**


```python
# %load ch14/script2/cubeMyNumberV2.py
# cubeMyNumberV2.py
# Purpose: Cube input value
#   or print traceback message.
# Usage: numeric_value
# Example input: 5
import sys, traceback
try:
    number = float(sys.argv[1])
    cube = number**3
    print 'The cubed number is {0}'.format()  # missing arg
except:
    print 'Input must be numerical.'
    traceback.print_exc()
print 'Good bye!'

```

## 14.2 Geoprocessing and Error Handling

### 14.2.1 Getting Geoprocessing Messages


```python
import arcpy
arcpy.env.overwriteOutput = True
arcpy.GetMessages()
```




    u'Executing: Buffer ch14/data/parkLines.shp ch14\\scratch\\buffer.shp "1 Miles" FULL ROUND NONE #\nStart Time: Fri Nov 25 00:34:00 2016\nFailed to execute. Parameters are not valid.\nERROR 000725: Output Feature Class: Dataset ch14\\scratch\\buffer.shp already exists.\nFailed to execute (Buffer).\nFailed at Fri Nov 25 00:34:00 2016 (Elapsed Time: 0.00 seconds)'




```python
inputFile = 'ch14/data/cover.shp'
count = arcpy.GetCount_management(inputFile)
print arcpy.GetMessages()
```

    Executing: GetCount ch14/data/cover.shp
    Start Time: Fri Nov 25 00:34:28 2016
    Row Count = 426
    Succeeded at Fri Nov 25 00:34:28 2016 (Elapsed Time: 0.00 seconds)



```python
inputFile = 'ch14/data/parkLines.shp'
outputFile = 'ch14/scratch/buffer.shp'
arcpy.Buffer_analysis(inputFile, outputFile, '1 mile')
print arcpy.GetMessages()
```

    Executing: Buffer ch14/data/parkLines.shp ch14\scratch\buffer.shp "1 Miles" FULL ROUND NONE #
    Start Time: Fri Nov 25 00:34:28 2016
    Succeeded at Fri Nov 25 00:34:28 2016 (Elapsed Time: 0.00 seconds)



```python
print arcpy.GetMessage(0)
```

    Executing: Buffer ch14/data/parkLines.shp ch14\scratch\buffer.shp "1 Miles" FULL ROUND NONE #



```python
arcpy.GetMessageCount()
```




    3




```python
print arcpy.GetMessage(arcpy.GetMessageCount() - 1)
```

    Succeeded at Fri Nov 25 00:34:28 2016 (Elapsed Time: 0.00 seconds)



```python
count = arcpy.GetCount_management()
```


```python
print arcpy.GetMessages()
```

    Executing: GetCount #
    Start Time: Fri Nov 25 00:35:02 2016
    Failed to execute. Parameters are not valid.
    ERROR 000735: Input Rows: Value is required
    Failed to execute (GetCount).
    Failed at Fri Nov 25 00:35:02 2016 (Elapsed Time: 0.00 seconds)


### 14.2.2 The arcpy Named Exception

* **Example 14.1 bufferTry.py**


```python
# %load ch14/script2/bufferTry.py
# bufferTry.py
# Purpose: Buffer the input dataset.
# Usage: Fullpath_filename outDir
# Example input: C:/gispy/data/ch14/parkLines.shp outputWorkspace
import arcpy, sys, os
arcpy.env.overwriteOutput = True
try:
    inFile = sys.argv[1]
    outDir = sys.argv[2]
    buffer = outDir + '/' + os.path.splitext(inFile)[0] + 'Buff.shp'
    arcpy.Buffer_analysis(inFile, buffer, '1 mile')
    print '{0} created.'.format(buffer)
except arcpy.ExecuteError:
    print arcpy.GetMessages()
except IndexError:
    print 'Usage: <full path shapefile name>'

```

## 14.3 Catching Exceptions in Loops

* *Example 14.2 bufferLoopTry.py**


```python
# %load ch14/script2/buffeLoopTry.py
# bufferLoopTry.py
# Purpose: Buffer the feature classes in a workspace.
# Usage: No arguments needed.
import arcpy, os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'ch14/data'
outDir = 'ch14/scratch/'
fcs = arcpy.ListFeatureClasses()
distance = '500 meters'

for fc in fcs:
    outFile = outDir + os.path.splitext(fc)[0] + 'Buff.shp'
    try:
        arcpy.Buffer_analysis(fc, outFile, distance)
        print 'Created: {0}'.format(outFile)
    except arcpy.ExecuteError:
        print arcpy.GetMessage(2)

```


```python
%run ch14/script2/buffeLoopTry.py
```

    Created: ch14/scratch/bufferBuff.shp
    Created: ch14/scratch/coverBuff.shp
    ERROR 000229: Cannot open ch14/data\dummyFile.shp
    Created: ch14/scratch/firesBuff.shp
    Created: ch14/scratch/no_damageBuff.shp
    Created: ch14/scratch/parkLinesBuff.shp


* *Example 14.3 bufferLoopDistTry.py**


```python
# %load ch14/script2/bufferLoopDistTry.py
# bufferLoopDistTry.py
# Purpose: Buffer the input file by the given distance.
# Usage: input_filename numeric_distance (using the default unit of measure)
# Example input: C:/gispy/data/ch14/cover.shp 3

import arcpy, sys, os
arcpy.env.workspace = os.path.dirname(sys.argv[1])
fc = os.path.basename(sys.argv[1])
outDir = 'ch14/scratch/'
arcpy.env.overwriteOutput = False
maxDist = float(sys.argv[2])
i = 1
while i <= maxDist:
    try:
        outFile = outDir + os.path.splitext(fc)[0] + str(i) + 'Buff.shp'
        distance = str(i) + ' miles'
        arcpy.Buffer_analysis(fc, outFile, distance)
        print 'Created: ', outFile
    except arcpy.ExecuteError:
        print arcpy.GetMessage(3)
    i = i + 1

```


```python
%run ch14/script2/bufferLoopDistTry.py ch14/data/cover.shp 3
```

    ERROR 000725: Output Feature Class: Dataset ch14\scratch\cover1Buff.shp already exists.
    ERROR 000725: Output Feature Class: Dataset ch14\scratch\cover2Buff.shp already exists.
    ERROR 000725: Output Feature Class: Dataset ch14\scratch\cover3Buff.shp already exists.


## 14.4 Discussion


```python
import sys, arcpy
if len(sys.argv) > 1:
    arcpy.env.workspace = sys.argv[1]
else:
    arcpy.env.workspace = 'C:/gispy/data/ch14'
for rast in arcpy.ListRasters():
    print rast
```


```python
import sys, arcpy
try:
    arcpy.env.workspace = sys.argv[1]
except IndexError:
    arcpy.env.workspace='C:/gispy/data/ch14'
for rast in arcpy.ListRasters():
    print rast
```


```python
import sys, arcpy
try:
    arcpy.env.workspace = sys.argv[1]
except IndexError:
    print 'Usage: <input workspace>'
sys.exit(0)
for rast in arcpy.ListRasters():
    printrast
```

## 14.5 Key Terms
* try and except blocks
* Named exceptions
* arcpy.GetMessages()
* Catch exceptions
* The arcpy.ExecuteError exception
* arcpy.GetMessage(index)
* arcpy.GetMessageCount()

## 14.6 Exercises
