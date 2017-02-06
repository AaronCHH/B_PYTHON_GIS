# writeUniqueValuesHTML.py
# Purpose: Write an HTML file with a list of distinct values in a field.
# Usage: No arguments required.

import arcpy, os, listManager4
baseDir = 'C:/gispy/'
fc = 'data/ch20/park.shp'
fcBase = os.path.basename(fc)
fieldname = 'COVER'
image = '../data/ch20/pics/park.png'

### Get all values for the given field, using a search cursor

### Get unique values for the given field, using a listManager4.py function

### Get an HTML bulleted list of the unique values, using a listManager4.py function

### Create HTML body with HTML bulleted list and embedded image

# Create header with dynamic title.
beginning = """<!DOCTYPE html>
<html>
 <body>
  <h1> Unique values in {0} field {1}: </h1>
""".format(fcBase, fieldname)

# Create footer to close body and html tags.
end = """
 </body>
</html>
"""
outfile = baseDir + '/scratch/DataReport.html'
outf = open(outfile, 'w')
outf.write(beginning)
### Write the body to the output file
outf.close()
print '{0} created.'.format(outfile)
