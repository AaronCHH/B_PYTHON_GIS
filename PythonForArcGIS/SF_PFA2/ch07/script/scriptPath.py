# scriptPath.py
# Purpose: List the files in the current directory.
# Usage: No user arguments needed.

import os

# Get the script location
scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)

# Print the contents of the script directory
print '{0} contains the following files:'.format(scriptDir)
print os.listdir(scriptDir)
