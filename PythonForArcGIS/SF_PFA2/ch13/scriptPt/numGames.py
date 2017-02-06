# numGames.py    # Usage: integer_value     # Example: 5
import sys
x = int(sys.argv[1])   # Get the input integer.
while x < 100:  # WHILE x is less than 100
    if x % 2 == 0:  # IF x is even THEN
        x = x + 50
        print x
    else:
        if x > 0:  # IF x is positive THEN
            print x
            x = x + 1
    else:
            print x
