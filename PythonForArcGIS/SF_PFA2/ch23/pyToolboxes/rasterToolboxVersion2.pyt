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
        # 1_Select_a_workspace_containing_rasters
        param1 = arcpy.Parameter()
        param1.name = '1_Select_a_workspace_containing_rasters'
        param1.displayName = '1. Select a workspace containing rasters:'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Workspace'

        # 2_Select_rasters_within_the_workspace
        param2 = arcpy.Parameter()
        param2.name = '2_Select_rasters_within_the_workspace'
        param2.displayName = '2. Select rasters within the workspace:'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'String'
        param2.multiValue = True
        param2.filter.list = []

        # 3_Select_rasters_within_the_workspace_
        param3 = arcpy.Parameter()
        param3.name = '3_Select_SA_operation'
        param3.displayName = '3: Select SA operation'
        param3.parameterType = 'Required'
        param3.direction = 'Input'
        param3.datatype = 'String'
        param3.filter.list = ['Sine', 'Cosine']

        return [param1, param2]

    def isLicensed(self):
        return True

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
        import rastModule
        wkspace = parameters[0].value
        rasters = parameters[1].values
        rastModule.batchSine(wkspace, rasters)
