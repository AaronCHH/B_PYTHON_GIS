
# 7 Getting User Input

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [7 Getting User Input](#7-getting-user-input)
  * [7.1 Hard-coding versus Soft-coding](#71-hard-coding-versus-soft-coding)
  * [7.2 Using GetParameterAsText](#72-using-getparameterastext)
  * [7.3 Using sys.argv](#73-using-sysargv)
  * [7.4 Missing Arguments](#74-missing-arguments)
  * [7.5 Argument Spacing](#75-argument-spacing)
  * [7.6 Handling File Names and Paths with os Module Functions](#76-handling-file-names-and-paths-with-os-module-functions)
    * [7.6.1 Getting the Script Path](#761-getting-the-script-path)
  * [7.7 Key Terms](#77-key-terms)
  * [7.8 Exercises](#78-exercises)

<!-- tocstop -->

## 7.1 Hard-coding versus Soft-coding

* **Example 7.1 boundingGeom.py**  


```python
# %load ch07/script2/boundingGeom.py
# boundingGeom.py
# Purpose: Find the minimum bounding geometry of a set of features.
# Usage: No arguments required.

import arcpy

arcpy.env.workspace = 'C:/gispy/data/ch07'
arcpy.env.overwriteOutput = True

inputFeatures = 'park.shp'
outputFeatures = 'C:/gispy/scratch/boundingBoxes.shp'

arcpy.MinimumBoundingGeometry_management(inputFeatures, outputFeatures)

```

## 7.2 Using GetParameterAsText

* **Example 7.2 boundingGeomV2.py**  


```python
# %load ch07/script2/boundingGeomV2.py
# boundingGeomV2.py (soft-coded using arcpy)
# Purpose: Find the minimum bounding geometry of a set of features.
# Usage: workspace, input_features, output_features
# Example: C:/gispy/data/ch07 park.shp C:/gispy/scratch/boundingBoxes.shp
import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)
arcpy.env.overwriteOutput = True

inputFeatures = arcpy.GetParameterAsText(1)
outputFeatures = arcpy.GetParameterAsText(2)

arcpy.MinimumBoundingGeometry_management(inputFeatures, outputFeatures)

```

## 7.3 Using sys.argv

* **Example 7.3 boundingGeomV3.py**  


```python
# %load ch07/script2/boundingGeomV3.py
# boundingGeomV3.py (soft-coded using sys)
# Purpose: Find the minimum bounding geometry of a set of features.
# Usage: workspace, input_features, output_features
# Example: C:/gispy/data/ch07 park.shp C:/gispy/scratch/boundingBoxes.shp
import arcpy, sys

arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteOutput = True

inputFeatures = sys.argv[2]
outputFeatures = sys.argv[3]

arcpy.MinimumBoundingGeometry_management(inputFeatures, outputFeatures)

```

## 7.4 Missing Arguments

## 7.5 Argument Spacing

* **Example 7.4 argSpacing.py**  


```python
# %load ch07/script2/argSpacing.py
# argSpacing.py
# Purpose: Print the number of incoming user arguments
# and the first 2 arguments.
import arcpy

numArgs = arcpy.GetArgumentCount()
print 'Number of user arguments: {0}'.format(numArgs)
print 'The first argument: {0}'.format(arcpy.GetParameterAsText(0))
print 'The second argument: {0}'.format(arcpy.GetParameterAsText(1))

```

## 7.6 Handling File Names and Paths with os Module Functions


```python
import os
inFile = 'ch07/data/park.shp'
# Get only the file name.
fileName = os.path.basename(inFile)
fileName
```




    'park.shp'




```python
# Get only the path.
filePath = os.path.dirname(inFile)
filePath
```




    'ch07/data'




```python
# Join the arguments into a valid file path.
fullPath = os.path.join(filePath, fileName)
fullPath
```




    'ch07/data\\park.shp'



* **Example 7.5 copyFile.py**  


```python
# %load ch07/script2/copyFile.py
# copyFile.py
# Purpose: Copy a file.
# Usage: source_full_path_file_name, destination_directory
# Example: C:/gispy/data/ch07/park.shp C:/gispy/scratch/

import arcpy, os

inputFile = arcpy.GetParameterAsText(0)
outputDir = arcpy.GetParameterAsText(1)

baseName = os.path.basename(inputFile)
outputFile = os.path.join(outputDir, baseName)

arcpy.Copy_management(inputFile, outputFile)

print 'inputFile =', inputFile
print 'outputDir =', outputDir
print
print 'baseName =', baseName
print 'outputFile = ', outputFile

```

* **Example 7.6  compact.py**  


```python
# %load ch07/script2/compact.py
# compact.py
# Purpose: Compact a file
# Usage: Full path file name of an mdb file.
# Example: C:/gispy/data/ch07/cities.mdb
import arcpy, os

# Get user input
fileName = arcpy.GetParameterAsText(0)
baseName = os.path.basename(fileName)

# Check size
size = os.path.getsize(fileName)
print '{0} file size before compact: {1} bytes.'.format(baseName, size)

# Compact the file
arcpy.Compact_management(fileName)

# Check size
size = os.path.getsize(fileName)
print '{0} file size AFTER compact: {1} bytes.'.format(baseName, size)

```


```python
myShapefile = 'parks.shp'
rootName = myShapefile[:-4]
rootName
```




    'parks'




```python
os.path.splitext(myShapefile)
```




    ('parks', '.shp')




```python
fc = 'farms'
os.path.splitext(fc)
```




    ('farms', '')




```python
os.path.splitext(myShapefile)[0]
```




    'parks'




```python
os.path.splitext(fc)[0]
```




    'farms'




```python
 fc[:-4]
```




    'f'



### 7.6.1 Getting the Script Path

* **Example 7.7 scriptPath.py**  


```python
# %load ch07/script2/scriptPath.py
# scriptPath.py
# Purpose: List the files in the current directory.
# Usage: No user arguments needed.

import os

# Get the script location
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)

# Print the contents of the script directory
print '{0} contains the following files:'.format(scriptDir)
print os.listdir(scriptDir)

```

## 7.7 Key Terms

```
Hard-coding vs. Soft-coding  
arcpy.GetParameterAsText(index)  
sys.argv  
os.path.dirname( fileName)  
os.path.basename( fileName)  
os.path.splitext( fileName)  
os.path.abspath(path)  
__file__  
File base name  
Full path fi le name  
```

## 7.8 Exercises


```python

```
