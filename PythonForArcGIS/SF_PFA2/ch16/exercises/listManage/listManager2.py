# listManager2.py
# Purpose: Provide three list and delimited string manipulation functions.


def list2String(delimiter, L):
    '''Take a list and return a delimited string'''
    # Use list comprehension to cast each element to string,
    # because join fails for non-string elements.
    stringL = [str(i) for i in L]
    # Join the string elements of stringL
    s = delimiter.join(stringL)
    return s


def string2List(delimiter, s):
    '''Take a delimited string and return a list'''
    L = s.split(delimiter)
    print L
    return L


def uniqueList(L):
    '''Find the set of unique entries in a list.'''
    # Python Set data type hold only unique entries
    # S collects unique entries in L
    S = set(L)
    # Copy S back to L
    U = list(S)
    return U

if __name__ == '__main__':
    ## test 1
    theString = 'x;z;x;y;x;x;y;y;y;z;y'  # Get delimited string.
    delimiter = ';'  # Get delimiter.

    # Get a list from the string.
    theList = string2List(delimiter, theString)

    # Get a list with only unique elements.
    theListUnique = uniqueList(theList)

    # Get a string from the list.
    theOutString = list2String(delimiter, theListUnique)

    print '{0} -> {1}'.format(theString, theOutString)

    ## test 2
    theOtherList = ['foo', 'bla', 'bla', 'bla', 'bla', 'fee', 'fi', 'fo', 'fum']
    output = uniqueList(theOtherList)
    print '{0} -> {1}'.format(theOtherList, output)
