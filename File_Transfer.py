import shutil
import os

#set where the source of the files are
source = '/Users/Jeffrey/Desktop/Folder_A/'

#set the destination path to folderB
destination = '/Users/Jeffrey/Desktop/folder_B/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represent by'i' to their new destination
    shutil.move(source+i, destination)
