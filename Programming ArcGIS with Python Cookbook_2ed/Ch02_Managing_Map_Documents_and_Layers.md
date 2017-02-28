
# Chapter 2: Managing Map Documents and Layers

In this chapter, we will cover the following recipes:  
* Referencing the current map document  
* Referencing map documents on a disk  
* Getting a list of layers in a map document  
* Restricting the list of layers  
* Zooming in to selected features  
* Changing the map extent  
* Adding layers to a map document  
* Inserting layers into a map document  
* Updating layer symbology  
* Updating layer properties  
* Working with time-enabled layers in a data frame  

## 2.1 Introduction

__The ArcPy mapping module provides some really exciting features for mapping automation__, including the ability to manage map documents and layer files, as well as the data within these files.  
Support is provided to automate map export and print, to create PDF map books, and publish map documents to ArcGIS Server map services.  
This is an incredibly useful module for accomplishing many of the day-to-day tasks performed by GIS analysts.  
  
In this chapter, you will learn how to use the ArcPy mapping module to manage map documents and layer files.  
You will also learn how to add and remove geographic layers and tables from map document files, insert layers into data frames, and move layers around within the map document.  
Finally, you will learn how to update layer properties and symbology.  

## 2.2 Referencing the current map document

When running a geoprocessing script from the ArcGIS Python window or a custom script tool, you will often need to make a reference to the map document which is currently loaded in ArcMap.  
This is typically the fist step in your script before you perform geoprocessing operations against layers and tables in a map document.  
In this recipe, you will learn how to reference the current map document from your Python geoprocessing script.  


### 2.2.1 Getting ready


```python
mxd = mapping.MapDocument("CURRENT")
```

### 2.2.2 How to do it

Follow these steps to learn how to access the currently active map document in ArcMap:  
1. Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
2. Click on the Python window button located on the main ArcMap toolbar.  
3. Import the arcpy.mapping module by typing the following into the Python window. Here, and in future recipes, we'll assign the arcpy.mapping module to a variable called mapping. This will make your code easier to read and cut down on the amount of code you have to write. Instead of having to prefi all your code with arcpy. mapping, you can just refer to it as mapping. It is not required that you follow this form, but it does make your code cleaner and faster to write. Furthermore, you can name the variable as you wish. For example, instead of calling it mapping you may call it MAP or mp or whatever makes sense. import arcpy.mapping as mapping  
4. Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable by typing the following into the Python Window below the fist line of code that you added in the last step:  
```
mxd = mapping.MapDocument("CURRENT")  
```
5. Set a title for map document:  
```
mxd.title = "Crime Project"  
```
6. Save a copy of the map document fie with the saveACopy()  method:  
```
mxd.saveACopy("c:/ArcpyBook/Ch2/crime_copy.mxd")  
```
7. Navigate to File | Map Document Properties, in order to view the new title you gave to the map document.  
8. You can check your work by examining the c:\ArcpyBook\code\Ch2\ReferenceCurrentMapDocument.py solution file.  


### 2.2.3 How it works

The MapDocument class has a constructor that creates an instance of this class.  
In object-oriented programming, an instance is also known as an object.  
The constructor for MapDocument can accept either the CURRENT keyword or a path to a map document file on a local or remote drive.  
The constructor creates an object and assigns it to the variable mxd.  
You can then access the properties and methods available on this object using dot notation.  
In this particular case, we printed out the title of the map document file using the MapDocument.title property and we also used the MapDocument.saveACopy()  method to save a copy of the map document file.  


## 2.3 Referencing map documents on a disk

In addition to being able to reference the currently active map document file in ArcMap, you can also access map document files that are stored on a local or remote drive by using the MapDocument() constructor.
In this recipe, you'll learn how to access these map documents.


### 2.3.1 Getting ready

As I mentioned earlier, you can also reference a map document file that resides somewhere on your computer or a shared server.  
This is done simply by providing a path to the file.  
This is a more versatile way of obtaining a reference to a map document because it can be run outside the ArcGIS Python window.  
Later, when we will discuss parameters in a script, you'll understand that you can make this path a parameter so that the script is even more versatile, with the ability to input a new path each time it is needed.  


### 2.3.2 How to do it

Follow these steps to learn how to access a map document stored on a local or remote drive:  
  
1.  Open the IDLE development environment from Start | All Programs | ArcGIS | Python 2.7 | IDLE.  
  
2.  Create a new IDLE script window by navigating to File | New Window from the IDLE shell window.  
  
3.  Import arcpy.mapping:  
```  
import arcpy.mapping as mapping  
```  
4.  Reference the copy of the crime map document that you created in the last recipe:  
```  
mxd = mapping.MapDocument("c:/ArcpyBook/Ch2/crime_copy.mxd")  
```  
  
5.  Print the title of the map document:  
```  
print(mxd.title)  
```  
  
6.  Run the script, and you will see the following output:  
```  
Crime Project  
```  
  
7.  You can check your work by examining the c:\ArcpyBook\code\Ch2\ ReferenceMapDocumentOnDisk.py solution file.  
   


### 2.3.3 How it works

The only difference between this recipe and the last one is that we provided a reference to a map document file on a local or remote drive rather than using the CURRENT keyword.  
This is the recommended way of referencing a map document file unless you know for sure that your geoprocessing script will be run inside ArcGIS, either in the Python window or as a custom script tool.  


## 2.4 Getting a list of layers in a map document

Frequently, one of the first steps in a geoprocessing script is to obtain a list of layers in the map document.  
Once obtained, your script may then cycle through each of the layers and perform some type of processing.  
The mapping module contains a ListLayers() function, which provides the capability of obtaining this list of layers.  
In this recipe, you will learn how to get a list of layers contained within a map document.  


### 2.4.1 Getting ready

The arcpy.mapping module contains various list functions to return lists of layers, data frames, broken data sources, table views, and layout elements.  
These list functions normally function as the first step in a multistep process, in which the script needs to get one or more items from a list for further processing.  
Each of these list functions returns a Python list, which, as you know from earlier in the book, is a highly functional data structure for storing information.  
  
Normally, the list functions are used as a part of a multistep process, in which creating a list is only the first step.  
Subsequent processing in the script will iterate over one or more of the items in this list.  
For example, you might obtain a list of layers in a map document and then iterate through each layer looking for a specific layer name, which will then be subjected to further geoprocessing.  

In this recipe, you will learn how to obtain a list of layers from a map document file.  


### 2.4.2 How to do it

Follow these steps to learn how to get a list of layers from a map document:  
  
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
2.  Click on the Python window button from the main ArcMap toolbar.  
3.  Import the arcpy.mapping module:  
```  
import arcpy.mapping as mapping  
```  
4.  Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable:  
```  
mxd = mapping.MapDocument("CURRENT")  
```  
5.  Call the ListLayers() function and pass a reference to the map document:  
```  
layers = mapping.ListLayers(mxd)  
```  
6.  Start a for loop and print out the name of each layer in the map document:  
```  
for lyr in layers: print(lyr.name)  
```  
7.  Run the script to see the following output (you can check your work by examining the  
c:\ArcpyBook\code\Ch2\GetListLayers.py solution file):  
```  
Burglaries in 2009  
Crime Density by School District Bexar County Boundary  
Test Performance by School District Bexar County Boundary  
Bexar County Boundary Texas Counties School_Districts Crime Surface  
Bexar County Boundary  
```  


### 2.4.3 How it works

The ListLayers() function retrieves a list of layers in a map document, specific data frame, or layer file.  
In this case, we passed a reference to the current map document to the ListLayers() function, which should retrieve a list of all the layers in the map document.  
The results are stored in a variable called layers, which is a Python list that can be iterated with a for loop.  
This Python list contains one or more Layer objects.  
   


### 2.4.4 There's more

The __ListLayers()__ function is only one of the many list functions provided by the __arcpy.mapping__ module.  
Each of these functions returns a Python list containing data of some type.  
Some of the other list functions include __ListTableViews()__, which returns a list of Table objects; ListDataFrames(), which returns a list of DataFrame objects; and __ListBoomarks()__, which returns a list of bookmarks in a map document.  
There are additional list functions, many of which we'll cover later in this book.  
   


## 2.5 Restricting the list of layers

In the previous recipe, you learned how to get a list of layers by using the ListLayers() function.  
There will be times when you will not want a list of all the layers in a map document, but rather only a subset of the layers.  
__The ListLayers() function allows you to restrict the list of layers that is generated__.  
In this recipe, you will learn how to restrict the layers returned using a wildcard and a specific data frame from the ArcMap table of contents.  
 


### 2.5.1 Getting ready

By default, if you only pass a reference to the map document or layer file, the ListLayers() function will return a list of all the layers in these files.  
However, you can restrict the list of layers returned by this function by using an optional wildcard parameter or by passing in a reference to a specific data frame.  
A wildcard is a character that will match any character or sequence of characters in a search.  
This will be demonstrated in this recipe.  
  
> If you're working with a layer file (.lyr), you can't restrict layers with a data frame.  
Layer files don't support data frames.  
  
In this recipe, you will learn how to restrict the list of layers returned by ListLayers() through the use of a wildcard and data frame.  
  


### 2.5.2 How to do it

Follow these steps to learn how to restrict a list of layers from a map document:  
  
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
2.  Click on the Python window button from the main ArcMap toolbar.  
3.  Import the arcpy.mapping module:  
```  
import arcpy.mapping as mapping  
```  
4.  Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable:  
```  
mxd = mapping.MapDocument("CURRENT")  
```  
5.  Get a list of data frames in the map document and search for a specific data frame named Crime (please note that text strings can be surrounded by either single or double quotation marks):  
```  
for df in mapping.ListDataFrames(mxd): if df.name == 'Crime':  
```  
  
6.  Call the ListLayers() function and pass a reference to the map document, a wildcard to restrict the search, and the data frame found in the last step to further restrict the search. The ListLayers() function should be indented inside the if statement you just created:  
```  
layers = mapping.ListLayers(mxd,'Burg*',df)  
```  
7.  Start a for loop and print out the name of each layer in the map document:  
```  
for layer in layers: print(layer.name)  
```  
8.  The complete script should appear as follows or you can consult the solution file at c:\ArcpyBook\code\Ch2\RestrictLayers.py:  
  
9.  Run the script to see the following output:  
```  
Burglaries in 2009  
```  


### 2.5.3 How it works

The ListDataFrames() function is another list function that is provided by arcpy.mapping.  
This function returns a list of all the data frames in a map document.  
We then loop through each of the data frames returned by this function, looking for a data frame that has the name Crime.  
If we do find a data frame that has this name, we call the ListLayers() function, passing in the optional wildcard value of Burg* as the second parameter, and a reference to the Crime data frame.  
The wildcard value passed in as the second parameter accepts any number of characters and an optional wildcard character (*).  
  
In this particular recipe, we searched for all the layers that begin with the characters Burg and have a data frame named Crime.  
Any layers found matching these restrictions were then printed.  
Keep in mind that all we did in this case was print the layer names, but in most cases, you would be performing additional geoprocessing with the use of tools or other functions, and having a shorter list will speed up your script and will keep things neat and tidy.  
  


## 2.6 Zooming in to selected features

Creating selection sets in ArcMap is a common task.  
Selection sets are often created as the result of an attribute or spatial query, but they can also occur when a user manually selects features and sometimes, under some additional circumstances.  
To better visualize selection sets, users often zoom to the extent of the selected feature.  
This can be accomplished programmatically with Python in several ways.  
In this recipe, you will learn how to zoom to all the selected features in a data frame as well as an individual layer.  



### 2.6.1 Getting ready

The DataFrame.zoomToSelectedFeatures property zooms to the extent of all the selected features from all the layers in the data frame.  
Essentially, it performs the same operation as the __Selection | Zoom to Selected Features__ operation.  
One difference is that it will zoom to the full extent of all the layers if no features are selected.  
  
Zooming to the extent of selected features in an individual layer requires you to use the Layer object.  
The Layer object includes a __getSelectedExtent()__ method that you can call to zoom to the extent of the selected records.  
This returns an Extent object, which you can then use as a parameter that is passed into the __DataFrame.panToExtent()__ method.  


### 2.6.2 How to do it

Follow these steps to learn how to get and set the active data frame and active view ArcMap:  
  
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
2.  In the ArcMap Table Of Contents pane, make sure that Crime is the active data frame.  
3.  In the Table Of Contents pane, click on the List By Selection button.  
4.  Make the Bexar County Boundaries layer unselectable by clicking on the toggle button just to the right of the layer name:  
  
5.  Click on the List By Source button in the Table Of Contents pane. Using the Select Features tool, drag a box around the cluster of burglaries inside the Northside ISD boundary. This should select the boundaries of a specific school district along with some burglaries as shown in the following diagram:  
  
  
6.  Click on the Python window button from the main ArcMap toolbar.  
7.  Import the arcpy.mapping module:  
```  
import arcpy.mapping as mapping  
```  
  
8.  Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable:  
```       
mxd = mapping.MapDocument("CURRENT")  
```  
  
9.  Get the active data frame (Crime) and zoom to the selected features:  
```  
mxd.activeDataFrame.zoomToSelectedFeatures()  
```  
  
10. If no records have been selected, a call to zoomToSelectedFeatures() will zoom to the extent of all the records in the data frame.  
Clear the selected features by navigating to Selection | Clear Selected Features.  
This will clear the selection set.  
Now, execute the same line of code again to see how this affects the operation of the zoomToSelectedFeatures() method: mxd.activeDataFrame.zoomToSelectedFeatures()  
  
11. Now, we'll zoom to the extent of the selected features in a specific layer.  
Using the Select Features tool, drag a box around the cluster of burglaries inside the Northside ISD boundary.  
  
12. First, get a reference to the Crime data frame.  
Calling the ListDataFrames() function and passing in a wildcard of Crime will return a Python list containing a single item.  
We pull this item out using [0], which returns the fi st and only item in the list:  
```  
df = mapping.ListDataFrames(mxd, "Crime")[0]  
```  
13. Now, we'll get a reference to the Burglaries layer, which contains some selected features.  
The following code uses a wildcard * to search for the Burglaries in  2009 layer within the data frame that we referenced in the last line of code.  
The ListLayers() function returns a Python list and we use [0] to pull out the first and  
only layer containing the word Burglaries:  
```  
layer = mapping.ListLayers(mxd,"Burglaries*",df)[0]  
```  
14. Finally, we'll set the extent of the data frame by getting the extent of the selected features in the layer:  
```  
df.extent = layer.getSelectedExtent  
```  
15. The complete script for zooming to the selected features of a layer should appear as follows or you can consult the solution file at c:\ArcpyBook\code\Ch2\ ZoomSelectedExtent.py:  
```  
import arcpy.mapping as mapping  
mxd = mapping.MapDocument("CURRENT")  
df = mapping.ListDataFrames(mxd, "Crime")[0]  
layer = mapping.ListLayers(mxd,"Burglaries*",df)[0] df.extent = layer.getSelectedExtent  
```  


### 2.6.3 How it works

In this recipe, you learned how to zoom to the extent of all the selected records from all the layers in a data frame as well as how to zoom to the extent of all the selected records from a specifi layer in a data frame.  
Zooming to the extent of all the selected records from all the layers in a data frame simply requires that you get a reference to the active data frame and then call zoomToSelectedFeatures() .  
  
Zooming to the extent of the selected records within a specifi layer requires a little more coding.  
After importing the arcpy.mapping module and getting a reference to the map document, we then got a reference to the Crime data frame.  
Using the ListLayers() function we passed in a reference to the data frame as well as a wildcard that searched for the layers that begin with the text Burglaries.  
The ListLayers()  function returned a Python list and since we knew that we only had one layer that matched the wildcard search, we pulled out the fist layer and assigned it to a variable called layer.  
Finally, we set the extent of the data frame using layer.getSelectedExtent.  


### 2.7 Changing the map extent

There will be many occasions when you will need to change the map extent.  
This is frequently the case when you are automating the map production process and need to create many maps of different areas or features.  
There are a number of ways that the map extent can be changed with arcpy.  
However, for this recipe, we'll concentrate on using a defiition expression to change the extent.  


### 2.7.1 Getting ready

The DataFrame class has an extent property that you can use to set the geographic extent.  
This is often used in conjunction with the Layer.definitionQuery property that is used to defie a defiition query for a layer.  
In this recipe, you will learn how to use these objects and properties to change the map extent.  


### 2.7.2 How to do it

Follow these steps to learn how to get a list of layers from a map document:  
1. Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
2. Click on the Python window button from the main ArcMap toolbar.  
3. Import the arcpy.mapping module:  
```py  
import arcpy.mapping as mapping  
```  
4. Reference the currently active document (Crime_Ch2.mxd) and assign the  
reference to a variable:  
```py  
mxd = mapping.MapDocument("CURRENT")  
```  
5. Create a for loop that will loop through all the data frames in the map document:  
```py  
for df in mapping.ListDataFrames(mxd):  
```  
6. Find the data frame called Crime and a specifi layer that we'll apply the defiition query against:  
```py  
if df.name == 'Crime':  
  layers = mapping.ListLayers(mxd,'Crime Density by School District',df)  
```  
7. Create a for loop that will loop through the layers.  
There will only be one, but we'll create the loop anyway.  
In the for loop, create a defiition query and set the new extent of the data frame:  
```py  
for layer in layers:  
query = '"NAME" = \'Lackland ISD\''  
layer.definitionQuery = query  
df.extent = layer.getExtent()  
```  
8. The entire script should appear as follows or you can consult the solution file at c:\ArcpyBook\code\Ch2\ChangeMapExtent.py:   
```py
import arcpy.mapping as mapping
mxd = mapping.MapDocument("CURRENT")
for df in mapping.ListDataFrames(mxd):
    if (df.name == 'Crime'):
        layers = mapping.ListLayers(mxd,'Crime Density by School District',df)
        for layer in layers:
            query = '"NAME" = \'Lackland ISD\''
            layer.definitionQuery = query
            df.extent = layer.getExtent()
```  
9. Save and run the script.  
The extent of the data view should update so that it visualizes only the features matching the defiition expression, as shown in the following screenshot:  


### 2.7.3 How it works

This recipe used a defiition query on a layer to update the map extent.  
Near the end of the script, you created a new variable called query that held the defiition expression.  
The defiition expression was set up to fid school districts with a name of Lackland ISD.  
This query string was then applied to the definitionQuery property.  
Finally, the df.extent property was set to the returned value of layer.getExtent() .  


## 2.8 Adding layers to a map document

There will be many situations where you will need to add a layer to a map document.  
The mapping module provides this functionality through the AddLayer() function.  
In this recipe, you will learn how to add a layer to a map document using this function.  


### 2.8.1 Getting ready

The arcpy.mapping module provides the ability to add layers or group layers into an existing map document file.  
You can take advantage of the ArcMap auto-arrange functionality, which automatically places a layer in the data frame for visibility.  
This is essentially the same functionality as is provided by the Add Data button in ArcMap, which positions a layer in the data frame based on geometry type and layer weight rules.  
  
When adding a layer to a map document, the layer must reference an existing layer found in a layer file on disk, the same map document and data frame, the same map document with a different data frame, or a completely separate map document.  
A layer can be either a layer in a map document or a layer in a .lyr file.  
To add a layer to a map document, you must first create an instance of the Layer class and then call the AddLayer() function, passing in the new layer along with the data frame where it should be placed and rules for how it is positioned.  


### 2.8.2 How to do it

Follow these steps to learn how to add a layer to a map document:  
  
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
2.  Click on the Python window button from the main ArcMap toolbar.  
3.  Import the arcpy.mapping module:  
```py  
import arcpy.mapping as mapping  
```  
4. Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable:  
```py  
mxd = mapping.MapDocument("CURRENT")  
```  
5.  Get a reference to the Crime data frame, which is the first data frame in the list returned by ListDataFrames(). The [0] value, specified at the end of the code, gets the first data frame returned from the ListDataFrames() method, which returns a list of data frames. Lists are 0-based, so in order to retrieve the first data frame, we provide an index of 0:  
```py  
df = mapping.ListDataFrames(mxd)[0]  
```  
6.  Create a Layer object that references a .lyr file:  
```py  
layer = mapping.Layer(r"C:\ArcpyBook\data\School_Districts.lyr")  
```  
7.  Add the layer to the data frame:  
```py 
mapping.AddLayer(df,layer,"AUTO_ARRANGE")  
```  
8.  You can consult the solution file at c:\ArcpyBook\code\Ch2\ AddLayersMapDocument.py.  
Run the script.  
The School_Districts.lyr file will be added to the data frame, as shown in the following screenshot:  
  
  


### 2.8.3 How it works

In the first two lines, we simply referenced the arcpy.mapping module and got a reference to the currently active map document.  
Next, we created a new variable called df, which held a reference to the Crime data frame.  
This was obtained through the ListDataFrames() function that returned a list of data frame objects.  
We then used list access to return the first item in the list, which is the Crime data frame.  
A new Layer instance, called layer, was then created from a layer file stored on disk.  
This layer file was called School_Districts.lyr.  
Finally, we called the AddLayer() function, passing in the data frame where the layer should ideally reside along with a reference to the layer, and a parameter indicating that we wanted to use the auto-arrange feature.  
In addition to allowing ArcMap to automatically place the layer into the data frame using auto-arrange, you can also specifically place the layer at either the top or bottom of the data frame or a group layer using the BOTTOM or TOP position.  
   
    

### 2.8.4 There's more...

In addition to providing the capability of adding a layer to a map document, arcpy.mapping also provides an AddLayerToGroup() function, which can be used to add a layer to a group layer.  
The layer can be added to the top or bottom of the group layer or you can use auto- arrange for placement.  
You may also add layers to an empty group layer.  
However, just as with regular layer objects, group layers cannot be added to a layer file.  
Layers can also be removed from a data frame or group layer.  
RemoveLayer() is the function used to remove a layer or group layer.  
In the event that two layers have the same name, only the first is removed, unless your script is set up to iterate.  


## 2.9 Inserting layers into a map document

__The AddLayer() function can be used to add a layer to a map document either through auto- arrange or as the first or last layer in a data frame.__  
However, it doesn't provide the control you need for inserting a layer in a specific position within a data frame.  
__For this added control, you can use the InsertLayer() function__.  
In this recipe, you will learn how to control the placement of layers that are added to a data frame.  
   


### 2.9.1 Getting ready

The AddLayer() function simply adds a layer into a data frame or a group layer and places the layer automatically using auto-arrange.  
You can choose to have the layer placed at the top or bottom of either.  
The InsertLayer() method allows you to have more precise positioning of a new layer into a data frame or a group layer.  
It uses a reference layer to specify a location and the layer is added either before or after the reference layer, as specified in your code.  
Since InsertLayer() requires the use of a reference layer, you can't use this method on an empty data frame.  
This is illustrated in the following screenshot, where District_Crime_Join is the reference layer and School_Districts is the layer to be added.  
The School_Districts layer can be placed either before or after the reference layer using InsertLayer():   


### 2.9.2 How to do it

Follow these steps to learn how to use InsertLayer() to insert a layer into a data frame:   
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.   
2.  Click on the Python window button from the main ArcMap toolbar.   
3.  Import the arcpy.mapping module:   
```py   
import arcpy.mapping as mapping   
```   
4.  Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable:   
```py   
mxd = mapping.MapDocument("CURRENT")   
```py   
5.  Get a reference to the Crime data frame:   
```py   
df = mapping.ListDataFrames(mxd, "Crime")[0]   
```   
   
6.  Define the reference layer:   
```py   
refLayer = mapping.ListLayers(mxd, "Burglaries*", df)[0]   
```py   
   
7.  Define the layer to be inserted relative to the reference layer:   
```py   
insertLayer = mapping.Layer(r"C:\ArcpyBook\data\CityOfSanAntonio.gdb\Crimes2009")   
```   
   
8.  Insert the layer into the data frame:   
```py   
mapping.InsertLayer(df,refLayer,insertLayer,"BEFORE")   
```   
9.  You can consult the solution file at c:\ArcpyBook\code\Ch2\ InsertLayerMapDocument.py to verify the accuracy of your code.   
10. Run the script. The Crimes2009 feature class will be added as a layer to the data frame, as seen in the following screenshot:   

### 2.9.3 How it works

After obtaining references to the arcpy.mapping module, current map document file, and the Crime data frame, our script then defines a reference layer.  
In this case, we used the ListLayers() function with a wildcard of Burglaries*, and the Crime data frame to restrict the list of layers returned to only one item.  
This item should be the Burglaries in 2009 layer.  
We used Python list access with a value of 0 to retrieve this layer from the list and assigned it to a Layer object.  
Next, we defined the insert layer, a new Layer object that references the Crimes2009 feature class from the CityOfSanAntonio geodatabase.  
Finally, we called the InsertLayer() function passing in the data frame, reference layer, layer to be inserted, and keyword indicating that the layer to be inserted should be placed before the reference layer.  
This is illustrated in the following screenshot:   


### 2.9.4 There's more

You can also reposition a layer that is already in a data frame or a group layer.  
The MoveLayer() function provides the ability to reposition the layer within a data frame or a group layer.  
Movement of a layer must be within the same data frame.  
You can't move a layer from one data frame to another.  
Just as with InsertLayer(), MoveLayer() uses a reference layer to reposition the layer.  


## 2.10 Updating layer symbology

There may be times when you will want to change the symbology of a layer in a map document.  
This can be accomplished through the use of the UpdateLayer() function, which can be used to change the symbology of a layer as well as various properties of a layer.  
In this recipe, you will use the UpdateLayer() function to update the symbology of a layer.  
    


### 2.10.1 Getting ready

The arcpy.mapping module also gives you the capability of updating layer symbology from your scripts by using the UpdateLayer() function.  
For example, you might want your script to update a layer's symbology from a graduated color to a graduated symbol, as illustrated   in the following screenshot.  
UpdateLayer() can also be used to update various layer properties, but the default functionality is to update the symbology.  
Since UpdateLayer() is a robust function that is capable of altering both symbology and properties, you do need to understand the various parameters that can be supplied as an input:  
  


### 2.10.2 How to do it

Follow these steps to learn how to update the symbology of a layer using UpdateLayer():  
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
  
2.  Click on the Python window button from the main ArcMap toolbar.  
  
3.  Import the arcpy.mapping module:  
```py  
import arcpy.mapping as mapping  
```  
  
4.  Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable:  
```py  
mxd = mapping.MapDocument("CURRENT")  
```  
  
5.  Get a reference to the Crime data frame:  
```py  
df = mapping.ListDataFrames(mxd, "Crime")[0]  
```  
  
6.  Define the layer that will be updated:  
```py  
updateLayer = mapping.ListLayers(mxd,"Crime Density by School District",df)[0]  
```  
  
7.  Define the layer that will be used to update the symbology:  
```py  
sourceLayer = mapping.Layer(r"C:\ArcpyBook\data\CrimeDensityGradSym.lyr")  
```  
  
8.  Call the UpdateLayer() function to update the symbology:  
```py  
mapping.UpdateLayer(df,updateLayer,sourceLayer,True)  
```  
  
9.  You can consult the solution file at c:\ArcpyBook\code\Ch2\ UpdateLayerSymbology.py to verify the accuracy of your code.  
  
10. Run the script. The Crime Density by School District layer will now be symbolized with graduated symbols instead of graduated colors, as shown in the following screenshot:  


### 2.10.3 How it works

In this recipe, we used the UpdateLayer() function to update the symbology of a layer.  
We didn't update any properties, but we'll do so in the next recipe.  
The UpdateLayer() function requires that you pass several parameters including a data frame, layer to be updated, and a reference layer from which the symbology will be pulled and applied to update the layer.  
In our code, the updateLayer variable holds a reference to the Crime Density by School District layer, which will have its symbology updated.  
The source layer from which the symbology will  be pulled and applied to the updated layer is a layer file (CrimeDensityGradSym.lyr), containing graduated symbols.  
  
To update the symbology for a layer, you must first ensure that the update layer and the source layer have the same geometry (point, line, or polygon).  
You also need to check that the attribute definitions are the same in some cases, depending upon the renderer.  
For example, graduated color symbology and graduated symbols are based on a particular attribute.  
In this case, both the layers had polygon geometry and a CrimeDens field containing crime density information.  
  


Once we had references to both the layers, we called the UpdateLayer() function, passing in the data frame and layers along with a fourth parameter that indicated that we're updating symbology only.  
We supplied a True value as this fourth parameter, indicating that we were only updating the symbology and not properties:    

```py  
mapping.UpdateLayer(df,updateLayer,sourceLayer,True)  
```


### 2.10.4 There's more

The UpdateLayer() function also provides the ability to remove one layer and add another layer in its place.  
The layers can be completely unrelated, so there is no need to ensure that the geometry type and attribute field are the same as you would when redefining the symbology of a layer.  
This switching of layers essentially executes a call to RemoveLayer() and then a call to AddLayer() as one operation.  
To take advantage of this functionality, you must set the symbology_only parameter to False.  

## 2.11 Updating layer properties

In the previous recipe, you learned how to update the symbology of a layer.  
As I mentioned, UpdateLayer() can also be used to update various properties of a layer, such as field aliases, query definitions, and others.  
In this recipe, you will use UpdateLayer() to alter various properties of a layer.  


### 2.11.1 Getting ready 

You can also use the UpdateLayer() function to update a limited number of layer properties.  
Specific layer properties, such as field aliases, selection symbology, query definitions, label fields, and others, can be updated using UpdateLayer().  
A common scenario is to have a layer in many map documents that needs to have a specific property changed across all the instances of the layer in all map documents.  
To accomplish this, you will have to use ArcMap to modify the layer with the appropriate properties and save it to a layer file.  
This layer file then becomes the source layer, which will be used to update the properties of another layer called update_layer.  
In this recipe, you'll use ArcMap to alter the properties of a layer, save to a layer file (.lyr) and then use Python to write a script that uses UpdateLayer() to apply the properties to another layer.  
  


### 2.11.2 How to do it

Follow these steps to learn how to update layer properties with UpdateLayer():  
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap. For this recipe, you will be working with the Burglaries in 2009 feature class, as shown in the following screenshot:  
  
2.  Double-click on the Burglaries in 2009 feature class in the Crime data frame to display the Layer Properties window, as shown in the following screenshot.  
Each of the tabs represents properties that can be set for this layer:  
  
3.  Click on the General tab and change the value in the Layer Name: textbox to the name, as shown in the following screenshot:  
  
4.  Click on the Definition Query tab and define the query, as shown in the following screenshot.  
You can use the Query Builder… button to define the query or simply type in the query:  
  
5.  Change the alias of the OFFDESC field to Offense Description, as shown in the next screenshot.  
6.  Click on the Fields tab in Layer Properties and make visible only those fields that are selected with a checkmark in the following screenshot.  
This is done by unchecking  the fields that you see in the following screenshot:  
  
7.  Click on OK to dismiss the Layer Properties dialog.  
  
8.  In the data frame, right-click on Burglaries – No Forced Entry and select Save as Layer File.  
  
9.  Save the file as c:\ArcpyBook\data\BurglariesNoForcedEntry.lyr.  
  
10. Right-click on the Burglaries – No Forced Entry layer and select Remove.  
   
11. Using the Add Data button in ArcMap, add the Crimes2009 feature class from the CityOfSanAntonio geodatabase.  
The feature class will be added to the data frame, as shown in the following screenshot:  
  
12. Open the Python window in ArcMap.  
  
13. Import the arcpy.mapping module:  
```py  
import arcpy.mapping as mapping  
```  
  
14. Reference the currently active document (Crime_Ch2.mxd) and assign the reference to a variable:  
```py  
mxd = mapping.MapDocument("CURRENT")  
```  
  
15. Get a reference to the Crime data frame:  
```py  
df = mapping.ListDataFrames(mxd, "Crime")[0]  
```  
  
16. Define the layer that will be updated:  
```py  
updateLayer = mapping.ListLayers(mxd,"Crimes2009",df)[0]  
```  
  
17. Define the layer that will be used to update the properties:  
```py  
sourceLayer = mapping.Layer(r"C:\ArcpyBook\data\ BurglariesNoForcedEntry.lyr")  
```  
  
18. Call the UpdateLayer() function to update the symbology:  
```py  
mapping.UpdateLayer(df,updateLayer,sourceLayer,False)  
```  
  
19. You can consult the solution file at c:\ArcpyBook\code\Ch2\ UpdateLayerProperties.py to verify the accuracy of your code.  
  
20. Run the script.  
  
21. The Crimes2009 layer will be updated with the properties associated with the BurglariesNoForcedEntry.lyr file.  
This is illustrated in the following screenshot.  
Turn on the layer to view the definition query that has been applied.  
You can also open the Layer Properties dialog to view the property changes that have been applied to the Crimes2009 feature class:  


## 2.12 Working with time-enabled layers in a data frame

In this recipe, you will learn how to time-enable a layer and data frame.  
You will then write a script that cycles through the time range for the layer and exports a PDF map showing crimes through time in seven-day intervals.  



### 2.12.1 Getting ready

The DataFrameTime object provides access to time management operations for time- enabled layers in a data frame.  
This object is returned when you reference the DataFrame.  
time property, and includes properties for retrieving the current time, end time, start time, time step interval, and others that are established by using the Time Slider Options dialog box and then saved with the map document.  
One or more layers in a data frame must be time-enabled for this functionality to be operational.  
  


### 2.12.2 How to do it

Follow these steps to learn how to work with time-enabled layers:  
  
1.  Open c:\ArcpyBook\Ch2\Crime_Ch2.mxd with ArcMap.  
  
2.  In the ArcMap Table Of Contents make sure Crime is the active data frame.  
  
3.  Open the Layer Properties dialog box for Burglaries in 2009 by right-clicking on the layer and selecting Properties. Select the Time tab, as shown in the following screenshot:  
  
Enable time for the layer by clicking on the Enable time on this layer checkbox.  
   
4.  Under Time properties, select Each feature has a single time field for Layer Time:.  
Select the SPLITDT field for the Time Field:.  
Define a Time Step Interval: of 7.00 Days, as shown in the following screenshot:  
  
Define the Layer Time Extent: by clicking the Calculate button, circled in the following screenshot:  
  
5.  Check the Time Step Interval: field. You may need to reset that to 7 Days.  
  
6.  Click on Apply and then OK.  
  
7.  In the ArcMap Tools toolbar, select the time slider options button to display the Time Slider Options dialog as shown in the following screenshot:  
  
8.  On the Time Display tab of the Time Slider Options dialog, make sure Time step interval: is set to 7.0 days.  
If not, set it to 7.0 days. Do the same for the Time window: option.  
  
9.  Click on OK.  
  
10. Save your map document.  
It's very important that you save the time-enabled data with your map document.  
The code you write next won't work unless you do so.  
  
11. Open the Python Window.  
  
12. Import the arcpy.mapping module:   
```py  
import arcpy.mapping as mapping  
```  
13. Reference the currently active document (Crime_Ch2.mxd), and assign the reference to a variable:  
```py  
mxd = mapping.MapDocument("CURRENT")  
```  
  
14. Retrieve the Crime data frame:  
```py  
df = mapping.ListDataFrames(mxd, "Crime")[0]  
```  
  
15. Generate the DataFrameTime object:  
```py  
dft = df.time  
```  
  
16. Set the DataFrameTime.currentTime property to the DataFrameTime. startTime property:  
```py  
dft.currentTime = dft.startTime  
```  
  
17. Start a while loop that will loop through the time while the currentTime is less than or equal to the endTime:  
```py  
while dft.currentTime <= dft.endTime:  
```  
  
18. Inside the while loop, create a file for each PDF that will be created, export the PDF, and reset the currentTime property.  
The entire while loop should appear as follows:  
```py  
while dft.currentTime <= dft.endTime:  
fileName = str(dft.currentTime).split(" ")[0] + ".pdf"  
mapping.ExportToPDF(mxd,os.path.join(r"C:\ArcpyBook\Ch2", fileName), df)  
print("Exported " + fileName) dft.currentTime = dft.currentTime + dft.timeStepInterval  
```  
  
19. The entire script should appear as follows. You can consult the solution file at c:\ArcpyBook\code\Ch2\TimeEnabledLayers.py to verify the accuracy of your code:  


### 2.12.3 How it works

The DataFrameTime object provides access to time management operations in a data frame.  
Several properties of DataFrameTime, including currentTime, startTime, endTime, and timeStepInterval, are used in this recipe.  
Initially, we set the currentTime property equal to the startTime property.  
The initial startTime was calculated when you set the Time Step Interval: properties in ArcMap.  
The while loop was set up to loop as long as the currentTime property is greater than the endTime property.  
Inside the loop, we created a fileName variable that is set to the currentTime property, plus an extension of .pdf.  
We then called the ExportToPDF() function, passing in a path and the filename.  
This should ideally export the page layout view to the PDF file.  
Finally, we updated the currentTime property by the timeStepInterval property that was set to 7.0 days in in the Time Step Interval: properties dialog.  
   

