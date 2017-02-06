# cubeMyNumberV2.py
# Purpose: Cube input value
#   or print traceback message.
# Usage: numeric_value
# Example input: 5
import sys, traceback
try:
    number = float(sys.argv[1])
    cube = number**3
    print 'The cubed number is {0}'.format()  # missing arg
except:
    print 'Input must be numerical.'
    traceback.print_exc()
print 'Good bye!'
