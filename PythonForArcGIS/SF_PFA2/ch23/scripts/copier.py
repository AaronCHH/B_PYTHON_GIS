# copier.py
# Purpose: Make a copy of argument 1 with a name specified by argument 2.

import arcpy, reportSTargs, sys

reportSTargs.printArgs()

arcpy.Copy_management(sys.argv[1], sys.argv[2])
