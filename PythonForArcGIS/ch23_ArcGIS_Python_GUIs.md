
# 23 ArcGIS Python GUIs

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [23 ArcGIS Python GUIs](#23-arcgis-python-guis)
  * [23.1 Creating a Script Tool](#231-creating-a-script-tool)
    * [23.1.1 Printing from a Script Tool](#2311-printing-from-a-script-tool)
    * [23.1.2 Making a Script Tool Button](#2312-making-a-script-tool-button)
    * [23.1.3 Pointing to a Script](#2313-pointing-to-a-script)
  * [23.2 Creating a GUI](#232-creating-a-gui)
    * [23.2.1 Using Parameter Data Types](#2321-using-parameter-data-types)
    * [23.2.2 Using Parameter Properties](#2322-using-parameter-properties)
      * [23.2.2.1 Type](#23221-type)
      * [23.2.2.2 Direction](#23222-direction)
      * [23.2.2.3 Multivalue](#23223-multivalue)
      * [23.2.2.4 Default or Schema](#23224-default-or-schema)
      * [23.2.2.5 Environment](#23225-environment)
      * [23.2.2.6 Filter](#23226-filter)
      * [23.2.2.7 Obtained from](#23227-obtained-from)
  * [23.3 Showing](#233-showing)
  * [23.4 Validating](#234-validating)
    * [23.4.1 The ToolValidator Class](#2341-the-toolvalidator-class)
      * [23.4.1.1 Initializing Parameter Objects](#23411-initializing-parameter-objects)
      * [23.4.1.2 AnupdateMessages Example](#23412-anupdatemessages-example)
      * [23.4.1.3 AninitializeParameters Example](#23413-aninitializeparameters-example)
      * [23.4.1.4 AnupdateParameters Example](#23414-anupdateparameters-example)
  * [23.5 Python Toolboxes](#235-python-toolboxes)
    * [23.5.1 Setting Up Parameters (getParameterInfo)](#2351-setting-up-parameters-getparameterinfo)
    * [23.5.2 Checking for Licenses (isLicensed)](#2352-checking-for-licenses-islicensed)
    * [23.5.3 Validation (updateParameters and updateMessages)](#2353-validation-updateparameters-and-updatemessages)
    * [23.5.4 Running the Code (execute)](#2354-running-the-code-execute)
    * [23.5.5 Comparing Tools](#2355-comparing-tools)
  * [23.6 Discussion](#236-discussion)
  * [23.7 Key Terms](#237-key-terms)
  * [23.8 Exercises](#238-exercises)

<!-- tocstop -->

## 23.1 Creating a Script Tool

* **Example 23.1:Simple script for illustrating Script Tools textLister.py**


```python
# %load ch23/scripts2/textLister.py
# textLister.py
# Purpose: Print the text file (.txt) names in the directory.
# Usage: No arguments required.
import arcpy, os
myDir = r'..\data\smallDir'

fileList = os.listdir(myDir)
for f in fileList:
    if f.endswith(".txt"):
        print f
arcpy.AddMessage('And I like pie!')

```


```python
import arcpy
message = 'And I like pie!'
print message
arcpy.AddMessage(message)
```


```python
def printArc(message):
'''Print message for Script Tool and standard output.'''
print message
arcpy.AddMessage(message)
```


```python
print 5, 'miles'
```


```python
arcpy.AddMessage(5,'miles')
```

* **Example 23.2:Print and AddMessage print4ScriptTools.py**


```python
# %load ch23/scripts2/print4ScriptTools.py
# print4ScriptTools.py
# Purpose: Prints a directory's file count using
#          both 'print' and 'AddMessage'
# Usage: No arguments required.

import arcpy, os


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)

myDir = r'..\data\smallDir'

# Lists all the files in the directory.
fileList = os.listdir(myDir)

myMessage = 'Directory {0} contains {1} files.'.format(myDir, len(fileList))

printArc(myMessage)

```


```python

```

### 23.1.1 Printing from a Script Tool

### 23.1.2 Making a Script Tool Button

### 23.1.3 Pointing to a Script

## 23.2 Creating a GUI

* **Example 23.3 deleter.py**


```python
# %load ch23/scripts2/deleter.py
# deleter.py
# Purpose: Delete files from a workspace based on their type and name.
# Usage: workspace datatype(raster, feature class, or other) wildcard
# Sample input: C:/gispy/data/ch23/rastTester.gdb raster _out

import arcpy, os, sys


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)

arcpy.env.workspace = sys.argv[1]
fType = sys.argv[2]
wildcard = sys.argv[3]
substring = '*{0}*'.format(wildcard)

if fType == 'raster':
    data = arcpy.ListRasters(substring)
elif fType == 'feature class':
    data = arcpy.ListFeatureClasses(substring)
else:
    entireDir = os.listdir(arcpy.env.workspace)
    data = []
    for d in entireDir:
        if d.endswith(wildcard):
            data.append(d)
for d in data:
    try:
        arcpy.Delete_management(d)
        printArc('{0}/{1} deleted.'.format(arcpy.env.workspace, d))
    except arcpy.ExecuteError:
        printArc(arcpy.GetMessages())

```

### 23.2.1 Using Parameter Data Types

### 23.2.2 Using Parameter Properties

#### 23.2.2.1 Type


```python
if sys.argv[2] == '#':
    power = 1
    reportSTargs.printArc('No exponent provided. Using default power of 1.')
else:
    power = float(sys.argv[2])
```

#### 23.2.2.2 Direction


```python
arcpy.Copy_management(sys.argv[1], sys.argv[2])
```


```python
arcpy.SetParameterAsText(0, outputFile)
```

* **Example 23.4 buffer1.py**


```python
# %load ch23/scripts2/buffer1.py
# buffer1.py
# Purpose:  Buffer a file and send the result to a script tool.

import arcpy
arcpy.env.overwriteOutput = True

fileToBuffer = 'data/smallDir/randpts.shp'
distance = '500 meters'
outputFile = 'scratch/randptsBuffer.shp'

arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)

arcpy.SetParameterAsText(0, outputFile)

```


```python

```

* **Example 23.5 buffer2.py**


```python
# %load ch23/scripts2/buffer2.py
# buffer2.py
# Purpose:  Buffer an input file by an input distance
#           and send the result to a script tool.

import arcpy, os, sys
arcpy.env.overwriteOutput = True

fileToBuffer = sys.argv[1]
distance = sys.argv[2]
arcpy.env.workspace = os.path.dirname(fileToBuffer)
outputFile = 'scratch/Buff'

arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)

arcpy.SetParameterAsText(2, outputFile)

```

#### 23.2.2.3 Multivalue

* **Example 23.6 multiIn.py**


```python
# %load ch23/scripts2/multiIn.py
# multiIn.py
# Purpose: Parse a semicolon delimited input string.
import reportSTargs, sys

inputString = sys.argv[1]

reportSTargs.printArc('Input string: {0}'.format(inputString))

inputList = inputString.split(';')

for i in inputList:
    reportSTargs.printArc('Input file: {0}'.format(i))

```


```python

```

* **Example 23.7 bufferAll.py**


```python
# %load ch23/scripts2/bufferAll.py
# bufferAll.py
# Purpose: Buffer all the feature classes in an input folder by the input distance and
#          send the output file names to script tool.
# Arguments: working_directory linear_unit
# Sample input: C:/gispy/data/ch23/smallDir "0.2 miles"

import arcpy, reportSTargs, sys

arcpy.env.overwriteOutput = True
arcpy.env.workspace = sys.argv[1]
distance = sys.argv[2]

fcs = arcpy.ListFeatureClasses()
outList = []
for fc in fcs:
    reportSTargs.printArc('Processing: {0}'.format(fc))
    outputFile = 'C:/gispy/scratch/' + fc[:-4] + 'Out.shp'
    try:
        arcpy.Buffer_analysis(fc, outputFile, distance)
        reportSTargs.printArc('Created {0}'.format(outputFile))
        outList.append(outputFile)
    except arcpy.ExecuteError:
        reportSTargs.printArc(arcpy.GetMessages())

results = ";".join(outList)

reportSTargs.printArc(results)

arcpy.SetParameterAsText(2, results)

```

#### 23.2.2.4 Default or Schema

* **Example 23.8 getFeatures.py**


```python
# %load ch23/scripts2/getFeatures.py
# getFeatures.py
# Purpose: Copy the digitized feature set input into a shapefile
#          and send this to the script tool as output.

import arcpy, sys
arcpy.env.overwriteOutput = True
fs = sys.argv[1]
outputFeat = 'C:/gispy/scratch/getFeaturesOutput.shp'
arcpy.CopyFeatures_management(fs, outputFeat)
arcpy.SetParameterAsText(1, outputFeat)

```

#### 23.2.2.5 Environment

#### 23.2.2.6 Filter

* **Example 23.9 regional.py**


```python
# %load ch23/scripts2/regional.py
# regional.py
# Purpose: Print the names of states in the input region.
# Usage: region
# Example input: Mountain

import arcpy, reportSTargs, sys

region = sys.argv[1]

inf = 'C:/gispy/data/ch23/USA/USA_States_Generalized.shp'

fields = ['SUB_REGION', 'STATE_NAME']

sc = arcpy.da.SearchCursor(inf, fields)

reportSTargs.printArc('\n--States in {0}--'.format(region))

for row in sc:
    if row[0] == region:
        reportSTargs.printArc(row[1])

reportSTargs.printArc('\n')
del sc

```

#### 23.2.2.7 Obtained from

* **Example 23.10 combineFields.py**


```python
# %load ch23/scripts2/combineFields.py
# combineFields.py
# Purpose: Create a new field that is the sum of two existing fields.
import arcpy, sys

dataset = sys.argv[1]
field1 = sys.argv[2]
field2 = sys.argv[3]
newfield = sys.argv[4]

arcpy.AddField_management(dataset, newfield)
expression = '!{0}!+!{1}!'.format(field1, field2)
arcpy.CalculateField_management(dataset, newfield, expression, 'PYTHON')

arcpy.SetParameterAsText(4, dataset)

```

* **Example 23.11 feature2point.py**


```python
# %load ch23/scripts2/feature2point.py
# feature2point.py
# Purpose: Find the centroids of the input polygons.

import arcpy, sys

arcpy.env.overwriteOutput = True
inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Find points based on the input.
arcpy.FeatureToPoint_management(inputFile, outputFile)

# Return the results to the tool.
arcpy.SetParameterAsText(1, outputFile)



```


```python

```

## 23.3 Showing

* **Example 23.12 Excerpt from defaultProgressor.py**


```python
# %load ch23/scripts2/defaultProgressor.py
# defaultProgressor.py
# Purpose: Delete files from a workspace based on their type and name and
#          use the default progressor to show progress.
# Arguments: workspace datatype(raster, feature class, or other) wildcard
# Sample input: C:/gispy/data/ch23/rastTester.gdb raster _out

import arcpy, os, sys, time


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)

arcpy.env.workspace = sys.argv[1]
fType = sys.argv[2]
wildcard = sys.argv[3]
substring = '*{0}*'.format(wildcard)

if fType == 'raster':
    data = arcpy.ListRasters(substring)
elif fType == 'feature class':
    data = arcpy.ListFeatureClasses(substring)
else:
    entireDir = os.listdir(arcpy.env.workspace)
    data = []
    for d in entireDir:
        if d.endswith(wildcard):
            data.append(d)

message = "Delete '{0}' files from {1}".format(wildcard, arcpy.env.workspace)
arcpy.SetProgressor('default', message)
time.sleep(1)
printArc(message)
for d in data:
    try:
        arcpy.SetProgressorLabel('Deleting {0}'.format(d))
        arcpy.Delete_management(d)
        printArc('{0}/{1} deleted'.format(arcpy.env.workspace, d))
        time.sleep(3)
    except arcpy.ExecuteError:
        printArc(arcpy.GetMessages())

```

* **Example 23.13 Excerpt from stepProgressor.py**


```python
# %load ch23/scripts2/stepProgressor.py
# stepProgressor.py
# Purpose: Delete files from a workspace based on their type and name and
#          use the step progressor to show progress.
# Arguments: workspace datatype(raster, feature class, or other) wildcard
# Sample input: C:/gispy/data/ch23/rastTester.gdb raster _out

import arcpy, os, sys, time


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)

arcpy.env.workspace = sys.argv[1]
fType = sys.argv[2]
wildcard = sys.argv[3]
substring = '*{0}*'.format(wildcard)

if fType == 'raster':
    data = arcpy.ListRasters(substring)
elif fType == 'feature class':
    data = arcpy.ListFeatureClasses(substring)
else:
    entireDir = os.listdir(arcpy.env.workspace)
    data = []
    for d in entireDir:
        if d.endswith(wildcard):
            data.append(d)

# Initialize progressor.
message = "Preparing to delete '{0}' files from {1}".format(wildcard, arcpy.env.workspace)
arcpy.SetProgressor('step', message, 0, len(data))
time.sleep(3)
printArc(message)
for d in data:
    try:
        # Update progress label
        arcpy.SetProgressorLabel('Deleting {0}'.format(d))
        arcpy.Delete_management(d)
        printArc('{0}/{1} deleted'.format(arcpy.env.workspace, d))
        time.sleep(3)
    except arcpy.ExecuteError:
        printArc(arcpy.GetMessages())
    # Update progress bar percent.
    arcpy.SetProgressorPosition()

```


```python

```

## 23.4 Validating

* **Example 23.14:ToolValidator code from Script Tool, '01_favorites_um', in validatorExamples.tbx**


```python
# Setting an error message
def updateMessages(self):
    """Modify the messages created by internal validation for
    each tool parameter. This method is called after
    internal validation."""
    if self.params[0].altered:
        ifself.params[0].value <= 0:
            self.params[0].setErrorMessage("Please specify \
                                           a positive number.")
return
```


```python

```

### 23.4.1 The ToolValidator Class

* **Example 23.15**


```python
class ToolValidator(object):
    """Class for validating a tool's parameter values and
    controlling the behavior of the tool's dialog."""
    def __init__(self):
        """Setup arcpy and the list of tool parameters."""
        self.params = arcpy.GetParameterInfo()
    def initializeParameters(self):
        """Re fine the properties of a tool's parameters. This method is
        called when the tool is opened."""
        return
    def updateParameters(self):
        """Modify the values and properties of parameters before
        internal validation is performed. This method is called
        whenever a parameter has been changed."""
        return
    def updateMessages(self):
        """Modify the messages created by internal validation
        for each tool parameter. This method is called after
        internal validation."""
        return
```

#### 23.4.1.1 Initializing Parameter Objects


```python
def __init__ (self):
    self.params = arcpy.GetParameterInfo()
```

#### 23.4.1.2 AnupdateMessages Example


```python
if self.params[0].altered:
```


```python
if self.params[0].value <= 0:
```


```python
if self.params[0].altered:
    if self.params[0].value <= 0:
        self.params[0].setErrorMessage('Please specify a positive number.')
```

#### 23.4.1.3 AninitializeParameters Example

*#** Example 23.16:Code in the 'validatorExamples.tbx/02_categories_ip'ToolValidator**


```python
def initializeParameters(self):
    """Assign parameter categories."""
    numParams = len(self.params)
    for index in range(numParams):
        if index < numParams/3.0:
            self.params[index].category = 'A. Really important!'
        elif index < (2*numParams)/3.0:
            self.params[index].category = 'B. If you have time.'
        else:
            self.params[index].category = "C. Meh. Don't bother."
    return
```

#### 23.4.1.4 AnupdateParameters Example

*#** Example 23.17:ToolValidator code from Script Tool, 'validatorExamples.tbx 03_rasters_up'.**


```python
defupdateParameters(self):
    '''Initialize raster list.'''
    if self.params[0].altered:
        arcpy.env.workspace = self.params[0].value
        rasts = arcpy.ListRasters()
        if rasts:
            self.params[1]. filter.list = rasts
        else:
            self.params[1]. filter.list = []
    return

def updateMessages(self):
    '''Check for rasters.'''
    if self.params[0].altered:
        if not self.params[1].filter.list:
            self.params[0].setErrorMessage('This directory does not contain any rasters.')
    return
```


```python

```

## 23.5 Python Toolboxes

* **Example 23.18:Python toolbox template**


```python
import arcpy

class Toolbox(object):
    def__init__(self):
        '''De fine the toolbox (name of the toolbox is the
        name of the '.pyt' file).'''
        self.label = 'Toolbox'
        self.alias = ''
        # List of tool classes associated with this toolbox
        self.tools = [Tool]

class Tool(object):
    def__init__(self):
    '''De fine the tool (tool name is the name of the class).'''
    self.label = 'Tool'
    self.description = ''
    self.canRunInBackground = False

    def getParameterInfo(self):
        '''De fine parameter de finitions'''
        params = None
    return params

    def isLicensed(self):
        '''Set whether tool is licensed to execute.'''
    return True

    def updateParameters(self, parameters):
        '''Modify parameters before internal validation. Called
        whenever a parameter has been changed.'''
    return

    def updateMessages(self, parameters):
        '''Modify messages created by internal validation. Called
        after internal validation.'''
    return

    def execute(self, parameters, messages):
        '''The source code of the tool.'''
    return
```

### 23.5.1 Setting Up Parameters (getParameterInfo)


```python
myParam = arcpy.Parameter()
```


```python
myParam.name = 'My_precious'
```


```python
return[param1, param2]
```

* **Example 23.19**


```python
def getParameterInfo(self):
    '''Set up the parameters and return
    the list of Parameter objects.'''
    # 1_Select_a_workspace_containing_rasters
    param1 = arcpy.Parameter()
    param1.name = '1_Select_a_workspace_containing_rasters'
    param1.displayName = '1. Select a workspace containing rasters:'
    param1.parameterType = 'Required'
    param1.direction = 'Input'
    param1.datatype = 'Workspace'
    param1. filter.list = ["Local Database"]
    # 2_Select_rasters_within_the_workspace
    param2 = arcpy.Parameter()
    param2.name = '2_Select_rasters_within_the_workspace'
    param2.displayName = '2. Select rasters within the workspace:'
    param2.parameterType = 'Required'
    param2.direction = 'Input'
    param2.datatype = 'String'
    param2.multiValue = True
    param2.filter.list = []
    return[param1, param2]
```

### 23.5.2 Checking for Licenses (isLicensed)

* **Example 23.20**


```python
def isLicensed(self):
    """Prevent the tool from running if the Spatial Analyst extension
    is not available."""
    if arcpy.CheckExtension('Spatial') == 'Available':
        returnTrue# tool can be executed
    else:
        return False# tool can not be executed
```

### 23.5.3 Validation (updateParameters and updateMessages)

* **Example 23.21**


```python
def updateParameters(self, parameters):
    '''Initialize raster list.'''
    if parameters[0].altered:
        arcpy.env.workspace = parameters[0].value
        rasts = arcpy.ListRasters()
    if rasts:
        parameters[1].filter.list = rasts
    else:
        parameters[1].filter.list = []
    return

def updateMessages(self, parameters):
    '''Check for rasters.'''
    if parameters[0].altered:
        if not parameters[1]. filter.list:
            parameters[0].setErrorMessage('This directory does not contain any rasters.')
    return
```

### 23.5.4 Running the Code (execute)

* **Example 23.22**


```python
def execute(self, parameters, messages):
    '''Calculate the Sine of each input raster.'''
    arcpy.CheckOutExtension('Spatial')
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = parameters[0].value# Set the workspace
    forrast in parameters[1].values:
    try:
        outSin = arcpy.sa.Sin(rast)
        outSin.save(rast + '_Sin')
        message = '{0}_Sin created in {1}.'.format(rast,
        arcpy.env.workspace)
        arcpy.AddMessage(message)
    except:
        message = '{0}_Sin could not be created.'.format(rast)
        arcpy.AddMessage(message)
```


```python
def execute(self, parameters, messages):
    '''Calculate the Sine of each input raster.'''
    import rastModule
    wkspace = parameters[0].value
    rasters = parameters[1].values
    rastModule.batchSine(wkspace, rasters)
```

* **Example 23.23 rastModule.py**


```python
# rastModule.py
import arcpy
def batchSine(workspace, rastList):
    '''Calculate the Sine of each raster in the list.'''
    arcpy.CheckOutExtension('Spatial')
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = workspace# Set the workspace
    for rast in rastList:
        try:
            outSin = arcpy.sa.Sin(rast)
            outSin.save(rast+'_Sin')
            message = '{0}_Sin created in {1}.'.format(rast,
            arcpy.env.workspace)
            arcpy.AddMessage(message)
        except:
            message = '{0}_Sin could not be created.'.format(rast)
            arcpy.AddMessage(message)
```

### 23.5.5 Comparing Tools

* **Example 23.24**


```python
def execute(self, parameters, messages):
    # From combineFields.py
    # Purpose: Create a new field that is the sum
    # of two existing fields.
    dataset = parameters[0].value.value
    field1 = parameters[1].value
    field2 = parameters[2].value
    new field = parameters[3].value
    arcpy.AddField_management(dataset, new field)
    expression = '!{0}!+!{1}!'.format( field1, field2)
    arcpy.CalculateField_management(dataset, new field,
    expression, 'PYTHON')
    arcpy.SetParameterAsText(4,dataset)
```

* **Example 23.25:TheparametersDependencies Parameter property is equivalent to the 'Obtained from' Script Tool property**


```python
def getParameterInfo(self):
    '''Create parameters and set their properties'''
    # Input_ file
    param1 = arcpy.Parameter()
    param1.name = 'Input_ file'
    param1.displayName = 'Input file'
    param1.parameterType = 'Required'
    param1.direction = 'Input'
    param1.datatype = 'Feature Class'
    # Field1
    param2 = arcpy.Parameter()
    param2.name = 'Field1'
    param2.displayName = 'Field 1'
    param2.parameterType = 'Required'
    param2.direction = 'Input'
    param2.datatype = 'Field'
    param2.parameterDependencies = [param1.name]
```

* **Example 23.26**


```python

```


```python
def getAbsPath(relativePath):
    '''Return the absolute path given a relative path to this file'''
    tbxPath = os.path.abspath( file
    tbxDir = os.path.dirname(tbxPath)
    fullPath = os.path.join(tbxDir, relativePath)
    returnos.path.abspath(fullPath)
```


```python

```

## 23.6 Discussion

## 23.7 Key Terms
* Script Tool  
* Geoprocessing Window  
* Widget  
* Combo box  
* ToolValidator class  
* Validation  
* Internal validation  
* Python toolbox  
* Parameter object  
* Value object  

## 23.8 Exercises
