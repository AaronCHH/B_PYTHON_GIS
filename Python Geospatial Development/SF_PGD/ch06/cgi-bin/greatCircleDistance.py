#!/usr/bin/python

# This CGI script implements a simple web service to calculate great-circle
# distances.

import cgi
import pyproj

form = cgi.FieldStorage()

lat1 = float(form['lat1'].value)
long1 = float(form['long1'].value)
lat2 = float(form['lat2'].value)
long2 = float(form['long2'].value)

geod = pyproj.Geod(ellps="WGS84")
angle1,angle2,distance = geod.inv(long1, lat1, long2, lat2)

print 'Content-Type: text/plain'
print
print distance
