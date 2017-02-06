# callInventory.py
# Purpose: Call the inventory tool.
import arcpy

arcpy.env.workspace = 'ch06/scratch'
inputDir = "ch06/data"
summary = 'summaryFile.txt'
arcpy.ImportToolbox('ch06/customTools.tbx')
arcpy.Inventory_custom(inputDir, 'SUMMARY_ONLY', summary)
print 'Summary text {0} created in {1}'.format(summary, inputDir)
