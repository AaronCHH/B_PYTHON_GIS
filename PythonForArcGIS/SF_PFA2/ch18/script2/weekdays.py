# weekdays.py
# Purpose: Print the day of the week, based on a number.
#          Contrast using ELIF branching (15 lines of code)
#          with using a dictionary (3 lines of code)
# Usage: Integer between 0 and 4.
# Example 3


import sys
code = int(sys.argv[1])
if code == 0:
    day = 'Monday'
    print 'Weekday: {0}'.format(day)
elif code == 1:
    day = 'Tuesday'
    print 'Weekday: {0}'.format(day)
elif code == 2:
    day = 'Wednesday'
    print 'Weekday: {0}'.format(day)
elif code == 3:
    day = 'Thursday'
    print 'Weekday: {0}'.format(day)
elif code == 4:
    day = 'Friday'
    print 'Weekday: {0}'.format(day)

#################################### Dictionary equivalent

weekdayDict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}

day = weekdayDict[code]
print 'Weekday: {0}'.format(day)
