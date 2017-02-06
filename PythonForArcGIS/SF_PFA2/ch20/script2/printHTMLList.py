# printHTMLList.py
# Purpose: Call a function that converts
#           a Python list to an HTML list.


def python2htmlList(myList, listType, attrs=''):
    '''Convert a Python list to HTML list.
    For example, convert [rast1,rast2] to:
    <ul>
       <li>rast1</li>
       <li>rast2</li>
    </ul>
    '''
    # Wrap items in item tags.
    htmlItems = ['<li>' + str(item) + '</li>' for item in myList]

    # Join the item list into a string with a line break after each item.
    itemsString = '''\n        '''.join(htmlItems)

    # Wrap the string of items in the list tag.
    htmlList = '''
    <{0} {1}>
        {2}
    </{0}>
    '''.format(listType, attrs, itemsString)
    return htmlList

rasts = [u'elev', u'landcov', u'soilsid', u'getty_cover']
htmlList = python2htmlList(rasts, 'ul')
print htmlList

htmlList2 = python2htmlList(rasts, 'ol')
print htmlList2

htmlList3 = python2htmlList(rasts, 'ol', 'type="a"')
print htmlList3
