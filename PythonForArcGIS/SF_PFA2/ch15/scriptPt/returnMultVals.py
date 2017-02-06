# returnMultVals.py
# Purpose: Find the midpoints of two line segments.
# Usage: No arguments needed.


def midPoint(x1, y1, x2, y2):
    '''Calculate the midpoint of line segment (x1,y1), (x2,y2).'''
    xVal = (x1 + x2)/2.0
    yVal = (y1 + y2)/2.0
    return xVal, yVal
# Find the midpoint of the line from (3,5) to (2,1).
# Capture the return values with two variables.
x, y = midPoint(3, 5, 2, 1)
print 'Midpoint of line segment (3,5),(2,1):'
print 'x = {0}'.format(x)
print 'y = {0}'.format(y)

# Find the midpoint of the line from (1,1) to (3,5).
# Capture the return values with one variable.
t = midPoint(1, 1, 3, 5)
print 'Midpoint of line segment (1,1),(3,5):'
print 'x = {0}'.format(t[0])
print 'y = {0}'.format(t[1])
