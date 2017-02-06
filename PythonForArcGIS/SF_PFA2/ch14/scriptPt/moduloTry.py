# moduloTry.py
# Purpose: Compute the remainder of dividing two numbers.
# Usage: Two integer values
# Example input1: 25 4
# Example input2: 5 0
# Example input3: woods 3

import sys

field1 = sys.argv[1]
field2 = sys.argv[2]
print "a: {0}   b: {1}".format(field1, field2)
a = int(field1)
b = int(field2)
c = a % b
print "c:", c
