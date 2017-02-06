# cond2.py
# Purpose:  Celebrate if input fruit is in list.
# Usage: fruit_name
# Input example 1:  grapes
# Input example 2:  guavas
import sys

fruit = sys.argv[1]

myList = ['grapes', 'mangos', 'blueberries']
if fruit not in myList:
    # do nothing
    pass
else:
    print 'Hurray, {0}!'.format(fruit)
