
# 6 Calling Tools with Arcpy

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [6 Calling Tools with Arcpy](#6-calling-tools-with-arcpy)
  * [6.1 Calling Tools](#61-calling-tools)
  * [6.2 Help Resources](#62-help-resources)
    * [6.2.1 Tool Help](#621-tool-help)
    * [6.2.2 Code Snippets](#622-code-snippets)
  * [6.3 Tool Parameters](#63-tool-parameters)
    * [6.3.1 Linear Units](#631-linear-units)
    * [6.3.2 Python Expressions as Input](#632-python-expressions-as-input)
    * [6.3.3 Multivalue Inputs](#633-multivalue-inputs)
    * [6.3.4 Optional Parameters](#634-optional-parameters)
  * [6.4 Return Values and Result Objects](#64-return-values-and-result-objects)
  * [6.5 Spatial Analyst Toolbox](#65-spatial-analyst-toolbox)
    * [6.5.1 Calling Spatial Analyst tools](#651-calling-spatial-analyst-tools)
    * [6.5.2 Importing spatial analyst](#652-importing-spatial-analyst)
    * [6.5.3 Raster Calculator](#653-raster-calculator)
  * [6.6 Temporary Feature Layers](#66-temporary-feature-layers)
  * [6.7 Using Variables for Multiple Tool Calls](#67-using-variables-for-multiple-tool-calls)
  * [Example 6.4 addLengthField.py](#example-64-addlengthfieldpy)
  * [6.8 Calling Custom Tools](#68-calling-custom-tools)
  * [6.9 A Word About Old Scripts](#69-a-word-about-old-scripts)
  * [6.10 Discussion](#610-discussion)
  * [6.11 Key Terms](#611-key-terms)
  * [6.12 Exercises](#612-exercises)

<!-- tocstop -->


## 6.1 Calling Tools


```python
import os, sys, arcpy
arcpy.env.overwriteOutput = True
```


```python
arcpy.env.workspace = 'ch06/data'
inputRaster = 'getty_rast'
outputFile = 'output.txt'
arcpy.RasterToASCII_conversion(inputRaster, outputFile)
```


```python
arcpy.env.overwriteOutput = True
arcpy.Buffer_analysis('ch06/data/park.shp',
                      'parkBuffer.shp','0.25 miles')
```


```python
arcpy.env.workspace = 'ch06/data/'
arcpy.Buffer_analysis('park.shp',
                      'ch06/scratch/parkBuffer.shp',
                      '0.25 miles')
```

## 6.2 Help Resources

### 6.2.1 Tool Help

### 6.2.2 Code Snippets

## 6.3 Tool Parameters

### 6.3.1 Linear Units
### 6.3.2 Python Expressions as Input


```python
data = 'ch06/data/data1.shp'
fieldName = 'result'
expr = 5
arcpy.CalculateField_management(data, fieldName, expr, 'PYTHON')
```


```python
expr = '2*!measure! - !coverage!'
arcpy.CalculateField_management(data, fieldName, expr,'PYTHON')
```


```python
data = 'ch06/data/special_regions.shp'
fieldName = 'PolyArea'
expr = '!shape.area!'
arcpy.CalculateField_management(data, fieldName, expr,'PYTHON')
```

### 6.3.3 Multivalue Inputs


```python
arcpy.env.workspace = 'ch06/data/'
inputFiles = ['park.shp', 'special_regions.shp', 'workzones.shp']
arcpy.Merge_management(inputFiles, 'mergedData.shp')
```


```python
inputFiles = 'park.shp;special_regions.shp;workzones.shp'
arcpy.Merge_management(inputFiles, 'mergedData2.shp')
```


```python
vt = arcpy.ValueTable()
vt.addRow('park.shp')
vt.addRow('special_regions.shp')
vt.addRow('workzones.shp')
arcpy.Merge_management(vt, 'mergedData3.shp')
```


```python
inputFiles = [['park.shp', 2], ['special_regions.shp', 2],
              ['workzones.shp',1]]
arcpy.Intersect_analysis(inputFiles, 'intersectData.shp')
```


```python
arcpy.env.workspace = "ch06/data/"
vt = arcpy.ValueTable()
vt.addRow('park.shp 2')
vt.addRow('special_regions.shp 2')
vt.addRow('workzones.shp 1')
arcpy.Intersect_analysis(vt, 'intersectData.shp')
```

### 6.3.4 Optional Parameters


```python
arcpy.env.workspace = 'ch06/data'
arcpy.env.overwriteOutput = True
# Use default values for the last 6 args.
arcpy.PolygonNeighbors_analysis('park.shp', 'PN.dbf')
# Another way to use default values for the last 6 args.
arcpy.PolygonNeighbors_analysis('park.shp', 'PN.dbf', '#','#','#', '#','#', '#')
```


```python
# Use default values for the last 5 parameters.
arcpy.PolygonNeighbors_analysis('park.shp', 'PN.dbf', 'COVER')
```


```python
# Use default value for in_fields,but set the value for area_overlap.
arcpy.PolygonNeighbors_analysis('park.shp','PN.dbf','#', 'AREA_OVERLAP')
```

## 6.4 Return Values and Result Objects


```python
pnResult = arcpy.PolygonNeighbors_analysis('park.shp', 'PN.dbf')
```


```python
type(pnResult)
```


```python
print pnResult
```


```python
pnResult.outputCount
```


```python
pnResult.getOutput(0)
```


```python
res = arcpy.Buffer_analysis('park.shp', 'outBuff.shp', '4 miles')
print res
```


```python
resGC = arcpy.GetCount_management('park.shp')
print resGC
```


```python
resGC + 25
```


```python
count = resGC.getOutput(0)
count
```


```python
count + 25
```


```python
int(count) + 25
```

* **Example 6.1 avgNearNeighbor.py**  


```python
# %load ch06/script2/avgNearNeighbor.py
# Name: avgNearNeighbor.py
# Purpose: Analyze crime data to determine if spatial patterns are
#         statistically significant.

import arcpy

arcpy.env.workspace = 'ch06/data'

annResult = arcpy.AverageNearestNeighbor_stats('points.shp', 'Euclidean Distance')

print 'Average Nearest Neighbor Output'
print 'Nearest neighbor ratio: {0}'.format(annResult.getOutput(0))
print 'z-score: {0}'.format(annResult.getOutput(1))
print 'p-value: {0}'.format(annResult.getOutput(2))
print 'Expected Mean Distance: {0}'.format(annResult.getOutput(3))
print 'Observed Mean Distance: {0}'.format(annResult.getOutput(4))

```


```python
%run ch06/script2/avgNearNeighbor.py
```

## 6.5 Spatial Analyst Toolbox

### 6.5.1 Calling Spatial Analyst tools


```python
import arcpy
arcpy.env.workspace = 'ch06/data'
arcpy.env.overwriteOutput = True
inRast = 'getty_rast'
arcpy.CheckOutExtension('Spatial')
outputRast = arcpy.sa.SquareRoot(inRast)
```


```python
outputRast
```


```python
outputRast.save()
outputRast
```


```python
outputRast.save('gettySqRoot')
```


```python
outputRast.save('gettySquareRoot')
```

### 6.5.2 Importing spatial analyst


```python
from arcpy.sa import *
```


```python
outputRast = arcpy.sa.SquareRoot(inRast)
```


```python
outputRast = SquareRoot(inRast)
```


```python
outputRast = Int(inRast)
```


```python
outputNum = int(myNum)
```

### 6.5.3 Raster Calculator

* **Example 6.2 computeRastEquation.py**  


```python
# %load ch06/script2/computeRastEquation.py
# computeRastEquation.py
# Purpose: Calculate 5 * 'getty_rast' - 2

import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'ch06/data/rastSmall.gdb'
arcpy.CheckOutExtension('Spatial')

outRast1 = arcpy.sa.Times(5, 'dataRast')
outRast2 = arcpy.sa.Minus(outRast1, 2)
outRast2.save('equationRast')

print 'Output raster written in {0}'.format(arcpy.env.workspace)
del outRast1, outRast2

```


```python
%run ch06/script2/computeRastEquation.py
```


```python
rastObj = arcpy.Raster('dataRast')
outRast = 5*rastObj - 2
outRast.save('equationRast2')
del outRast
```


```python
r1 = arcpy.Raster('out1')
r2 = arcpy.Raster('out2')
r3 = arcpy.Raster('out3')
outRast = (5*r1*r2*r3)/2
outRast.save('output')
del outRast
```

## 6.6 Temporary Feature Layers


```python
import arcpy, os
arcpy.env.overwriteOutput = True
myData = './ch06/data/xyData.csv' # xyData.txt doesn't work (why?)
arcpy.MakeXYEventLayer_management(myData, 'x', 'y', 'tmpLayer')
```




    <Result 'tmpLayer'>




```python
countRes = arcpy.GetCount_management('tmpLayer')
countRes.getOutput(0)
```




    u'8'




```python
arcpy.CopyFeatures_management('tmpLayer', './ch06/scratch/bufferflies.shp')
```




    <Result '.\\ch06\\scratch\\bufferflies.shp'>



## 6.7 Using Variables for Multiple Tool Calls


```python
fireDamage = 'special_regions.shp'
fireBuffer = fireDamage[:-4] + 'Buffer.shp'
fireBuffer
```

* **Example 6.3 buffer_clip.py**  


```python
# %load ch06/script2/buffer_clip.py
# buffer_clip.py (hard-coded version)
# Purpose: Buffer a zone and use it to clip another file
# Input: No arguments needed.

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'ch06/data'

outDir = 'ch06/scratch'

# Set buffer params
fireDamage = 'special_regions.shp'
fireBuffer = outDir + fireDamage[:-4] + 'Buffer.shp'
bufferDist = '1 mile'

# Set clip params
park = 'park.shp'
clipOutput = outDir + park[:-4] + 'DamageBuffer.shp'

arcpy.Buffer_analysis(fireDamage, fireBuffer, bufferDist)
print '{0} created.'.format(fireBuffer)
arcpy.Clip_analysis(park, fireBuffer, clipOutput)
print '{0} created.'.format(clipOutput)

```


```python
%run ch06/script2/buffer_clip.py
```

    ch06/scratchspecial_regionsBuffer.shp created.
    ch06/scratchparkDamageBuffer.shp created.


## Example 6.4 addLengthField.py


```python
# %load ch06/script2/addLengthField.py
# addLengthField.py
# Purpose: Add a field containing polygon lengths to the shapefile.
# Usage: No arguments needed.
import arcpy
arcpy.env.workspace = 'ch06/data'

inputFile = 'special_regions.shp'
fieldName = 'Length'
arcpy.AddField_management(inputFile, fieldName, 'FLOAT')
arcpy.CalculateField_management(inputFile, fieldName, '!shape.length!', 'PYTHON')

```


```python
%run ch06/script2/addLengthField.py
```

    done!


## 6.8 Calling Custom Tools

* **Example 6.5 callInventory.py**  


```python
# %load ch06/script2/callInventory.py
# callInventory.py
# Purpose: Call the inventory tool.
import arcpy

arcpy.env.workspace = 'ch06/scratch'
inputDir = "ch06/data"
summary = 'summaryFile.txt'
arcpy.ImportToolbox('ch06/customTools.tbx')
arcpy.Inventory_custom(inputDir, 'SUMMARY_ONLY', summary)
print 'Summary text {0} created in {1}'.format(summary, inputDir)

```


```python
%run ch06/script2/callInventory.py
```

    Summary text summaryFile.txt created in ch06/data


## 6.9 A Word About Old Scripts

## 6.10 Discussion

## 6.11 Key Terms
## 6.12 Exercises


```python

```
