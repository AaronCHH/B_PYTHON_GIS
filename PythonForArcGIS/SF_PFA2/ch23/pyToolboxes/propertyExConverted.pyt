import arcpy, os, sys


def getAbsPath(relativePath):
    '''Return the absolute path given a relative path to this file'''
    tbxPath = os.path.abspath(__file__)
    tbxDir = os.path.dirname(tbxPath)
    fullPath = os.path.join(tbxDir, relativePath)
    return os.path.abspath(fullPath)


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)


def printArgs(params):
    '''Print user arguments.'''
    printArc('Number of arguments = {0}'.format(len(params)))
    for index, arg in enumerate(params):
        printArc('Argument {0}: {1}'.format(index, arg.value))


# Export of toolbox C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx
class Toolbox(object):
    def __init__(self):
        self.label = 'propertyExConverted'
        self.alias = ''
        self.tools = [ToolOptionalParam1, ToolOptionalParam2, ToolRequiredOutput, ToolDerivedOutput1,
                      ToolDerivedOutput2, ToolmultiValueIn, ToolMultiValueOut, ToolDefaultVals,
                      ToolSchema, ToolEnvironments, ToolFilterRange, ToolFilterValueList,
                      ToolInputObtainedFrom, ToolDerivedObtainedFrom, ToolSymbology]


# Tool implementation code
class ToolOptionalParam1(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\01optionalParam1'''
    def __init__(self):
        self.label = '01_optionalParam'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Areal_unit__required_
        param1 = arcpy.Parameter()
        param1.name = 'Areal_unit__required_'
        param1.displayName = 'Areal unit (required)'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Areal unit'

        # Cell_size
        param2 = arcpy.Parameter()
        param2.name = 'Cell_size'
        param2.displayName = 'Cell size'
        param2.parameterType = 'Optional'
        param2.direction = 'Input'
        param2.datatype = 'Cell Size'

        # Compression
        param3 = arcpy.Parameter()
        param3.name = 'Compression'
        param3.displayName = 'Compression'
        param3.parameterType = 'Optional'
        param3.direction = 'Input'
        param3.datatype = 'Compression'

        # Double
        param4 = arcpy.Parameter()
        param4.name = 'Double'
        param4.displayName = 'Double'
        param4.parameterType = 'Optional'
        param4.direction = 'Input'
        param4.datatype = 'Double'

        # Feature_class
        param5 = arcpy.Parameter()
        param5.name = 'Feature_class'
        param5.displayName = 'Feature class'
        param5.parameterType = 'Optional'
        param5.direction = 'Input'
        param5.datatype = 'Feature Class'

        return [param1, param2, param3, param4, param5]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # Purpose: Print the arguments passed into a script tool.
        # Arguments: Variable (can be used for any number of arguments)
        printArgs(parameters)


class ToolOptionalParam2(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\02optionalParam'''

    def __init__(self):
        self.label = '02_optionalParam'
        self.description = 'Exponentiate the base by the power.'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Base
        param1 = arcpy.Parameter()
        param1.name = 'Base'
        param1.displayName = 'Base'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Double'

        # Power
        param2 = arcpy.Parameter()
        param2.name = 'Power'
        param2.displayName = 'Power'
        param2.parameterType = 'Optional'
        param2.direction = 'Input'
        param2.datatype = 'Double'

        return [param1, param2]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # exponentiator.py
        # Purpose: Raise base to a power.
        # Arguments: base power(must be a number or #)

        base = float(parameters[0].value)
        # Handle optional argument.
        if not parameters[1].value:
            power = 1
            printArc('No exponent provided.  Using default power of 1.')
        else:
            power = float(parameters[1].value)

        # Calculate the exponentiation.
        result = base**power

        # Report the results.
        printArc('{0} raised to the {1} is {2}'.format(base, power, result))


class ToolRequiredOutput(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\03requiredOutput'''

    def __init__(self):
        self.label = '03_requiredOutput'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input_feature_class
        param1 = arcpy.Parameter()
        param1.name = 'Input_feature_class'
        param1.displayName = 'Input feature class'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Feature Class'

        # Output_feature_class
        param2 = arcpy.Parameter()
        param2.name = 'Output_feature_class'
        param2.displayName = 'Output feature class'
        param2.parameterType = 'Required'
        param2.direction = 'Output'
        param2.datatype = 'Feature Class'

        return [param1, param2]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From copier.py
        # Purpose: Make a copy of argument 1 with a name specified by argument 2.

        printArgs(parameters)
        arcpy.Copy_management(parameters[0].value, parameters[1].value)


class ToolDerivedOutput1(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\04derivedOutput1'''
    def __init__(self):
        self.label = '04_derivedOutput1'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # This_name_is_not_displayed
        param1 = arcpy.Parameter()
        param1.name = 'This_name_is_not_displayed'
        param1.displayName = 'This name is not displayed'
        param1.parameterType = 'Derived'
        param1.direction = 'Output'
        param1.datatype = 'Feature Class'

        return [param1]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From buffer1.py
        # Purpose:  Buffer a file and send the result to a script tool.

        arcpy.env.overwriteOutput = True

        fileToBuffer = 'C:/gispy/data/ch23/smallDir/randpts.shp'
        distance = '500 meters'
        outputFile = 'C:/gispy/scratch/randptsBuffer.shp'

        arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)

        arcpy.SetParameterAsText(0, outputFile)


class ToolDerivedOutput2(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\05derivedOutput2'''
    def __init__(self):
        self.label = '05_derivedOutput2'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # File_to_buffer
        param1 = arcpy.Parameter()
        param1.name = 'File_to_buffer'
        param1.displayName = 'File to buffer'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Feature Class'

        # Buffer_distance
        param2 = arcpy.Parameter()
        param2.name = 'Buffer_distance'
        param2.displayName = 'Buffer distance'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'Linear unit'

        # Derived_output_fc
        param3 = arcpy.Parameter()
        param3.name = 'Derived_output_fc'
        param3.displayName = 'Derived output fc'
        param3.parameterType = 'Derived'
        param3.direction = 'Output'
        param3.datatype = 'Feature Class'

        return [param1, param2, param3]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From buffer2.py
        # Purpose:  Buffer an input file by an input distance
        #           and send the result to a script tool.

        arcpy.env.overwriteOutput = True

        fileToBuffer = parameters[0].value.value
        distance = parameters[1].value
        arcpy.env.workspace = os.path.dirname(fileToBuffer)
        outputFile = 'C:/gispy/scratch/Buff'

        arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)

        arcpy.SetParameterAsText(2, outputFile)


class ToolmultiValueIn(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\06multiValueIn'''
    def __init__(self):
        self.label = '06_multiValueIn'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Select_rasters
        param1 = arcpy.Parameter()
        param1.name = 'Select_rasters'
        param1.displayName = 'Select rasters'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Raster Dataset'
        param1.multiValue = True

        return [param1]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From multiIn.py
        # Purpose: Print the list of input values.
        # Script tools receive a semicolon delimited string;
        # but the Python toolbox receive a Python list.
        inputList = parameters[0].values

        printArc('Input list: {0}'.format(inputList))

        for i in inputList:
            printArc('Input file: {0}'.format(i))


class ToolMultiValueOut(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\07multiValueOut'''
    def __init__(self):
        self.label = '07_multiValueOut'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Enter_a_data_directory
        param1 = arcpy.Parameter()
        param1.name = 'Enter_a_data_directory'
        param1.displayName = 'Enter a data directory'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Folder'

        # Buffer_distance
        param2 = arcpy.Parameter()
        param2.name = 'Buffer_distance'
        param2.displayName = 'Buffer distance'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'Linear unit'

        # Output_files
        param3 = arcpy.Parameter()
        param3.name = 'Output_files'
        param3.displayName = 'Output files'
        param3.parameterType = 'Derived'
        param3.direction = 'Output'
        param3.datatype = 'Shapefile'
        param3.multiValue = True

        return [param1, param2, param3]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From bufferAll.py
        # Purpose: Buffer all the feature classes in an input folder by the input distance and
        #          send the output file names to script tool.
        # Arguments: working_directory linear_unit
        # Sample input: C:/gispy/data/ch23/smallDir "0.2 miles"
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = parameters[0].value
        distance = parameters[1].value

        fcs = arcpy.ListFeatureClasses()
        outList = []
        for fc in fcs:
            printArc('Processing: {0}'.format(fc))
            outputFile = 'C:/gispy/scratch/' + fc[:-4] + 'Out.shp'
            try:
                arcpy.Buffer_analysis(fc, outputFile, distance)
                printArc('Created {0}'.format(outputFile))
                outList.append(outputFile)
            except arcpy.ExecuteError:
                printArc(arcpy.GetMessages())

        results = ";".join(outList)

        printArc(results)

        arcpy.SetParameterAsText(2, results)


class ToolDefaultVals(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\08defaultVals'''
    def __init__(self):
        self.label = '08_defaultVals'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Areal_unit__required_
        param1 = arcpy.Parameter()
        param1.name = 'Areal_unit__required_'
        param1.displayName = 'Areal unit (required)'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Areal unit'
        param1.value = '5 SquareKilometers'

        # Cell_size
        param2 = arcpy.Parameter()
        param2.name = 'Cell_size'
        param2.displayName = 'Cell size'
        param2.parameterType = 'Optional'
        param2.direction = 'Input'
        param2.datatype = 'Cell Size'
        param2.value = 'MINOF'

        # Compression
        param3 = arcpy.Parameter()
        param3.name = 'Compression'
        param3.displayName = 'Compression'
        param3.parameterType = 'Optional'
        param3.direction = 'Input'
        param3.datatype = 'Compression'
        param3.value = u"'JPEG' 75"

        # Double
        param4 = arcpy.Parameter()
        param4.name = 'Double'
        param4.displayName = 'Double'
        param4.parameterType = 'Optional'
        param4.direction = 'Input'
        param4.datatype = 'Double'
        param4.value = '1.5'

        # Feature_class
        param5 = arcpy.Parameter()
        param5.name = 'Feature_class'
        param5.displayName = 'Feature class'
        param5.parameterType = 'Optional'
        param5.direction = 'Input'
        param5.datatype = 'Feature Class'
        relativePath = '../../../data/ch23/smallDir/trails.shp'
        param5.value = getAbsPath(relativePath)

        return [param1, param2, param3, param4, param5]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # Purpose: Print the arguments passed into a script tool.
        # Arguments: Variable (can be used for any number of arguments)
        printArgs(parameters)


class ToolSchema(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\09schema'''
    def __init__(self):
        self.label = '09_schema'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input_features
        param1 = arcpy.Parameter()
        param1.name = 'Input_features'
        param1.displayName = 'Input features'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Feature Set'
        relativePath = '../../../data/ch23/training/COVER4.lyr'
        param1.value = getAbsPath(relativePath)

        # output_features
        param2 = arcpy.Parameter()
        param2.name = 'output_features'
        param2.displayName = 'output features'
        param2.parameterType = 'Derived'
        param2.direction = 'Output'
        param2.datatype = 'Shapefile'

        return [param1, param2]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From getFeatures.py
        # Purpose: Copy the digitized feature set input into a shapefile
        #          and send this to the script tool as output.

        arcpy.env.overwriteOutput = True
        fs = parameters[0].value
        outputFeat = 'C:/gispy/scratch/out.shp'
        arcpy.CopyFeatures_management(fs, outputFeat)
        arcpy.SetParameterAsText(1, outputFeat)


class ToolEnvironments(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\10environments'''
    def __init__(self):
        self.label = '10_environ'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Workspace
        param1 = arcpy.Parameter()
        param1.name = 'Workspace'
        param1.displayName = 'Workspace'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Workspace'
        param1.defaultEnvironmentName = 'scratchWorkspace'

        return [param1]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # Purpose: Print the arguments passed into a script tool.
        # Arguments: Variable (can be used for any number of arguments)
        printArgs(parameters)


class ToolFilterRange(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\12FilterRange'''
    def __init__(self):
        self.label = '12_filterRange'
        self.description = 'Exponentiate the base by the power.'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Base
        param1 = arcpy.Parameter()
        param1.name = 'Base'
        param1.displayName = 'Base'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Double'

        # Power
        param2 = arcpy.Parameter()
        param2.name = 'Power'
        param2.displayName = 'Power'
        param2.parameterType = 'Optional'
        param2.direction = 'Input'
        param2.datatype = 'Long'
        param2.filter.type = 'Range'
        param2.filter.list = [1, 5]

        return [param1, param2]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From exponentiator.py
        # Purpose: Raise base to a power.
        # Arguments: base power(must be a number or #)

        base = float(parameters[0].value)

        # Handle optional argument.
        if not parameters[1].value:
            power = 1
            printArc('No exponent provided.  Using default power of 1.')
        else:
            power = float(parameters[1].value)

        # Calculate the exponentiation.
        result = base**power

        # Report the results.
        printArc('{0} raised to the {1} is {2}'.format(base, power, result))


class ToolFilterValueList(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\11filterValueList'''
    def __init__(self):
        self.label = '11_filterValueList'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # U_S__Region
        param1 = arcpy.Parameter()
        param1.name = 'U_S__Region'
        param1.displayName = 'U.S. Region'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'String'
        param1.filter.list = ['East North Central', 'East South Central', 'Middle Atlantic', 'Mountain',
                              'New England', 'Pacific', 'South Atlantic', 'West North Central', 'West South Central']
        return [param1]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From regional.py
        # Purpose: Print the names of states in the input region.capitalize

        region = parameters[0].value

        inf = 'C:/gispy/data/ch23/USA/USA_States_Generalized.shp'

        fields = ['SUB_REGION', 'STATE_NAME']

        sc = arcpy.da.SearchCursor(inf, fields)

        printArc('\n--States in {0}--'.format(region))

        for row in sc:
            if row[0] == region:
                printArc(row[1])
        printArc('\n')
        del sc


class ToolInputObtainedFrom(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\13inputObtainedFrom'''
    def __init__(self):
        self.label = '13_inputObtainedFrom'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input_feature_class
        param1 = arcpy.Parameter()
        param1.name = 'Input_feature_class'
        param1.displayName = 'Input feature class'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Feature Class'

        # Field_name
        param2 = arcpy.Parameter()
        param2.name = 'Field_name'
        param2.displayName = 'Field name'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'Field'
        param2.parameterDependencies = [param1.name]
        return [param1, param2]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        printArgs(parameters)


class ToolDerivedObtainedFrom(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\14derivedObtainedFrom'''
    def __init__(self):
        self.label = '14_derivedObtainedFrom'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input_file
        param1 = arcpy.Parameter()
        param1.name = 'Input_file'
        param1.displayName = 'Input file'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Feature Class'

        # Field1
        param2 = arcpy.Parameter()
        param2.name = 'Field1'
        param2.displayName = 'Field 1'
        param2.parameterType = 'Required'
        param2.direction = 'Input'
        param2.datatype = 'Field'
        param2.parameterDependencies = [param1.name]

        # Field2
        param3 = arcpy.Parameter()
        param3.name = 'Field2'
        param3.displayName = 'Field 2'
        param3.parameterType = 'Required'
        param3.direction = 'Input'
        param3.datatype = 'Field'
        param3.parameterDependencies = [param1.name]

        # New_field_name
        param4 = arcpy.Parameter()
        param4.name = 'New_field_name'
        param4.displayName = 'New field name'
        param4.parameterType = 'Required'
        param4.direction = 'Input'
        param4.datatype = 'String'

        # Output_file
        param5 = arcpy.Parameter()
        param5.name = 'Output_file'
        param5.displayName = 'Output file'
        param5.parameterType = 'Derived'
        param5.direction = 'Output'
        param5.datatype = 'Feature Class'
        param5.parameterDependencies = [param1.name]

        return [param1, param2, param3, param4, param5]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From combineFields.py
        # Purpose: Create a new field that is the sum of two existing fields.
        dataset = parameters[0].value.value
        field1 = parameters[1].value
        field2 = parameters[2].value
        newfield = parameters[3].value
        arcpy.AddField_management(dataset, newfield)
        expression = '!{0}!+!{1}!'.format(field1, field2)
        arcpy.CalculateField_management(dataset, newfield, expression, 'PYTHON')

        arcpy.SetParameterAsText(4, dataset)


class ToolSymbology(object):
    '''From C:\gispy\sample_scripts\ch23\toolboxes\propertyExamples.tbx\15symbology'''
    def __init__(self):
        self.label = '15_symbology'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input_data
        param1 = arcpy.Parameter()
        param1.name = 'Input_data'
        param1.displayName = 'Input data'
        param1.parameterType = 'Required'
        param1.direction = 'Input'
        param1.datatype = 'Feature Class'
        param1.filter.list = ['Polygon']

        # Output_data
        param2 = arcpy.Parameter()
        param2.name = 'Output_data'
        param2.displayName = 'Output data'
        param2.parameterType = 'Derived'
        param2.direction = 'Output'
        param2.datatype = 'Feature Class'
        layerFilePath = getAbsPath('../../../data/ch23/training/starPoints.lyr')
        param2.symbology = layerFilePath

        return [param1, param2]

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # From feature2point.py
        # Purpose: Find the centroids of the input polygons.

        arcpy.env.overwriteOutput = True
        inputFile = parameters[0].value.value
        outputFile = 'C:/gispy/scratch/Points.shp'

        # Find points based on the input.
        arcpy.FeatureToPoint_management(inputFile, outputFile)

        # Return the results to the tool.
        arcpy.SetParameterAsText(1, outputFile)
