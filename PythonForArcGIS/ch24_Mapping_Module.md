
# 24 Mapping Module

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [24 Mapping Module](#24-mapping-module)
  * [24.1 Map Documents](#241-map-documents)
    * [24.1.1 Map Name or 'CURRENT'  Map](#2411-map-name-or-current-map)
    * [24.1.2 MapDocument Properties](#2412-mapdocument-properties)
    * [24.1.3 Saving Map Documents](#2413-saving-map-documents)
  * [24.2 Working with Data Frames](#242-working-with-data-frames)
  * [24.3 Working with Layers](#243-working-with-layers)
    * [24.3.1 Moving, Removing, and Adding Layers](#2431-moving-removing-and-adding-layers)
    * [24.3.2 Working with Symbology](#2432-working-with-symbology)
  * [24.4 Managing Layout Elements](#244-managing-layout-elements)
  * [24.5 Discussion](#245-discussion)
  * [24.6 Key Terms](#246-key-terms)
  * [24.7 Exercises](#247-exercises)
  * [Index](#index)

<!-- tocstop -->

## 24.1 Map Documents


```python
import arcpy
myMap = 'ch24/data/maps/dataSourceExample.mxd'
mxd = arcpy.mapping.MapDocument(myMap)
mxd
```




    <MapDocument object at 0x40dae30[0x41ae640]>




```python
arcpy.mapping.ListBrokenDataSources(mxd)
```




    [<map layer u'potHoles'>, <map layer u'township'>]




```python
del mxd
```

* **Example 24.1:Export the layout view of a map document to a PNG image (Figure24.2)**


```python
# %load ch24/script2/mapToPhoto.py
# mapToPhoto.py
# Purpose: Export the 'Layout view' of a map as a PNG image.
# Usage: fullpath_mxd_filename fullpath_output_png_filename
# Sample input: C:/gispy/data/ch24/maps/landCover.mxd C:/gispy/scratch/getty_map.png
# Note: Portable Network Graphic (PNG) is an image format used for Internet content.
# Many other map export formats are available.

import arcpy, sys

# Full path names of an existing map and an image to create.
mapName = sys.argv[1]
imageName = sys.argv[2]

# Create a mapDocument object.
mxd = arcpy.mapping.MapDocument(mapName)

# Create an image of the map in 'Layout view'
arcpy.mapping.ExportToPNG(mxd, imageName)

print '{0} created.'.format(imageName)

# Delete the MapDocument object.
del mxd

```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-4-b9e12210457c> in <module>()
         14
         15 # Create a mapDocument object.
    ---> 16 mxd = arcpy.mapping.MapDocument(mapName)
         17
         18 # Create an image of the map in 'Layout view'


    C:\Program Files (x86)\ArcGIS\Desktop10.1\arcpy\arcpy\arcobjects\mixins.py in __init__(self, mxd)
        607            A string that includes the full path and file name of an existing map
        608            document ( .mxd ) or a string that contains the keyword CURRENT."""
    --> 609         assert (os.path.isfile(mxd) or (mxd.lower() == "current")), gp.getIDMessage(89004, "Invalid MXD filename")
        610         super(MapDocumentMethods, self).__init__(mxd)
        611     @property


    AssertionError: Invalid MXD filename.


### 24.1.1 Map Name or 'CURRENT'  Map


```python
mxd = arcpy.mapping.MapDocument('CURRENT')
```


```python
arcpy.env.workspace = 'C:/gispy/data/ch24/maps/'
mapName = 'landCover.mxd'
mxd = arcpy.mapping.MapDocument(mapName)
```


```python
# File name of an existing map
mapName = arcpy.env.workspace + '/landCover.mxd'
# Create a MapDocument object.
mxd = arcpy.mapping.MapDocument(mapName)
```

### 24.1.2 MapDocument Properties


```python
mxd = arcpy.mapping.MapDocument('CURRENT')
```


```python
mxd.author
mxd.author = 'Wonderful me!'
mxd.author
```


```python
mxd.activeView
mxd.activeView = 'PAGE_LAYOUT'
```


```python
mxd.title
mxd.title = 'Eastern US'
arcpy.RefreshActiveView()
```


```python
mxd.relativePaths
mxd.relativePaths = False
```


```python
mxd.filePath
mxd.filePath = 'C:\\gispy\\data\\ch24\\maps\\US.mxd'
```

### 24.1.3 Saving Map Documents


```python
mxd.saveACopy('modi fiedMap.mxd')
```


```python
import os
os.startfile('C:/gispy/data/ch24/maps/landCover.mxd')
```


```python
mxd.save()
```


```python

```

## 24.2 Working with Data Frames


```python
dfs = arcpy.mapping.ListDataFrames(mxd)
dfs
```


```python
# Get the first data frame.
df = dfs[0]
df.name
# Get the second data frame.
df2 = dfs[1]
df2.name
df.description
df2.description = "My very cool data frame"
df2.description
df2.displayUnits
```


```python
ext = df2.extent
ext.YMin
```


```python
arcpy.SelectLayerByAttribute_management('VA')
df2.zoomToSelectedFeatures()
```


```python
for df in dfs:
    # Print the name of the current data frame.
    print df.name
```


```python

```

## 24.3 Working with Layers


```python
layers = arcpy.mapping.ListLayers(mxd)
myLayer = layers[0]
myLayer.dataSource
```


```python
myLayer.isFeatureLayer
```


```python
myLayer.isRasterLayer
```


```python
e = myLayer.getExtent()
e
```


```python
e.YMin
```


```python
df.extent = myLayer.getExtent()
```


```python
layers = arcpy.mapping.ListLayers(mxd)
for myLayer in layers:
    print myLayer.name
```


```python
# Get a list of DataFrame objects.
dfs = arcpy.mapping.ListDataFrames(mxd)
# Get the first DataFrame object.
df = dfs[0]
# Get a list of Layer objects in this data frame.
layers = arcpy.mapping.ListLayers(mxd, '*', df)
for myLayer in layers:
    print myLayer.name
```

### 24.3.1 Moving, Removing, and Adding Layers


```python
mxd = arcpy.mapping.MapDocument('CURRENT')
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]
lyrs = arcpy.mapping.ListLayers(mxd)
```


```python
layerToMove = lyrs[2]
layerToMove.name
referenceLayer = lyrs[0]
referenceLayer.name
```


```python
arcpy.mapping.MoveLayer(df, referenceLayer, layerToMove, 'BEFORE')
```

* **Example 24.2:Remove the first layer from a map removeLayers.py**


```python
# %load ch24/script2/removeLayers.py
# removeLayers.py
# Purpose: Remove the first layer in the table of contents.
# Input: No arguments required.

import arcpy

# Get a MapDocument object.
mxdName = 'layerManipExample2.mxd'
mapPath = 'C:/gispy/data/ch24/maps/'
mxd = arcpy.mapping.MapDocument(mapPath + mxdName)

# Get a list of the DataFrame objects.
dfs = arcpy.mapping.ListDataFrames(mxd)

# Get the first DataFrame object.
df = dfs[0]

# Get a list of Layer objects in this data frame.
lyrs = arcpy.mapping.ListLayers(mxd, '', df)

# Get the first Layer object.
layerToRemove = lyrs[0]

# Remove the layer.
arcpy.mapping.RemoveLayer(df, layerToRemove)

# Save a copy of the map.
copyName = 'C:/gispy/scratch/' + mxdName[:-4] + '_V2.mxd'
mxd.saveACopy(copyName)
print '{0} created.'.format(copyName)

# Delete the <code>MapDocument</code> object to release the map.
del mxd

```

* **Example 24.3:Adding a shapefile layer to a map addLayer.py**


```python
# %load ch24/script2/addLayers.py
# addLayer.py
# Purpose: Add a data layer to a map.
# Input: No arguments required.
import arcpy

# Initialize data variables.
arcpy.env.workspace = 'C:/gispy/data/ch24/maps/'
fileName = '../USstates/MA.shp'
mapName = 'layerManipExample3.mxd'

# Instantiate MapDocument and DataFrame objects.
mxd = arcpy.mapping.MapDocument(arcpy.env.workspace + '/' +
                                mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)

# Get the first data frame.
df = dfs[0]

# Instantiate a Layer object.
layerObj = arcpy.mapping.Layer(fileName)

# Add the new layer to the map.
arcpy.mapping.AddLayer(df, layerObj)

# Save a copy of the map.
copyName = 'C:/gispy/scratch/' + mapName[:-4] + '_V2.mxd'
mxd.saveACopy(copyName)
print '{0} created.'.format(copyName)

# Delete the MapDocument object to release the map.
del mxd

```

### 24.3.2 Working with Symbology


```python
mxd = arcpy.mapping.MapDocument('CURRENT')
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]
lyrs = arcpy.mapping.ListLayers(mxd)
layerToModify = lyrs[0]
layerToModify.symbologyType
```


```python
layerToModify.symbology
```


```python
layerToModify.symbologyType = 'GRADUATED_COLORS'
```


```python
srcLay = 'C:/gispy/data/ch24/symbolTraining/gradColorsNE.lyr'
srcLayObj = arcpy.mapping.Layer(srcLay)
arcpy.mapping.UpdateLayer(df, layerToModify, srcLayObj)
layerToModify.symbologyType
```


```python
layerToModify.symbology.valueField
layerToModify.symbology.valueField = 'AVE_FAM_SZ'
arcpy.RefreshActiveView()
layerToModify.symbology.numClasses
layerToModify.symbology.numClasses = 3
arcpy.RefreshActiveView()
```

## 24.4 Managing Layout Elements


```python
mxd = arcpy.mapping.MapDocument('CURRENT')
elems = arcpy.mapping.ListLayoutElements(mxd)
for e in elems:
    printe.name
```


```python
for e in elems:
    if 'Title' in e.name:
        title = e
title
```


```python
arrow = arcpy.mapping.ListLayoutElements(mxd,'MAPSURROUND_ELEMENT', '*Arrow*')[0]
arrow.name
```


```python
title.text
title.text = 'USA'
arcpy.RefreshActiveView()
title.fontSize
title.fontSize = 72
arcpy.RefreshActiveView()
```


```python
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]
title.elementPositionX = df.elementPositionX + (df.elementWidth*0.5) - (title.elementWidth*0.5)
arcpy.RefreshActiveView()
```


```python
title.elementPositionY = df.elementPositionY + df.elementHeight - title.elementHeight
arcpy.RefreshActiveView()
```


```python
myExport = 'C:/gispy/scratch/noSurrounds.pdf'
arcpy.mapping.ExportToPDF(mxd, myExport)
```

## 24.5 Discussion

## 24.6 Key Terms
* MapDocument objects
* DataFrame objects
* Layer objects
* 'CURRENT'  vs. map name
* RefreshActiveView method
* Layer file (.lyr extension)  
* SymbologyType property
* Layer object symbology class
* Layout element objects

## 24.7 Exercises

## Index
