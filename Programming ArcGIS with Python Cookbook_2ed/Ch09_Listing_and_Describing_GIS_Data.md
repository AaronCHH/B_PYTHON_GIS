
# Chapter 9: Listing and Describing GIS Data

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 9: Listing and Describing GIS Data](#chapter-9-listing-and-describing-gis-data)
  * [9.1 Introduction](#91-introduction)
  * [9.2 Working with the ArcPy list functions](#92-working-with-the-arcpy-list-functions)
    * [9.2.1 Getting ready](#921-getting-ready)
    * [9.2.2 How to do it](#922-how-to-do-it)
    * [9.2.3 How it works](#923-how-it-works)
    * [9.2.4 There's more](#924-theres-more)
  * [9.3 Getting a list of fields in a feature class or table](#93-getting-a-list-of-fields-in-a-feature-class-or-table)
    * [9.3.1 Getting ready](#931-getting-ready)
    * [9.3.2 How to do it](#932-how-to-do-it)
    * [9.3.3 How it works](#933-how-it-works)
  * [9.4 Using the Describe() function to return descriptive information about a feature class](#94-using-the-describe-function-to-return-descriptive-information-about-a-feature-class)
    * [9.4.1 Getting ready](#941-getting-ready)
    * [9.4.2 How to do it](#942-how-to-do-it)
    * [9.4.3 How it works](#943-how-it-works)
  * [9.5 Using the Describe() function to return descriptive information about a raster image](#95-using-the-describe-function-to-return-descriptive-information-about-a-raster-image)
    * [9.5.1 Getting ready](#951-getting-ready)
    * [9.5.2 How to do it](#952-how-to-do-it)
    * [9.5.3 How it works](#953-how-it-works)

<!-- tocstop -->

In this chapter, we will cover the following recipes:

* Working with the ArcPy list functions
* Getting a list of fields in a feature class or table
* Using the Describe() function to return descriptive information about a feature class
* Using the Describe() function to return descriptive information about a raster image


## 9.1 Introduction

Python provides you with the ability to batch process data through scripting.
This helps you automate workflows and to increase the efficiency of your data processing.
For example, you may need to iterate through all datasets on disk and perform a specific action for each dataset.
The first step is often to perform an initial gathering of data before proceeding to the main body of the geoprocessing task.
This initial data gathering is often accomplished through the use of one or more list methods found in ArcPy.
These lists are returned as true Python list objects.
These list objects can then be iterated for further processing.
ArcPy provides a number of functions that can be used to generate lists of data.
These methods work on many different types of GIS data.
In this chapter, we will examine the many functions provided by ArcPy to create lists of data.
In Chapter 2, Managing Map Documents and Layers, we also covered a number of list functions.
However, these functions were related to working with the arcpy.mapping module, and specifically, for working with map documents and layers.
The list functions we cover in this chapter reside directly in ArcPy and are more generic in nature.


We will also cover the Describe() function to return a dynamic object that will contain property groups.
These dynamically generated Describe objects contain property groups that are dependent on the type of data that has been described.
For instance, when the Describe() function is run against a feature class, properties specific to a feature class will be returned.
In addition to this, all data, regardless of the data type, acquires a set of generic properties, which we'll discuss shortly.


## 9.2 Working with the ArcPy list functions

Getting a list of data is often the first step in a multistep geoprocessing operation.
ArcPy provides many list functions that you can use to gather lists of information, whether they are feature classes, tables, workspaces, and so on.
After gathering a list of data, you will often perform geoprocessing operations against the items in the list.
For example, you might want   to add a new field to all the feature classes in a file geodatabase.
To do this, you'd first need to get a list of all the feature classes in the workspace.
In this recipe, you'll learn how to use the list functions in ArcPy by working with the ListFeatureClasses() function.
All the ArcPy list functions work in the same fashion.


### 9.2.1 Getting ready

ArcPy provides functions to get lists of fields, indexes, datasets, feature classes, files, rasters, tables, and more.
All the list functions perform the same type of basic operations.
The ListFeatureClasses() function can be used to generate a list of all feature classes in a workspace.
The ListFeatureClasses() function has three optional arguments that can  be passed into the function that will serve to limit the returned list.
The first optional argument is a wildcard that can be used to limit the feature classes that are returned based on a name, and the second optional argument can be used to limit the feature classes that are returned based on a data type (such as point, line, polygon, and so on).
The third optional parameter limits the returned feature classes by a feature dataset.
In this recipe, you will learn how to use the ListFeatureClasses() function to return a list of feature classes.
You'll also learn how to restrict the list that is returned.


### 9.2.2 How to do it

Follow these steps to learn how to use the ListFeatureClasses() function to retrieve a list of the feature classes in a workspace:

1. Open IDLE and create a new script window.

2. Save the script as C:\ArcpyBook\Ch9\ListFeatureClasses.py.

3. Import the arcpy module:
```py
import arcpy
```

4. Set the workspace:
```py
arcpy.env.workspace = "C:/ArcpyBook/data/CityOfSanAntonio.gdb"
```
> You should always remember to set the workspace using the environment settings before calling any list function in a script developed with IDLE or any other Python development environment.
If this isn't done, the list function would not know which dataset the list should be pulled from. If the script is run inside ArcMap,   it returns the feature classes from the default geodatabase if you don't set the workspace.

5. Call the ListFeatureClasses() function and assign the results to a variable called fcList:
```py
fcList = arcpy.ListFeatureClasses()
```

6. Loop through each of the feature classes in fcList and print them to the screen:
```py
for fc in fcList: print(fc)
```

7. You can check your work by examining the C:\ArcpyBook\code\Ch9\ ListFeatureClasses_Step1.py solution file.

8. Save and run the script. You should see this output.
```py
Crimes2009
CityBoundaries
CrimesBySchoolDistrict
SchoolDistricts
BexarCountyBoundaries
Texas_Counties_LowRes
```

9. The list of feature classes returned by the ListFeatureClasses() function can be restricted through the use of a wildcard passed as the first parameter.
The wildcard is used to restrict the contents of your list based on a name.
For example, you may want to return only a list of feature classes that start with C.
To accomplish this, you can use an asterisk along with a combination of characters.
Update the ListFeatureClasses() function to include a wildcard that will find all feature classes that begin with an uppercase C and also have any number of characters:
```py
fcList = arcpy.ListFeatureClasses("C*")
```

10. You can check your work by examining the C:\ArcpyBook\code\Ch9\ ListFeatureClasses_Step2.py solution file.

11. Save and run the script to see this output:
```py
Crimes2009
CityBoundaries
CrimesBySchoolDistrict
```

12. In addition to using a wildcard to restrict the list returned by the ListFeatureClasses() function, a type restriction can also be applied, either in conjunction with the wildcard or by itself. For example, you could restrict the list of feature classes that are returned to contain only feature classes that begin with C and have a polygon data type. Update the ListFeatureClasses() function to include a wildcard that will find all feature classes that begin with an uppercase C and have a polygon data type:
```py
fcs = arcpy.ListFeatureClasses("C*", "Polygon")
```

13. You can check your work by examining the C:\ArcpyBook\code\Ch9\ ListFeatureClasses_Step3.py solution file.

14. Save and run the script. You will see the following output:
```py
CityBoundaries
CrimesBySchoolDistrict
```

### 9.2.3 How it works

Before calling any list functions, you will need to set the workspace environment setting that sets the current workspace from which you will generate the list.
The ListFeatureClasses() function can accept three optional parameters, which will limit  the feature classes that are returned.
The three optional parameters include a wild card, feature type, and feature dataset.
In this recipe, we've applied two of the optional parameters including a wildcard and a feature type.
Most of the other list functions work the same way.
The parameter types will vary, but how you call the functions will essentially be the same.


### 9.2.4 There's more

Instead of returning a list of feature classes in a workspace, you may need to get a list of tables.
The ListTables() function returns a list of standalone tables in a workspace.
This list can be filtered by name or table type.
Table types can include dBase, INFO, and ALL.
All values in the list are of the string data type and contain table names.
Other list functions include ListFields(), ListRasters(), ListWorkspaces(), ListIndexes(), ListDatasets(), ListFiles(), and ListVersions().



## 9.3 Getting a list of fields in a feature class or table

Feature classes and tables contain one or more columns of attribute information.
You can get a list of the fields in a feature class through the ListFields() function.


### 9.3.1 Getting ready

The ListFields() function returns a list containing individual Field objects for each field in a feature class or table.
Some functions, such as ListFields() and ListIndexes(), require an input dataset to operate on.
You can use a wildcard or field type to constrain the list that is returned.
Each Field object contains various read-only properties including Name, AliasName, Type, Length, and others.


### 9.3.2 How to do it

Follow these steps to learn how to return a list of fields in a feature class.

1.  Open IDLE and create a new script window.

2.  Save the script as C:\ArcpyBook\Ch9\ListOfFields.py.

3.  Import the arcpy module:
```py
import arcpy
```

4.  Set the workspace:
```py
arcpy.env.workspace = "C:/ArcpyBook/data/CityOfSanAntonio.gdb"
```

5.  Call the ListFields() method on the Burglary feature class inside a try block:
```py
try:
    fieldList = arcpy.ListFields("Burglary")
```

6.  Loop through each of the fields in the list of fields and print out the name, type, and
length.
Make sure you indent as needed:
```py
for fld in fieldList:
    print("%s is a type of %s with a length of %i" % (fld.name, fld.type, fld.length))
```

7.  Add the Exception block:
```py
except Exception as e: print(e.message)
```

8.  The entire script should appear as follows:
```py
import arcpy
arcpy.env.workspace = "C:/ArcpyBook/data/CityOfSanAntonio.gdb"
try:
    fieldList = arcpy.ListFields("Burglary")
    for fld in fieldList:
        print("%s is a type of %s with a length of %i" % (fld.name, fld.type, fld.length))
except Exception as e:
    print(e.message)
```

9.  You can check your work by examining the C:\ArcpyBook\code\Ch9\ ListOfFields.py solution file.

10. Save and run the script. You should see the following output:
```
OBJECTID is a type of OID with a length of 4
Shape is a type of Geometry with a length of 0
CASE is a type of String with a length of 11
LOCATION is a type of String with a length of 40
DIST is a type of String with a length of 6
SVCAREA is a type of String with a length of 7
SPLITDT is a type of Date with a length of 8
SPLITTM is a type of Date with a length of 8
HR is a type of String with a length of 3
DOW is a type of String with a length of 3
SHIFT is a type of String with a length of 1
OFFCODE is a type of String with a length of 10
OFFDESC is a type of String with a length of 50
ARCCODE is a type of String with a length of 10
ARCCODE2 is a type of String with a length of 10
ARCTYPE is a type of String with a length of 10
XNAD83 is a type of Double with a length of 8
YNAD83 is a type of Double with a length of 8
```


### 9.3.3 How it works

The ListFields() function returns a list of fields from a feature class or a table.
This function accepts one required parameter, which is a reference to the feature class or table the function should be executed against.
You can limit the fields returned by using a wildcard or a field type.
In this recipe, we only specified a feature class that indicates that all the fields will be returned.
For each field returned, we printed the name, field type, and field length.
As I mentioned earlier when discussing the ListFeatureClasses() function, ListFields() and all the other list functions are often called as the first step in a multistep process within a script.
For example, you might want to update the population statistics contained within a population field for a census tract feature class.
To do this, you could get a list of all the fields within a feature class, loop through this list by looking for a specific field name that contains information on the population, and then update the population information for each row.
Alternatively, the ListFields() function accepts a wildcard as one of its parameters, so if you already know the name of the population field, you would pass this as the wildcard and only a single field will be returned.



## 9.4 Using the Describe() function to return descriptive information about a feature class

All datasets contain information that is descriptive in nature.
For example, a feature class has a name, shape type, spatial reference, and so on.
This information can be valuable to your scripts when you are seeking specific information before continuing with further processing in the script.
For example, you might want to perform a buffer only on polyline feature classes instead of points or polygons.
Using the Describe() function, you can obtain basic descriptive information about any dataset.
You can think of this information as metadata.


### 9.4.1 Getting ready

The Describe() function provides you with the ability to get basic information about datasets.
These datasets could include feature classes, tables, ArcInfo coverages, layer files, workspaces, rasters, and so on.
A Describe object is returned and contains specific properties, based on the data type being described.
Properties on the Describe object are organized into property groups and all datasets fall into at least one property group.
For example, performing Describe() against a geodatabase would return the GDB FeatureClass, FeatureClass, Table, and Dataset property groups.
Each of these property groups contains specific properties that can be examined.

The Describe() function accepts a string parameter, which is a pointer to a datasource.
In the following code example, we pass a feature class that is contained within a file geodatabase.
The function returns a Describe object that contains a set of dynamic properties called property groups.
We can then access these various properties as we have done in this case by simply printing out the properties using the print function:
```py
arcpy.env.workspace = "c:/ArcpyBook/Ch9/CityOfSanAntonio.gdb" desc = arcpy.Describe("Schools")
print("The feature type is: " + desc.featureType)
The feature type is: Simple
print("The shape type is: " + desc.shapeType)
The shape type is: Polygon print("The name is: " + desc.name)
The name is: Schools
print("The path to the data is: " + desc.path)
The path to the data is: c:/ArcpyBook/Ch9/CityOfSanAntonio.gdb
```

All datasets, regardless of their type, contain a default set of properties located on the Describe object.
These are read-only properties.
Some of the more commonly used properties include dataType, catalogPath, name, path, and file.

In this recipe, you will write a script that obtains descriptive information about a feature class using the Describe() function.


### 9.4.2 How to do it

Follow these steps to learn how to obtain descriptive information about a feature class:

1.  Open IDLE and create a new script window.

2.  Save the script as C:\ArcpyBook\Ch9\DescribeFeatureClass.py.

3.  Import the arcpy module:
```py
import arcpy
```

4.  Set the workspace:
```py
arcpy.env.workspace = "C:/ArcpyBook/data/CityOfSanAntonio.gdb"
```

5.  Start a try block:
```py
try:
```

6.  Call the Describe() function on the Burglary feature class and print out the shape type:
```py
descFC = arcpy.Describe("Burglary")
print("The shape type is: " + descFC.ShapeType)
```

7.  Get a list of fields in the feature class and print out the name, type, and length
of each:
```py
flds = descFC.fields for fld in flds:
    print("Field: " + fld.name)
    print("Type: " + fld.type
    print("Length: " + str(fld.length))
```

8.  Get the geographic extent of the feature class and print out the coordinates that
define the extent:
```py
ext = descFC.extent
print("XMin: %f" % (ext.XMin))
print("YMin: %f" % (ext.YMin))
print("XMax: %f" % (ext.XMax))
print("YMax: %f" % (ext.YMax))
```

9.  Add the Exception block:
```py
except Exception as e: print(e.message)
```

10. The entire script should appear as follows:
```py
import arcpy arcpy.env.workspace =
"c:/ArcpyBook/data/CityOfSanAntonio.gdb"
try
  descFC = arcpy.Describe("Burglary")
  print("The shape type is: " + descFC.ShapeType)
  flds = descFC.fields
  for fld in flds:
    print("Field: " + fld.name)
    print("Type: " + fld.type)
    print("Length: " + str(fld.length))
    ext = descFC.extent
    print("XMin: %f" % (ext.XMin))
    print("YMin: %f" % (ext.YMin))
    print("XMax: %f" % (ext.XMax))
    print("YMax: %f" % (ext.YMax))
except:
  print(arcpy.GetMessages())
```

11. You can check your work by examining the C:\ArcpyBook\code\Ch9\ DescribeFeatureClass.py solution file.

12. Save and run the script. You should see the following output:
```py
The shape type is: Point Field: OBJECTID
Type: OID Length: 4 Field: Shape Type: Geometry Length: 0 Field: CASE Type: String Length: 11 Field: LOCATION
Type: String Length: 40
```

### 9.4.3 How it works

Performing a Describe() against a feature class, which we have done in this script, returns a FeatureClass property group along with access to the Table and Dataset property groups, respectively.
In addition to returning a FeatureClass property group, you also have access to a Table properties group.

The Table property group is important primarily because it gives you access to the fi  lds in a standalone table or feature class.
You can also access any indexes on the table or feature class through this property group.
The Fields property in Table Properties returns a Python list containing one Field object for each fi ld in the feature class.
Each fi ld has a number of read- only properties including the name, alias, length, type, scale, precision, and so on.
The most obviously useful properties are name and type.
In this script, we printed out the fi  ld name, type, and length.
Note the use of a Python for loop to process each field in the Python list.

Finally, we printed out the geographic extent of the layer through the use of the Extent object, returned by the extent property in the Dataset property group.
The Dataset property group contains a number of useful properties.
Perhaps, the most used properties include extent and spatialReference, as many geoprocessing tools and scripts require this information at some point during execution.
You can also obtain the datasetType and versioning information along with several other properties.



## 9.5 Using the Describe() function to return descriptive information about a raster image

Raster files also contain descriptive information that can be returned by the Describe() function.


### 9.5.1 Getting ready

A raster dataset can also be described through the use of the Describe() function.
In this recipe, you will describe a raster dataset by returning its extent and spatial reference.
The Describe() function contains a reference to the general purpose Dataset properties group and also contains a reference to the SpatialReference object for the dataset.
The SpatialReference object can then be used to get detailed spatial reference information for the dataset.


### 9.5.2 How to do it

Follow these steps to learn how to obtain descriptive information about a raster image file.

1. Open IDLE and create a new script window.

2. Save the script as C:\ArcpyBook\Ch9\DescribeRaster.py.

3. Import the arcpy module:
```py
import arcpy
```

4. Set the workspace:
```py
arcpy.env.workspace = "C:/ArcpyBook/data"
```

5. Start a try block:
```py
try:
```

6. Call the Describe() function on a raster dataset:
```py
descRaster = arcpy.Describe("AUSTIN_EAST_NW.sid")
```

7. Get the extent of the raster dataset and print it out:
```py
ext = descRaster.extent
print("XMin: %f" % (ext.XMin))
print("YMin: %f" % (ext.YMin))
print("XMax: %f" % (ext.XMax))
print("YMax: %f" % (ext.YMax))
```

8. Get a reference to the SpatialReference object and print it out:
```py
sr = descRaster.SpatialReference print(sr.name)
print(sr.type)
```

9. Add the Exception block:
```py
except Exception as e: print(e.message)
```

10. The entire script should appear as follows:
```py
import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data" try:
descRaster = arcpy.Describe("AUSTIN_EAST_NW.sid") ext = descRaster.extent
print("XMin: %f" % (ext.XMin))
print("YMin: %f" % (ext.YMin))
print("XMax: %f" % (ext.XMax))
print("YMax: %f" % (ext.YMax))
sr = descRaster.SpatialReference print(sr.name)
print(sr.type) except Exception as e:
print(e.message)
```

11. You can check your work by examining the C:\ArcpyBook\code\Ch9\ DescribeRaster.py solution file.

12. Save and run the script. You should see the following output:
```py
XMin: 3111134.862457
YMin: 10086853.262238
XMax: 3131385.723907
YMax: 10110047.019228
NAD83_Texas_Central Projected
```

### 9.5.3 How it works

This recipe is very similar to previous recipes.
The difference is that we're using the Describe() function against a raster dataset instead of a vector feature class.
In both cases, we've returned the geographic extent of the datasets using the extent object.
However, in the script, we've also obtained the SpatialReference object for the raster dataset and printed out information about this object including its name and type.
