# reportSTargs.py
# Purpose: Print the arguments passed into a script tool.
# Arguments: Variable (can be used for any number of arguments)

import arcpy, sys


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)


def printArgs():
    '''Print user arguments.'''
    printArc('Number of arguments = {0}'.format(len(sys.argv)))
    for index, arg in enumerate(sys.argv):
        printArc('Argument {0}: {1}'.format(index, arg))

if __name__ == '__main__':
    printArgs()
