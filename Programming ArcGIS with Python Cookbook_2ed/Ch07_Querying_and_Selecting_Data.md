
# Chapter 7: Querying and Selecting Data

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 7: Querying and Selecting Data](#chapter-7-querying-and-selecting-data)
  * [7.1 Introduction](#71-introduction)
  * [7.2 Constructing a proper attribute query syntax](#72-constructing-a-proper-attribute-query-syntax)
    * [7.2.1 Getting ready](#721-getting-ready)
    * [7.2.2 How to do it](#722-how-to-do-it)
    * [7.2.3 How it works](#723-how-it-works)
  * [7.3 Creating feature layers and table views](#73-creating-feature-layers-and-table-views)
    * [7.3.1 Getting ready](#731-getting-ready)
    * [7.3.2 How to do it](#732-how-to-do-it)
    * [7.3.3 How it works](#733-how-it-works)
    * [7.3.4 There's more](#734-theres-more)
  * [7.4 Selecting features and rows with the Select Layer by Attribute tool](#74-selecting-features-and-rows-with-the-select-layer-by-attribute-tool)
    * [7.4.1 Getting ready](#741-getting-ready)
    * [7.4.2 How to do it](#742-how-to-do-it)
    * [7.4.3 How it works](#743-how-it-works)
  * [7.5 Selecting features with the Select by Location tool](#75-selecting-features-with-the-select-by-location-tool)
    * [7.5.1 Getting ready](#751-getting-ready)
    * [7.5.2 How to do it](#752-how-to-do-it)
    * [7.5.3 How it works](#753-how-it-works)
  * [7.6 Combining a spatial and attribute query with the Select by Location tool](#76-combining-a-spatial-and-attribute-query-with-the-select-by-location-tool)
    * [7.6.1 Getting ready](#761-getting-ready)
    * [7.6.2 How to do it](#762-how-to-do-it)
    * [7.6.3 How it works](#763-how-it-works)

<!-- tocstop -->

In this chapter, we will cover the following recipes:

* Constructing a proper attribute query syntax
* Creating feature layers and table views
* Selecting features and rows with the Select Layer by Attribute tool
* Selecting features with the Select by Location tool
* Combining a spatial and attribute query with the Select by Location tool


## 7.1 Introduction

Selecting features from a geographic layer or rows from a standalone attribute table is one of the most common GIS operations.
Queries are created to enable these selections, and can   be either attribute or spatial queries.
Attribute queries use SQL statements to select features or rows through the use of one or more fields or columns in a dataset.
An example attribute query would be "Select all land parcels with a property value greater than ```$500,000```".
Spatial queries are used to select features based on some type of spatial relationship.
An example might be "Select all land parcels that intersect a school district" or perhaps "Select all streets that are completely within Travis County, Texas." It is also possible to combine attribute and spatial queries.
An example might be "Select all land parcels that intersect the 100 year floodplain and have a property value greater than ```$500,000```".



## 7.2 Constructing a proper attribute query syntax

The construction of property attribute queries is critical to your success in creating geoprocessing scripts that query data from feature classes and tables.

All attribute queries that you execute against feature classes and tables will need to have the correct SQL syntax and also follow various rules depending upon the data type that you execute the queries against.


### 7.2.1 Getting ready

Creating the syntax for attribute queries is one of the most difficult and time-consuming tasks that you'll need to master when creating Python scripts that incorporate the use of the Select by Attributes tool.
These queries are basically SQL statements along with a few idiosyncrasies that you'll need to master.
If you already have a good understanding of creating queries in ArcMap or perhaps experience in creating SQL statements in other programming languages, then this will be a little easier for you.
In addition to creating valid SQL statements, you also need to be aware of some specific Python syntax requirements and some data type differences that will result in a slightly altered formatting of your statements for some data types.
In this recipe, you'll learn how to construct valid query syntax and understand the nuances of how different data types alter the syntax as well as some Python-specific constructs.


### 7.2.2 How to do it

Initially, we're going to take a look at how queries are constructed in ArcMap, so that you can get a feel of how they are structured.

1. In ArcMap, open C:\ArcpyBook\Ch7\Crime_Ch7.mxd.

2. Right-click on the Burglaries in 2009 layer and select Open Attribute Table.
You should see an attribute table similar to the following screenshot.
We're going to be querying the SVCAREA field:

3. With the attribute table open, select the Table Options button and then Select by Attributes to display a dialog box that will allow you to construct an attribute query.
Notice the Select * FROM Burglary WHERE: statement on the query dialog box (shown in the following screenshot).
This is a basic SQL statement that will return all the columns from the attribute table for Burglary that meet the condition that we define the query builder.
The asterisk (*) simply indicates that all fi lds will be returned:

4. Make sure that Create a new selection is the selected item in the Method dropdown list.
This will create a new selection set.

5. Double-click on SVCAREA from the list of fields to add the field to the SQL statement builder, as follows:

6. Click on the = button.

7. Click on the Get Unique Values button.

8. From the list of values generated, double-click on 'North' to complete the SQL statement, as shown in the following screenshot:

9. Click on the Apply button to execute the query.
This should select 7520 records.
Many people mistakenly assume that you can simply take a query that has been generated in this fashion and paste it into a Python script.
That is not the case.
There are some important differences that we'll cover next.

10. Close the Select by Attributes window and the Burglaries in 2009 table.

11. Clear the selected feature set by navigating to Selection | Clear Selected Features.

12. Open the Python window and add the code to import arcpy:
import arcpy

13. Create a new variable to hold the query and add the same statement that you created earlier:
```sql
qry = "SVCAREA" = 'North'
```

14. Press Enter on your keyboard and you should see an error message similar to the following: Runtime error SyntaxError: can't assign to literal ```(<string>, line 1)```
Python interprets SVCAREA and North as strings, but the equal to sign between the two is not part of the string used to set the qry variable.
There are several things we need to do to generate a syntactically correct statement for the Python interpreter.
One important thing has already been taken care of though.
Each field name used in a query needs to be surrounded by double quotes.
In this case, SVCAREA is the only field used in the query and it has already been enclosed by double quotes.
This will always be the case when you're working with shapefiles, file geodatabases, or ArcSDE geodatabases.
Here is where it gets a little confusing though.
If you're working with data from a personal geodatabase, the field names will need to be enclosed by square brackets instead of double quotes, as shown in the following code example.
This can certainly leads to confusion for script developers:
```sql
qry = [SVCAREA] = 'North'
```
Now, we need to deal with the single quotes surrounding 'North'.
When querying data from fields that have a text data type, the string being evaluated must be enclosed by quotes.
If you examine the original query, you'll notice that we have in fact already enclosed North with quotes, so everything should be fine, right? Unfortunately, it's not that simple with Python.
Quotes along with a number of other characters must be escaped with a forward slash followed by the character being escaped.
In this case, the escape sequence would be \' as shown in the following steps:

15. Alter your query syntax to incorporate the escape sequence:
```sql
qry = "SVCAREA" = \'North\'
```

16. Finally, the entire query statement should be enclosed with quotes:
```sql
qry = '"SVCAREA" = \'North\''
```
In addition to the = sign, which tests for equality, there are a number of additional operators that you can use with strings and numeric data, including not equal (< >), greater than (>), greater than or equal to (>=), less than (<), and less than or equal to (<=).
Wildcard characters, including % and _, can also be used for shapefiles, file geodatabases, and ArcSDE geodatabases.
These include % that represents any number of characters.
The LIKE operator is often used with wildcard characters to perform partial string matching.
For example, the following query would find all records with a service area that begins with N and has any number of characters after it:
```sql
qry = '"SVCAREA" LIKE \'N%\''
```
The (_) underscore character can be used to represent a single character.
For personal geodatabases, the (*) asterisk is used to represent a wildcard character for any number of characters, while (?) represents a single character.
You can also query for the absence of data, also known as NULL values.
A NULL value is often mistaken for a value of zero, but this does not always hold true.
The NULL values indicate the absence of data, which is different from a value of zero.
Null operators include IS NULL and   IS NOT NULL.
The following code example will find all the records where the SVCAREA field contains no data:
```sql
qry = '"SVCAREA" IS NULL'
```
The final topic that we'll cover in this section are operators used to combine expressions where multiple query conditions need to be met.
The AND operator requires that both query conditions be met for the query result to be true, resulting in selected records.
The OR operator requires that at least one of the conditions be met.


### 7.2.3 How it works

The creation of syntactically correct queries is one of the most challenging aspects of programming ArcGIS with Python.
However, once you understand some basic rules, it gets a little easier.
In this section, we'll summarize these rules.
One of the more important things to keep in mind is that field names must be enclosed with double quotes for all datasets, with the exception of personal geodatabases, which require braces surrounding field names.
There is also an AddFieldDelimiters() function that you can use to add the correct delimiter to a field based on the datasource supplied as a parameter to the function.
The syntax for this function is as follows:
```py
AddFieldDelimiters(dataSource,field)
```
Additionally, most people, especially those new to programming with Python, struggle with the issue of adding single quotes to string values being evaluated by the query.
In Python, quotes  have to be escaped with a single forward slash followed by the quote.
Using this escape sequence will ensure that Python does in fact see this as a quote rather than the end of the string.
Finally, take some time to familiarize yourself with the wildcard characters.
For datasets  other than personal geodatabases, you'll use the % character for multiple characters and an underscore character for a single character.
If you're using a personal geodatabase, the * character is used to match multiple characters and the ? character is used to match a single character.
Obviously, the syntax differences between personal geodatabases and all other types of datasets can lead to some confusion.


## 7.3 Creating feature layers and table views

Feature layers and table views serve as intermediate datasets held in memory specifically for use with tools, such as Select by Location and Select Attributes.
Although these temporary datasets can be saved, they are not needed in most cases.



### 7.3.1 Getting ready

Feature classes are physical representations of geographic data and are stored as files (shapefiles, personal geodatabases, and file geodatabases) or within a geodatabase.
Environmental Systems Research Institute (Esri) defines a feature class as "a collection of features that shares a common geometry (point, line, or polygon), attribute table, and spatial reference."

Feature classes can contain default and user-defined fields.
Default fields include the SHAPE and OBJECTID fields.
These fields are maintained and updated automatically by ArcGIS.
The SHAPE field holds the geometric representation of a geographic feature, while the OBJECTID field holds a unique identifier for each feature.
Additional default fields will also exist depending on the type of feature class.
A line feature class will have a SHAPE_LENGTH field.
A polygon feature class will have both, a SHAPE_LENGTH and a SHAPE_AREA field.

Optional fields are created by end users of ArcGIS and are not automatically updated by GIS.
These contain attribute information about the features.
These fields can also be updated by your scripts.

Tables are physically represented as standalone DBF (also known as dBase File Format) tables or within a geodatabase.
Both, tables and feature classes, contain attribute information.
However, a table contains only attribute information.
There isn't a SHAPE field associated with a table, and they may or may not contain an OBJECTID field.

Standalone Python scripts that use the Select by Attributes or Select by Location tool require that you create an intermediate dataset rather than using feature classes or tables.
These intermediate datasets are temporary in nature and are called feature layers or table views.
Unlike feature classes and tables, these temporary datasets do not represent actual files on disk or within a geodatabase.
Instead, they are an in-memory representation of feature classes and tables.
These datasets are active only while a Python script is running.
They are removed from memory after the tool has been executed.
However, if the script is  run from within ArcGIS as a script tool, then the temporary layer can be saved either by right- clicking on the layer in the table of contents and selecting Save As Layer File or simply by saving the map document file.

Feature layers and table views must be created as a separate step in your Python scripts before you can call the Select by Attributes or Select by Location tools.
The Make Feature Layer tool generates the in-memory representation of a feature class, which can then be used to create queries and selection sets as well as join tables.
After this step has been completed, you can use the Select by Attributes or Select by Location tool.
Similarly, the Make Table View tool is used to create an in-memory representation of a table.
The function of this tool is the same as Make Feature Layer.
Both the Make Feature Layer and Make Table View tools require an input dataset, an output layer name, and an optional query expression, which can be used to limit the features or rows that are a part of the output layer.
In addition to this, both tools can be found in the Data Management Tools toolbox.

The syntax to use the Make Feature Layer tool is as follows:
```py
arcpy.MakeFeatureLayer_management(<input feature layer>, <output layer name>,{where clause})
```
The syntax to use the Make Table View tool is as follows:
```py
Arcpy.MakeTableView_management(<input table>, <output table name>, {where clause})
```
In this recipe, you will learn how to use the Make Feature Layer and Make Table View tools.
These tasks will be done inside ArcGIS, so that you can see the in-memory copy of the layer that is created.


### 7.3.2 How to do it

Follow these steps to learn how to use the Make Feature Layer and Make Table View tools:

1.  Open c:\ArcpyBook\Ch7\Crime_Ch7.mxd in ArcMap.

2.  Open the Python window.

3.  Import the arcpy module:
```py
import arcpy
```

4.  Set the workspace:
```py
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"
```

5.  Start a try block:
```py
try:
```

6.  Make an in-memory copy of the Burglary feature class using the Make Feature Layer tool.
Make sure you indent this line of code:
```py
flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_ Layer")
```

7.  Add an except block and a line of code to print an error message in the event of a problem:
```py
except Exception as e: print(e.message)
```

8.  The entire script should appear as follows:
```py
import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb" try:
flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_ Layer")
except Exception as e: print(e.message)
```

9.  Save the script to C:\ArcpyBook\Ch7\CreateFeatureLayer.py.

10. You can check your work by examining the c:\ArcpyBook\code\Ch7\ CreateFeatureLayer.py solution file.

11. Run the script. The new Burglary_Layer file will be added to the ArcMap table
of contents:

12. The functionality of the Make Table View tool is equivalent to the Make Feature Layer tool. The difference is that it works against standalone tables instead of feature classes.

13. Remove the following line of code:
```py
flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_ Layer")
```

14. Add the following line of code in its place:
```py
tView = arcpy.MakeTableView_management("Crime2009Table","Crime2009 TView")
```

15. You can check your work by examining the c:\ArcpyBook\code\Ch7\ CreateTableView.py solution file.

16. Run the script to see the table view added to the ArcMap table of contents.


### 7.3.3 How it works

The Make Feature Layer and Make Table View tools create in-memory representations of feature classes and tables, respectively.
Both, the Select by Attributes and Select by Location tools, require that these temporary, in-memory structures be passed as parameters when called from a Python script.
Both tools also require that you pass a name for the temporary structures.


### 7.3.4 There's more

You can also apply a query to either the Make Feature Layer or the Make Table View tools to restrict the records returned in the feature layer or table view.
This is done through the addition of a where clause when calling either of the tools from your script.
This query is similar to a situation where you set a definition query on the layer by navigating to __Layer Properties | Definition Query.__
The syntax to add a query is as follows:
```py
MakeFeatureLayer(in_features, out_layer, where_clause)
MakeTableView(in_table, out_view, where_clause)
```


## 7.4 Selecting features and rows with the Select Layer by Attribute tool

Attribute queries can be executed against a feature class or table through the use of the Select Layer by Attribute tool.
A where clause can be included to filter the selected records and various selection types can be included.



### 7.4.1 Getting ready

The Select Layer by Attribute tool, shown in the following screenshot, is used to select records from a feature class or table based on a query that you define.
We covered the somewhat complex topic of queries in an earlier recipe in this chapter, so hopefully, you now understand the basic concepts of creating a query.
You have also learned how to create a temporary, in-memory representation of a feature class or table, which is a pre-requisite to using either the Select by Attributes or Select by Location tool.

The Select by Attributes tool uses a query along with either a feature layer or table view and a selection method to select records.
By default, the selection method will be a new selection set.
Other selection methods include __"add to selection", "remove from selection", "subset selection", "switch selection", and "clear selection".__
Each of the selection methods is summarized as follows:

* NEW_SELECTION: This is the default selection method and it creates a new selection set
* ADD_TO_SELECTION: This adds a selection set to the currently selected records based on a query
* REMOVE_FROM_SELECTION: This removes records from a selection set based on a query
* SUBSET_SELECTION: This combines selected records that are common to the existing selection set
* SWITCH_SELECTION: This selects records that are not selected currently and unselects the existing selection set
* CLEAR_SELECTION: This clears all records that are currently a part of the selected set

The syntax to call the Select by Attributes tool is as follows:
```py
arcpy.SelectLayerByAttribute_management(<input feature layer or table view>, {selection method}, {where clause})
```
In this recipe, you'll learn how to use the Select by Attributes tool to select features from a feature class.
You'll use the skills you learned in previous recipes to build a query, create a feature layer, and finally call the Select by Attributes tool.


### 7.4.2 How to do it

Follow these steps to learn how to select records from a table or feature class using the
Select Layer by Attributes tool:

1.  Open IDLE and create a new script window.

2.  Save the script to c:\ArcpyBook\Ch7\SelectLayerAttribute.py.

3.  Import the arcpy module:
```
import arcpy
```

4.  Set the workspace to the City of San Antonio geodatabase.
```py
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"
```

5.  Start a try block:
```py
try:
```

6.  Create the query that we used in the first recipe in this chapter. This will serve as a where clause that will select all the records with a service area of North. This line of code and the next four should be indented:
```sql
qry = '"SVCAREA" = \'North\''
```

7.  Make an in-memory copy of the Burglary feature class:
```py
flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_ Layer")
```

8.  Call the Select Layer by Attribute tool by passing in a reference to the feature layer we just created. Define this as a new selection set and pass in a reference to the query:
```py
arcpy.SelectLayerByAttribute_management(flayer, "NEW_SELECTION", qry)
```

9.  Print the number of selected records in the layer using the Get Count tool:
```py
cnt = arcpy.GetCount_management(flayer)
print("The number of selected records is: " + str(cnt))
```

10. Add an except block and a line of code to print an error message in the event of a problem:
```
except Exception as e: print(e.message)
```

11. The entire script should appear as shown in the following code snippet. Please remember to include indentation with the try and except blocks:
```py
import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"
try:
        qry = '"SVCAREA" = \'North\''
        flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_Layer")
        arcpy.SelectLayerByAttribute_management(flayer, "NEW_SELECTION", qry)
        cnt = arcpy.GetCount_management(flayer)
        print("The number of selected records is: " + str(cnt))
except Exception as e:
        print(e.message)
```

12. Save the script.

13. You can check your work by examining the c:\ArcpyBook\code\Ch7\ SelectLayerAttribute.py solution file.

14. Run the script. If everything has been done correctly, you should see a message indicating that 7520 records have been selected:
The total number of selected records is: 7520


### 7.4.3 How it works

The Select by Attributes tool requires that either a feature layer or table view be passed as the first parameter.
In this recipe, we passed a feature layer that was created by the Make Feature Layer tool in the preceding line.
We used Make Feature Layer to create a feature layer from the Burglary feature class.
This feature layer was assigned to the flayer variable, which is then passed into the Select by Attribute tool as the first parameter.
In this script, we also passed in a parameter indicating that we'd like to create a new selection set along with the final parameter, which is a where clause.
The where clause is specified in the qry variable.
This variable holds a query that will select all the features with a service area of North.



## 7.5 Selecting features with the Select by Location tool

The Select Layer by Location tool, as shown in the next screenshot, can be used to select features based on some type of spatial relationship.
Since it deals with spatial relationships, this tool only applies to feature classes and their corresponding in-memory feature layers.


### 7.5.1 Getting ready

There are many different types of spatial relationships that you can apply while selecting features using the Select by Location tool, including intersect, contains, within, boundary touches, is identical, and many others.
If it's not specified, the default intersect spatial relationship will be applied.
The input feature layer is the only required parameter, but there are a number of optional parameters, including the spatial relationship, search distance, a feature layer, or feature class to test against the input layer, and a selection type.
In this recipe, you will learn how to use the Select by Location tool in a Python script to select features based on a spatial relationship.
You'll use the tool to select burglaries that are within the boundaries of the Edgewood school district.


### 7.5.2 How to do it

Follow these steps to learn how to perform a spatial query using the Select by Location tool:

1. Open IDLE and create a new script window.

2. Save the script to c:\ArcpyBook\Ch7\SelectByLocation.py.

3. Import the arcpy module:
```py
import arcpy
```

4. Set the workspace to the City of San Antonio geodatabase:
```py
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"
```

5. Start a try block:
```py
try:
```

6. Make an in-memory copy of the Burglary feature class:
```py
flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_Layer")
```

7. Call the Select Layer by Location tool passing in a reference to the feature layer we just created.
The spatial relationship test will be COMPLETELY_WITHIN, meaning that we want to find all burglaries that are completely within the boundaries of the comparison layer.
Define EdgewoodSD.shp as the comparison layer:
```py
arcpy.SelectLayerByLocation_management (flayer, "COMPLETELY_ WITHIN", "c:/ArcpyBook/Ch7/EdgewoodSD.shp")
```

8. Print the number of selected records in the layer using the Get Count tool:
```py
cnt = arcpy.GetCount_management(flayer)
print("The number of selected records is: " + str(cnt))
```

9. Add an except block and a line of code to print an error message in the event of a problem:
```py
except Exception as e: print e.message
```

10. The entire script should appear as shown in the following code snippet. Remember to include indentation with the try and except blocks:
```py
import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb" try:
flayer =  arcpy.MakeFeatureLayer_ management("Burglary","Burglary_Layer")
arcpy.SelectLayerByLocation_management (flayer, "COMPLETELY_ WITHIN", "c:/ArcpyBook/Ch7/EdgewoodSD.shp")
cnt = arcpy.GetCount_management(flayer)
print("The number of selected records is: " + str(cnt)) except Exception as e:
print("An error occurred during selection")
```

11. Save the script.

12. You can check your work by examining the c:\ArcpyBook\code\Ch7\ SelectByLocation_Step1.py solution file.

13. Run the script. If everything was done correctly, you should see a message indicating that 1470 records have been selected:
The total number of selected records is: 1470
In this case, we did not define the optional search distance and selection type parameters.
By default, a new selection will be applied as the selection type.
We didn't apply a distance parameter in this case, but we'll do this now to illustrate how it works.

14. Update the line of code that calls the Select Layer by Location tool:
```py
arcpy.SelectLayerByLocation_management (flayer, "WITHIN_A_ DISTANCE", "c:/ArcpyBook/Ch7/EdgewoodSD.shp","1 MILES")
```

15. Save the script.

16. You can check your work by examining the c:\ArcpyBook\code\Ch7\ SelectByLocation_Step2.py solution file.

17. Run the script.
If everything was done correctly, you should see a message indicating that 2976 records have been selected.
This will select all burglaries within the boundaries of the Edgewood school district along with any burglaries within one mile of the boundary:
The total number of selected records is: 2976
The final thing you'll do in this section is use the Copy Features tool to write the temporary layer to a new feature class.

18. Comment out the two lines of code that get a count of the number of features and print them to the screen:
```py
## cnt = arcpy.GetCount_management(flayer)
## print("The number of selected records is: " + str(cnt))
```

19. Add a line of code that calls the Copy Features tool.
This line should be placed just below the line of code that calls the Select Layer by Location tool.
The Copy Features tool accepts a feature layer as the first input parameter and an output feature class, which in this case will be a shapefile called EdgewoodBurglaries.shp:
```py
arcpy.CopyFeatures_management(flayer, 'c:/ArcpyBook/Ch7/ EdgewoodBurglaries.shp')
```

20. The entire script should now appear as shown in the following code snippet.
Remember to include indentation with the try and except blocks:
```py
import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb" try:
flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_ Layer")
arcpy.SelectLayerByLocation_management (flayer, "WITHIN_A_ DISTANCE", "c:/ArcpyBook/Ch7/EdgewoodSD.shp","1 MILES")
arcpy.CopyFeatures_management(flayer, 'c:/ArcpyBook/Ch7/ EdgewoodBurglaries.shp')
# cnt = arcpy.GetCount_management(flayer)
# print("The total number of selected records is: " + str(cnt)) except Exception as e:
print(e.message)
```

21. Save the script.

22. You can check your work by examining the c:\ArcpyBook\code\Ch7\ SelectByLocation_Step3.py solution file.

23. Run the script.

24. Examine your c:\ArcpyBook\Ch7 folder to see the output shapefile.


### 7.5.3 How it works

The Select by Location tool requires that a feature layer be passed as the first parameter.
In this recipe, we pass a feature layer that was created by the Make Feature Layer tool in the preceding line.
We used Make Feature Layer to create a feature layer from the Burglary feature class.
This feature layer was assigned to the flayer variable, which is then passed into the Select by Location tool as the first parameter.
In this script, we've also passed a parameter that indicates the spatial relationship that we'd like to apply.
Finally, we've also defined a source layer to use for the comparison of the spatial relationship.
Other optional parameters that can be applied include a search distance and a selection type.



## 7.6 Combining a spatial and attribute query with the Select by Location tool

There may be times when you may want to select features using a combined attribute and spatial query.
For example, you might want to select all burglaries within the Edgewood school district that occurred on a Monday.
This can be accomplished by running the Select by Location and Select by Attributes tools sequentially and applying a SUBSET SELECTION selection type.



### 7.6.1 Getting ready

This recipe will require that you create a feature layer that will serve as a temporary layer, which will be used with the Select by Location and Select Layer by Attributes tools.
The Select by Location tool will find all burglaries that are within the Edgewood School District and apply a selection set to these features.
The Select Layer by Attributes tool uses the same temporary feature layer and applies a where clause that finds all burglaries that occurred on a particular Monday.
In addition to this, the tool also specifies that the selection should be a subset of the currently selected features found by the Select by Location tool.
Finally, you'll print the total number of records that were selected by the combined spatial and attribute query.


### 7.6.2 How to do it

1.  Open IDLE and create a new script window.

2.  Save the script as c:\ArcpyBook\Ch7\SpatialAttributeQuery.py.

3.  Import the arcpy module:
```py
import arcpy
```

4.  Set the workspace to the geodatabase of the City of San Antonio:
```py
arcpy.env.workspace = "c:/ArcpyBook/data/CityofSanAntonio.gdb"
```

5.  Start a try block. You'll have to indent the following line up to the except block:
```py
try:
```

6.  Create a variable for the query and define the where clause:
```py
qry = '"DOW" = \'Mon\''
```

7.  Create the feature layer:
```py
flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_ Layer")
```

8.  Execute the Select by Location tool to find all burglaries within the Edgewood School District:
```py
arcpy.SelectLayerByLocation_management (flayer, "COMPLETELY_ WITHIN", "c:/ArcpyBook/Ch7/EdgewoodSD.shp")
```

9.  Execute the Select Layer by Attributes tool to find all the burglaries that match the query we previously defined in the qry variable. This should be defined as a subset query:
```py
arcpy.SelectLayerByAttribute_management(flayer, "SUBSET_ SELECTION", qry)
```

10. Print the number of records that were selected:
```py
cnt = arcpy.GetCount_management(flayer)
print("The total number of selected records is: " + str(cnt))
```

11. Add the except block:
```py
except Exception as e: print(e.message)
```

12. The entire script should appear as follows:
```py
import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"
try:
    qry = '"DOW" = \'Mon\''
    flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_ Layer")
    arcpy.SelectLayerByLocation_management (flayer, "COMPLETELY_ WITHIN", "c:/ArcpyBook/Ch7/EdgewoodSD.shp")
    arcpy.SelectLayerByAttribute_management(flayer, "SUBSET_ SELECTION", qry)
    cnt = arcpy.GetCount_management(flayer)
    print("The total number of selected records is: " + str(cnt)) except
Exception as e:
    print(e.message)
```

13. Save and run the script. If everything was done correctly, you should see a message indicating that 197 records have been selected. This will select all the burglaries within the boundaries of the Edgewood School District that occurred on a Monday:
The total number of selected records is: 197

14. You can check your work by examining the c:\ArcpyBook\code\Ch7\ SpatialAttributeQuery.py solution file.



### 7.6.3 How it works

A new feature layer is created with the Make Feature Layer tool and assigned to the variable flayer.
This temporary layer is then used as an input to the Select by Location tool along with   a COMPLETELY_WITHIN spatial operator, to fi all the burglaries within the Edgewood School District.
This same feature layer, with a selection set already defi  d, is then used as an input parameter to the Select Layer by Attributes tool.
In addition to passing a reference to the feature layer, the Select Layer by Attributes tool is also passed a parameter that defi s the selection type and a where clause.
The selection type is set to SUBSET_SELECTION.
This selection type creates a new selection that is combined with the existing selection.
Only the records that are common to both remain selected.
The where clause passed in as the third parameter is an attribute query to fi all the burglaries that occurred on a Monday.
The query uses the DOW fi ld and looks for a value of Mon.
Finally, the Get Count tool is used against the flayer variable to get a count of the number of selected records, and this is printed on the screen.
