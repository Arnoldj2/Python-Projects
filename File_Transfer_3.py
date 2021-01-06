from tkinter import * 
import tkinter as tk   
from tkinter import filedialog
import os
import webbrowser




class ParentWindow(Frame): #  Tkinter frame class 
     def __init__(self, master, *args, **kwargs):
         Frame.__init__(self, master, *args, **kwargs)
          # define our master frame configuration
         self.master = master 
         self.master.minsize(500,300)
         self.master.maxsize(700,500)
         self.master.title("Web Page Generator")

 
         
         folder_path = StringVar()
         self.lbl1 = tk.Label(self.master,textvariable=folder_path)
         self.lbl1.grid(row=0, column=1)
         self.button1 = Button(text="Source Folder")
         self.button1.grid(row=0, column=4)
          
         self.lbl2 = tk.Label(self.master,textvariable=folder_path)
         self.lbl2.grid(row=2, column=1)
         self.button2 = Button(text="Destination Folder" )
         self.button2.grid(row=2, column=4)


         self.button3 = Button(self.master, text="Initiate File Check ")
         self.button3.grid(row=4, column=4)

         self.button4= Button(self.master, text = "Browse", command = self.loadtemplate, width = 10)
         self.button4.grid(row=6, column=4)

              
     def browse_button(self):
         # Allow user to select a directory and store it in global var
         # called folder_path
         global folder_path
         filename = filedialog.askdirectory()
         folder_path.set(filename)
         print(filename)
     


  
if __name__ == "__main__":
     root = tk.Tk()
     App = ParentWindow(root)
     root.mainloop()
