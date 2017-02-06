# parseKMLDescription.py
# Purpose: Parse KML description tags.
# Usage: kml_fullpath_filename
# Example input: C:/gispy/data/Ch20/Sample_7_Day_GPS_Data.kml
import sys, BeautifulSoup
    
filename = sys.argv[1]

# Read the kml file and put contents in BeautifulSoup object.
data = open(filename, 'r')
soup = BeautifulSoup.BeautifulSoup(data)
data.close()

# GET kml with name and description tags.
names = soup.findAll("name")
descriptions = soup.findAll("description")

# Parse Placemarks.
placemarks = soup.findAll("placemark")

totalDist = 0
for placemark in placemarks:
    # Some placemarks are points, some are linestrings.
    lineSoup = placemark.findAll("linestring")
    # If it's a point placemark 'lineSoup' is an empty string.
    if lineSoup:
        ## Line placemarks look like this:
        # <placemark> <name>Route #30</name> <description><br />Driving Time: 00h:11m:29s<br />Distance Traveled: 0.05 mile<br />Maximum Speed:
        # 9.98 mile/hour<br />Average Speed: 0.29 mile/hour</description> <styleurl>#yellowLineGreenPoly2</styleurl> <linestring> <extrude>1
        # </extrude> <tessellate>1</tessellate> <coordinates> -78.677147,35.781898,0  -78.677147,35.781898,0  -78.677147,35.781898,0
        # -78.677147,35.781898,0  -78.677147,35.781898,0  -78.677147,35.781898,0  -78.677147,35.781898,0  -78.677147,35.781898,0
        # </coordinates> </linestring></placemark>
        description = placemark.find("description")
        descriptionList = description.contents

        ## descriptionList looks like this:
        # [<br />, u'Driving Time: 00h:01m:49s', <br />,
        # u'Distance Traveled: 0 mile', <br />, u'Maximum Speed: 1.25 mile/hour',
        # <br />, u'Average Speed: 0.05 mile/hour']
