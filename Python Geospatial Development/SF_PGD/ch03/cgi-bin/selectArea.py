#!/usr/bin/env python

import cgi, os.path, sys
import shapely.wkt
import database
import mapGenerator

HEADER = "Content-Type: text/html; charset=UTF-8\n\n" \
       + "<html><head><title>Select Area</title>" \
       + "</head><body>"

FOOTER = "</body></html>"

MAX_WIDTH = 600
MAX_HEIGHT = 400

database.open()

form = cgi.FieldStorage()
if not form.has_key("countryID"):
    print HEADER
    print '<b>Please select a country</b>'
    print FOOTER
    sys.exit(0)

countryID = int(form['countryID'].value)

details = database.get_country_details(countryID)
if details == None:
    print HEADER
    print '<b>Missing Country ' + repr(countryID) + '</b>'
    print FOOTER
    sys.exit(0)

envelope = shapely.wkt.loads(details['bounds_wkt'])
minLong,minLat,maxLong,maxLat = envelope.bounds
minLong = minLong - 0.2
minLat = minLat - 0.2
maxLong = maxLong + 0.2
maxLat = maxLat + 0.2

width = float(maxLong - minLong)
height = float(maxLat - minLat)
aspectRatio = width/height

mapWidth = MAX_WIDTH
mapHeight = int(mapWidth / aspectRatio)

if mapHeight > MAX_HEIGHT:
    # Scale the map to fit.
    scaleFactor = float(MAX_HEIGHT) / float(mapHeight)
    mapWidth = int(mapWidth * scaleFactor)
    mapHeight = int(mapHeight * scaleFactor)

datasource = database.get_country_datasource()

imgFile = mapGenerator.generateMap(datasource,
                                   minLong, minLat,
                                   maxLong, maxLat,
                                   mapWidth, mapHeight,
                                   "[id] = "+str(countryID))

print 'Content-Type: text/html; charset=UTF-8\n\n'
print '<html>'
print '<head><title>Select Area</title></head>'
print '<body>'
print '<b>' + details['name'] + '</b>'
print '<p>'
print '<form method="POST" action="showResults.py">'
print 'Select all features within'
print '<input type="text" name="radius" value="10" size="2">'
print 'miles of a point.'
print '<p>'
print 'Click on the map to identify your starting point:'
print '<br>'
print '<input type="image" src="' + imgFile + '" ismap>'
print '<input type="hidden" name="countryID"'
print '       value="' + str(countryID) + '">'
print '<input type="hidden" name="mapWidth"'
print '       value="' + str(mapWidth) + '">'
print '<input type="hidden" name="mapHeight"'
print '       value="' + str(mapHeight) + '">'
print '</form>'
print '</body></html>'

