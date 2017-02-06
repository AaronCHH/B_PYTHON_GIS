# writeSimpleHTML.py
# Purpose: Write HTML page from hard-coded string.
# Usage: No arguments needed.

mystr = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Asian Elephant</h1>
        <img src="../data/ch20/pics/lakshmi.jpg" alt="elephant">
    </body>
</html>
'''
htmlFile = 'C:/gispy/scratch/output.html'
outf = open(htmlFile, 'w')
outf.write(mystr)
outf.close()
print '{0} created.'.format(htmlFile)
