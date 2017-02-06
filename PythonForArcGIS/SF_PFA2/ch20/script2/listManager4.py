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


def python2htmlList(L, listType):
    '''Convert a Python list to HTML list of type ul or ol.
    For example, convert [rast1,rast2] to:
    <ul>
       <li>rast1</li>
       <li>rast2</li>
    </ul>
    '''
    # Wrap items in item tags.
    htmlItems = ['<li>' + item + '</li>' for item in L]

    # Join the item list into a string with a line break after each item.
    itemsString = '''\n'''.join(htmlItems)

    # Wrap the string of items in the list tag.
    htmlList = '''
    <{0}>
        {1}
    </{0}>
    '''.format(listType, itemsString)
    return htmlList


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
    ## Test 1
    theString = 'x;z;x;y;x;x;y;y;y;z;y'  # Set a delimited string.
    delimiter = ';'  # Set a delimiter.

    # Get a list from the string.
    theList = string2List(delimiter, theString)

    # Get a list with only unique elements.
    theListUnique = uniqueList(theList)

    # Get a string from the list.
    theOutString = list2String(delimiter, theListUnique)

    print '{0} -> {1}'.format(theString, theOutString)

    ## Test 2
    theOtherList = ['foo', 'bla', 'bla', 'bla', 'bla', 'fee', 'fi', 'fo', 'fum']
    output = uniqueList(theOtherList)
    print '{0} -> {1}'.format(theOtherList, output)

    # Generate an HTML list from a Python list.
    htmlList = python2htmlList(theList, 'ol')
    print htmlList
