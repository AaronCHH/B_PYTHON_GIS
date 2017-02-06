# writeSimpleHTML2.py
# Purpose: Write HTML page in 3 parts.
# Usage: workspace title image_path
# Example input: C:/gispy/scratch "Asian Elephant" ../data/ch20/pics/lakshmi.jpg
import sys
workspace = sys.argv[1]
title = sys.argv[2]
image = sys.argv[3]

beginning = '''<!DOCTYPE html>
<html>
    <body>'''

middle = '''
        <h1>{0}</h1>
        <img src='{1}' >\n'''.format(title, image)

end = '''   </body>
</html>
'''

htmlfile = workspace + '/output2.html'
with open(htmlfile, 'w') as outf:
    outf.write(beginning)
    outf.write(middle)
    outf.write(end)

print '{0} created.'.format(htmlfile)
