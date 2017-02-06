
# 10 Repetition: Looping for Geoprocessing

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [10 Repetition: Looping for Geoprocessing](#10-repetition-looping-for-geoprocessing)
  * [10.1 Looping Syntax](#101-looping-syntax)
    * [10.1.1 WHILE-Loops](#1011-while-loops)
    * [10.1.2 FOR-Loops](#1012-for-loops)
  * [10.2 Nested Code Blocks](#102-nested-code-blocks)
  * [10.3 Directory Inventory](#103-directory-inventory)
  * [10.4 Indentation and the TabNanny](#104-indentation-and-the-tabnanny)
  * [10.5 Key Terms](#105-key-terms)
  * [10.6 Exercises](#106-exercises)

<!-- tocstop -->

## 10.1 Looping Syntax

### 10.1.1 WHILE-Loops

* **Example 10.1 simpleWhileLoop.py**  


```python
# %load ch10/script2/simpleWhileLoop.py
# simpleWhileLoop.py
x = 1
while x <= 5:
    print x
    x = x + 1
print "I'm done!"

```


```python
%run ch10/script2/simpleWhileLoop.py
```

    1
    2
    3
    4
    5
    I'm done!


* **Example 10.2: Use aWHILE -loop to create 3 rasters containing random values with a normal distribution**  


```python
# %load ch10/script2/normalRastsLoop.py
# normalRastsLoop.py
# Purpose: Create 3 raster containing random values with a normal (gaussian) distribution.

import arcpy
arcpy.env.workspace = 'ch10/data'
outDir = 'ch10/scratch'
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension('Spatial')

n = 1
while n < 4:
    outputName = 'out{0}'.format(n)
    tempRast = arcpy.sa.CreateNormalRaster()
    tempRast.save(outDir + outputName)
    print '{0}{1} created.'.format(outDir, outputName)
    n = n + 1
del tempRast
print 'Normal raster creation complete.'

```


```python
%run ch10/script2/normalRastsLoop.py
```

    ch10/scratchout1 created.
    ch10/scratchout2 created.
    ch10/scratchout3 created.
    Normal raster creation complete.


### 10.1.2 FOR-Loops

* **Example 10.3: Basic FOR-loop simpleForLoop.py**  


```python
# %load ch10/script2/simpleForLoop.py
# simpleForLoop.py
myFiles = ['data1.shp', 'data2.shp',  'data3.shp', 'data4.shp']
for currentFile in myFiles:
    print currentFile
print "I'm done!"

```


```python
%run ch10/script2/simpleForLoop.py
```

    data1.shp
    data2.shp
    data3.shp
    data4.shp
    I'm done!



```python
dFiles = ['data1.shp', 'data2.shp','data3.shp','data4.shp']
for elephant in dFiles:
    print elephant
```

    data1.shp
    data2.shp
    data3.shp
    data4.shp


* **Example 10.4: Use aFOR -loop to perform a point to line conversion on a hard coded file list**  


```python
# %load ch10/script2/point2Line.py
# point2Line.py
# Purpose: Create a set of line features from a set of point features in a list.
import arcpy
arcpy.env.workspace = 'ch10/data'
outDir = 'ch10/scratch'
arcpy.env.overwriteOutput = True

theFiles = ['data1.shp', 'data2.shp', 'data3.shp', 'data4.shp']
for currentFile in theFiles:
    # Remove file extension from the current name.
    baseName = currentFile[:-4]
    # Create unique output name. E.g., 'data1Line.shp'.
    outName = outDir + baseName + 'Line.shp'
    arcpy.PointsToLine_management(currentFile, outName)
    print '{0}{1} created.'.format(outDir, outName)

```


```python
%run ch10/script2/point2Line.py
```

    ch10/scratchch10/scratchdata1Line.shp created.
    ch10/scratchch10/scratchdata2Line.shp created.
    ch10/scratchch10/scratchdata3Line.shp created.
    ch10/scratchch10/scratchdata4Line.shp created.


* **Example 10.5: FOR-loop using therange function to update the linear unit**  


```python
# %load ch10/script2/bufferLoopRange.py
# bufferLoopRange.py
# Purpose: Buffer a park varying buffer distances from 1 to 5 miles.

import arcpy
arcpy.env.workspace = 'ch10/data'
outDir = 'ch10/scratch'
arcpy.env.overwriteOutput = True
inName = 'park.shp'
for num in range(1, 6):
    # Set the buffer distance based on num ('1 miles', '2 miles', ...).
    distance = '{0} miles'.format(num)
    # Set the output name based on num ('buffer1.shp', 'buffer2.shp', ...)
    outName = outDir + 'buffer{0}.shp'.format(num)
    arcpy.Buffer_analysis(inName, outName, distance)
    print '{0}{1} created.'.format(outDir, outName)

```


```python
%run ch10/script2/bufferLoopRange.py
```

    ch10/scratchch10/scratchbuffer1.shp created.
    ch10/scratchch10/scratchbuffer2.shp created.
    ch10/scratchch10/scratchbuffer3.shp created.
    ch10/scratchch10/scratchbuffer4.shp created.
    ch10/scratchch10/scratchbuffer5.shp created.


## 10.2 Nested Code Blocks

* **Example 10.6 emotaLoop.py**  


```python
# %load ch10/script2/emotaLoop.py
# emotaLoop.py
# Purpose: Nest conditions inside a loop to print an emoticon for each file name.
myFiles = ['crops.csv', 'data1.shp', 'rast', 'xy1.txt']

for f in myFiles:
    if f.endswith('.shp'):
        print '   ;]   ' + f
    elif f.endswith('.txt'):
        print '   :(   ' + f
    else:
        print '   :o   ' + f

```


```python
%run ch10/script2/emotaLoop.py
```

       :o   crops.csv
       ;]   data1.shp
       :o   rast
       :(   xy1.txt


* **Example 10.7 scatting.py**  


```python
# %load ch10/script2/scatting.py
# scatting.py
# Purpose: Use nested loops to scat.
print '\nskeep-de'
for i in range(2):
    print '    beep'
    for j in range(3):
        print '        bop'
print 'ba-doop!'

```


```python
%run ch10/script2/scatting.py
```


    skeep-de
        beep
            bop
            bop
            bop
        beep
            bop
            bop
            bop
    ba-doop!


## 10.3 Directory Inventory


```python
import os
theDir = 'ch10/data/pics'
# os.listdir returns a list of the files
theFiles = os.listdir(theDir)
theFiles
```




    ['istanbul.jpg',
     'istanbul2.jpg',
     'italy',
     'jerusalem',
     'marbleRoad.jpg',
     'schema.ini',
     'spice_market.jpg',
     'stage.jpg']




```python
for fileName in theFiles:
    print fileName
```

    istanbul.jpg
    istanbul2.jpg
    italy
    jerusalem
    marbleRoad.jpg
    schema.ini
    spice_market.jpg
    stage.jpg


* **Example 10.8: List files with theos module and geoprocess the files: copyLoop.py**  


```python
# %load ch10/script2/copyLoop.py
# copyLoop.py
# Purpose: Make a copy of each ASCII .txt extension file.

import arcpy, os

arcpy.env.workspace = 'ch10/data'
outDir = 'ch10/scratch/'
theFiles = os.listdir(arcpy.env.workspace)
for fileName in theFiles:
    if fileName.endswith('.txt'):
        outName = outDir + fileName[:-4] + 'V2.txt'
        arcpy.Copy_management(fileName, outName)
        print '{0} created.'.format(outName)

```


```python
%run ch10/script2/copyLoop.py
```

    ch10/scratch/dataV2.txt created.
    ch10/scratch/xy1V2.txt created.
    ch10/scratch/xy_currentV2.txt created.



```python
import os
theDir = 'ch10/data/pics'
# os.listdir returns a list of the files
theFiles = os.listdir(theDir)
for fileName in theFiles:
    print os.path.exists( fileName)
```

    False
    False
    False
    False
    False
    False
    False
    False


* **Example 10.9: Useos.path.join inside a loop to create full path fi le names printModTime.py**  


```python
# %load ch10/script2/printModTime.py
# printModTime.py
# Purpose: For each file, print the time of most recent modification.
# Input:   No arguments required.

import os, datetime

theDir = "ch10/data/pics"
theFiles = os.listdir(theDir)
for f in theFiles:
    fullName = os.path.join(theDir, f)
    # Get the modification time.
    print os.path.getmtime(fullName)



##import os, datetime  #(this version provides fancier formatting)
##
##theDir = "C:/gispy/data/ch10/pics"
##theFiles = os.listdir(theDir)
##for f in theFiles:
##	fullName = os.path.join(theDir, f)
##	# Get the modification time.
##	modTime = os.path.getmtime(fullName)
##	# Convert Epoch time to a time stamp.
##	theDate = datetime.datetime.fromtimestamp(modTime)
##	# Reformat the time stamp
##	print theDate.strftime("%m/%d/%Y %H:%M:%S")

```


```python
%run ch10/script2/printModTime.py
```

    1455059926.0
    1455059926.0
    1479981414.48
    1479981414.55
    1455059926.0
    1455059926.0
    1455059926.0
    1455059926.0


## 10.4 Indentation and the TabNanny

## 10.5 Key Terms

## 10.6 Exercises

```
The while keyword
The for keyword
The for andin keyword pairing
Iterating variable
Sequence data objects
Nested looping
The os.listdir function
```


```python

```
