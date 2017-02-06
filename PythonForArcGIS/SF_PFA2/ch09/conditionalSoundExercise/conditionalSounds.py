# conditionalSound.py
# Purpose: Practice with conditional statements and the describe object.mro
# Input: A full path file name.
# The code assumes'wav' files reside in the same directory as this Python script.
import winsound, os, sys, time, arcpy

scriptPath =  os.path.abspath(__file__)
mydir = os.path.dirname(scriptPath) + '/'

def playSound(soundfile):
    # Function to play the input sound file using the winsound module.
    winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)
    # Wait 1.5 seconds
    time.sleep( 1.5 )  

# If sys.argv list length is one, no argument was passed.
if len(sys.argv) < 2:       
    playSound( mydir + 'wah_wah_wah.wav' ) 

else:
    fileName = sys.argv[1]

    # Get the describe object
    desc = arcpy.Describe(fileName)      
    dataType = desc.dataType

    if dataType == 'RasterDataset':
        playSound( mydir + 'haha.wav' )
        
        if desc.Format == 'GIF':
            playSound( mydir + 'pukpukpuk.wav' )

        else:
            playSound( mydir + 'doh.wav' )

    elif dataType == 'ShapeFile':
        playSound( mydir + 'oh.wav' )
            
    
playSound( mydir + 'yeehaa.wav' )  


#Predict what sounds you'll hear if run with these input files
#----------------------------------------------------------------
#a. No arguments.

#b. C:/gispy/data/ch09/park.shp

#c. C:/gispy/data/ch09/tree.gif

#d. C:/gispy/data/ch09/jack.jpg

#e. C:/gispy/data/ch09/xy1.txt