
# Chapter 8: Using the ArcPy Data Access Module with Feature Classes and Tables

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 8: Using the ArcPy Data Access Module with Feature Classes and Tables](#chapter-8-using-the-arcpy-data-access-module-with-feature-classes-and-tables)
  * [8.1 Introduction](#81-introduction)
  * [8.2 Retrieving features from a feature class with  SearchCursor](#82-retrieving-features-from-a-feature-class-with-searchcursor)
    * [8.2.1 Getting ready](#821-getting-ready)
    * [8.2.2 How to do it](#822-how-to-do-it)
    * [8.2.3 How it works](#823-how-it-works)
  * [8.3 Filtering records with a where clause](#83-filtering-records-with-a-where-clause)
    * [8.3.1 Getting ready](#831-getting-ready)
    * [8.3.2 How to do it](#832-how-to-do-it)
    * [8.3.3 How it works](#833-how-it-works)
  * [8.4 Improving cursor performance with geometry tokens](#84-improving-cursor-performance-with-geometry-tokens)
    * [8.4.1 Getting ready](#841-getting-ready)
    * [8.4.2 How to do it](#842-how-to-do-it)
    * [8.4.3 How it works](#843-how-it-works)
  * [8.5 Inserting rows with InsertCursor](#85-inserting-rows-with-insertcursor)
    * [8.5.1 Getting ready](#851-getting-ready)
    * [8.5.2 How to do it](#852-how-to-do-it)
    * [8.5.3 How it works](#853-how-it-works)
  * [8.6 Updating rows with UpdateCursor](#86-updating-rows-with-updatecursor)
    * [8.6.1 Getting ready](#861-getting-ready)
    * [8.6.2 How to do it](#862-how-to-do-it)
    * [8.6.3 How it works](#863-how-it-works)
  * [8.7 Deleting rows with UpdateCursor](#87-deleting-rows-with-updatecursor)
    * [8.7.1 Getting ready](#871-getting-ready)
    * [8.7.2 How to do it](#872-how-to-do-it)
    * [8.7.3 How it works](#873-how-it-works)
  * [8.8 Inserting and updating rows inside an edit session](#88-inserting-and-updating-rows-inside-an-edit-session)
    * [8.8.1 Getting ready](#881-getting-ready)
    * [8.8.2 How to do it](#882-how-to-do-it)
  * [8.9 Reading geometry from a feature class](#89-reading-geometry-from-a-feature-class)
    * [8.9.1 Getting ready](#891-getting-ready)
    * [8.9.2 How to do it](#892-how-to-do-it)
    * [8.9.3 How it works](#893-how-it-works)
  * [8.10 Using Walk() to navigate directories](#810-using-walk-to-navigate-directories)
    * [8.10.1 Getting ready](#8101-getting-ready)
    * [8.10.2 How to do it](#8102-how-to-do-it)
    * [8.10.3 How it works](#8103-how-it-works)

<!-- tocstop -->

In this chapter, we will cover the following recipes:

* Retrieving features from a feature class with SearchCursor
* Filtering records with a where clause
* Improving cursor performance with geometry tokens
* Inserting rows with InsertCursor f  Updating rows with UpdateCursor f Deleting rows with UpdateCursor
* Inserting and updating rows inside an edit session
* Reading geometry from a feature class
* Using Walk() to navigate directories


## 8.1 Introduction

We'll start this chapter with a basic question.
What are cursors? Cursors are in-memory objects containing one or more rows of data from a table or feature class.
Each row contains attributes from each field in a data source along with the geometry for each feature.
Cursors allow you to search, add, insert, update, and delete data from tables and feature classes.

The arcpy data access module or arcpy.da was introduced in ArcGIS 10.1 and contains methods that allow you to iterate through each row in a cursor.
Various types of cursors can be created depending on the needs of developers.
For example, search cursors can be created to read values from rows.
Update cursors can be created to update values in rows or delete rows, and insert cursors can be created to insert new rows.

There are a number of cursor improvements that have been introduced with the arcpy data access module.
Prior to the development of ArcGIS 10.1, cursor performance was notoriously slow.
Now, cursors are significantly faster.
Esri has estimated that SearchCursors are up to 30 times faster, while InsertCursors are up to 12 times faster.
In addition to these general performance improvements, the data access module also provides a number of new options that allow programmers to speed up processing.
Rather than returning all the fields in a cursor, you can now specify that a subset of fields be returned.
This increases the performance as less data needs to be returned.
The same applies to geometry.
Traditionally, when accessing the geometry of a feature, the entire geometric definition would be returned.
You can now use geometry tokens to return a portion of the geometry rather than the full geometry of the feature.
You can also use lists and tuples rather than using rows.
There are also other new features, such as edit sessions and the ability to work with versions, domains, and subtypes.

There are three cursor functions in arcpy.da.
Each returns a cursor object with the same name as the function.
SearchCursor() creates a read-only SearchCursor object containing    rows from a table or feature class.
InsertCursor() creates an InsertCursor object that can be used to insert new records into a table or feature class.
UpdateCursor() returns a cursor object that can be used to edit or delete records from a table or feature class.
Each of these cursor objects has methods to access rows in the cursor.
You can see the relationship between the cursor functions, the objects they create, and how they are used, as follows:

The SearchCursor() function is used to return a SearchCursor object.
This object can only be used to iterate through a set of rows returned for read-only purposes.
No insertions, deletions, or updates can occur through this object.
An optional where clause can be set to limit the rows returned.

Once you've obtained a cursor instance, it is common to iterate the records, particularly with SearchCursor or UpdateCursor.
There are some peculiarities that you need to understand when navigating the records in a cursor.
Cursor navigation is forward-moving only.
When a cursor is created, the pointer of the cursor sits just above the first row in the cursor.
The first call to next() will move the pointer to the first row.
Rather than calling the next() method, you can also use a for loop to process each of the records without the need to call the next() method.
After performing whatever processing you need to do with this row, a subsequent call to next() will move the pointer to row 2.
This process continues as long as you need to access additional rows.
However, after a row has been visited, you can't go back a single record at a time.
For instance, if the current row is row 3, you can't programmatically back up to row 2.
You can only go forward.
To revisit rows 1 and 2, you would need to either call the reset() method or recreate the cursor and move back through the object.
As I mentioned earlier, cursors are often navigated through the use of for loops as well.
In fact, this is a more common way to iterate a cursor and a more efficient way to code your scripts.
Cursor navigation is illustrated in the following diagram:  The InsertCursor() function is used to create an InsertCursor object that allows you  to programmatically add new records to feature classes and tables.
To insert rows, call the insertRow() method on this object.
You can also retrieve a read-only tuple containing the field names in use by the cursor through the fields property.
A lock is placed on the table or feature class being accessed through the cursor.
Therefore, it is important to always design your script in a way that releases the cursor when you are done.

The UpdateCursor() function can be used to create an UpdateCursor object that can update and delete rows in a table or feature class.
As is the case with InsertCursor, this function places a lock on the data while it's being edited or deleted.
If the cursor is used  inside a Python's with statement, the lock will automatically be freed after the data has been processed.
This hasn't always been the case.
Prior to ArcGIS 10.1, cursors were required to be manually released using the Python del statement.
Once an instance of UpdateCursor has been obtained, you can then call the updateCursor() method to update records in tables or feature classes and the deleteRow() method to delete a row.
The subject of data locks requires a little more explanation.
The insert and update  cursors must obtain a lock on the data source they reference.
This means that no other application can concurrently access this data source.
Locks are a way of preventing multiple users from changing data at the same time and thus, corrupting the data.

When the InsertCursor() and UpdateCursor() methods are called in your code, Python attempts to acquire a lock on the data.
This lock must be specifically released after the cursor has finished processing so that the running applications of other users, such as ArcMap or ArcCatalog, can access the data sources.
If this isn't done, no other application will be   able to access the data.
Prior to ArcGIS 10.1 and the with statement, cursors had to be specifically unlocked through Python's del statement.
Similarly, ArcMap and ArcCatalog also acquire data locks when updating or deleting data.
If a data source has been locked by either of these applications, your Python code will not be able to access the data.
Therefore, the best practice is to close ArcMap and ArcCatalog before running any standalone Python scripts that use insert or update cursors.

In this chapter, we're going to cover the use of cursors to access and edit tables and feature classes.
However, many of the cursor concepts that existed before ArcGIS 10.1 still apply.



## 8.2 Retrieving features from a feature class with  SearchCursor

There are many occasions when you need to retrieve rows from a table or feature class for read-only purposes.
For example, you might want to generate a list of all land parcels in a city with a value greater than $100,000.
In this case, you don't have any need to edit the data.
Your needs are met simply by generating a list of rows that meet some sort of criteria.
A SearchCursor object contains a read-only copy of rows from a table or feature class.
These objects can also be filtered through the use of a where clause so that only a subset of the dataset is returned.



### 8.2.1 Getting ready

The SearchCursor() function is used to return a SearchCursor object.
This object can only be used to iterate a set of rows returned for read-only purposes.
No insertions, deletions, or updates can occur through this object.
An optional where clause can be set to limit the rows returned.
In this recipe, you will learn how to create a basic SearchCursor object on a feature class through the use of the SearchCursor() function.

The SearchCursor object contains a fields property along with the next() and reset() methods.
The fields property is a read-only structure in the form of a Python tuple, containing the fields requested from the feature class or table.
You are going to hear the term tuple a lot in conjunction with cursors.
If you haven't covered this topic before, tuples are a Python structure to store a sequence of data similar to Python lists.
However, there are some important differences between Python tuples and lists.
Tuples are defined as a sequence of values inside parentheses, while lists are defined as a sequence of values inside brackets.
Unlike lists, tuples can't grow and shrink, which can be a very good thing in some cases when you want data values to occupy a specific position each time.
This is the case with cursor objects that use tuples to store data from fields in tables and feature classes.


### 8.2.2 How to do it

Follow these steps to learn how to retrieve rows from a table or feature class inside a
SearchCursor object:
1. Open IDLE and create a new script window.

2. Save the script as C:\ArcpyBook\Ch8\SearchCursor.py.

3. Import the arcpy.da module:
```py
import arcpy.da
```

4. Set the workspace:
```py
arcpy.env.workspace = "c:/ArcpyBook/Ch8"
```

5. Use a Python with statement to create a cursor:
```py
with arcpy.da.SearchCursor("Schools.shp",("Facility","Name")) as cursor:
```

6. Loop through each row in SearchCursor and print the name of the school. Make sure you indent the for loop inside the with block:
```py
for row in sorted(cursor): print("School name: " + row[1])
```

7. The entire script should appear as follows:
```py
import arcpy.da
arcpy.env.workspace = "c:/ArcpyBook/Ch8" with
arcpy.da.SearchCursor("Schools.shp",("Facility","Name")) as cursor:
    for row in sorted(cursor): print("School name: " + row[1])
```
8. Save the script.

9. You can check your work by examining the C:\ArcpyBook\code\Ch8\ SearchCursor_Step1.py solution file.

10. Run the script. You should see the following output:
```py
School name: ALLAN
School name: ALLISON
School name: ANDREWS
School name: BARANOFF
School name: BARRINGTON
School name: BARTON CREEK
School name: BARTON HILLS
School name: BATY
School name: BECKER
School name: BEE CAVE
```

### 8.2.3 How it works

The with statement used with the SearchCursor() function will create, open, and close the cursor.
So, you no longer have to be concerned with explicitly releasing the lock on the cursor as you did prior to ArcGIS 10.1.
The first parameter passed into the SearchCursor() function is a feature class, represented by the Schools.shp file.
The second parameter is a Python tuple containing a list of fields that we want returned in the cursor.
For performance reasons, it is a best practice to limit the fields returned in the cursor to only those that you need to complete the task.
Here, we've specified that only the Facility and Name fields should be returned.
The SearchCursor object is stored in a variable called cursor.
Inside the with block, we use a Python for loop to loop through each school returned.
We also use the Python sorted() function to sort the contents of the cursor.
To access the values from a field on the row, simply use the index number of the field you want to return.
In this case, we want to return the contents of the Name column, which will be the 1 index number, since it is the second item in the tuple of field names that are returned.



## 8.3 Filtering records with a where clause

By default, SearchCursor will contain all rows in a table or feature class.
However, in many cases, you will want to restrict the number of rows returned by some sort of criteria.
Applying a filter through the use of a where clause limits the records returned.


### 8.3.1 Getting ready

By default, all rows from a table or feature class will be returned when you create a SearchCursor object.
However, in many cases, you will want to restrict the records returned.
You can do this by creating a query and passing it as a where clause parameter when calling the SearchCursor() function.
In this recipe, you'll build on the script you created in the previous recipe by adding a where clause that restricts the records returned.



### 8.3.2 How to do it

Follow these steps to apply a filter to a SearchCursor object that restricts the rows returned from a table or feature class:

1.  Open IDLE and load the SearchCursor.py script that you created in the previous recipe.

2.  Update the SearchCursor() function by adding a where clause that queries the facility field for records that have the HIGH SCHOOL text:
```py
with arcpy.da.SearchCursor("Schools.shp",("Facility","Name"), '"FACILITY" = \'HIGH SCHOOL\'') as cursor:
```

3.  You can check your work by examining the C:\ArcpyBook\code\Ch8\ SearchCursor_Step2.py solution file.

4.  Save and run the script.
The output will now be much smaller and restricted to high schools only:
```py
High school name: AKINS
High school name: ALTERNATIVE LEARNING CENTER
High school name: ANDERSON
High school name: AUSTIN
High school name: BOWIE
High school name: CROCKETT
High school name: DEL VALLE
High school name: ELGIN
High school name: GARZA
High school name: HENDRICKSON
High school name: JOHN B CONNALLY
High school name: JOHNSTON
High school name: LAGO VISTA
```


### 8.3.3 How it works

We covered the creation of queries in Chapter 7, Querying and Selecting Data, so hopefully you now have a good grasp of how these are created along with all the rules you need to follow when coding these structures.
The where clause parameter accepts any valid SQL query, and is used in this case to restrict the number of records that are returned.


## 8.4 Improving cursor performance with geometry tokens

Geometry tokens were introduced in ArcGIS 10.1 as a performance improvement for cursors.
Rather than returning the entire geometry of a feature inside the cursor, only a portion of the geometry is returned.
Returning the entire geometry of a feature can result in decreased cursor performance due to the amount of data that has to be returned.
It's significantly faster to return only the specific portion of the geometry that is needed.


### 8.4.1 Getting ready

A token is provided as one of the fields in the field list passed into the constructor for a cursor and is in the SHAPE@<Part of Feature to be Returned> format.
The only exception  to this format is the OID@ token, which returns the object ID of the feature.
The following code example retrieves only the X and Y coordinates of a feature:
```py
with arcpy.da.SearchCursor(fc, ("SHAPE@XY","Facility","Name")) as cursor:
```

The following table lists the available geometry tokens.
Not all cursors support the full list of tokens.
Check the ArcGIS help files for information about the tokens supported by each cursor type.
__The SHAPE@ token returns the entire geometry of the feature.__
Use this carefully though, because it is an expensive operation to return the entire geometry of a feature and can dramatically affect performance.
If you don't need the entire geometry, then do not include this token!

In this recipe, you will use a geometry token to increase the performance of a cursor.
You'll retrieve the X and Y coordinates of each land parcel from the parcels feature class along with some attribute information about the parcel.


### 8.4.2 How to do it

Follow these steps to add a geometry token to a cursor, which should improve the performance of this object:

1.  Open IDLE and create a new script window.

2.  Save the script as C:\ArcpyBook\Ch8\GeometryToken.py.

3.  Import the arcpy.da module and the time module:
```py
import arcpy.da import time
```

4.  Set the workspace:
```py
arcpy.env.workspace = "c:/ArcpyBook/Ch8"
```

5.  We're going to measure how long it takes to execute the code using a geometry token. Add the start time for the script:
```py
start = time.clock()
```

6.  Use a Python with statement to create a cursor that includes the centroid of each feature as well as the ownership information stored in the PY_FULL_OW field:
```py
with arcpy.da.SearchCursor("coa_parcels.shp",("PY_FULL_OW","SHAPE@XY")) as cursor:
```

7.  Loop through each row in SearchCursor and print the name of the parcel and location. Make sure you indent the for loop inside the with block:
```py
for row in cursor:
print("Parcel owner: {0} has a location of:
{1}".format(row[0], row[1]))
```

8.  Measure the elapsed time:
```py
elapsed = (time.clock() - start)
```

9.  Print the execution time:
```py
print("Execution time: " + str(elapsed))
```

10. The entire script should appear as follows:
```py
import arcpy.da import time
arcpy.env.workspace = "c:/ArcpyBook/Ch9" start = time.clock()
with arcpy.da.SearchCursor("coa_parcels.shp",("PY_FULL_OW", "SHAPE@XY")) as cursor:
for row in cursor:
print("Parcel owner: {0} has a location of:
{1}".format(row[0], row[1])) elapsed = (time.clock() - start)
print("Execution time: " + str(elapsed))
```

11. You can check your work by examining the C:\ArcpyBook\code\Ch8\ GeometryToken.py solution file.

12. Save the script.

13. Run the script.
You should see something similar to the following output.
Note the execution time; your time will vary:
```py
Parcel owner: CITY OF AUSTIN ATTN REAL ESTATE DIVISION has a location of: (3110480.5197341456, 10070911.174956793)
Parcel owner: CITY OF AUSTIN ATTN REAL ESTATE DIVISION has a location of: (3110670.413783513, 10070800.960865)
Parcel owner: CITY OF AUSTIN has a location of: (3143925.0013213265, 10029388.97419636)
Parcel owner: CITY OF AUSTIN % DOROTHY NELL ANDERSON ATTN BARRY LEE ANDERSON has a location of: (3134432.983822767, 10072192.047894118)
Execution time: 9.08046185109
```

Now, we're going to measure the execution time if the entire geometry is returned instead of just the portion of the geometry that we need:

1.  Save a new copy of the script as C:\ArcpyBook\Ch8\ GeometryTokenEntireGeometry.py.

2.  Change the SearchCursor() function to return the entire geometry using SHAPE@ instead of SHAPE@XY:
```
with arcpy.da.SearchCursor("coa_parcels.shp",("PY_FULL_OW", "SHAPE@")) as cursor:
```

3.  You can check your work by examining the C:\ArcpyBook\code\Ch8\GeometryTokenEntireGeometry.py solution file.

4.  Save and run the script.
You should see the following output.
Your time will vary from mine, but notice that the execution time is slower.
In this case, it's only a little over a second slower, but we're only returning 2600 features.
If the feature class were significantly larger, as many are, this would be amplified:
```
Parcel owner: CITY OF AUSTIN ATTN REAL ESTATE DIVISION has a
location of: <geoprocessing describe geometry object object at 0x06B9BE00>
Parcel owner: CITY OF AUSTIN ATTN REAL ESTATE DIVISION has a
location of: <geoprocessing describe geometry object object at 0x2400A700>
Parcel owner: CITY OF AUSTIN has a location of: <geoprocessing describe geometry object object at 0x06B9BE00>
Parcel owner: CITY OF AUSTIN % DOROTHY NELL ANDERSON ATTN
BARRY LEE ANDERSON has a location of: <geoprocessing describe geometry object object at 0x2400A700>
Execution time: 10.1211390896
```


### 8.4.3 How it works

A geometry token can be supplied as one of the field names supplied in the constructor for the cursor.
These tokens are used to increase the performance of a cursor by returning only a portion of the geometry instead of the entire geometry.
This can dramatically increase the performance of a cursor, particularly when you are working with large polyline or polygon datasets.
If you only need specific properties of the geometry in your cursor, you should use these tokens.



## 8.5 Inserting rows with InsertCursor

You can insert a row into a table or feature class using an InsertCursor object.
If you want to insert attribute values along with the new row, you'll need to supply the values in the order found in the attribute table.



### 8.5.1 Getting ready

The InsertCursor() function is used to create an InsertCursor object that allows you to programmatically add new records to feature classes and tables.
The insertRow() method on the InsertCursor object adds the row.
A row in the form of a list or tuple is passed into the insertRow() method.
The values in the list must correspond to the field values defined when the InsertCursor object was created.
Similar to instances that include other types of cursors, you can also limit the field names returned using the second parameter of the method.
This function supports geometry tokens as well.

The following code example illustrates how you can use InsertCursor to insert new rows into a feature class.
Here, we insert two new wildfire points into the California feature class.
The row values to be inserted are defined in a list variable.
Then, an InsertCursor object is created, passing in the feature class and fields.
Finally, the new rows are inserted into the feature class by using the insertRow() method:
```py
rowValues = [(Bastrop','N',3000,(-105.345,32.234)), ('Ft Davis','N', 456, (-109.456,33.468))]
fc = "c:/data/wildfires.gdb/California"
fields = ["FIRE_NAME", "FIRE_CONTAINED", "ACRES", "SHAPE@XY"]
with arcpy.da.InsertCursor(fc, fields) as cursor: for row in rowValues:
    cursor.insertRow(row)
```

In this recipe, you will use InsertCursor to add wildfires retrieved from a .txt file into a point feature class.
When inserting rows into a feature class, you will need to know how to add the geometric representation of a feature into the feature class.
This can be accomplished by using InsertCursor along with two miscellaneous objects: Array and Point.
In this exercise, we will add point features in the form of wildfire incidents to an empty point feature class.
In addition to this, you will use Python file manipulation techniques to read the coordinate data from a text file.



### 8.5.2 How to do it

We will be importing the North American wildland fire incident data from a single day in October, 2007.
This data is contained in a comma-delimited text file containing one line for each fire incident on this particular day.
Each fire incident has a latitude, longitude coordinate pair separated by commas along with a confidence value.
This data was derived by automated methods that use remote sensing data to derive the presence or absence of a wildfire.
Confidence values can range from 0 to 100.
Higher numbers represent a greater confidence that this is indeed a wildfire:

1. Open the file at C:\ArcpyBook\Ch8\Wildfire Data\ NorthAmericaWildfire_2007275.txt and examine the contents.
You will notice that this is a simple comma-delimited text file containing the longitude and latitude values for each fire along with a confidence value.
We will use Python to read the contents of this file line by line and insert new point features into the FireIncidents feature class located in the C:\ArcpyBook\Ch8 \ WildfireData\WildlandFires.mdb personal geodatabase.

2. Close the file.

3. Open ArcCatalog.

4. Navigate to C:\ArcpyBook\Ch8\WildfireData.
You should see a personal geodatabase called WildlandFires.
Open this geodatabase and you will see a point feature class called FireIncidents.
Right now, this is an empty feature class.
We will add features by reading the text file you examined earlier and inserting points.

5. Right-click on FireIncidents and select Properties.

6. Click on the Fields tab.
The latitude/longitude values found in the file we examined earlier will be imported into the SHAPE field and the confidence values will be written to the CONFIDENCEVALUE field.

7. Open IDLE and create a new script.

8. Save the script to C:\ArcpyBook\Ch8\InsertWildfires.py.

9. Import the arcpy modules:
```py
import arcpy
```

10. Set the workspace:
```py
arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
```

11. Open the text file and read all the lines into a list:
```py
f = open("C:/ArcpyBook/Ch8/WildfireData/NorthAmericaWildfires_2007275. txt","r")
lstFires = f.readlines()
```

12. Start a try block:
```py
try:
```

13. Create an InsertCursor object using a with block.
Make sure you indent inside the try statement.
The cursor will be created in the FireIncidents feature class: with arcpy.da.InsertCursor("FireIncidents",("SHAPE@ XY","CONFIDENCEVALUE")) as cur:

14. Create a counter variable that will be used to print the progress of the script:
```py
cntr = 1
```

15. Loop through the text file line by line using a for loop.
Since the text file is comma-delimited, we'll use the Python split() function to separate each value into a list variable called vals.
We'll then pull out the individual latitude, longitude, and confidence value items and assign them to variables.
Finally, we'll place these values into a list variable called rowValue, which is then passed into the insertRow() function for the InsertCursor object, and we then print a message:
```py
for fire in lstFires:
if 'Latitude' in fire: continue
vals = fire.split(",") latitude = float(vals[0]) longitude = float(vals[1]) confid = int(vals[2])
rowValue = [(longitude,latitude),confid] cur.insertRow(rowValue)
print("Record number " + str(cntr) + " written to feature class")
#arcpy.AddMessage("Record number" + str(cntr) + " written to feature class")
cntr = cntr + 1
```

16. Add the except block to print any errors that may occur:
```py
except Exception as e: print(e.message)
```

17. Add a finally block to close the text file:
```py
finally: f.close()
```

18. The entire script should appear as follows:
```py
import arcpy
arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/ WildlandFires.mdb"
f = open("C:/ArcpyBook/Ch8/WildfireData/ NorthAmericaWildfires_2007275.txt","r")
lstFires = f.readlines()
try:
        with arcpy.da.InsertCursor("FireIncidents", ("SHAPE@XY","CONFIDENCEVALUE")) as cur:
            cntr = 1
        for fire in lstFires:
            if 'Latitude' in fire:
                continue
vals = fire.split(",")
latitude = float(vals[0])
longitude = float(vals[1])
confid = int(vals[2])
rowValue = [(longitude,latitude),confid]
cur.insertRow(rowValue)
print("Record number " + str(cntr) + " written to feature class")
#arcpy.AddMessage("Record number" + str(cntr) + " written to feature class")
cntr = cntr + 1
except Exception as e:
        print(e.message)
finally:
        f.close()
```

19. You can check your work by examining the C:\ArcpyBook\code\Ch8\ InsertWildfires.py solution file.

20. Save and run the script. You should see messages being written to the output window as the script runs:
```py
Record number: 406 written to feature class Record number:
407 written to feature class Record number:
408 written to feature class Record number:
409 written to feature class Record number:
410 written to feature class Record number:
411 written to feature class
```

21. Open ArcMap and add the FireIncidents feature class to the table of contents. The points should be visible, as shown in the following screenshot:

22. You may want to add a basemap to provide some reference for the data. In ArcMap, click on the Add Basemap button and select a basemap from the gallery.


### 8.5.3 How it works

Some additional explanation may be needed here.
The lstFires variable contains a list of  all the wildfires that were contained in the comma-delimited text file.
The for loop will loop through each of these records one by one, inserting each individual record into the fire variable.
We also include an if statement that is used to skip the first record in the file, which serves as the header.
As I explained earlier, we then pull out the individual latitude, longitude, and confidence value items from the vals variable, which is just a Python list object and assign them to variables called latitude, longitude, and confid.
We then place these values into a new list variable called rowValue in the order that we defined when we created InsertCursor.
Thus, the latitude and longitude pair should be placed first followed by the confidence value.
Finally, we call the insertRow() function on the InsertCursor object assigned to the cur variable, passing in the new rowValue variable.
We close by printing a message that indicates the progress of the script and also create the except and finally blocks to handle errors and close the text file.
Placing the file.close() method in the finally block ensures that it will execute and close the file even if there is an error in the previous try statement.



## 8.6 Updating rows with UpdateCursor

If you need to edit or delete rows from a table or feature class, you can use UpdateCursor.
As is the case with InsertCursor, the contents of UpdateCursor can be limited through the use of a where clause.



### 8.6.1 Getting ready

The UpdateCursor() function can be used to either update or delete rows in a table or feature class.
The returned cursor places a lock on the data, which will automatically be released if used inside a Python with statement.
An UpdateCursor object is returned from a call to this method.

The UpdateCursor object places a lock on the data while it's being edited or deleted.
If the cursor is used inside a Python with statement, the lock will automatically be freed after the data has been processed.
This hasn't always been the case.
Previous versions of cursors were required to be manually released using the Python del statement.
Once an instance of UpdateCursor has been obtained, you can then call the updateCursor() method to update records in tables or feature classes and the deleteRow() method can be used to delete a row.

In this recipe, you're going to write a script that updates each feature in the FireIncidents feature class by assigning a value of poor, fair, good, or excellent to a new field that is more descriptive of the confidence values using an UpdateCursor.
Prior to updating the records, your script will add the new field to the FireIncidents feature class.


### 8.6.2 How to do it

Follow these steps to create an UpdateCursor object that will be used to edit rows in a feature class:

1. Open IDLE and create a new script.

2. Save the script to C:\ArcpyBook\Ch8\UpdateWildfires.py.

3. Import the arcpy module:
```py
import arcpy
```

4. Set the workspace:
```py
arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
```

5. Start a try block:
```py
try:
```

6. Add a new field called CONFID_RATING to the FireIncidents feature class. Make sure to indent inside the try statement:
```py
arcpy.AddField_management("FireIncidents","CONFID_RATING", "TEXT","10")
print("CONFID_RATING field added to FireIncidents")
```

7. Create a new instance of UpdateCursor inside a with block:
```py
with arcpy.da.UpdateCursor("FireIncidents",
("CONFIDENCEVALUE","CONFID_RATING")) as cursor:
```

8. Create a counter variable that will be used to print the progress of the script. Make sure you indent this line of code and all the lines of code that follow inside the with block:
```py
cntr = 1
```

9. Loop through each of the rows in the FireIncidents fire class.
Update the
```sql
CONFID_RATING field according to the following guidelines:
    Confidence value 0 to 40 = POOR
    Confidence value 41 to 60 = FAIR
    Confidence value 61 to 85 = GOOD
    Confidence value 86 to 100 = EXCELLENT
This can be translated in the following block of code:
```
```py
for row in cursor:
    # update the confid_rating field
    if row[0] <= 40:
        row[1] = 'POOR'
    elif row[0] > 40 and row[0] <= 60: row[1] = 'FAIR'
    elif row[0] > 60 and row[0] <= 85: row[1] = 'GOOD'
    else:
        row[1] = 'EXCELLENT'
        cursor.updateRow(row)
        print("Record number " + str(cntr) + " updated") cntr = cntr + 1
```

10. Add the except block to print any errors that may occur:
```py
except Exception as e: print(e.message)
```
11. The entire script should appear as follows:
```py
import arcpy
arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
try:
    #create a new field to hold the values arcpy.AddField_management("FireIncidents",
    "CONFID_RATING","TEXT","10")
    print("CONFID_RATING field added to FireIncidents")
    with arcpy.da.UpdateCursor("FireIncidents",("CONFIDENCEVALUE", "CONFID_RATING")) as cursor:
        cntr = 1
        for row in cursor:
            # update the confid_rating field
            if row[0] <= 40:
                row[1] = 'POOR'
                elif row[0] > 40 and row[0] <= 60: row[1] = 'FAIR'
                elif row[0] > 60 and row[0] <= 85: row[1] = 'GOOD'
            else:
                row[1] = 'EXCELLENT'
            cursor.updateRow(row)
            print("Record number " + str(cntr) + " updated")
            cntr = cntr + 1
except Exception as e: print(e.message)
```

12. You can check your work by examining the C:\ArcpyBook\code\Ch8\ UpdateWildfires.py solution file.

13. Save and run the script. You should see messages being written to the output window as the script runs:
```py
Record number
406 updated Record number
407 updated Record number
408 updated Record number
409 updated Record number
410 updated
```

14. Open ArcMap and add the FireIncidents feature class.
Open the attribute table and you should see that a new CONFID_RATING field has been added and populated by UpdateCursor:


### 8.6.3 How it works

In this case, we've used UpdateCursor to update each of the features in a feature class.
We first used the Add Field tool to add a new field called CONFID_RATING, which will hold new values that we assign based on values found in another field.
The groups are poor, fair, good, and excellent and are based on numeric values found in the CONFIDENCEVALUE field.
We then created a new instance of UpdateCursor based on the FireIncidents feature class, and returned the two fields mentioned previously.
The script then loops through each of the features and assigns a value of poor, fair, good, or excellent to the CONFID_RATING field (row[1]), based on the numeric value found in CONFIDENCEVALUE.
A Python if/elif/ else structure is used to control the flow of the script based on the numeric value.
The value for CONFID_RATING is then committed to the feature class by passing the row variable into the updateRow() method.



## 8.7 Deleting rows with UpdateCursor

In addition to being used to edit rows in a table or feature class, UpdateCursor can also be used to delete rows.
Keep in mind that when rows are deleted outside an edit session, the changes are permanent.



### 8.7.1 Getting ready

In addition to updating records, UpdateCursor can also delete records from a table or feature class.
The UpdateCursor object is created in the same way in either case, but instead of calling updateRow(), you call deleteRow() to delete a record.
You can also  apply a where clause to UpdateCursor, to limit the records returned.
In this recipe, we'll use an UpdateCursor object that has been filtered using a where clause to delete records from our FireIncidents feature class.


### 8.7.2 How to do it

Follow these steps to create an UpdateCursor object that will be used to delete rows from a feature class:

1.  Open IDLE and create a new script.

2.  Save the script to C:\ArcpyBook\Ch8\DeleteWildfires.py.

3.  Import the arcpy and os modules:
```py
import arcpy import os
```

4.  Set the workspace:
```py
arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
```

5.  Start a try block:
```py
try:
```

6.  Create a new instance of UpdateCursor inside a with block. Make sure you indent inside the try statement:
```py
with arcpy.da.UpdateCursor("FireIncidents",("CONFID_RATING"), '[CONFID_RATING] = \'POOR\'') as cursor:
```

7.  Create a counter variable that will be used to print the progress of the script. Make sure you indent this line of code and all the lines of code that follow inside the with block:
```py
cntr = 1
```

8.  Delete the returned rows by calling the deleteRow() method. This is done by looping through the returned cursor and deleting the rows one at a time:
```py
for row in cursor:
        cursor.deleteRow()
        print("Record number " + str(cntr) + " deleted") cntr = cntr + 1
```

9.  Add the except block to print any errors that may occur:
```py
except Exception as e: print(e.message)
```

10. The entire script should appear as follows:
```py
import arcpy import os
arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
try:
    with arcpy.da.UpdateCursor("FireIncidents",("CONFID_RATING"), '[CONFID_RATING] = \'POOR\'') as cursor:
        cntr = 1
    for row in cursor:
        cursor.deleteRow()
        print("Record number " + str(cntr) + " deleted")
        cntr = cntr + 1
except Exception as e:
    print(e.message)
```

11. You can check your work by examining the C:\ArcpyBook\code\Ch8\ DeleteWildfires.py solution file.

12. Save and run the script. You should see messages being written to the output window as the script runs. 37 records should be deleted from the FireIncidents feature class:
Record number
```py
1 deleted Record number
2 deleted Record number
3 deleted Record number
4 deleted Record number
5 deleted
```

### 8.7.3 How it works

Rows from feature classes and tables can be deleted using the deleteRow() method in UpdateCursor.
In this recipe, we used a where clause in the constructor of UpdateCursor to limit the records returned to only features that included CONFID_RATING of POOR.
We then looped through the features returned in the cursor and called the deleteRow() method to delete the row from the feature class.



## 8.8 Inserting and updating rows inside an edit session

As I've mentioned throughout the chapter, inserts, updates, or deletes made to a table or feature class done outside an edit session are permanent.
They can't be undone.
Edit sessions give you much more flexibility to roll back any unwanted changes.


### 8.8.1 Getting ready

Up until now, we've used insert and update cursors to add, edit, and delete data from feature classes and tables.
These changes are permanent as soon as the script is executed and can't be undone.
The new Editor class in the data access module supports the ability to create edit sessions and operations.
With edit sessions, changes applied to feature classes or tables are temporary until permanently applied with a specific method call.
This is the same functionality provided by the Edit toolbar in ArcGIS for Desktop.
Edit sessions begin with a call to Editor.startEditing(), which initiates the session.
Inside the session, you then start an operation with the Editor.startOperation() method.
Within this operation, you then perform various operations that perform edits on   your data.
These edits can also be subject to undo, redo, and abort operations to roll back,  roll forward, and abort your editing operations.
After the operations have been completed, you then call the Editor.stopOperation() method followed by Editor.stopEditing().
Sessions can be ended without saving changes.
In this event, changes are not permanently applied.
An overview of this process is provided in the following screenshot:

Edit sessions can also be ended without saving changes.
In this event, changes are not permanently applied.
Edit sessions also allow for operations to be applied inside the session and then either applied permanently to the database or rolled back.
Additionally, the Editor class also supports undo and redo operations.
The following code example shows the full edit session stack, including the creation of the Editor object, the beginning of an edit session and an operation, edits to the data (an insert operation in this case), stopping the operation, and finally, the end of the edit session by saving the data:
```py
edit = arcpy.da.Editor('Database Connections/Portland.sde') edit.startEditing(False)
edit.startOperation()
with arcpy.da.InsertCursor("Portland.jgp.schools",("SHAPE","Name")) as cursor:
    cursor.insertRow([(7642471.100, 686465.725), 'New School']) edit.stopOperation()
edit.stopEditing(True)
```

The Editor class can be used with personal, file, and ArcSDE geodatabases.
Also, sessions can also be started and stopped on versioned databases.
You are limited to editing only a single workspace at a time, and this workspace is specified in the constructor of the Editor object simply by passing in a string that references the workspace.
Once created, this Editor object then has access to all the methods to start, stop, and abort operations as well as perform undo and redo operations.



### 8.8.2 How to do it

Follow these steps to wrap UpdateCursor inside an edit session:
1.  Open IDLE.

2.  Open the C:\ArcpyBook\Ch8\UpdateWildfires.py script and save it to a new script called C:\ArcpyBook\Ch8\EditSessionUpdateWildfires.py.

3.  We're going to make several alterations to this existing script that updates values in the CONFID_RATING field.

4.  Remove the following lines of code:
```py
arcpy.AddField_management("FireIncidents","CONFID_RATING", "TEXT","10")
print("CONFID_RATING field added to FireIncidents")
```

5.  Create an instance of the Editor class and start an edit session.
These lines of code should be placed inside the try block:
```py
edit = arcpy.da.Editor(r'C:\ArcpyBook\Ch8\WildfireData\ WildlandFires.mdb')
edit.startEditing(True)
```

6.  Alter the if statement so that it appears as follows:
```py
if row[0] > 40 and row[0] <= 60: row[1] = 'GOOD'
elif row[0] > 60 and row[0] <= 85: row[1] = 'BETTER'
else:
row[1] = 'BEST'
```

7.  End the edit session and save the edits. Place this line of code just below the counter increment:
edit.stopEditing(True)

8.  The entire script should appear as follows:
```py
import arcpy import os
arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
try:
    edit = arcpy.da.Editor(r'C:\ArcpyBook\Ch8\WildfireData\ WildlandFires.mdb')
    edit.startEditing(True)
    with arcpy.da.UpdateCursor("FireIncidents",("CONFIDENCEVALUE", "CONFID_RATING")) as cursor:
        cntr = 1
        for row in cursor:
            # update the confid_rating field if row[0] > 40 and row[0] <= 60:
            row[1] = 'GOOD'
        elif row[0] > 60 and row[0] <= 85:
            row[1] = 'BETTER'
        else:
            row[1] = 'BEST'
        cursor.updateRow(row)
        print("Record number " + str(cntr) + " updated") cntr = cntr + 1
        edit.stopEditing(True)
except Exception as e:
    print(e.message)
```

9.  You can check your work by examining the C:\ArcpyBook\code\Ch8\ EditSessionUpdateWildfires.py solution file.

10. Save and run the script to update 374 records.

 8.8.3 How it works

Edit operations should take place inside an edit session, which can be initiated with the Editor.startEditing() method.
The startEditing() method takes two optional parameters including with_undo and multiuser_mode.
The with_undo parameter accepts a Boolean value of true or false, with a default of true.
This creates an undo/ redo stack when set to true.
The multiuser_mode parameter defaults to true.
When it's false, you have full control of editing a nonversioned or versioned dataset.
If your dataset is nonversioned and you use stopEditing(False), your edit will not be committed.
Otherwise, if set to true, your edits will be committed.
The Editor.stopEditing() method takes a single Boolean value of true or false, indicating whether changes should be saved or not.
This defaults to true.
The Editor class supports undo and redo operations.
We'll first look at undo operations.
During an edit session, various edit operations can be applied.
In the event that you need to undo a previous operation, a call to Editor.undoOperation() will remove the most recent edit operation in the stack.
This is illustrated as follows:

Redo operations, initiated by the Editor.redoOperation() method, will redo an operation that was previously undone.
This is illustrated as follows:


## 8.9 Reading geometry from a feature class

There may be times when you need to retrieve the geometric definition of features in a feature class.
ArcPy provides the ability to read this information through various objects.


### 8.9.1 Getting ready

In ArcPy, feature classes have associated geometry objects, including Polygon, Polyline, PointGeometry, or MultiPoint that you can access from your cursors.
These objects refer to the shape field in the table attribute of a feature class.
You can read the geometries of each feature in a feature class through these objects.

Polyline and polygon feature classes are composed of features containing multiple parts.
You can use the partCount property to return the number of parts per feature and then use getPart() for each part in the feature to loop through each of the points and pull out the coordinate information.
Point feature classes are composed of one PointGeometry object per feature that contains the coordinate information for each point.

In this recipe, you will use the SearchCursor and Polygon objects to read the geometry of a polygon feature class.


### 8.9.2 How to do it

Follow these steps to learn how to read the geometric information from each feature in a feature class:
1.  Open IDLE and create a new script.

2.  Save the script to C:\ArcpyBook\Ch8\ReadGeometry.py.

3.  Import the arcpy module:
```py
import arcpy
```

4.  Set the input feature class to the SchoolDistricts polygon feature class:
```py
infc = "c:/ArcpyBook/data/CityOfSanAntonio.gdb/SchoolDistricts"
```

5.  Create a SearchCursor object with the input feature class, and return the ObjectID and Shape fields. The Shape field contains the geometry for each feature. The cursor will be created inside a for loop that we'll use to iterate all the features in the feature class:
```py
for row in arcpy.da.SearchCursor(infc, ["OID@", "SHAPE@"]):
    # Print the object id of each feature.
    # Print the current ID
    print("Feature {0}:".format(row[0])) partnum = 0
```

6.  Use a for loop to loop through each part of the feature:
```py
# Step through each part of the feature
for part in row[1]:
    # Print the part number
    print("Part {0}:".format(partnum))
```

7.  Use a for loop to loop through each vertex in each part and print the X and Y
```py
coordinates:
    # Step through each vertex in the feature
    #
    for pnt in part: if pnt:
        # Print x,y coordinates of current point
        #
        print("{0}, {1}".format(pnt.X, pnt.Y)) else:
            # If pnt is None, this represents an interior ring
            #
            print("Interior Ring:") partnum += 1
```

8.  You can check your work by examining the C:\ArcpyBook\code\Ch8\ ReadGeometry.py solution file.

9.  Save and run the script. You should see the following output as the script writes the information for each feature, each part of the feature, and the X and Y coordinates that define each part:
```
Feature 1:
Part 0:
-98.492224986, 29.380866971
-98.489300049, 29.379610054
-98.486967023, 29.378995028
-98.48503096, 29.376808947
-98.481447988, 29.375624018
-98.478799041, 29.374304981
```

### 8.9.3 How it works

We initially created a SearchCursor object to hold the contents of our feature class.
After this, we looped through each row in the cursor by using a for loop.
For each row, we looped through all the parts of the geometry.
Remember that polyline and polygon features are composed of two or more parts.
For each part, we also return the points associated with each part and we print the X and Y coordinates of each point.



## 8.10 Using Walk() to navigate directories

In this recipe, you will learn how to generate data names in a catalog tree using the Arcpy Walk() function.
Though similar to the Python os.walk() function, the da.Walk() function provides some important enhancements related to geodatabases.


### 8.10.1 Getting ready

The Walk() function, which is part of arcpy.da, generates data names in a catalog tree by walking the tree top-down or bottom-up.
Each directory or workspace yields a tuple containing the directory path, directory names, and filenames.
This function is similar to the Python os.walk() function but it has the added advantage of being able to recognize geodatabase structures.
The os.walk() function is file-based so it isn't able to tell you information about geodatabase structures while arcpy.da.walk() can do so.


### 8.10.2 How to do it

Follow these steps to learn how to use the da.Walk() function to navigate directories and workspaces to reveal the structure of a geodatabase:

1. In IDLE, create a new Python script called DAWalk.py and save it to the
C:\ArcpyBook\data folder.

2. Import the arcpy, arcpy.da, and os modules:
```py
import arcpy.da as da import os
```

3. First, we'll use os.walk() to obtain a list of filenames in the current directory. Add this code:
```py
print("os walk")
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        print(filename)
```

4. Save the file and run it to see output similar to what you see here:
```
a00000001.gdbindexes
a00000001.gdbtable
a00000001.gdbtablx
a00000002.gdbtable
a00000002.gdbtablx
a00000003.gdbindexes
a00000003.gdbtable
a00000003.gdbtablx
a00000004.CatItemsByPhysicalName.atx
a00000004.CatItemsByType.atx
a00000004.FDO_UUID.atx
a00000004.freelist
a00000004.gdbindexes
a00000004.gdbtable
a00000004.gdbtablx
```

5. Although os.walk() can be used to print all filenames within a directory, you'll notice that it doesn't have an understanding of the structure of Esri GIS format datasets,  such as file geodatabases. Files, such as a000000001.gdbindexes, are physical files that make up a feature class but os.walk() can't tell you the logical structure of a feature class. In the next step, we'll use da.walk() to resolve this problem.

6. Comment out the code you just added.

7. Add the following code block:
print("arcpy da walk")
for dirpath, dirnames, filenames in da.Walk(os.getcwd(),datatype=" FeatureClass"):
for filename in filenames: print(os.path.join(dirpath, filename)

8. The entire script should appear as follows:
```py
import arcpy.da as da import os
print("os walk")
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        print(filename)
        print("arcpy da walk")
        for dirpath, dirnames, filenames in da.Walk(os.getcwd(),datatype="FeatureClass"):
            for filename in filenames:
                print(os.path.join(dirpath, filename))
```

9. You can check your work by examining the C:\ArcpyBook\code\Ch8\Walk.py solution file.

10. Save and execute the script to see the following output.
Notice how much cleaner the output is and that the actual feature class names contained within the geodatabase are printed out instead of the physical filenames:
```
C:\ArcpyBook\data\Building_Permits.shp
C:\ArcpyBook\data\Burglaries_2009.shp
C:\ArcpyBook\data\Streams.shp
C:\ArcpyBook\data\CityOfSanAntonio.gdb\Crimes2009
C:\ArcpyBook\data\CityOfSanAntonio.gdb\CityBoundaries
C:\ArcpyBook\data\CityOfSanAntonio.gdb\CrimesBySchoolDistrict
C:\ArcpyBook\data\CityOfSanAntonio.gdb\SchoolDistricts
C:\ArcpyBook\data\CityOfSanAntonio.gdb\BexarCountyBoundaries
C:\ArcpyBook\data\CityOfSanAntonio.gdb\Texas_Counties_LowRes
C:\ArcpyBook\data\CityOfSanAntonio.gdb\Burglary
C:\ArcpyBook\data\TravisCounty\BuildingPermits.shp
C:\ArcpyBook\data\TravisCounty\CensusTracts.shp
C:\ArcpyBook\data\TravisCounty\CityLimits.shp
C:\ArcpyBook\data\TravisCounty\Floodplains.shp
C:\ArcpyBook\data\TravisCounty\Hospitals.shp
C:\ArcpyBook\data\TravisCounty\Schools.shp
C:\ArcpyBook\data\TravisCounty\Streams.shp
C:\ArcpyBook\data\TravisCounty\Streets.shp
C:\ArcpyBook\data\TravisCounty\TravisCounty.shp
C:\ArcpyBook\data\Wildfires\WildlandFires.mdb\FireIncidents
```

### 8.10.3 How it works

The da.Walk() function accepts two parameters including the top-level workspace that will be retrieved (the current working directory), as well as the data type that will be used to filter the returned list.
In this case, we retrieved only feature class-related files.
The Walk() function returns a tuple containing the directory path, directory names, and filenames.
