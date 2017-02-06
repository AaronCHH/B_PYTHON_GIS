# addLayer.py
# Purpose: Add a data layer to a map.
# Input: No arguments required.
import arcpy

# Initialize data variables.
arcpy.env.workspace = 'C:/gispy/data/ch24/maps/'
fileName = '../USstates/MA.shp'
mapName = 'layerManipExample3.mxd'

# Instantiate MapDocument and DataFrame objects.
mxd = arcpy.mapping.MapDocument(arcpy.env.workspace + '/' +
                                mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)

# Get the first data frame.
df = dfs[0]

# Instantiate a Layer object.
layerObj = arcpy.mapping.Layer(fileName)

# Add the new layer to the map.
arcpy.mapping.AddLayer(df, layerObj)

# Save a copy of the map.
copyName = 'C:/gispy/scratch/' + mapName[:-4] + '_V2.mxd'
mxd.saveACopy(copyName)
print '{0} created.'.format(copyName)

# Delete the MapDocument object to release the map.
del mxd
