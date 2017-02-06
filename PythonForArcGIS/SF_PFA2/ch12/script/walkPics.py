# walkPics.py
# Purpose: Demostrate the 'os.walk' function.
import os
myDir = 'C:/gispy/data/ch12/pics'
for root, dirs, files in os.walk(myDir):
    print 'root = {0}'.format(root)
    print 'dirs = {0}'.format(dirs)
    print 'files = {0}\n'.format(files)
