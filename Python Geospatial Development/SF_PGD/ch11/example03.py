import pyproj

# Translate UTM Zone 11 coordinates into lat/long values:

UTM_X = 565718.5235
UTM_Y = 3980998.9244

srcProj = pyproj.Proj(proj="utm", zone="11", ellps="clrk66", units="m")
dstProj = pyproj.Proj(proj="longlat", ellps="WGS84", datum="WGS84")

long,lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)

print "UTM zone 11 coordinate (%0.4f, %0.4f) = %0.4f, %0.4f" \
    % (UTM_X, UTM_Y, lat, long)

# Calculate another point 10 kilometres northeast of this location:

angle   = 315 # 315 degrees = northeast.
distance = 10000

geod = pyproj.Geod(ellps="WGS84")
long2,lat2,invAngle = geod.fwd(long, lat, angle, distance)

print "%0.4f, %0.4f is 10km northeast of %0.4f, %0.4f" \
    % (lat2, long2, lat, long)

