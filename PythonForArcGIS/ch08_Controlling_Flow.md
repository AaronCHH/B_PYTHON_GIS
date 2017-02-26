
# 8 Controlling Flow

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [8 Controlling Flow](#8-controlling-flow)
  * [8.1 Outlining Workflow](#81-outlining-workflow)
  * [8.2 Key Terms](#82-key-terms)
  * [8.3 Exercises](#83-exercises)

<!-- tocstop -->

## 8.1 Outlining Workflow

* **Example 8.1: Pseudocode for processing dredging sediment data repeats steps 3–5 for each table.**

```
GET a list of the weekly data base tables.
FOR each table in the list
    Make a spatial layer from the table.
    Clip the new layer on the disposal site extent.
    Convert clipped vector data to raster format.
ENDFOR
Find weighted sum of output rasters.
```

* **Example 8.2: Pseudocode for automatically fetching and uncompressing data files listed on a web site.**

```
GET the data center web page URL.
READ the data center web page contents.
GET a list of links to data in the page contents.
FOR each data link
    Fetch the data from the specified link.
    Save the data.
    IF the data is zip compressed THEN
        Unzip data.
        Delete zip file.
    ELSE IF the data is tar compressed THEN
        Untar data.
        Delete tar file.
    ENDIF
ENDFOR
```

* **Example 8.3: Pseudocode for preparing a table for ArcGIS import by deleting unneeded rows and columns and repairing fi eld names.**

```
FUNC preprocessTable (data table, field name row number, first
invalid column number)
    OPEN data table.
    SET row number to 1.
    WHILE row number < field name row number
        Delete row.
        INCREMENT row number.
    ENDWHILE
    SET column number to first invalid column number.
    WHILE column number <= number of columns
        Delete column.
        INCREMENT column number.
    ENDWHILE
    GET a list of field names in the table.
    FOR each field name in the list
        Replace special characters in field name with underscore.
    ENDFOR
    Save the data table.
    Close the data table.
ENDFUNC
```

* **Example 8.4: Pseudocode for preparing a set of tables for ArcGIS import; For each table, it deletes the fi rst 5 rows and the columns beyond column 50, and repairs the fi eld names.**

```
GET a list of table names.
FOR each table name in the list
    CALL preprocessTable(table name, 6, 51).
ENDFOR
```

* **Example 8.5: Pseudocode for correcting a misspelled fi eld name (vlue to value) in each of a set of tables that are distributed through a set of subdirectories.**

```
FOR each subdirectory of the current directory
    FOR each table in this subdirectory
        FOR each field in this table
            GET the field name.
            IF the field name is 'vlue' THEN
                SET field name to 'value'.
            ENDIF
        ENDFOR
    ENDFOR
ENDFOR
```

## 8.2 Key Terms
* Workflow structures: sequential steps, repetition, decision-making
* Looping
* Branching
* Pseudocode
* Block structures
* WHILE-loop
* FOR-loop
* Looping variable
* Iterate  
* Functions (procedures, subroutines)
* Nested structures

## 8.3 Exercises


```python

```
