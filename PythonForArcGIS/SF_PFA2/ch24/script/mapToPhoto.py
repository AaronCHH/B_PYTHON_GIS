# mapToPhoto.py
# Purpose: Export the 'Layout view' of a map as a PNG image.
# Usage: fullpath_mxd_filename fullpath_output_png_filename
# Sample input: C:/gispy/data/ch24/maps/landCover.mxd C:/gispy/scratch/getty_map.png
# Note: Portable Network Graphic (PNG) is an image format used for Internet content.
# Many other map export formats are available.

import arcpy, sys

# Full path names of an existing map and an image to create.
mapName = sys.argv[1]
imageName = sys.argv[2]

# Create a mapDocument object.
mxd = arcpy.mapping.MapDocument(mapName)

# Create an image of the map in 'Layout view'
arcpy.mapping.ExportToPNG(mxd, imageName)

print '{0} created.'.format(imageName)

# Delete the MapDocument object.
del mxd
