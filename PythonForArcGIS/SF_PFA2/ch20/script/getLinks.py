# getLinks.py
# Purpose: Read and print the links in an html file.

import sys
basedir = 'C:/gispy/'
sys.path.append(basedir + 'sample_scripts/ch20')
import BeautifulSoup

# Read the HTML file contents.
with open(basedir + 'data/ch20/htmlExamplePages/elephant2.html', 'r') as infile:

    # Create a soup object and find all the hyperlinks.
    soup = BeautifulSoup.BeautifulSoup(infile)
    linkTags = soup.findAll('a')

    # Print each hyperlink reference.
    for linkTag in linkTags:
        print 'Link: {0}'.format(linkTag['href'])
