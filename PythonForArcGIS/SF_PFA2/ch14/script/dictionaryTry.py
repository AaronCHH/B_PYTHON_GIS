# dictionaryTry.py
# Purpose: Print days.
# Usage: No arguments needed.

dictionary = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}

try:
    for dayofWeek in range(7):
        print dictionary[dayofWeek]
except:
    print 'An error occurred.'
    ### Use the traceback module to force an exception to print now
