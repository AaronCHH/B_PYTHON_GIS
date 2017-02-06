import arcpy, string
import arcpy.mapping as MAP

# Read input parameters from script tool
MXDList = string.split(arcpy.GetParameterAsText(0), ";")
printer = arcpy.GetParameterAsText(1)

# Loop through each MXD and print
for MXDPath in MXDList:
	MXD = MAP.MapDocument(MXDPath)
	MAP.PrintMap(MXD, printer)

# Remove variable reference to file
del MXD