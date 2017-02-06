import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [RastersExample]


class RastersExample(object):
    '''Perform SA operations on the selected rasters'''
    def __init__(self):
        self.label = 'RastersExample'
        self.canRunInBackground = False

    def getParameterInfo(self):
        '''Set up the parameters and return the list of parameter objects.'''
        # theWorkspace
        param1 = arcpy.Parameter()
        param1.name = 'theWorkspace'
        param1.displayName = '1. Select a workspace containing rasters:'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Workspace'
        param1.filter.list = ["Local Database"]

        # theRasters
        param2 = arcpy.Parameter()
        param2.name = 'theRasters'
        param2.displayName = '2. Select rasters within the workspace:'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'String'
        param2.multiValue = True
        # param2.filter.list = []

        return [param1, param2]

    def isLicensed(self):
        """Prevent the tool from running if the Spatial Analyst extension
        is not available."""
        if arcpy.CheckExtension('Spatial') == 'Available':
            return True  # The tool can be executed.
        else:
            return False  # The tool can not be executed.

    def updateParameters(self, parameters):
        '''Initialize raster list.'''
        if parameters[0].altered:
            arcpy.env.workspace = parameters[0].value
            rasts = arcpy.ListRasters()
            if rasts:
                parameters[1].filter.list = rasts
            else:
                parameters[1].filter.list = []
        return

    def updateMessages(self, parameters):
        '''Check for rasters.'''
        if parameters[0].altered:
            if not parameters[1].filter.list:
                parameters[0].setErrorMessage('This directory does not contain any rasters.')
        return

    def execute(self, parameters, messages):
        '''Calculate the Sine of each input raster.'''
        arcpy.CheckOutExtension('Spatial')
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = parameters[0].value  # Set the workspace.
        for rast in parameters[1].values:
            try:
                outSin = arcpy.sa.Sin(rast)
                outSin.save(rast+'_Sin')
                message = '{0}_Sin created in {1}.'.format(rast, arcpy.env.workspace)
                arcpy.AddMessage(message)
            except:
                message = '{0}_Sin could not be created.'.format(rast)
                arcpy.AddMessage(message)
