from tkinter import * 
import tkinter as tk   
from tkinter import filedialog
import os
from datetime import *
import os.path, time




class ParentWindow(Frame): #  Tkinter frame class 
     def __init__(self, master, *args, **kwargs):
         Frame.__init__(self, master, *args, **kwargs)
          # define our master frame configuration
         self.master = master 
         self.master.minsize(500,300)
         self.master.maxsize(700,500)
         self.master.title("File Copy")
 
         
        
         self.lbl1 = tk.Entry(self.master)
         self.lbl1.grid(row=0, columnspan=5)
         self.button1 = Button(text="Source Folder",command=self.browse_button_1)
         self.button1.grid(row=0, column=8)
          
         self.lbl2 = tk.Entry(self.master)
         self.lbl2.grid(row=2, columnspan=5)
         self.button2 = Button(text="Destination Folder",command=self.browse_button_2)
         self.button2.grid(row=2, column=8)


         self.button3 = Button(self.master, text="Initiate File Check ",comman=self.transfer)
         self.button3.grid(row=4, column=4)

     def browse_button_1(self):

         
         filename = filedialog.askdirectory()
         self.lbl1.insert(0,filename)

     def browse_button_2(self):
  
         
         filename1 = filedialog.askdirectory()
         self.lbl2.insert(0,filename1)

     def transfer(self):

         source = self.lbl1.get() # get() to pull variable 
         destination = self.lbl2.get()
 
         files = os.listdir(source)
             
         
         for i in files:
             modifyTime = os.path.getmtime(source+i)   # Returns the time of last modification for all files in the source folder.
             modifyDate = datetime.fromtimestamp(modifyTime)#.strftime('%Y-%m-%d') to convert to a formated string 
             todaysDate = datetime.today() # current date
             DateLimit = todaysDate - timedelta(days=1) # If modified within last 24 hours
        
         if modifyDate > DateLimit : # If the file was edited less then 24 hours ...
                 shutil.copy(source+i, destination)  # ... copy file

  
if __name__ == "__main__":
     root = tk.Tk()
     App = ParentWindow(root)
     root.mainloop()
