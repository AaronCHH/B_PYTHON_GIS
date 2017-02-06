# timeReport.py
# Purpose: Provide time-related functions.
# Usage: No script arguments needed for module testing.
import datetime, time


def getDay(theDate):
    '''Given a date, return the day of the week'''
    index = theDate.weekday()
    wDict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
             3: 'Thursday', 4: 'Friday', 5: 'Saturday',
             6: 'Sunday'}
    return wDict[index]


def getTime():
    '''Report the current time'''
    t = datetime.datetime.now()
    return t


def reportDiffTime(start, end, message='Time elapsed'):
    '''Print the number of seconds that passed
    between "start" and "end".'''
    difference = end - start
    seconds = difference.total_seconds()
    print '{0}: {1} seconds.'.format(message, seconds)


def reportTime(message='The current date and time is'):
    '''Print the current time'''
    now = time.ctime()
    print '{0}: {1}'.format(message, now)

if __name__ == '__main__':
    reportTime('Script began running at')
    # Get current time.
    beforeSleep = getTime()
    time.sleep(5)
    # Get current time.
    afterSleep = getTime()

    message = 'Time elapsed for sleeping'
    # Print the time difference.
    reportDiffTime(beforeSleep, afterSleep, message)
    reportTime('Script completed at')
    print 'Hurray! I like {0}s.'.format(getDay(afterSleep))
    raw_input()
