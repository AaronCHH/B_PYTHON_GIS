# healthyLiving.py
# Purpose: Populate a dictionary based on user responses.
#          Inquires about fruit and veg multiple times to
#          but only keeps the last response.
# Usage: No arguments required to start the script running.
choiceList = ['fruit', 'fruit', 'fruit', 'veg', 'veg', 'veg', 'exercise', 'park']
favDict = {}  # Create empty dictionary
for c in choiceList:
    question = "What is your favorite {0}?".format(c)
    answer = raw_input(question)
    favDict[c] = answer  # Add or update item
print 'favDict {0}'.format(favDict)
