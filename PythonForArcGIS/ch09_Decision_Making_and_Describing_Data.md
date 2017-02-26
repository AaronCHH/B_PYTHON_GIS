
# 9 Decision-Making and Describing Data

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [9 Decision-Making and Describing Data](#9-decision-making-and-describing-data)
  * [9.1 Conditional Expressions](#91-conditional-expressions)
    * [9.1.1 Comparison Operators](#911-comparison-operators)
    * [9.1.2 Equality vs. Assignment](#912-equality-vs-assignment)
    * [9.1.3 Logical Operators](#913-logical-operators)
    * [9.1.4 Membership Operators](#914-membership-operators)
  * [9.2 ArcGIS Tools That Make Selections](#92-arcgis-tools-that-make-selections)
    * [9.2.1 Select by Attributes and Temporary Feature Layers](#921-select-by-attributes-and-temporary-feature-layers)
  * [9.3 Getting a Description of the Data](#93-getting-a-description-of-the-data)
    * [9.3.1 Describe Object Properties](#931-describe-object-properties)
    * [9.3.2 Lists of Properties](#932-lists-of-properties)
    * [9.3.3 Using Specialized Properties](#933-using-specialized-properties)
    * [9.3.4 Compound vs. Nested Conditions](#934-compound-vs-nested-conditions)
    * [9.3.5 Testing Conditions](#935-testing-conditions)
  * [9.4 Required and Optional Script Input](#94-required-and-optional-script-input)
  * [9.5 Creating Output Directories](#95-creating-output-directories)
  * [9.6 Key Terms](#96-key-terms)
  * [9.7 Exercises](#97-exercises)

<!-- tocstop -->

* **Example 9.1**

```python
if speciesCount < 500:
    print 'Endangered species'
print speciesFID
```


```python
speciesCount = 250
if speciesCount < 500:
    print'Endangered species'
```

    Endangered species


```
Check the weather forecast
IF weather is sunny and calm THEN
    Swim in ocean.
ELSE IF weather is sunny and windy THEN
    Fly a kite.
ELSE IF weather is cold and clear THEN
    Go ice-skating.
ELSE
    Write GIS Python code.
ENDIF
```

* **Example 9.2: Check for valid polygon areas**

```python
if area > 0:
print 'The area is valid.'
    else:
print 'The area is invalid.'
```

## 9.1 Conditional Expressions


```python
bool(0)
```




    False




```python
bool(5)
```




    True



### 9.1.1 Comparison Operators


```python
100 < 'A' < 'a' < 'b'
```




    True




```python
'aa' < 'ab'
```




    True




```python
128 > 15
```




    True




```python
'128' > '15'
```




    False



* **Example 9.3: Print the ID numbers of highways and rivers**

```python
if classType == 'major highway':
    print 'Highway--', FID
elif classType == 'river':
    print 'River--', FID
```

* **Example 9.4: Print the ID number for all class types**

```python
if classType == 'highway’:
    print 'Highway--', FID
elif classType == 'river':
    print 'River--', FID
else:
print 'Other--', FID
```

### 9.1.2 Equality vs. Assignment

### 9.1.3 Logical Operators


```python
fileName = 'park.shp'
if fileName.endswith('.shp') or fileName.endswith('.txt'):
    print fileName
```

    park.shp



```python
if not fileName.endswith('.csv'):
    print fileName
```

    park.shp



```python
species = 'trout'
if species == 'salmon' or 'cat fish':
    print species
```

    trout



```python
if species == 'salmon' or species == 'catfish':
    print species
```

### 9.1.4 Membership Operators


```python
if classType == 'major highway' or classType == 'river' or classType == 'stream' or classType == 'bridge':
    print classType, '--',FID
else:
    print 'Other--', FID
```


```python
specialTypes = ['highway', 'river', 'stream', 'bridge']
if classType in specialTypes:
    print classType, '--',FID
else:
    print 'Other--', FID
```


```python
specialTypes = ['highway', 'river', 'stream', 'bridge']
if classType not inspecialTypes:
    print classType, '--', FID
```

## 9.2 ArcGIS Tools That Make Selections

* **Example 9.5: Using a hard-coded where-clause.**


```python
# %load ch09/script2/where_clause1.py
# where_clause1.py
# Purpose: Select features with high reclassification numbers.
# Usage: No arguments needed.

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'ch09/data'
inputFile = 'park.shp'
whereClause = 'RECNO >= 400'
arcpy.Select_analysis(inputFile, 'ch09/scratch/out.shp', whereClause)

```


```python
%run ch09/script2/where_clause1.py
```


```python
whereClause2 = 'RECNO > 400 AND RECNO < 410'
```


```python
whereClause3 = "COVER = 'orch'"
```


```python
whereClauseBogus = 'COVER = 'orch''
```


```python
fieldValue = 'orch'
whereClause4 = "COVER = '{0}'".format( fieldValue)
whereClause4
```


```python
fieldName = 'COVER'
fieldValue = 'orch'
whereClause5 = "{0} = '{1}'".format( fieldName, fieldValue)
whereClause5
```

* **Example 9.6: Using a where clause with variables.**


```python
# %load ch09/script2/where_clause2.py
# where_clause2.py
# Purpose: Extract raster features by attributes based on user input.
# Usage: fieldName fieldValue
# Example: COUNT 6000

import arcpy, sys

arcpy.env.workspace = 'ch09/data'
arcpy.CheckOutExtension('Spatial')

inputRast = 'getty_rast'

fieldName = sys.argv[1]
fieldValue = sys.argv[2]

whereClause = '{0} > {1}'.format(fieldName, fieldValue)

outputRast = arcpy.sa.ExtractByAttributes(inputRast, whereClause)
outputRast.save('ch09/scratch/attextract')
del outputRast

```


```python
%run ch09/script2/where_clause2.py
```

### 9.2.1 Select by Attributes and Temporary Feature Layers


```python
arcpy.env.workspace = 'ch09/data/tester.gdb'
tmp = 'tmpLayer'
arcpy.MakeFeatureLayer_management('park', tmp)
```




    <Result 'tmpLayer'>




```python
maxArea = 20000
coverType = 'woods'
whereClause = "Shape_area < {0} AND COVER ='{1}'".format(maxArea,coverType)
arcpy.SelectLayerByAttribute_management(tmp, 'NEW_SELECTION', whereClause)
```




    <Result 'tmpLayer'>




```python
output = 'smallWoods'
arcpy.CopyFeatures_management(tmp, output)
```




    <Result 'ch09/data/tester.gdb\\smallWoods'>



## 9.3 Getting a Description of the Data


```python
import arcpy
arcpy.env.workspace = 'ch09/data'
rastFile = 'getty_rast'
desc = arcpy.Describe(rastFile)
desc
```




    <geoprocessing describe data object at 0x3f189b0>



### 9.3.1 Describe Object Properties


```python
desc.dataType
```




    u'RasterDataset'




```python
desc.baseName
```




    u'getty_rast'




```python
desc.extension
```




    u''




```python
desc.catalogPath
```




    u'ch09/data\\getty_rast'




```python
desc.CatalogPath
```




    u'ch09/data\\getty_rast'




```python
desc.bandCount
```




    1




```python
desc.compressionType
```




    u'RLE'




```python
desc.format
```




    u'GRID'




```python
bounds = desc.extent
```


```python
bounds
```




    <Extent object at 0x13709bb0[0x3f18650]>




```python
bounds.XMax
```




    2167608.390378157



### 9.3.2 Lists of Properties
### 9.3.3 Using Specialized Properties

* **Example 9.7: Using a Describe properties inside a conditional block**


```python
# %load ch09/script2/describeRaster.py
# describeRaster.py
# Purpose: Report the format of raster input file.
# Usage: workspace, raster_dataset
# Example: C:/gispy/data/ch09 getty.tif

import arcpy
arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
desc = arcpy.Describe(data)
if desc.dataType == 'RasterDataset':
    print 'Image format: {0}'.format(desc.format)

```

### 9.3.4 Compound vs. Nested Conditions


```python
desc = arcpy.Describe('ch09/data/getty.tif')
desc.dataType
```




    u'RasterDataset'




```python
if desc.shapeType == 'Polyline' and desc.dataType in ['FeatureClass','Shapefile']:
    print 'Smooth line'
```

* **Example 9.8: Using a Describe properties inside a conditional block**


```python
# %load ch09/script2/smoothLineCompound.py
# smoothLineCompound.py
# Usage: workspace, features_with_line_geometry
# Example 1: C:/gispy/data/ch09 trails.shp
# Example 2: C:/gispy/data/ch09 park.shp

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
outFile = 'C:/gispy/scratch/smoothOut'
desc = arcpy.Describe(data)
if desc.dataType in ['FeatureClass', 'ShapeFile'] and desc.shapeType == 'Polyline':
    result = arcpy.SmoothLine_cartography(data, outFile, \
                                          'BEZIER_INTERPOLATION')
    print 'Smooth line created {0}.'.format(result.getOutput(0))

```

* **Example 9.9: Using Describe properties inside a nested conditional block**


```python
# %load ch09/script2/smoothLineNested.py
# smoothLineNested.py
# Usage: workspace, features_with_line_geometry
# Example 1: C:/gispy/data/ch09 trails.shp
# Example 2: C:/gispy/data/ch09 park.shp
# Example 3: C:/gispy/data/ch09 getty.tif
import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
outFile = 'C:/gispy/scratch/output'
desc = arcpy.Describe(data)

if desc.dataType in ['FeatureClass', 'ShapeFile']:
    if desc.shapeType == 'Polyline':
        result = arcpy.SmoothLine_cartography(data, outFile,
                                              'BEZIER_INTERPOLATION')
        print 'Smooth line created {0}.'.format(result.getOutput(0))
    else:
        print 'Warning: shape type is {0}. Smooth Line only works on Polyline \
shape types. '.format(desc.shapeType)
else:
    print "Warning: Input data type must be 'FeatureClass' or 'ShapeFile'."
    print 'Input dataType:', desc.dataType

```

### 9.3.5 Testing Conditions

## 9.4 Required and Optional Script Input

* **Example 9.10 scriptPathOptionalv1.py**


```python
# %load ch09/script2/scriptPathOptionalv1.py
# scriptPathOptionalv1.py
# Purpose: List the files in the given directory or the current directory.
# Usage: {directory path}
import sys, os

if len(sys.argv) >= 2:
    workingDir = sys.argv[1]
else:
    # Get the script location
    scriptPath = os.path.abspath(__file__)
    workingDir = os.path.dirname(scriptPath)

print '{0} contains the following files:'.format(workingDir)
print os.listdir(workingDir)

```

* **Example 9.11 scriptPathOptionalv2.py**


```python
# %load ch09/script2/scriptPathOptionalv2.py
# scriptPathOptionalv2.py
# Purpose: List the files in the given directory or the current directory.
# Usage: {directory path}
import arcpy, os

if arcpy.GetParameterAsText(0):
    workingDir = arcpy.GetParameterAsText(0)
else:
    # Get the script location
    scriptPath = os.path.abspath(__file__)
    workingDir = os.path.dirname(scriptPath)

print '{0} contains the following files:'.format(workingDir)
print os.listdir(workingDir)

```

* **Example 9.12: Simple distance converter distanceConvertv1.py**


```python
# %load ch09/script2/distanceConvertv1.py
# distanceConvertv1.py
# Purpose: Converts km to miles and vice versa.
# Usage: numerical_distance, unit_of_measure
# Example: 5 km

import sys

dist = float(sys.argv[1])  # Cast string to float
unit = sys.argv[2]

mileList = ['mi', 'mi.', 'mile', 'miles']

if unit.lower() in mileList:
        output = dist*1.6
        print '{0} {1} is equivalent to {2} kilometers(s).'.format(dist, unit, output)
else:
        output = dist*.62
        print '{0} {1} is equivalent to {2} mile(s).'.format(dist, unit, output)

```

* **Example 9.13: Distance converter with input checking distanceConvertv2.py**


```python
# %load ch09/script2/distanceConvertv2.py
# distanceConvertv2.py
# Purpose: Converts km to miles and vice versa.
# Usage: numerical_distance, {unit_of_measure}
# Example 1: 5 km
# Example 2:
# Example 3: 2.3
# Example 4: 10 MI
# Example 5: 2.2 bananas

import sys

numArgs = len(sys.argv)

# If no user arguments are given, exit the script and warn the user.
if numArgs == 1:
        print 'Usage: numeric_distance {distance_unit (mi or km)}'
        print 'Example: 5 km'
        sys.exit(0)  # exit the script

# If only one user argument is given, set the unit to miles.
if numArgs < 3:
        unit = 'miles'
        print 'Warning: No distance unit provided. Assuming input is in miles.'
else:
        # Get the unit provided by the user
        unit = sys.argv[2]

# Get the numeric distance (cast string to float).
dist = float(sys.argv[1])

# Perform conversion.
mileList = ['mi', 'mi.', 'mile', 'miles']

if unit.lower() in mileList:
        output = dist*1.6
        print'{0} {1} is equivalent to {2} kilometers(s).'.format(dist, unit, output)
else:
        output = dist*.62
        print '{0} {1} is equivalent to {2} mile(s).'.format(dist, unit, output)

```

## 9.5 Creating Output Directories


```python
myDir = 'ch09/data/happyGoat'
os.path.exists(myDir)
os.mkdir(myDir)
os.path.exists(myDir)
os.mkdir(myDir)
```


```python
if not os.path.exists(myDir):
    os.mkdir(myDir)
```


```python
outPath = 'C:/gispy/data/ch09/'
gdbName = 'happyHorse.gdb'
```


```python
if not arcpy.Exists(outPath + gdbName):
    arcpy.CreateFileGDB_management(outPath, gdbName)
```

* **Example 9.14 copyFilev2.py**


```python
# %load ch09/script2/copyFilev2.py
# copyFilev2.py
# Purpose: Copy a file.
# Usage: source_directory destination_directory file_to_backup
# Example: C:/gispy/data/ch09/ C:/gispy/scratch/backup park.shp
# The example works even if the C:/gispy/scratch/backup
#    directory doesn't exist yet.

import arcpy, os

arcpy.env.workspace = arcpy.GetParameterAsText(0)
outputDir = arcpy.GetParameterAsText(1)
fileToCopy = arcpy.GetParameterAsText(2)

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

outputFile = os.path.join(outputDir, fileToCopy)
arcpy.Copy_management(fileToCopy, outputFile)

print 'source =', os.path.join(arcpy.env.workspace, fileToCopy)
print 'destination =', outputFile

```

## 9.6 Key Terms
* if, elif, else, Python keywords  
* Conditional constructs
* Boolean expressions
* Conditional expressions
* Compound conditional expressions
* The os.path.exists function
* The os.mkdir function
* The CreateFileGDB tool

## 9.7 Exercises

```
if, elif, else,  Python keywords
Conditional constructs
Boolean expressions
Conditional expressions
Compound conditional expressions
The os.path.exists function
The os.mkdir function
The CreateFileGDB tool
```


```python

```
