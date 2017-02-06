# campusCrimes.py
# Analyze crime data
# Usage: crime_report_filename
# Example input: C:/gispy/data/ch21/crimes.csv

import sys

### Define an 'Incident' class.

    ### Define a method named '__init__' to Initialize the
    ### ID, Time, Type, Location, Narrative, Status object properties.

    ### Define a method named 'brief' to Print the ID, type, status, and narrative
    ### for the Incident.

    ### Define a method named 'isMorning' to return True if time
    ### was before noon, False otherwise.

    ### Define a method named 'resolve' to set status to 'Resolved'
    ### if the current status is 'Pending'.

try:
    dataset = sys.argv[1]
except IndexError:
    print 'Usage: Requires full path input file name.'
    sys.exit()
    
# Create an empty list to contain the Incident objects.
crimeList = []

# Read the crime report.
with open(dataset, 'r') as f:
    # Read the header.
    headers = f.readline().split(',')
    # Read each record and parse the attributes.
    for line in f:
        lineList = line.strip().split(',')
        reportNumber = lineList[0]
        timeReported = lineList[1]
        incidentType = lineList[2]
        location = lineList[3]
        narrative = lineList[4]
        status = lineList[5].strip()
        ### Create initialize an Incident object instance and store it in a variable
        ### Append the new Incident object to the crimeList.

### For the fourth Incident in the list...
###     call the 'brief' method
###     call the 'resolve' method.
###     call the 'brief' method again.

### For the twelve Incident in the list...
###     call the 'isMorning' method and store the return value.
###     replace 'bla' with the 'ID' property and 'Dunno' with the 'isMorning' return value
print 'Did incident {0} occur in the morning? {1}'.format('bla', 'Dunno')

### For the twelve Incident in the list...
###     change the Incident status to 'Bummer'
###     call the 'brief' method.

### Delete the twelve Incident in the list.

### For the twelve Incident in the list, call the 'brief' method again.
