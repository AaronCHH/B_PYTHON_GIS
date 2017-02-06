# fieldIndex.py
# Purpose: Find the index of a field name in a text
#         file with space separated fields in the first row.
# Input: No arguments required.  Input file hard-coded.
infile = 'C:/gispy/data/ch19/cfactors.txt'
fieldName = 'Label'


def getIndex(delimString, delimiter, name):
    '''Get position of item in a delimited string'''
    delimString = delimString.strip()
    rowList = delimString.split(delimiter)
    index = rowList.index(name)
    return index

with open(infile, 'r') as f:
    row = f.readline()
    ind = getIndex(row, ' ', fieldName)
    print '{0} has index {1}'.format(fieldName, ind)
