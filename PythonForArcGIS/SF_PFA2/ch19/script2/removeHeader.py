# removeHeader.py
# Purpose: Remove header rows.
# Usage: No arguments required.  Input file hard-coded.
# Output: Modified text file *v2.txt

import os
headers = 2
infile = 'data/eyeTrack.csv'
baseN = os.path.basename(infile)
outfile = 'scratch/' + os.path.splitext(baseN)[0] \
          + 'v2.txt'
try:
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            # READ header lines, but don't write them.
            for i in range(headers):
                fin.readline()
            # READ and WRITE the remaining lines.
            for line in fin:
                fout.write(line)
            print '{0} created.'.format(outfile)
except IOError:
    print "{0} doesn't exist.".format(infile)
