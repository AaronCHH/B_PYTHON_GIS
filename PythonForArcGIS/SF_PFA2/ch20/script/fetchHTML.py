# fetchHTML.py
# Fetch HTML from a site and print the number of lines in the HTML
import urllib2

url = 'http://www.google.com'
response = urllib2.urlopen(url)
contents = response.read()
response.close()
print 'This page has {0} characters.'.format(len(contents))
