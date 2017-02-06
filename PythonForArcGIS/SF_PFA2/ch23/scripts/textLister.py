# textLister.py
# Purpose: Print the text file (.txt) names in the directory.
# Usage: No arguments required.
import arcpy, os
myDir = r'C:\gispy\data\ch23\smallDir'

fileList = os.listdir(myDir)
for f in fileList:
    if f.endswith(".txt"):
        print f
arcpy.AddMessage('And I like pie!')
