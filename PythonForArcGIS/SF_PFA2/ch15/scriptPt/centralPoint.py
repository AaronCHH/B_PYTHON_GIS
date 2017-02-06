# centralPoint.py
# Purpose: Use time-related functions to time geoprocessing tool calls.
# Comment: When complete, step through with the DEBUGGER to
#          see non-zero times!!!!
# Usage: input_polygon_shapefile output_directory
# Example script input: C:/gispy/data/ch15/park.shp C:/gispy/scratch/

import datetime, time


def getTime():
    '''Return a time object for the current time'''
    t = datetime.datetime.now()  # Get a datetime object
    return t  # Return the datetime object to the caller


def timeDifference(start, end, message='Time elapsed:'):
    '''Print a message and the difference between 2 time objects'''
    difference = end - start
    weeks, days = divmod(difference.days, 7)
    minutes, seconds = divmod(difference.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print message
    print '{0} weeks, {1} days, {2}:{3}:{4}'.format(weeks,
                                                    days,
                                                    hours,
                                                    minutes,
                                                    seconds)

# Example of calling the time functions.
t1 = getTime()
time.sleep(3)
t2 = getTime()
timeDifference(t1, t2, 'Time for the sleep command:')
