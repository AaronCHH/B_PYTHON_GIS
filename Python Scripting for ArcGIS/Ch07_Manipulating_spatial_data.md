
# Chapter 7: Manipulating spatial data

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 7: Manipulating spatial data](#chapter-7-manipulating-spatial-data)
  * [7.1 Introduction](#71-introduction)
  * [7.2 Using cursors to access data](#72-using-cursors-to-access-data)
    * [Search](#search)
    * [Insert](#insert)
    * [Update](#update)
  * [7.3 Using SQL in Python](#73-using-sql-in-python)
  * [7.4 Working with table and fild names](#74-working-with-table-and-fild-names)
  * [7.5 Parsing table and field names](#75-parsing-table-and-field-names)
  * [7.6 Working with text files](#76-working-with-text-files)
  * [Points to remember](#points-to-remember)

<!-- tocstop -->


## 7.1 Introduction

> This chapter introduces the ArcPy data access module arcpy .
da for working with data.

> This module allows control of an edit session, edit ing operations, cursor support, functions for converting tables and feature classes to and from NumPy arrays for additional processing, and support for versioning and replica workflows.

> This chapter focuses on cursors, which are used to iterate over rows in a table.
Different types of cursors can be used to search records , add new records , and make changes to exist ing records.

> Search cursors can be used to carry out SQL query expressions in Python.

> Validation of text and fteld names is also covered


## 7.2 Using cursors to access data

| Cursor Type | Method    | Description                                |
|-------------|-----------|--------------------------------------------|
| Search      | next      | Retrieves the next row                     |
|             | reset     | Resets the cursor to its sta ing position  |
| Inset       | insertRow | Inserts a row into the table               |
|             | next      | Retrieves the next row object              |
| Update      | deleteRow | Removes the row from the table             |
|             | next      | Retrieves the next row object              |
|             | reset     | Resets the cursor to its starting position |
|             | updateRow | Updates the current row                    |

```py
arcpy.da.InsertCursor(in_table, field_names)
arcpy.da.SearchCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explore_to_points})
arcpy.da.UpdateCursor(in_table, field_names, {where_clause}, {spatial_reference}, {explore_to_polnts})
```

### Search

> Following is an example of using a search cursor to iterate over the rows in a table.
In the example code that fo llows, the SearchCursor function retrieves the rows in a table.
A for loop is used to it over the rows in the table and print the values for a given field.


```python
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.SearchCursor(fc, ["STREETNAME"])
for row in cursor:
    print "Streetname={0}".format(row[0])
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-4-0e54c8c7adcc> in <module>()
          1 import arcpy
          2 fc = "C:/Data/study.gdb/roads"
    ----> 3 cursor = arcpy.da.SearchCursor(fc, ["STREETNAME"])
          4 for row in cursor:
          5     print "Streetname={0}".format(row[0])


    RuntimeError: cannot open 'C:/Data/study.gdb/roads'


> Search and update cursors also support with statements.
A with state ment has the advantage of guaranteeing closure and release of database locks and resetting iteration , regardless of whether the cursor fmished run ning successfully or not.
The previous example using a with statement is coded as follows:



```python
import arcpy
fc = "C:/Data/study.gdb/roads"
with arcpy.da_SearchCursor(fc,["STREETNAME"]) as cursor:
    for row in cursor:
        print "Streetname={0}".format(row[0])
```

### Insert

> The following code illustrates how a new row is inserted.
A cursor object is created using the InsertCursor function.
Once the cursor is created, the insertRow method is used to insert a list of values that will be included by the new row.
The code is as follows:


```python
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.InsertCursor(fc, ["STREETNAME"])
cursor.insertRow(["NEW_STREET"] )
```

> You can insert multiple rows using a loop:


```python
cursor = arcpy.da.InsertCursor(fc, ["STREETNAME"])
x = 1
while x <= 5:
    cursor.insertRow(["NEWS_TREET"])
    x+= 1
```

### Update

> In the following example, the cursor object is created using the UpdateCursor function.
In the for loop , the values of one held (Acres) in the row are updated using the values of another held (Shape_Area).
If the Shape_Area held is in square feet , the value needs to be divided by 43 ,560 to obtain the area in acres.
The row is updated using the updateRow method on the row object.


```python
import arcpy
fc = "C:/Data/study.gdb/zones"
cursor = arcpy.da.UpdateCursor(fc, ["ACRES", "SHAPEAREA"])
for row in cursor:
    row[0] = row[1]/43560
    cursor.updateRow([row])
```

> The deleteRow method is used to delete the row at the current position of the UpdateCursor.
After the cursor retrieves the row object, calling the deleteRow method deletes the row, as follows:


```python
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.UpdateCursor(fc,["STREETNAME"])
for row in cursor:
if row[0] == "MAINST":
    cursor.deleteRow()
```

> Once an exclusive lock is created by a script, the lock persists until the script releases the lock.
This is accomplished using the del statement to delete the cursor object creating the lock.
Without this statement, a lock could needlessly block other applications or scripts from accessing a data set.
A typical script that creates an insert or update cursor should therefore include two del statements - one to delete the row object, such as del row, and one to delete the cursor object, such as del cursor .
For example:


```python
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.UpdateCursor(fc, ["STREETNAME"])
for row in cursor:
if row[0] == "MAINST":
    cursor.deleteRow()
del row
del cursor
```

* __TIP__
Forgetting to use the del statements at the end of a script can lead to errors so be sure to include the del statements after using insert and update cursor.
Search and update cursors suppo wi th statements , which guarantee closure and release of database locks .
Therefore, when a wi th statement is used , the del statements are not needed.

## 7.3 Using SQL in Python

> SQL queries can be carried out in Python using the SearchC urso r function.
The syntax for SearchCursor is

```py
SearchCursor(in_table, field_names {where_clause}, {spatial_reference}, {felds}, {explode_to_points})
```

> The following code shows an examp1e of using an SQL expression:


```python
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.SearchCursor(fc, ["NAME", "CLASSCODE"], '"CLASSCODE"=1')
for row in cursor:
    print row[0]
del row
del cursor
```

> SQL syntax can be cumbersome since it depends on the format of the feature class.
For example, field delimiters for shape files and file geodatabase feature classes consist of double quotation marks (“ ”), personal geodatabase feature classes use square brackets ([ ]) , and ArcSDE geodatabase feature classes use no delimiters.
To avoid confusion and to ensure the field delimiters are the correct ones, you can use the AddFieldDelimiters function.
The syntax of this function is

```py
AddFieldDelimiters(datasource , field)
```

> The function recognizes the type of dataset being used, such as a shapefile or personal geodatabase, and adds the correct delimiters.
In the following example code, the fie1d name is first assigned to a variable and the AddFieldDelimiters function is used to add the correct de1imiters to the field name prior to using it in an SQL explession:


```python
import arcpy
fc = "C:/Data/zipcodes.shp"
fieldname = "CITY"
delimfield = arcpy.AddFieldDelimiters(fc, fieldname)
cursor = arcpy.da.SearchCursor(fc, ["NAME", "CLASSCODE"], delimfield + " = 'LONGWOOD'")
for row in cursor:
    print row[0]
del row
del cursor
```

> SQL is commonly used in other functions as well.
A number of built-in tools use SQL - for example, the Select tool.
The generic syntax of the Select tool is

```py
Select_analysis(in_features, out_feature_class, {where_clause})
```

> The where_clause parameter is an SQL expression, and to avoid confusion over the proper neld delimiters, the following example code also uses the AddFieldDelimiters function:


```python
import arcpy
infc = "C:/Data/zipcodes.shp"
fieldname = "CITY"
outfc = "C:/Data/zip_select.shp"
delimfield = arcpy AddFieldDelimiters(infc, fieldname)
arcpy.Select_analysis(infc, outfc, delimfield + " = 'LONGWOOD'")
```

## 7.4 Working with table and fild names

> The ValidateTableName function can be used to determine whether a specinc table name is valid for a specinc workspace.
The syntax of this function is

```py
ValidateTableName(name, {workspace})
```

> For example, the following script determines whether all roads is a valid table name for the nle geodatabase called study:


```python
import arcpy
tablename = arcpy.ValidateTableName("all_roads", "C:/Data/study.gdb")
print tablename
```

> In this example, the value all_roads is returned for the table name.
An underscore (_) is added because the table name cannot contain spaces.
Validating table names is commonly used w hen moving data from one work space to another.
For example, the following code uses the Copy Features tool to copy all shapefiles from a folder to a geodatabase.
The .shp file extension is removed from the file name using the basename property and the nam es are validated prior to copying the shape files to feature classes, as follows



```python
import arcpy
import os
from arcpy import env
env.workspace = "C:/Data"
outworkspace = "C:/Data/test/study.gdb"
fclist = arcpy.ListFeatureClasses()
for shape in fclist:
    fcname = arcpy.Describe(shapefile).basename
    newfcname = arcpy.ValidateTableName(fcname)
    outfc = os.path.join(outworkspace, newfcname)
    arcpy.CopyFeatures_management(shapefile, outfc)
```

> A similar approach can be applied to field names using the ValidateFieldName function.
Fields cannot be added unless their name is valid, so unless field names are validated first a script may fail during execution.
The syntax of this function is

```py
ValidateFieldName(name, {workspace})
```

> The ValidateFieldName func tion takes a field name and a workspace and returns a valid field name for the workspace.
Invalid characters are replaced by an underscore (_).
The following code validates the name of a new field, and then uses the returned value to add the new field using the Add Field tool:


```python
import arcpy
fc = "C:/Data/roads.shp"
fieldname = arcpy.ValidateFieldName("NEW")
arcpy.AddFiel_management(fc, fieldname, "", "", "TEXT", 12)
```

> In this example, the string "NEW%^" is replaced by "NEW__"

> An alternative to trying to determine whether a table name exists is to use the Cr e ate Un iqueName function.
This function creates a unique name in the specifted workspace by appending a number to the input name.
This number is increased until the name is unique.
For example, if the name "Clip" already exists, the CreateUn i que Name function will change it to "Clip0"; if this name also exists, the function will change the name to "Clip1 , " and so on.
This function can be used only to create unique table names w ithin a workspace.
It does not work for fteld names.
For example:



```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
unique_name = arcpy.CreateUniqueName("buffer.shp")
arcpy.Buffer_analysis("roads.shp", unque_name, "100 FEET")
```

## 7.5 Parsing table and field names

> The ParseTableName function can be used to split the fully qualifted name for a dataset into its components. The syntax of this function is

```py
ParseTableName(name, {workspace})
```

> The ParseTableName function returns a single string with the database name, owner name, and table name, each separated by a comma (,).
For example, the following code uses the ParseTableName function on a feature class to obtain the components of the fully gualified name, and then splits these components into a list:



```python
import arcpy
from arcpy import env
env.workspace = "C:/Data/study.gdb"
fc = "roads"
fullname = arcpy.ParseTableName(fc)
namelist = fullname.split(",")
databasename = namelist[0]
ownername = namelist[1]
fcname = namelist[2]
print databasename
print ownername
print fcname
```

> A similar approach can be used to split the fully gualif1 ed name of a f1 eld in a table into its components using the ParseFieldName function.
This function returns a single string with the database name, owner name, table name, and f1 eld name, each separated by a comma (,).

## 7.6 Working with text files

> You can open files using the open function, which has the following syntax:

```py
open(name, {mode}, {buffering})
```

The only reguired argument is a file name and the function returns an object.
For example, the following code opens an existing text file (.txt) on disk.

```py
>>> f = open("C:/Data/sample.txt")
```

> Using only a file name as a parameter returns a &le object you can read from.
If you want to do something else, such as w rite to the file, this must be stated explicitly by specifying a mode.
The most common values for the mode are as follows:


```
r: read mode
w: write mode
+: read/write mode (added to another mode)
b: binary mode (added to another mode - for example rb, wb, and others)
a: append mode
```

> To create a new file object, you can use the open function and specify write mode:

```py
>>> f = open("C:/Data/mytext.txt", "w")
```

> Several file methods exist to manipulate the contents of a text file, including write , read, and close.
Consider the following example:

```py
>>> f = open("C:/Data/mytext.txt", "w")
>>> f.write("Geographic for at on Systems")
>>> f.close()
```

> Running this code creates a new file object.
If the file mytext.txt already exists, the existing file will be overwritten, so be careful.
The write method is used to write a string to the file and the close method is used to close the file (and save its contents).
Reading a file works as follows:

```py
>>> f = open("C:/Data/mytext.txt")
>>> f.read()
```

> When opening a file just to read its contents, it is not necessary to specify a mode because r (read mode) is the default.
The read method is used to read the contents of the text file.
When no argument is specified, the script reads the entire contents of the file.
An optional argument can be supplied to indicate the number of charac ters to be read.
For example:

```py
>>> f = open("C:/Data/mytext.txt")
>>> f.read(3)
```

> Once you open a file, reading the file is like making a single pass through the string of characters.
The next time you use the read method, the script picks up where it stopped the last time.
For example:


```python
>>> f.read(5)
```

> The result is


```python
' graph '
```

For example:


```python
>>> f.read()
```

> The result is
'ic Information Systems'

> After you start reading a file, you can use the seek method to set the file’s current position without opening the file again. For example:


```python
>>> f.seek(0)
>>> f.read(10)
```

> The result is
'Geographic'

![]('Ch07/sql.png')

> Reading the contents of this file can be accomplished in a number of ways, starting with the read method, as follows:


```python
>>> f = open("C:/Data/sqltext.txt")
>>> f.read()
```

> The result is


```python
'Structured\nQuery\nLanguage'
```

> And run again:


```python
>>> f . readline()
```

> The result is


```python
' Query\n '
```

> And run again:


```python
>>> readline()
```

> The result is
' Language '

> The readline method reads the next line from the text file and returns it as a string.
Continuing to use the readl ne m ethod returns the lines that follow.
The line separators (\n) are also returned


Finally, the readlines method reads all the lines in the files and returns the result as a list.
For example:


```python
>>> f = open("C:/Data/sqltext.txt")
>>> f.readlines()
```

The result is


```python
['Structured\n', 'Query\n' , 'Language']
```

Writing a file with multiple lines can be accomplished using the write and writelines methods.
To add new lines, the line separators have to be used.
For example:



```python
>>> f = open("C:/Data/tintext.txt", "w")
>>> f.write("Triangulated\nlrregular\nNode")
>>> f.close()
```

The writelines method can be used to modify the string for a particular line.
For example:


```python
>>> f = open("C:/Data/tintext.txt")
>>> lines = f.readlines()
>>> f.close()
>>> lines[2] = "Network"
>>> f = open("C:/Data/tintext.txt", "w")
>>> f.writelines(lines)
>>> f.close()
```

First, files in Python are iterable , which means you can use them directly in a for loop to iterate over their lines. The code is as follows:


```python
f = open("C:/Data/mytext.txt")
for line in f:
    <function>
f.close()
```

Iteration can also be accomplished using the readline method.
For example:


```python
f = open("C:/Data/mytext.txt")
while True:
    line = f.readline()
    if not line:
        break
    <function>
f.close()
```

For relatively small files, you can also read the entire file in step using the read method (to read the entire file as a string) or the readlines method (to read the file into a list of strings).
For example:


```python
f = open("C:/Data/mytext.txt")
for line in readlines():
    <function>
f.close()
```

Reading the entire file using the read m ethod or the readlines method can use excessive memory.
One alternative is to use a while loop with the readline method.
A second alternative is to use the fileinput module instead of the open function.
This module enables you to create an object that you can iteI over in a for loop.
For example:


```python
import fileinput
for line in fileinput.input("C:/Data/mytext.txt"):
    <function>
```

The following script opens an existing file in read mode and creates a new output file in write mode.
A for loop is used to iterate over the lines in the input file.
In the block of code that follows, the replace method is used three times to remove specific strings from each line.
The resulting string is written to the output file.
The code is as follows:


```python
input = open("C:/Data/coordinates.txt")
output = open("C:/Data/coordinates_clean.txt", "w")
for line in input:
    str = line.replace("ID:", "")
    str = str.replace(", Latitude:","")
    str = str.replace(", Longtude:","")
    output.write(str)
input.close()
output.close()
```

## Points to remember

* The ArcPy data access module, arcpy.da, provides support for editing and cursors.Cursors can be used to iterate over rows in a table.
Iteration is typically accomplished using a for loop or a with statement.

* Search cursors are used to iterate over records.Insert cursors are used to add new records to a table.
Update cursors are used to make changes.

* SQL query expressions can be used in Python using search cursors Proper syntax is facilitated using the AddFieldDelimiters function.

* Table and field names can be validated using the ValidateTable Name and ValidateFieldName functions, respectively.
These functions convert all invalid characters into an underscore (_).
The CreateUniqueName function can be used to cre ate a unique name by adding a number to a name.

* Table and field names can be parsed into separate elements using the ArcPy parsing functions.

* The contents of text files can be manipulated in Python.
The open function creates a file object and a number of methods can be used to read and write text, including read, readline , readlines , write , and telines One of the more common operations on fi les is to iterate over their contents performing the same manipulation repeat edly, such as replacing strings to make the text files more usable.



```python

```
