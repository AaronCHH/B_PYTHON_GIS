# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# script2.py
# Created on: 2016-08-02 12:31:51.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: script2 <input> <output> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
input = arcpy.GetParameterAsText(0)
if input == '#' or not input:
    input = "D:\\BOOKS\\GISen\\_PYTHON\\PythonForArcGIS\\SF_PFA\\ch06\\data\\getty_rast" # provide a default value if unspecified

output = arcpy.GetParameterAsText(1)

# Local variables:

# Process: Raster to ASCII
arcpy.RasterToASCII_conversion("", output)

