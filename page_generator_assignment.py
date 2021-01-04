from tkinter import * 
import tkinter as tk   

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
         
         self.lbl_welcome = tk.Label(self.master,text='select a font from the below dropdown menu')  #creates label
         self.lbl_welcome.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
     
         self.createpage = Button(self.master,text="createpage",width=5,height=2,command=self.build) #create page ( calls build func )
         self.createpage.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=E+W)

         OPTIONS = ["Cursive","Monospace", "Fantasy", "Courier"]  

         self.variable = StringVar(self.master)  # Create a Tkinter variable
         self.variable.set(OPTIONS[0]) # default value
         
         self.x = OptionMenu(self.master, self.variable, *OPTIONS)  #creates menu for font selections
         self.x.grid(row=2, column=0, padx=(27,0),pady=(10,0),sticky=E+W)

         self.bodytextlabel = tk.Label(self.master,text='Enter a message for the webpage to display')  #creates label
         self.bodytextlabel.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

         self.bodytext = tk.Entry(self.master,text='')
         self.bodytext.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=E+W)  # creates entry field for custom text


      

     def build(self):

        var_bodytext = self.bodytext.get()  # get() to pull variable 
        var_x = self.variable.get()
    
        f = open("summersale.html", "w")
        f.write('<html> <body style="font-family:{}"> <h1> Stay tuned for our amazing summer sale! {} </h1> </body> </html>'.format(var_x,var_bodytext)) #calls variables and plugs string 
        f.close()
            

    

     #Change path to reflect file location
        filename = 'file:///'+os.getcwd()+'/' + 'summersale.html'  
        webbrowser.open_new_tab(filename) # opens html file in browser window


    
  
if __name__ == "__main__":
     root = tk.Tk()
     App = ParentWindow(root)
     root.mainloop()

