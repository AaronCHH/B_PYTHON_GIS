# argHandler.py
# Purpose: Provide functions for checking the user input.func_closure.
#    Can be used as a support module for another script by passing in
#    the argument list.
#   For example, the following code could be placed in another script to
#      returns True or False to tell the caller
#      if the first user argument is a shapefile:
#             valid = argHandler.isShapefile(sys.argv,1)
# Input example1: meh
# Input example2: meh bleh blah
# Input example3: meh 4.5 C:/gispy/data/ch16/park.shp


import arcpy


def printArgs(arguments):
    '''Print user arguments.'''
    for index, arg in enumerate(arguments):
        print 'Argument {0}: {1}'.format(index, arg)


def requiredCount(argList, numRequiredArgs, message=''):
    '''
    Return True if the argument list length matches required number,
    else print warnings and return False.
    ------
    argList is the list of user arguments (e.g., sys.argv could be passed in here)
    numReturedArgs is the number of required arguments.
    message is an optional message to be printed if not all argus are passed in.
    '''
    if len(argList) == numRequiredArgs + 1:
        return True
    else:
        print 'This script requires {0} arguments.'.format(numRequiredArgs)
        print message
        return False


def getFloatArg(argList, position):
    '''
    Return the numeric value of a float argument
    in the given position or return None if the value is not a float
    ------
    argList is the list of user arguments (e.g., sys.argv could be passed in here)
    position is the index in the list of the argument of interest.
    '''
    try:
        num = float(argList[position])
        return num
    except:
        print 'Argument {0} is not a floating point number.'.format(position)
        return None


def isShapefile(argList, position):
    '''
    Return True if the arg in the given position is a shapefile
    else return False
    ------
    argList is the list of user arguments (e.g., sys.argv could be passed in here)
    position is the index in the list of the argument of interest.
    '''
    try:
        dsc = arcpy.Describe(argList[position])
        if dsc.dataType == 'ShapeFile':
            return True
        else:
            print 'Expecting a shapefile for arg {0}. Got {1} instead.'.format(position, dsc.dataType)
            return False
    except:
        print 'Input {0} is not a valid shapefile.'.format(position)
        return False

if __name__ == '__main__':
    # Test the functions.
    import sys

    # Test the printArgs function.
    printArgs(sys.argv)

    # Test the requiredCount function.
    requiredCount(sys.argv, 3, 'Not enough arguments, silly!')

    # Test the getFloatArg function.
    value = getFloatArg(sys.argv, 2)
    print 'The numerical value is {0}'.format(value)

    # Test the isShapefile function.
    ans = isShapefile(sys.argv, 3)
    if ans:
        import arcpy
        count = arcpy.GetCount_management(sys.argv[3])
        print 'The number of records is {0}'.format(count)

    print 'And finally, I like giant pandas.'
