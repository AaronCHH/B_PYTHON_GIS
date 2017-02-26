
# Chapter 6: Exploring spatial data

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 6: Exploring spatial data](#chapter-6-exploring-spatial-data)
  * [6.1 Introduction](#61-introduction)
  * [6.2 Checking for the existence of data](#62-checking-for-the-existence-of-data)
  * [6.3 Describing data](#63-describing-data)
  * [6.4 Listing data](#64-listing-data)
    * [ListFeatureClasses](#listfeatureclasses)
    * [ListRasters](#listrasters)
    * [ListFields](#listfields)
  * [6.5 Using lists in for loops](#65-using-lists-in-for-loops)
  * [6.6 Working with lists](#66-working-with-lists)
  * [6.7 Working with tuples](#67-working-with-tuples)
  * [6.8 Working with dictionaries](#68-working-with-dictionaries)
  * [Points to remember](#points-to-remember)

<!-- tocstop -->

## 6.1 Introduction

>This chapter describes several approaches to exploring spatial data, including checking for the existence of datasets and describing datasets in a workspace.

> List functions can be used not only to list datasets, but also to list elements such as workspaces, fields, and tables. Lists are common in scripts because they make it possible to iterate over a large number of elements.

> The built-in Python functions can be used to manipulate lists. Tuples and dictionaries are also introduced in this chapter as additional data structures.

## 6.2 Checking for the existence of data

* The syntax of the Exists function is
```py
arcpy.Exists(<dataset>)
```

* For example, the following code determines whether a particular shapefile exists:
```py
import arcpy
prlnt = arcpy.Exists("C:/Data/streams.shp")
```

## 6.3 Describing data

* In a Python script, you can use the Describe function to determine the feature type of a dataset before using it in a tool.
The syntax to describe a dataset is as follows:
```py
import arcpy
<variable> = arcpy.Describe(<input dataset>)
```

* Running the code returns an object that contains the properties of the data set. These properties can be accessed using an ```<object>.<property>``` statement.
For example, the following code describes a shape and then prints the geometry shape type:


```python
import arcpy
desc = arcpy.Describe("C:/Data/streams.shp")
print desc.shapeType
```

* For example, the following code determines the geometry shape type of the clip features, and the Clip tool is run only if the shape type is polygons:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
infc = "streams.shp"
clipfc = "study.shp"
outfc = "result.shp"
desc = arcpy.Describe(clipfc)
type = desc.shapeType
if type == "Polygon":
    arcpy.Clip_analysis(infc, clipfc, outfc)
else:
    print "The clip features are not polygons."
```

* The following code describes a shapefile and prints the type of dataset and the name of the spatial reference:


```python
import arcpy
fc = "C:/Data/streams.shp"
desc = arcpy.Describe(fc)
sr = desc.spatialReference
print "Dataset type:" + desc.datasetType
print "Spatial reference:" + sr.name
```

* For example, the following code determines the dataset type of an element inside a geodatabase


```python
import arcpy
element = "C:/Data/study.gdb final"
desc = arcpy.Describe(element)
print "Dataset type:" + desc.datasetType
```

* The Describe function also returns a number of properties for Descr objects. It includes such properties as the file path, catalog path, name, file name, and base name. Running the following code prints a number of these different properties:


```python
import arcpy
arcpy.env.workspace = "C:/Data/study.gdb"
element = "roads"
desc = arcpy.Describe(element)
print " Data type: " + desc.dataType
print " File path: " + desc.path
print " Catalog path: " + desc.catalogPath
print " File name: " + desc.file
print " Base name: " + desc.baseName
print " Name: " + desc.name
```

## 6.4 Listing data

> Batch processing is one of the primary reasons for developing geoprocessing scripts.

> The ArcPy list functions include ListFields, ListIndexes, ListDatasets, ListFeatureClasses, ListFiles, ListRasters , ListTables, ListWorkspaces and ListVersions.

> All functions have a wild card(*), which defines a name filter. This filter is used to list only the elements that meet a particular criterion.

### ListFeatureClasses

* The List FeatureClasses function returns a list of feature classes in the current workspace. The syntax of the function is
```py
ListFeatureClasses({wild_card}, {feature_type}, {feature_dataset})
```

* This function has three parameters, all of which are optional. These parame ters make it possible to limit the list by name, feature type, or feature dataset. For example, the following code returns a list of all feature classes in the current workspace:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fclist = arcpy.ListFeatureClasses()
```

* All the list functions return a Python list. To confirm the contents of a list, you can print the values using a statement like the following:
```py
print fclist
```

* The wild card can be used to limit the list by name. For example, the following code creates a list of all feature classes in th e current workspace
that start with the letter w:
```py
fclist = arcpy.ListFeatureClasses("w*")
```

> Note: Remember that string values preceded by the letter **u** are **Unicode strings**.
Unicode strings work just like regular strings but are more robust when working with different international character sets

* The second parameter in the ListFeatureClasses function is the feature type. This parameter can be used to restrict the list to match certain data properties, such as point feature classes only.
For example, the following code creates a list of all the point feature classes in the current workspace:
```py
fclist = arcpy.ListFeatureClasses("", "point")
```
* Notice the use of an empty string ("") for the wild card. Parameters have to be entered in the order defined by the syntax and cannot be skipped unless you specifically refer to them by name. Using " *" would give the same result, in this case.
* Valid feature types include **annotation, arc, dimension, edge, junction, label, line, multipatch, node, point, polygon, polyline, region, route, and tic**.


### ListRasters

* To create a list of raster datasets in the current workspace, you can use the ListRasters function. The syntax is very similar to the **ListFeatureClasses** function:
```py
ListRasters( {wild_card}, {raster_type} )
```

* The two parameters are optional and allow you to restrict the list by name or type. The following code creates a list of all raster datasets in the current workspace:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
rasterlist = arcpy.ListRasters()
```

* To restrict the list to all rasters that are TIFF images, you can specify the raster type parameter as follows:


```python
rasterlist = arcpy.ListRasters("", "tif")
```

A complete list of supported raster data types can be found in ArcGIS Desktop Help. The raster type parameter should be specified as the file extension, not the generic name of the format.
For exampl e, a TIFF file has the file extension .tif, so tif is the correct syntax. Similarly, a JPEG file has the file extension .jpg, so jpg is the correct syntax.
The syntax for raster data types is not case sensitive, so both TIF and tif are correct.
Also note that the Esri GRID format does not have a file extension and the proper syntax for this format is GRID (also not case sensitive).

### ListFields

* Another list function is ListFields. This function lists the fields in a feature class or table in a specified dataset.
The syntax is
```py
ListFields(dataset , {wild card} , {field type})
```


* The **ListFields** function has three parameters-name, field type, and dataset-of which the dataset is required. The dataset is the specified features class or table whose fields will be returned as values in a list. For example, the fo llowing code creates a list of all the fields in a shapefile:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fieldlist = arcpy.ListFields("roads.shp")
```

* The two optional parameters allow you to restrict the list by name or field type. The following code creates a list of all the fields in a shapefile that are integers:
```py
fieldlist = arcpy.ListFields("roads.shp", "", "Integer")
```

* Valid field types include All, **BLOB (binary large object) , Date, Double, Geometry, GUID (globally unique identifier) , Integer, OID (object identifier), Raster, Single, SmallInteger, and String**.

* Field types are strings and are **not** case sensltive

* The ListFields function returns a list of field objects. By contrast, most of the other list functions return a list of strings. Field object properties include the **field name, alias, type, and length**. For example, the following script creates a list of fields of type String and determines for each text field what the length of the field is:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fieldlist = arcpy.ListFields("roads.shp", "", "String")
for field in fieldlist:
    print field.name + " " + str(field.length)
```

* The length property returns an integer and is converted to a string for printing purposes.

## 6.5 Using lists in for loops

Once you have the list of desired values, you can use the list for batch processing. This is most commonly accomplished using a for loop . A for loop can be used to iterate over the list, one element at a time, and when there are no values left to be iterated, the loop is finished. For example, consider using a for loop with raster data. The code is as follows:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
tifflist = arcpy.ListRasters("", "TIF")
for ff in tifflist:
    arcpy.BuildPyramids_management(tiff)
```

In this example, the ListRasters function is used to create a list of TIFF files.
The for loop iterates over each element in the list and builds pyramids for each.
This becomes quite powerful because it can automate rather tedious tasks.
For example, building pyramids for hundreds of rasters could become quite time consuming.
The few lines of Python code used here carry out this task and the code is the same whether there are only a few raster datasets or several hundreds.

---

Iteration using a for loop can also be used in combination with the ListFields function to provide a detailed description of the fields and their properties.
The following code creates a list of fields in a single shapefile, and then prints the name, type, and length of each field:


```python
import arcpy
from arcpy mport env
env.workspace = "C:/Data"
fieldlist = arcpy.ListFields("roads.shp")
for field in fieldlist :
    print "{0} is a type of {1} with a length of {2}".format(field.name, field.type, field.length)
```

## 6.6 Working with lists

Lists are a versatile Python type and can be manipulated in many different ways.
So although a list of feature classes, fields, or rasters is created using an ArcPy function, the list can be manipulated in Python using the functions and methods of a Python list.
Following are a few examples.
The number of feature classes in a workspace can be determined using the built-in Python len function. The code is as follows:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data/study.gdb"
fcs = arcpy.ListFeatureClasses()
print len(fcs)
```

**Lists can be sorted using the sort method**. The default sorting is in alphanumerical order, but it can be reversed using the reverse argument of the sort method. The following code creates a list of feature classes, sorts them alphanumerically, and prints their names. The sorting is then reversed and the names are printed again. The code is as follows:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data/study.gdb"
fcs = arcpy.ListFeatureClasses()
fcs.sort()
print fcs
fcs.sort(reverse = True)
print fcs
```

> Working with lists is covered in more detail in chapter 4, including the use of indexing, slicing, and list methods. All of it can be used when working with lists of **feature classes, tables, fields, rasters**, or other spatial data types.

## 6.7 Working with tuples

Lists are common in Python, and you will often use lists when writing geo processing scripts, including lists of map documents, layers, feature classes, fields, and more. Lists are quite versatile since you can modify them in many ways, as discussed in the previous section.

**Sometimes, however, you may want to use a list without allowing its elements to be modified.** That is where tuples come in. Tuples are sequences of elements, just like lists, but tuples are immutable, meaning they cannot be changed. The syntax of a tuple is simple-separate a set of values with commas (, ), and you have a tuple. For example, the following code returns a tuple with five elements:
```py
>>> 1 , 2 , 3 , 4 , 5
```

How to get a tuple with only one element? Add a comma (,), even though there is no element following the comma:
```py
>>> 6,
```

Working with tuples is similar to working with lists. Elements in the tuple have an index value, which can be used to obtain specific elements of the tuple. For example:
```py
>>> x = ("a", "b" ,"c")
>>> x[0]
```

However, the sequence of elements cannot be modified. **So list operations such as deleting, appending, removing, and others are not supported by tuples**. The only methods that work on tuples are count and index because these methods do not modify the sequence of elements. Other operations can be applied but return a different tuple. Running the follow ing code slices a tuple and returns a different tuple:


```python
>>> x ("a", "b", "c", "d", "e", "f", "g")
>>> x[2:5]
```

> Notice that the slicing operation returns another tuple , not a list. You can not modify the elements of a tuple, unlike the elements of a list.

If you cannot modify a tuple, why are tuples important? First, some built-in Python functions and modules return tuples-in which case, you have to deal with them. Second, tuples are often used in dictionaries, which are covered next.

> TIP: In general, if you are using a set of values that won't be modified, use a tuple instead of a list.

## 6.8 Working with dictionaries

Lists and tuples are useful for gro uping elements into a structure, and the elements can be referred to by their index number, starting with zero (0) Working with index numbers works fine, but it has its limitations. Consider the example of the following list of cities:
```py
cities = ["Austin", "Baltimore", "Cleveland", "Denver"]
```

Suppose you want to have a database that contains the state for each city.
You can do this by creating a list as follows:
```py
states = ["Texas", "Maryland", "Ohio", "Colorado"]
```

Because the index numbers correspond, you can access elements from one list by using the index number from the other list. For example, to get the state for Cleveland, you can use the following code:
```py
>>> states[cities.index("Cleveland")]
```

This process is useful but cumbersome. Imagine lists that have a large number of elements. In addition, some states will have more than one city. Making only a minor edit to one of the lists could disrupt the entire sequence. You can use tuples to ensure no changes are made to the sequence, but that also has its limitations. What you really need is a lookup table that would work as follows:
```py
>>> statelookup["Cleveland"]
```

A lookup table is commonly used to display information from one table based on a corresponding value in another table. A Table Join operation in ArcGIS is an example of using a lookup table. In Python , one way to implement a lookup table is to use a dictionary. Dictionaries consist of pairs of keys and their corresponding values. Pairs are also referred to as the items of the dictionary. A dictionary item consists of a key, followed by a colon (:), and then the corresponding value. Items are separated by a comma (,). The dictionary itself is surrounded by curly brackets({}).

The dictiona for the preceding examp le would look as follows:
```py
>>> statelookup = {"Austin":"Texas", "Baltimore":"Maryland", "Cleveland":"Ohio", "Denver":"Colorado"}
```
You can now use this dictionary to look up the state for each city:
```py
>>> statelookup["Cleveland"]
```
The result is 'Ohio'.

**The order in which the items were created in the dictionary does not matter.** The dictionary can be modified, and as long as the pairs of keys and their corresponding values are intact, the dictionary will continue to func tion. Keep in mind when creating the dictionary that the keys have to be unique, but the values do not.

---

Dictionaries can be created and populated at the same time, as in the preceding statelookup example. You can also create an empty dictionary first using only curly brackets ({}), and then add items to it. Here is the code to create a new empty dictionary:
```py
>>> zoning = {}
```

Items can be added using square brackets ({}) and an assignment statement as follows:
```py
>>> zoning["RES"] = "Residential"
```

You can continue to add items to the dictionary. Elements are sorted in
alphanumerical order based on the key. The code is as follows:
```py
>>> zoning["IND"] = "Industry"
>>> zoning["WAT"] = "Water"
>>> print zoning
```

Items can be modified using the same syntax. Setting the value using a key that is already in use overwrites the existing value. The code is as follows:
```py
>>> zoning["IND"] = "Industrial"
>>> print zoning
```

Items can be deleted using square brackets ([]) and the keyword del as follows:
```py
>>> del zoning["WAT"]
>>> print zoning
```

There are several dictionary methods. The keys method returns a list of all the keys in the dictionary, follows:
```py
>>> zoning.keys()
```

The values method returns a list of all the values in the dictionary, as follows:
```py
>>> zoning.values( )
```

The items method returns a list of all items in the dictionary-that is, all key-value pairs, as follows:
```py
>>> zoning.items()
```

Dictionaries are not common in ArcPy, but there is one function that uses them: GetInstallInfo. This function returns a Python dictionary that contains the information on the installation type properties. The general syntax of the Getln s talllnfo function is:
```py
Getlnstalllnfo(Install_name)
```

For example, the following code returns the installation information for the product being used in Python:


```python
import arcpy
install = arcpy.GetInstallInfo()
for key in install:
    print "{0}:{1}".format(key, install[key])
```

    SourceDir:G:\Desktop\
    InstallDate:9/11/2016
    InstallDir:c:\program files (x86)\arcgis\desktop10.1\
    ProductName:Desktop
    BuildNumber:3143
    InstallType:N/A
    Version:10.1
    SPNumber:1
    Installer:AaronHsu
    SPBuild:10.1.1.3143
    InstallTime:13:24:39


## Points to remember

* The Exists function can be used to determine whether a particular dataset exists. The Descrbe function can be used to describe the properties of a dataset. These functions are commonly used to ensure that inputs for a script conform to expectations.


* List functions are used to facilitate batch processing. Once a list of elements is created, a script can be design ed to iterate over all the elements in the list. For example, the ListFeatureClasses function can be used to create a list of all feature classes in a workspace, and a for loop can be used to iterate over all the elements in the list to perform the same operation on each feature class. List functions exist for different types of elements, including workspaces, files, datasets , feature classes, fields, rasters, tables , and others. Lists are very common ìn scripts.


* Tuples and dictionaries are important data structures in Python. A tuple is a sequence of elements, just like a list, but the elements of a tuple cannot be changed. A dictionary consists of pairs of keys and their corresponding values. Dictionaries work the same way as lookup tables.


```python

```
