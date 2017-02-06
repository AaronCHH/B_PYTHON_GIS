
# 11 Batch Geoprocessing

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [11 Batch Geoprocessing](#11-batch-geoprocessing)
  * [11.1 List GIS Data](#111-list-gis-data)
  * [11.2 Specify Data Name and Type](#112-specify-data-name-and-type)
  * [11.3 List Fields](#113-list-fields)
  * [11.4 Administrative Lists](#114-administrative-lists)
  * [11.5 Batch Geoprocess Lists of Data](#115-batch-geoprocess-lists-of-data)
  * [11.6 Debug: Step Through Code](#116-debug-step-through-code)
  * [11.7 Key Terms](#117-key-terms)
  * [11.8 Exercises](#118-exercises)

<!-- tocstop -->


## 11.1 List GIS Data


```python
import arcpy
arcpy.env.workspace = 'ch11/data'
# The ListFeatureClasses method returns a Python list of strings.
fcs = arcpy.ListFeatureClasses()
fcs
```




    [u'data1.shp',
     u'data1Buffer.shp',
     u'park.shp',
     u'parkBuffer.shp',
     u'USA.shp',
     u'USABuffer.shp']




```python
fcs[0]
```




    u'data1.shp'




```python
type(fcs[0])
```




    unicode




```python
for fc in fcs:
    print fc
```

    data1.shp
    data1Buffer.shp
    park.shp
    parkBuffer.shp
    USA.shp
    USABuffer.shp


* **Example 11.1: Call anarcpy listing method and loop through the results**  


```python
# %load ch11/script2/listStuff.py
# listStuff.py
# Purpose: Use arcpy to list workspaces and tables.
import arcpy

arcpy.env.workspace = 'ch11/data'

print '---Workspaces---'
workspaces = arcpy.ListWorkspaces()
for wspace in workspaces:
    print wspace

print '\n---Tables---'

tables = arcpy.ListTables()
for table in tables:
    print table

```


```python
%run ch11/script2/listStuff.py
```

    ---Workspaces---
    ch11/data\pics
    ch11/data\rastTester.gdb
    ch11/data\tester.gdb
    ch11/data\trains

    ---Tables---
    䥍啎当䅒⹓乂d
    䥍啎当䅒⹓呓aᒨ缈ᒨ繸ᒨ纈ᒨ纨ᒨ¸
    䥍啎当䅒⹓䅖tᒨ耈ᒨ缈ᒨ缘ᒨ纈ᒨ¨
    coords.csv
    loveLetter.txt
    xy1.txt
    xy_current.txt
    summary.dbf


## 11.2 Specify Data Name and Type

* **Example 11.2a–c: List rasters in workspace and usewild_card arguments**  


```python
# %load ch11/script2/wildcards.py
# wildcards.py
# Purpose: Use a wildcard to selectively list files.

import arcpy
arcpy.env.workspace = 'ch11/data/rastTester.gdb'

# a. Use '*' or empty parentheses to list ALL the rasters in the workspace.
rasts = arcpy.ListRasters('*')
print 'a. All the rasters:'
print rasts
print

# b. List the rasters whose names START with 'elev'.
rasts = arcpy.ListRasters('elev*')
print 'b. elev* rasters:'
print rasts
print

# c. List a raster whose name is exactly 'elev'.
rasts = arcpy.ListRasters('elev')
print 'c. elev raster:'
print rasts

```


```python
%run ch11/script2/wildcards.py
```

    a. All the rasters:
    [u'elev', u'landcov', u'soilsid', u'getty_cover', u'landc197', u'landuse', u'aspect', u'soils_kf', u'plus_ras', u'CoverMinus', u'elev_srt', u'elev_sh', u'elev_ned', u'Int_rand1', u'Int_rand2', u'landc196', u'TimesCOVER']

    b. elev* rasters:
    [u'elev', u'elev_srt', u'elev_sh', u'elev_ned']

    c. elev raster:
    [u'elev']


* **Example 11.3a–e: List rasters in workspace using wild_card and raster_type arguments**  


```python
# %load ch11/script2/rasterTypes.py
# rasterTypes.py
# Purpose: Use a wildcard to selectively list files.
import arcpy
arcpy.env.workspace = 'ch11/data'

# a. Use empty parenthesis to list ALL the rasters in the current workspace.
rasts = arcpy.ListRasters()
print 'a. All the rasters:'
print rasts
print

# b. List ALL the GIF type rasters.
rasts = arcpy.ListRasters('*', 'GIF')
print 'b. GIF rasters:'
print rasts
print

# c. List the raster whose name is GIF
rasts = arcpy.ListRasters('GIF')
print 'c. raster named GIF:'
print rasts
print

# d. List the rasters whose names start with 'tree'.
rasts = arcpy.ListRasters('tree*')
print 'd. tree* rasters:'
print rasts
print

# e. List the rasters whose names start with 'tree' which are GIF type files.
rasts = arcpy.ListRasters('tree*', 'GIF')
print 'e. tree* GIF type rasters:'
print rasts
print

```


```python
%run ch11/script2/rasterTypes.py
```

    a. All the rasters:
    [u'jack.jpg', u'minus_ras', u'tree.gif', u'tree.jpg', u'tree.png', u'tree.tif', u'tree2.gif', u'tree2.jpg', u'window.jpg']

    b. GIF rasters:
    [u'tree.gif', u'tree2.gif']

    c. raster named GIF:
    []

    d. tree* rasters:
    [u'tree.gif', u'tree.jpg', u'tree.png', u'tree.tif', u'tree2.gif', u'tree2.jpg']

    e. tree* GIF type rasters:
    [u'tree.gif', u'tree2.gif']




```python

```

## 11.3 List Fields


```python
# List the Field objects for this dataset.
fields = arcpy.ListFields('ch11/data/park.shp')
fields
```




    [<Field object at 0x14b530f0[0x3f8b158]>,
     <Field object at 0x14b530b0[0x3f8ba70]>,
     <Field object at 0x14b53110[0x3f8b890]>,
     <Field object at 0x146eae90[0x3f8b920]>]




```python
for fieldObject in fields:
    print fieldObject.name
```

    FID
    Shape
    COVER
    RECNO


* **Example 11.4: List theField object properties**  


```python
# %load ch11/script2/listFields.py
# listFields.py
# Purpose: List attribute table field properties.
import arcpy
arcpy.env.workspace = 'ch11/data'

fields = arcpy.ListFields('park.shp')
for fieldObject in fields:
    print 'Name: {0}'.format(fieldObject.name)
    print 'Length: {0}'.format(fieldObject.length)
    print 'Type: {0}'.format(fieldObject.type)
    print 'Editable: {0}'.format(fieldObject.editable)
    print 'Required: {0}\n'.format(fieldObject.required)

```


```python
%run ch11/script2/listFields.py
```

    Name: FID
    Length: 4
    Type: OID
    Editable: False
    Required: True

    Name: Shape
    Length: 0
    Type: Geometry
    Editable: True
    Required: True

    Name: COVER
    Length: 5
    Type: String
    Editable: True
    Required: False

    Name: RECNO
    Length: 11
    Type: Double
    Editable: True
    Required: False




```python
parkData = 'ch11/data/park.shp'
fields2 = arcpy.ListFields(parkData,'*', 'Double')
# The list length shows how many Field objects were returned.
len( fields2)
fields2[0].name
```




    u'RECNO'



## 11.4 Administrative Lists

## 11.5 Batch Geoprocess Lists of Data


```python
# List all coverage, geodatabase, TIN, Raster, and CAD datasets.
datasets = arcpy.ListDatasets('out*', 'GRID')
for data in datasets:
    arcpy.Delete_management(data)
```

* **Example 11.5: Batch buffer the feature class files in 'C:/gispy/data/ch11/'**  


```python
# %load ch11/script2/batchBuffer.py
# batchBuffer.py
# Purpose: Buffer each feature class in the workspace.
# Usage: No arguments required.

import arcpy, os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'ch11/data'

# GET a list of feature classes.
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    # SET the output variable. 
    fcBuffer = os.path.splitext(fc)[0] + 'Buffer.shp'
    # Call Buffer (Analysis) tool.
    arcpy.Buffer_analysis(fc, fcBuffer, '1 mile')
    print '{0} created.'.format(fcBuffer)

```


```python
%run ch11/script2/batchBuffer.py
```

    data1Buffer.shp created.
    data1BufferBuffer.shp created.
    parkBuffer.shp created.
    parkBufferBuffer.shp created.
    USABuffer.shp created.
    USABufferBuffer.shp created.


* **Example 11.6: Batch buffer files in 'C:/gispy/data/ch11/' and place them in directory**  


```python
# %load ch11/script2/batchBufferv2.py
# batchBufferv2.py
# Purpose: Buffer each feature class in the workspace and
#          place output in a different workspace.
import arcpy, os
arcpy.env.overwriteOutput = True
# SET workspaces
arcpy.env.workspace = 'ch11/data'
outDir = 'ch11/scratch/buffers/'
if not os.path.exists(outDir):
    os.mkdir(outDir)
# GET a list of feature classes
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    # SET the output variable
    outName = os.path.splitext(fc)[0] + '_buffer.shp'
    fcBuffer = os.path.join(outDir, outName)
    # Call buffer tool
    arcpy.Buffer_analysis(fc, fcBuffer, '1 mile')
    print '{0} created in {1}.'.format(fcBuffer, outDir)

```


```python
%run ch11/script2/batchBufferv2.py
```

    ch11/scratch/buffers/data1_buffer.shp created in ch11/scratch/buffers/.
    ch11/scratch/buffers/data1Buffer_buffer.shp created in ch11/scratch/buffers/.

* **Example 11.7 tableLister.py**  


```python
# %load ch11/script2/tableLister.py
# tableLister.py
# Purpose: Create shapefiles from 'stations*' xy tables, connect the points,
#          and then find then intersection of the lines.
# Usage:  workspace_containing_tables
# Example: C:/gispy/data/ch11/trains
import arcpy, os, sys
arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteOutput = True
tables = arcpy.ListTables('stations*', 'dBASE')

tempPoints = 'temporaryPointLayer'

for table in tables:
    # SET the output variable.
    lineFile = os.path.splitext(table)[0] + 'Line'
    # CALL geoprocessing tools.
    arcpy.MakeXYEventLayer_management(table, 'POINT_X', 'POINT_Y', tempPoints)
    arcpy.PointsToLine_management(tempPoints, lineFile)
    print '\t{0}/{1} created.'.format(arcpy.env.workspace, lineFile)

# GET the list of lines and intersect the lines.
lineList = arcpy.ListFeatureClasses('stations*Line*')
arcpy.Intersect_analysis(lineList, 'hubs', '#', '0.5 mile', 'POINT')
print '{0}/hubs created.'.format(arcpy.env.workspace)

```


```python
%run ch11/script2/tableLister.py ch11/data/trains
```

    	ch11/data/trains/stations1Line created.
    	ch11/data/trains/stations2Line created.
    	ch11/data/trains/stations3Line created.
    	ch11/data/trains/stations4Line created.
    ch11/data/trains/hubs created.


## 11.6 Debug: Step Through Code


```python

```


```python

```

## 11.7 Key Terms

## 11.8 Exercises
