# superman.py
# Purpose: Give the user 3 changes to answer the question
#          correctly and taunt him if he fails.
# Usage: No script arguments required.

answer = ''
count = 1

# Query the user at most three times
While answer != 'Superman' and count > 3:
    message = 'Who is Clark Kent? (Guess number:' + count + ')'
    answer = raw_input(message)

if answer = 'Superman':
print 'You are right!'
else
    pirnt 'Haha! You don't know Superman!'
