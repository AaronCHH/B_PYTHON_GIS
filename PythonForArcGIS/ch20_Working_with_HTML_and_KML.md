
# 20 Working with HTML and KML

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [20 Working with HTML and KML](#20-working-with-html-and-kml)
  * [20.1 Working with HTML](#201-working-with-html)
    * [20.1.1 Specifying Links](#2011-specifying-links)
    * [20.1.2 Embedding Images](#2012-embedding-images)
    * [20.1.3 HTML Lists](#2013-html-lists)
    * [20.1.4 HTML Tables](#2014-html-tables)
    * [20.1.5 Writing HTML with Python](#2015-writing-html-with-python)
    * [20.1.6 Parsing HTML with BeautifulSoup](#2016-parsing-html-with-beautifulsoup)
  * [20.2 Fetching and Uncompressing Data](#202-fetching-and-uncompressing-data)
    * [20.2.1 Fetching HTML](#2021-fetching-html)
    * [fetchHTML.py import urllib2](#fetchhtmlpy-import-urllib2)
    * [20.2.2 Fetching Compressed Data](#2022-fetching-compressed-data)
    * [20.2.3 Expanding Compressed Data](#2023-expanding-compressed-data)
  * [20.3 Working with KML](#203-working-with-kml)
    * [20.3.1 The Structure of KML](#2031-the-structure-of-kml)
    * [20.3.2 Parsing KML](#2032-parsing-kml)
    * [20.3.3 Converting KML to Shapefile](#2033-converting-kml-to-shapefile)
  * [20.4 Discussion](#204-discussion)
  * [20.5 Key Terms](#205-key-terms)
  * [20.6 Exercises](#206-exercises)

<!-- tocstop -->

## 20.1 Working with HTML

* **Example 20.1: HTML code from the file elephant1.html**


```python
# %load ch20/data/htmlExamplePages/elephant1.html
<!DOCTYPE html>
<html>
<body bgcolor="Aquamarine">
<!-- blablabla -->
<h1>Elephants Say</h1>
<p> We <b>like</b> HTML.</p>
We <i>love</i> Python <br /> and GIS.
</body>
</html>
```

### 20.1.1 Specifying Links

```html
<a href="elephant1.html">A link</a>
```

### 20.1.2 Embedding Images

```html
<img src="../pics/lakshmi.jpg" width="32" height="32">
```

### 20.1.3 HTML Lists

```html
<ol>
    <li>Savannah</li>
    <li>Bush</li>
    <li>African</li>
</ol>
```

### 20.1.4 HTML Tables

```html
<table border="3">
    <tr>
        <th>Species</th>
        <th>2011 Population</th>
    </tr>
    <tr>
        <td>African</td>
        <td>Less than 690000</td>
    </tr>
    <tr>
        <td>Asian</td>
        <td>Less than 32700</td>
    </tr>
</table>
```

### 20.1.5 Writing HTML with Python

* **Example 20.2 writeSimpleHTML.py**


```python
# %load ch20/script2/writeSimpleHTML.py
# writeSimpleHTML.py
# Purpose: Write HTML page from hard-coded string.
# Usage: No arguments needed.

mystr = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Asian Elephant</h1>
        <img src="../data/ch20/pics/lakshmi.jpg" alt="elephant">
    </body>
</html>
'''
htmlFile = 'scratch/output.html'
outf = open(htmlFile, 'w')
outf.write(mystr)
outf.close()
print '{0} created.'.format(htmlFile)

```

* **Example 20.3 writeSimpleHTML2.py**


```python
# %load ch20/script2/writeSimpleHTML2.py
# writeSimpleHTML2.py
# Purpose: Write HTML page in 3 parts.
# Usage: workspace title image_path
# Example input: C:/gispy/scratch "Asian Elephant" ../data/ch20/pics/lakshmi.jpg
import sys
workspace = sys.argv[1]
title = sys.argv[2]
image = sys.argv[3]

beginning = '''<!DOCTYPE html>
<html>
    <body>'''

middle = '''
        <h1>{0}</h1>
        <img src='{1}' >\n'''.format(title, image)

end = '''   </body>
</html>
'''

htmlfile = workspace + '/output2.html'
with open(htmlfile, 'w') as outf:
    outf.write(beginning)
    outf.write(middle)
    outf.write(end)

print '{0} created.'.format(htmlfile)

```

* **Example 20.4 excerpt from printHTMLList.py**


```python
# %load ch20/script2/printHTMLList.py
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

```


```python

```

### 20.1.6 Parsing HTML with BeautifulSoup

```python
import sys
sys.path.append('ch20/sample_scripts')
import BeautifulSoup
```


```python
import BeautifulSoup
mystr = '<!DOCTYPE html><html><body><h1>Asian Elephant</h1><img src="lakshmi.jpg" alt="elephant"></body></html>'
```


```python
soup = BeautifulSoup.BeautifulSoup(mystr)
```


```python
h = soup.prettify()
print h
```

    <!DOCTYPE html>
    <html>
     <body>
      <h1>
       Asian Elephant
      </h1>
      <img src="lakshmi.jpg" alt="elephant" />
     </body>
    </html>



```python
t = soup. find('h1')
t
```




    <h1>Asian Elephant</h1>




```python
t = soup.find('h1')
t
```


```python
type(t)
```


```python
t.name
```


```python
t.attrs
```


```python
t.contents
```


```python
t.contents[0]
```


```python
t2 = soup.find('img')
t2
```


```python
t2.attrs
```


```python
t2['src']
```


```python
t2['alt']
```


```python
for name, value in t2.attrs:
    print 'Name: ' + name + ' Value: ' + value
```


```python
htmlList = '\n <ul>\n <li>elev</li>\n <li>landcov</li>\n<li>soilsid</li>\n <li>getty_cover</li>\n </ul>\n'
soup2 = BeautifulSoup.BeautifulSoup(htmlList)
tags = soup2.findAll('li')
tags
```




    [<li>elev</li>, <li>landcov</li>, <li>soilsid</li>, <li>getty_cover</li>]




```python
for t in tags:
    print t.contents[0]
```

    elev
    landcov
    soilsid
    getty_cover


* **Example 20.5 getLinks.py**


```python
# %load ch20/script2/getLinks.py
# getLinks.py
# Purpose: Read and print the links in an html file.

import sys
basedir = ''
sys.path.append(basedir + 'data/script')
import BeautifulSoup

# Read the HTML file contents.
with open(basedir + 'data/htmlExamplePages/elephant2.html', 'r') as infile:

    # Create a soup object and find all the hyperlinks.
    soup = BeautifulSoup.BeautifulSoup(infile)
    linkTags = soup.findAll('a')

    # Print each hyperlink reference.
    for linkTag in linkTags:
        print 'Link: {0}'.format(linkTag['href'])

```

## 20.2 Fetching and Uncompressing Data


```python

```

### 20.2.1 Fetching HTML

### fetchHTML.py import urllib2


```python
# %load ch20/script2/fetchHTML.py
# fetchHTML.py
# Fetch HTML from a site and print the number of lines in the HTML
import urllib2

url = 'http://www.google.com'
response = urllib2.urlopen(url)
contents = response.read()
response.close()
print 'This page has {0} characters.'.format(len(contents))

```


```python
%run ch20/script2/fetchHTML.py
```

    This page has 10410 characters.



```python
pics = soup.findAll('img')
```


```python
pics
```




    [<img src="lakshmi.jpg" alt="elephant" />]



### 20.2.2 Fetching Compressed Data

* **Example 20.6 fetchZip.py**


```python
# %load ch20/script2/fetchZip.py
# fetchZip.py
# Purpose: Fetch a zip file and place it in an output directory.
import os, urllib2


def fetchZip(url, outputDir):
    '''Fetch binary web content located at 'url'
    and write it in the output directory'''
    response = urllib2.urlopen(url)
    binContents = response.read()
    response.close()

    # Save zip file to output dir (write it in 'wb' mode).
    outFileName = outputDir + os.path.basename(url)
    with open(outFileName, 'wb') as outf:
        outf.write(binContents)

outputDir = 'scratch/'
theURL = 'file:///D:/BOOKS/GISen/_PYTHON/PythonForArcGIS/SF_PFA/ch20/data/getty.zip'
fetchZip(theURL, outputDir)
print '{0}{1} created.'.format(outputDir, os.path.basename(theURL))

```

### 20.2.3 Expanding Compressed Data

* **Example 20.7 extractFiles.py**


```python
# %load ch20/script2/extractFiles.py
# extractFiles.py
# Purpose: Extract files from an archive;
#     Place the files into an output directory.
# Usage: No script arguments

import os, zipfile


def unzipArchive(archiveName, dest):
    '''Extract files from an archive
    and save them in the destination directory'''
    print 'Unzip {0} to {1}'.format(archiveName, dest)
    # Get a Zipfile object.
    with zipfile.ZipFile(archiveName, 'r') as zipObj:
        zipObj.extractall(dest)
        # Report the list of files extracted from the archive.
        archiveList = zipObj.namelist()
        for fileName in archiveList:
            print ' Extract file: {0} ...'.format(fileName)
    print 'Extraction complete.'

archive = 'park.zip'
baseDir = ''
archiveFullName = baseDir + 'data/' + archive
destination = baseDir + 'scratch/' + os.path.splitext(archive)[0] + '/'
if not os.path.exists(destination):
    os.makedirs(destination)
unzipArchive(archiveFullName, destination)

```

```
FETCH the data download page.
CREATE a soup object.
GET a list of the links in the data download page.
FOR each link
    IF the link references a Zip file THEN
        CALL fetchZip to fetch the Zip file, saving it locally.
        CALL unzipArchive to extract the compressed files.
    ENDIF
ENDFOR
```

## 20.3 Working with KML


```python

```

### 20.3.1 The Structure of KML

* **Example 20.8: KML code from the restaurants.kml file**

```html
<?xml version="1.0" encoding="UTF-8"?>

<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
    <Placemark>
       <name>Bubba's Tofu Gumbo</name>
       <description>Tofu Gumbo and Zydeco!<br />Score: 97</description>
       <Point>
          <coordinates>-90,30,0</coordinates>
       </Point>
    </Placemark>

    <Placemark>
       <name>Joe Bob's Good Cookin'</name>
       <description>The best tree top grits n' greens restaurant south of the Mason-Dixon line.<br />Score: 94</description>
       <Point>
          <coordinates>-78,35,0</coordinates>
       </Point>
    </Placemark>
    </Document>
</kml>
```

### 20.3.2 Parsing KML

* **Example 20.9 parseKMLrestaurants.py**


```python
# %load ch20/script2/parseKMLrestaurants.py
# parseKMLrestaurants.py
# Purpose: Print kml placemark names and descriptions.
import sys

baseDir = ''
sys.path.append(baseDir + 'script')
import BeautifulSoup

fileName = baseDir + 'data/restaurants.kml'

# Get the KML soup.
with open(fileName, 'r') as kmlCode:
    soup = BeautifulSoup.BeautifulSoup(kmlCode)

# Print the names and descriptions.
names = soup.findAll('name')
descriptions = soup.findAll('description')
for name, description in zip(names, descriptions):
    print name.contents[0]
    print '\t{0}'.format(description.contents)

```

### 20.3.3 Converting KML to Shapefile

```
CALL the Create Feature Class (Data Management) tool
SET the field names and types
FOR each field name
    CALL the Add Field (Data Management) tool
ENDFOR
CREATE a soup object from the KML file contents
GET tag lists from the soup ( findAll)
CREATE an insert cursor
FOR each item in the tag lists
    GET the value for each field
    PUT field values in a list
    INSERT the new row into the shape file
ENDFOR
```

* **Example 20.10 Excerpt from restaurantKML2shp.py**


```python
# %load ch20/script2/restaurantKML2shp.py
# restaurantKML2shp.py
# Purpose: Create a shapefile from a kml file using an insert cursor.
# Usage: kml_directory output_directory
# Example input: C:/gispy/data/ch20 C:/gispy/scratch/

import arcpy, os, sys, BeautifulSoup

dataDir = sys.argv[1]
outDir = sys.argv[2]
arcpy.env.workspace = outDir
kmlFile = 'restaurants.kml'
kmlPath = os.path.join(dataDir, kmlFile)
baseName = os.path.splitext(kmlFile)[0]
fc = baseName + '.shp'

fieldNames = ['name', 'blurb', 'score']
fieldTypes = ['TEXT', 'TEXT', 'FLOAT']

# If the shapefile already been created, delete it.
if arcpy.Exists(fc):
    arcpy.Delete_management(fc)

sr = arcpy.SpatialReference('NAD 1983 UTM Zone 17N')
arcpy.CreateFeatureclass_management(outDir, fc, 'POINT', '#', '#', '#', sr)
for field, type in zip(fieldNames, fieldTypes):
    arcpy.AddField_management(fc, field, type)

# Get the tag soup.
with open(kmlPath, 'r') as kmlCode:
    soup = BeautifulSoup.BeautifulSoup(kmlCode)
coordinates = soup.findAll('coordinates')
names = soup.findAll('name')
descriptions = soup.findAll('description')

# Populate the shapefile.
with arcpy.da.InsertCursor(fc, ['SHAPE@XY'] + fieldNames) as ic:
    for c, n, d in zip(coordinates, names, descriptions):
        # Get field values.
        [x, y, z] = c.contents[0].split(',')
        myPoint = arcpy.Point(x, y)
        name = n.contents[0]
        blurb = d.contents[0]
        scoreString = d.contents[2]
        scoreList = scoreString.split(':')
        score = float(scoreList[1])
        # Put row values in a list & insert the new row.
        newRow = [myPoint, name, blurb, score]
        ic.insertRow(newRow)
print '{0}{1} created.'.format(outDir, fc)
if ic:
    del ic
```

## 20.4 Discussion

## 20.5 Key Terms
* HTML
* KML
* HTML lists
* HTML tables
* Tags
* Start tag and end tag
* Tag content
* Tag attributes
* Wrapped tags
* Beginning and ending tags
* Fetch  
* URL
* Compressed file
* Binary file
* TheBeautifulSoup module

## 20.6 Exercises


```python

```
