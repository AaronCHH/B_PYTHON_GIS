# print4ScriptTools.py
# Purpose: Prints a directory's file count using
#          both 'print' and 'AddMessage'
# Usage: No arguments required.

import arcpy, os


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)

myDir = r'..\data\smallDir'

# Lists all the files in the directory.
fileList = os.listdir(myDir)

myMessage = 'Directory {0} contains {1} files.'.format(myDir, len(fileList))

printArc(myMessage)
