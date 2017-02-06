# listingDir.py
# Purpose: Print the files in a directory.
import os
theDir = "C:/gispy/data/ch10/pics"
# os.listdir returns a list of the files (and directories in the input directory)
theFiles = os.listdir(theDir)
print theFiles
