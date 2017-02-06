# walkCount.py
# Purpose: Walk and get the record count for each file, where possible.
# Usage: input_directory
# Example input: C:/gispy/data/ch15
import arcpy, datetime, sys
mydir = sys.argv[1]


def diffTime(start, end):
    '''Calculate the difference between two datetime objects'''
    difference = end - start
    weeks, days = divmod(difference.days, 7)
    minutes, seconds = divmod(difference.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return weeks, days, hours, minutes, seconds

before = datetime.datetime.now()
for root, dirs, files in arcpy.da.Walk(mydir):
    for f in files:
        try:
            count = arcpy.GetCount_management(root + "/" + f)
            print '{0}/{1}  Count = {2}'.format(root, f, count)
        except arcpy.ExecuteError:
            print arcpy.GetMessages()

after = datetime.datetime.now()

t = diffTime(before, after)

print 'Time elapsed: {0} weeks, {1} days, {2}:{3}:{4}'.format(t[0], t[1], t[2], t[3], t[4])
