import arcpy, os, sys


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)


def printArgs(params):
    '''Print user arguments.'''
    printArc('Number of arguments = {0}'.format(len(params)))
    for index, arg in enumerate(params):
        printArc('Argument {0}: {1}'.format(index, arg.value))


# Conversion of toolbox C:\gispy\sample_scripts\ch23\toolboxes\validatorExamples.tbx
class Toolbox(object):
    def __init__(self):
        self.label = 'validatorExConverted'
        self.alias = ''
        self.tools = [Favorites_um, Categories_ip, Rasters_up]


# Tool implementation code
class Favorites_um(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\validatorExamples.tbx\01_favorites_um'''
    def __init__(self):
        self.label = '01_favorites_um'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Favorite_positive_number
        param1 = arcpy.Parameter()
        param1.name = 'Favorite_positive_number'
        param1.displayName = 'Favorite positive number'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Double'

        # Favorite_color
        param2 = arcpy.Parameter()
        param2.name = 'Favorite_color'
        param2.displayName = 'Favorite color'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'String'

        return [param1, param2]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        if parameters[0].altered:
            if parameters[0].value <= 0:
                parameters[0].setErrorMessage("Please specify a positive number.")
        return

    def execute(self, parameters, messages):
        num = parameters[0].value
        color = parameters[1].value

        printArc('''Your favorite positive number is {0}?
        That's my favorite too!'''.format(num))

        printArc('''Your favorite color is {0}?
        Erm...I don't like {0}!'''.format(color))


class Categories_ip(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\validatorExamples.tbx\02_categories_ip'''
    def __init__(self):
        self.label = '02_categories_ip'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Address_Locator
        param1 = arcpy.Parameter()
        param1.name = 'Address_Locator'
        param1.displayName = 'Address Locator'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Address Locator'

        # Areal_unit
        param2 = arcpy.Parameter()
        param2.name = 'Areal_unit'
        param2.displayName = 'Areal unit'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'Areal unit'

        # Boolean
        param3 = arcpy.Parameter()
        param3.name = 'Boolean'
        param3.displayName = 'Boolean'
        param3.parameterType = 'Required'
        param3.direction = 'Input'
        param3.datatype = 'Boolean'

        # Cell_size
        param4 = arcpy.Parameter()
        param4.name = 'Cell_size'
        param4.displayName = 'Cell size'
        param4.parameterType = 'Optional'
        param4.direction = 'Input'
        param4.datatype = 'Cell Size'

        # Compression
        param5 = arcpy.Parameter()
        param5.name = 'Compression'
        param5.displayName = 'Compression'
        param5.parameterType = 'Optional'
        param5.direction = 'Input'
        param5.datatype = 'Compression'

        # Coordinate_system
        param6 = arcpy.Parameter()
        param6.name = 'Coordinate_system'
        param6.displayName = 'Coordinate system'
        param6.parameterType = 'Optional'
        param6.direction = 'Input'
        param6.datatype = 'Coordinate System'

        # Date
        param7 = arcpy.Parameter()
        param7.name = 'Date'
        param7.displayName = 'Date'
        param7.parameterType = 'Optional'
        param7.direction = 'Input'
        param7.datatype = 'Date'

        # Double
        param8 = arcpy.Parameter()
        param8.name = 'Double'
        param8.displayName = 'Double'
        param8.parameterType = 'Optional'
        param8.direction = 'Input'
        param8.datatype = 'Double'

        # Extent
        param9 = arcpy.Parameter()
        param9.name = 'Extent'
        param9.displayName = 'Extent'
        param9.parameterType = 'Optional'
        param9.direction = 'Input'
        param9.datatype = 'Extent'

        params = [param1, param2, param3, param4, param5, param6, param7, param8, param9]

        numParams = len(params)
        for index in range(numParams):
            if index < numParams/3.0:
                params[index].category = 'A. Really important!'
            elif index < (2*numParams)/3.0:
                params[index].category = 'B. If you have time.'
            else:
                params[index].category = "C. Meh. Don't bother."
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        printArgs(parameters)


class Rasters_up(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\validatorExamples.tbx\03_rasters_up'''
    def __init__(self):
        self.label = '03_rasters_up'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # 1__Select_a_workspace_containing_rasters_
        param1 = arcpy.Parameter()
        param1.name = '1__Select_a_workspace_containing_rasters_'
        param1.displayName = '1. Select a workspace containing rasters:'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Workspace'

        # 2__Select_rasters_within_the_workspace_
        param2 = arcpy.Parameter()
        param2.name = '2__Select_rasters_within_the_workspace_'
        param2.displayName = '2. Select rasters within the workspace:'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'String'
        param2.multiValue = True

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
        printArgs(parameters)
