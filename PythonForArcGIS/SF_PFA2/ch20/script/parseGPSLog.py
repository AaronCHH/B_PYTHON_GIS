# parseGPSLog.py
# Purpose: Read GPS point data and create corresponding KML file
# Usage: kml_directory output_directory
# Example input: C:/gispy/data/ch20 C:/gispy/scratch

import arcpy, os, sys, time, traceback
# Assuming BeautifulSoup is in the same directory as our script...
import BeautifulSoup


class kmlPoint():
    def __init__(self):
        self.name = ""
        self.date = ""
        self.time = ""
        self.x = 0
        self.y = 0
        self.z = 0

    def parseDescription(self, descriptionList):
        '''Parse a point description '''
        # Description looks like: [u'Date: 01/18/2012', <br />, u'Time: 02:28:23 PM']
        try:
            # Get the date.
            date = descriptionList[0].split(":")
            self.date = date[1].strip()
            # Get the time.
            time = descriptionList[2]
            time = time.lower()
            time = time.replace("time:", "")
            self.time = time.strip()
        except:
            print traceback.format_exc()
            print "Data in {0} has an incomplete description: {1}".format(self.name, description.contents)

    def parsePoint(self, coord):
        '''Parse the coordinate values from  -78.67717,35.781952,0'''
        ### Split the coordinates string and set the point's x, y, and z coordinate values
        print self.y, self.x, self.z

dataDir = sys.argv[1]
outputDir = sys.argv[2]
if not os.path.exists(outputDir):
    os.mkdir(outputDir)

kmlFile =  "Sample_7_Day_GPS_Data.kml"

# Read the kml file and put contents in BeautifulSoup object.
data = open(dataDir + '/' + kmlFile, 'r')
soup = BeautifulSoup.BeautifulSoup(data)
data.close()

# GET kml with name and description tags.
names = soup.findAll("name")
descriptions = soup.findAll("description")

# Parse Placemarks
### Find all the placemarks in the soup and put the results in a variable named placesmarks.

pointList = []
for placemark in placemarks:
    # Check if the placemark contains a point or a linestring.
    pointSoup = placemark.find("point")
    if pointSoup:
        mypoint = kmlPoint()
        # point placemarks look like this:
        # <placemark> <name>Stop #30</name><styleurl>#normalPlacemark</styleurl> <description>Date: 01/18/2012<br />
        # Time: 02:28:23 PM</description> <point> <coordinates> -78.67717,35.781952,0</coordinates> </point> </placemark>
        mypoint.name = placemark.find("name").contents[0]
        mypoint.parseDescription(placemark.find("description").contents)

        # point Soup looks like this: [<point> <coordinates> -78.67717,35.781952,0</coordinates> </point>]
        coords = placemark.find("coordinates").contents[0]
        mypoint.parsePoint(coords)
        pointList.append(mypoint)
    else:
        print 'Skipping this Linestring placemark.'

# Create output shapefiles.
fc = '{0}.shp'.format(kmlFile[:-4])
arcpy.env.workspace = outputDir
arcpy.env.overwriteOutput = True

if arcpy.Exists(fc):
    arcpy.Delete_management(fc)

# Create spatial reference object to be used in 'CreateFeatureclass' tool call.
sr = arcpy.SpatialReference('WGS 1984')
### Create a POINT feature class, fc, in outputDir with spatial reference sr.

# Add fields.
fieldNames = ["Name", "Date", "Time"]
### Loop through the fields in the fieldnames list
    ### Add text fields for each field name in the list

# Insert kml points into point shapefile.
### Create an insert cursor named in a 'with' statement
    # Loop through the point list and create a new record for each.
    print "--Adding entries to {0}/{1}--".format(outputDir, fc)
    for currPoint in pointList:
        ### create a Geometry object, using the current point's x,y, and z values.
        ### Put row values in a list (Set the row's Geometry object, Name, Date, and Time field values based on the current point.)
        ### Insert the row.

print "--Output created: {0}--".format(outputDir + "/" + fc)
