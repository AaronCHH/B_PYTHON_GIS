# inventory.py
# Purpose: Summarize the file content of a directory, listing the number
#   of each file type and more detail if requested.
# Usage: workspace, level of detail (SUMMARY_ONLY or DETAILED_INVENTORY)
# Example: C:/gispy/data/ch06 SUMMARY_ONLY summary.txt

import arcpy, sys, os, traceback

debug = 1
if debug:
    for i, v in enumerate(sys.argv):
        print 'Input {0}: {1}'.format(i, v)


def printMessages(message):
    '''Print in both the Geoprocessing Window and the Interpreter Window'''
    arcpy.AddMessage(message)
    print message


def printSummary(title, listDict):
    '''Report the summary'''
    message = '''\nSummary of {0}
-------------------------------------\n'''.format(title)
    for key in listDict:
        listLen = len(listDict[key])
        message = message + '{0} {1}s\n'.format(listLen, key)
    printMessages(message)
    return message


def printDetails(title, listDict):
    '''Report the directory contents'''
    message = '''\nFile types in {0}
-------------------------------------\n'''.format(title)
    for key in listDict:
        message = message + '{0}s: {1}\n'.format(key, listDict[key])
    printMessages(message)
    return message

outfile = os.path.join(sys.argv[1], sys.argv[3])
with open(outfile, 'w') as outf:
    try:
        arcpy.env.workspace = sys.argv[1]
        fcs = arcpy.ListFeatureClasses()

        if os.path.isdir(arcpy.env.workspace):
            fs = os.listdir(arcpy.env.workspace)
            fDict = {}
            for f in fs:
                desc = arcpy.Describe(f)
                fType = desc.dataType
                if fType in fDict:
                    fDict[fType].append(f)
                else:
                    fDict[fType] = [f]
            m = printSummary(arcpy.env.workspace, fDict)
            outf.write(m)
            if sys.argv[2] == 'DETAILED_INVENTORY':
                m = printDetails(arcpy.env.workspace, fDict)
                outf.write(m)
        else:
            m = 'Not a valid directory {0}'.format(arcpy.env.workspace)
            printMessages(m)
            outf.write(m)
    except IndexError:
        m = 'Not enough arguments.  Usage: workspace level of detail \
            (SUMMARY_ONLY or DETAILED_INVENTORY)'
        printMessages(m)
        outf.write(m)
    except:
        traceback.print_exc()
        printMessages('The file that broke it is named {0}'.format(f))
        outf.write(m)
