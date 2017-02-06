
# 5 ArcGIS and Python

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [5 ArcGIS and Python](#5-arcgis-and-python)
  * [5.1 ArcToolbox](#51-arctoolbox)
  * [5.2 ArcGIS Python Resources](#52-arcgis-python-resources)
  * [5.3 Exporting Models](#53-exporting-models)
  * [5.4 Working with GIS](#54-working-with-gis)
  * [5.5 ArcGIS + Python = arcpy](#55-arcgis-python-arcpy)
  * [5.6 arcpy Functions](#56-arcpy-functions)
  * [5.7 Environment Settings](#57-environment-settings)
  * [5.8 Key Terms](#58-key-terms)
  * [5.9 Exercises](#59-exercises)

<!-- tocstop -->


## 5.1 ArcToolbox
## 5.2 ArcGIS Python Resources
## 5.3 Exporting Models
## 5.4 Working with GIS
## 5.5 ArcGIS + Python = arcpy
## 5.6 arcpy Functions


```python
import arcpy
arcpy.CheckExtension('3D')
```




    u'Available'




```python
print arcpy.CheckExtension('3D')
```

    Available



```python
arcpy.ListPrinterNames()
```




    [u'\u50b3\u9001\u81f3 OneNote 2013',
     u'Print to Evernote',
     u'Microsoft XPS Document Writer',
     u'HP LJ300-400 color M351-M451 PCL6 Class Driver',
     u'HP LaserJet Professional P 1102w',
     u'HP LaserJet Enterprise 600 M601 M602 M603 PCL6 Class Driver',
     u'Gestetner MP 2001 PCL 6',
     u'Foxit PhantomPDF Printer',
     u'Fax',
     u'Adobe PDF']




```python
pt = arcpy.CreateObject('Point')
pt
```




    <Point (0.0, 0.0, #, #)>




```python
arcpy.Exists('ch05/data/park.shp')
```




    True



## 5.7 Environment Settings


```python
# Setting the current workspace path
arcpy.env.workspace = 'ch05/Forestry'
# Getting the current workspace path
mydir = arcpy.env.workspace
mydir
```




    u'ch05/Forestry'




```python
arcpy.env.overwriteOutput
```




    False




```python
arcpy.env.overwriteOutput = True
```


```python
arcpy.env.overwriteoutput = False
arcpy.env.overwriteOutput
```




    True



## 5.8 Key Terms


```python

```

## 5.9 Exercises


```python

```


```python

```
