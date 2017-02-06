# checkForBrokenDataSources.py
# Input: Path to map directory
# Sample input C:/gispy/data/ch24/maps
import arcpy, os, sys

mydir = sys.argv[1]
files = os.listdir(mydir)

maps = [f for f in files if f.endswith('.mxd')]

for m in maps:
    mxd = arcpy.mapping.MapDocument(mydir + '/' + m)
    broken = arcpy.mapping.ListBrokenDataSources(mxd)
    print m
    print broken
    del mxd
