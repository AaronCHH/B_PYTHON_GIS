
# 3 Basic Data Types: Numbers and Strings

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [3 Basic Data Types: Numbers and Strings](#3-basic-data-types-numbers-and-strings)
  * [3.1 Numbers](#31-numbers)
  * [3.2 What Is a String?](#32-what-is-a-string)
  * [3.3 String Operations](#33-string-operations)
    * [3.3.1 Find the Length of Strings](#331-find-the-length-of-strings)
    * [3.3.2 Indexing into Strings](#332-indexing-into-strings)
    * [3.3.3 Slice Strings](#333-slice-strings)
    * [3.3.4 Concatenate Strings](#334-concatenate-strings)
    * [3.3.5 Check for Substring Membership](#335-check-for-substring-membership)
  * [3.4 More Things with Strings (a.k.a. String Methods)](#34-more-things-with-strings-aka-string-methods)
    * [**replace**](#replace)
    * [**split**](#split)
    * [**join**](#join)
    * [**endswith**](#endswith)
  * [3.5 File Paths and Raw Strings](#35-file-paths-and-raw-strings)
  * [3.6 Unicode Strings](#36-unicode-strings)
  * [3.7 Printing Strings and Numbers](#37-printing-strings-and-numbers)
    * [Commas](#commas)
    * [Concatenation](#concatenation)
    * [String formatting](#string-formatting)
  * [3.8 Key Terms](#38-key-terms)
  * [3.9 Exercises](#39-exercises)

<!-- tocstop -->

## 3.1 Numbers


```python
x = 2
y = 2.0
type(x)
```




    int




```python
type(y)
```




    float




```python
8/3
```




    2




```python
8.0/3
```




    2.6666666666666665



* **Table3.1**  

| Operation        | Operator | Example | Result |
|------------------|----------|---------|--------|
| Addition         |     +    |   7+2   |    9   |
| Subtraction      |     -    |   7-2   |    5   |
| Multiplication   |     *    |   7*2   |   14   |
| Division         |     /    |   7/2   |    3   |
| Exponentiation   |    **    |   7**2  |    9   |
| Modulus division |     %    |   7%2   |    1   |

## 3.2 What Is a String?


```python
inputData = 'trees.shp'
```


```python
inputData
```




    'trees.shp'




```python
print(inputData)
```

    trees.shp



```python
output = 'a b c
```


      File "<ipython-input-11-80aae2a16023>", line 1
        output = 'a b c
                      ^
    SyntaxError: EOL while scanning string literal




```python
output = """a b c
... d e f"""
print(output)
```

    a b c
    d e f



```python
output = 'a b c \
d e f \
g h i'
print(output)   
```

    a b c d e f g h i



```python
FID = 145
type(FID)
```




    int




```python
countyNum = '145'
type(countyNum)
```




    str



## 3.3 String Operations

### 3.3.1 Find the Length of Strings


```python
len('trees.shp')
```




    9




```python
data = 'trees.shp'
len(data)
```




    9



### 3.3.2 Indexing into Strings


```python
fieldName = 'COVER'
fieldName[0]
```




    'C'




```python
len(fieldName)
```




    5




```python
fieldName[5]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-22-98f469b91ffe> in <module>()
    ----> 1 fieldName[5]


    IndexError: string index out of range



```python
fieldName[4]
```




    'R'




```python
fieldName[-1]
```




    'R'




```python
fieldName[0] = 'D'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-f493e2e687d5> in <module>()
    ----> 1 fieldName[0] = 'D'


    TypeError: 'str' object does not support item assignment



```python
fieldName = 'DOVER'
```


```python
fieldName = fieldName.replace('C','D')
fieldName
```




    'DOVER'



### 3.3.3 Slice Strings


```python
fieldName = 'COVER'
fieldName[1:3]
```




    'OV'




```python
fieldName[:3]
```




    'COV'




```python
fieldName[1:]
```




    'OVER'




```python
inputData = 'trees.shp'
baseName = inputData[:-4]# Remove the file extension.
baseName
```




    'trees'



### 3.3.4 Concatenate Strings


```python
5 + 6# adding two numbers together
```




    11




```python
'5' + '6'# concatenating two strings
```




    '56'




```python
rasterName = 'NorthEast'
route = 'ATrain'
output = rasterName + route
output
```




    'NorthEastATrain'




```python
i = 1
rasterName = 'NorthEast'
output = rasterName + i
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-36-6dbbbff999cb> in <module>()
          1 i = 1
          2 rasterName = 'NorthEast'
    ----> 3 output = rasterName + i


    TypeError: cannot concatenate 'str' and 'int' objects



```python
i = 145
str(i)
```




    '145'




```python
rasterName = 'NorthEast'
output = rasterName + str(i)
output
```




    'NorthEast145'




```python
inputData = 'trees.shp'
baseName = inputData[:-4]
baseName
```




    'trees'




```python
outputData = baseName + '_buffer.shp'
outputData
```




    'trees_buffer.shp'



### 3.3.5 Check for Substring Membership


```python
substring = 'buff'
```


```python
substring in outputData
```




    True




```python
substring in inputData
```




    False



* **Exercise**


```python
exampleString = 'tuzigoot'
```


```python
len(exampleString)
```




    8




```python
exampleString[2]
```




    'z'




```python
exampleString[:-4]
```




    'tuzi'




```python
exampleString + exampleString
```




    'tuzigoottuzigoot'




```python
'ample' in exampleString
```




    False



## 3.4 More Things with Strings (a.k.a. String Methods)

### **replace**


```python
line = '238998,NPS,NERO,Northeast'
```


```python
line.replace(',' , ';')
```




    '238998;NPS;NERO;Northeast'




```python
line = '238998,NPS,NERO,Northeast'
line.replace(',' , ';')
line
```




    '238998,NPS,NERO,Northeast'




```python
line = '238998,NPS,NERO,Northeast'
semicolonLine = line.replace(',' , ';')
semicolonLine
```




    '238998;NPS;NERO;Northeast'




```python
line = line.replace(',' , ';')
line
```




    '238998;NPS;NERO;Northeast'




```python
name = 'Delaware Water Gap'
name = name.upper()
print name
```

    DELAWARE WATER GAP


### **split**


```python
path = 'C:/gispy/data/ch03/xy1.txt'
path.split('/')
```




    ['C:', 'gispy', 'data', 'ch03', 'xy1.txt']



### **join**


```python
numList = ['1', '2', '3']
animal = 'elephant'
animal.join(numList)
```




    '1elephant2elephant3'




```python
pathList = ['C:', 'gispy', 'data', 'ch03', 'xy1.txt']
';'.join(pathList)
```




    'C:;gispy;data;ch03;xy1.txt'



### **endswith**


```python
path = 'C:/gispy/data/ch03/xy1.txt'
path.endswith('.shp')
```




    False




```python
path.endswith('.txt')
```




    True



Help documentation and a comprehensive list of string methods is available online (search for **'Python String Methods'**).  
String method names are often intuitive.  
Testing them in the Interactive Window helps to clarify their functionality  

## 3.5 File Paths and Raw Strings


```python
'X\tY\tValue\n\n16\t255\t6.3'
```




    'X\tY\tValue\n\n16\t255\t6.3'




```python
print'X\tY\tValue\n\n16\t255\t6.3'
```

    X	Y	Value

    16	255	6.3



```python
dataRecord = ' \n\t\tX\tY\tZ\tM\t'
print dataRecord
```


    		X	Y	Z	M



```python
dataRecord = dataRecord.strip()
dataRecord
```




    'X\tY\tZ\tM'




```python
print dataRecord
```

    X	Y	Z	M


**Escape sequences can lead to unintended consequences with fi le paths that con tain backslashes.  
In this example, thet in terrain and then inneuse are replaced by whitespace when the string is printed:**


```python
dataPath = 'C:\terrain\neuse_river'
dataPath
```




    'C:\terrain\neuse_river'




```python
print dataPath
```

    C:	errain
    euse_river


**Here are three options for avoiding this problem:**


```python
dataPath = 'C:/terrain/neuse_river'
print dataPath
```

    C:/terrain/neuse_river



```python
dataPath = 'C:\\terrain\\neuse_river'
print dataPath
```

    C:\terrain\neuse_river



```python
dataPath = r'C:\terrain\neuse_river'
print dataPath
```

    C:\terrain\neuse_river


## 3.6 Unicode Strings

**When you start using ArcGIS functionality in Chapter 6 , you will begin to see a lowercase u preceding strings that are returned by GIS methods.  
The u stands for unicode string.  
Aunicode string is a specially encoded string that can represent thousands of characters, so that non-English characters, such as the Hindi alphabet can be represented.  
A unicode string is created by prepending a u to a string literal, as shown here:**  



```python
dataFile = u'counties.shp'
dataFile
```




    u'counties.shp'




```python
type(dataFile)
```




    unicode




```python
dataFile.endswith('.shp')# Does the string end with '.shp'?
```




    True




```python
dataFile.startswith('co')# Does the string start with 'co'?
```




    True




```python
dataFile.count('s')# How many times does 's' occur in the string?
```




    2




```python
dataFile.upper()# Return an all caps. string.
```




    u'COUNTIES.SHP'




```python
dataFile[5]# Index the 6th character in the string.
```




    u'i'




```python
dataFile + dataFile# Concatenate two strings
```




    u'counties.shpcounties.shp'




```python
print dataFile
```

    counties.shp


## 3.7 Printing Strings and Numbers

### Commas


```python
dataFile = 'counties.shp'
FID = 862
print dataFile, FID
```

    counties.shp 862



```python
print 'The first FID in', dataFile, 'is', FID, '!'
```

    The first FID in counties.shp is 862 !


### Concatenation


```python
print 'The first FID in' + dataFile + 'is' + FID + '!'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-94-0fd3abbbea07> in <module>()
    ----> 1 print 'The first FID in' + dataFile + 'is' + FID + '!'


    TypeError: cannot concatenate 'str' and 'int' objects



```python
print 'The first FID in' + dataFile + 'is' + str(FID) + '!'
```

    The first FID incounties.shpis862!



```python
print 'The first FID in ' + dataFile + ' is ' + str(FID) + '!'
```

    The first FID in counties.shp is 862!


### String formatting


```python
print 'The first FID in {0} is {1}!'.format(dataFile, FID)
```

    The first FID in counties.shp is 862!



```python
print '''X Y Value
... -------------------
... {0} {1} {2}'''.format(16, 255, 6.3)
```

    X Y Value
    -------------------
    16 255 6.3


## 3.8 Key Terms

| int data type        | Casting               |
|----------------------|-----------------------|
| float data type      | Thein keyword         |
| Integer division     | Dot notation          |
| str data type        | Objects               |
| String literal       | Methods               |
| String variable      | Context menus         |
| Line continuation    | Whitespace characters |
| Zero-based indexing  | Escape sequences      |
| Built-inlen function | Raw strings           |
| Slicing              | Unicode strings       |
| Concatenating        | String formatting     |

## 3.9 Exercises


```python

```
