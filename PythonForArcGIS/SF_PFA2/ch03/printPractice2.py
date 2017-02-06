# printPractice.py
# Correct the mistakes in this script so that it prints
#    the same statement 4 times, using 4 different methods:
#    1) hard-coding 2) commas 3) concatenation 4) string formatting
trafficLightsCount = 12
bufferDist = '5 mi.'
intersectionCount = 20

# 1) Entirely hard-coded statement.  Don't change this one.
#      Make the other print statements match this output.
print 'Found 12 lights in the 5 mi. buffer and 20 intersections.'

# 2) Modify the code to correctly use the three variables
#      and use commas to join expression components.
print 'Found', trafficLightsCount, 'lights in the', bufferDist, 'buffer and', intersectionCount, 'intersections.'

# 3) Modify the code to correctly use the three variables
#      and use concatenation to join expression components.
print 'Found ' + str(trafficLightsCount) + ' lights in the ' + str(bufferDist) + ' buffer and ' + str(intersectionCount) + ' intersections.'

# 4) Modify the code to correctly use ALL three variables
#      and use the string 'format' method.
print 'Found {0} lights in the {1} buffer and 30 intersections.'.format(trafficLightsCount, bufferDist)
