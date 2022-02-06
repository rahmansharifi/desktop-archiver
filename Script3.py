# IMPORT MODULES
from datetime import datetime
from time import sleep
import os
import json
import shutil

# EDIT THESE STRINGS
DesktopDirectory = "C:/Users/rahman/Desktop/"
ArchiverDirectory = "C:/DesktopArchiver/"

# DEFINING VARIABLES
ScriptName = __file__.split('/')[-1]
ScriptFolder = os.path.dirname(__file__)
LogFile = ScriptFolder+"/Log.json"
CurrentTime = datetime.now()
CurrentDate = CurrentTime.strftime("%y.%m.%d")

# CHECKING DATABASE
if os.path.isfile(LogFile):
    Data = open(LogFile,'r')
    Data = json.loads(Data.read())
else:
    Data = {'CleanedUpToday':False,'LastTimeArchived':None}

# DEFINING VARIABLES
CleanedUpToday = Data['CleanedUpToday']
LastTimeArchived = Data['LastTimeArchived']

# RE-DIFINING VARIABLES
if LastTimeArchived != CurrentDate:
    CleanedUpToday = False

# ASKKING QUESTION
while True:
    if CleanedUpToday:
        Answer = input("\n\r Desktop Archiver\n\r Desktop has been cleaned up today.\n\r Are you willing to archive again? (y/n): ").lower()
    else:
        Answer = input("\n\r Desktop Archiver\n\r Desktop hasn't been cleaned up today.\n\r Are you willing to archive now? (y/n): ").lower()

    if Answer == 'y' or Answer == 'n':
        break

# PROCESSING
if Answer == 'y':
    print("\n\r Working...")
    if not os.path.exists(ArchiverDirectory+CurrentDate):
        os.mkdir(ArchiverDirectory+CurrentDate)
    Files = os.listdir(DesktopDirectory)
    for FileID in range(0,len(Files)):
        if os.path.isfile(DesktopDirectory+Files[FileID]):
            shutil.move(DesktopDirectory+Files[FileID],ArchiverDirectory+CurrentDate+"/"+Files[FileID])
    Data['CleanedUpToday'] = True
    Data['LastTimeArchived'] = CurrentDate
    Data = json.dumps(Data)
    File = open(LogFile,'w+')
    File.write(Data)
    File.close()
    sleep(1)
elif Answer == 'n':
    print("\n\r Ignoring...")
    Data = json.dumps(Data)
    File = open(LogFile,'w+')
    File.write(Data)
    File.close()
    sleep(1)
