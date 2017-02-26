
# Chapter 9: Working with rasters

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 9: Working with rasters](#chapter-9-working-with-rasters)
  * [9.1 Introduction](#91-introduction)
  * [9.2 Listing rasters](#92-listing-rasters)
  * [9.3 Describing raster properties](#93-describing-raster-properties)
  * [9.4 Working with raster objects](#94-working-with-raster-objects)
  * [9.5 Working with the ArcPy Spatial Analyst module](#95-working-with-the-arcpy-spatial-analyst-module)
  * [9.6 Using map algebra operators](#96-using-map-algebra-operators)
  * [9.7 Using the ApplyEnvironment function](#97-using-the-applyenvironment-function)
  * [9.8 Using classes of the arcpy.sa module](#98-using-classes-of-the-arcpysa-module)
  * [9.9 Using raster functions to work with NumPy arrays](#99-using-raster-functions-to-work-with-numpy-arrays)
  * [Points to remember](#points-to-remember)

<!-- tocstop -->


## 9.1 Introduction

Rasters present a unique type of spatial data, and a number of geopro cessing tools are designed specificauy to take advantage of the raster data structure.
This chapter iuustrates how to use regular ArcPy functions to list and describe rasters.
ArcPy also includes a Spatial Analyst module referred to as arcpy.sa, which fuuy integrates map algebra into the Python environment, making scripting much more efficient.
Map algebra operators are described, as well as functions and classes of the arcpy.sa module.

## 9.2 Listing rasters

The ListRasters function returns a Python list of rasters in a workspace.
The syntax of the function is


```python
ListRasters({wildcard}, {rastertype})
```

The following code illustrates the llse of the ListRasters function to print a list of the rasters in a workspace:


```python
import arcpy
from arcpy import env
env.workspace = "C:/raster"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster
```

The parameters of the ListRasters function can be used to filter the results.
For example, the following code prints a list of the rasters in the workspace that are in the ERDAS IMAGINE format:


```python
import arcpy
from arcpy import env
env.workspace = "C:/raster"
rasterlist = arcpystRasters("*", "IMG")
for raster in rasterlist:
    print raster
```

## 9.3 Describing raster properties

Three different raster data elem ents can be distinguished:
1. **Raster dataset** - a raster spatial data model that is stored on disk or in a geodatabase. Raster datasets can be stored in many formats , including TIFF, JPEG , IMAGINE , Esri GRID , and MrSID. Raster datasets can be single band or multiband.

2. **Raster band** - one layer in a raster dataset that represents data values for a speciiic range in the electromagnetic spectrum or other values derived by manipulating the original image bands. Many types of satellite images, for example, contain multiple bands.

3. **Raster catalog** - a collection of raster datasets deiined in a table of any format, in which the records deiine the individual raster data sets that are included in the catalog. Raster catalogs can be used to display adjacent or overlapping raster datasets without having to combine them into a mosaic in one large iile

The following code illustrates the use of the Describe function, which returns an object with properties that can be accessed, in this case for printing:


```python
import a rc py
from arcpy import env
env.workspace"C:/raster"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
print desc.dataType
```

For this example of a raster in TIFF format, the dataType property returns the type RasterDatase t. Properties that are speciiic to raster datasets only include the following:
* **bandCount** - the number of bands in the raster dataset
* **compressionType** - the compression type (LZ77, JPEG, JPEG2000, or None)
* **format** - the raster format (GRID, IMAGINE, TIFF, and more)
* **permanent** indicates the permanent state of the raster: False if the raster is temporary, True if the raster is permanent
* **sensorType** - the sensor type used to capture the image


Once it has been determined that an element is a raster dataset , these properties can be accessed.
For example, the following code includes additional properties used to describe the TIFF file:


```python
import arcpy
from arcpy import env
env.workspace = "C:/raster"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
print desc.dataType
print desc.badnCount
print desc.compressionType
```

Many other properties that are commonly associated with rasters can be accessed for individual raster bands only.
For example, the cell resolution is a very important raster property, but individual bands within one raster dataset can have different resolutions.
A number of properties are specific to raster bands, including the following:

* **height** - the number of rows
* **Integer** - indicates whether the raster band is an integer type
* **meanCellHeight** - the cell size in y direction
* **meanCellWidth** - the cell size in x direction
* **noDataValue** - the NoData value of the raster band
* **pixelType** - the pixel type, such as 8-bit integer, 16-bit integer, single precision floating point, and others
* **primaryField** - the index of the field
* **tableType** - the class name of the table
* **width** - the number of columns

For single-band raster datasets, the band itself does not have to b e specified (there is only one, after all) and the properties can be accessed directly by describing the raster dataset.
For example, the following code determines the cell size and pixel type of a raster:



```python
import arcpy
from arcpy import env
env.workspace = "C:/raster"
rasterband = "landcover.tif"
desc = arcpy.Describe(raster)
print desc.meanCellHeight
print desc.meanCellWidth
print desc.pixelType
```

For this particular example, the code returns values of 30.0 by 30.0 and U8 - this means the cell size is 30 by 30 meters and the pixel type is an unsigned 8-bit integer.
These properties do not report the unit type, which has to be obtained from the Spatial Reference property.
For example, the following code determines the name of the spatial reference and the unit:



```python
spatialref = desc.spatialReference
print spatialref.name
print spatialref.linearUnitName
```

For multiband rasters, however, the specific band needs to be specified Without a particular band being specified, prop erties such as cell size, height, w idth, and pixel type cannot be accessed.
Specific bands are refer enced using Band_1 , Band_2, and so on.
The following code illustrates how the properties for a band in a multiband raster dataset are accessed:



```python
import arcpy
from arcpy import env
env.workspace = "C:/raster"
rasterband = "img.tif/Band_1"
desc = arcpy.Describe(rasterband)
print desc.meanCellHeight
print desc.meanCellWidth
print desc.pixelType
```

## 9.4 Working with raster objects

ArcPy also contains a Raster class that is used to reference a raster dataset.
A raster obj ect can be created in two ways: (1) by referencing an existing raster on disk and (2) by using a map algebra staternent.
The syntax for the Raster class is



```python
Raster(inRaster)
```

The following code illustrates how to create a raster object by referencing a raster on disk:


```python
import arcpy
myraster = arcpy.Raster("C:/raster/elevation")
```

When using map algebra statements, the code looks sornething like the following:


```python
import arcpy
outraster = arcpy.sa.Slope("C:/raster/elevation")
```

**Raster objects have only one method: save.**
The raster object (the variable and associated dataset) returned frorn a map algebra expression is temporary by default.
This means the variable and the referenced dataset are deleted when the variable goes out of scope - for example, when ArcGlS is closed or when a stand-alone script is closed.
The save method can be called to rnake the raster object permanent.
The syntax of the save method is


```python
save({name})
```

In the earlier example, the raster object outraster is temporary but can be made permanent using the following code:


```python
import arcpy
outraster = arcpy.sa.Slope("/raster/elevation")
outraster.save("C:/raster/slope")
```

It may appear somewhat counterintuitive that map algebra expressions result in temporary outputs .
Keep in mind that a typical workflow using rasters can involve numerous steps.
If only the fmal output is actually needed, keeping temporary outputs as intermediate steps results in fewer output files and lower storage reguirements.


## 9.5 Working with the ArcPy Spatial Analyst module

ArcPy includes a Spatial Analyst module, arcpy.sa , to carry out map alge bra and other operations.
The functionality provided by the Spatial Analyst module is largely the same as that of the tools in the Spatial Analyst toolbox.
For example, you can run the Slope tool by referencing the Slope tool in the Spatial Analyst toolbox or by importing the arcpy.sa module and directly referencing the Slope tool.



```python
import arcpy
elevraster = arcpy.Raster("C:/raster/elevation")
cutraster = arcpy.sa.Slope(elevraster)
```

Notice that the Slope tool is called using arcpy.sa.
Slope, which appears to follow the regular syntax used for all tools: arcpy.<toolboxalias>.<toolname>.
However, the alternative arcpy.<toolname>_<tooboxalias> syntax does not apply here, and arcpy.Slope_sa is not valid.
Because sa is a module, and not just the alias of a toolbox, the code can be simplified as follows:



```python
import arcpy
from arcpy.sa import *
elevraster = arcpy.Raster("C:/raster/elevation")
raster = Slope(elevraster)
```

## 9.6 Using map algebra operators

In addition to providing access to all the Spatial Analyst geoprocessing tools, the arcpy.sa module also includes a number of map algebra operators.
Most of these operators are available as geoprocessing tools under the Math toolset in the Spatial Analyst toolbox yet are also available as operators in Python.
Consider the following example, whic h converts elevation values from feet to meters using the Times tool:


```python
import arcpy
from arcpy.sa import *
elevraster = arcpy.Raster("C:/raster/elevation")
utraster = Times(elevraster, "0.3048")
outraster.save("C:/raster/elevm")
```

Instead of using the Times tool, the map algebra operator (*) can be used.
The second-to-last line of code would look as follows:


```python
outraster = elevraster * 0.3048
```

Consider the example of a suitability model in which you create three different rasters, each representing a different factor in the suitabilitymodel.
ln the final analysis step, you want to add these three rasters together and determine the average suitability score.
Your code could looksomething like the following:



```python
import arcpy
from arcpy.sa import *
fl = arcpy.Raster("C:/raster/factor1")
f2 = arcpy.Raster("C:/raster/factor2")
f3 = arcpy.Raster("C:/raster/factor3")
templraster = Plus(f1, f2)
temp2raster = Plus(temp1raster, f3)
outraster = Divide(temp2raster, "3")
outraster.save("C:/raster/final)
```

The Plus tool has to be used twice to add all three rasters together because the tool can use only two inputs at a time.
The Divide tool is used to divide the sum of the three rasters by 3.
Using map algebra expressions, this code can be reduced as follows:



```python
import arcpy
from arcpy.sa import *
f1raster = arcpy.Raster("C:/raster/factor1")
f2raster = arcpy.Raster("C:/raster/factor2")
f3raster = arcpy.Raster("C:/raster/factor3")
outraster = ( f1 + f2 + f3 ) / 3
outraster.save("C:/raster/final")
```

It looks very much like the Python code used earlier.
In effect, the map algebra operators in the arcpy.sa module allow you to create Raster Calculator-style expressions directly in Python.
You can also call the Raster Calculator tool using the follow ing syntax:



```python
RasterCalculator(expression, output_raster)
```

* **Table 9.1 Map algebra operators**

|  Category  | Operator |        Description       | Spatial Analyst tool |
|:----------:|:--------:|:------------------------:|:--------------------:|
| Arithmetic |     -    | Subtraction              | Minus                |
|            |     -    | Unary Minus              | Negate               |
|            |     %    | Modulo                   | Mod                  |
|            |     *    | Multiplication           | Times                |
|            |     /    | Divis ion                | Divide               |
|            |    //    | Integer Divis ion        | N/A                  |
|            |     +    | Add ition                | Plus                 |
|            |     +    | Unary Plus               | N/A                  |
|            |    **    | Power                    | Power                |
| Bitwise    |    >>    | Bitwise Right Shift      | Bitwise Right Shift  |
|            |    <<    | Bitwise Left Shift       | Bitwise Left Shift   |
| Boolean    |     ~    | Boolean Complement       | Boolean Not          |
|            |     &    | Boolean And              | Boolean And          |
|            |     ^    | Boolean Exc lusive Or    | Boolean XOr          |
|            |          | Boolean Or               | Boolean Or           |
| Relational |     <    | Less Than                | Less Than            |
|            |    <=    | Less Than or Equal To    | Less Than Equal      |
|            |     >    | Greater Than             | Greater Than         |
|            |    >=    | Greater Than or Equal To | Greater Than Equal   |
|            |    ==    | Equal To                 | Equal To             |
|            |    !=    | Not Equal To             | Not Equal            |

A detailed discussion of each operator is beyond the scope of this book, but some observations are in order:
* Most oper ors have an equivalent tool in the Math toolset, but two do not: // (integer division) and + (unary plus).
However, the same tasks can be accomplished using a combination of tools.
* Many of the tools in the Math toolset do not have an equivalent map algebra operator in Python, including commonly used tools such as Abs, Int, Float, Exp10, Log10, and many others.

## 9.7 Using the ApplyEnvironment function

In addition to the geoprocessing tools in the Spatial Analyst toolbox, there is one more function: the ApplyEnvironment function.
This function copies an existing raster and applies the current environment settings.
The syntax of the function is:


```python
ApplyEnvironment(inraster)
```

This function allows you to change things like the extent or the cell size or to apply an analysis mask.
The following code illustrates how the ApplyEnvironment function is used to set a new cell size of 30 and apply an analysis mask based on an existing shape file:


```python
import arcpy
from arcpy import env
from arcpy.sa import *
elevfeet = arcpy.Raster("C:/raster/elevation")
elevmeter = elevfeet * 0.3048
env.cellsize = 30
env.mask = "C:/raster/studyarea.shp"
elevrasterclip = ApplyEnvironment(elevmeter)
elevrasterclip.save("C:/raster/dem30_m")
```

Not all environment settings apply to the **ApplyEnvironment** function.
They are limited to the following: **Cell Size, Current Workspace, Extent, Mask, Output Coordinate System , Scratch Workspace, and Snap Raster**.
These are the most relevant environment settings when working with rasters.

## 9.8 Using classes of the arcpy.sa module

![](Ch09/reclassify.PNG)

The arcpy.sa module also contains a number of classes that are used for deflll ing parameters of raster tools.
Typically, these classes are used as shortcuts for tool parameters that would otherwise require a more compli cated string value.
Consider the example of the Reclassification tool.
With this tool, raster cells are given a n ew value b ased o n a reclassifI cation table.
The tool dialog box in the figure shows an example of a land-use raster b eing reclassified into a number of values as part of a suitability model.



```python
Reclassify(in_raste , reclass_field, remap, {missing_values})
```

Typing all the values of this table would be rather complicated since this table can have many different entries.
Instead, the remap parameter is expressed as a remap object.
There are two different Remap classes, depending on the nature of the reclassification:


1. RemapValue - a list of individual input values to be reclassified
2. RemapRange - a list identifying ranges of input values to be reclassified

The syntax of the RemapValue object is


```python
RemapValue(remapTable)
```

A remapTable object is defined using a Python of lists that each contain old and new values, similar to the reclassification table on the tool dialog box.
The syntax of a remaptable for use in a RemapValue object is.


```python
[[oldValue1, newValue1], [oldValue2, newValue2], ...]
```

The following code illustrates the use of a remap object to carry out a reclassification of a raster representing land use:


```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/raster"
myremap = RemapValue([["Barren", 1], ["Mixed Forest", 4], ["Coniferous Forest", 0], ["Cropland", 2], ["Grassland", 3], ["Shrub", 3], ["Water", 0]])
outreclass = Reclassify("landuse", "S_VALUE", myremap)
outreclass.save("C:/raster/lu_recl")
```

The RemapRange object works in a similar manner but uses value ranges rather than individual values.
The syntax of a remap table for use in a RemapRange object is


[[startValue, endValue, newValue], ...]

The following code illustrates the use of a remap object to carry out a reclassification of a raster of elevation:


```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace("C:/raster")
myremap = RemapRange([[1, 1000, 0], [1000, 2000, 1], [2000, 3000, 2], [3000, 4000, 3]])
outreclass = Reclassify("elevation", "TYPE", myremap)
outreclass.save("C:/raster/elev_recl")
```

Notice that the end value of the first range is the same as the start value of the second range, and so on.
mThis type of remap table is common when data is continuous, as in the case of a raster of elevation.
In addition to the Reclassify tool, remap tables are also used in the Weighted Overlay tool.


There are many other classes in the arcpy.sa module.
They can be grouped into a number of categories based on logical functionality.
Table 9.2 lists these categories.

* **Table 9.2 Categories of classes in the arcpy.sa module**

| Category          | Description                                                          |
|-------------------|----------------------------------------------------------------------|
| Fuzzy Membership  | Defines the membership function for fuzzy logic analysis             |
| Horizontal Factor | Identifies the horizontal factor for the Path Distance tool       |
| Kriging Models    | Develops the model for creating surfaces with kriging                |
| Neig hborhood     | Defines the input neighborhood for a series of tools                |
| Overlay           | Creates input tables for the Weighted Overlay and Weighted Sum tools |
| Radius            | Identifies a radius for the IDW and Kriging tools                    |
| Remap             | Defines various remap tables used in recl assification               |
| Time              | Identifies the time interval to use in the solar radiation tools     |
| Topo Input        | Defines the input to the Topo To Raster tool                         |
| Vertical Factor   | Identifies the vertical factor for the Path Distance tool            |

Among the more widely used classes, in addition to the Remap classes already discussed, are th e Neighborhood classes, which define neighborhoods of different shapes and sizes.
Consider, for example, the Focal Statistics tool.
This tool, as well as oth er tools in the Neighborhood toolbox, requires the definition of a specific neighborhood


![](Ch09/focalStats.PNG)

The neighborhood settings vary with the type of neighborhood.
For example, for the default rectangular neighborhood, settings include height and width in cell or map units.
However, for the wedge neighborhood, the parameters include start angle and end angle and a radius in cell or map units.

![](Ch09/neighborhood.PNG)

Because of the variability of these parameters, neighborhood functions include a neighborhood object.
For example, the syntax of the Focal Statistics tool is as follows:


```python
FocalStatistics(in_raster, {neighborhood}, {statistics_type}, {ignore_nodata})
```

There are six different neighborhood objects, each with its own unique set of parameters. They are as follows:

1. **NbrAnnulus** - defines an annulus, or ringlike, neighborhood, which is created by specifying an inner circle's and outer circle's radii in either map units or number of cells.

2. **NbrCircle** - defines a circular neighborhood, which is created by specifying the radius in either map units or number of cells.

3. **NbrIrregular** - defines an irregular neighborhood, which is created by a kernel file.

4. **NbrRectangle** - defines a rectangular neighborhood, which is created by specifying the height and the width in either map units or number of cells.

5. **NbrWedge** - defines a wedge neighborhood , which is created by specifying a radius and two angles in either map units or number of cells

6. **NbrWeight** -defi. nes a weight neighborhood, which identifi. es the cell positions to be included w ithin the neighborhood and the weights for multiplying the cell values of the input raster.

For example, the syntax of the NbrRectangle object is


```python
NbrRectangle({width}, {height}, {units})
```

The following code defmes a neighborhood object and uses it in the FocalStatistics function:


```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/raster"
mynbr = NbrRectangle(5, 5, "CELL")
outraster = FocalStatistics("landuse", mynbr, "VARIETY")
outraster.save("C:/raster/lu_var")
```

In this example, the output is a raster of land cover based on a rectangular neighborhood of 5 cells by 5 cells.

## 9.9 Using raster functions to work with NumPy arrays

Two more raster functions need to be mentioned: NumPyArrayToRaster and RasterToNumPyArray .
These are regular ArcPy functions, not functions of the arcpy.sa module.
These two functions allow for conver sions between rasters and NumPy arrays.
A NumPy array is designed to work with very large arrays.
NumPy itself is a package used for scienti fl c computing with Python.
Among other things, it provides a very powerful n-dimensional array objec t.
This type of object makes it possible to move data between databases.
For example, the SciPy package contains numerous algorithms that may be useful for a particular app lication, such as Fourier transforms, maximum entropy models, and multidimensional image pro cessing.
Rather than trying to build a tool in ArcGlS that carries out these specialized functions, you could write a script tool that converts a raster to a NumPy array, and then calls specialized functions from the SciPy package.
A generic script would look as follows:


```python
import arcpy, scipy
from arcpy.sa import *
inRaster = arcpy.Raster("C:/raster/myraster")
my_array = RasterToNumPyArray(inRaster)
outarray = scipy.<module>.<function>(my_array)
outraster = NumPyArrayToRaster(outarray)
outraster.save("C:/raster/result")
```

This is a simplified example and references a generic SciPy function, yet it illustrates how NumPy array functions can be used to export data for processing in another environment and to import the result back into an ArcGIS-compatible format - all within the same Python script.
More information on NumPy (Numerical Python) and SciPy (Scientific Library for Python) can be found at http://numpy.scipy.org and http://www.scipy.org respectively.

## Points to remember

* The ListRasters function is used to list rasters in a workspace.
The Describe function is used to describe raster datasets and raster bands.
Properties of objects returned by the Describe function are dynamic-that is, they depend on the nature of the data type.
* The arcpy.sa module integrates map algebra into the Python envi ronment.
In addition to providing access to all the tools in the Spatial Analyst toolbox, the arcpy.sa module contains a number of map algebra operators, which make scripting with rasters more efficient.
* The arcpy.sa module also contains a number of classes, which are primarily used for defining certain types of parameters of raster tools.
* Conversion functions are available to export a raster to a NumPy array, which makes it possible to use analysis functions from other Python libraries such as SciPy.


```python

```
