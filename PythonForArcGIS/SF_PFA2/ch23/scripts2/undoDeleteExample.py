import arcpy, os, reportSTargs, sys

arcpy.env.overwriteOutput = True
workspace = sys.argv[1]
orig = sys.argv[2]

dupStr = sys.argv[3]

dupList = dupStr.split(';')

if arcpy.Describe(orig).dataType == 'Workspace':
    # for each output workspace
    for outF in dupList:
        if not arcpy.Exists(outF):
            arcpy.CreateFileGDB_management(workspace, os.path.basename(outF))
        arcpy.env.workspace = orig
        for root, dirs, files in arcpy.da.Walk(orig):
            for f in files:
                if not arcpy.Exists('{0}/{1}'.format(outF, f)):
                    arcpy.Copy_management(f, '{0}/{1}'.format(outF, f))
                    reportSTargs.printArc('{0}/{1} created.'.format(outF, f))
else:
    for outF in dupList:
        arcpy.Copy_management(orig, outF)
        reportSTargs.printArc('{0} overwritten'.format(outF))
