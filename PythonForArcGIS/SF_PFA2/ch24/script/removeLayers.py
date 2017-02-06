# removeLayers.py
# Purpose: Remove the first layer in the table of contents.
# Input: No arguments required.

import arcpy

# Get a MapDocument object.
mxdName = 'layerManipExample2.mxd'
mapPath = 'C:/gispy/data/ch24/maps/'
mxd = arcpy.mapping.MapDocument(mapPath + mxdName)

# Get a list of the DataFrame objects.
dfs = arcpy.mapping.ListDataFrames(mxd)

# Get the first DataFrame object.
df = dfs[0]

# Get a list of Layer objects in this data frame.
lyrs = arcpy.mapping.ListLayers(mxd, '', df)

# Get the first Layer object.
layerToRemove = lyrs[0]

# Remove the layer.
arcpy.mapping.RemoveLayer(df, layerToRemove)

# Save a copy of the map.
copyName = 'C:/gispy/scratch/' + mxdName[:-4] + '_V2.mxd'
mxd.saveACopy(copyName)
print '{0} created.'.format(copyName)

# Delete the <code>MapDocument</code> object to release the map.
del mxd
