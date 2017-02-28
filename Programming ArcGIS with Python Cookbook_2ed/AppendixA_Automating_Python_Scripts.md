
# Appendix A: Automating Python Scripts

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Appendix A: Automating Python Scripts](#appendix-a-automating-python-scripts)
  * [A.1 Introduction](#a1-introduction)
  * [A.2 Running Python scripts from the command line](#a2-running-python-scripts-from-the-command-line)
    * [A.2.1 Getting ready](#a21-getting-ready)
    * [A.2.2 How to do it](#a22-how-to-do-it)
    * [A.2.3 How it works](#a23-how-it-works)
  * [A.3 Using sys.argv[ ] to capture command-line input](#a3-using-sysargv-to-capture-command-line-input)
    * [A.3.1 Getting ready](#a31-getting-ready)
    * [A.3.2 How to do it](#a32-how-to-do-it)
    * [A.3.3 How it works](#a33-how-it-works)
  * [A.4 Adding Python scripts to batch files](#a4-adding-python-scripts-to-batch-files)
    * [A.4.1 Getting ready](#a41-getting-ready)
    * [A.4.2 How to do it](#a42-how-to-do-it)
    * [A.4.3 How it works](#a43-how-it-works)
    * [A.4.4 There's more](#a44-theres-more)
  * [A.5 Scheduling batch files to run at prescribed times](#a5-scheduling-batch-files-to-run-at-prescribed-times)
    * [A.5.1 Getting ready](#a51-getting-ready)
    * [A.5.2 How to do it](#a52-how-to-do-it)
    * [A.5.3 How it works](#a53-how-it-works)

<!-- tocstop -->


In this chapter, we will cover the following topics:

* Running Python scripts from the command line f Using sys.argv[ ] to capture command-line input f Adding Python scripts to batch files
* Scheduling batch files to run at prescribed times



## A.1 Introduction

Python geoprocessing scripts can be executed either outside ArcGIS as standalone scripts or inside ArcGIS as script tools.
Both methods have their advantages and disadvantages.
Up to this point in the book, all our scripts have been run either inside ArcGIS as a script tool, from a Python development environment such as IDLE, or the Python window in ArcGIS.
However, Python scripts can also be executed from the Windows operating system command line.
The command line is a window that you can use to type in commands, rather than the usual point- and-click approach provided by Windows.
This method of running Python scripts is useful for scheduling the execution of a script.
There are a number of reasons why you might want to schedule your scripts.
Many geoprocessing scripts take a long time to fully execute and need to be scheduled to run during nonworking hours on a regular basis.
Additionally, some scripts need to be executed on a routine basis (every day, week, month, and so on), and should be scheduled for efficiency.
In this chapter, you will learn how to execute scripts from the command line, place scripts inside a batch file, and schedule the execution of scripts at prescribed times.
Keep in mind that any scripts run from the command line will still need access to an ArcGIS for Desktop license in order to use the arcpy module.



## A.2 Running Python scripts from the command line

Up to this point in the book, all your Python scripts have been run as either script tools in ArcGIS or from a Python development environment.
The Windows command prompt provides yet another way of executing your Python scripts.
The command prompt is used primarily to execute scripts that will be run as a part of a batch file and/or as scheduled tasks.


### A.2.1 Getting ready

There are a couple advantages of running Python geoprocessing scripts from the command prompt.
These scripts can be scheduled to batch process your data during off hours for more efficient processing, and they are easier to debug due to the built-in Python error handling and debugging capabilities.
In this recipe, you will learn how to use the Windows command prompt to execute a Python script.
You will need administrative rights to complete this recipe, so you may need to contact your information technology support group to make this change.



### A.2.2 How to do it

Follow these steps to learn how to run a script from the Windows command prompt:

1. In Windows, navigate to Start | All Programs | Accessories | Command Prompt which will display a window similar to the following screenshot:

The window will display the current directory. Your directory will differ to some degree. Let's change to the directory for this appendix.

2. Type cd c:\ArcpyBook\Appendix1.

3. Type dir to see a listing of the files and subdirectories.
You should see only a single Python file called ListFields.py:

4. You will need to make sure that the Python interpreter can be run from anywhere in your directory structure.
Navigate to Start | All Programs | Accessories | System Tools | Control Panel as shown in the following screenshot:

5. Click on System and Security.

6. Click on System.

7. Click on Advanced system settings.

8. In the System Properties dialog box, select the Advanced tab and then the Environment Variables button, as shown in the following screenshot:

9. Find the Path system variable, as can be seen in the following screenshot, and click on Edit…:

10. Examine the entire text string for the C:\Python27\ArcGIS10.3 directory.
If the text string isn't found, add it to the end.
Make sure that you add a semicolon before adding the path as shown in the following screenshot.
Now, when you type python in the command prompt, it will look through each of the directories in the Path system variable, checking for an executable called python.exe.

11. Click on OK to dismiss the Edit System Variable dialog box.

12. Click on OK to dismiss the Environment Variables dialog box.

13. Click on OK to dismiss the System Properties dialog box.

14. Return to the command prompt.

15. Type python ListFields.py.
This will run the ListFields.py script.
After a brief delay, you should see the following output:

The delay is caused by the first line of code that imports the arcpy module.



### A.2.3 How it works

The ListFields.py script provided for you in this recipe is a simple script that lists the attribute fields for Burglary feature class.
The workspace and feature class name are hardcoded in the script.
Typing python followed by the name of the script, which is ListFields.py in this case, triggered the execution of a script using the Python interpreter.
As I mentioned earlier, the workspace and feature class names were hardcoded in this script.
In the next recipe, you will learn how to pass in arguments to the script so that you can remove the hardcoding and make your script more flexible.



## A.3 Using sys.argv[ ] to capture command-line input

Instead of hardcoding your scripts with paths to specific datasets, you can make your scripts more flexible by allowing them to accept input in the form of parameters from the command prompt.
These input parameters can be captured using Python's sys.argv[] object.


### A.3.1 Getting ready

Python's sys.argv[] object allows you to capture input parameters from the command line when a script is executed.
We will use an example to illustrate how this works.
Take a look at the following screenshot:
Each word must be separated by a space.
These words are stored in a zero-based list object called sys.argv[].
In the sys.argv[] object, the first item in the list referenced by the 0 index, stores the name of the script.
In this case, it would be ListFields.py.
Each successive word is referenced by the next integer.
Therefore, the first parameter (c:\ArcpyBook\data) will be stored in sys.argv[1], and the second parameter (Burglaries.shp) will be stored in sys.argv[2].
Each of the arguments in the sys.
argv[] object can be accessed and used inside your geoprocessing script.
In this recipe, you're going to update the ListFields.py script so that it accepts input parameters from the command line.



### A.3.2 How to do it

Follow these steps to create a Python script that can accept input parameters from the command prompt, using sys.argv[]:
1. Open C:\ArcpyBook\Appendix1\ListFields.py in IDLE.

2. Import the sys module: import arcpy import sys

3. Create a variable to hold the workspace that will be passed into the script:
```py
wkspace = sys.argv[1]
```

4. Create a variable to hold the feature class that will be passed into the script:
```
fc = sys.argv[2]
```

5. Update the lines of code that set the workspace and call the ListFields()
function:
```py
arcpy.env.workspace = wkspace fields = arcpy.ListFields(fc)
```
Your completed script should appear as follows:
```py
import arcpy import sys
wkspace = sys.argv[1] fc = sys.argv[2]
try:
    arcpy.env.workspace = wkspace fields = arcpy.ListFields(fc) for fld in fields:
    print(fld.name)
except Exception as e:
    print(e.message)
```

6. You can check your work by examining the C:\ArcpyBook\code\Appendix1\ ListFields_Step2.py solution file.

7. Save the script.

8. If necessary, open the command prompt and navigate to C:\ArcpyBook\ Appendix1.

9. On the command line, type the following and press the Enter key:
python ListFields.py c:\ArcpyBook\data Burglaries_2009.shp

10. Once again, you should see the output detailing the attribute fields for the Burglaries_2009.shp file.
The difference is that your script no longer has a hardcoded workspace and feature class name. You now have a more flexible script, which is capable of listing the attribute fields for any feature class.


### A.3.3 How it works

The sys module contains a list object called argv[], which is used to store the input parameters for the command-line execution of a Python script.
The first item stored in the list is always the name of the script.
So, in this case, sys.argv[0] contains ListFields.py.
Two parameters are passed into the script, including the workspace and a feature class.
These are stored in sys.argv[1] and sys.argv[2], respectively.
These values are then assigned to variables and used in the script.


## A.4 Adding Python scripts to batch files

Scheduling your Python scripts to run at prescribed times will require that you create a batch file containing one or more scripts and or operating system commands.
These batch files can then be added to the Windows scheduler to run at a specific time interval.



### A.4.1 Getting ready

Batch files are text files containing command-line sequences to run Python scripts or perform operating system commands.
They have a file extension of .bat, which Windows recognizes as an executable file.
Since batch files simply contain command-line sequences, they can be written with any text editor, though it is recommended that you use a basic text editor, such as Notepad.
This is done so that you can avoid the inclusion of invisible special characters, which are sometimes inserted by programs, such as Microsoft Word.
In this recipe, you will create a simple batch file that navigates to the directory containing your ListFields.py script and executes it.



### A.4.2 How to do it

Follow these steps to create a batch file:

1. Open a Notepad.
2. Add the following lines of text to the file:
```py
cd c:\ArcpyBook\Appendix1
python ListFields.py c:\ArcpyBook\data Burglaries_2009.shp
```

3. Save the file to your desktop as ListFields.bat. Make sure you change the Save as Type drop-down list to All Files, otherwise you'll wind up with a file called ListFields.bat.txt.

4. In Windows, navigate to your desktop and double-click on ListFields.bat to execute the sequence of commands.

5. A command prompt will be displayed during execution. After the commands have been executed, the command prompt will automatically close.



### A.4.3 How it works

Windows treats a batch file as an executable, so double-clicking on the file will automatically execute the sequence of commands contained within the file in a new command prompt window.
All the print statements will be written to the window.
After the commands have been executed, the command prompt will automatically close.
In the event that you need to keep a track of the output, you can write the statements to an output log file.



### A.4.4 There's more

Batch files can contain variables, loops, comments, and conditional logic.
These functionalities are beyond the scope of this recipe.
However, if you're writing and running a number of scripts for your organization, it's worthwhile spending some time learning more about batch files.
Batch files have been around for a long time, so there is no shortage of information about these files on the Web.
For more information about batch files, please consult the Wikipedia page for this topic.


## A.5 Scheduling batch files to run at prescribed times

Once created, your batch files can then be scheduled to run at prescribed times using the Windows scheduler.



### A.5.1 Getting ready

Many geoprocessing scripts are time-intensive and best run after hours when they can take full advantage of system resources and free up your time to concentrate on other tasks.
In  this recipe, you will learn how to use the Windows scheduler to schedule the execution of your batch file.



### A.5.2 How to do it

Follow these steps to schedule a batch file with the Windows scheduler:

1.  Open the Windows scheduler by navigating to __Start | All Programs | Accessories | System Tools | Control Panel | Administrative Tools__.
Select Task Scheduler.
The scheduler should appear, as shown in the following screenshot:

2.  Select the Action menu item and then Create Basic Task to display the Create Basic Task Wizard dialog box, as shown in the next screenshot.

3.  Give your task a name. In this case, we will call it List Fields from a Feature Class. Click on Next:

4.  Select a trigger for when the task should be executed.
This can, and often will be a time-based trigger, but there can also be other types of triggers, such as a user login or computer start.
In this case, let's just select Daily.
Click on Next:

5.  Select a start date/time as well as a recurrence interval.
In the following screenshot, I have selected the date as 12/3/2012, with the time as 1:00:00 AM, and a recurrence interval of 1 day.
So, every day at 1:00 AM, this task will be executed. Click on Next:

6.  Select Start a program as the action:

7.  Browse to your script and add the parameters. Click on Next:

8.  Click on Finish to add a task to the scheduler:

9.  The tasks should now be displayed in the list of active tasks:


### A.5.3 How it works

The Windows task scheduler keeps track of all the active tasks and handles the execution of these tasks when the prescribed trigger is fired.
In this recipe, we have scheduled our task to execute each day at 1:00 AM.
At this time, the batch file we created will be triggered and the arguments we specified when creating the task will be passed into the script.
Using the scheduler to automatically execute geoprocessing tasks after hours, without the need for GIS staff to interact with the scripts gives you more flexibility and increases your efficiency.
You might also want to consider logging the errors in your Python scripts to a log file for more information about specific problems.
