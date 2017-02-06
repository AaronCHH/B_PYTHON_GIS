# multiIn.py
# Purpose: Parse a semicolon delimited input string.
import reportSTargs, sys

inputString = sys.argv[1]

reportSTargs.printArc('Input string: {0}'.format(inputString))

inputList = inputString.split(';')

for i in inputList:
    reportSTargs.printArc('Input file: {0}'.format(i))
