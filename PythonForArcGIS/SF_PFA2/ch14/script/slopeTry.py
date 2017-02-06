# slopeTry.py
# Purpose: Find the slope, given rise and run.
# Usage: slope_rise slope_run
# Example input: 1 3
import sys

rise = sys.argv[1]
run = sys.argv[2]

try:
    print 'Rise: {0} Run: {1}'.format(rise, run)
    slope = float(rise)/float(run)
    print 'Slope = rise/run'
except ZeroDivisionError:
    slope = 'Undefined (line is vertical)'
except ValueError:
    print 'Usage: <numeric rise> <numeric run>'
    slope = 'Not found'

print 'Slope:', slope
