# buggyLoop.py
# Remove feature classes whose names do not contain the given tag
tag = 'zones'  #'data'
fcs = [u'data1', u'data2', u'data3', u'fireStations',
       u'park_data', u'PTdata4', u'schoolzones',
       u'regions1', u'regions2', u'workzones']

print 'Before loop: {0}'.format(fcs)
for fcName in fcs:
    if tag in fcName:
        fcs.remove(fcName)
print 'After loop: {0}'.format(fcs)


##print 'Before loop: {0}'.format(fcs)
##fcsOut = []
##for fcName in fcs:
##	if tag not in fcName:
##		fcsOut.append(fcName)
##print 'After loop: {0}'.format(fcsOut)
