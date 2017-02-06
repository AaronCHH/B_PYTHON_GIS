# argPrint.py
# Purpose: Print args with built-in 'enumerate' function.
# Usage: Any arguments.
# Example input: 500 miles
import sys
for index, arg in enumerate(sys.argv):
    print 'Argument {0}: {1}'.format(index, arg)
