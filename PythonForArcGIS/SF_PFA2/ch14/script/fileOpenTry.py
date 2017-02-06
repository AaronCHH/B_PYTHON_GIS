# fileopenTry.py
# Purpose: Open and read the contents of an ASCII file.
# Usage: fullpath_filename
# Example input1: C:/gispy/data/ch14/cover.prj
# Example input2: C:/gispy/data/ch14/dummyFile.prj
import sys

# Get a full path filename from the user 
filename = sys.argv[1]

# Open user-input file for reading
### put this inside a TRY block
file = open(filename,"r") 
### Insert a named EXCEPT block.
### Inside the block print the warning and then call the system exit function,
###     so that it doesn't reach the code below if an exception has occurred.

### No need to modify below this line.
    
# Read in the entire file and print the file contents 
contents = file.readlines()
for line in contents:
    print line
file.close()
    