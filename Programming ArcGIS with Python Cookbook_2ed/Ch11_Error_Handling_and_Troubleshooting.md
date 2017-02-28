
# Chapter 11: Error Handling and Troubleshooting

In this chapter, we will cover the following recipes:  
  
* Exploring the default Python error message  
* Adding Python exception handling structures (try/except/else)  
* Retrieving tool messages with GetMessages()  
* Filtering tool messages by the level of severity  
* Testing for and responding to specific error messages  


## 11.1 Introduction

Various messages are returned during the execution of ArcGIS geoprocessing tools and functions.   
These messages can be informational in nature or indicate warning or error conditions that can result in the tool not creating the expected output or result in outright failure of the tool to be executed.   
These messages do not appear as message boxes.   
Instead, you will need to retrieve them by using various ArcPy functions.   
Up to this point in the book, we have ignored the existence of these messages, warnings, and errors.   
This is mainly due to the fact that I wanted you to concentrate on learning some basic concepts, without adding the extra layer of code complexity that is necessary to create robust geoprocessing scripts that can handle error situations gracefully.   
This being said, it's now time that you learn how to create geoprocessing and Python exception handling structures that will enable you to create versatile geoprocessing scripts.   
These scripts can handle messages that indicate warnings, errors, and general information, which    are generated while your script is running.   
These code details will help make your scripts more flexible and less error prone.   
You've already used the basic try and except blocks to perform some basic error handling.   
However, in this chapter, we'll go into more detail about why and how these structures are used.   
   


## 11.2 Exploring the default Python error message

By default, Python will generate an error message whenever it encounters a problem in your script.  
These error messages will not always be very informative to the end user who is running the script.  
However, it is valuable to take a look at these raw messages.  
In later recipes, we'll use Python error handling structures to get a cleaner look at the errors and respond as required.  


### 11.2.1 Getting ready

In this recipe, we will create and run a script that intentionally contains error conditions.   
We will not include any geoprocessing or Python exception handling techniques in the script.   
We are doing this intentionally because we want you to see the error information returned by Python.   
    


### 11.2.2 How to do it

Follow these steps to see a raw Python error message, which is generated when an error occurs while a tool is being executed in a script:  
1. Open IDLE and create a new script.  
  
2. Save the script to C:\ArcpyBook\Ch11\ErrorHandling.py.  
  
3. Import the arcpy module:  
```py      
import arcpy  
```  
  
4. Set the workspace:  
```py  
arcpy.env.workspace = "c:/ArcpyBook/data"  
```  
  
5. Call the Buffer tool. The Buffer tool requires a buffer distance be entered as one of its parameters. In this code block, we have intentionally left out the distance parameter:  
```py  
arcpy.Buffer_analysis("Streams.shp","Streams_Buff.shp")  
```  
  
6. You can check your work by examining the C:\ArcpyBook\code\Ch11\ ErrorHandling1.py solution file.  
  
7. Run the script. You should see the following error message:  
```py  
Runtime error Traceback (most recent call last): File "<string>", line 1, in <module> File "c:\program files (x86)\arcgis\ desktop10.1\arcpy\arcpy\analysis.py", line 687, in Buffer  raise e ExecuteError: Failed to execute. Parameters are not valid. ERROR 000735: Distance [value or field]: Value is required Failed to execute (Buffer).  
```  


### 11.2.3 How it works

This output error message isn't terribly informative.  
If you are a fairly experienced programmer, you'll generally be able to make out what the problem is in this case (it did not include buffer distance).  
However, in many cases, the returned error message will not give you much information that you can use to resolve the problem.  
Errors in your code are simply a fact of life in programming.  
However, how your code responds to these errors, also called exceptions, is very important.  
You should plan to handle errors gracefully through the use of Python error handling structures, which examine arcpy generated exceptions and act accordingly.  
Without these structures in place, your scripts will fail immediately, frustrating your users in the process.  
   


## 11.3 Adding Python exception handling structures (try/except/else

Python has built-in exception handling structures that allows you to capture error messages that are generated.  
Using this error information, you can then display a more appropriate message to the end user and respond to the situation as needed.  


### 11.3.1 Getting ready

Exceptions are unusual or error conditions that occur in your code. Exception statements in Python enable you to trap and handle errors in your code, allowing you to gracefully recover from error conditions.  
In addition to error handling, exceptions can be used for a variety of other things, including event notification and handling of special cases.  
Python exceptions occur in two ways.  
Exceptions in Python can either be intercepted or  triggered.  
When an error condition occurs in your code, Python automatically triggers an exception, which may or may not be handled by your code.  
It is up to you as a programmer to catch an automatically triggered exception.  
Exceptions can also be triggered manually by your code.  
In this case, you would also provide an exception handling routine to catch these manually triggered exceptions.  
You can manually trigger an exception by using the raise statement.  
The try/except statement is a complete, compound Python statement, which is used   to handle exceptions.  
This variety of try statement starts with a try header line followed by a block of indented statements, then one or more optional except clauses that name exceptions to be caught, and an optional else clause at the end.  
The try/except/else statement works as follows.  
Once inside a try statement, Python marks the fact that you are in a try block and knows that any exception condition that occurs within this block will be forwarded to the various except statements for handling.  
     
Each statement inside the try block is executed.  
Assuming there aren't any conditions in which exceptions occur, the code pointer will then jump to the else statement and execute the code block contained within the else statement before moving to the next line of code below the try block.  
If an exception occurs inside the try block, Python searches for a matching exception code.  
If a matching exception is found, the code block inside the except block is executed.  
The code then reappears below the full try statement.  
The else statements are not executed in this case.  
If a matching exception header is not found, Python will propagate the exception to a try statement above this code block.  
In the event that no matching except header is found, the exception comes out of the top level of the process.  
This results in an unhandled exception and you wind up with the type of error message that we saw in our first recipe in this chapter.  
This is illustrated in the following figure:  
    
In this recipe, we're going to add in some basic Python exception handling structures.  
There are several variations of the try/except/else/finally exception handling structure.  
In this recipe, we'll start with a very simple try/except structure.  
   


### 11.3.2 How to do it

Follow these steps to add Python error handling structures to a script.

1. If necessary, open the C:\ArcpyBook\Ch11\ErrorHandling.py file in IDLE.

2. Alter your script to include a try/except block:
```py
import arcpy try:
arcpy.env.workspace = "c:/ArcpyBook/data" arcpy.Buffer_analysis("Streams.shp","Streams_Buff.shp")
except: print("Error")
```

3. You can check your work by examining the C:\ArcpyBook\code\Ch11\ ErrorHandling2.py solution file.

4. Save and run the script. You should see the simple Error message. This is no more helpful than the output we received in our first recipe. In fact, it's even less useful. However, the point of this recipe is simply to introduce you to the try/except error handling structure.



### 11.3.3 How it works

This is an extremely simple structure.  
The try block indicates that everything indented under the try statement will be subject to exception handling.  
If an exception of any type is found, control of the code processing jumps to the except section and prints the error message(s), which in this case is simply Error.  
Now, as I mentioned, this is hardly informative to your users, but hopefully, it gives you a basic idea of how the try/except blocks work, and as a programmer you will better understand any errors reported by your users.  
In the next recipe, you'll learn how to add tool-generated messages to this structure.  
   


### 11.3.4 There's more

The other type of try statement is the try/finally statement, which allows for finalization actions.  
When a finally clause is used in a try statement, its block of statements always run at the very end, whether an error condition occurs or not.  
This is how the try/finally statement works: if an exception occurs, Python runs the except block, then the finally block.  
If an exception does not occur during execution, Python runs the try block, and then the finally block.  
This is useful when you want to make sure that an action takes place after a code block runs, regardless of whether or not an error condition occurs.  
   


## 11.4 Retrieving tool messages with GetMessages()

ArcPy includes a GetMessages() function that you can use to retrieve messages generated when an ArcGIS tool is executing.  
Messages can include informational messages, such as the start and ends times of a tool execution as well as warnings and errors, which can result in something less than the desired result or complete failure of the tool to execute to completion.  


### 11.4.1 Getting ready

During the execution of a tool, various messages are generated.  
These messages include informational messages, such as the start and end times of a tool execution, parameter values passed to the tool, and progress information.  
In addition to this, warnings and errors can also be generated by the tool.  
These messages can be read by your Python script, and your code can be designed to appropriately handle any warnings or errors that have been generated.  
   
ArcPy stores the messages from the last tool that was executed and you can retrieve these messages using the GetMessages() function, which returns a single string containing all messages from the tool that was last executed.  
You can filter this string in terms of severity to return only certain types of messages such as warnings or errors.  
The first message will always include the name of the tool executed, and the last message is the start and end time.  
In this recipe, you will add a line of code to the except statement, which will print more descriptive information about the current tool run.  
   


### 11.4.2 How to do it

Follow these steps to learn how to add a GetMessages() function to your script that generates a list of messages from the tool that was last executed:  
  
1. If necessary, open the C:\ArcpyBook\Ch11\ErrorHandling.py file in IDLE.  
  
2. Alter your script to include the GetMessages() function:  
```py  
import arcpy try:  
arcpy.env.workspace = "c:/ArcpyBook/data" arcpy.Buffer_analysis("Streams.shp","Streams_Buff.shp")  
except: print(arcpy.GetMessages())  
```  
  
3. You can check your work by examining the C:\ArcpyBook\code\Ch11\ ErrorHandling3.py solution file.  
  
4. Save and run the script. This time, the error message should be much more informative. Also notice that there are other types of messages that are generated including the start and end times of the script's execution:  
```  
Executing: Buffer c:/ArcpyBook/data\Streams.shp c:/ArcpyBook/data\ Streams_Buff.shp # FULL ROUND NONE #  
Start Time: Tue Nov 13 22:23:04 2012  
Failed to execute. Parameters are not valid.  
ERROR 000735: Distance [value or field]: Value is required Failed to execute (Buffer).  
Failed at Tue Nov 13 22:23:04 2012 (Elapsed Time: 0.00 seconds)  
```  

### 11.4.3 How it works

The GetMessages() function returns all the messages generated by the last tool that was run.  
I want to emphasize that it only returns messages from the last tool that was run.  
Keep this in mind if you have a script with multiple tools that are being run.  
Historical tool messages are not accessible through this function.  
However, there is a Result object that you can use   if you need to retrieve historical tool messages.  
   


## 11.5 Filtering tool messages by the level of severity

As I mentioned in the last recipe, all tools generate a number of messages that can be classified as information, warnings, or error messages.  
The GetMessages() method accepts a parameter that allows you to filter the messages that are returned.  
For example, you may not be interested in the informative or warning messages in your script.  
However, you will certainly be interested in error messages as they indicate a fatal error that will not allow a tool to successfully execute.  
Using GetMessages(), you can filter the returned message to include only error messages.  


### 11.5.1 Getting ready

Messages are classified into one of three types, which are indicated by the level of severity.  
Informational messages provide descriptive information concerning things, such as a tools progress, start and end times of the tool, output data characteristics, and much more.  
The severity of an informational message is indicated by a value of 0.  
Warning messages  are generated when a problem has occurred during execution that may affect the output.  
Warnings are indicated with a severity level of 1 and don't normally stop a tool from running.  
The last type of message is an error message, which is indicated by a numeric value of 2.  
These indicate fatal events that prevent a tool from running.  
Multiple messages may be generated during the execution of a tool, and these are stored in a list.  
More information about the severity of message is provided in the following image.  
In this recipe, you will learn how to filter the messages generated by the GetMessages() function:    


### 11.5.2 How to do it

Filtering the messages returned by a tool is really quite simple. You simply provide the severity level you'd like to return as a parameter for the GetMessages() function. 
1. If necessary, open the C:\ArcpyBook\Ch11\ErrorHandling.py file in IDLE. 

2. Alter the GetMessages() function so that you pass in a value of 2 as the only parameter:  
```py
import arcpy 
try:  
    arcpy.env.workspace = "c:/ArcpyBook/data" 
    arcpy.Buffer_analysis("Streams.shp","Streams_Buff.shp")  
except: 
    print(arcpy.GetMessages(2))  
```

3. You can check your work by examining the C:\ArcpyBook\code\Ch11\ ErrorHandling4.py solution file. 

4. Save and run the script to see the output:  
```py
Failed to execute. Parameters are not valid. 
ERROR 000735: Distance [value or field]: Value is required Failed to execute (Buffer). 
```

### 11.5.3 How it works

As I mentioned earlier, the GetMessages() method can accept an integer argument of 0,  1, or 2.  
Passing a value of 0 indicates that all messages should be returned, while passing a value of 1 indicates that you wish to see warnings.  
In our case, we have passed a value of 2, which indicates that we only want to see error messages.  
Therefore, you won't see any of the other information messages, such as the start and end times of the script.  


## 11.6 Testing for and responding to specific error messages

All errors and warnings generate a specific error code.  
It is possible to check for specific error codes in your scripts and perform some type of action based on these errors.  
This can make your scripts even more versatile.  
   


### 11.6.1 Getting ready

All errors and warnings generated by a geoprocessing tool contain both a six-digit code and a description.  
Your script can test for specific error codes and respond accordingly.  
You can get a listing of all the available error messages and codes in the ArcGIS for Desktop help system by navigating to Geoprocessing | Tool errors and warnings.  
This is illustrated in the following screenshot.  
All errors have a unique page that briefly describes the error by the code number:     
    


### 11.6.2 How to do it

Follow these steps to learn how to write code that responds to specific error codes generated by the execution of a geoprocessing tools:    
    
1. Open the ArcGIS for Desktop help system by navigating to Start | All Programs | ArcGIS | ArcGIS for Desktop Help    
    
2. Navigate to Geoprocessing | Tool errors and warnings | Tool errors 1-10000 | Tool errors and warnings 701-800.    
    
3. Select 000735:<value>:Value is required.    
This error indicates that a parameter required by the tool has not been provided.    
You'll recall from running this script earlier that we have not provided the buffer distance and the resulting error message generated, as a result, contains the error code that we are viewing in the help  system.    
In the following code, you will find the full text of the error message.    
Notice the error code:    
```py    
ERROR000735:Distance[valueorfield]:Valueisrequired    
```    
    
4. If necessary, open the C:\ArcpyBook\Ch11\ErrorHandling.py file in IDLE.    
    
5. In your script, alter the except statement so that it appears as follows:    
```py    
import arcpy try:    
    arcpy.env.workspace = "c:/ArcpyBook/data"   
    arcpy.Buffer_analysis("Streams.shp", "Streams_Buff.shp")    
except:    
    print("Error found in Buffer tool \n") errCode = arcpy.GetReturnCode(3)    
    if str(errCode) == "735":    
        print("Distance value not provided \n")    
        print("Running the buffer again with a default valuevalue \n")   
        defaultDistance = "100 Feet"   
        arcpy.Buffer_analysis("Streams.shp", "Streams_Buff", defaultDistance)    
    print("Buffer complete")    
```    
    
6. You can check your work by examining the C:\ArcpyBook\code\Ch11\ ErrorHandling5.py solution file.    
    
7. Save and run the script. You should see various messages printed, as follows:    
```py    
Error found in Buffer tool    
Distance value not provided for buffer    
Running the buffer tool again with a default distance value Buffer complete    
```    


### 11.6.3 How it works

What you've done in this code block is use the arcpy.GetReturnCode() function to return the error code generated by the tool.  
Then, an if statement is used to test whether the error code contains the 735 value, which is the code that indicates that a required parameter has not been provided to the tool.  
You then provided a default value for the buffer distance and called the Buffer tool again, providing the default buffer value this time.  
   

