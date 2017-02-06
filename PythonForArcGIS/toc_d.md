# 1 Introduction
## 1.1 Python and GIS
## 1.2 Sample Data and Scripts
## 1.3 GIS Data Formats
### 1.3.1 GRID
### 1.3.2 Shapefile
### 1.3.3 dBASE Files
### 1.3.4 Layer Files
### 1.3.5 Geodatabase
## 1.4 An Introductory Example
## 1.5 Organization of This Book
## 1.6 Key Terms
 
# 2 Beginning Python
## 2.1 Where to Write Code
## 2.2 How to Run Code in PythonWin and PyScripter
## 2.3 How to Pass Input to a Script
## 2.4 Python Components
### 2.4.1 Comments
### 2.4.2 Keywords
### 2.4.3 Indentation
### 2.4.4 Built-in Functions
### 2.4.5 Variables, Assignment Statements, and Dynamic
### 2.4.6 Variables Names and Tracebacks
### 2.4.7 Built-in Constants and Exceptions
### 2.4.8 Standard (Built-in) Modules
## 2.5 Key Terms
## 2.6 Exercises
 
# 3 Basic Data Types: Numbers and Strings
## 3.1 Numbers
## 3.2 What Is a String?
## 3.3 String Operations
### 3.3.1 Find the Length of Strings
### 3.3.2 Indexing into Strings
### 3.3.3 Slice Strings
### 3.3.4 Concatenate Strings
### 3.3.5 Check for Substring Membership
## 3.4 More Things with Strings (a.k.a. String Methods)
## 3.5 File Paths and Raw Strings
## 3.6 Unicode Strings
## 3.7 Printing Strings and Numbers
## 3.8 Key Terms
## 3.9 Exercises
 
# 4 Basic Data Types: Lists and Tuples
## 4.1 Lists
### 4.1.1 Sequence Operations on Lists
### 4.1.2 List Methods
### 4.1.3 The Built-in range Function
### 4.1.4 Copying a List
## 4.2 Tuples
## 4.3 Syntax Check and Tracebacks
## 4.4 Key Terms
## 4.5 Exercises
 
# 5 ArcGIS and Python
## 5.1 ArcToolbox
## 5.2 ArcGIS Python Resources
## 5.3 Exporting Models
## 5.4 Working with GIS
## 5.5 ArcGIS + Python = arcpy
## 5.6 arcpy Functions
## 5.7 Environment Settings
## 5.8 Key Terms
## 5.9 Exercises

# 6 Calling Tools with Arcpy
## 6.1 Calling Tools
## 6.2 Help Resources
### 6.2.1 Tool Help
### 6.2.2 Code Snippets
## 6.3 Tool Parameters
### 6.3.1 Linear Units
### 6.3.2 Python Expressions as Input
### 6.3.3 Multivalue Inputs
### 6.3.4 Optional Parameters
## 6.4 Return Values and Result Objects
## 6.5 Spatial Analyst Toolbox
### 6.5.1 Calling Spatial Analyst tools
### 6.5.2 Importing spatial analyst
### 6.5.3 Raster Calculator
## 6.6 Temporary Feature Layers
## 6.7 Using Variables for Multiple Tool Calls
## 6.8 Calling Custom Tools
## 6.9 A Word About Old Scripts
## 6.10 Discussion
## 6.11 Key Terms
## 6.12 Exercises

# 7 Getting User Input
## 7.1 Hard-coding versus Soft-coding
## 7.2 Using GetParameterAsText
## 7.3 Using sys.argv
## 7.4 Missing Arguments
## 7.5 Argument Spacing
## 7.6 Handling File Names and Paths with os Module Functions
### 7.6.1 Getting the Script Path
## 7.7 Key Terms
## 7.8 Exercises

# 8 Controlling Flow
## 8.1 Outlining Workflow
## 8.2 Key Terms
## 8.3 Exercises
 
# 9 Decision-Making and Describing Data
## 9.1 Conditional Expressions
### 9.1.1 Comparison Operators
### 9.1.2 Equality vs. Assignment
### 9.1.3 Logical Operators
### 9.1.4 Membership Operators
## 9.2 ArcGIS Tools That Make Selections
### 9.2.1 Select by Attributes and Temporary Feature Layers
## 9.3 Getting a Description of the Data
### 9.3.1 Describe Object Properties
### 9.3.2 Lists of
### 9.3.3 Using Specialized Properties
### 9.3.4 Compound vs. Nested Conditions
### 9.3.5 Testing Conditions
## 9.4 Required and Optional Script Input
## 9.5 Creating Output Directories
## 9.6 Key Terms
## 9.7 Exercises

# 10 Repetition: Looping for Geoprocessing
## 10.1 Looping Syntax
### 10.1.1 WHILE-Loops
### 10.1.2 FOR-Loops
## 10.2 Nested Code Blocks
## 10.3 Directory Inventory
## 10.4 Indentation and the TabNanny
## 10.5 Key Terms
## 10.6 Exercises

# 11 Batch Geoprocessing 
## 11.1 List GIS Data 
## 11.2 Specify Data Name and Type
## 11.3 List Fields 
## 11.4 Administrative Lists 
## 11.5 Batch Geoprocess Lists of Data 
## 11.6 Debug: Step Through Code 
## 11.7 Key Terms 
## 11.8 Exercises 
 
# 12 Additional Looping Functions
## 12.1 List Comprehension
## 12.2 The Built-in enumerate Function
## 12.3 The Built-in zip Function
## 12.4 Walking Through Subdirectories
## 12.5 Key Terms
## 12.6 Exercises
 
# 13 Debugging
## 13.1 Syntax Errors
## 13.2 Exceptions
## 13.3 Logic Errors
## 13.4 PythonWin Debugging Toolbar
### 13.4.1 Using Breakpoints
## 13.5 Running in Debug Mode
## 13.6 PyScripter Debugging Toolbar
## 13.7 Debugging Tips
## 13.8 Key Terms
## 13.9 Exercises
 
# 14 Error Handling
## 14.1 try/except Structures
### 14.1.1 Using Named Exceptions
### 14.1.2 Multiple except Blocks
### 14.1.3 Error Handling Gotcha
## 14.2 Geoprocessing and Error Handling
### 14.2.1 Getting Geoprocessing Messages
### 14.2.2 The arcpy Named Exception
## 14.3 Catching Exceptions in Loops
## 14.4 Discussion
## 14.5 Key Terms
## 14.6 Exercises
 
# 15 User-Defined Functions 
## 15.1 A Word About Function Words 
### 15.1.1 How It Works 
### 15.1.2 The Docstring 
## 15.2 Custom Functions with Arguments 
### 15.2.1 Script Arguments vs. Functions Arguments 
### 15.2.2 Optional Arguments 
## 15.3 Returning Values 
### 15.3.1 A Common Mistake: Where Did the None Come from? 
### 15.3.2 Returning Multiple Values 
## 15.4 When to Write Functions 
### 15.4.1 Where to Defi ne 
## 15.5 Variables Inside and Outside of Functions 
### 15.5.1 Mutable Arguments Can Change 
### 15.5.2 Pass in Outside Variables 
## 15.6 Key Terms 
## 15.7 Exercises 

# 16 User-Defined Modules
## 16.1 Importing User-Defi ned Modules
## 16.2 Using Functions in Another Module
## 16.3 Modifying User-Defi ned Modules (Reload!)
## 16.4 Am I the Main Module? What’s My Name?
## 16.5 Time Handling Example
## 16.6 Summary
## 16.7 Key Terms
## 16.8 Exercises

# 17 Reading and Writing with Cursors
## 17.1 Introduction to Cursors
## 17.2 Reading Rows
## 17.3 The Field Names Parameter
## 17.4 The Shape Field and Geometry Tokens
## 17.5 Looping with Cursors
## 17.6 Locking
### 17.6.1 The del Statement
### 17.6.2 The with Statement
## 17.7 Update Cursors
## 17.8 Insert Cursors
### 17.8.1 Inserting Geometric Objects
## 17.9 Selecting Rows with SQL
## 17.10 Key Terms
## 17.11 Exercises
 
# 18 Dictionaries
## 18.1 Dictionary Terms and Syntax
### 18.1.1 Access by Key, Not by Index
### 18.1.2 Conditional Construct vs. Dictionary
### 18.1.3 How to Modify: Update/Add/Delete Items
## 18.2 Dictionary Operations and Methods
### 18.2.1 Does It Have That Key?
### 18.2.2 Listing Keys, Values, and Items
### 18.2.3 Looping Through Dictionaries
## 18.3 Populating a Dictionary
### 18.3.1 Dictionaries and Cursors
## 18.4 Discussion
## 18.5 Key Terms
## 18.6 Exercises

# 19 Reading and Writing Text Files
## 19.1 Working with file Objects
### 19.1.1 The WITH Statement
### 19.1.2 Writing Text Files
### 19.1.3 Safe File Reading
### 19.1.4 The os Working Directory vs. the arcpy workspace
### 19.1.5 Reading Text Files
## 19.2 Parsing Line Contents
### 19.2.1 Parsing Field Names
## 19.3 Modifying Text
### 19.3.1 Pseudocode for Modifying Text Files
### 19.3.2 Working with Tabular Text
## 19.4 Pickling
## 19.5 Discussion
## 19.6 Key Terms
## 19.7 Exercises
 
# 20 Working with HTML and KML
## 20.1 Working with HTML
### 20.1.1 Specifying Links
### 20.1.2 Embedding Images
### 20.1.3 HTML Lists
### 20.1.4 HTML Tables
### 20.1.5 Writing HTML with Python
### 20.1.6 Parsing HTML with BeautifulSoup
## 20.2 Fetching and Uncompressing Data
### 20.2.1 Fetching HTML
### 20.2.2 Fetching Compressed Data
### 20.2.3 Expanding Compressed Data
## 20.3 Working with
### 20.3.1 The Structure of KML
### 20.3.2 Parsing
### 20.3.3 Converting KML to Shapefi le
## 20.4 Discussion
## 20.5 Key Terms
## 20.6 Exercises

# 21 Classes
## 21.1 Why Use OOP?
## 21.2 Defi ning a Class
## 21.3 Object Initialization and Self
## 21.4 Using Class Objects
## 21.5 Where to Defi ne a Class
## 21.6 Classes Within a Separate User-Defined Module
## 21.7 Discussion
## 21.8 Key Terms
## 21.9 Exercises

# 22 User Interfaces for File and Folder Selection
## 22.1 A Simple Interface with raw_input
## 22.2 File Handling with tkFileDialog
### 22.2.1 Getting File and Directory Names
### 22.2.2 Options
### 22.2.3 Opening Files for Reading and Writing
## 22.3 Discussion
## 22.4 Key Terms
## 22.5 Exercises
 
# 23 ArcGIS Python GUIs
## 23.1 Creating a Script Tool
### 23.1.1 Printing from a Script Tool
### 23.1.2 Making a Script Tool Button
### 23.1.3 Pointing to a Script
## 23.2 Creating a GUI
### 23.2.1 Using Parameter Data Types
### 23.2.2 Using Parameter Properties
## 23.3 Showing
## 23.4 Validating
### 23.4.1 The ToolValidator Class
## 23.5 Python Toolboxes
### 23.5.1 Setting Up Parameters (getParameterInfo)
### 23.5.2 Checking for Licenses (isLicensed)
### 23.5.3 Validation (updateParameters and updateMessages)
### 23.5.4 Running the Code (execute)
### 23.5.5 Comparing Tools
## 23.6 Discussion
## 23.7 Key Terms
## 23.8 Exercises
 
# 24 Mapping Module
## 24.1 Map Documents
### 24.1.1 Map Name or 'CURRENT'  Map
### 24.1.2 MapDocument Properties
### 24.1.3 Saving Map Documents
## 24.2 Working with Data Frames
## 24.3 Working with
### 24.3.1 Moving, Removing, and Adding Layers
### 24.3.2 Working with Symbology
## 24.4 Managing Layout Elements
## 24.5 Discussion
## 24.6 Key Terms
## 24.7 Exercises
## Index
