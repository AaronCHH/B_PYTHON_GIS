# parseTable.py
# Purpose: Parse numeric values in a tabular text file.
# Usage: No arguments required.  Input file hard-coded.
# Output: Printed ID, sum, count, and data value list for each row of a table in the text file.

cap = 5
infile = 'C:/gispy/data/ch19/report.txt'
try:
    with open(infile, 'r') as f:
        for line in f:
            # String to list of strings.
            lineList = line.split()
            # String items to float items.
            nums = [float(i) for i in lineList]
            # First col is ID, rest are data values.
            ID = nums[0]
            data = nums[1:]
            # Cap the data values at 5.
            for index, val in enumerate(data):
                if val > cap:
                    data[index] = cap
            # Count and sum the values and report the results.
            count = len(data)
            total = sum(data)
            print 'ID: {0}   Sum: {1}   Count {2}'.format(ID, total, count)
            print 'Data: {0}'.format(data)
except IOError:
    print "{0} doesn't exist or can't be opened.".format(infile)
