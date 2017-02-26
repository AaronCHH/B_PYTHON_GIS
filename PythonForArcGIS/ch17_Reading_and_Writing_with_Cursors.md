
# 17 Reading and Writing with Cursors

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [17 Reading and Writing with Cursors](#17-reading-and-writing-with-cursors)
  * [17.1 Introduction to Cursors](#171-introduction-to-cursors)
  * [17.2 Reading Rows](#172-reading-rows)
  * [17.3 The Field Names Parameter](#173-the-field-names-parameter)
    * [Example 17.1: Print data values with unknown field names](#example-171-print-data-values-with-unknown-field-names)
  * [17.4 The Shape Field and Geometry Tokens](#174-the-shape-field-and-geometry-tokens)
  * [17.5 Looping with Cursors](#175-looping-with-cursors)
  * [17.6 Locking](#176-locking)
    * [17.6.1 The del Statement](#1761-the-del-statement)
    * [Example 17.2: Using try/except blocks with cursor looping](#example-172-using-tryexcept-blocks-with-cursor-looping)
    * [17.6.2 The with Statement](#1762-the-with-statement)
  * [17.7 Update Cursors](#177-update-cursors)
    * [Example 17.3: Perform more than one update](#example-173-perform-more-than-one-update)
    * [Example 17.4: Delete rows](#example-174-delete-rows)
  * [17.8 Insert Cursors](#178-insert-cursors)
    * [Example 17.5: Insert a row.](#example-175-insert-a-row)
    * [Example 17.6: Find the maximum value of an attribute and insert multiple rows using this information](#example-176-find-the-maximum-value-of-an-attribute-and-insert-multiple-rows-using-this-information)
    * [17.8.1 Inserting Geometric Objects](#1781-inserting-geometric-objects)
    * [Create 2 polyline endpoints](#create-2-polyline-endpoints)
    * [Create an array with a Python list of Point objects.](#create-an-array-with-a-python-list-of-point-objects)
    * [Create a line with an Array object that has points.](#create-a-line-with-an-array-object-that-has-points)
    * [Example 17.7: Insert a point](#example-177-insert-a-point)
    * [Example 17.8: Insert a polygon](#example-178-insert-a-polygon)
  * [17.9 Selecting Rows with SQL](#179-selecting-rows-with-sql)
    * [Example 17.9:Use awhere_clause with a cursor](#example-179use-awhere_clause-with-a-cursor)
    * [Example 17.10: Use a cursorwhere_clause with a variable](#example-1710-use-a-cursorwhere_clause-with-a-variable)
  * [17.10 Key Terms](#1710-key-terms)
  * [17.11 Exercises](#1711-exercises)

<!-- tocstop -->



```python
import os, sys, arcpy
```

## 17.1 Introduction to Cursors

## 17.2 Reading Rows


```python
import arcpy
# Create a cursor
fc = 'C:/gispy/data/ch17/ fires.shp'
cursor = arcpy.da.SearchCursor fc, ['FID', 'FireId', 'FireName'])
```


```python
row = cursor.next() # Get an individual row.
row
```


```python
row[0]# FID
```


```python
row[1]# FireId
```


```python
row[2]# FireName
```


```python
row = cursor.next()# Get the second row
row
```


```python
row = cursor.next()# Get the third row
row
```


```python
cursor.reset()
row = cursor.next()
row
```


```python
fds = cursor. fields
fds
```


```python
row = sc.next# Missing parentheses!
row
```


```python
row[0]
```

## 17.3 The Field Names Parameter


```python
# Create a cursor
fc = 'C:/gispy/data/ch17/ fires.shp'
cursor = arcpy.da.SearchCursor(fc, ['FireName', 'FID'])
row = cursor.next()
row
```


```python
row[0]
```


```python
row[1]
```


```python
# Create a cursor with access to ALL the fields.
cursor = arcpy.da.SearchCursor(fc, '*')
cursor.fields
```

### Example 17.1: Print data values with unknown field names


```python
# %load ch17/script2/printTableExclude.py
# printTableExclude.py
# Purpose: Print the names of the non-geometry non-OID type fields in the
#     input file and the value of these fields for each record.
# Usage: Full path file name
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, sys


def excludeFields(table, types=[]):
    '''Return a list of fields minus those with specified field types'''
    fieldNames = []
    fds = arcpy.ListFields(table)
    for f in fds:
        if f.type not in types:
            fieldNames.append(f.name)
    return fieldNames

fc = sys.argv[1]
excludeTypes = ['Geometry', 'OID']
fields = excludeFields(fc, excludeTypes)

with arcpy.da.SearchCursor(fc, fields) as cursor:
    print cursor.fields
    for row in cursor:
        print row
del cursor

```

## 17.4 The Shape Field and Geometry Tokens


```python
fds = arcpy.ListFields('C:/gispy/data/ch17/park.shp')
[f.name for f in fds]
```


```python
[f.type for f in fds]
```


```python
data = 'C:/gispy/data/ch17/special_regions.shp'
fieldName = 'PolyArea'
expr = '!shape.area!'
arcpy.CalculateField_management(data, fieldName, expr, 'PYTHON')
```


```python
parkData = 'C:/gispy/data/ch17/parks.shp'
cursor = arcpy.da.SearchCursor (parkData,['SHAPE@AREA'])
row = cursor.next()
row[0]
```


```python
cursor = arcpy.da.SearchCursor (parkData, ['SHAPE@'])
row = cursor.next()
row[0].type
row[0].area
row[0].centroid
row[0].firstPoint
row[0].area
```


```python
cursor = arcpy.da.SearchCursor (parkData, ['SHAPE'])
row = cursor.next()
row[0].centroid
row[0]
```

## 17.5 Looping with Cursors


```python
import arcpy
fc = 'C:/gispy/data/ch17/ fires.shp'
fields = ['FireName']
cursor = arcpy.da.SearchCursor(fc, fields)
for row in cursor:
    printrow[0]
del cursor
```

## 17.6 Locking

### 17.6.1 The del Statement


```python
del cursor
```


```python
fc = 'C:/gispy/data/ch17/fires.shp'
cursor = arcpy.da.SearchCursor(fc,['FireName'])
for row in cursor:
    print row[0]
```


```python
del cursor
```


```python
cursor = arcpy.da.SearchCursor(fc, ['FireName'])
for row in cursor:
    # Try to index a second field, but there is none.
    printrow[1]
del cursor
```

### Example 17.2: Using try/except blocks with cursor looping


```python
# %load ch17/script2/searchNprint.py
# searchNprint.py
# Purpose: Print each fire name in a file.
# Usage: No script arguments needed.
import arcpy, traceback
try:
    cursor = arcpy.da.SearchCursor('C:/gispy/data/ch17/fires.shp', ['FireName'])
    for row in cursor:
        print row[0]
    del cursor
except:
    print 'An error occurred'
    traceback.print_exc()
    del cursor

```

### 17.6.2 The with Statement

```python
with arcpy_cursor_function as cursor:
    code statement(s) using the cursor
```

## 17.7 Update Cursors

### Example 17.3: Perform more than one update


```python
# %load ch17/script2/updateValues.py
# updateValues.py
# Purpose: Modify the fire type value and the fire name in each record.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys

fcOrig = sys.argv[1]
fc = 'scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)
fields = ['FireType_P', 'FireName']
cursor = arcpy.da.UpdateCursor(fc, fields)
try:
    for row in cursor:
        # Make changes to the list of values in 'row'
        row[0] = row[0] + 2      # Example: 13->15
        row[1] = row[1].title()  # Example: LITTLE CRK->Little Crk
        # Update the table (otherwise the changes won't be saved)
        cursor.updateRow(row)
        print 'Updated {0} and {1}'.format(row[0], row[1])
    del cursor
except:
    print 'An error occurred'
    traceback.print_exc()
    del cursor

```

### Example 17.4: Delete rows


```python
# %load ch17/script2/deleteRows.py
# deleteRows.py
# Purpose: Delete the first x rows.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys

fcOrig = sys.argv[1]
fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)

field = 'FID'
x = 7
try:
    cursor = arcpy.da.UpdateCursor(fc, [field])
    # Delete the first x rows.
    for row in cursor:
        if row[0] < x:
            # Delete this row.
            cursor.deleteRow()
            print 'Deleted row {0}'.format(row[0])
    del cursor
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor

```

## 17.8 Insert Cursors

### Example 17.5: Insert a row.


```python
# %load ch17/script2/insertRow.py
# insertRow.py
# Purpose: Insert a new row without geometry.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys
fcOrig = sys.argv[1]
fc = '' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)
fields = ['FireId', 'CalendarYe']
# Create an insert cursor.
try:
    cursor = arcpy.da.InsertCursor(fc, fields)
    # Create a list with FireId=513180 & CalendarYr=2009.
    newRecord = [513180, 2009]
    # Insert the row (otherwise no change would occur).
    cursor.insertRow(newRecord)
    print 'Point inserted.'
    del cursor
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor

```

### Example 17.6: Find the maximum value of an attribute and insert multiple rows using this information


```python
# %load ch17/script2/insertRows.py
# insertRows.py
# Purpose: Insert multiple rows without geometry.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, sys, traceback
fcOrig = sys.argv[1]
fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)

# Find the current fire numbers.
try:
    fields = ['FireNumber']
    cursor = arcpy.da.SearchCursor(fc, fields)
    fireNumbers = [row[0] for row in cursor]
    print '{0} fire numbers found.'.format(len(fireNumbers))
    del cursor
except:
    print 'An error occurred in the search.'
    traceback.print_exc()
    del cursor

# Insert 5 new fires for year 2015.
try:
    fields.append('CalendarYe')
    cursor = arcpy.da.InsertCursor(fc, fields)
    # Find the max value in list and increment by 1.
    fireNum = max(fireNumbers) + 1
    for i in range(5):
        # Create a row with unique fire number & year=2015.
        newRow = [fireNum, 2015]
        fireNum = fireNum + 1
        # Insert the row.
        cursor.insertRow(newRow)
        print 'New row created with fire# {0} and year = {1}.'.format(
                                newRow[0], newRow[1])
    del cursor
except:
    print 'An error occurred in the insertion.'
    traceback.print_exc()
    del cursor

```

### 17.8.1 Inserting Geometric Objects


```python
myPoint = arcpy.Point(-70.1, 42.07)
myPoint
```




    <Point (-70.1, 42.07, #, #)>



### Create 2 polyline endpoints


```python
x = 2134000
y = 179643
a = arcpy.Point(x,y)
x = 2147000
y = 163267
b = arcpy.Point(x,y)
a
```




    <Point (2134000.0, 179643.0, #, #)>




```python
b
```




    <Point (2147000.0, 163267.0, #, #)>



### Create an array with a Python list of Point objects.


```python
myArray = arcpy.Array([a,b])
```

### Create a line with an Array object that has points.


```python
line = arcpy.Polyline(myArray)
line.length
```




    20908.691398554813



### Example 17.7: Insert a point


```python
# %load ch17/script2/insertPoint.py
# insertPoint.py
# Purpose: Insert a point with a Geometry object.
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp

import arcpy, os, traceback, sys

# fcOrig = sys.argv[1]
# fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
# arcpy.Copy_management(fcOrig, fc)
fc = 'data/firesCopy.shp'

try:
    ic = arcpy.da.InsertCursor(fc, ['FireId', 'SHAPE@XY'])

    # Create a point with x = -70.1 and y = 42.07 to be used for the Shape field.
    myPoint = arcpy.Point(-70.1, 42.07)

    # Create a row list with FireId=500000 and the new point
    newRow = [500000, myPoint]

    # Insert the new row.
    ic.insertRow(newRow)
    print 'New row inserted.'

    del ic
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor

```

### Example 17.8: Insert a polygon


```python
# %load ch17/script2/insertPolygon.py
# insertPolygon.py
# Insert cursor polygon example
# Usage: Full path of file to copy and modify.
# Example input: C:/gispy/data/ch17/fires.shp
import arcpy, os, traceback, sys

# Create 3 point objects for the triangle.
a = arcpy.Point(2134000, 179643)
b = arcpy.Point(2147000, 163267)
c = arcpy.Point(2131327, 167339)

# Create an array, needed for creating a polygon.
myArray = arcpy.Array([a, b, c])

# Create a polygon.
poly = arcpy.Polygon(myArray)

fcOrig = sys.argv[1]
fc = 'C:/gispy/scratch/' + os.path.basename(fcOrig)
arcpy.Copy_management(fcOrig, fc)
try:
    # Create an insert cursor.
    cursor = arcpy.da.InsertCursor(fc, ['SHAPE@', 'Id'])

    # Create row list.
    newRow = [poly, 333]

    # Insert the new row.
    # It's automatically given an FID one greater
    # than the largest existing one.
    cursor.insertRow(newRow)
    print 'Polygon inserted.'
    del cursor
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor

```

## 17.9 Selecting Rows with SQL


```python
query1 = "SizeClass = 'A'"# Fires of size class A.
query2 = "FireName <> 'MEADOW'"# Fires not named MEADOW.
query3 = 'FID > 6'# Fires with ID greater than 6.
query4 = "StartTime = date '2000-01-06'"# After Jan.6,2000
```

### Example 17.9:Use awhere_clause with a cursor


```python
# %load ch17/script2/sqlQueryCursor.py
# sqlQueryCursor.py
# Purpose: Use a SQL query to select specific records.
# Usage: No script arguments needed.
import arcpy, traceback
fc = 'data/fires.shp'

# Create the where_clause.
query = "SizeClass = 'A'"
try:
    sc = arcpy.da.SearchCursor(fc, ['CalendarYe'], query)

    for row in sc:
        print row[0],
    del sc
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor

```

### Example 17.10: Use a cursorwhere_clause with a variable


```python
# %load ch17/script2/whereClauseWithVar.py
# whereClauseWithVar.py
# Purpose: Use a SQL query to select specific records based on user arguments.
# Example: C:/gispy/data/ch17/fires.shp FID FireName
import arcpy, sys, traceback

fc = sys.argv[1]
numericField = sys.argv[2]
fieldToPrint = sys.argv[3]

query = '{0} > 6'.format(numericField)  # String formatting.

try:
    with arcpy.da.SearchCursor(fc, [fieldToPrint], query) as cursor:
        recordList = [row[0] for row in cursor]
    del cursor

    print recordList
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor

```

## 17.10 Key Terms
* Cursor  
* Record  
* arcpy DataAccess (da)  module search, update,   and * insert cursors  
* Search and update cursornext and reset methods  
* Cursor fields property  
* Update cursorupdateRow and deleteRow methods  
* Insert cursorinsertRow method  
* arcpy geometry tokens  
* arcpy Geometry objects  
* arcpy Point, Array, Polyline, and Polygon   methods

## 17.11 Exercises


```python

```
