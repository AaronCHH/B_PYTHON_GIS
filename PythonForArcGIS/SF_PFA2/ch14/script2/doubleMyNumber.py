# doubleMyNumber.py
# Purpose: Multiply input by 2.
# Usage: numeric_value
# Example input: 5
import sys

try:
    number = float(sys.argv[1])
    product = 2*number
    print 'The doubled number is {0}'.format(product)
except:
    print 'An error occurred.'
    print 'Please enter a numerical argument.'

print 'Good bye!'
