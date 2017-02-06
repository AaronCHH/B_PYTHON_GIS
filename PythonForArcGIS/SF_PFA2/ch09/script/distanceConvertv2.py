# distanceConvertv2.py
# Purpose: Converts km to miles and vice versa.
# Usage: numerical_distance, {unit_of_measure}
# Example 1: 5 km
# Example 2:
# Example 3: 2.3
# Example 4: 10 MI
# Example 5: 2.2 bananas

import sys

numArgs = len(sys.argv)

# If no user arguments are given, exit the script and warn the user.
if numArgs == 1:
        print 'Usage: numeric_distance {distance_unit (mi or km)}'
        print 'Example: 5 km'
        sys.exit(0)  # exit the script

# If only one user argument is given, set the unit to miles.
if numArgs < 3:
        unit = 'miles'
        print 'Warning: No distance unit provided. Assuming input is in miles.'
else:
        # Get the unit provided by the user
        unit = sys.argv[2]

# Get the numeric distance (cast string to float).
dist = float(sys.argv[1])

# Perform conversion.
mileList = ['mi', 'mi.', 'mile', 'miles']

if unit.lower() in mileList:
        output = dist*1.6
        print'{0} {1} is equivalent to {2} kilometers(s).'.format(dist, unit, output)
else:
        output = dist*.62
        print '{0} {1} is equivalent to {2} mile(s).'.format(dist, unit, output)
