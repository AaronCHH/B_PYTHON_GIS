import os
import arcpy
import random
from arcpy import env
env.workspace = os.getcwd()
# ----
env.overwriteoutput = True
inputfc = arcpy.GetParameterAsText(0)
outputfc = arcpy.GetParameterAsText(1)
percent = int(arcpy.GetParameterAsText(2))
desc = arcpy.Describe(inputfc)
input_count = int(arcpy.GetCount_management(inputfc)[0])
outcount = int(round(input_count * percent * 0.01))
inlist = []
randomlist = []
fldname = desc.OIDFieldName
rows = arcpy.SearchCursor(inputfc)
row = rows.next()
while row:
  id = row.getValue(fldname)
  inlist.append(id)
  row = rows.next()
while len(randomlist) < outcount:
  selitem = random.choice(inlist)
  randomlist.append(selitem)
  inlist.remove(selitem)
length = len(str(randomlist))
sqlexp = '"' + fldname + '"' + " in " + "(" + str(randomlist)[1:length - 1] + ")"
arcpy.MakeFeatureLayer_management(inputfc, "selection", sqlexp)
arcpy.CopyFeatures_management("selection", outputfc)