# cubeMyNumber.py
# Purpose: Cube input value.
# Usage: numeric_value
# Example input: 5
import sys
try:
    number = float(sys.argv[1])
    cube = number**3
    print 'The cubed number is {0}'.format()  # missing arg
except:
    print 'Input must be numerical.'
print 'Good bye!'
