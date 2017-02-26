#!/usr/bin/env python

import cgi
import time

import shapely.wkt

import database
import mapGenerator

#############################################################################

METERS_PER_MILE = 1609.344

#############################################################################

# Open the database.

database.open()

# Get our CGI parameters.

form = cgi.FieldStorage()

countryID = int(form['countryID'].value)
radius    = int(form['radius'].value)
x         = int(form['x'].value)
y         = int(form['y'].value)
mapWidth  = int(form['mapWidth'].value)
mapHeight = int(form['mapHeight'].value)

# Calculate the lat/long bounds for the map the user clicked on.

details = database.get_country_details(countryID)
envelope = shapely.wkt.loads(details['bounds_wkt'])

minLong,minLat,maxLong,maxLat = envelope.bounds
minLong = minLong - 0.2
minLat = minLat - 0.2
maxLong = maxLong + 0.2
maxLat = maxLat + 0.2

# Calculate the lat/long coordinate the user clicked on.

xFract = float(x)/float(mapWidth)
longitude = minLong + xFract * (maxLong-minLong)

yFract = float(y)/float(mapHeight)
latitude = minLat + (1-yFract) * (maxLat-minLat)

# Find all places within 'radius' miles of the given lat/long coordinate.

radius_in_meters = radius * METERS_PER_MILE

results = database.find_places_within(latitude, longitude,
                                      radius_in_meters)

# Generate the map.

#datasource = database.get_shoreline_datasource()
iLat  = int(round(latitude))
iLong = int(round(longitude))
datasource = database.get_tiled_shoreline_datasource(iLat, iLong)

imgFile = mapGenerator.generateMap(datasource,
                                   results['minLong'],
                                   results['minLat'],
                                   results['maxLong'],
                                   results['maxLat'],
                                   600, 600,
                                   points=results['places'])

# Finally, display the results.

print 'Content-Type: text/html; charset=UTF-8\n\n'
print '<html>'
print '<head><title>Search Results</title></head>'
print '<body>'
print '<b>' + details['name'] + '</b>'
print '<p>'
print '<img src="' + imgFile + '">'
print '</body>'
print '</html>'

