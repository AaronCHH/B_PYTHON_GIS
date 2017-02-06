# latLong.py
# Purpose: Convert geographic coordinate formats.


def dd2dms(ddValue):
    '''Convert from decimal degrees to degrees minutes seconds.'''
    # Compute degrees
    posDD = abs(ddValue)
    posDegs = int(posDD)
    degs = posDegs
    if ddValue < 0:
        degs = -1*posDegs

    # Computer minutes
    rem = abs(ddValue) - abs(posDegs)
    prd = rem*60
    mins = int(prd)

    # Compute seconds
    secs = (prd - mins)*60
    dms = '{0} {1} {2}'.format(degs, mins, secs)


def dms2dd(dmsValue):
    '''Convert from degrees minutes seconds to decimal degrees.'''
    parts = dmsValue.split(' ')
    degs = int(parts[0])
    mins = int(parts[1])
    secs = float(parts[2])
    totalSeconds = secs + mins*60
    dd = degs + totalSeconds/3600.0
    return dd

# Convert point 1 from dd to dms
lat1 = 35.684072
long1 = -78.728027

# Call dd2dms for the longitude and latitude
y1 = dd2dms(lat1)
x1 = dd2dms(long1)

print 'Point 1: ({0}, {1}) -> ({2}, {3})'.format(lat1, long1, y1, x1)

# Convert point2 = (long2, lat2) from dms to dd...
lat2 = '-33 43 27.6234'
long2 = '24 31 17.521484'

# Convert point 2 from dms to dd
lat2 = '-33 43 27.6234'
long2 = '24 31 17.521484'

y2 = dms2dd(lat2)
x2 = dms2dd(long2)

print 'Point 2: ({0}, {1}) -> ({2}, {3})'.format(lat2, long2, y2, x2)
