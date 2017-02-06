# wakeURL.py
# Usage: One required argument, the data download page url
# Example: http://www.wakegov.com/gis/services/Pages/data.aspx
# Note: The above URL may change. Search online for 'Data download Wake GIS'

### Add imports as needed


def fetchZip(url, outputDir):
    '''Fetch binary web content located at 'url'
    and write it in the output directory'''
    response = urllib2.urlopen(url)
    binContents = response.read()
    response.close()

    # Save zip file to output dir (write it in 'wb' mode).
    outFileName = outputDir + os.path.basename(url)
    with open(outFileName, 'wb') as outf:
        outf.write(binContents)


def unzipArchive(archiveName, dest):
    '''Extract files from an archive
    and save them in the destination directory'''
    print 'Unzip {0} to {1}'.format(archiveName, dest)
    # Get a Zipfile object.
    with zipfile.ZipFile(archiveName, 'r') as zipObj:
        zipObj.extractall(dest)
        # Report the list of files extracted from the archive.
        archiveList = zipObj.namelist()
        for fileName in archiveList:
            print ' Extract file: {0} ...'.format(fileName)
    print 'Extraction complete.'

# Fetch HTML from a data download website.
url = sys.argv[1] 
workingDir = sys.argv[2]
response = urllib2.urlopen(url)
html = response.read()
response.close()

# Parse hyperlinks in Data Download page.
soup = BeautifulSoup.BeautifulSoup(html)
tags = soup.findAll('a', href=True)

### Loop through the link tags.

    ### GET the tag's hyperlink reference (href).

    ### IF the string 'Streets' is in the link and the link ends with '.zip'.

        ### Fetch the Zip file and unzip it.
