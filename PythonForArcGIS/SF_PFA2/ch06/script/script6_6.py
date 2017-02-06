import arcpy
arcpy.env.workspace = './data'
myData = 'xyData.txt'
arcpy.MakeXYEventLayer_management(myData,'x','y','tmpLayer')
countRes = arcpy.GetCount_management('tmpLayer')
countRes.getOutput(0)
arcpy.CopyFeatures_management('tmpLayer', 'butter flies.shp')