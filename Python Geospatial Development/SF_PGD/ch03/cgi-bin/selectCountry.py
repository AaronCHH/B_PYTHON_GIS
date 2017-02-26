#!/usr/bin/env python

import database
database.open()

print 'Content-Type: text/html; charset=UTF-8\n\n'
print '<html>'
print '<head><title>Select Country</title></head>'
print '<body>'
print '<form method="POST" action="selectArea.py">'
print '<select name="countryID" size="10">'

for id,name in database.list_countries():
    print '<option value="'+str(id)+'">'+name+'</option>'

print '</select>'
print '<p>'
print '<input type="submit" value="OK">'
print '</form>'
print '</body>'
print '</html>'

