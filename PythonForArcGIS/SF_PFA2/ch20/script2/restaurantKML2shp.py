# restaurantKML2shp.py
# Purpose: Create a shapefile from a kml file using an insert cursor.
# Usage: kml_directory output_directory
# Example input: C:/gispy/data/ch20 C:/gispy/scratch/

import arcpy, os, sys, BeautifulSoup

dataDir = sys.argv[1]
outDir = sys.argv[2]
arcpy.env.workspace = outDir
kmlFile = 'restaurants.kml'
kmlPath = os.path.join(dataDir, kmlFile)
baseName = os.path.splitext(kmlFile)[0]
fc = baseName + '.shp'

fieldNames = ['name', 'blurb', 'score']
fieldTypes = ['TEXT', 'TEXT', 'FLOAT']

# If the shapefile already been created, delete it.
if arcpy.Exists(fc):
    arcpy.Delete_management(fc)

sr = arcpy.SpatialReference('NAD 1983 UTM Zone 17N')
arcpy.CreateFeatureclass_management(outDir, fc, 'POINT', '#', '#', '#', sr)
for field, type in zip(fieldNames, fieldTypes):
    arcpy.AddField_management(fc, field, type)

# Get the tag soup.
with open(kmlPath, 'r') as kmlCode:
    soup = BeautifulSoup.BeautifulSoup(kmlCode)
coordinates = soup.findAll('coordinates')
names = soup.findAll('name')
descriptions = soup.findAll('description')

# Populate the shapefile.
with arcpy.da.InsertCursor(fc, ['SHAPE@XY'] + fieldNames) as ic:
    for c, n, d in zip(coordinates, names, descriptions):
        # Get field values.
        [x, y, z] = c.contents[0].split(',')
        myPoint = arcpy.Point(x, y)
        name = n.contents[0]
        blurb = d.contents[0]
        scoreString = d.contents[2]
        scoreList = scoreString.split(':')
        score = float(scoreList[1])
        # Put row values in a list & insert the new row.
        newRow = [myPoint, name, blurb, score]
        ic.insertRow(newRow)
print '{0}{1} created.'.format(outDir, fc)
if ic:
    del ic