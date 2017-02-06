# fileDates.py
# Purpose: Collect filenames and modification dates in a dictionary.
# Usage: No arguments needed.
import os, time

inputDir = 'data/smallDir'

fileList = os.listdir(inputDir)

fileDict = {}
for f in fileList:
    epochNum = os.path.getmtime(inputDir + '/' + f)
    modTime = time.ctime(epochNum)
    fileDict[f] = modTime

print fileDict
