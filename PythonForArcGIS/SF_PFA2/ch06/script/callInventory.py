# callInventory.py
# Purpose: Call the inventory tool.
import arcpy

arcpy.env.workspace = 'C:/gispy/sample_scripts/ch06'
inputDir = "C:/gispy/data/ch06/"
summary = 'summaryFile.txt'
arcpy.ImportToolbox('customTools.tbx')
arcpy.Inventory_custom(inputDir, 'SUMMARY_ONLY', summary)
print 'Summary text {0} created in {1}'.format(summary, inputDir)
