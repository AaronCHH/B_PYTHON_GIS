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
print 'Found', trafficLightCount, lights in the intersectionCount buffer and, ' buffereDist 'intersections.'

# 3) Modify the code to correctly use the three variables
#      and use concatenation to join expression components.
print 'Found' + trafficLightCount + lights in the buffereDist buffer and intersectionCount intersections.'

# 4) Modify the code to correctly use ALL three variables
#      and use the string 'format' method.
print 'Found {1} lights in the {0} buffer and 30 intersections.'format(trafficLightsCount, bufferDist)
