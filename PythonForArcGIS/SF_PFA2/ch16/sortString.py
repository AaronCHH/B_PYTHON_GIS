# sortString.py
# Purpose: Sort the items in a delimited string.

import os, sys
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relativePath = 'supportCode'
modulePath = os.path.join(scriptDir, relativePath)
sys.path.append(modulePath)
import listManager
##reload(listManager)

delimiter = '~'  # Set delimiter.
theString = 'fireID~unit~shelter~alt~campgr'  # Set delimited string.

# Get a list from the string. module.function(argv1, argv2,...) format.
theList = listManager.string2List(delimiter, theString)

# Sort the list. Sort is a native list method (not a method defined in listManager.
# Notice the difference in how it is called. It's called with object.method format,
# where the object is theList.
theList.sort()

# Get a string from the list. module.function(argv1, argv2,...) format.
newString = listManager.list2String(delimiter, theList)

print '\nsortString.py results:'
print '{0} -> {1}'.format(theString, newString)

##num = listManager.delimStrLen(delimiter , theString )
##print 'Number of items: {0}'.format(num)
