# age.py
# Purpose: Calculate age.
# Usage: No script arguments needed.
import datetime


def calculateAge(yr, mo, day):
    '''Calculate age based on the given birth date.'''
    # Get datetime objects for birth date and today
    born = datetime.date(yr, mo, day)
    today = datetime.date.today()
    # Get this year's birthday and handle leap year exceptions
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day-1)
    # Return age
    if birthday < today:
        return today.year - born.year
    else:
        return today.year - born.year - 1

print calculateAge(2012, 4, 20)
