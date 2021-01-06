import shutil
import os
from datetime import *
import os.path, time


#set where the source of the files are
source = '/Users/Jeffrey/Desktop/Folder_A/'

#set the destination path to folderB
destination = '/Users/Jeffrey/Desktop/folder_B/'



def myList():

    files = os.listdir(source)
    for i in files:
        modTimesinceEpoc = os.path.getctime(source)
        modificationTime = datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
        print("Last Modified Time : ", modificationTime )


def transfer():
    
       
    files = os.listdir(source)    

    for i in files:
        modifyTime = os.path.getmtime(source+i)   # Returns the time of last modification for all files in the source folder.
        modifyDate = datetime.fromtimestamp(modifyTime)#.strftime('%Y-%m-%d') to convert to a formated string 
        todaysDate = datetime.today() # current date
        DateLimit = todaysDate - timedelta(days=1) # If modified within last 24 hours
        
        if modifyDate > DateLimit : # If the file was edited less then 24 hours ...
            shutil.copy(source+i, destination)  # ... copy file

if __name__ == "__main__":
  transfer()
  
    
