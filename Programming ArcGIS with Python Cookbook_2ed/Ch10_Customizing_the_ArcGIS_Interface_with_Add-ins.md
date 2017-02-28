
# Chapter 10: Customizing the ArcGIS Interface with Add-ins

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 10: Customizing the ArcGIS Interface with Add-ins](#chapter-10-customizing-the-arcgis-interface-with-add-ins)
  * [10.1 Introduction](#101-introduction)
  * [10.2 Downloading and installing the Python Add-in Wizard](#102-downloading-and-installing-the-python-add-in-wizard)
    * [10.2.1 Getting ready](#1021-getting-ready)
    * [10.2.2 How to do it](#1022-how-to-do-it)
    * [10.2.3 How it works](#1023-how-it-works)
  * [10.3 Creating a button add-in and using the Python add-ins module](#103-creating-a-button-add-in-and-using-the-python-add-ins-module)
    * [10.3.1 Getting ready](#1031-getting-ready)
    * [10.3.2 How to do it](#1032-how-to-do-it)
    * [10.3.3 How it works](#1033-how-it-works)
  * [10.4 Installing and testing an add-in](#104-installing-and-testing-an-add-in)
    * [10.4.1 Getting ready](#1041-getting-ready)
    * [10.4.2 How to do it](#1042-how-to-do-it)
    * [10.4.3 How it works](#1043-how-it-works)
  * [10.5 Creating a tool add-in](#105-creating-a-tool-add-in)
    * [10.5.1 Getting ready](#1051-getting-ready)
    * [10.5.3 How it works](#1053-how-it-works)
    * [10.5.4 There's more](#1054-theres-more)

<!-- tocstop -->


In this chapter, we will cover the following recipes:

* Downloading and installing the Python Add-in Wizard
* Creating a button add-in and using the Python add-ins module
* Installing and testing an add-in
* Creating a tool add-in



## 10.1 Introduction

In this chapter, we're going to cover the creation, testing, editing, and sharing of add-ins created with Python.
Add-ins provide a way of adding user interface items to ArcGIS for Desktop through a modular code base designed to perform specific actions.
Interface components can include buttons, tools, toolbars, menus, combo boxes, tool palettes, and application extensions.
The add-in concept was first introduced in ArcGIS for Desktop 10.0 and could be created with .NET or Java.
However, starting with the release of ArcGIS 10.1, add-ins can now be created with Python.
Add-ins are created using Python scripts and an XML file that defines how a user interface should appear.
Add-ins provide an easy way to distribute user interface customizations to end users.
No installation programs are necessary.
A single compressed file with a file extension of sriaddin is copied to a well-known folder, and ArcGIS for Desktop handles the rest.
To simplify the development even further, a Python Add-In Wizard has been provided by Esri.
You can download the wizard from the Esri website.
We'll do this in the first recipe of this chapter.

 There are a number of add-in types that can be created.
Buttons and tools are the simplest types of add-ins that you can create.
Buttons simply execute business logic when clicked.
Tools are similar to buttons but require interaction with the map before the business logic is executed.
Combo boxes provide a list of choices for the user to select from.
There are also a number of container objects, including menus, toolbars, tool palettes, and application extensions.
Menus act as a container for buttons or other menus.
Toolbars are a container for buttons, tools, combo boxes, tool palettes, and menus.
They are the most versatile type of container for add-ins.
Tool palettes also act as a container for tools, and need to be added to a toolbar before the tools are exposed.
Finally, application extensions are the most complex add-in type.
This type of add-in coordinates activities between other components and is responsible for listening and responding to various events, such as the addition or removal of a layer from a data frame.


## 10.2 Downloading and installing the Python Add-in Wizard

Esri provides a tool that you can use to make the development of add-ins easier.
The Python Add-In Wizard can be downloaded from the Esri website and is a great resource to create add-ins.



### 10.2.1 Getting ready

The Python Add-In Wizard is a great resource to create the necessary files for an add-in.
It generates the required files for the add-ins from a visual interface.
In this recipe, you will download and install the Python Add-In Wizard.



### 10.2.2 How to do it

Follow these steps to learn how to download and install the Python Add-in Wizard:

1.  Open a web browser and navigate to http://www.arcgis.com/home/item.html?id=5f3aefe77f6b4f61ad3e4c62f30bff3b.
You should see a web page similar to the following screenshot:

2.  Click on the Open button to download the installer file.

3.  Using Windows Explorer, create a new folder called Python Add-In Wizard somewhere on your computer. The name of the folder is irrelevant, but to keep things simple and easy to remember, you should go with Python Add-In Wizard or something similar.

4.  Unzip the file to this new folder There are many utilities that can be used to unzip a file. Each will differ slightly in how they are used but with WinZip, you should be able to right-click on the file and select Extract.

5.  Open the bin folder that was unzipped and double-click on addin_assistant. exe to run the wizard. In the following screenshot, I have created a new folder called Python Add-In Wizard and unzipped the downloaded file. The bin folder was created, and inside this folder is a file called addin_assistant.exe:

6.  Double-clicking on addin_assistant.exe will prompt you to choose a directory to use as the add-in project root:


### 10.2.3 How it works

The Python Add-In Wizard is a visual interface tool that you can use to create add-ins for ArcGIS for Desktop.
It greatly simplifies the process through a point-and-click tool.
In the next recipe, you'll create basic ArcGIS for Desktop add-ins using the wizard.



## 10.3 Creating a button add-in and using the Python add-ins module

A Button add-in is the simplest type of add-in and is also the most commonly used. With button add-ins, the functionality that you code in your script is executed each time the button is clicked on.

### 10.3.1 Getting ready

Creating an add-in project is the first step in the creation of a new add-in.
To create a project using the Python Add-In Wizard, you select a working directory, enter various project settings, and click on the Save button.
Creation of the add-in then follows a well-defined process, as illustrated in the following screenshot:

You must first create a container for the add-in and this can either be in the form of a toolbar or menu.
Next, create the button, tool, or any other add-in that you want to add to the container.
In this recipe, we'll create a button.
Next, you need to edit the Python script that is associated with the button.
You'll also want to test the button to make sure it works as expected.
Finally, you can share the add-in with others.
In this recipe, you'll learn how to use the Add-In Wizard to create a button add-in for ArcGIS for Desktop.
The button add-in will execute code that uses the pythonaddins module to display a dialog that allows the user to add feature classes that have already been created for a data frame.



### 10.3.2 How to do it

Follow these steps to learn how to create a button add-in:

1. Open the ArcGIS Python Add-In Wizard by double-clicking on the addin_assistant.
exe file located in the bin folder, where you extracted the wizard.

2. Create a new project folder called Wildfire_Addin and select OK:

3. The Project Settings tab should be active initially and display the working directory that you just created.
By default, ArcMap should be the selected product, but you should verify that this is the case:

4. Give your project a name. We'll call it Load Wildfire Data Addin:

5. By default, the Version: is 0.1.
You can change this if you like.
Version numbers should change as you update or make additions to your tool.
This helps with the tracking and sharing of your add-ins:

6. The Name: and Version: properties are the only two required properties.
It's a good practice to go ahead and add the company, description, and author information, as shown in the following screenshot.
Add your own information:

7. You may also wish to add an image for the add-in.
A file called wildfire.png has been provided for this purpose in the C:\ArcpyBook\Ch10 folder:

8. The Add-In Contents tab is used to define the various add-ins that can be created.
In this step, we're going to create a toolbar to hold a single button add-in that runs  a wildfire script, which imports fires from a text file to a feature class.
Click on the Add-In Contents tab:

9. In the Add-In Contents tab, right-click on TOOLBARS and select New Toolbar.
Give the toolbar a Caption:, accept the default name, and make sure the Show Initially checkbox is selected: While it doesn't do a whole lot functionally, the Toolbar add-in is very important because it acts as a container for other add-ins, such as buttons, tools, combo boxes, tool palettes, and menus.
Toolbars can be floating or docked.
Creating a toolbar add- in is easy using the Python Add-In Wizard.

10. Click on the Save button.

11. Now, we'll add a button by right-clicking on the new Wildfire Toolbar option and selecting New Button.

12. Fill in the Button details, including a Caption:, Class Name:, ID (Variable Name):, Tooltip:, and so on.
You can also include an Image for control:.
I haven't done so in this case, but you may choose to do this.
This information is saved to the configuration file for the add-in:

13. Click on the Save button.
Add-ins have a Python script that they are attached to.
This file, by default, will be named AddIns_addin.py and can be found in the install directory of your working project folder.

14. We've already created a custom ArcToolbox Python script tool that loads a comma-delimited text file from a disk containing wildfire data to a feature class.
We will be using the results of this script in our add-in.
In Windows Explorer, go to the addin directory that you created earlier.
It should be called Wildfire_Addin.
Go  to the Install folder and you should find a file called WildfireAddin_addin.py. Load this file into your Python editor.

15. In this next step, we'll write code that uses the pythonaddins module to open a dialog that allows you to add one or more layers to a selected data frame.
The OpenDialog() and GetSelectedTOCLayerorDataFrame() functions in pythonaddins are used to accomplish this task.
Find the onClick(self) method, which is shown in the following code snippet.
This method is triggered when the button is clicked.
Remove the pass statement from the onClick event and add this code:

```py
import arcpy
import pythonaddins

class ButtonClassImportWildfires(object):
    """Implementation for Wildfire_addin.button (Button)""" def   init  (self):
    self.enabled = True self.checked = False
    def onClick(self):
        layer_files = pythonaddins.OpenDialog('Select Layers to Add', True, r'C:\ArcpyBook\data\Wildfires', 'Add')
        mxd = arcpy.mapping.MapDocument('current')
        df = pythonaddins.GetSelectedTOCLayerOrDataFrame()
        if not isinstance(df, arcpy.mapping.Layer):
            for layer_file in layer_files:
                layer = arcpy.mapping.Layer(layer_file)
                arcpy.mapping.AddLayer(df, layer)
else:
    pythonaddins.MessageBox('Select a data frame', 'INFO', 0)
```

16. Save the file.

17. You can check your work by examining the C:\ArcpyBook\code\Ch10\ WildfireAddIn.py solution file.
In the next recipe, you will learn how to install your new add-in.



### 10.3.3 How it works

As you've seen in this recipe, the Python Add-In Wizard handles the creation of the add-in through a visual interface.
However, behind the scenes, the wizard creates a set of folders and files for the add-in.
The add-in file structure is really quite simple.
Two folders and a set of files comprise the add-in structure.
You can see this structure in the following screenshot:     The Images folder contains any icons or other image files used by your add-in.
In this recipe, we used the wildfire.png image.
So, this file should now be in the Images folder.
The Install folder contains the Python script that handles the business logic of the add-in.
This is the file you will work with extensively to code the add-in.
It performs whatever business logic needs to be performed by the buttons, tools, menu items, and so on.
The config.xml file in the main folder of the add-in defines the user interface and static properties, such as the name, author, version, and so on.
The makeaddin.py file can be double-clicked on to create the .esriaddin file, which wraps everything into a compressed file with an .esriaddin extension.
This .esriaddin file is what will be distributed to end users, so that the add-in can be installed.



## 10.4 Installing and testing an add-in

You'll want to test add-ins before distributing them to your end users.
To test these, you first need to install the add-in.



### 10.4.1 Getting ready

In the working folder of your add-in, the makeaddin.py script can be used to copy all files and folders to a compressed add-in folder in a working directory with the <working folder name>.esriaddin file format.
Double-click on this .esriaddin file to launch the Esri ArcGIS add-in installation utility, which will install your add-in.
You can then go into ArcGIS for Desktop and test the add-in.
The custom toolbar or menu may already be visible and ready to test.
If it is not visible, go to the Customize menu and click on Add-in Manager.
The Add- In Manager dialog box lists the installed add-ins that target the current application.
Add-in information, such as name, description, and image, which are entered as project settings, should be displayed.



### 10.4.2 How to do it

1. Inside the main folder for your add-in, there will be a Python script file called makeaddin.py.
This script creates the .esriaddin file.
Double-click on the script to execute and create the .esriaddin file.
This process is illustrated in the following screenshot:

2. To install the add-in for ArcGIS for Desktop, double-click on the Widlfire_Add-In.
esriaddin file, which will launch the Esri ArcGIS Add-In Installation Utility window, as shown in the following screenshot:

3. Click on Install Add-In. If everything was successful, you should see the following message:

4. To test the add-in, open ArcMap.
Your add-in may already be active.
If not, navigate to Customize | Add-In Manager.
This will display the Add-In Manager dialog box, as shown in the following screenshot.
You should be able to see the add-in that you created:

5. If needed, select the Customize button.
To add the toolbar to the application, click on the Toolbars tab and choose the toolbar you created: The add-in should now be displayed, as seen in this screenshot:

6. Click on the button and in the dialog that is displayed, navigate to the Wildfires layers you created earlier inside the WildlandFires.mdb.
Select and add them to the display: Here, you will see the output of having selected one or more layers from the dialog:


### 10.4.3 How it works

The utility will place the add-in into a well-known folder discoverable by ArcGIS for Desktop.
The locations of this folder are as follows:
* Windows 8: C:\Users\<username>\Documents\ArcGIS\AddIns\Desktop10.3
* Vista/7: C:\Users\<username>\Documents\ArcGIS\AddIns\Desktop10.3
* XP: C:\Documents and Settings\<username>\My Documents\ArcGIS\AddIns\Desktop10.3

A folder with a unique globally unique identifier or GUID name will be created inside the well- known folder.
The add-in will reside inside this unique folder name.
This is illustrated in the following screenshot.
When ArcGIS for Desktop starts, it will search these directories and load the add-ins:

The add-in will look similar to the following:

>The default add-in folder is located in the ArcGIS folder within your user account.
For example, if your ArcGIS installation is version 10.1, the add-in is copied to C:\users\<username>\ Documents\ArcGIS\AddIns\Desktop10.1 on a Vista or Windows 7 operating system.

You can also use a private network drive to distribute add-ins to end users.
The Add-In Manager in ArcGIS for Desktop adds and maintains lists of folders that can be searched for add-ins.
Select the Options tab and then Add Folder to add a network drive to the list.



## 10.5 Creating a tool add-in

Tool add-ins are similar to buttons with the exception that tools require some type of interaction with the map.
The zoom-in tool, for example, is a type of tool.
Tools should be placed inside a toolbar or tool palette.
The properties similar to those of a button.
You'll also need to edit the Python script.


### 10.5.1 Getting ready

The Tool class has a number of properties, including cursor, enabled, and shape.
The cursor property sets the cursor for the tool when it is clicked on, and is defined as an integer value corresponding to the cursor types, as follows:

By default, tools are enabled.
This can be changed, though, by setting the enabled property to false.
Finally, the shape property specifi  s the type of shape to be drawn and it can be a line, rectangle, or circle.
These properties are typically set inside the constructor of the tool, which is defi  d by the     init  method, as shown in the following code example.
The self object refers to the current object (a tool in this case) and is a variable that refers to this current object:
```py
def __init__(self):
    self.enabled = True
    self.cursor = 3
    self.shape = 'Rectangle'
```
There are a number of functions associated with the Tool class.
All classes will have  a constructor, which is used to define the properties for the class.
You saw an example of this __init__ function earlier.
Other important functions of the tool class include onRectangle(), onCircle(), and onLine().
These functions correspond to the shape that will be drawn on the map with the tool.
The geometry of the drawn shape is passed into the function.
There are also a number of mouse and key functions that can be used.
Finally, the deactivate() function can be called when you want to deactivate the tool.


We've already seen the constructor for the Tool class in action.
This function, called     init , is used to set various properties for the tool when it is created.
Here, we've also shown the onRectangle() function for the Tool class.
This function is called when a rectangle is drawn on the map.
The geometry of the rectangle is passed into the function along with a reference to the tool itself:
```py`m
def onRectangle(self, rectangle_geometry):
```

In this recipe, you will learn how to create a tool add-in that responds to the user dragging a rectangle on the map.
The tool will use the Generate Random Points tool to generate points within the rectangle.


### 10.5.2 How to do it

Follow these steps to create a tool add-in with the ArcGIS Python Add-In Wizard:

1. Open the ArcGIS Python Add-In Wizard by double-clicking on the addin_ assistant.exe file that is located in the bin folder, where you extracted the wizard.

2. Create a new project folder called Generate_Random_Points and select OK.

3. Enter properties, including Name:, Version:, Company:, Description:, and Author:, in the Project Settings tab:

4. Click on the Add-In Contents tab.

5. Right-click on TOOLBARS and select New Toolbar.

6. Set the caption for the toolbar to Random Points Toolbar.

7. Right-click on the newly created Random Points Toolbar and select New Tool.

8. Enter items for the tool as shown in the following screenshot:

9. Click on Save. This will generate the folder and file structure for the add-in.

10. Go to the Install folder for the new add-in and open GenerateRandomPoints_ addin.py in IDLE.

11. Add the following code to the __init__ function, which is the constructor for the tool:
```py
def __init__(self):
    self.enabled = True
    self.cursor = 3
    self.shape = 'Rectangle'
```

12. In the onRectangle() function, write a code to generate a set of random points within the rectangle drawn on the screen:
```py
import arcpy
import pythonaddins
def __init__(self):
    self.enabled = True
    self.cursor = 3
    self.shape = 'Rectangle'
def onRectangle(self, rectangle_geometry):
    extent = rectangle_geometry
    arcpy.env.workspace = r'c:\ArcpyBook\Ch10'
    if arcpy.Exists('randompts.shp'):
        arcpy.Delete_management('randompts.shp')
        randompts = arcpy.CreateRandomPoints_management(arcpy.env.workspace,
        'randompts.shp',"",rectangle_geometry)
        arcpy.RefreshActiveView() return randompts
```

13. Save the file.

14. You can check your work by examining the C:\ArcpyBook\code\Ch10\ GenerateRandomPoints_addin.py solution file.

15. Generate the .esriaddin file by double-clicking on the makeaddin.py file in the main folder for the add-in.

16. Install the add-in by double-clicking on GenerateRandom_Points.esriaddin.

17. Open ArcMap and add the Generate Random Points toolbar, if necessary.

18. Add the BexarCountyBoundaries feature class from C:\ArcpyBook\data\ CityOfSanAntonio.gdb.

19. Test the add-in by dragging a rectangle on the map.
The output should appear similar to the following screenshot.
Your map will vary because the points are generated randomly:



### 10.5.3 How it works

Tool add-ins are very similar to button add-ins with the difference being that tool add-   ins require some sort of interaction with the map before the functionality is triggered.
An interaction with the map can include a number of things, such as clicking on the map, drawing a polygon or rectangle, or performing various mouse or key events.
Python code is written to respond to one or more of these events.
In this recipe, you learned how to write a code that responds to the onRectangle() event.
You also set various properties inside the constructor for the add-in, including cursor and shape, which will be drawn on the map.


### 10.5.4 There's more

There are a number of additional add-ins that you can create.
The ComboBox add-in provides a drop-down list of values that the user can select from, or alternatively type a new value into an editable field.
As with the other add-ins, you'll first want to create a new project with the Python Add-In Wizard, add a new toolbar, and then create a combo box to add to the toolbar.
The Tool Palette provides a way of grouping related tools.
It does need to be added to an existing toolbar.
By default, tools will be added to the palette in a grid-like pattern.
The Menu add-in acts as a container for buttons and other menus.
Menus, in addition to being displayed by the ArcGIS for Desktop Add-in Manager, will also be displayed in the Customize dialog box for ArcGIS for Desktop.
Application extensions are used to add specific sets of related functionality to ArcGIS for Desktop.
Several examples include Spatial Analyst, 3D Analyst, and Business Analyst.
Typically, application extensions are responsible for listening for events and handling them.
For example, you could create an application extension that saves the map document file each time a user adds a layer to the map.
Application extensions also coordinate activities between components.




```python

```
