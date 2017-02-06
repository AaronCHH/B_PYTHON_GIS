# copyFilev2.py
# Purpose: Copy a file.
# Usage: source_directory destination_directory file_to_backup
# Example: C:/gispy/data/ch09/ C:/gispy/scratch/backup park.shp
# The example works even if the C:/gispy/scratch/backup 
#    directory doesn't exist yet.

import arcpy, os

arcpy.env.workspace = arcpy.GetParameterAsText(0)
outputDir = arcpy.GetParameterAsText(1)
fileToCopy = arcpy.GetParameterAsText(2)

if not os.path.exists(outputDir):
    os.mkdir(outputDir)

outputFile = os.path.join(outputDir, fileToCopy)
arcpy.Copy_management(fileToCopy, outputFile)

print 'source =', os.path.join(arcpy.env.workspace, fileToCopy)
print 'destination =', outputFile
