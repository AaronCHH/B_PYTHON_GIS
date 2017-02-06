# passVars.py
# Purpose: Demonstrate 'UnboundLocalError'.
# Usage: No script arguments needed.
x = 5


def addOne():
    '''Add one to x and print x.'''
    x = x + 1
    print 'In here', x

print 'Out here', x
addOne()