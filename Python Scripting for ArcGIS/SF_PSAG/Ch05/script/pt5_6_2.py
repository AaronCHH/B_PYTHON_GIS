import arcpy
tools = arcpy.ListTools("*_analysis")
for tool in tools:
	print arcpy.Usage(tool)