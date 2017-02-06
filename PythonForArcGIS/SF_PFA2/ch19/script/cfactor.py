# cfactor.py
# Purpose: Read a text file contents into a dictionary.
# Input: No arguments required.  Input file hard-coded.
# Output: Printed cfactor:label dictionary.

factorDict = {}
infile = 'C:/gispy/data/ch19/cfactors.txt'
try:
    with open(infile, 'r') as f:
        f.readline()
        for row in f:
            row = row.split('=')
            factor = int(row[0])
            label = row[1].rstrip()
            factorDict[factor] = label
    print factorDict
except IOError:
    print "{0} doesn't exist.".format(infile)
