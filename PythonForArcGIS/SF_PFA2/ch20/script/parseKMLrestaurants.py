# parseKMLrestaurants.py
# Purpose: Print kml placemark names and descriptions.
import sys

baseDir = 'C:/gispy/'
sys.path.append(baseDir + 'sample_scripts/ch20')
import BeautifulSoup

fileName = baseDir + 'data/ch20/restaurants.kml'

# Get the KML soup.
with open(fileName, 'r') as kmlCode:
    soup = BeautifulSoup.BeautifulSoup(kmlCode)

# Print the names and descriptions.
names = soup.findAll('name')
descriptions = soup.findAll('description')
for name, description in zip(names, descriptions):
    print name.contents[0]
    print '\t{0}'.format(description.contents)
