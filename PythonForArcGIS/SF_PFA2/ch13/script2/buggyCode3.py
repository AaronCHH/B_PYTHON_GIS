# buggyCode3.py
# Purpose: Normalize data time steps.
timeSteps = [2011, 2009, 2008, 2005, 2004, 2003, 2001, 1999]
# Normalize to values between 0 and 1.
maxv = max(timeSteps)
minv = min(timeSteps)
r = maxv - minv
normalizedList = [v - minv/r for v in timeSteps]
print normalizedList
