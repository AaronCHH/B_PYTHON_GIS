# returnVSprint.py
# Purpose: Demonstrate that the default return value is 'None'.
# Usage: No script arguments needed.


def positiveMinV1(numList):
    '''Find the minimum positive number in the list'''
    pos = []
    for val in numList:
        if val >= 0:
            pos.append(val)
    positiveMin = min(pos)
    print 'Min positive number = {0}'.format(positiveMin)

theList = [8, 2.5, 0, 12, 5]
print 'Run function 1...'
value = positiveMinV1(theList)
print 'positiveMinV1 returned: {0}'.format(value)


def positiveMinV2(numList):
    pos = []
    for val in numList:
        if val >= 0:
            pos.append(val)
    return min(pos)
print 'Run function 2...'
value = positiveMinV2(theList)
print 'positiveMinV2 returned: {0}'.format(value)
