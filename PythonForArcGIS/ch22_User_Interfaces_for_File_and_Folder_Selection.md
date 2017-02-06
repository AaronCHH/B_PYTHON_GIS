
# 22 User Interfaces for File and Folder Selection

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [22 User Interfaces for File and Folder Selection](#22-user-interfaces-for-file-and-folder-selection)
  * [22.1 A Simple Interface with raw_input](#221-a-simple-interface-with-raw_input)
  * [22.2 File Handling with tkFileDialog](#222-file-handling-with-tkfiledialog)
    * [22.2.1 Getting File and Directory Names](#2221-getting-file-and-directory-names)
    * [22.2.2 Options](#2222-options)
      * [22.2.2.1 File-Handling Options](#22221-file-handling-options)
      * [22.2.2.2 Close the Tk Window](#22222-close-the-tk-window)
    * [askAndDestroy.py](#askanddestroypy)
    * [22.2.3 Opening Files for Reading and Writing](#2223-opening-files-for-reading-and-writing)
  * [22.3 Discussion](#223-discussion)
  * [22.4 Key Terms](#224-key-terms)
  * [22.5 Exercises](#225-exercises)

<!-- tocstop -->

## 22.1 A Simple Interface with raw_input

* **Example 22.1 askWorkspaceRaw.py**  


```python
# %load ch22/script2/askWorkspaceRaw.py
# askWorkspaceRaw.py
# Purpose: Get a workspace with the raw_input function.
# Usage: No script arguments needed.
# raw_input DOES NOT restrict the user to valid workspaces.
# Use tkFileDialog askDirectory or a script tool instead.
import arcpy
arcpy.env.workspace = raw_input('Enter a workspace:')
print arcpy.env.workspace

```

## 22.2 File Handling with tkFileDialog


```python

```

### 22.2.1 Getting File and Directory Names

* **Example 22.2 getFileName.py**  


```python
# %load ch22/script2/getFileName.py
# getFileName.py
# Purpose: Get a shapefile name from the user and print the shapeType.
# Usage: No script arguments required.
import tkFileDialog, arcpy, Tkinter
fatherWilliam = Tkinter.Tk()
fatherWilliam.withdraw()
fc = tkFileDialog.askopenfilename(
    filetypes=[("shapefiles", "*.shp")],
    title='Choose a SHAPEFILE that defines the STATISTICAL ZONES',
    parent=fatherWilliam)
print 'fc = {0}'.format(fc)
desc = arcpy.Describe(fc)
print 'Shape type = {0}'.format(desc.ShapeType)
fatherWilliam.destroy()

```

* **Example 22.3: askdirectory askDirectory.py**  


```python
# %load ch22/script2/askdirectory.py
# askDirectory.py
# Purpose: Get a directory from the user and set the workspace.
# Usage: No script arguments required.
import tkFileDialog, arcpy

arcpy.env.workspace = tkFileDialog.askdirectory(initialdir="./",
                                                title='Select the FOLDER containing Landuse RASTERS')

print 'Workspace = {0}'.format(arcpy.env.workspace)

```


```python

```

### 22.2.2 Options

#### 22.2.2.1 File-Handling Options

**File Types**


```python
t = ('shape files','*.shp')
fname1 = tkFileDialog.askopenfilename(filetypes=[t])
```


```python
fname2 = tkFileDialog.askopen filename(
    filetypes=[('csv (Comma delimited)','*.csv'),
               ('Text Files','*.txt')])
```

**Initial Directory**


```python
fname3 = tkFileDialog.askopen filename(initialdir = 'C:/gispy')
```


      File "<ipython-input-6-5dccb1b52486>", line 1
        fname3 = tkFileDialog.askopen filename(initialdir = 'C:/gispy')
                                             ^
    SyntaxError: invalid syntax



**Initial File**


```python
fname4 = tkFileDialog.askopen filename(initial file = 'bogus.shp')
```

**Multiple Files**

* **Example 22.4 excerpt from fileDialogOptions.py**  


```python
# %load ch22/script2/fileDialogOptions.py
# fileDialogOptions.py
# Purpose: Vary file dialog options to get file and directory
#          names from user and print the results.
# Usage: No script arguments required.
import tkFileDialog

t = ("shapefiles ", "*.shp")
print 'Type = {0}'.format(type(t))

fname1 = tkFileDialog.askopenfilename(filetypes=[t])
print 'fname1 = {0}'.format(fname1)

fname2 = tkFileDialog.askopenfilename(title='Test 2 filetypes',
                                      filetypes=[("csv (Comma delimited) ", "*.csv"),("Text Files ", "*.txt")])
print 'fname2 = {0}'.format(fname2)

fname3 = tkFileDialog.askopenfilename(title='Test initialdir', initialdir='C:/gispy')

print 'fname3 = {0}'.format(fname3)

fname4 = tkFileDialog.askopenfilename(title='Test initialfile', initialfile='bogus.shp')

print 'fname4 = {0}'.format(fname4)

fnames = tkFileDialog.askopenfilename(title='Test multiple selections allowed', multiple=True)
files = fnames.split()
print 'Name list:'
for fname in files:  # For each file selected by the user,...
    print '   {0}'.format(fname)

inputDir = tkFileDialog.askdirectory(title='Test mustexist =True', mustexist=True)
print 'inputDir = {0}'.format(inputDir)

```


```python
inputDir = tkFileDialog.askdirectory(mustexist = True)
```

#### 22.2.2.2 Close the Tk Window


```python
import tkFileDialog, Tkinter
tkObj = Tkinter.Tk()
inputDir = tkFileDialog.askdirectory(parent=tkObj)
tkObj.destroy()
```

### askAndDestroy.py


```python
# %load ch22/script2/askAndDestroy.py
# askAndDestroy.py
# Purpose: Get a directory from the user and suppress the root Tk window.
# Usage: No script arguments required

import tkFileDialog, Tkinter
# Get a tk object.
fatherWilliam = Tkinter.Tk()

# Hide the tk window.
fatherWilliam.withdraw()

inputDir = tkFileDialog.askopenfilename(parent=fatherWilliam)

# Destroy the tk window.
fatherWilliam.destroy()

```


```python

```

### 22.2.3 Opening Files for Reading and Writing


```python
fobject = tkFileDialog.askopen file(
    filetypes=[('shape files','*.shp')],
    initial file='data.txt', title='Open a data file...')
firstLine = fobject.readline()
fobject.close()
```


```python
myTitle = 'Select an output file name'
with tkFileDialog.asksaveas file(title=myTitle)aso file:
    o file.write('I like tkFileDialog')
```

## 22.3 Discussion


```python

```

## 22.4 Key Terms

## 22.5 Exercises
