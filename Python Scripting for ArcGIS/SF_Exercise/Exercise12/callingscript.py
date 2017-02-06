import arcpy
import mycount
table = "DATA/streets.shp"
print mycount.countstringfields(table)
raw_input()