
# 16 User-Defined Modules

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [16 User-Defined Modules](#16-user-defined-modules)
  * [16.1 Importing User-Defi ned Modules](#161-importing-user-defi-ned-modules)
  * [16.2 Using Functions in Another Module](#162-using-functions-in-another-module)
  * [16.3 Modifying User-Defi ned Modules (Reload!)](#163-modifying-user-defi-ned-modules-reload)
  * [16.4 Am I the Main Module? What’s My Name?](#164-am-i-the-main-module-whats-my-name)
  * [16.5 Time Handling Example](#165-time-handling-example)
  * [16.6 Summary](#166-summary)
  * [16.7 Key Terms](#167-key-terms)
  * [16.8 Exercises](#168-exercises)

<!-- tocstop -->


## 16.1 Importing User-Defi ned Modules


```python
import arcpy, os, sys
```

* **Example 16.1: A user-defined module**


```python
# %load ch16/supportCode/listManager.py
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

```


```python
import listManager
```


```python
import sys
sys.path
```




    ['',
     'C:\\Windows\\SYSTEM32\\python27.zip',
     'c:\\python27\\arcgis10.1\\DLLs',
     'c:\\python27\\arcgis10.1\\lib',
     'c:\\python27\\arcgis10.1\\lib\\plat-win',
     'c:\\python27\\arcgis10.1\\lib\\lib-tk',
     'c:\\python27\\arcgis10.1',
     'c:\\python27\\arcgis10.1\\lib\\site-packages',
     'C:\\Program Files (x86)\\ESRI\\WaterUtils\\ArcHydro\\bin',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\bin',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\arcpy',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\ArcToolbox\\Scripts',
     'c:\\python27\\arcgis10.1\\lib\\site-packages\\IPython\\extensions',
     'C:\\Users\\AaronHsu\\.ipython']




```python
sys.path.append('ch16/supportCode')
sys.path
```




    ['',
     'C:\\Windows\\SYSTEM32\\python27.zip',
     'c:\\python27\\arcgis10.1\\DLLs',
     'c:\\python27\\arcgis10.1\\lib',
     'c:\\python27\\arcgis10.1\\lib\\plat-win',
     'c:\\python27\\arcgis10.1\\lib\\lib-tk',
     'c:\\python27\\arcgis10.1',
     'c:\\python27\\arcgis10.1\\lib\\site-packages',
     'C:\\Program Files (x86)\\ESRI\\WaterUtils\\ArcHydro\\bin',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\bin',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\arcpy',
     'C:\\Program Files (x86)\\ArcGIS\\Desktop10.1\\ArcToolbox\\Scripts',
     'c:\\python27\\arcgis10.1\\lib\\site-packages\\IPython\\extensions',
     'C:\\Users\\AaronHsu\\.ipython',
     'ch16/supportCode']




```python
import sys
sys.path.append('ch16/otherCode')
import script4
```

    Inside script4
    D:\BOOKS\GISen\_PYTHON\PythonForArcGIS\SF_PFA2\ch16\otherCode\script4.py



```python
import sys, os
scriptPath = os.path.abspath(__ file__)
```


```python
scriptDir = os.path.dirname(scriptPath)
relativePath = 'otherCode'
modulePath = os.path.join(scriptDir, relativePath)
```


```python
sys.path.append(modulePath)
```


```python
import script4
```


```python
import sys, os
scriptPath = os.path.abspath(__ file__)
scriptDir = os.path.dirname(scriptPath)
relativePath = '../../ch15'
modulePath = os.path.join(scriptDir, relativePath)
sys.path.append(modulePath)
import punctuationArt
```

## 16.2 Using Functions in Another Module


```python
import listManager
theString = 'z;x;y'
theList = listManager.string2List(';' , theString)
theList
```

* **Example 16.2:Using a user-defi ned module from a script excerpt from sortString.py**


```python
# %load ch16/sortString.py
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

```

## 16.3 Modifying User-Defi ned Modules (Reload!)


```python
def delimStrLen(delimiter, s):
    '''Return the number of items in a delimited string.'''
    theList = string2List(delimiter, s)
    return len(theList)
```


```python
num = listManager.delimStrLen(delimiter,theString)
print 'Number of items: {0}'.format(num)
```


```python
import listManager
reload(listManager)
```

## 16.4 Am I the Main Module? What’s My Name?


```python
print '\nIn listManager.py, test string2List: '
theString = 'z;x;y'
theList = string2List(';', theString)
print '{0} -> {1}'.format(theString,theList)
```

## 16.5 Time Handling Example


```python
import time
time.ctime()
```


```python
time.sleep(10)
```


```python
import datetime
dt = datetime.datetime(1999, 12 ,31, 23, 59)
dt
```


```python
dt.hour
```


```python
dt.year
```


```python
dt.weekday()
```


```python
dt2 = datetime.datetime(1999,12,31, 11, 59)
timeDiff = dt - dt2
timeDiff
```


```python
timeDiff.days
```


```python
 timeDiff.total_seconds()
```


```python
hrs = timeDiff.total_seconds()/3600
hrs
```


```python
 dt2 < dt
```


```python
datetime.datetime.now() < dt
```

* **Example 16.3:A user-defi ned module timeReport.py**


```python
# %load ch16/supportCode/timeReport.py
# timeReport.py
# Purpose: Provide time-related functions.
# Usage: No script arguments needed for module testing.
import datetime, time


def getDay(theDate):
    '''Given a date, return the day of the week'''
    index = theDate.weekday()
    wDict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
             3: 'Thursday', 4: 'Friday', 5: 'Saturday',
             6: 'Sunday'}
    return wDict[index]


def getTime():
    '''Report the current time'''
    t = datetime.datetime.now()
    return t


def reportDiffTime(start, end, message='Time elapsed'):
    '''Print the number of seconds that passed
    between "start" and "end".'''
    difference = end - start
    seconds = difference.total_seconds()
    print '{0}: {1} seconds.'.format(message, seconds)


def reportTime(message='The current date and time is'):
    '''Print the current time'''
    now = time.ctime()
    print '{0}: {1}'.format(message, now)


if __name__ == '__main__':
    reportTime('Script began running at')
    # Get current time.
    beforeSleep = getTime()
    time.sleep(5)
    # Get current time.
    afterSleep = getTime()

    message = 'Time elapsed for sleeping'
    # Print the time difference.
    reportDiffTime(beforeSleep, afterSleep, message)
    reportTime('Script completed at')
    print 'Hurray! I like {0}s.'.format(getDay(afterSleep))

```

## 16.6 Summary

## 16.7 Key Terms

* User-defined module
* sys.path variable
* Built-in ```__file__``` variable
* Absolute vs. relative paths
* Built-in reload function
* Built-in ```__name__``` variable
* Built-in time anddatetime modules


## 16.8 Exercises


```python

```
