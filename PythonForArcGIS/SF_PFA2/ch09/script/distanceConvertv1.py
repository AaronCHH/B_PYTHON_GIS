# distanceConvertv1.py
# Purpose: Converts km to miles and vice versa.
# Usage: numerical_distance, unit_of_measure
# Example: 5 km

import sys

dist = float(sys.argv[1])  # Cast string to float
unit = sys.argv[2]

mileList = ['mi', 'mi.', 'mile', 'miles']

if unit.lower() in mileList:
        output = dist*1.6
        print '{0} {1} is equivalent to {2} kilometers(s).'.format(dist, unit, output)
else:
        output = dist*.62
        print '{0} {1} is equivalent to {2} mile(s).'.format(dist, unit, output)
