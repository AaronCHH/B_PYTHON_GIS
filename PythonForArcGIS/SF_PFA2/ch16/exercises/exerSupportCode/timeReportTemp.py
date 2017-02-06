# timeReport.py
# Purpose: Provide time-related functions.
# Usage: No script arguments needed for module testing.

import datetime, time


def reportTime():
    '''Print the current time'''
    t = datetime.datetime.now()
    print t.ctime()


def getTime():
    '''Report the current time'''
    t = datetime.datetime.now()
    return t


def reportDiffTime(start, end, message='Time elapsed:'):
    '''Print the amount of time that based between "start" and "end"'''
    difference = end - start
    weeks, days = divmod(difference.days, 7)
    minutes, seconds = divmod(difference.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print message
    # Print time difference. Example=> 438 weeks, 5 days, 0:49:35
    print '{0} weeks, {1} days, {2}:{3}:{4}'.format(weeks, days, hours, minutes, seconds)

if __name__ == '__main__':
    print 'Script began running at: '
    reportTime()

    beforeSleep = getTime()  # Get current time,
    time.sleep(10)
    afterSleep = getTime()  # Get current time,

    message = 'Time elapsed for sleeping'
    reportDiffTime(beforeSleep, afterSleep, message)  # Print the time difference.
    print 'Script completed at:'
    reportTime()
