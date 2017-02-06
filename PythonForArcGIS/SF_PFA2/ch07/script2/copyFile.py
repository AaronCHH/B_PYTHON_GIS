# copyFile.py
# Purpose: Copy a file.
# Usage: source_full_path_file_name, destination_directory
# Example: C:/gispy/data/ch07/park.shp C:/gispy/scratch/

import arcpy, os

inputFile = arcpy.GetParameterAsText(0)
outputDir = arcpy.GetParameterAsText(1)

baseName = os.path.basename(inputFile)
outputFile = os.path.join(outputDir, baseName)

arcpy.Copy_management(inputFile, outputFile)

print 'inputFile =', inputFile
print 'outputDir =', outputDir
print
print 'baseName =', baseName
print 'outputFile = ', outputFile
