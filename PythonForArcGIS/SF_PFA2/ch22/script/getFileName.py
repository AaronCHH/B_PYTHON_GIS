# getFileName.py
# Purpose: Get a shapefile name from the user and print the shapeType.
# Usage: No script arguments required.
import tkFileDialog, arcpy, Tkinter
fatherWilliam = Tkinter.Tk()
fatherWilliam.withdraw()
fc = tkFileDialog.askopenfilename(
    filetypes=[("shapefiles", "*.shp")],
    title='Choose a SHAPEFILE that defines the STATISTICAL ZONES',
    parent=fatherWilliam)
print 'fc = {0}'.format(fc)
desc = arcpy.Describe(fc)
print 'Shape type = {0}'.format(desc.ShapeType)
fatherWilliam.destroy()
