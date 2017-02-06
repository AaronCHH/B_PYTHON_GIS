# numChars.py  # Correct the 5 errors
# Purpose: Get a file object and count the number of character
#          in the user selected text file.
# Usage: No script arguments required.

import Tkinter

root = Tkinter.Tk()
root.withdraw()
fileObj = tkFileDialog.askopenfilename(
    filetypes=('text file', '*.txt'),
    title='Select a text file',
    initialdir='C:/gispy/data/ch22/',
    initialfile='precip.txt',
    parent='root')
root.destroy()

contents = fileObj.read()
fileObj.close()
numCharacters = len(contents)
print "'{0}' has {1} characters.".format(fileObj.name)
