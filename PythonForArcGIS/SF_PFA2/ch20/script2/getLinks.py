# getLinks.py
# Purpose: Read and print the links in an html file.

import sys
basedir = ''
sys.path.append(basedir + 'data/script')
import BeautifulSoup

# Read the HTML file contents.
with open(basedir + 'data/htmlExamplePages/elephant2.html', 'r') as infile:

    # Create a soup object and find all the hyperlinks.
    soup = BeautifulSoup.BeautifulSoup(infile)
    linkTags = soup.findAll('a')

    # Print each hyperlink reference.
    for linkTag in linkTags:
        print 'Link: {0}'.format(linkTag['href'])
