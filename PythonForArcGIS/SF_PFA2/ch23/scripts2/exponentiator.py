# exponentiator.py
# Purpose: Raise base to a power.
# Arguments: base power(must be a number or #)

import sys, reportSTargs

base = float(sys.argv[1])

# Handle optional argument.
if sys.argv[2] == '#':
    power = 1
    reportSTargs.printArc('No exponent provided.  Using default power of 1.')
else:
    power = float(sys.argv[2])

# Calculate the exponentiation.
result = base**power

# Report the results.
reportSTargs.printArc('{0} raised to the {1} is {2}'.format(base, power, result))
