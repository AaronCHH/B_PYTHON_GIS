# fileDialogOptions.py
# Purpose: Vary file dialog options to get file and directory
#          names from user and print the results.
# Usage: No script arguments required.
import tkFileDialog

t = ("shapefiles ", "*.shp")
print 'Type = {0}'.format(type(t))

fname1 = tkFileDialog.askopenfilename(filetypes=[t])
print 'fname1 = {0}'.format(fname1)

fname2 = tkFileDialog.askopenfilename(title='Test 2 filetypes',
                                      filetypes=[("csv (Comma delimited) ", "*.csv"),("Text Files ", "*.txt")])
print 'fname2 = {0}'.format(fname2)

fname3 = tkFileDialog.askopenfilename(title='Test initialdir', initialdir='C:/gispy')

print 'fname3 = {0}'.format(fname3)

fname4 = tkFileDialog.askopenfilename(title='Test initialfile', initialfile='bogus.shp')

print 'fname4 = {0}'.format(fname4)

fnames = tkFileDialog.askopenfilename(title='Test multiple selections allowed', multiple=True)
files = fnames.split()
print 'Name list:'
for fname in files:  # For each file selected by the user,...
    print '   {0}'.format(fname)

inputDir = tkFileDialog.askdirectory(title='Test mustexist =True', mustexist=True)
print 'inputDir = {0}'.format(inputDir)
