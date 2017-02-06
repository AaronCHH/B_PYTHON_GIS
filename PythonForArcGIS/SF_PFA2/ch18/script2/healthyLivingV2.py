# healthyLivingV2.py
# Purpose: Populate a dictionary based on user responses.
#          Inquires about fruit and veg multiple times to
#          and collects ALL of the responses.
# Usage: No arguments required to start the script running.
choiceList = ['fruit', 'fruit', 'fruit', 'veg', 'veg', 'veg', 'exercise', 'park']
topDict = {}  # Create empty dictionary
for c in choiceList:
    question = "What is your favorite {0}?".format(c)
    answer = raw_input(question)
    if not c in topDict:
        topDict[c] = [answer]  # Add a new item to the dictionary.
    else:
        topDict[c].append(answer)  # Update an item by adding to an item's list.

print 'topDict {0}'.format(topDict)
