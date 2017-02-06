# 1 Introduction

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [1 Introduction](#1-introduction)
  * [1.1 Python and GIS](#11-python-and-gis)
  * [1.2 Sample Data and Scripts](#12-sample-data-and-scripts)
  * [1.3 GIS Data Formats](#13-gis-data-formats)
    * [1.3.1 GRID](#131-grid)
    * [1.3.2 Shapefile](#132-shapefile)
    * [1.3.3 dBASE Files](#133-dbase-files)
    * [1.3.4 Layer Files](#134-layer-files)
    * [1.3.5 Geodatabase](#135-geodatabase)
  * [1.4 An Introductory Example](#14-an-introductory-example)
  * [1.5 Organization of This Book](#15-organization-of-this-book)
  * [1.6 Key Terms](#16-key-terms)

<!-- tocstop -->

## 1.1 Python and GIS

## 1.2 Sample Data and Scripts
## 1.3 GIS Data Formats
### 1.3.1 GRID
### 1.3.2 Shapefile
### 1.3.3 dBASE Files
### 1.3.4 Layer Files
### 1.3.5 Geodatabase
## 1.4 An Introductory Example

* **simpleBuffer_1.py**  


```python
# %load simpleBuffer_1.py
# simpleBuffer.py
import arcpy
from arcpy import env
env.overwriteOutput = True

# Buffer park.shp by 0.25 miles around each feature exterior.
# Buffers ends are rounded & all buffers are dissolved into a single feature.
arcpy.Buffer_analysis('./ch01/data/park.shp',
                      './ch01/scratch/parkBuffer.shp',
                      '0.25 miles', 'OUTSIDE_ONLY', 'ROUND', 'ALL')
```




    <Result '.\\ch01\\scratch\\parkBuffer.shp'>



## 1.5 Organization of This Book
## 1.6 Key Terms


```python

```
