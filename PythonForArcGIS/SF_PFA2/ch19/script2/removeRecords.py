# removeRecords.py
# Purpose: Demonstrate emoving rows under specific conditions.
# Input: No arguments required.  Input file hard-coded.
# Output: Modified text file *v2.txt

import os
headers = 2
field1 = 'FPOGX'
field2 = 'FPOGY'
sep = ','


def getIndex(delimString, delimiter, name):
    '''Get position of item in a delimited string'''
    delimString = delimString.strip()
    lineList = delimString.split(delimiter)
    index = lineList.index(name)
    return index

infile = 'data/eyeTrack.csv'
baseN = os.path.basename(infile)
outfile = 'scratch/' + os.path.splitext(baseN)[0] \
          + 'v2' + os.path.splitext(baseN)[1]
try:
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            # READ header lines, but don't write them.
            for i in range(headers):
                line = fin.readline()
            # READ and WRITE field names
            line = fin.readline()
            fout.write(line)

            # FIND field indices
            findex1 = getIndex(line, sep, field1)
            findex2 = getIndex(line, sep, field2)

            # FOR the remaining lines:
            for line in fin:
                lineList = line.split(sep)
                v1 = float(lineList[findex1])
                v2 = float(lineList[findex2])
                v2 = float(lineList[findex2])
                # IF condition is TRUE, write line.
                if v1 > 0 and v2 > 0:
                    fout.write(line)
            print '{0} created.'.format(outfile)

except IOError:
    print "{0} doesn't exist.".format(infile)
