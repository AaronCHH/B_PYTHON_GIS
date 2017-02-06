# askAndDestroy.py
# Purpose: Get a directory from the user and suppress the root Tk window.
# Usage: No script arguments required

import tkFileDialog, Tkinter
# Get a tk object.
fatherWilliam = Tkinter.Tk()

# Hide the tk window.
fatherWilliam.withdraw()

inputDir = tkFileDialog.askopenfilename(parent=fatherWilliam)

# Destroy the tk window.
fatherWilliam.destroy()
