# 2 Beginning Python

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [2 Beginning Python](#2-beginning-python)
  * [2.1 Where to Write Code](#21-where-to-write-code)
  * [2.2 How to Run Code in PythonWin and PyScripter](#22-how-to-run-code-in-pythonwin-and-pyscripter)
  * [2.3 How to Pass Input to a Script](#23-how-to-pass-input-to-a-script)
  * [2.4 Python Components](#24-python-components)
    * [2.4.1 Comments](#241-comments)
    * [2.4.2 Keywords](#242-keywords)
    * [2.4.3 Indentation](#243-indentation)
    * [2.4.4 Built-in Functions](#244-built-in-functions)
    * [2.4.5 Variables, Assignment Statements, and Dynamic](#245-variables-assignment-statements-and-dynamic)
    * [2.4.6 Variables Names and Tracebacks](#246-variables-names-and-tracebacks)
    * [2.4.7 Built-in Constants and Exceptions](#247-built-in-constants-and-exceptions)
    * [2.4.8 Standard (Built-in) Modules](#248-standard-built-in-modules)
  * [2.5 Key Terms](#25-key-terms)
  * [2.6 Exercises](#26-exercises)

<!-- tocstop -->


## 2.1 Where to Write Code
## 2.2 How to Run Code in PythonWin and PyScripter
## 2.3 How to Pass Input to a Script

* **ch02/add_version1.py**  

```python
import os, sys
```

```python
# %load ch02/add_version1.py
# add_version1.py adds two numbers.
a = 2
b = 3
c = a + b
# format(c) substitutes the value of c for {0} in the print statement.
print 'The sum is {0}.'.format(c)

```


```python
%run ch02/add_version1.py
```

    The sum is 5.


## 2.4 Python Components

* **ch02/add_version2.py**  


```python
# %load ch02/add_version2.py
# add_version2.py adds two numbers given as arguments.

import sys  # Now the script can use the built-in Python system module.

# sys.argv is the system argument vector.
# int changes the input to an integer number.
a = int(sys.argv[1])
b = int(sys.argv[2])

c = a + b
# format(c) substitutes the value of c for {0} in the print statement.
print 'The sum is {0}.'.format(c)

```


```python
%run ch02/add_version2.py 3 5
```

    The sum is 8.


* **ch02/describe_fc.py**  


```python
# %load ch02/describe_fc.py
# describe_fc.py
# Purpose: Print information about each feature class in a workspace.
# Usage: Workspace
# Example input: C:/gispy/data/ch02
# Output: A list of basic information about each feature class.
# Author: Lou Lou Who 7/20/2055

import arcpy, sys

# GET the input workspace from the user.
arcpy.env.workspace = sys.argv[1]

# GET a list of the feature classes in the workspace.
fcs = arcpy.ListFeatureClasses()

# PRINT basic information about each feature class in the folder.
print 'Feature classes in folder {0}:'.format(arcpy.env.workspace)
for fc in fcs:
    desc = arcpy.Describe(fc)
    print 'Name:        {0}'.format(fc)
    print 'Data type:   {0}'.format(desc.dataType)
    print 'Data class:  {0}'.format(desc.dataSetType)
    print 'Type:        {0}'.format(desc.featureType)
    print 'Shape type:  {0}'.format(desc.shapeType)
    print 'Has M:       {0}'.format(desc.hasM)
    print 'Has Z:       {0}'.format(desc.hasZ)
    print
print 'Feature class list complete.'

```


```python
%run ch02/describe_fc.py ch02/data/
```

    Feature classes in folder ch02/data:
    Name:        fires.shp
    Data type:   ShapeFile
    Data class:  FeatureClass
    Type:        Simple
    Shape type:  Point
    Has M:       False
    Has Z:       False

    Name:        park.shp
    Data type:   ShapeFile
    Data class:  FeatureClass
    Type:        Simple
    Shape type:  Polygon
    Has M:       False
    Has Z:       False

    Feature class list complete.


### 2.4.1 Comments
### 2.4.2 Keywords
### 2.4.3 Indentation
### 2.4.4 Built-in Functions
### 2.4.5 Variables, Assignment Statements, and Dynamic


```python
FID = 145
```


```python
inputData='trees.shp'
inputData
```




    'trees.shp'




```python
type(FID)
```




    int




```python
 type(inputData)
```




    str




```python
avg = 92
type(avg)
```




    int




```python
avg = 'A'
type(avg)
```




    str



### 2.4.6 Variables Names and Tracebacks

### 2.4.7 Built-in Constants and Exceptions


```python
type(True)
```




    bool




```python
True
```




    True




```python
import arcpy
arcpy.env.overwriteOutput=True
```


```python
 dir(__builtins__)
```




    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BaseException',
     'BufferError',
     'BytesWarning',
     'DeprecationWarning',
     'EOFError',
     'Ellipsis',
     'EnvironmentError',
     'Exception',
     'False',
     'FloatingPointError',
     'FutureWarning',
     'GeneratorExit',
     'IOError',
     'ImportError',
     'ImportWarning',
     'IndentationError',
     'IndexError',
     'KeyError',
     'KeyboardInterrupt',
     'LookupError',
     'MemoryError',
     'NameError',
     'None',
     'NotImplemented',
     'NotImplementedError',
     'OSError',
     'OverflowError',
     'PendingDeprecationWarning',
     'ReferenceError',
     'RuntimeError',
     'RuntimeWarning',
     'StandardError',
     'StopIteration',
     'SyntaxError',
     'SyntaxWarning',
     'SystemError',
     'SystemExit',
     'TabError',
     'True',
     'TypeError',
     'UnboundLocalError',
     'UnicodeDecodeError',
     'UnicodeEncodeError',
     'UnicodeError',
     'UnicodeTranslateError',
     'UnicodeWarning',
     'UserWarning',
     'ValueError',
     'Warning',
     'WindowsError',
     'ZeroDivisionError',
     '__IPYTHON__',
     '__debug__',
     '__doc__',
     '__import__',
     '__name__',
     '__package__',
     'abs',
     'all',
     'any',
     'apply',
     'basestring',
     'bin',
     'bool',
     'buffer',
     'bytearray',
     'bytes',
     'callable',
     'chr',
     'classmethod',
     'cmp',
     'coerce',
     'compile',
     'complex',
     'copyright',
     'credits',
     'delattr',
     'dict',
     'dir',
     'divmod',
     'dreload',
     'enumerate',
     'eval',
     'execfile',
     'file',
     'filter',
     'float',
     'format',
     'frozenset',
     'get_ipython',
     'getattr',
     'globals',
     'hasattr',
     'hash',
     'help',
     'hex',
     'id',
     'input',
     'int',
     'intern',
     'isinstance',
     'issubclass',
     'iter',
     'len',
     'license',
     'list',
     'locals',
     'long',
     'map',
     'max',
     'memoryview',
     'min',
     'next',
     'object',
     'oct',
     'open',
     'ord',
     'pow',
     'print',
     'property',
     'range',
     'raw_input',
     'reduce',
     'reload',
     'repr',
     'reversed',
     'round',
     'set',
     'setattr',
     'slice',
     'sorted',
     'staticmethod',
     'str',
     'sum',
     'super',
     'tuple',
     'type',
     'unichr',
     'unicode',
     'vars',
     'xrange',
     'zip']



### 2.4.8 Standard (Built-in) Modules


```python
import math
math.radians(180)
```




    3.141592653589793




```python
import sys
sys.path
```




    ['',
     'C:\\Windows\\SYSTEM32\\python27.zip',
     'c:\\python27\\arcgis10.1\\DLLs',
     'c:\\python27\\arcgis10.1\\lib',
     'c:\\python27\\arcgis10.1\\lib\\plat-win',
     'c:\\python27\\arcgis10.1\\lib\\lib-tk',
     'c:\\python27\\arcgis10.1',
     'c:\\python27\\arcgis10.1\\lib\\site-packages',
     'C:\\Program Files (x86)\\ESRI\\WaterUtils\\ArcHydro\\bin',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\bin',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\arcpy',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\ArcToolbox\\Scripts',
     'c:\\python27\\arcgis10.1\\lib\\site-packages\\IPython\\extensions',
     'C:\\Users\\AaronHsu\\.ipython']




```python
sys.argv[0]
```




    'c:\\python27\\arcgis10.1\\lib\\site-packages\\ipykernel\\__main__.py'




```python
import os
os.listdir('ch02/data')
```




    ['fires.dbf',
     'fires.prj',
     'fires.sbn',
     'fires.sbx',
     'fires.shp',
     'fires.shp.xml',
     'fires.shx',
     'park.dbf',
     'park.prj',
     'park.sbn',
     'park.sbx',
     'park.shp',
     'park.shp.xml',
     'park.shx']




```python

```

## 2.5 Key Terms

## 2.6 Exercises


```python

```
