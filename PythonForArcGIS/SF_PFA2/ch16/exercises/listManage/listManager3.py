# listManager3.py
# Purpose: Provide list and delimited string manipulation functions.


def list2String(delimiter, L):
    '''Take a list and return a delimited string'''
    # Use list comprehension to cast each element to string,
    # because join fails for non-string elements.
    stringL = [str(i) for i in L]
    # Join the string elements of stringL.
    s = delimiter.join(stringL)
    return s


def string2List(delimiter, s):
    '''Take a delimited string and return a list'''
    L = s.split(delimiter)
    return L


def delimStrLen(delimiter, s):
    '''Return the number of items in a delimited string.'''
    theList = string2List(delimiter, s)
    return len(theList)

##def delimStrLen2(delimiter, s):
##    '''Return the number of non-empty items in a delimited string.'''
##    s = s.strip(delimiter) #strip leading/trailing delimiters
##    s = s.strip() #strip leading/trailing empty strings
##    theList = string2List(delimiter, s)
##    filteredList = [i for i in theList if i] #remove empty strings
##    return len(filteredList)
