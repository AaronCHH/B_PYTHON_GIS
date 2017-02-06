# removeColumns.py
# Purpose: Demonstrate removing columns, given the field names.
# Input: No arguments required.  Input file hard-coded.
# Output: Modified text file *v2.txt
import os


def getIndex(delimString, delimiter, name):
    '''Get position of item in a delimited string'''
    delimString = delimString.strip()
    lineList = delimString.split(delimiter)
    index = lineList.index(name)
    return index


def removeItems(indexList, delimiter, delimString):
    '''Remove items at given indices in a delimited string'''
    lineList = delimString.split(delimiter)
    indexList.sort(reverse=True)
    for i in indexList:
        lineList.pop(i)
    stringLine = delimiter.join(lineList)
    return stringLine

headers = 2
sep = ','
removeFields = ['LPCX', 'LPCY', 'RPCX', 'RPCY', 'LGX', 'LGY', 'RGX', 'RGY']
infile = 'C:/gispy/data/ch19/eyeTrack.csv'
baseN = os.path.basename(baseN)
outfile = 'C:/gispy/scratch/' + os.path.splitext(baseN)[0] \
          + 'v2' + os.path.splitext(baseN)[1]
try:
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            # READ header lines, but don't write them.
            for i in range(headers):
                fin.readline()
            # READ field names.
            fieldNamesLine = fin.readline()
            # FIND field indices.
            rfIndex = []
            for field in removeFields:
                rfIndex.append(getIndex(fieldNamesLine, sep, field))
            line = removeItems(rfIndex, sep, fieldNamesLine)
            fout.write(line)
            # READ and WRITE the remaining lines.
            for line in fin:
                line = removeItems(rfIndex, sep, line)
                fout.write(line)
            print '{0} created.'.format(outfile)
except IOError:
    print "{0} doesn't exist.".format(infile)
