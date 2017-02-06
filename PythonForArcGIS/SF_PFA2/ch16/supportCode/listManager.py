# listManager.py
# Purpose: Provide list and delimited string manipulation functions.
# Usage: No script arguments needed.


def list2String(delimiter, L):
    '''Take a list and return a delimited string.'''
    # Join fails for non-string elements, so use list
    # comprehension to cast each element to string.
    stringL = [str(i) for i in L]
    # Join the string elements of stringL
    s = delimiter.join(stringL)
    return s


def string2List(delimiter, s):
    '''Take a delimited string and return a list.'''
    L = s.split(delimiter)
    return L

##def delimStrLen(delimiter, s):
##    '''Return the number of items in a delimited string.'''
##    theList = string2List(delimiter, s)
##    return len(theList)

##print '\nIn listManager.py, test string2List: '
##theString = 'z;x;y'
##theList = string2List( ';' , theString )
##print '{0} -> {1}'.format(theString,theList)
