# reportArgs.py
# Purpose: Print the script arguments.
import sys


def printArgs():
    '''Print user arguments.'''
    for index, arg in enumerate(sys.argv):
        print 'Argument {0}: {1}'.format(index, arg)

printArgs()
