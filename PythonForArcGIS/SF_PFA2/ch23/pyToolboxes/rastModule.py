# rastModule.py
import arcpy


def batchSine(workspace, rastList):
    '''Calculate the Sine of each raster in the list.'''
    arcpy.CheckOutExtension('Spatial')
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = workspace
    for rast in rastList:
        try:
            outSin = arcpy.sa.Sin(rast)
            outSin.save(rast+'_Sin')
            message = '{0}_Sin created in {1}.'.format(rast, arcpy.env.workspace)
            arcpy.AddMessage(message)
        except:
            message = '{0}_Sin could not be created.'.format(rast)
            arcpy.AddMessage(message)
