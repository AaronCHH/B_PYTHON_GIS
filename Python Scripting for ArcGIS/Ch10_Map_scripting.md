
# Chapter 10: Map scripting

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 10: Map scripting](#chapter-10-map-scripting)
  * [10.1 Introduction](#101-introduction)
  * [10.2 Working with the ArcPy mapping module](#102-working-with-the-arcpy-mapping-module)
  * [10.3 Opening map documents](#103-opening-map-documents)
  * [10.4 Accessing map document properties and methods](#104-accessing-map-document-properties-and-methods)
  * [10.5 Working with data frames](#105-working-with-data-frames)
  * [10.6 Working with layers](#106-working-with-layers)
  * [10.7 Fixing broken data sources](#107-fixing-broken-data-sources)
  * [10.8 Working with page layout elements](#108-working-with-page-layout-elements)
  * [10.9 Exporting maps](#109-exporting-maps)
  * [10.10 Printing maps](#1010-printing-maps)
  * [10.11 Working with PDFs](#1011-working-with-pdfs)
  * [10.12 Creating map books](#1012-creating-map-books)
  * [10.13 Using sample mapping scripts](#1013-using-sample-mapping-scripts)
  * [Points to remember](#points-to-remember)

<!-- tocstop -->


## 10.1 Introduction

This chapter describes the ArcPy mapping module, also referred to as arcpy.mapping.
The ArcPy mapping module helps automate mapping tasks, including managing map documents, data frames, layer files, and the data within these files.
There is also support for the automation of map export and printing, as well as the creation of PDF map books.


## 10.2 Working with the ArcPy mapping module

The ArcPy mapping module can be used to automate ArcMap workflows to speed up repetitive tasks. Some typical examples of uses for the ArcPy mapping module are as follows:
* Finding a layer with a particular data source and replacing it with another data source
* Modifying the display properties of a speci&c layer in multiple ArcMap documents
* Generating reports that describe the properties of ArcMap documents, including data sources, layers with broken data links, information on the spatial reference of data frames, and more

## 10.3 Opening map documents

There are two ways to start working with a map document using the ArcPy mapping module:
(1) use the map document from the current ArcMap session or
(2) reference an existing .mxd &le stored on disk.
The MapDocument function is used to accomplish both.
The syntax of the MapDocument function is


```python
MapDocument(mxd_path)
```

The path is a string representing an .mxd file on disk.
The following code
opens a map document:


```python
mapdoc = arcpy.mapping.MapDocument(C:/Mapping/Study_Areas.mxd")
```

To use the current map document in ArcMap, the keyword CURRENT (in all uppercase letters) is used:


```python
mapdoc = arcpy.mapping.MapDocument("CURRENT")
```

When a MapDocument object is referenced in a script, the .mxd file is locked.
This prevents other applications from making changes to the file.
It is therefore good practice to remove the reference to a map document when it is no longer needed in a script by using the Python del statement.
A mapping script therefore often has a structure that looks something like the following:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/Mapping/Study_Areas.mxd")
# <code that modifies map document properties>
mapdoc.save()
del mapdoc
```


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("./Ch10/ch10.mxd")
# <code that modifies map document properties>
mapdoc.save()
del mapdoc
```

## 10.4 Accessing map document properties and methods

In the following example, the CURRENT keyword is used to obtain the map document currently open in ArcMap, and the filePath property is used to print the system path for the .mxd file:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
path = mapdoc.filePath
print path
del mapdoc
```


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("./Ch10/ch10.mxd")
path = mapdoc.filePath
print path
del mapdoc
```

The following example updates the current map document's title and saves the .mxd file:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
mapdoc.title = "Final map of study areas"
mapdoc.save()
del mapdoc
```

As you review these basic examples, remember that they can be used to automate more complex tasks, such as making changes to multiple map documents rather than just the current one.


## 10.5 Working with data frames

Map documents contain one or more data frames and each data frame typically contains one or more layers.
Data frames and layers are perfect objects for use in lists, which can help automate tasks.
The ListDataFrames function returns a list of DataFrame objects in a map document.
The syntax is as follows


```python
ListDataFrames(map_document, {wild_card})
```

Once you have a list of data frames in a map document, you can look through them to examine or modify their properties.
Running the following code prints a list of all the data frames in a map document:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
listdf = arcpy.mapping.ListDataFrames(mapdoc)
for df in listdf:
    print df.name
del mapdoc
```

If you want to work with just one of the data frames, you can use its index number, as follows:


```python
print listdf[0].name
```

The order of a list of data frames is the same as the order used in the Arcmap table of contents.


DataFrame object properties, such as map extent, scale, rotation, and spatial reference, use map units.
Other properties use page units to position and size the data frame on the layout page.
Data frames are also used to access other objects - for example, the ListLayers function is used to access the layers in each dataframe.
**You can then loop through the layers to get their properties.**
It is therefore important to **uniquely** name the data frames within a single map document.

There are quite a number of data frame properties, which are described in the ArcPy documentation in ArcGIS Desktop Help.
The properties of the DataFrame object are a subset of all the properties on the Data Frame Properties dialog box in Arcmap (right-click a data frame in the Tab1e Of Contents window and click Properties).

Scripting does not provide access to all the properties on the Data Frame Properties dialog box, and conversely, some DataFrame object properties are not on the Data Frame Properties dialog box.
For example, the scale of a data frame can be set using scripting, but in ArcMap, it is accomplished by using a tool on the Standard toolbar.

In most cases when you work with a map document, you are not interested in changing all the properties of a data frame , but only a few selected ones.
For example, in the following code, the spatial reference of all data frames in a map document is set to the same spatial reference as that of a specific shapefile, and the scale of all data frames is set to 1:24,000:



```python
import arcpy
dataset = "C:/map/boundary.shp"
spatialRef = arcpy.Describe(dataset).spatalReference
mapdoc = arcpy.mapping.MapDocument("C:/map/final.mxd")
for df in arcpy.mapping.ListDataFrames(mapdoc):
    df.spatalReference = spatialRef
    df.scale = 24000
mapdoc.save()
del mapdoc
```

In addition to the properties already discussed, the DataFrame object also has two methods: panToExtent and zoomToSelectedFeatures.
The panToExtent method maintains the data frame scale but pans and cen ters the data frame extent based on the properties of an Extent object, which has to be provided as a parameter.
An Extent object is a rectangle specified by providing the coordinates of the lower-left corner and the upper-right corner in map units.
In most cases, this property is derived from an existing object, such as a feature or a layer.
For example, the getExtent method can be used to obtain the extent of a layer.
The follow ing code pans the extent of a data frame called df based on the extent of the features in a layer object called lyr:



```python
df.panToExtent(lyr.getExtent())
```

The zoomToSelectedFeatures method is similar to the ArcMap opera tion Selection > Zoom to Selected Features.
Running the following code zooms to the extent of all selected features in a data frame called df:


```python
df.zoomToSelectedFeatures()
```

If no features are selected, the code will zoom to the full extent of alllayers.

## 10.6 Working with layers

A data frame typically contains one or more layers and the Layer object is essential to managing these layers.
The Layer object provides access to many different layer properties and methods.
There are two ways to reference Layer objects.
The first approach is to use the Layer function to reference a layer (.lyr) file on disk.
It is similar to how map document files (.mxd) are referenced.
The syntax of the Layer function is


```python
Layer(lyr_file_ path)
```

The parameter of the Layer function is the full path and file name of an
existing .lyr file. For example:


```python
Lyr = arcpy.mapping.Laye("C:/Mapping/study.lyr")
```

The second approach is to use the ListLayers function to reference the layers in an .mxd file, or just the layers in a particular data frame in a map document, or the layers within a .lyr file.
The syntax of the List La yers function is


```python
Layer(ly_rfile_path)
```

The parameter of the Layer function is the full path and file name of an
existing .lyr file. For example:


```python
Lyr = arcpy.maping.Layer("C:/Mappng/study.lyr")
```

The second approach is to use the ListLayers function to reference the layers in an .mxd file, or just the layers in a particular data frame in a map document, or the layers within a .lyr file.
The syntax of the List La yers function is


```python
ListLayers(map_document_or_layer, {wild_card}, {data_frame})
```

The only required element is a map document or layer file.
An optional wild card can be used to limit the result.
An optionaldata frame variable can be used that references a specific DataFrame object.
For example, the follow ing code returns a list of all the layers in an ArcMap document, and then prints the names of all the layers:


```python
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
lyrlist = arcpy.mapping.ListLayers(mapdoc)
for lyr in lyrlist:
    print lyr.name
```

To access just the layers in a specific data frame, the Data Frame object has to be referenced as a parameter.
In the following example, the st aye function returns only the layers in the data frame that have index number 0.
The wild_card parameter is skipped using an empty string ("")


```python
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
dflist = arcpy.mapping.ListDataFrames(mapdoc)
lyrlist = arcpy.mapping.ListLayers(mapdoc, "", dflist[0])
for lyr in lyrlist:
    print lyr.name
```

The following code illustrates how to reference the layers in a .layer file on disk and print the name of layer objects:


```python
import arcpy
lyrfile = arcpy.mapping.Layer("C:/Data/mylayers.lyr")
lyrlist = arcpy.mapping.ListLayers(lyrfile)
for lyr in lyr list:
    print lyr.name
```

A few examples will serve to illustrate the use of layer properties.
For example, the following code turns on all the labels for the layers in the current map document using the showLabels property:


```python
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
dflist = arcpy.mapping.ListDataFrames(mapdoc)
lyrlist = arcpy.mapping.ListLayers(mapdoc, "", dflist[0])
for lyr in lyrlist:
    lyr.showLabels = True
del lyrlist
```

Instead of changing the properties of all the layers in a map document or a data frame , the layer properties can also be used to find a layer with a particular name.
For example, the following code searches for a layer called "hospitals":


```python
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
lyrlist = arcpy.mapping.ListLayers(mapdoc)
for lyr in lyrlist :
    if lyr.name == "hospitals":
        lyr.showLabels = True
del lyrlist
```

Layer names can be a bit confusing.
The name of a layer is w hat is shown in the ArcMap table of contents.
This may or may not be the same as the name of the source dataset for the layer.
In any case, the name of a lay does not have an extension.
So the name of a feature class could be hospitals.shp, but as a layer in ArcMap, the name of the layer is hospitals.


Also remember that strings are case sensitive, so Hospitals is different from hospitals.
To make your statements insensitive to case, you can use basic string operators.
For example:


```python
if lyr.name.lower() == "hospitals":
```

Because not all types of layers support the same properties, the supports method can be used to determine whether a layer supports a particular property.
This makes it possible to test whether a layer supports a property before trying to get or set its value.
This reduces the need for error checking.
In the earlier example where the labels were shown for alllayers in a data frame, it would make sense to f1 rst use the supp orts method to test whether this property is supported for each layer.
The syntax of the supports method is


```python
supports(layer property)
```

The parameter, in this case, would consist of one of the Layer object properties, such as br ghtness contrast, datasetName, or others.
The supports method returns a Boolean value, so the example code to test whether labeling is possible would look as follows:


```python
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
dflist = arcpy.mapping.ListDataFrames(mapdoc)
lyrlist = arcpy.mapping.ListLayers(mapdoc, "", dflist[0])
for lyr in lyrlist:
    if lyr.supports("SHOWLABELS") == True:
        lyr.showLabels = True
del lyrlist
```

If you are unsure whether a layer supports a particular property, use the supports method to test it.
Otherwise, you will need to use an error trapping method, such as a try - except statement, which is covered in chapter 11.

In addition to properties and methods of layer objects, there are several functions in the ArcPy mapping module that are specifically designed to manage layers within a data frame.
These include the following:

* **AddLayer** - makes it possible to add a layer to a data frame within a map document using general placement options.
* **AddLayerToGroup** - makes it possible to add a layer to a group layer within a map document using general placement options.
* **InsertLayer** - makes it possible to add a layer to a data frame or to a group layer within a map document.
It provides a more precise way of positioning the layer by using a reference layer.
* **MoveLayer** - makes it possible to move a layer to a specific location within a data frame or group layer within a map document.
* **RemoveLayer** - makes it possible to remove a layer from a map document.
* **UpdateLayer** - makes it possible to update the layer properties or just the symbology of a layer in a map document by extracting the information from a source layer.

These functions all must reference an already existing layer.
It can be a layer file on disk, a layer from within the same map document, or a layer from a different map document.
Thus, these functions do not perform the task of adding data to a map document, as Add Data does in ArcMap.

## 10.7 Fixing broken data sources

Broken data sources are very common, and fixing them manually can be tedio us.
Scripting can be used to automate these corrections once the nature of the fix has been identified.
Changes can be made to the map docu ment w ithout even opening it.
Before examining th ese methods in more detail, a few definitions are in order:

* **Worhspace** - a container for data.
It can be a folder that contains shapefiles, a coverage, or a geodatabase - for example, mydata.

* **Worhspace path** - the system path to a workspace. It includes the drive letter where the folder is located and any subfolders - for example, C:\mydata.
For a file-based geodatabase, it includes the name of the geodatabase - for example, C:\mydata\project.gdb.

* **Dαtaset** - the feature class or table in the workspace.
It is the actual name on disk, not the name displayed in the ArcMap table of contents.
For a shapefile, it would be something like hospitals.shp.
For a feature class in a geodatabase, it would be something like hospitals.

* **Dαta source** - the combination of workspace and dataset - for example, mydata\hospitals.shp or mydata\project.gdb\hospitals

Prior to using a map document, you should check for broken data sources using the ListBrokenDataSources function.
This arcpy.mapping function returns a Python list of layer objects within a map document or layer file that have broken connections to their original data source.
The syntax is


```python
ListBrokenDataSources(map_document_or_layer)
```

The following code illustrates how this function can be used to print the names of the layers in a map document that have broken data sources:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
brokenlist = arcpy.mapping.ListBrokenDataSources(mapdoc)
for lyr in brokenlist:
    print lyr.name
del mapdoc
```

Running this code returns the nam es of the layers as they appear in the ArcMap table of contents.
Instead of the name, the layer property dataSource can be used to see the current data source being referenced by the layer, as follows:


```python
print lyr.dataSource
```

Once it is established that data sources ne ed to be updated or fixed, the following methods can be applied to map documents, layers, or tables:

* **```findAndReplaceWorkspacePaths```** and **```replaceWorkspaces```** - use to perform a find-and-replace operation on the workspace path and the workspace, respectively.
This assumes that the datasets are correct.
For example, you can change C:\mydata\hospitals.shp to C:\newdata\hospitals.shp, but the name of the dataset (in this case, hospitals.shp) cannot be modified.

* **```replaceDataSource```** - use to perform a find-and-replace opera tion on the workspace and the dataset.
You can modify both the workspace and the dataset, or just the dataset.
For example, you can change C:\mydata\hospitals.shp to C:\mydata\newhospitals.shp.

The following methods work on three different classes: MapDocument, Layer , and TableV ew objects.
In total, there are six different methods:

```
1. MapDocument.findAndReplaceWorkspacePaths
2. MapDocument.replaceWorkspaces
3. Layer.findAndReplaceWorkspacePath
4. Layer.replaceDataSource
5. TableView.findAndReplaceWorkspacePath
6. TableView.replaceDataSource
```

The syntax of Map Document.findAndReplaceWorkspacePaths is


```python
MapDocument.findAndReplaceWorkspacePaths(findworkspacepath, replace_workspace_path, {validate})
```

Running this code searches for and replaces the workspace paths of all layers and tables in a map document that share that workspace.
For example, the following code replaces all the workspace paths in the current map document:



```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
mapdoc.findAndReplaceWorkspacePaths("C:/mydata", "C:/newdata")
mapdoc.save()
del mapdoc
```

The MapDocument.findAndReplaceWorkspacePaths method works on multiple workspace types at once, including shapefiles, file geodata bases, and others.
However, the workspace type cannot be modified.
The MapDocument.replaceWorkspaces method can be used to modify both the workspace path and the workspace type - for example, from a folder containing shapefiles to a file geodatabase.
The m ethod works on only one workspace at a time but can be used multiple times if more than one workspace type needs to be replaced.
The syntax of the MapDocument.replaceWorkspaces method is


```python
MapDocument.replaceWorkspaces(old_workspace_path, old_workspace_type, new_workspace_path, new_workspace_type, {validate})
```

For example, in the following code, references to shapefiles are redirected to feature classes in a file geodatabase:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
mapdoc.replaceWorkspaces("C:/mydata/shapes", "SHAPEFILEWORKSPACE", "C:/mydata/database.gdb", "FILEGDBWORKSPACE")
mapdoc.save()
del mapdoc
```

Notice exactly what happened here.
The workspace is changed, but not the dataset.
For example, if the data source for a layer was C:\mydata\hospitals.shp, it has been modified to C: \mydata\database.gdb\hospitals.
Because the type of workspace is specified, the .shp extension for the datasets is auto matically removed.
The example code assumes that feature classes with the exact same names as the shapefiles exist in the file geodatabase.
Remember that paths are not case sensitive

Valid workspace types are listed as follows:
* ACCESS_WORKSPACE
* ARCINFO_WORKSPACE
* CAD_WORKSPACE
* EXCEL_WORKSPACE
* FILEGDB_WORKSPACE
* OLEDB_WORKSPACE
* PCCOVERAGE_WORKSPACE
* RASTER_WORKSPACE
* SDE_WORKSPACE
* SHAPEFILE_WORKSPACE
* TEXT_WORKSPACE
* TIN_WORKSPACE
* VPF_WORKSPACE

Notice that "personal geodatabase" is not specifically included as a type instead ACCESS_WORKSPACE is used.

When workspaces in a map docurnent are modified, there are a few things that may not work:
* Joins and relates associated with raster layers and stand-alone tables are not updated.
* Definition queries may no longer work because a slightly different SQL syntax is used-for exarnple, between file geodatabases and personal geodatabases.
A slight modificaion to the SQL staternent would fix this problem.
* Label expressions rnay no longer work for the sarne reason.

The methods discussed so far work on map documents.
However, data sources can also be modified for individuallayers.
The Layer.findAndReplaceWorkspacePath method works on a Layer object and performs a find-and-replace operation on the workspace path for a single layer in a map document or layer file.
The syntax of this method is


```python
Layer.findAndReplaceWorkspacePath(find_workspace_path, replace_workspace_path, {validate})
```

The following code modifies the workspace for a layer that references a particular feature class in a personal geodatabase.
Only a portion of the full path of the data source is rep laced-in this case, using a different personal geodatabase:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
lyrlist = arcpy.mapping.ListLayers(mapdoc):
for lyr in lyrlist :
    if lyr.supports("DATASOORCE"):
        lyr.dataSource == "C:/mydata/database.gdb/hospitals":
            lyr.findAndReplaceWorkspacePath("database.gdb", "newdata.gdb")
mapdoc.save()
del mapdoc
```

The Layer.findAndReplaceWorkspacePath method assumes the dataset has not changed.
The replaceDataSource method can be used to change both the workspace and the dataset.
The syntax of this method is


```python
Layer.replaceDataSource(workspace_path, workspace type, dataset name, {validate})
```

The following code replaces a specific data source.
In this case, the value of the dataSource property is used to determine whether a layer should have its data source updated:


```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
lyrlist = arcpy.mapping.ListLayers(mapdoc):
for lyr in lyrlist:
    if lyr.supports("DATASOURCE"):
        lyr.dataSource == "C:/mydata/hospitals.shp":
            lyr.replaceDataSource("C:/mydata/hospitals.shp", "SHAPEFILE_WORKSPACE", "C:/mydata/newhospitals.shp")
mapdoc.save()
del mapdoc
```

The findAndReplaceWorkspacePath and replaceDataSource methods also exist for TableView objects.
The syntax for using these methods to work with single tables is very similar to the syntax for working with layers.

## 10.8 Working with page layout elements

Map scripting can also be used to work with page layout elements, including graphics, legends, pictures, text, and several others.
Typical properties that can be changed include name, size, position, and sometimes other properties that vary with each element type.
Similar to map documents, layo ut elements cannot be created using scripti so they have to already exist in a map document.
The ListLayoutElements function can be used to identify which ele ments exist within the layout of a particular map document.
The syntax of this function is


```python
ListLayoutElements(map_document, {element_type}, {wild_card})
```

The ListLayoutElements function returns a Python list of elements.
The optional parameter element_type can be used to limit the list of elements to only those of a specific type.
The specific types of elements that can be used in scripting are as follows:

* DATAFRAME_ELEMENT
* GRAPHIC_ELEMENT
* LEGEND_ELEMENT
* MAPSURROUND_ELEMENT
* PICTURE_ELEMENT
* TEXT_ELEMENT

Each of these elements corresponds to a class in the arcpy.mapping module.
Several of these elements are described in this section in a bit more detail.
When getting started with layout elements, however, it can be useful to first create an inventory of what exists.
**For example, the following code creates a list of all layout elements and prints their name and type:**


```python
import arcpy
mapdoc = arcpy.mapping MapDocument(r"C:\mydata\project.mxd")
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
    print elem.name & " " & elem.type
del mapdoc
```

The printout may look something like the following:


```python
Legend LEGEND_ELEMENT
Alternating Scale Bar MAPSURROUND_ELEMENT
North Arrow MAPSURROUND_ELEMENT
Title TEXT_ELEMENT
Study Area DATAFRAME_ELEMENT
```

Once it is determined what layout elements are available, a specific element can be selected by using:
**(1) the index number of the element,**
**(2) the element_type parameter, or**
**(3) the wild_card parameter.**
For example, to work with the title element, the following lines of code can be used to obtain a list with only the object that contains the title.
Using the index number directly:



```python
title = arcpy.mapping.ListLayoutElements(mapdoc)[3]
```


```python
title = arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT")[0]
```


```python
title = arcpy.mapping.ListLayoutElements(mapdoc, "Title")[0]
```

In the case of the element_type and wild_card parameters, theListLayoutElements function returns a list with only a single object.
Using an index number of zero ([0]) on this list returns the object instead of a list.

> Note: Not all elements have a default name, especially if they have been copied from other applications.
To use these elements in scripting, the user has to fzrst manually set the name in the map document.

Once a specific element is referenced, various properties can be accessed, such as the element's name, type, height, and width, and the x,y coordinates of the element's anchor position.
Other properties will vary with the typ e of element.
For example, an important property of the text Element object is the text property.

For a text element, all properties are read/write, with the exception of the type.
The following code modifies the text of the title in a page layout to a new string.



```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
title = arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT")[0]
title.text = "New Study Area"
mapdoc.save()
del mapdoc
```

A Picture Element object has a sourceImage property, which represents the path to the image data source.
The follow ing code illustrates how this path can be modified:



```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
elemlist = arcpy.mapping.ListLayoutElements(mapdoc, "PICTUREELEMENT")
for elem in elemlist:
    if elem.name == "photol":
        elem.sourceImage = "C:/myphotos/newimage.jpg"
mapdoc.save()
del mapdoc
```

The LegendElement object has an autoAdd property, which controls whether a layer should be automatically added to the legend when a layer is added to a data frame using the AddLayer function.
The following code illustrates how the a u toAdd property can be modified to control which layer gets added:


```python
import arcpy
mapdoc = arcpy.mapping MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mapdoc)[0]
lyr1 = arcpy.mapping.Layer("C:/mydata/Streets.lyr")
lyr2 = arcpy.mapping.Layer("C:/mydaa/Ortho.ly")
legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT")[0]
legend.autoAdd = True
arcpy.mapping.AddLayer(df, lyr1, "BOTTOM")
legend.autoAdd = False
arcpy.mapping.AddLayer(df, lyr2, "BOTTOM")
mapdoc.save()
del mapdoc
```

Another useful property of the LegendElement object is items, which returns a list of the nam es of the individuallegend items.
The LegendElement object also has one method, adjustColumnCount, which allows you to set the number of columns in the legend.

## 10.9 Exporting maps

The ArcPy mapping module has a number of exporting functions.
They are similar to the ArcMap operation File > Export Map.
There is a separate function for each format.
The functions are as follows:


* ExportToAI
* ExportToBMP
* ExportToEMF
* ExportToEPS
* ExportToGIF
* ExportToJPEG
* ExportToPDF
* ExportToPNG
* ExportToSVG
* ExportToTIFF

These functions all work in a similar manner.
The only required elements for the export functions are a map document and the path and file name of the output file.
For example, the syntax of the ExportToJPEG function is as follows:



```python
ExportToJPEG(map_document, out_jpeg, {data_frame}, {df_export_width}, {df_export_height},
             {resoluton}, {world_file}, {color_mode}, {jpeg_quality}, {progressive})
```

The dialog box options correspond directly to the parameters in the ExportToJPEG function.
All these parameters have default values, and typically only selected parameters need to be set.
The following code exports the page layout of a map document to a .jpg file, setting a resolution of 600 dpi:



```python
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/project/study.mxd")
arcpy.mapping.ExportToJPEG(mapdoc, "C:/project/final.jpg", "", "", "", 600)
del mapdoc
```

Notice the use of empty strings ("") to skip several optional parameters.

One of the optional parameters in all export functions is the data frame parameter.
This parameter makes it possible to reference an individual DataFrame object to export, exporting just the data frame in Data View without any of the layout elements.
By default, the page layout is used for export, including all data frames and layout elements.
Many of the other parameters will vary with the specific format selected


## 10.10 Printing maps

In addition to exporting maps to files, the ArcPy mapping module contains a basic PrintMap function, which prints a specific data frame or map document to a printer or file.
The syntax of this function is



```python
PrintMap(map_document, {printer_name}, {data_frame}, {out_print_file})
```

The only required parameter is a map document.
An optional printer_ name parameter can be specified to represent the name of a printer on a local computer.
If no printer is specified, the PrintMap function uses the printer that is saved with the map document or the default system printer if no printer is saved with the map document.
An optional data_frame parameter can be used to reference a specinc data frame-by default, the page layout is printed.


## 10.11 Working with PDFs

The PDF format has become widely used in the distribution of cartographic products.
In addition to the ExportToPDF function, the ArcPy.mapping module has a number of classes and functions to work with .pdf files.
First, there is the PDFDocument class.
This object allows for the manipulation of PDF documents, including the merging of pages, setting document behavior, and creating security settings.
The syntax of the PDFDocument class is



```python
PDFDocument(pdf_path)
```

The only parameter is a string that specifies the path and file name of the .pdf file.
A PDFDocument object has only one property: pageCount, which is an integer for the number of pages.
A PDFDocument object has five methods: **appendPages, insertPages, saveAndClose, update DocPropertes and updateDocSecurity**.

There are two PDFDocument functions:
1. **PDFDocumentCreate** - creates an empty PDFDocument object in memory.
The function receives a path and file name to determine the save location where a new PDF file will be created.
2. **PDFDocumentOpen** - returns a PDFDocument object from a PDF file on disk


These functions are often used to create a PDF map book.
A number of separate .pdf files can be exported from map documents - for example, using the DataDrivenPages object discussed in the next section.
These are appended in a newly created PDFDocument obj ect and saved as a final PDF map book.


The following code creates an empty PDFDocument using the PDFDocumentCreate function, and appends three existing .pdf files into a single PDF.
The saveAndClose method saves the resulting PDF, as follows:



```python
import arcpy
pdfpath = "C:/project/MapBook.pdf"
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)
pdfdoc.appendPages("C:/project/Cover.pdf")
pdfdoc.appendPages("C:/project/Map1.pdf")
pdfdoc.appendPages("C:/project/Map2.pdf")
pdfdoc.saveAndClose()
del pdfdoc
```

> The PDFDocumentCreate function does not actually create any blank PDF pages In the example at left, the actual PDF pages come from existing PDF files.
However, these pages could also be created in a script from a map document by using the ExportToPDFfunction


## 10.12 Creating map books

ArcGIS has a set of tools to create a map book, which is simpl y a collec tion of pages printed together.
A typical example of a map book includes an index page followed by individual m aps.
The index page shows the extent of the individual maps.
An example map book is shown in the figure, including an index map and two of the many individual maps.


![](ch10/10_12_1.PNG)

These map books can be created manually simply by printing each map separately.
However, ArcMap contains a toolbar called Data Driven Pages to automate this process.
More advanced map books require the use of scripting with the DataDrivenPages object in the ArcPy.mapping module.


Automating the creation of map books using scripting requires that Data Driven Pages be enabled in the map document.
This can be accomplished using the Data Driven Pages toolbar in ArcMap.
On the Setup Data Driven Pages dialog box, a layer is selected that defines a series of extents-this layer is referred to as an index layer.

![](ch10/10_12_2.PNG)

The DataDrivenPages object in the ArcPy.scripting module can be used to access the properties and methods for managing the individual pages within the map document.

> Note: A detailed explanation of how to worh with Data Driven Pages and create map books is not provided in this book.
For detailed explanalions of these procedures, see "CreatÍng a map book "and "Creating Data Driven Pages" on the Contents tab in ArcGIS Deshtop Help (Mapping > Page Layouts).


The exportToPDF method for the DataDrivenPages object can be used to create a map book in POF format.
This is not the same as the ExportToPDF function.
The syntax of the exportToPDF method is as follows:



```python
exportToPDF(Out_pdf, {page_range_type}, {page_range_string}, {multiple_files},
 {resolution}, {image qualty}, {colorspace}, {compress_vectors},
 {image_compression}, {picture_symbol}, {convert_markers}, {embed_fonts},
 {layers_attributes}, {georef_info})
```

The following code prints all the pages from a map document that has Data Driven Pages enabled to a PDF file and places an existing cover page in front:


```python
import arcpy
pdfpath = "C:/project/MapBook.pdf"
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)
mapdoc = arcpy.mapping.MapDocument("C:/project/Maps.mxd")
mapdoc.dataDrivenPages.exportToPDF("C:/project/Maps.pdf")
pdfdoc.appendPages("C:/project/Cover.pdf")
pdfdoc.appendPages("C:/project/Maps.pdf")
pdfdoc.saveAndClose()
del mapdoc
```

The Data Driven Pages toolbar and scripting can be used in combination to effectively produce map books.
Some of the inherent behavior of Data Driven Pages such as page extents, scales, dynamic text, and the like are probably easiest to control on the Setup Data Driven Pages dialog box in ArcMap , although printing the pages and merging different POF files is easiest to contr0l using scripting


## 10.13 Using sample mapping scripts

With the re1ease of ArcGIS 10, Esri started making a number of script to01s available to illustrate the use of ArcPy.
These include a set of mapping script to01s created as representative samp1es of how arcpy.
mapping can be used to perform a variety of mapping tasks .
These tools can be found in the Geo processing Model and Script Tool Gallery on the ArcGIS Resource Center.



> Note: To obtain the sample tools, go to http://resources.ArcGIS.com and in the Search box, type **arcpy.mapping sample script tools**.
This brings up a link to the sample tools
Update: https://www.arcgis.com/home/item.html?id=18c19ec00acb4d568c27bc20a72bfdc8

The sample tools consist of three different toolboxes: Cartography Tools (not to be confused with the existing Cartography system toolbox ), Export and Printing Tools, and MXD and LYR Management Tools.
Each toolbox contains a number of script tools, each of which references a Python script.


![](ch10/10_12_3.PNG)

The sample tools include most of the functionality covered earlier in this chapter.
Some of the scripts are quite short and simple.
For example, the Print Map Document(s) tool prints the layout page of one or more map documents to a local printer.
The tool dialog box, shown in the figure, allows you to select multiple map documents and select a local printer


![](ch10/10_12_4.PNG)

The Print Map Document(s) tool references the script file called PrintMXDs.py, which is included in the files you get when downloading the tools

![](ch10/10_12_5.PNG)

The script tool uses the GetParameterAsText function to get the list of map documents and the local printer from a user.
You will learn about this function in chapter 13 on creating custom tools.
The script tool then uses the PrintMap function in the arcpy.
mapping module to print the map docume nts.
It can be useful to review sample scripts like this to get ideas for your own scripts.


You can use these code examples as is, but you are encouraged to modify them or use parts of the code in your own scripts.


> **Tips**: When modifying sample scripts, you should first save a copy of the script since there is no Undo button once you save your changes to the script

## Points to remember

* The arcpy.mapping module makes it possible to automate mapping tasks.
A number of specific mapping classes and functions allow for the manipulation of map documents, data frames, layers, and page layouts.

* The functionality of the arcpy.mapping module reflects some of the typical workflows in ArcMap to produce cartographic output.
Many procedures, however, are not part of the arcpy.mapping module because they lend themselves much more to the highly visual inter face of ArcMap.
For example, most of the layer symbology properties can be set only on the Layer Properties dialog box in ArcMap.
The arcpy.mapping module can be used to automate certain repetitive tasks, such as updating the data sources for a large number of layers or replacing text in a large number of map documents.


* Map documents can be opened by refer xd fil es on disk or by calling the map document currently in use.
Map document prop erties can be accessed, modified, and saved.
The arcpy.mapping module cannot create new map documents.


* Data frames within a map document can be accessed using the ListDataFrames function.
Data frame properties can be accessed, modified, and saved.


* Layers within a data frame can be accessed using the Layer and ListLayers functions.
Layer properties can be accessed, modified, and saved.


* Broken data sources in map documents can be identified using the ListBrokenDataSources function.
Various methods exist to fix broken data sources for map document, layer, and table view objects.
These methods can find and replace workspaces, wo rkspace paths, and data sources.


* Individual elements on page layouts can be accessed and modified.


* Maps can be exported to various formats, including PDF, JPEG, and TIFF formats.
Maps can also be printed to a local printer or to PDF form at.
When Data Driven Pages is enabled, scripting can be used to create a map book in PDF format.



```python

```
