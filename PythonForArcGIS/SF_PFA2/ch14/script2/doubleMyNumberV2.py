# doubleMyNumberV2.py
# Purpose: Multiply input by 2
#          or catch value error.
# Usage: numeric_value
# Example input: 5
import sys

try:
    number = float(sys.argv[1])
    product = 2*number
    print 'The doubled number is {0}'.format(product)
except ValueError:
    print 'Input must be numerical.'
print 'Good bye!'
