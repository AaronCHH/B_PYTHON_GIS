# printModTime.py
# Purpose: For each file, print the time of most recent modification.
# Input:   No arguments required.

import os, datetime

theDir = "data/pics"
theFiles = os.listdir(theDir)
for f in theFiles:
    fullName = os.path.join(theDir, f)
    # Get the modification time.
    print os.path.getmtime(fullName)



##import os, datetime  #(this version provides fancier formatting)
##
##theDir = "C:/gispy/data/ch10/pics"
##theFiles = os.listdir(theDir)
##for f in theFiles:
##	fullName = os.path.join(theDir, f)
##	# Get the modification time.
##	modTime = os.path.getmtime(fullName)
##	# Convert Epoch time to a time stamp.
##	theDate = datetime.datetime.fromtimestamp(modTime)
##	# Reformat the time stamp
##	print theDate.strftime("%m/%d/%Y %H:%M:%S")
