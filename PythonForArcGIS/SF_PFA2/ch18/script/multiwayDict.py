# multiwayDict.py
# Purpose: Generate a list of sea level rise (SLR) for each year
#          based on  an IPCC scenario.
# Usage: sea_level_rise_model time_interval
#        SLR should be B1, A1T, B2, A1B, A2, or A1F1;
#        time_interval must be between 1 and 100
# Example input:  AIB 50
import sys

# Input sea level rise model: B1, A1T, B2, A1B, A2, or A1F1
sres = sys.argv[1]

# Input time interval to examine sea level rise
#      (Must be integer between 1 and 100)
interval = int(sys.argv[2])

# Generate a list of sea level rise (SLR) based in the IPCC scenario for each year

# Create the list of elevations for scenario B1.
if sres == "B1":
    sinkB1 = []   # Create an empty list.
    print "Running Sea Level Rise Model for ",  sres
    b1 = 0           # starting a baseline elevation
    for year in range(0, 101, interval):   # Loop to generate sea level rise for next 100 years
        rate = 0.0038                      # .38 mm increase in SL
        b1 = b1 + (rate*interval)
        sinkB1.append(b1)                  # Append value to the list.
    print sinkB1

# Do the same for the 5 other SLR scenarios.####

elif sres == "A1T":
    sinkA1T = []
    print "Running Sea Level Rise Model for ",  sres
    a1t = 0
    for year in range(0, 101, interval):
        rate = 0.0045
        a1t = a1t + (rate*interval)
        sinkA1T.append(a1t)
    print sinkA1T

elif sres == "B2":
    sinkB2 = []
    print "Running Sea Level Rise Model for ",  sres
    b2 = 0
    for year in range(0, 101, interval):
        rate = 0.0043
        b2 = b2 + (rate*interval)
        sinkB2.append(b2)
    print sinkB2

elif sres == "A1B":
    sinkA1B = []
    print "Running Sea Level Rise Model for ",  sres
    a1b = 0
    for year in range(0, 101, interval):
        rate = 0.0048
        a1b = a1b + (rate*interval)
        sinkA1B.append(a1b)
    print sinkA1B

elif sres == "A2":
    sinkA2 = []
    print "Running Sea Level Rise Model for ",  sres
    a2 = 0
    for year in range(0, 101, interval):
        rate = 0.0051
        a2 = a2 + (rate*interval)
        sinkA2.append(a2)
    print sinkA2

elif sres == "A1F1":
    sinkA1F1 = []
    print "Running Sea Level Rise Model for ",  sres
    a1f1 = 0
    for year in range(0, 101, interval):
        rate = 0.0059
        a1f1 = a1f1 + (rate*interval)
        sinkA1F1.append(a1f1)
    print sinkA1F1
