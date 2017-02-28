
# Appendix B: Five Python Recipes Every GIS Programmer Should Know

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Appendix B: Five Python Recipes Every GIS Programmer Should Know](#appendix-b-five-python-recipes-every-gis-programmer-should-know)
  * [B.1 Introduction](#b1-introduction)
  * [B.2 Reading data from a delimited text file](#b2-reading-data-from-a-delimited-text-file)
    * [B.2.1 Getting ready](#b21-getting-ready)
    * [B.2.2 How to do it](#b22-how-to-do-it)
    * [B.2.3 How it works](#b23-how-it-works)
    * [B.2.4 There's more](#b24-theres-more)
  * [B.3 Sending e-mails](#b3-sending-e-mails)
    * [B.3.1 Getting ready](#b31-getting-ready)
    * [B.3.2 How to do it](#b32-how-to-do-it)
    * [B.3.3 How it works](#b33-how-it-works)
  * [B.4 Retrieving files from an FTP server](#b4-retrieving-files-from-an-ftp-server)
    * [B.4.1 Getting ready](#b41-getting-ready)
    * [B.4.2 How to do it](#b42-how-to-do-it)
    * [B.4.3 How it works](#b43-how-it-works)
    * [B.4.4 There's more](#b44-theres-more)
  * [B.5 Creating ZIP files](#b5-creating-zip-files)
    * [B.5.1 Getting ready](#b51-getting-ready)
    * [B.5.2 How to do it](#b52-how-to-do-it)
    * [B.5.3 How it works](#b53-how-it-works)
    * [B.5.4 There's more](#b54-theres-more)
  * [B.6 Reading XML files](#b6-reading-xml-files)
    * [B.6.1 Getting ready](#b61-getting-ready)
    * [B.6.2 How to do it](#b62-how-to-do-it)
    * [B.6.3 How it works](#b63-how-it-works)
    * [B.6.4 There's more](#b64-theres-more)

<!-- tocstop -->


In this chapter, we will cover the following topics:

* Reading data from a delimited text file
* Sending e-mails
* Retrieving files from an FTP server
* Creating ZIP files
* Reading XML files



## B.1 Introduction

In this chapter, you will learn how to write scripts that perform general purpose tasks with Python.
Tasks, such as reading and writing delimited text files, sending e-mails, interacting with FTP servers, creating .zip files, and reading and writing JSON and XML files, are common.
Every GIS programmer should know how to write Python scripts that incorporate these functionalities.



## B.2 Reading data from a delimited text file

File handling with Python is a very important topic for GIS programmers.
Text files have been used as an interchange format to exchange data between systems.
They are simple, cross-platform, and easy to process.
Comma and tab-delimited text files are among the most commonly used formats for text files, so we'll take an extensive look at the Python tools available to process these files.
A common task for GIS programmers is to read comma-delimited text files containing x and y coordinates, along with other attribute information.
This information is then converted into GIS data formats, such as shapefiles or geodatabases.



### B.2.1 Getting ready

To use Python's built-in file processing functionality, you must first open the file.
Once open, data within the file is processed using functions provided by Python, and file, the file is closed.

> Always remember to close the file when you're done.
Python does not necessarily close the files for you, so it is possible that you could run out of resources or overwrite something.
Also, some operating system platforms won't let the same file be simultaneously open for read-only and writing purposes.

In this recipe, you will learn how to open, read, and process a comma-delimited text file.



### B.2.2 How to do it

Follow these steps to create a Python script that reads a comma-delimited text file:

1. In your C:\ArcpyBook\data folder, you will find a file called N_America. A2007275.txt. Open this file in a text editor. It should appear as follows:
```
18.102,-94.353,310.7,1.3,1.1,10/02/2007,0420,T,72
19.300,-89.925,313.6,1.1,1.0,10/02/2007,0420,T,82
19.310,-89.927,309.9,1.1,1.0,10/02/2007,0420,T,68
26.888,-101.421,307.3,2.7,1.6,10/02/2007,0425,T,53
26.879,-101.425,306.4,2.7,1.6,10/02/2007,0425,T,45
36.915,-97.132,342.4,1.0,1.0,10/02/2007,0425,T,100
```
This file contains data related to wildfire incidents that was derived from a satellite sensor from a single day in 2007. Each row contains latitude and longitude information for the fire along with additional information, including the date and time, satellite type, confidence value, and other details. In this recipe, you are going to pull out only the latitude, longitude, and confidence value. The first item contains the latitude, the second contains longitude, and the final value contains the confidence value.

2. Open IDLE and create a file called C:\ArcpyBook\Appendix2\ReadDelimitedTextFile.py.

3. Use the Python open() function to open the file in order to read it:
```py
f = open("c:/ArcpyBook/data/N_America.A2007275.txt','r')
```

4. Add a for loop to iterate all the rows:
```py
for fire in f:
```

5. Use the split() function to split the values into a list, using a comma as the delimiter. The list will be assigned to a variable called lstValues. Make sure that you indent this line of code inside the for loop you just created:
```py
lstValues = fire.split(",")
```

6. Using the index values that reference latitude, longitude, and confidence values, create new variables:
```py
latitude = float(lstValues[0])
longitude = float(lstValues[1])
confid = int(lstValues[8])
```

7. Print the values of each with the print statement:
```py
print("The latitude is: " + str(latitude) + " The longitude is: " + str(longitude) + " The confidence value is: " + str(confid))
```

8. Close the file:
```py
f.close()
```

9. The entire script should appear as follows:
```py
f = open('c:/ArcpyBook/data/N_America.A2007275.txt','r')
for fire in f.readlines():
    lstValues = fire.split(',')
    latitude = float(lstValues[0])
    longitude = float(lstValues[1])
    confid = int(lstValues[8])
    print("The latitude is: " + str(latitude) + " The longitude is: " + str(longitude) + " The confidence value is: " + str(confid))
f.close()
```

10. You can check your work by examining the C:\ArcpyBook\code\Appendix2\ ReadDelimitedTextFile.py solution file.

11. Save and run the script. You should see the following output:
```py
The latitude is: 18.102 The longitude is: -94.353 The confidence value is: 72
The latitude is: 19.3 The longitude is: -89.925 The confidence value is: 82
The latitude is: 19.31 The longitude is: -89.927 The confidence value is: 68
The latitude is: 26.888 The longitude is: -101.421 The confidence value is: 53
The latitude is: 26.879 The longitude is: -101.425 The confidence value is: 45
The latitude is: 36.915 The longitude is: -97.132 The confidence value is: 100
```

### B.2.3 How it works

Python's open() function creates a file object, which serves as a link to a file residing on your computer.
You must call the open() function on a file before reading or writing data in a file.
The first parameter for the open() function is a path to the file you'd like to open.
The second parameter of the open() function corresponds to a mode, which is typically read (r), write (w), or append (a).
A value of r indicates that you'd like to open the file for read-only operations, while a value of w indicates that you'd like to open the file for write operations.
If the file you open in write mode already exists, it will overwrite any existing data in the file, so be careful when using this mode.
Append (a) mode will open a file for write operations, but instead of overwriting any existing data, it will append data to the end of the file.
So, in this recipe, we have opened the N_America.A2007275.txt file in read-only mode.
Inside the for loop, which is used to loop through each of the values in the text fi   one line at a time, the split() function is used to create a list object from a line of text that is delimited  in some way.
Our fi   is comma-delimited, so we can use split(",").
You can also split based on other delimiters, such as tabs, spaces, or any other delimiter.
This new list object created by split() is stored in a variable called lstValues.
This variable contains each of the wildfi values.
This is illustrated in the following screenshot.
You'll notice that latitude is located in the   fi st position, longitude is located in the second position, and so on.
Lists are zero-based:

 Using the index values (which references latitude, longitude, and confidence values), we create new variables called latitude, longitude, and confid.
Finally, we print each of the values.
A more robust geoprocessing script might write this information into a feature class using an InsertCursor object.
We actually did this in a previous recipe in Chapter 8, Using the ArcPy Data Access Module with Feature Classes and Tables.
It would be possible to use the readlines() function to read the entire contents of the file into a Python list, which could then be iterated.
Each row in the text file will be a unique value in the list.
Since this function reads the entire file into a list, you need to use this method with caution, as large files can cause significant performance problems.


### B.2.4 There's more

Similar to instances of reading files, there are a number of methods that you can use to write data to a file.
The write() function is probably the easiest to use.
It takes a single string argument and writes it to a file.
The writelines() function can be used to write the contents of a list structure to a file.
Before writing data to a text file, you will need to open the file in either a write or append mode.



## B.3 Sending e-mails

There will be occasions when you may need to send an e-mail from a Python script.
An example of this might be an alert for the successful completion or errors incurred in a long-running geoprocessing operation.
On these and other occasions, sending an e-mail can be helpful.



### B.3.1 Getting ready

There will be occasions when you may need toSending an e-mail through a Python script will require you to have access to a mail server.
This can be a public e-mail service, such as Yahoo, Gmail, or others.
It can also use outgoing mail servers that is configured with applications, such as Microsoft Outlook.
In either case, you'll need to know the host name and port of the e-mail server.
The Python smtplib module is used to create connections to the mail server and to send e-mails.

The Python email module contains a Message class that represents e-mail messages.
Each message contains both headers and a body.
This class can't be used to send e-mails, it just handles its object representation.
In this recipe, you'll learn how to use the smtp class to send e-mails containing an attachment through your script.
The Message class can parse a stream of characters or a file containing an e-mail by using either the message_from_file() or message_from_string() functions.
Both will create a new Message object.
The body of the mail can be obtained by calling Message.getpayload().

> We are using the Google Mail service for this exercise. If you already have a Gmail account, then simply provide your
username and password as the values for these variables. If you don't have a Gmail account, you'll need to create one or use a different mail service to complete this exercise. Gmail accounts are free. Google may block attempts to send an
e-mail through scripts, so be aware that this may not work as expected if you're using Gmail.
send an e-mail from a Python script.
An example of this might be an alert for the successful completion or errors incurred in a long-running geoprocessing operation.
On these and other occasions, sending an e-mail can be helpful.



### B.3.2 How to do it

Follow these steps to create a script that can send e-mails:

1.  Open IDLE and create a file called C:\ArcpyBook\Appendix2\SendEmail.py.

2.  In order to send e-mails with attachments, you're going to need to import the smtplib module along with the os module, and several classes from the e-mail module.
Add the following import statements to your script:
```py
import smtplib
from email.MIMEMultipart import MIMEMultipart from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText from email import Encoders
import os
```

3.  Create the following variables and assign your Gmail username and password as the values.
Keep in mind that this method of e-mailing from your Python script can invite problems, as it requires that you include your username and password:
```py
gmail_user = "<username>" gmail_pwd = "<password>"
```
> Note that including an e-mail username and password in a script is not secure so you wouldn't want to include these in a production script.
There are ways of encrypting these values but that is beyond the scope of this recipe.

4.  Create a new Python function called mail().
This function will accept four parameters: to, subject, text, and attach.
Each of these parameters should be self-explanatory.
Create a new MIMEMultipart object and assign the from, to, and subject keys.
You can also attach the text of the e-mail to this new msg object using MIMEMultipart.attach():
```py
def mail(to, subject, text, attach):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to msg['Subject'] = subject
    msg.attach(MIMEText(text))
```

5.  Attach the file to the e-mail:
```py
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)
```

6.  Create a new SMTP object that references the Google Mail service, passes in the username and password to connect to the mail services, sends the e-mail, and closes the connection:
```
mailServer = smtplib.SMTP("smtp.gmail.com", 587)
mailServer.ehlo()
mailServer.starttls() mailServer.ehlo()
mailServer.login(gmail_user, gmail_pwd)
mailServer.sendmail(gmail_user, to, msg.as_string())
mailServer.close()
```

7.  Call the mail() function, passing in the recipient of the e-mail, a subject for the e-mail, the text of the e-mail, and the attachment:
```py
mail("<email to send to>", "Hello from python!",
"This is an email sent with python", "c:/ArcpyBook/data/bc_pop1996.csv")
```

8.  The entire script should appear as follows:
```py
import smtplib
from email.MIMEMultipart import MIMEMultipart from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText from email import Encoders
import os
gmail_user = "<username>" gmail_pwd = "<password>"
def mail(to, subject, text, attach):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to msg['Subject'] = subject
    msg.attach(MIMEText(text))
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587) mailServer.ehlo()
    mailServer.starttls() mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd) mailServer.sendmail(gmail_user, to, msg.as_string()) mailServer.close()
mail("<email to send to>", "Hello from python!", "This is an email sent with python", "bc_pop1996.csv")
```
9.  You can check your work by examining the C:\ArcpyBook\code\Appendix2\ SendEmail.py solution file.
10. Save and run the script.
For testing, I used my personal Yahoo account as the recipient.
You'll notice that my inbox has a new message from my Gmail account; also, notice the attachment:

### B.3.3 How it works

The first parameter passed into the mail() function is the e-mail address that will receive the e-mail.
This can be any valid e-mail address, but you'll want to supply a mail account that you can actually check, so that you can make sure your script runs correctly.
The second parameter is just the subject line of the e-mail.
The third parameter is the text.
The final parameter is the name of a file that will be attached to the e-mail.
Here, I've simply defined that the bc_pop1996.csv file should be attached.
You can use any file you have access to, but you may want to just use this file for testing.

We then create a new MIMEMultipart object inside the mail() function, and assign the from, to, and subject keys.
You can also attach the text of the e-mail to this new msg object using MIMEMultipart.attach().
The bc_pop1996.csv file is then attached to the e-mail using a MIMEBase object and attached to the e-mail using msg.attach(part).
At this point, we've examined how a basic text e-mail can be sent.
However, we want to send a more complex e-mail message that contains text and an attachment.
This requires the use of MIME messages, which provide the functionality to handle multipart e-mails.
MIME messages need boundaries between multiple parts of an e-mail along with extra headers to specify the content being sent.
The MIMEBase class is an abstract subclass of Message and enables   this type of an e-mail to be sent.
Since it is an abstract class, you can't create actual instances of this class.
Instead, you use one of the subclasses, such as MIMEText.
The last step of the mail() function is to create a new SMTP object that references the Google Mail service, passes in the username and password in order to connect to the mail services, sends the ail, and then closes the connection.


## B.4 Retrieving files from an FTP server

Retrieving files from an FTP server for processing is a very common operation for GIS programmers and can be automated with a Python script.

### B.4.1 Getting ready

Connecting to an FTP server and downloading a file is accomplished through the ftplib module.
A connection to an FTP server is created through the FTP object, which accepts a host, username, and password to create the connection.
Once a connection has been opened,      you can then search for and download files.
In this recipe, you will connect to the National Interagency Fire Center Incident FTP site and download a PDF file for a wildfire in Colorado.
Before you run the following script, you will need to create a username/password through http://gis.nwcg.gov/data_nifcftp.html.


### B.4.2 How to do it

Follow these steps to create a script that connects to an FTP server and downloads a file:

1. Open IDLE and create a file called C:\ArcpyBook\Appendix2\ftp.py.

2. We'll be connecting to an FTP server at the NIFC.
Visit their website at http://gis.nwcg.gov/data_nifcftp.html for more information.

3. Import the ftplib, os, and socket modules:
```py
import ftplib import os import socket
```

4. Add the following variables that define the URL, directory, and filename:
```py
HOST = 'ftp.nifc.gov'
USER = '<your username here>' PASSW = '<your password here>'
DIRN = '/Incident_Specific_Data/2012 HISTORIC/ROCKY_MTN/Arapaho/GIS/20120629'
FILE = '20120629_0600_Arapaho_PIO_0629_8x11_land.pdf'
```

5. Add the following code block to create a connection.
If there is a connection error, a message will be generated.
If the connection was successful, a success message will be printed:
```py
try:
f = ftplib.FTP(HOST,USER,PASS)
except (socket.error, socket.gaierror), e: print('ERROR: cannot reach "%s"' % HOST) print('*** Connected to host "%s"' % HOST)
```

6. Add the following code block to anonymously log in to the server:
```py
try:
f.login()
except ftplib.error_perm: print('ERROR: cannot login') f.quit()
print('*** Logged in ')
```

7. Add the following code block to change to the directory specified in our DIRN variable:
```py
try:
f.cwd(DIRN)
except ftplib.error_perm:
print('ERROR: cannot CD to "%s"' % DIRN) f.quit()
print('*** Changed to "%s" folder' % DIRN)
```

8. Use the FTP.retrbinary() function to retrieve the PDF file:
```py
try:
f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
except ftplib.error_perm:
print('ERROR: cannot read file "%s"' % FILE) os.unlink(FILE)
else:
print('*** Downloaded "%s" to CWD' % FILE)
```

9. Make sure you disconnect from the server:
```py
f.quit()
```

10. The entire script should appear as follows:
```py
import ftplib import os import socket
HOST = 'ftp.nifc.gov'
USER = '<your username here>' PASSW = '<your password here>'
DIRN = '/Incident_Specific_Data/2012 HISTORIC/ROCKY_MTN/Arapaho/GIS/20120629'
FILE = '20120629_0600_Arapaho_PIO_0629_8x11_land.pdf'
try:
    f = ftplib.FTP(HOST,USER,PASSW)
    except (socket.error, socket.gaierror), e:
    print('ERROR: cannot reach "%s"' % HOST)
    print('*** Connected to host "%s"' % HOST)
try:
    f.login()
except ftplib.error_perm: print('ERROR: cannot login') f.quit()
    print('*** Logged in ')
try:
    f.cwd(DIRN)
except ftplib.error_perm:
    print('ERROR: cannot CD to "%s"' % DIRN) f.quit()
    print('*** Changed to "%s" folder' % DIRN)
try:
    f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
except ftplib.error_perm:
    print('ERROR: cannot read file "%s"' % FILE)
    os.unlink(FILE)
else:
    print('*** Downloaded "%s" to CWD' % FILE) f.quit()
```

11. You can check your work by examining the C:\ArcpyBook\code\Appendix2\ftp.
py solution file.

12. Save and run the script. If everything is successful, you should see the following output:
```py
*** Connected to host "ftp.nifc.gov"
*** Logged in as "anonymous"
*** Changed to "'/Incident_Specific_Data/2012 HISTORIC/ROCKY_MTN/Arapaho/GIS/20120629'" folder
*** Downloaded "'20120629_0600_Arapaho_PIO_0629_8x11_land.pdf " to CWD
```

13. Check your C:\ArcpyBook\Appendix2 directory for the file.
By default, FTP will download files to the current working directory.


### B.4.3 How it works

To connect to an FTP server, you need to know the URL.
You also need to know the directory and filename for the file that will be downloaded.
In this script, we have hardcoded this information, so that you can focus on implementing the FTP-specific functionality.
Using this information, we then created a connection to the NIFC FTP server.
This is done through the ftplib.FTP() function, which accepts a URL to the host.
Keep in mind that you'll need to obtain a username/password to log in and download the data.
Once logged in, the script then changes directories from the root of the FTP server to the    path defined in the DIRN variable.
This was accomplished with the cwd(<path>) function.
The PDF file was retrieved by using the retrbinary() function.
Finally, you will want to close your connection to the FTP server when you're done.
This is done with the quit() method.



### B.4.4 There's more

There are a number of additional FTP-related methods that you can use to perform various actions.
Generally, these can be divided into directory-level operations and file-level operations.
Directory level methods include the dir() method to obtain a list of files in a directory, mkd() to create a new directory, pwd() to get the current working directory, and cwd() to change the current directory.

Keep in mind that the actions you attempt to perform through your script will be governed by the privileges assigned to your account, so you may not be able to successfully execute every method that I mention.
The ftplib module also includes various methods to work with files.
You can upload and download files in a binary or plain text format.
The retrbinary() and storbinary() methods are used to retrieve and store binary files, respectively.
Plain text files can be retrieved and stored using retrlines() and storlines().

There are several others methods on the FTP class that you should be aware of.
Deleting a  file can be done with the delete() method, while renaming a file can be accomplished with rename().
You can also send commands to the FTP server through the sendcmd() method.

## B.5 Creating ZIP files

GIS often requires the use of large files that will be compressed into a .zip format for ease of sharing.
Python includes a module that you can use to decompress and compress files in this format.



### B.5.1 Getting ready

ZIP is a common compression and archive format and is implemented in Python through the zipfile module.
The ZipFile class can be used to create, read, and write .zip files.
To create a new .zip file, simply provide the filename along with a mode as w, which indicates that you want to write data to the file.
In the following code example, we are creating a .zip file called datafile.zip.
The second parameter, w, indicates that a new file will be created.
A new file will be created or an existing file with the same name will be truncated in the write mode.
An optional compression parameter can also be used when creating the file.
This value can be set to either ZIP_STORED or ZIP_DEFLATED:
```py
zipfile.ZipFile('dataFile.zip', 'w',zipfile.ZIP_STORED)
```
In this exercise, you will use Python to create file, add files, and apply compression to a .zip file.
You'll be archiving all the shapefiles located in the C:\ArcpyBook\data directory.



### B.5.2 How to do it

Follow these steps to learn how to create a script that builds a .zip file:

1. Open IDLE and create a script called C:\ArcpyBook\Appendix2\ CreateZipfile.py.

2. Import the zipfile and os modules:
```py
import os import zipfile
```

3. Create a new .zip file called shapefiles.zip in write mode and add a compression parameter:
```py
zfile = zipfile.ZipFile("shapefiles.zip", "w", zipfile.ZIP_STORED)
```

4. Next, we'll use the os.listdir() function to create a list of files in the data directory:
```py
files = os.listdir("c:/ArcpyBook/data")
```

5. Loop through a list of all the files and write to the .zip file if the file ends with shp, dbf, or shx:
```py
for f in files:
if f.endswith("shp") or f.endswith("dbf") or f.endswith("shx"):
zfile.write("C:/ArcpyBook/data/" + f)
```

6. Print out a list of all the files that were added to the ZIP archive.
You can use the ZipFile.namelist() function to create a list of files in the archive.
```py
for f in zfile.namelist(): print "Added %s" % f
```

7. Close the .zip archive:
```py
zfile.close()
```

8. The entire script should appear as follows:
```py
import os import zipfile
#create the zip file
zfile = zipfile.ZipFile("shapefiles.zip", "w", zipfile.ZIP_STORED)
files = os.listdir("c:/ArcpyBook/data")
for f in files:
if f.endswith("shp") or f.endswith("dbf") or f.endswith("shx"):
zfile.write("C:/ArcpyBook/data/" + f)
# list files in the archive for f in zfile.namelist():
print("Added %s" % f)
zfile.close()
```

9. You can check your work by examining the C:\ArcpyBook\code\Appendix2\ CreateZipfile_Step1.py solution file.

10. Save and run the script. You should see the following output:
```py
Added ArcpyBook/data/Burglaries_2009.dbf
Added ArcpyBook/data/Burglaries_2009.shp
Added ArcpyBook/data/Burglaries_2009.shx
Added ArcpyBook/data/Streams.dbf
Added ArcpyBook/data/Streams.shp
Added ArcpyBook/data/Streams.shx
```

11. In Windows Explorer, you should be able to see the output .zip file, as shown in the following screenshot. Note the size of archive. This file was created without compression:

12. Now, we're going to create a compressed version of the .zip file to see the difference. Make the following changes to the line of code that creates the .zip file:
```py
zfile = zipfile.ZipFile("shapefiles2.zip", "w", zipfile.ZIP_DEFLATED)
```

13. You can check your work by examining the C:\ArcpyBook\code\Appendix2\ CreateZipfile_Step2.py solution file.

14. Save and rerun the script.

15. Take a look at the size of the new shapefiles2.zip file that you just created. Note the decreased size of the file due to compression:




### B.5.3 How it works

In this recipe, you created a new .zip file called shapefiles.zip in write mode.
In the first iteration of this script, you didn't compress the contents of the file.
However, in the second iteration, you did it by using the DEFLATED parameter that was passed into the constructor   for the ZipFile object.
The script then obtained a list of files in the data directory and looped through each of the files.
Each file that has an extension of .shp, .dbf, or .shx is then written to the archive file, using the write() function.
Finally, the names of each of the files written to the archive are printed to the screen.



### B.5.4 There's more

The contents of an existing file  stored in a ZIP archive can be read by using the read() method.
The file should first be opened in a read mode, and then you can call the read() method passing a parameter that represents the file name that should be read.
The contents of the fi can then be printed to the screen, written to another file, or stored as a list or dictionary variable.


## B.6 Reading XML files

XML files were designed as a way to transport and store data.
They are platform-independent since the data is stored in a plain text file.
Although similar to HTML, XML differs from HTML since the former is designed for display purposes, whereas XML data is designed for data.
XML files are sometimes used as an interchange format for GIS data that is going between various software systems.



### B.6.1 Getting ready

XML documents have a tree-like structure that is composed of a root element, child elements, and element attributes.
Elements are also called nodes.
All XML files contain a root element.
This root element is the parent to all other elements or child nodes.
The following code example illustrates the structure of an XML document.
Unlike HTML files, XML files are case sensitive:
```xml
<root>
  <child att="value">
  <subchild>.....</subchild>
  </child>
</root>
```

> Python provides several programming modules that you can use to process XML files.
The module that you use should be determined by the module that is right for the job.
Don't try to force a single module to do everything.
Each module has specific functions that they are good at performing.

In this recipe, you will learn how to read data from an XML file using the nodes and element attributes that are a part of the document.

There are a number of ways that you can access nodes within an XML document.
Perhaps, the easiest way to do so is to fi nodes by tag name and then through walk the tree containing a list of the child nodes.
Before doing so, you'll want to parse the XML document with the minidom.parse() method.
Once parsed, you can then use the childNodes attribute to obtain a list of all the child nodes starting at root of the tree.
Finally, you can search the nodes by tag names with the getElementsByTagName(tag) function, which accepts a tag name as an argument.
This will return a list of all child nodes that are associated with the tag.
You can also determine if a node contains an attribute by calling hasAttribute(name), which will return a true/false value.
Once you've determined that an attribute exists, a call to getAttribute(name) will obtain the value for the attribute.

In this exercise, you will parse an XML file and pull out values associated with a particular element (node) and attribute.
We'll load an XML file containing wildfire data.
In this file, we'll look for the <fire> node and the address attribute for each of these nodes.
The addresses will be printed out.


### B.6.2 How to do it

1. Open IDLE and create a script called C:\ArcpyBook\Appendix2\ XMLAccessElementAttribute.py.

2. The WitchFireResidenceDestroyed.xml file will be used. The file is located in your C:\ArcpyBook\Appendix2 folder. You can see a sample of its contents, as follows:
```py
<fires>
  <fire address="11389 Pajaro Way" city="San Diego" state="CA" zip="92127" country="USA" latitude="33.037187" longitude="-117.082299" />
  <fire address="18157 Valladares Dr" city="San Diego" state="CA" zip="92127" country="USA" latitude="33.039406" longitude="-117.076344" />
  <fire address="11691 Agreste Pl" city="San Diego" state="CA" zip="92127" country="USA" latitude="33.036575" longitude="-117.077702" />
  <fire address="18055 Polvera Way" city="San Diego" state="CA" zip="92128" country="USA" latitude="33.044726" longitude="-117.057649" />
</fires>
```

3. Import minidom from xml.dom:
```py
from xml.dom import minidom
```

4. Parse the XML file:
```py
xmldoc = minidom.parse("WitchFireResidenceDestroyed.xml")
```

5. Generate a list of nodes from the XML file:
```py
childNodes = xmldoc.childNodes
```
6. Generate a list of all the <fire> nodes:
```py
eList = childNodes[0].getElementsByTagName("fire")
```

7. Loop through the list of elements, test for the existence of the address attribute and print the value of the attribute, if it exists:
```py
for e in eList:
    if e.hasAttribute("address"):
        print(e.getAttribute("address"))
```
8. You can check your work by examining the C:\ArcpyBook\code\Appendix2\ XMLAccessElementAttribute.py solution file.

9. Save and run the script. You should see the following output:
```py
11389 Pajaro Way
18157 Valladares Dr
11691 Agreste Pl
18055 Polvera Way
18829 Bernardo Trails Dr 18189 Chretien Ct
17837 Corazon Pl
18187 Valladares Dr
18658 Locksley St
18560 Lancashire Way
```

### B.6.3 How it works

Loading an XML document into your script is probably the most basic thing you can do with XML files.
You can use the xml.dom module to do this through the use of the minidom object.
The minidom object has a method called parse(), which accepts a path to an XML document and creates a document object model (DOM) tree object from the WitchFireResidenceDestroyed.xml file.

The childNodes property of the DOM tree generates a list of all the nodes in the XML file.
You can then access each of the nodes using the getElementsByTagName() method.
The final step is to loop through each of the <fire> nodes contained within the eList variable.
For each node, we then check for the address attribute with the hasAttribute() method, and if it exists, we call the getAttribute() function and print the address to the screen.


### B.6.4 There's more

There will be times when you will need to search an XML document for a specific text string.
This requires the use of the xml.parsers.expat module.
You'll need to define a search class derived from the basic expat class and then create an object from this class.

Once created, you can call the parse() method on the search object to search for data.
Finally, you can then search the nodes by tag names with the getElementsByTagName(tag) function, which accepts a tag name as an argument.
This will return a list of all child nodes that are associated with the tag.




```python

```
