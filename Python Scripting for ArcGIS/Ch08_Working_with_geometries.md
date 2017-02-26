
# Chapter 8: Working with geometries

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 8: Working with geometries](#chapter-8-working-with-geometries)
  * [8.1 Introduction](#81-introduction)
  * [8.2 Working with geometry objects](#82-working-with-geometry-objects)
  * [8.3 Reading geometries](#83-reading-geometries)
  * [8.4 Working with multipart features](#84-working-with-multipart-features)
  * [8.5 Working with polygons with holes](#85-working-with-polygons-with-holes)
  * [8.6 Writing geometries](#86-writing-geometries)
  * [8.7 Using cursors to set the spatial reference](#87-using-cursors-to-set-the-spatial-reference)
  * [8.8 Using geometry objects to work with geoprocessing tools](#88-using-geometry-objects-to-work-with-geoprocessing-tools)
  * [Points to remember](#points-to-remember)

<!-- tocstop -->


## 8.1 Introduction

This chapter describes how to work with geometries, including how to create geometry objects from existing feature classes and how to read the properties of these geometry objects.
lndividual features , such as points, polylines, and polygons, can be broken down into their vertices.
Geometries can also be written by creating geometry objects from a list of coordinates.
Being able to read and write geometries provides detailed control of feature classes, features , and the parts and vertices that make up features.


## 8.2 Working with geometry objects

Accessing full geometry objects is somewhat time consuming.
As a result, scripts that work with the full geometry objects of large datasets can become very slow.
If yo u need only specihc properties of the geometry, you can use geometry tokens as shortcuts to access geometry properties.
For example, **```SHAPE@XY```** will return a tuple of x,y coordinates representing the feature's centroid, and **```SHAPE@LENGTH```** will return the feature's length as a double.
On the other hand, **```SHAPE@```** will return the full geometry object.


The following example will determine the combined length of all features in a polyline feature class:


```python
import arcpy
fc = "C:/Data/roads.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0
for row in cursor:
    length += row[0]
print length

```

## 8.3 Reading geometries

In the following example, a search cursor and a for loop are used to iterate over the rows of a point feature class called hospitals.shp.
A geom etry token is used to retrieve the x,y coordinates of the point objects, which are then printed.
The script is as follows:



```python
import arcpy
fc = "C:/Data/hospitals.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])
for row in cursor:
    X, Y = row[0]
    print("{0}, {1}".format(x,y))
```

In the following example code, a for loop is used to iterate over the rows in a shapefile.
For every row, the value of the OID (object identifier) field is printed-without it, you could not tell the start and end of each array of points.
For each row, a geometry ect is obtained, which consists of an array containing an array of point objects.
The getPart method is used to obtain an array of point objects for the first (and only) part of the geometry.
(Note: Geometry coν ered in more detail in the next section.)
A for loop is used to iterate over all the point obj ects in the array and print the x,y coordinates.
The code is as follows:



```python
import arcpy
from arcpy impor env
env.workspace="C:/Data"
fc = "roads.shp"
cursor = arcpy.da.SearchCursor(fc, ["OIO@", "SHAPE@"])
for row cursor:
    print("Feature{0}:".format(row[0]))
    for point in row[1].getPart(0):
        print("{0}, {1}".format(point.X, point.Y))
```

## 8.4 Working with multipart features

The following example code illustrates how this is accomplished for polyline and polygon feature classes:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fc = "roads.shp"
cursor = arcpy.SearchCursor(fc, ["OIO@", "SHAPE@"])
for row in cursor:
    print("Feature{0}:".format(row[0]))
    partnum = 0
    for part in row[1]:
        print("part{0}:".format(partnum))
        for point in part:
            print("{0}, {1}".format(point.X,point.Y))
    partnum += 1
```

## 8.5 Working with polygons with holes

A script to read the geometry of polygons with holes is very similar to the script in the preceding section for multipart features.
The third for loop is replaced by the following:



```python
for point in part:
    if point:
        print("{0}, {1}".format(poont.Y, point.Y))
    else:
        print("Interior Ring")
partnum += 1
```

## 8.6 Writing geometries

The CreateFeatureclass function can be used to create a new, empty feature class, which will be used to hold the new point objects whose coordinates are taken from the preceding list.
The syntax of this tool is as follows:



```python
CreateFeature class_management(out_path, out name, {geometry_type}, {template}, {has_m}, {has_z}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
```

The only required parameters are the path for the location of the new feature class (folder or geodatabase) and the name of the new feature class The default value of the geometry is Polygon.
There is no default for the spatial reference, so if none is speci&ed, the coordinate system will be "unknown."
The first part of the script is as follows:



```python
import arcpy, fileinput, string
from arcpy mport env
env.overwriteOutput = True
infile = "C:/Data/points.txt"
fc = "C:/Data/newpoly.shp"
arcpy.CreateFeatureclass_management("C:/Data", fc, "polygon")
```

The point objects representing the vertices of the polygon can be cre ated using the ArcPy Point class.
These point ects have to be stored in an array.
An array object can be created using the ArcPy Array class.
In general, an array can contain any number of geoprocessing ects such as points, geometries, or spatial references.
In this case, the array will contain point objects.
In addition, an insert cursor is created to make it possible to create new rows - that is, new features.
These lines of code are as follows:



```python
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
point = arcpy.Point()
```

Next, the properties of the point objects have to be set using the values in the text file.
This requires the fileinput Python module to read the text file, and the split method to parse the text into separate strings for the point ID number, the x-coordinate, and the y-coordinate.
These lines of code are as follows:



```python
for line in fileinput.input(infile):
    point.ID, point.X, point.Y = line.split()
```

Finally, the script needs to iterate over the lines of the input text file and create a point object for every line.
The result is a single array with 21 point objects.
The completed script is as follows:



```python
import arcpy, fileinput, os
from arcpy import env
env.workspace = "C:/Data"
infile = "C:/Data/points.txt"
fc = "newpoly.shp"
arcpy.CreateFeatureclass_management("C:/Data", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
po nt = arcpy.Point()
for line in fileinput.input(infile):
    point.ID, point.X, point.Y = line.split()
    line_array.add(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
fileinput.close()
del cur
```

## 8.7 Using cursors to set the spatial reference

Consider the example of using a point feature class in state p lane coordinates and writing a script that exports the x,y coordinate pairs of the point objects in decimal degrees.
The SearchCursor function is used to establish a read-only cursor on the state plane coordinates of the feature class, but the spatial reference of this cursor is set to the desired geographic coordinate system, in decimal degrees.
This is accomplished using the following code:



```python
import arcpy
fc = "C:/Data/hospitals.shp"
prjfile = "C:/projections/GCS_NAD_1983.prj"
spatialref = arcpy.SpatialReference(prjfile)
cursor = arcpy.da.SearchCursor(fc,["SHAPE@"], "", spatialref)
```

Next, an output file is created, using the open function.
This opens the file in writing mode ("w") so that new lines of text can be written to it, as follows:


```python
output = open("result.txt", "w")
```

The next step is to iterate over the rows, create a geometry object for each row, and write the x,y coordinates to the output file using the write method.
This part of the code is as follows:



```python
for row in cursor:
    point = row[0]
    output.write(str(point.X) + " " + str(point.Y) + "\n")
```


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fc = hostals.shp
prjfile = "C:/Projections/GCS_NAO_1983.prj"
spatalref = arcpy.SpatialReference(prjfile)
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"], "", spatialref)
output = open("result.txt", "w")
for row in cursor:
    point = row[0]
    output.write(str(point.X) + " " + str(point.Y) + "\n")
output.close()
```

## 8.8 Using geometry objects to work with geoprocessing tools

For example, the following code creates a list of geometry objects from a list of coordinates, and then uses the geometry objects as input to the Buffer tool, as follows


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
coordlist = [[17.0, 20.0], [125.0, 32.0], [4.0, 87.0]]
pointlist = []
for x, y in coordlist:
    point = arcpy.Point(x,y)
    pointgeometry = arcpy.PointGeometry(point)
    pointlist.append(pointgeometry)
arcpy.Buffer_analysis(pointlist, "buffer.shp", "10 METERS")
```

Geometry objects can also be created directly as the output of geopro cessing tools.
For example, the following code uses an empty geometry object as the output of the Copy Features tool , and the result is a list of geometry objects, as follows:



```python
import arcpy
fc = "C:/Data/roads.shp"
geolist = arcpy.CopyFeatures_management(fc, arcpy.Geometry())
length = 0
for geometry in geolist:
    length += geometry.length
print "Total length:" + length
```

The use of geometry objects can improve the efficiency of your code because it allows you to avoid the steps of having to create temporary feature classes and use a cursor to read through all the features.


## Points to remember

* The geometry object provides access to a number of properties, including length and area. Geometry tokens can be used as shortcuts to specifi. c geometry properties.

* lndividual vertices of geometry objects are stored as an array of point objects (or an array containing multiple arrays of point objects in the case of multipart features)

* New features can be created or updated using the insert and update cursors. A script can defi. ne a feature by creating point ec ts popu lating their properties, and placing the point objects in an array. This new array can then be used to set the geometry of a feature .

* The spatial reference can be set on cursors to work with geometries in a coordinate system that is different from that of the feature class

* Geometry objects can be used instead of feature classes as inputs and outputs for geoprocessing tools to make scripting easier.




```python

```
