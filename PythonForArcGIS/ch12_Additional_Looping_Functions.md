
# 12 Additional Looping Functions

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [12 Additional Looping Functions](#12-additional-looping-functions)
  * [12.1 List Comprehension](#121-list-comprehension)
  * [12.2 The Built-in enumerate Function](#122-the-built-in-enumerate-function)
  * [12.3 The Built-in zip Function](#123-the-built-in-zip-function)
  * [12.4 Walking Through Subdirectories](#124-walking-through-subdirectories)
  * [12.5 Key Terms](#125-key-terms)
  * [12.6 Exercises](#126-exercises)

<!-- tocstop -->


## 12.1 List Comprehension


```python
# Mixed-case list of field names.
listA = ['FID', 'Shape', 'COVER', 'RECNO']
for field in listA:
    field = field.lower()
print' field =', field
```

     field = recno



```python
listA
```




    ['FID', 'Shape', 'COVER', 'RECNO']




```python
listA = ['FID', 'Shape', 'COVER', 'RECNO']
listB = []
for field in listA:
    lowName = field.lower()
    listB.append(lowName)
listB
```




    ['fid', 'shape', 'cover', 'recno']




```python
listA = ['FID', 'Shape', 'COVER', 'RECNO']
listB = [ field.lower() for field in listA] # List comprehension
listB
```




    ['fid', 'shape', 'cover', 'recno']




```python
listA = range(1,6)
listA
```




    [1, 2, 3, 4, 5]




```python
listB = [i*2 for i in listA]
listB
```




    [2, 4, 6, 8, 10]




```python
listA
```




    [1, 2, 3, 4, 5]




```python
listA = [i**2 for i in listA]
listA
```




    [1, 4, 9, 16, 25]




```python
IDlist = ['000004', '000345', '003000', '000860']
IDlist = [ID.lstrip('0') for ID in IDlist]
IDlist
```




    ['4', '345', '3000', '860']




```python

```

## 12.2 The Built-in enumerate Function


```python
listA
```




    [1, 4, 9, 16, 25]




```python
for i, v in enumerate(listA):
    print i, v
```

    0 1
    1 4
    2 9
    3 16
    4 25


* **Example 12.1: Use the built-inenumerate function to print system arguments**  


```python
# %load ch12/script2/argPrint.py
# argPrint.py
# Purpose: Print args with built-in 'enumerate' function.
# Usage: Any arguments.
# Example input: 500 miles
import sys
for index, arg in enumerate(sys.argv):
    print 'Argument {0}: {1}'.format(index, arg)

```


```python
%run ch12/script2/argPrint.py 500 miles
```

    Argument 0: ch12/script2/argPrint.py
    Argument 1: 500
    Argument 2: miles


* **Example 12.2: Use enumerate to create unique output names**  


```python
# %load ch12/script2/point2LineV2.py
# point2LineV2.py (a modification of 'points2Line.py' from Chapter 10.)
# Purpose: V2 one uses the 'enumerate' function in the loop to
#     create a unique output name based on a number.
# Usage: No arguments needed.
import arcpy
arcpy.env.workspace = 'ch12/data'
arcpy.env.overwriteOutput = True
outDir = 'ch12/scratch/'

myFiles = ['data1.shp', 'data2.shp', 'data3.shp', 'data4.shp']
for index, currentFile in enumerate(myFiles):
    # Create a unique output names, 'Line1.shp,', 'Line2.shp'...
    outputName = 'Line{0}.shp'.format(index)
    arcpy.PointsToLine_management(currentFile, outDir + outputName)
    print outputName,

```


```python
%run ch12/script2/point2LineV2.py
```

    Line0.shp Line1.shp Line2.shp Line3.shp



```python

```

## 12.3 The Built-in zip Function


```python
listA = ['FID', 'Shape', 'COVER', 'RECNO']
listB = ['OID', 'Geometry', 'String']
zip(listA,listB)
```




    [('FID', 'OID'), ('Shape', 'Geometry'), ('COVER', 'String')]




```python
for a, b in zip(listA, listB):
    print 'a: ', a ,' b: ', b
```

    a:  FID  b:  OID
    a:  Shape  b:  Geometry
    a:  COVER  b:  String


## 12.4 Walking Through Subdirectories


```python
root = 'ch12/data/pics'
dirs = ['italy', 'jerusalem']
files = ['istanbul.jpg', 'istanbul2.jpg', 'marbleRoad.jpg', 'spice_market.jpg', 'stage.jpg']
```


```python
root = 'ch12/data/pics\italy'
dirs = ['venice']
files = ['backSeat.jpg', 'bridge.jpg', 'ct.jpg', ' florence.jpg']
```


```python
root = 'ch12/data/pics\italy\venice'
dirs = []
files = ['canal.jpg', 'fruitMarket.jpg']
```


```python
root = 'ch12/data/pics\jerusalem'
dirs = []
files = ['gate.jpg', 'old_city.jpg']
```

* **Example 12.3: Walk through subdirectories**  


```python
# %load ch12/script2/walkPics.py
# walkPics.py
# Purpose: Demostrate the 'os.walk' function.
import os
myDir = 'ch12/data/pics'
for root, dirs, files in os.walk(myDir):
    print 'root = {0}'.format(root)
    print 'dirs = {0}'.format(dirs)
    print 'files = {0}\n'.format(files)

```


```python
%run ch12/script2/walkPics.py
```

    root = ch12/data/pics
    dirs = ['italy', 'jerusalem']
    files = ['istanbul.jpg', 'istanbul2.jpg', 'marbleRoad.jpg', 'spice_market.jpg', 'stage.jpg']

    root = ch12/data/pics\italy
    dirs = ['venice']
    files = ['backSeat.jpg', 'bridge.jpg', 'ct.jpg', 'florence.jpg']

    root = ch12/data/pics\italy\venice
    dirs = []
    files = ['canal.jpg', 'fruitMarket.jpg']

    root = ch12/data/pics\jerusalem
    dirs = []
    files = ['gate.jpg', 'old_city.jpg']




```python
import arcpy, os
myDir = 'ch12/data/pics'
for root, dirs, files in os.walk(myDir):
    print files
```

    ['istanbul.jpg', 'istanbul2.jpg', 'marbleRoad.jpg', 'spice_market.jpg', 'stage.jpg']
    ['backSeat.jpg', 'bridge.jpg', 'ct.jpg', 'florence.jpg']
    ['canal.jpg', 'fruitMarket.jpg']
    ['gate.jpg', 'old_city.jpg']



```python
for root, dirs, files in os.walk(myDir):
    for f in files:
        print f
```

    istanbul.jpg
    istanbul2.jpg
    marbleRoad.jpg
    spice_market.jpg
    stage.jpg
    backSeat.jpg
    bridge.jpg
    ct.jpg
    florence.jpg
    canal.jpg
    fruitMarket.jpg
    gate.jpg
    old_city.jpg



```python
for root, dirs, files in os.walk(myDir):
    for f in files:
        print arcpy.Exists(f)
```

    False
    False
    False
    False
    False
    False
    False
    False
    False
    False
    False
    False
    False



```python
for root, dirs, files in os.walk(myDir):
    arcpy.env.workspace = root
    for f in files:
        print arcpy.Exists(f)
```

    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True


* **Example 12.4: Walk and print the full path names of the fi les with 'txt' extensions**  


```python
# %load ch12/script2/walkTXT.py
# walkTXT.py
# Purpose: Walk and print the full path file names of
#    'txt' extension files in the input directory.
# Usage: input_directory
# Example: C:/gispy/data/ch12/wTest
import arcpy, os, sys
mydir = sys.argv[1]
for root, dirs, files in os.walk(mydir):
    arcpy.env.workspace = root
    for f in files:
        if f.endswith('.shp'):
            # Print the full path file name of f
            print '{0}/{1}'.format(root, f)

```


```python
%run ch12/script2/walkTXT.py ch12/data/wTest
```

    ch12/data/wTest/data1.shp
    ch12/data/wTest\trains/regions1.shp
    ch12/data/wTest\trains/s2.shp


* **Example 12.5: Walk through the directories and buffer each shapefile**  


```python
# %load ch12/script2/osWalkBuffer.py
# osWalkBuffer.py
# Purpose: Walk and buffer the point shapefiles.
# Usage: input_directory output_directory
# Example: C:/gispy/data/ch12/wTest C:/gispy/scratch
import arcpy, os, sys
rootDir = sys.argv[1]
outDir = sys.argv[2]
arcpy.env.overwriteOutput = True
for root, dirs, files in os.walk(rootDir):
    arcpy.env.workspace = root
    fcs = arcpy.ListFeatureClasses('*', 'POINT')
    for f in fcs:
        # Set output name and perform geoprocessing on f
        outfile = outDir + '/' + os.path.splitext(f)[0] + '_buffer.shp'
        arcpy.Buffer_analysis(f, outfile, '1 mile')
        print '{0}/{1}  buffer ouput: {2}'.format(root, f, outfile)

```


```python
%run ch12/script2/osWalkBuffer.py ch12/data/wTest ch12/scratch
```

    ch12/data/wTest/data1.shp  buffer ouput: ch12/scratch/data1_buffer.shp
    ch12/data/wTest\trains/s2.shp  buffer ouput: ch12/scratch/s2_buffer.shp
    ch12/data/wTest\tSmall.gdb/c1  buffer ouput: ch12/scratch/c1_buffer.shp



```python

```

## 12.5 Key Terms


* List comprehension
* The string lstrip method
* Built-inenumerate function
* Built-inzip function
* The os.walk function
* The arcpy.Exists function


## 12.6 Exercises


```python

```
