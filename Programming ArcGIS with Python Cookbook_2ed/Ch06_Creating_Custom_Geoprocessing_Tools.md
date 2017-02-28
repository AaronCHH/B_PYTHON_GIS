
# Chapter 6: Creating Custom Geoprocessing Tools

In this chapter, we will cover the following recipes:  
* Creating a custom geoprocessing tool  
* Creating a Python toolbox  


## 6.1 Introduction

__In addition to accessing the system tools provided by ArcGIS, you can also create your own custom tools__.  
These tools work in the same way as system tools and can be used in ModelBuilder, a Python window, or standalone Python scripts.  
Many organizations build their own library of tools that perform geoprocessing operations specific to their data.  


## 6.2 Creating a custom geoprocessing tool

Along with being able to execute any of the available tools in your scripts, you can also create your own custom tools, which can also be called from a script.  
Custom tools are frequently created to handle geoprocessing tasks that are specific to an organization.  
These tools can be easily shared as well.  
   


### 6.2.1 Getting ready

In this recipe, you will learn how to create custom geoprocessing script tools by attaching a Python script to a custom toolbox in ArcToolbox.  
There are a number of advantages of creating a custom script tool.  
When you take this approach, the script becomes a part of the geoprocessing framework, which means that it can be run from a model, command line, or another script.  

Also, the script has access to the environment settings and help documentation of ArcMap.  
Other advantages include a nice, easy-to-use user interface and error prevention capabilities.  
Error prevention capabilities that are provided include a dialog box that informs the user of certain errors.  
These custom developed script tools must be added to a custom toolbox that you create, because the system toolboxes provided with ArcToolbox are read-only toolboxes, and thus can't accept new tools.  

In this recipe, you are going to be provided with a prewritten Python script that reads wildfire data from a comma-delimited text file, and writes this information to a point feature class called FireIncidents.  
References to these datasets have been hardcoded, so you are going to have to alter the script to accept dynamic variable inputs.  
You'll then attach the script to a custom tool in ArcToolbox to give your end users a visual interface to use the script.  


### 6.2.2 How to do it

The custom Python geoprocessing scripts that you write can be added to ArcToolbox inside custom toolboxes.  
You are not allowed to add your scripts to any of the system toolboxes, such as Analysis or Data Management.  
However, by creating a new custom toolbox, you can add scripts in this way:  
  
1. Open ArcMap with an empty map document file and open the ArcToolbox window.  
  
2. Right-click anywhere in the white space area of ArcToolbox and select Add Toolbox.  
  
3. Navigate to the C:\ArcpyBook\Ch6 folder.  
  
4. In the Add Toolbox dialog box, click on the new toolbox button. This will create a new toolbox with a default name of Toolbox.tbx; you will rename the toolbox in the next step:  
  
5. Name the toolbox WildfireTools.tbx:  
  
6. Open the toolbox by selecting WildfireTools.tbx and clicking on the Open button. The toolbox should now be displayed in ArcToolbox, as shown in the following screenshot:  
  
7.  Each toolbox should be given a name and an alias.  
The alias will be used to uniquely define your custom tool.  
Alias names should be kept short and should not include any special characters.  
Right-click on the new toolbox and select Properties.  
Add an alias of wildfire, as shown in the following screenshot:  

8.  In this next step, we will alter an existing Python script called InsertWildfires.  
py to accept dynamic inputs that will be provided by the user of the tool through the ArcToolbox interface.  
Open c:\ArcpyBook\Ch6\InsertWildfires.py in IDLE.  
Notice that we have hardcoded the path to our workspace as well as the comma- delimited text file containing the wildland fire incidents:
```py  
arcpy.env.workspace = "C:/ArcpyBook/data/Wildfires/WildlandFires.mdb" 
f = open("C:/ArcpyBook/data/Wildfires/NorthAmericaWildfires_2007275.txt","r")  
```  

9.  Delete the preceding two lines of code.  
In addition to this, we have also hardcoded the name of the output feature class:  
```py  
cur = arcpy.InsertCursor("FireIncidents")  
```  
This hardcoding limits the usefulness of our script.  
If the datasets move or are deleted, the script will no longer run.  
Additionally, the script lacks the flexibility to specify different input and output datasets.  
In the next step, we will remove this hardcoding and replace it with the ability to accept dynamic input.  
  
10. We will use the GetParameterAsText() function found in arcpy to accept dynamic input from the user.  
Add the following lines of code to the try block, so that your code appears as follows:  
```py  
try:  
    # the output feature class name 
    outputFC = arcpy.GetParameterAsText(0)  
    # template featureclass that defines the attribute schema 
    fClassTemplate = arcpy.GetParameterAsText(1)    
    # open the file to read  
    f = open(arcpy.GetParameterAsText(2),'r')
    arcpy.CreateFeatureclass_management (os.path.split(outputFC)[0], os.path.split(outputFC)[1], "point", fClassTemplate)  
```  
Notice that we call the CreateFeatureClass tool, found in the Data Management Tools toolbox, passing the outputFC variable along with the template feature class (fClassTemplate).  
This tool will create the empty feature class containing the output feature class defined by the user.  
  
11. You will also need to alter the line of code that creates an InsertCursor object. Change the line as follows:  
with arcpy.da.InsertCursor(outputFC) as cur:  
  
12. The entire script should appear as follows:  
```py  
#Script to Import data to a feature class within a geodatabase import arcpy, os  
try:  
    outputFC = arcpy.GetParameterAsText(0) 
    fClassTemplate = arcpy.GetParameterAsText(1)  
    f = open(arcpy.GetParameterAsText(2),'r') 
    arcpy.CreateFeatureclass_management(os.path.split(outputFC) [0], os.path.split(outputFC)[1],"point",fClassTemplate) 
    lstFires = f.readlines()  
    with arcpy.da.InsertCursor(outputFC) as cur: 
        cntr = 1  
        for fire in lstFires:  
            if 'Latitude' in fire: continue  
            vals = fire.split(",") latitude = float(vals[0]) longitude = float(vals[1]) confid = int(vals[2])  
            pnt = arcpy.Point(longitude, latitude) feat = cur.newRow()  
            feat.shape = pnt feat.setValue("CONFIDENCEVALUE", confid) cur.insertRow(feat)  
            arcpy.AddMessage("Record number" + str(cntr) + "written to feature class")  
            cntr = cntr + 1  
except:
    print arcpy.GetMessages() 
finally:
    f.close()  
```  
  
13. You can check your work by examining the c:\ArcpyBook\code\Ch6\ InsertWildfires.py solution file.  
  
14. In the next step, we will add the script that we just created to the Wildfire Tools toolbox as a script tool.  
  
15. In ArcToolbox, right-click on the Wildfire Tools custom toolbox that you created earlier and navigate to Add | Script.  
This will display the Add Script dialog, as shown in the following screenshot.  
Give your script a name, label, and description.  
The Name: field can not contain any spaces or special characters.  
The Label: field is the name that shows up next to the script.  
For this example, give it a label of Load Wildfires From Text.  
Finally, add some descriptive information that details the operations that the script will perform.  
  
16. The details relating to Name:, Label:, and Description: are shown in the following screenshot:  
  
17. Click on Next to display the next input dialog box for Add Script.  
  
18. In this dialog box, you will specify the script that will be attached to the tool.  
Navigate to c:\ArcpyBook\Ch6\InsertWildfires.py and add InsertWildfires.py as the script.  
  
19. You will also want to make sure that the Run Python script in process checkbox is selected, as shown in the following screenshot.  
Running a Python script in process.  
increases the performance of your script.    
  
20. Click on Next to display the parameter window, as shown in the following screenshot:  
Each parameter that you enter in this dialog box corresponds to a single call to GetParameterAsText(). Earlier, you altered your script to accept dynamic parameters through the GetParameterAsText() method. The parameters should be entered in this dialog box in the same order that your script expects to receive them. For instance, you inserted the following line of code in your code:  
outputFC = arcpy.GetParameterAsText(0)    
The first parameter that you add to the dialog box will need to correspond to this line.  
In our code, this parameter represents the feature class that will be created as a result of this script.  
You add parameters by clicking on the first available row under Display Name.  
You can enter any text in this row.  
This text will be displayed to the user.  
You will also need to select a corresponding data type for the parameter.  
In this case, Data Type should be set to Feature Class, since this is the expected data that will be gathered from the user.  
Each parameter also has a number of properties that can be set.  
Some of the more important properties include Type, Direction, and Default.  
  
21. Enter the information, as shown in the following screenshot, into your dialog box, for the output feature class.  
Make sure that you set Direction to Output:  
  
22. Next, we need to add a parameter that defines the feature class that will be used as the attribute template for our new feature class.  
Enter the following information in your dialog box:  
    
23. Finally, we need to add a parameter that will be used to specify the comma-delimited text file that will be used as an input in the creation of our new feature class.  
Enter the following information into your dialog box:  
  
24. Click on Finish.  
The new script tool will be added to your Wildfire Tools toolbox, as shown in the following screenshot:  
     
25. Now, we'll test the tool to make sure it works.  
Double-click on the script tool to display the dialog box, as shown in the following screenshot:  
    
26. Define a new output feature class, which should be loaded inside the existing WildlandFires.mdb personal geodatabase, as shown in the next screenshot.  
Click on the open folder icon and navigate to the WildlandFires.mdb personal geodatabase, which should be located in c:\ArcpyBook\data\Wildfires.  
  
27. You will also need to give your new feature class a name.  
In this case, we'll name the feature class TodaysWildfires, but the name can be whatever you'd like.  
In the following screenshot, you can see an example of how this should be done.  
Click on the Save button:  
  
28. For the attribute template, you will want to point to the FireIncidents feature class that has already been created for you.  
This feature class contains a fi  ld called CONFIDENCEVAL.  
This fi ld will be created in our new feature class.  
Click on the Browse button, navigate to c:\ArcpyBook\data\Wildfires\WildlandFires.  
mdb, and you should see the FireIncidents feature class.  
Select it and click on Add.  
    
29. Finally, the last parameter needs to point to our comma-delimited text file containing wildland fires.  
This file can be found at c:\ArcpyBook\data\ Wildfires\NorthAmericaWildfires_2007275.txt.  
Click on the Browse button and navigate to c:\ArcpyBook\data\Wildfires.  
Click on NorthAmericaWildfires_2007275.txt and click on the Add button.  
Your tool should appear as follows:  
    
30. Click on OK to execute the tool.  
Any messages will be written to the dialog box shown in the following screenshot.  
This is a standard dialog box for any geoprocessing tool.  
    
31. If everything is set up correctly, you should see the following screenshot, which shows that a new feature class will be added to the ArcMap display:    
  
32. In ArcMap, select add basemap and then choose the Topographic basemap.  
Click on the Add button to add the basemap layer.    
This will provide a reference for the data that you have just imported, as seen in the preceding screenshot.  


### 6.2.3 How it works

Almost all script tools have parameters, and the values are set for the tool dialog box.  
When the tool is executed, the parameter values are sent to your script.  
Your script reads these values and then proceeds with its work.  
Python scripts can accept parameters as input.  
Parameters, also known as arguments, allow your scripts to become dynamic.  
Up to this point, all of our scripts have used hardcoded values.  
By specifying input parameters for a script, you are able to supply the name of the feature class at runtime.  
This capability makes your scripts more versatile.  
   
  
The GetParameterAsText() method, which is used to capture parameter input, is zero-based with the first parameter entered occupying a 0 index and each successive parameter is incremented by 1.  
The output feature class that will be created by reading the comma-delimited text file is specified in the outputFC variable, which is retrieved by GetParameterAsText(0).  
With GetParameterAsText(1), we capture a feature class that will act as a template for the output feature class attribute schema.  
The attribute fields in the template feature class are used to define the fields that will populate our output feature class.  
Finally, GetParameterAsText(2) is used to create a variable called f, which will hold the comma-delimited text file that will be read.  


### 6.2.4 There's more

__The arcpy.GetParameterAsText() method is not the only way to capture information passed into your script.__  
When you call a Python script from the command line, you can pass in a set of arguments.  
When passing arguments to a script, each word must be separated  by a space.  
These words are stored in a zero-based list object called sys.argv.  
__With sys.argv, the first item in the list, referenced by the 0 index, stores the name of the script.__  
Each successive word is referenced by the next integer.  
Therefore, the first parameter will be stored in sys.argv[1], the second in sys.argv[2], and so on.  
These arguments can then be accessed from within your script.  
It is recommended that you use the GetParameterAsText() function rather than sys.argv, because GetParameterAsText() does not have a character limit, whereas sys.argv has a limit of 1,024 characters per parameter.  
__In either case, once the parameters have been read into the script, your script can continue execution using the input values.__  


## 6.3 Creating a Python toolbox

There are two ways to create toolboxes in ArcGIS: script tools in custom toolboxes that we covered in the last recipe, and script tools in Python toolboxes.  
Python toolboxes  were introduced in version 10.1 of ArcGIS and they encapsulate everything in one place: parameters, validation code, and source code.  
This is not the case with custom toolboxes, which are created using a wizard and a separate script that processes business logic.  


### 6.3.1 Getting ready

A Python Toolbox is similar to any other toolbox in ArcToolbox, but it is created entirely in Python and has a file extension of .pyt.  
It is created programmatically as a class named Toolbox.  
In this recipe, you will learn how to create a Python Toolbox and add a custom tool.  
After creating the basic structure of Toolbox and Tool, you'll complete the functionality of the tool by adding code that connects to an ArcGIS Server map service, downloads real-time data, and inserts it into a feature class.  
   


### 6.3.2 How to do it

Complete these steps to create a Python Toolbox and create a custom tool that connects to an ArcGIS Server map service, downloads real-time data, and inserts it into a feature class:  
  
1. Open ArcCatalog.  
You can create a python toolbox in a folder by right-clicking on the folder and selecting New | Python Toolbox.  
In ArcCatalog, there is a folder called Toolboxes and inside it is a My Toolboxes folder, as seen in this screenshot:  
  
2. Right-click on this folder and select New | Python Toolbox.  
  
3. The name of the toolbox is controlled by the file name.  
Name the toolbox InsertWildfires.pyt:  
    
4.  The Python Toolbox file (.pyt) can be edited in any text or code editor.  
By default, the code will open in Notepad.  
You can change this by setting the default editor for your script by going to Geoprocessing | Geoprocessing Options and going to the Editor section.  
You'll notice in the following screenshot that I have set my editor to PyScripter, which is my preferred environment.  
You may want to change this to IDLE or whatever development environment you are currently using.  
Please note that this step is not required though.  
As mentioned, by default, it will open your code in Notepad.  
  
5. Right-click on InsertWildfires.pyt and select Edit. This will open your development environment. Your development environment will vary depending on the editor that you have defined.  
  
6. Remember that you will not be changing the name of the class, which is Toolbox.  
However, you will rename the Tool class to reflect the name of the tool you want to create.  
Each tool will have various methods, including     init (), which is the constructor for the tool along with getParameterInfo(), isLicensed(), updateParameters(), updateMessages(), and execute().  
You can use the   init () method to set initialization properties, such as the tool's label and description.  
Look for the Tool class and change the name to USGSDownload.  
Also, set the label, and description, as seen in this code:  
```py
class USGSDownload(object):
    def __init__(self):  
    """Define the tool (tool name is the name of the class)."""  
    self.label = "USGS Download"  
    self.description = "Download from USGS ArcGIS Server instance"  
```

7.  You can use the Tool class as a template for other tools you'd like to add to the toolbox by copying and pasting the class and its methods.  
We're not going to do this in this particular exercise, but I wanted you to be aware of this fact.  
You will need to add each tool to the tools property of Toolbox.  
Add the USGS Download tool, as seen in this code: class Toolbox(object): 
```py    
def __init__(self):  
    """Define the toolbox (the name of the toolbox is the name of the .pyt file).""" 
    self.label = "Toolbox" self.alias = ""  
    # List of tool classes associated with this toolbox self.tools = [USGSDownload]  
```

8. When you close the code editor, your Toolboxes should automatically be refreshed.  
You can also manually refresh a toolbox by right-clicking on the toolbox and selecting Refresh.  
If a syntax error occurs in your code, the toolbox icon will change, as seen in the following screenshot.  
Note the red X next to the toolbox.  
  
9. You shouldn't have any errors at this time, but if you do, right-click on the toolbox and select Check Syntax to display the errors, as seen in the following screenshot.  
Note that if you have an error, it may be different from the following example:  
  
10. Assuming that you don't have any syntax errors, you should see the following Toolbox/ Tool structure:  
  
11. Almost all tools have parameters, and you set their values in the tool dialog box or within a script. When the tool is executed, the parameter values are sent to your tool's source code. Your tool reads these values and proceeds with its work. You use the getParameterInfo() method to define the parameters for your tool. Individual Parameter objects are created as part of this process. Add the following parameters in the getParameterInfo() method and then we'll discuss them:      
Each Parameter object is created using arcpy.Parameter and is passed a number of arguments that define the object.  
For the first Parameter object (param0), we are going to capture a URL for an ArcGIS Server map service containing current wildfire data.  
We give it a display name (ArcGIS Server Wildfire URL), which will be displayed in the dialog box for the tool, a name for the parameter, data type, parameter type (this is mandatory), and direction.  
In the case of the first parameter (param0), we also assign an initial value, which is the URL for an existing map service containing wildfire data.    
For the second parameter, we define an output feature class where the wildfire data that is read from the map service will be written.  
An empty feature class to store the data has already been created for you.  
Finally, we added both parameters to a Python list called params and return the list to the calling function  
  
12. The main work of a tool is done inside the execute() method.  
This is where the geoprocessing of your tool takes place.  
The execute() method, seen in the following code, can accept a number of arguments, including the tool (self), parameters, and messages:  
```py  
def execute(self, parameters, messages):   
    """The source code of the tool. """ return  
```

13. To access the parameter values that are passed into the tool, you can use the valueAsText() method.  
Add the following code to access the parameter values that will be passed into your tool.  
Remember, as seen in a previously mentioned step, that the first parameter will contain a URL for a map service containing wildfire data, and the second parameter is the output feature class where the data will be written:  
```py        
def execute(self, parameters, messages): 
    inFeatures = parameters[0].valueAsText  
    outFeatureClass = parameters[1].valueAsText  
```

14. At this point, you have created a Python toolbox, added a tool, defined the parameters for the tool, and created variables that will hold the parameter values that the end user has defined.  
Ultimately, this tool will use the URL that is passed into the tool to connect to an ArcGIS Server map service, download the current wildfire data, and write the wildfire data to a feature class.  
We'll do this next.  
  
15. Note that to complete the remainder of this exercise, you will need to install the Python requests (refer to http://docs.python-requests.org/en/latest/) module using pip (refer to https://pip.pypa.io/en/latest/installing.html).  
Do this now before proceeding to the next step.  
Installation instructions for both pip and requests can be found at the links provided.  
16. Next, add the code that connects to the wildfire map service to perform a query.  
In this step, you will also define the QueryString parameters that will be passed into the query of the map service.  
First, we'll import the requests and json modules by adding this code:  
```py  
import requests import json  
```

17. Then, create the payload variable that will hold the QueryString parameters.  
Notice that in this case we have defined a where clause so that only the fires greater than 5 acres in size will be returned.  
The inFeatures variable holds the URL:  
```py
def execute(self, parameters, messages): 
inFeatures = parameters[0].valueAsText  
outFeatureClass = parameters[1].valueAsText agisurl = inFeatures  
payload = { 'where': 'acres > 5','f': 'pjson', 'outFields': 'latitude,longitude,fire_name,acres'}  
```

18. Submit the request to the ArcGIS Server instance and the response should be stored in a variable called r.  
Print a message to the dialog indicating the response: def execute(self, parameters, messages): inFeatures = parameters[0].valueAsText outFeatureClass = parameters[1].valueAsText agisurl = inFeatures payload = { 'where': 'acres > 5','f': 'pjson', 'outFields': 'latitude,longitude,fire_name,acres'}  
```py  
r = requests.get(inFeatures, params=payload)  
```

19. Let's test the code to make sure we're on the right track.  
Save the file and refresh your toolbox in ArcCatalog.  
Execute the tool and leave the default URL.  
If everything works as expected, you should see a JSON object output of the progress dialog.  
Your output will probably vary somewhat.  
  
20. Return to the execute() method and convert the JSON object to a Python dictionary: def execute(self, parameters, messages): inFeatures = parameters[0].valueAsText outFeatureClass = parameters[1].valueAsText  
```py  
agisurl = inFeatures  
payload = { 'where': 'acres > 5','f': 'pjson', 'outFields': 'latitude,longitude,fire_name,acres'}  
r = requests.get(inFeatures, params=payload)    
decoded = json.loads(r.text)  
```
  
21. Create an InsertCursor by passing the output feature class defined in the tool dialog along with the fields that will be populated.  
We then start a for loop that loops through each of the features (wildfires) that have been returned from the request to the ArcGIS Server map service.  
The decoded variable is a Python dictionary.  
Inside the for loop, we retrieve the fire name, latitude, longitude, and acres from the attributes dictionary.  
Finally, we call the insertRow() method to insert a new row into the feature class along with the fire name and acres as attributes.  
The progress information is written to Progress Dialog and the counter is updated.  
The execute() method should now appear as follows:  
   
22. Save the file and refresh your Python Toolbox if needed.  
  
23. You can check your work by examining the c:\ArcpyBook\code\Ch6\ InsertWildfires_PythonToolbox.py solution file.  
  
24. Double-click on the USGS Download tool.  
  
25. Leave the default URL and select the RealTimeFires feature class in the WildlandFires geodatabase found in c:\ArcpyBook\data.  
The RealTimeFires feature class is empty and has fields for NAME and ACRES.  
  
26. Click on OK to execute the tool.  
The number of features written to the feature class will vary depending on the current wildfire activity.  
Most of the time, there is at least a little bit of activity, but it is possible (though not likely) that there wouldn't be any wildfires in the U.S:  
  
27. View the feature class in ArcMap to see its features.  
You may want to add a basemap layer to provide a reference, as seen in this screenshot:  
  


### 6.3.3 How it works

__The newer style ArcGIS Python Toolbox provides a Python-centric way of creating your custom script tools.__  
The older style of creating custom script tools in ArcGIS for Desktop uses a combination of Python along with a wizard-based approach to define various aspects of the tool.  
The newer approach provides a more straightforward method for creating your tools.  
All the tools that you create are contained within a Toolbox class that should not be renamed.  

By default, a single Tool class will be created inside Toolbox.  
This Tool class should be renamed.  
In this recipe, we renamed it USGSDownload.  
Inside the USGSDownload class, the getParameterInfo() and execute() methods are present, among others.  

Using  the getParameterInfo() method, Parameter objects can be defined to hold input data.  
In this tool, we defined a Parameter to capture a URL for an ArcGIS Server map service containing live wildfire data and a second Parameter object to reference a local feature class to hold the data.  

__Finally, the execute() method is triggered when the user clicks on the OK button in the tool.__  
Parameter information is sent as an argument to the execute() method   in the form of the parameters variable.  
Inside this method, a request to obtain the wildfire data from the remove ArcGIS Server instance is submitted using the Python requests module.  
The response is returned as a json object that is converted into a Python dictionary stored in a variable called decoded.  
The fire name, latitude, longitude, and acres are pulled out of the decoded variable and written to the local feature class using an InsertCursor object from the arcpy.da module.  
__We'll cover the arcpy.da module in great detail in a later chapter of the book.__  
   


### 6.3.4 There's more


```python

```
