# boogieWoogie.py
# Purpose: Get a list of Python and ASCII txt file names selected by the user.
# Usage: No script arguments required.
import tkFileDialog

files = tkFileDialog.askopenfilename(filetypes=[('spam', '*.py'),
                                     ('Text files', '*.txt')],
                                     title='Boogiewoogie',
                                     initialdir='C:/gispy/sample_scripts/ch22/',
                                     initialfile='superman.py',
                                     multiple=True)
