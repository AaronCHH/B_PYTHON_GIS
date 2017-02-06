# extractFiles.py
# Purpose: Extract files from an archive;
#     Place the files into an output directory.
# Usage: No script arguments

import os, zipfile


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

archive = 'park.zip'
baseDir = 'C:/gispy/'
archiveFullName = baseDir + 'data/ch20/' + archive
destination = baseDir + 'scratch/' + os.path.splitext(archive)[0] + '/'
if not os.path.exists(destination):
    os.makedirs(destination)
unzipArchive(archiveFullName, destination)
