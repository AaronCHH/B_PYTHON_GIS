
# 19 Reading and Writing Text Files

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [19 Reading and Writing Text Files](#19-reading-and-writing-text-files)
  * [19.1 Working with file Objects](#191-working-with-file-objects)
    * [19.1.1 The WITH Statement](#1911-the-with-statement)
    * [19.1.2 Writing Text Files](#1912-writing-text-files)
    * [19.1.3 Safe File Reading](#1913-safe-file-reading)
    * [19.1.4 The os Working Directory vs. the arcpy workspace](#1914-the-os-working-directory-vs-the-arcpy-workspace)
    * [19.1.5 Reading Text Files](#1915-reading-text-files)
  * [19.2 Parsing Line Contents](#192-parsing-line-contents)
    * [19.2.1 Parsing Field Names](#1921-parsing-field-names)
  * [19.3 Modifying Text](#193-modifying-text)
    * [19.3.1 Pseudocode for Modifying Text Files](#1931-pseudocode-for-modifying-text-files)
    * [19.3.2 Working with Tabular Text](#1932-working-with-tabular-text)
  * [19.4 Pickling](#194-pickling)
  * [19.5 Discussion](#195-discussion)
  * [19.6 Key Terms](#196-key-terms)
  * [19.7 Exercises](#197-exercises)

<!-- tocstop -->


## 19.1 Working with file Objects


```python
f = open('ch19/data/poem.txt', 'r')
```


```python
f = open('ch19/data/poem.txt', 'r')
f.read()
```




    'Scripterwocky\n`Twas brillig, and the Python lists\nDid join and pop-le in the loop:\nAll-splitsy were the string literals,\nAnd the boolean values were true.\t \n'




```python
f.close()
```

### 19.1.1 The WITH Statement


```python
with open('C:/gispy/data/ch19/poem.txt', 'r')as f:
    print f.read()
```


```python
f = open('C:/gispy/data/ch19/poem.txt', 'r')
f.read()
f.close()
```


```python
with open('C:/gispy/data/ch19/poem.txt', 'r')as f:
    print f.read()
f.read()
```

### 19.1.2 Writing Text Files


```python
f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
f.write('haa')
f.write('choo')
f.close()
```


```python
f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
f.write('snork\nsnif fle\n')
f.write('haaack\n')
f.write('*sigh*')
f.close()
```


```python
f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
f.close()
```


```python
f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
csv = ','.join(['glug', 'gulp', 'erp'])
f.write(csv)
f.write('\n')
lines = '\n'.join(['ack', 'hmmm', 'sniff'])
f.write(lines)
f.close()
```


```python
f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
f.write(5000)
```


```python
f.write(str(5000))
lament = 'I sneezed {0} times today.'.format(5000)
f.write(lament)
f.close()
```

### 19.1.3 Safe File Reading


```python
f = open('C:/gispy/data/ch19/bogus.txt', 'r')
```


```python
# %load ch19/script2/safeFileRead.py
import os, sys
infile = sys.argv[1]
try:
    f = open(infile, 'r')
    print f.read()
    f.close()
except IOError:
    print"{0} doesn't exist or can't be opened.".format(infile)
```

### 19.1.4 The os Working Directory vs. the arcpy workspace


```python
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch19'
f = open('poem.txt', 'r')
```


```python
import os
os.path.is file('C:/gispy/data/ch19/poem.txt')
```


```python
os.getcwd()
```


```python
os.chdir('C:/gispy/data/ch19')
os.getcwd()
```


```python
f = open('poem.txt', 'r')
f.readline()
```


```python
f.close()
```

### 19.1.5 Reading Text Files


```python
f = open('C:/gispy/data/ch19/poem.txt', 'r')
f.readline()
```


```python
f.readline()
```


```python
f.readline()
```


```python
f.readline()
```


```python
f.readline()
```


```python
f.readline()
```


```python
f.close()
```


```python
for line in f:
    print line
```


```python
f.readline()
```


```python
f.close()
```


```python
f = open('C:/gispy/data/ch19/poem.txt', 'r')
f.readline()
for line in f:
    print line
f.close()
```

## 19.2 Parsing Line Contents


```python
f = open('ch19/data/report.txt', 'r')
f.readline()
```




    '1\t2.07\t5.21\t4.05\t3.64\t2.03\t3.74\n'




```python
line = f.readline()
line
```




    '2\t3.51\t7.29\t4.2\t4.44\t3.67\t4.46\n'




```python
lineList = line.split()
lineList
```




    ['2', '3.51', '7.29', '4.2', '4.44', '3.67', '4.46']




```python
nums = [float(i) for i in lineList]
nums
```




    [2.0, 3.51, 7.29, 4.2, 4.44, 3.67, 4.46]




```python
data = nums[1:]
data
```




    [3.51, 7.29, 4.2, 4.44, 3.67, 4.46]




```python
sum(data)
```




    27.57



* **Example 19.1 parseTable.py**


```python
# %load ch19/script2/parseTable.py
# parseTable.py
# Purpose: Parse numeric values in a tabular text file.
# Usage: No arguments required.  Input file hard-coded.
# Output: Printed ID, sum, count, and data value list for each row of a table in the text file.

cap = 5
infile = 'data/report.txt'
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

```

* **Example 19.2 cfactor.py**


```python
# %load ch19/script2/cfactor.py
# cfactor.py
# Purpose: Read a text file contents into a dictionary.
# Input: No arguments required.  Input file hard-coded.
# Output: Printed cfactor:label dictionary.

factorDict = {}
infile = 'data/cfactors.txt'
try:
    with open(infile, 'r') as f:
        f.readline()
        for row in f:
            row = row.split('=')
            factor = int(row[0])
            label = row[1].rstrip()
            factorDict[factor] = label
    print factorDict
except IOError:
    print "{0} doesn't exist.".format(infile)

```

### 19.2.1 Parsing Field Names


```python
mylist = ['a','b','c','d']
mylist.index('c')
```




    2



* **Example 19.3 fieldIndex.py**


```python
# %load ch19/script2/fieldIndex.py
# fieldIndex.py
# Purpose: Find the index of a field name in a text
#         file with space separated fields in the first row.
# Input: No arguments required.  Input file hard-coded.
infile = 'data/cfactors.txt'
fieldName = 'Label'


def getIndex(delimString, delimiter, name):
    '''Get position of item in a delimited string'''
    delimString = delimString.strip()
    rowList = delimString.split(delimiter)
    index = rowList.index(name)
    return index

with open(infile, 'r') as f:
    row = f.readline()
    ind = getIndex(row, ' ', fieldName)
    print '{0} has index {1}'.format(fieldName, ind)

```


```python

```

## 19.3 Modifying Text

* **Example 19.4 cfactorModify.py**


```python
# %load ch19/script2/cfactorModify.py
# cfactorModify.py
# Purpose: Demonstrate reading and writing files.
# IUsage: No arguments required.  Input file hard-coded.
# Output: Modified text file *v2.txt

import os

infile = 'data/cfactors.txt'
baseN = os.path.basename(infile)
outfile = 'scratch/' + os.path.splitext(baseN)[0] + 'v2.txt'
try:
    # OPEN the input and output files.
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            # READ/MODIFY/WRITE the first line.
            line = fin.readline()
            line = line.replace(' ', ',')
            fout.write(line)

            # FOR the remaining lines.
            for line in fin:
                # MODIFY the line.
                line = line.replace('=', ',')
                # WRITE to output.
                fout.write(line)
            print '{0} created.'.format(outfile)
except IOError:
    print "{0} doesn't exist.".format(infile)

```


```python

```

### 19.3.1 Pseudocode for Modifying Text Files

```
SET the input and output file name
IF the input file exists:
    OPEN the input and output files
    FOR EACH line in the input file
        MODIFY the line.
        WRITE the modi fied line to the output file.
    END FOR
    CLOSE the input and output files (automatic if WITH block is used).
    REPLACE original
ENDIF
```


```python

```

### 19.3.2 Working with Tabular Text

* **Example 19.5 removeHeader.py**


```python
# %load ch19/script2/removeHeader.py
# removeHeader.py
# Purpose: Remove header rows.
# Usage: No arguments required.  Input file hard-coded.
# Output: Modified text file *v2.txt

import os
headers = 2
infile = 'data/eyeTrack.csv'
baseN = os.path.basename(infile)
outfile = 'scratch/' + os.path.splitext(baseN)[0] \
          + 'v2.txt'
try:
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            # READ header lines, but don't write them.
            for i in range(headers):
                fin.readline()
            # READ and WRITE the remaining lines.
            for line in fin:
                fout.write(line)
            print '{0} created.'.format(outfile)
except IOError:
    print "{0} doesn't exist.".format(infile)

```

```
FOR each line in the input file:
    SPLIT the line (string to list)
    IF condition is TRUE THEN
        WRITE the string line to the output file.
    ENDIF
ENDFOR
```

## 19.4 Pickling

* **Example 19.6 Excerpt from sample script 'removeRecords.py'**


```python
import pickle
f = open('ch19/data/gherkin.txt', 'w')
pickle.dump(2.71828,f)
pickle.dump(['FireId', 'Org', 'FireType'],f)
f.close()
```


```python
f2 = open('ch19/data/gherkin.txt', 'r')
thing1 = pickle.load(f2)
thing1
```




    2.71828




```python
type(thing1)
```




    float




```python
thing2 = pickle.load(f2)
thing2
```




    ['FireId', 'Org', 'FireType']




```python
type(thing2)
```




    list




```python
f2.close()
```

## 19.5 Discussion

## 19.6 Key Terms
* The 'file'  data type
* The built-inopen function
* The fileread, readline, write,  and close methods
* The WITH statement for opening files
* The for line in f reading approach
* The IOError exception
* Current working directory vs.arcpy workspace
* Parse
* The open/read/parse/modify/write/close/replace workflow
* The shutil module
* The listpop method
* The pickle module

## 19.7 Exercises


```python

```
