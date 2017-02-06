# gridToPoly.py
# Purpose:      Convert GRID format raster datasets to polygon feature classes.
#               If not a raster nor a GRID then warn the user.
#               Otherwise, report the output file name.
# Usage:        full_path_filename


import arcpy, os, sys

if len(sys.argv) >= 2:
    fileName = sys.argv[1]
    arcpy.env.workspace = os.path.dirname(fileName)
    raster = os.path.basename(fileName)
    dsc = arcpy.Describe(raster)
    if dsc.dataType == 'RasterDataset':
        if dsc.Format == 'GRID':
            polygonFile = 'C:/gispy/scratch/' + raster + '.shp'
            arcpy.RasterToPolygon_conversion(raster, polygonFile)
            print 'Conversion complete to:', polygonFile
        else:
            print '\n Warning: Conversion not performed.\n \
            Input raster format is {0} not GRID.'.format(dsc.Format)
    else:
        print '\n Warning: Conversion not performed.\n \
        Input data type is {0} not RasterDataset.'.format(dsc.dataType)
else:
    print 'Usage: GRID format raster dataset full path name'
