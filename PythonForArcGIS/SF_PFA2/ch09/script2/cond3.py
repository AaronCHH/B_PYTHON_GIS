# cond3.py
# Purpose:  Check if the input file exists and has a txt extension.
# Usage: full_path_filename
# Input example 1:  C:/gispy/data/ch09/xy1.txt
# Input example 2:  C:/gispy/data/ch09/park.shp
# Input example 3:  C:/gispy/data/ch09/bogus.txt

import os, sys

inputName = sys.argv[1]

if os.path.exists(inputName):
    if inputName.endswith('.txt'):
        print 'The following text file exists: {0}'.format(inputName)
