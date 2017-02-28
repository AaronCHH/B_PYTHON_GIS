
# Chapter 1: Fundamentals of the Python Language for ArcGIS

Python supports many of the programming constructs found in other languages.  
In this chapter, we'll cover many of the basic language constructs found in Python.  
Initially, we'll cover how to create new Python scripts and edit existing scripts.  
From there, we'll delve into language features, such as adding comments to your code, creating and assigning data to variables, and built-in variable typing with Python, which makes coding with Python easy and compact.  
  
Next, we'll look at the various built-in data types that Python offers, such as strings, numbers, lists, and dictionaries.  
Classes and objects are a fundamental concept in object-oriented programming and in the Python language.  
We'll introduce you to these complex data structures, which you'll use extensively when you write geoprocessing scripts with ArcGIS.  
  
In addition to this, we'll cover statements, including decision support and looping structures to make decisions in your code, and/or looping through a code block multiple times along with the with statement, which is used extensively with the cursor objects from the ArcPy data access module that are used to insert, search, and update data.  
Finally, you'll learn how to access modules that provide additional functionality to the Python language.  
By the end of this chapter, you will have learned the following:  
  
* How to create and edit new Python scripts in IDLE  
* How to create and edit scripts in the ArcGIS Python window  
* The language features of Python  
* Comments and data variables  
* Built-in data types (strings, numbers, lists, and dictionaries)  
* Complex data structures  
* Looping structures  
* Additional Python functionalities  

## 1.1 Using IDLE for Python script development

### 1.1.1 The Python shell window

### 1.1.2 The Python script window

### 1.1.3 Editing existing Python scripts

### 1.1.5 Executing scripts from IDLE

## 1.2 Using the ArcGIS Python window

### 1.2.1 The ArcGIS Python window

### 1.2.2 Displaying the ArcGIS Python window

## 1.3 Python language fundamentals

### 1.3.1 Commenting code

### 1.3.2 Importing modules

### 1.3.3 Variables

### 1.3.4 Built-in data types

### 1.3.5 Classes and objects

__Classes and objects are a fundamental concept in object-oriented programming.__  
While Python is more of a procedural language, it also supports object-oriented programming.  
In object-oriented programming, classes are used to create object instances.  
You can think of classes as blueprints for the creation of one or more objects.  
Each object instance has the same properties and methods, but the data contained in an object can and usually will differ.  
Objects are complex data types in Python composed of properties and methods, and can be assigned to variables just like any other data type.  
Properties contain data associated with an object, while methods are actions that an object can perform.  
  
__These concepts are best illustrated with an example.__  
In ArcPy, the extent class is a rectangle specifid by providing the coordinate of the lower-left corner and the coordinate of the upper-right corner in map units.  
The extent class contains a number of properties and methods.  
Properties include XMin, XMax, YMin, YMax, spatialReference, and others.  
The minimum and maximum of x and y properties provide the coordinates for the extent rectangle.  
The spatialReference property holds a reference to a spatialReference object for extent.  
Object instances of the extent class can be used both to set and get the values of these properties through dot notation.  
An example of this is seen in the following code example:  



```python
# get the extent of the county boundary
ext = row[0].extent
# print out the bounding coordinates and spatial reference
print("XMin: " + str(ext.XMin))
print("XMax: " + str(ext.XMax))
print("YMin: " + str(ext.YMin))
print("YMax: " + str(ext.YMax))
print("Spatial Reference: " + ext.spatialReference.name)
```

Running this script yields the following output:


```python
XMin: 2977896.74002
XMax: 3230651.20622
YMin: 9981999.27708
YMax:10200100.7854
Spatial Reference:
NAD_1983_StatePlane_Texas_Central_FIPS_4203_Feet
```

The extent class also has a number of methods, which are actions that an object can perform.  
In the case of this particular object, most of the methods are related to performing some sort of geometric test between the extent object and another geometry.  
__Examples include contains() , crosses() , disjoint() , equals() , overlaps() , touches() , and within().__  
  
One additional object-oriented concept that you need to understand is dot notation.  
Dot notation provides a way of accessing the properties and methods of an object.  
It is used to indicate that a property or method belongs to a particular class.  
  
The syntax for using dot notation includes an object instance followed by a dot and then the property or method.  
The syntax is the same regardless of whether you're accessing a property or a method.  
A parenthesis and zero or more parameters at the end of the word following the dot indicates that a method is being accessed.  
Here are a couple of examples to better illustrate this concept:  
  


```python
Property: extent.XMin  
Method: extent.touches()  
```

### 1.3.6 Statements


```python

```

### 1.3.7 File I/O

__You will often find it necessary to retrieve or write information to files on your computer.__  
Python has a built-in object type that provides a way to access files for many tasks.  
We're only going to cover a small subset of the file manipulation functionality provided, but we'll touch on the most commonly used functions, including opening and closing files, and reading and writing data to a file.  
  
Python's open()  function creates a file object, which serves as a link to a file residing on your computer.  
You must call the open()  function on a file before reading and/or writing data to a file.  
The fist parameter for the open()  function is a path to the file you'd like to open.  
__The second parameter corresponds to a mode, which is typically read (r), write (w), or append (a)__.  
A value of r indicates that you'd like to open the file for read-only operations, while a value of w indicates you'd like to open the file for write operations.  
In the event that you open a file that already exists for write operations, this will overwrite any data currently in the file, so you must be careful with the write mode.  
The append mode (a) will open a file for write operations, but instead of overwriting any existing data, it will append the new data to the end of the file.  
The following code example shows the use of the open()  function to open a text file in a read-only mode:  



```python
with open('Wildfires.txt','r') as f:
```

Notice that we have also used the with keyword to open the file, ensuring that the file resource will be cleaned up after the code that uses it has fiished executing.  
  
After a file has been opened, data can be read from it in a number of ways and using various methods.  
The most typical scenario would be to read data one line at a time from a file through the readline()  method.  
The readline()  function can be used to read the file one line at a time into a string variable.  
You would need to create a looping mechanism in your Python code to read the entire file line by line.  
__If you would prefer to read the entire file into a variable, you can use the read()  method, which will read the file up to the End Of File (EOF) marker__.  
You can also use the __readlines()__  method to read the entire contents of a file, separating each line into individual strings, until the EOF is found.  
  
In the following code example, we have opened a text file called Wildfires.txt in the read-only mode and used the readlines()  method on the file to read its entire contents into a variable called lstFires, which is a Python list containing each line of the file as a separate string value in the list.  
In this case, the Wildfire.txt file is a comma-delimited text file containing the latitude and longitude of the file along with the confilence values for each file.  
We then loop through each line of text in lstFires and use the split()  function to extract the values based on a comma as the delimiter, including the latitude, longitude, and confilence values.  
The latitude and longitude values are used to create a new Point object, which is then inserted into the feature class using an insert cursor:    



```python
import arcpy, os
try:
    arcpy.env.workspace = "C:/data/WildlandFires.mdb"
    # open the file to read
    with open('Wildfires.txt','r') as f: #open the file
        lstFires = f.readlines() #read the file into a list
        cur = arcpy.InsertCursor("FireIncidents")
        
        for fire in lstFires: #loop through each line
            if 'Latitude' in fire: #skip the header
                continue
            vals = fire.split(",") #split the values based on comma
            latitude = float(vals[0]) #get latitude
            longitude = float(vals[1]) #get longitude
            confid = int(vals[2]) #get confidence value
            
            #create new Point and set values
            pnt = arcpy.Point(longitude,latitude)
            feat = cur.newRow()
            feat.shape = pnt
            feat.setValue("CONFIDENCEVALUE", confid)
            cur.insertRow(feat) #insert the row into featureclass
except:
    print(arcpy.GetMessages()) #print out any errors
finally:
    del cur
    f.close()
```

Just as is the case with reading files, there are a number of methods that you can use to write data to a file.  
The write()  function is probably the easiest to use and takes a single string argument and writes it to a file.  
The writelines()  function can be used to write the contents of a list structure to a file.  
In the following code example, we have created a list structure called fcList, which contains a list of feature classes.  
We can write this list to a file using the writelines()  method:  



```python
outfile = open('c:\\temp\\data.txt','w')
fcList = ["Streams", "Roads", "Counties"]
outfile.writelines(fcList)
```

## 1.4 Summary

In this chapter, we covered some of the fundamental Python programming concepts that you'll need to understand before you can write effective geoprocessing scripts.  
We began the chapter with an overview of the IDLE development environment to write and debug Python scripts.  
You learned how to create a new script, edit existing scripts, check for syntax errors, and execute scripts.  
We also covered the basic language constructs, including importing modules, creating and assigning variables, if/else statements, looping statements, and the various data-types including strings, numbers, Booleans, lists, dictionaries, and objects.  
You also learned how to read and write text files.  


```python

```
