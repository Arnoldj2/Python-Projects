import shutil
import os
from datetime import *


#set where the source of the files are
source = '/Users/Jeffrey/Desktop/Folder_A/'

#set the destination path to folderB
destination = '/Users/Jeffrey/Desktop/folder_B/'

twentyfour = datetime.now() + timedelta(days=1) # current time + 24 hours 

print(twentyfour)
print(datetime.now())
print(timedelta(days=1))


def GetFileList():  # returns a list with all queried files:

    files = os.listdir(source)

    for i in files:
        print(i)


def transfer():
    
    files = os.listdir(source)

    modifyTime = os.path.getmtime(source)   # Returns the time of last modification of path.
    date = datetime.fromtimestamp(modifyTime)#.strftime('%Y-%m-%d') to convert to a formated string
    currentTime = datetime.now() # Returns the current time
    
        

    for i in files:

        if date < twentyfour: # If the file was edited less then 24 hours ...
            shutil.copy(source+i, destination)  # ... copy file

if __name__ == "__main__":
    transfer()
    
'''

the below is all test info 

modifyTime = os.path.getmtime(source)   # Returns the time of last modification of path.
date = datetime.fromtimestamp(modifyTime)#.strftime('%Y-%m-%d') to convert to a formated string
print(date)

'''
