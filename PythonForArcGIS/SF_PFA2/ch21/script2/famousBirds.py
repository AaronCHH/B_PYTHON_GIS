# famousBirds.py
# Purpose: Use the Bird class in 'birds.py'
import birds

sam = birds.Bird('Toucan', 'South America', 1.9)
sam.talk()
sam.talk()
print '{0}s eat {1}.'.format(sam.name, sam.diet())
sam.weight = sam.weight + 0.0625
print 'Sam gained an ounce. He weighs {0} lbs'.format(sam.weight)

polly = birds.Bird('Parrot', 'Central America', 0.4)
polly.talk()
food = polly.diet()
print '{0}s eat {1}.'.format(polly.name, food)
