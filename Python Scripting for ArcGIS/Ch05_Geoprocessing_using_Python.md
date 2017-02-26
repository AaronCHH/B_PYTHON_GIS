
# Chapter 5: Geoprocessing using Python

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 5: Geoprocessing using Python](#chapter-5-geoprocessing-using-python)
  * [5.1 Introduction](#51-introduction)
  * [5.2 Using the ArcPy site package](#52-using-the-arcpy-site-package)
  * [5.3 Importing ArcPy](#53-importing-arcpy)
  * [5.4 Working with earlier versions of ArcGIS](#54-working-with-earlier-versions-of-arcgis)
  * [5.5 Using tools](#55-using-tools)
  * [5.6 Working with toolboxes](#56-working-with-toolboxes)
  * [5.7 Using functions](#57-using-functions)
  * [5.8 Using classes](#58-using-classes)
  * [5.9 Using environment settings](#59-using-environment-settings)
  * [5.10 Working with tool messages](#510-working-with-tool-messages)
  * [5.11 Working with licenses](#511-working-with-licenses)
  * [5.12 Accessing ArcGIS Desktop Help](#512-accessing-arcgis-desktop-help)
  * [Points to remember](#points-to-remember)

<!-- tocstop -->

## 5.1 Introduction

## 5.2 Using the ArcPy site package

## 5.3 Importing ArcPy


```python
import arcpy
```


```python
import arcpy.mapping
```


```python
import arcpy
arcpy.env.workspace = "C:/Data"
```


```python
arcpy.<class>.<property>
```


```python
from arcpy import env
env.workspace = "C:/Data"
```


```python
from arcpy import env as myenv
myenv.workspace = "C:/Data"
```


```python
from arcpy import env as *
workspace = "C:/Data"
```

## 5.4 Working with earlier versions of ArcGIS


```python
import ArcGISscripting
gp = ArcGISscripting.create(9.3)
```


```python
import ArcGISscripting
gp = ArcGISscripting.create()
```


```python
import win32com.client
gp = win32com.client.Dispatch("esriGeoprocessing.GpDispatch.1")
```


```python
gp.workspace = "C:/Data"
```

## 5.5 Using tools

```
arcpy.<toolname_toolboxalias>(<parameters>)
```


```python
# For example, the following code runs the Clip tool:
import arcpy
arcpy.env.workspace = "C:/Data"
arcpy.Clip_analysis("streams.shp", "study.shp", "result.shp")
```

```
arcpy.<toolboxalias>.<toolname>(<parameters>)
```


```python
# Here is what the example looks like for running the Clip tool:
import arcpy
arcpy.env.workspace = "C:/Data"
arcpy.analysis.Clip("streams.shp", "study.shp", "result.shp")
```

* The Clip tool has four parameters, with the last one (cluster_tolerance) being optional.
The syntax of the Clip tool is
```
Clip_analysls(in_features, clip features, out_feature_class, {cluster tolerance})
```

* Consider, for example, the syntax of the Buffer tool:
```
Buffer_ana1ysis(in_features, out_feature_class, buffer_distance_or_field,
                {line_side}, {line_end_type} , {dissolve_option}, {dissolve_fie1d})
```

* A code example of the Buffer tool is as follows:


```python
import arcpy
arcpy.env.workspace = "C:/Data/study.gdb"
arcpy.Buffer_analysis("roads", "buffer", "100 METERS")
```


```python
arcpy.Buffer_analysis("roads", "buffer", "100 METERS", "", "", "LIST", "Code")
```


```python
arcpy.Buffer_analysis("roads", "buffer", "100 METERS", "#", "#", "LIST", "Code")
```


```python
arcpy.Buffer_analysis("roads", "buffer", "100 METERS", "", "", "LIST", "Code")
```

In the examples so far, the parameters of the tool use the actual file name (for example, "roads"). This means the file names are hard-coded. (That is, the parameters are not set as variables, but use the values directly. Although this syntax is correct and works fine, it is often more useful to make your code flexible by using variables for parameters instead of using file names. First, create a variable and assign it a value. Then you can use the variable for a parameter. These variable values are passed to the tool. For example, in the case of the Clip tool, it would look as follows:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
infc = "streams.shp"
clipfc = "study.shp"
outfc = "result.shp"
arcpy.Clip_analysis(infc, clpfc, outfc)
```

In this example script, the names of the datasets are still hard-coded in the script itself but not in the specific line of code that calls the Clip tool. The next logical step is to have the values of the variables provided by a user or another tool, which means the actual file names would no longer appear in the script. For example, the following code runs the Copy tool, and the input and output feature classes are obtained from user input using the GetParameterAsText function:


```python
import arcpy
infc = arcpy.GetParameterAsText(0)
outfc = arcpy.GetParameterAsText(1)
arcpy.Copy_management(infc, outfc)
```

ArcPy returns the output of a tool as a result ect. When the output of a tool is a new or updated feature class, the result object includes the path to the dataset. For other tools, however, the result object can consist of a string, a number, or a Boolean value. One of the advantages of result objects is that you can keep track of information about the running of tools This includes not only the output, but also messages and parameters.

* For example, in the following code, a geoprocessing tool is run and the output is returned as a result object:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
mycount_arcpy.GetCount_management("streams.shp")
print mycount
```

When the output of a tool consists of a feature class, the result object includes the path to the dataset. For example, the following code runs the Clip tool:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
mycount_arcpy.analysis.Clip("streams.shp", "study.shp", "result.shp")
print mycount
```

The output polygon feature class is returned as an object and the object is used as the input to the Get Count tool , follows:


```python
import arcpy
arcpy.env.workspace = "C:/Data/study.gdb"
buffer = arcpy.Buffer analysis ("str", "str_buf", "100_METERS")
count = arcpy.GetCount_management(buffer)
print count
```

Although many tools have only a single output, some tools have muitiple outputs. The getOutput method of the result ect can be used to obtain a specific output by using an index number. A more generic way to get a geoprocessing result follows:


```python
import arcpy
arcpy.env.workspace = "C:/Data/study.gdb"
buffer = arcpy.Buffer_ana1ysis("str", "str_buf", "100 METERS")
count = arcpy.GetCount_management(buffer).getOutput(0)
print str(count)
```

## 5.6 Working with toolboxes

When the ArcPy site package is imported into Python, all the system tool-boxes are available. When custom tools are created and stored in a custom toolbox, these tools can be accessed in Python only by importi the custom toolbox. So even if a custom toolbox has been added to Arctoolbox in ArcMap or ArcCatalog , Python is not aware of this toolbox until it has been imported. This is accomplished using the Importtoolbox function. The following code illustrates how to import a toolbox:


```python
import arcpy
arcpy.ImportToolbox("C:/Data/samp1etools.tbx")
```

* After importing a toolbox, the syntax for accessing a tool in Python is as follows:

```
arcpy.<toolname>_<toolboxalias>
```

Once the alias is set, tools in the toolbox can be accessed using Python. For example, if the sampletools.tbx file contains a tool called MyModel, the syntax to access this tool would look as follows:


```python
arcpy.MyModel_mytools(<parameters>)
```

Or alternatively:


```python
arcpy.mytools.MyModel(<parameters>)
```

Once a particular tool is identified, the tool's syntax can be accessed from Python using the Usage function. For example, the following code prints the syntax of all the tools in the Editing Tools toolbox:


```python
import arcpy
tools = arcpy.ListTools("*_analysis")
for tool in tools:
    print arcpy.Usage(tool)
```

Another way to access the syntax directly is to use Python's built-in help function. For example, the following code prints the syntax of the Clip tool:


```python
print help(arcpy.Clip_analysis)
```

## 5.7 Using functions

* The syntax of a function is the same as for tools

```py
arcpy.<functionname>(<arguments>)
```

For example, the following code determines whether a particular dataset exists, and then prints either True or False:


```python
import arcpy
print arcpy.Exists("C:/Data.streams.shp")
```

There are a large number of functions, which can be divided into the following categories:
* Cursors
* Describing data
* Environment and settings
* Fields
* Geodatabase administration
* General
* General data functions
* Getting and setting parameters
* Licensing and installation
* Listing data
* Log history
* Messaging and error handling
* Progress dialog boxes
* Raster
* Spatial reference and transformations
* Tools and toolboxes

## 5.8 Using classes

For example, workspace is a property of the
env class, so the syntax becomes env.workspace.

The syntax for setting the property of a class is
```
<classname>.<property> = <value>
```

As discussed earlier, the code to set the current workspace is as follows:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
```

Another frequently used ArcPy class is the SpatialReference class. This class has a number of properties, including the coordinate system parameters. To work with these properties, however, the class first has to be instantiated.

* The syntax for using a method to initialize a new instance of a class is
```python
arcpy.<classname>(parameters)
```

The code to initialize a new instance of the SpatialReference class is as follows:


```python
import arcpy
prjfile = "C:/Data/myprojection.prj"
spatialref = arcpy.SpatialReference(prjfile)
```

For example, the following code creates a spatial reference object based on an existing .prj file and then uses the name property to get the name of the spatial reference:


```python
import arcpy
prjfile = "C:/Data/streams.prj"
spatialref = arcpy.SpatialReference(prjfile)
myref = spatialRef.name
print myref
```

* The syntax of the Create Feature Class tool is as follows:
```py
CreateFeatureclass_management(out_path, out_name, {geometry_type}, {template}, {has_m}, {has_z}, {spatial_reference}, {config_keyword}, {spatial grid_1}, {spatial_grid_2}, {spatial_grid_3})
```

* The following code creates a spatial reference object and uses it to define the output coordinate system of a new feature class:


```python
import arcpy
out_path = "C:/Data"
out_name = "lines.shp"
prjfile = "C:/Data/streams.prj"
spatialref = arcpy.SpatialReference(prjfile)
arcpy.CreateFeatureclass_management(out_path, out_name, "POLYLINE", "", "", "", spatialref)
```

## 5.9 Using environment settings

Environment settings are exposed as properties of the env class. These properties can be used to retrieve the current values or to set them. Each property has a name and a label. The labels are displayed on the Environ ment Settings dialog box in ArcGIS, but Python works with names only. The syntax for accessing the properties from the environment class is.
```py
arcpy.env.<environmentName>
```

*  For example, to set the current workspace, the following code is used:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
```

Alternatively, environments can be accessed using the from-import statement:


```python
import arcpy
from arcpy import env
env.workspace = "C:/Data"
```

For example, cell size, compression, and mask are used for raster datasets only. The following code sets the cell size to 30:


```python
import arcpy
from arcpy import env
env.cellSize = 30
```

For example, the following code retrieves the current settings for the XY tolerance:


```python
import arcpy
from arcpy import env
print env.XYTolerance
```

To get a complete list of properties, you can use the ArcPy ListEnvironments function:


```python
import arcpy
print arcpy.ListEnvironments()
```

In ArcMap, this is not part of the Environment Settings dialog box but is a separate option on the
menu bar under **Geoprocessing > Options**.

In Python, this is a property
of the env class. The default value of this overwriteOutput property is
False. The following code sets the value to True :


```python
import arcpy
from arcpy import env
env.overwriteOutput = True
```

## 5.10 Working with tool messages

The basic syntax for retrieving messages an d printing them is
```py
print arcpy.GetMesssages()
```

* For example, when a Clip tool is run, the messages can be tri ev as follows:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
infc = "streams.shp"
clipfc = "study.shp"
outfc = "result.shp"
arcpy.Clip_analysis(infc, clipfc, outfc)
print arcpy.GetMessages()
```

Individual messages can be retrieved using the GetMessage function (note, this is different from the GetMessages function). This function has only one parameter, which is the index position of the message. For example, the foIlowing code retrieves the first message only:
```py
print arcpy.GetMessage(0)
```

The number of message from the last tool that is run can be obtained using the GetMessageCount function This function is particularly useful for retrieving just the last message. Since you typically will not know in advance how many messages may have resulted from running a tool, you can use the message count to retrieve the last message. The code to obtain the message count is
```py
arcpy.GetMessageCount()
```

To retrieve the last essage only, you would use the following:
```py
count = arcpy.GetMessageCount()
print arcpy.GetMessage(count - 1)
```

In addition to getting the number of messages, you can also query the maximum severity of the messages using the GetMaxSeverity function as follows:
```py
print arcpy.GetMaxSeverty()
```

So rather than a tool being run for output files, the result of the geoprocessing operation is returned as an object. For example:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
result = arcpy.GetCount_management("streams.shp")
```

For example, running the following code retrieves the number of messages, followed by the last message:


```python
import arcpy
arcpy.env.workspace = "C:/Data"
result = arcpy.GetCount_management("streams.shp")
count = result.messageCount
print result.getMessage(count - 1)
```

## 5.11 Working with licenses


```python

```

## 5.12 Accessing ArcGIS Desktop Help


```python

```

## Points to remember

* The ArcPy site package introduced in ArcGIS version 10 provides access to the Python geoprocessing functionality in ArcGIS. It is the successor to the ArcGISscripting module from earlier versions. ArcPy is organized in modules, functions, and classes.


* All geoprocessing tools in ArcGIS are provided as functions. Once ArcPy is imported to a Python script, you can run all the geopro cessing tools found in the standard toolboxes that are installed with ArcGIS. The syntax for running a tool is arcpy.<toolname_toolboxalias>(<parameters>). The documentation on each tool provides details on the required and optional parameters needed for a tool to run. Additional nontool functions in ArcPy are available to support geoprocessing tasks.


* Classes in ArcPy are used to create objects. Commonly used classes are the env class and the SpatialReference class. The syntax for setting the property of a class is
```py
arcpy.<classname>.<property> = <value>.
```


* Messages that result from running a tool can be retrieved using message functions, including GetMessages, GetMessage, and GetMaxSeverity. Messages can consist of information, warning, or error messages


* Several functions are available to check available licenses for products and extensions, to check out licenses, and to check licenses back in


* ArcGIS for Desktop Help contains many examples of Python code, including the Help page for individual geoprocessing tools.


```python

```
