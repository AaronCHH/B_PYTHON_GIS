# eyeTrackSHP.py
# Purpose: Modify raw eye tracking data and import it into a shapefile.
# Usage: fullpath_filename output_directory
# Output: A modified text file and a point shapefile.
# Example input: C:/gispy/data/ch19/eyeTrack.csv C:/gispy/scratch/
import os, arcpy, sys


def transformPoints(resX, resY, rawX, rawY):
    '''Transform raw eye tracking data based on extent of
    stimulus and resolution of screen'''
    minXP = 2.0
    maxXP = 1260.0
    minYP = resY - 984.0
    maxYP = resY - 51.0
    xMin = -18695125.3795
    xMax = 19465354.9216
    yMin = -12958672.9716
    yMax = 15351008.2049

    # Convert eye track screen percentages to pixels.
    pixX = rawX*resX
    pixY = (1-rawY)*resY
    #pixX = [676.00,105.00,391.00]
    #pixY= [739.00,881.00,453.00]

    # Calculate geographic coordinate system dx and dy.
    geoDX = xMax - xMin
    geoDY = yMax - yMin

    # Calculate pixel dx and dy.
    pixDX = maxXP - minXP
    pixDY = maxYP - minYP

    # FPOGXG and YG are the eye tracking points represented in the map document's coordinate system
    geoX = xMin + (pixX-minXP)*geoDX/pixDX
    geoY = yMin + (pixY-minYP)*geoDY/pixDY
    return geoX, geoY


def getIndex(delimString, delimiter, name):
    '''Get position of item in a delimited string'''
    delimString = delimString.strip()
    lineList = delimString.split(delimiter)
    index = lineList.index(name)
    return index

try:
    infile = sys.argv[1]
    outDir = sys.argv[2]
except IndexError:
    print 'Required input: The full path file name of an eye tracking dataset and an output directory.'
    sys.exit(0)

headers = 2
field1 = 'FPOGX'
field2 = 'FPOGY'

sep = ','  # Delimiter is a comma.
baseN = os.path.basename(infile)
outfile = outDir + os.path.splitext(baseN)[0] + 'v2' + \
    os.path.splitext(baseN)[1]
with open(infile, 'r') as fin:
    ### 1. Write a 'with' statement that opens the 'output' file for writing and creates a file object.
    ###
        # GET screen w/h field index from first line.
        ### 2. Read the first line.
        ###
        findex1 = getIndex(line, sep, 'SCREEN_WIDTH')
        findex2 = getIndex(line, sep, 'SCREEN_HEIGHT')
        ### 3. Read the second line.
        ###

        lineList = line.split(sep)
        dx = float(lineList[findex1])
        dy = float(lineList[findex2])
        # READ and WRITE field names.
        ### 4. Read the third line
        ###
        ### 5. Write the line to the output file.
        ###

        # FIND field indices.
        findex1 = getIndex(line, sep, field1)
        findex2 = getIndex(line, sep, field2)
        
        ### 6. Use a FOR-loop to loop through the remaining lines of the input file.
        ###
            ### 7. Split the line on the field delimiter and store the result in 'lineList'.
            ###
            v1 = float(lineList[findex1])
            v2 = float(lineList[findex2])
            # IF condition is TRUE, write line.
            if v1 > 0 and v2 > 0:
                x,y = transformPoints(dx, dy, v1, v2)
                lineList[findex1] = str(x)
                lineList[findex2] = str(y)
                line = ','.join(lineList) + '\n'
                ### 8. Write the line to the output file.
                ###
        print '{0} complete.'.format(outfile)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = os.path.dirname(infile)
tempLayer = 'tmpLayer'
if arcpy.Exists(tempLayer):
    arcpy.Delete_management(tempLayer)
### 9. Call the MakeXYEventLayer management tool to create a temorary layer 'tempLayer'
###    from the modified csv (v2) file. Use the field1 and field2 (assigned earlier in the sample script) as x and y respectively.
###

output = outDir + os.path.splitext(baseN)[0] + '.shp'
### 10. Call the arcpy CopyFeatures management tool to copy the temporary layer to the
###     output shapefile (a persistent file instead of a temp. one)
###
print 'Shapefile complete. View {0} in ArcCatalog.'.format(output)
