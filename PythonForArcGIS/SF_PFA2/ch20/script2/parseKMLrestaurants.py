# parseKMLrestaurants.py
# Purpose: Print kml placemark names and descriptions.
import sys

baseDir = ''
sys.path.append(baseDir + 'script')
import BeautifulSoup

fileName = baseDir + 'data/restaurants.kml'

# Get the KML soup.
with open(fileName, 'r') as kmlCode:
    soup = BeautifulSoup.BeautifulSoup(kmlCode)

# Print the names and descriptions.
names = soup.findAll('name')
descriptions = soup.findAll('description')
for name, description in zip(names, descriptions):
    print name.contents[0]
    print '\t{0}'.format(description.contents)
