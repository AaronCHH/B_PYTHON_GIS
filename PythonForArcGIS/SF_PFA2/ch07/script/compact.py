# compact.py
# Purpose: Compact a file
# Usage: Full path file name of an mdb file.
# Example: C:/gispy/data/ch07/cities.mdb
import arcpy, os

# Get user input
fileName = arcpy.GetParameterAsText(0)
baseName = os.path.basename(fileName)

# Check size
size = os.path.getsize(fileName)
print '{0} file size before compact: {1} bytes.'.format(baseName, size)

# Compact the file
arcpy.Compact_management(fileName)

# Check size
size = os.path.getsize(fileName)
print '{0} file size AFTER compact: {1} bytes.'.format(baseName, size)
