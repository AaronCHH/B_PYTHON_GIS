import os, sys
infile = sys.argv[1]
try:
  f = open(infile, 'r')
  print f.read()
  f.close()
except IOError:
  print"{0} doesn't exist or can't be opened.".format(infile)