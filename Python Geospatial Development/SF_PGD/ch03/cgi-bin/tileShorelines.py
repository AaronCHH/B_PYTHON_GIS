import math

import pyproj
from shapely.geometry import Polygon
from shapely.ops import cascaded_union
import shapely.wkt

import database

#############################################################################

MAX_DISTANCE = 100000 # Maximum search radius, in meters.

#############################################################################

def expandRect(minLat, minLong, maxLat, maxLong, distance):

    geod = pyproj.Geod(ellps="WGS84")
    midLat  = (minLat + maxLat) / 2.0
    midLong = (minLong + maxLong) / 2.0

    try:
        availDistance = geod.inv(midLong, maxLat, midLong,
                                 +90)[2]
        if availDistance >= distance:
            x,y,angle = geod.fwd(midLong, maxLat, 0, distance)
            maxLat = y
        else:
            maxLat = +90
    except:
        maxLat = +90 # Can't expand north.

    try:
        availDistance = geod.inv(maxLong, midLat, +180,
                                 midLat)[2]
        if availDistance >= distance:
            x,y,angle = geod.fwd(maxLong, midLat, 90,
                                 distance)
            maxLong = x
        else:
            maxLong = +180
    except:
        maxLong = +180 # Can't expand east.

    try:
        availDistance = geod.inv(midLong, minLat, midLong,
                                 -90)[2]
        if availDistance >= distance:
            x,y,angle = geod.fwd(midLong, minLat, 180,
                                 distance)
            minLat = y
        else:
            minLat = -90
    except:
        minLat = -90 # Can't expand south.

    try:
        availDistance = geod.inv(maxLong, midLat, -180,
                                 midLat)[2]
        if availDistance >= distance:
            x,y,angle = geod.fwd(minLong, midLat, 270,
                                 distance)
            minLong = x
        else:
            minLong = -180
    except:
        minLong = -180 # Can't expand west.

    return (minLat, minLong, maxLat, maxLong)

#############################################################################

# Load the shoreline outlines into memory:

print "opening"

database.open()
shorelines = database.load_shorelines()

# Initialize the tilePolys arrays:

print "init"

tilePolys = []
for iLat in range(-90, +90):
    tilePolys.append([])
    for iLong in range(-180, +180):
        tilePolys[-1].append([])

# Calculate the list of polygons which belong in each tile:

n = 0
for shoreline in shorelines:
    print "%d of %d" % (n, len(shorelines))
    n = n + 1

    minLong,minLat,maxLong,maxLat = shoreline.bounds
    minLong = int(math.floor(minLong))
    minLat  = int(math.floor(minLat))
    maxLong = int(math.ceil(maxLong))
    maxLat  = int(math.ceil(maxLat))

    print minLong,minLat,maxLong,maxLat

    vStrips = []
    for iLong in range(minLong, maxLong+1):
        print iLong

        stripMinLat  = minLat
        stripMaxLat  = maxLat
        stripMinLong = iLong
        stripMaxLong = iLong + 1

        bMinLat,bMinLong,bMaxLat,bMaxLong = \
                expandRect(stripMinLat, stripMinLong,
                           stripMaxLat, stripMaxLong,
                           MAX_DISTANCE)

        bounds = Polygon([(bMinLong, bMinLat),
                          (bMinLong, bMaxLat),
                          (bMaxLong, bMaxLat),
                          (bMaxLong, bMinLat),
                          (bMinLong, bMinLat)])

        strip = shoreline.intersection(bounds)
        vStrips.append(strip)

    print "got strips.  Splitting each strip."
    stripNum = 0
    for iLong in range(minLong, maxLong+1):
        print iLong
        vStrip = vStrips[stripNum]
        stripNum = stripNum + 1

        for iLat in range(minLat, maxLat+1):
            bMinLat,bMinLong,bMaxLat,bMaxLong = \
                expandRect(iLat, iLong, iLat+1, iLong+1,
                           MAX_DISTANCE)

            bounds = Polygon([(bMinLong, bMinLat),
                              (bMinLong, bMaxLat),
                              (bMaxLong, bMaxLat),
                              (bMaxLong, bMinLat),
                              (bMinLong, bMinLat)])

            polygon = vStrip.intersection(bounds)
            if not polygon.is_empty:
                tilePolys[iLat][iLong].append(polygon)

# Create our tiled_shorelines database table:

database.create_tile_tables()

# Finally, save the tiled polygons into the database:

print "Saving"

for iLat in range(-90, +90):
    print iLat
    for iLong in range(-180, +180):
        polygons = tilePolys[iLat][iLong]
        if len(polygons) == 0:
            outline = Polygon()
        else:
            outline = shapely.ops.cascaded_union(polygons)
        wkt = shapely.wkt.dumps(outline)

        database.save_tiled_shoreline(iLat, iLong, wkt)

