from tkinter import * 
import tkinter as tk   

import os
import webbrowser


class ParentWindow(Frame):
     def __init__(self, master, *args, **kwargs):
         Frame.__init__(self, master, *args, **kwargs)
         self.master = master
         self.master.minsize(500,300)
         self.master.maxsize(700,500)
         self.master.title("Web Page Generator")
         
         self.lbl_welcome = tk.Label(self.master,text='select a font from the below dropdown menu')
         self.lbl_welcome.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
     
         self.createpage = Button(self.master,text="createpage",width=5,height=2,command=build)
         self.createpage.grid(row=3,column=0,padx=(27,0),pady=(10,0),sticky=E+W)

         OPTIONS = ["Arial","Times New Roman", "Verdana", "Courier"] 

         variable = StringVar(self.master)
         variable.set(OPTIONS[0]) # default value

         self.x = OptionMenu(self.master, variable, *OPTIONS)
         self.x.grid(row=6, column=0, padx=(27,0),pady=(10,0),sticky=E+W) 


      

def build():
    f = open("summersale.html", "w")
    f.write('<html> <body font-family:' + variable.get()'> <h1> Stay tuned for our amazing summer sale! </h1> </body> </html>')
    f.close()

    #Change path to reflect file location
    filename = 'file:///'+os.getcwd()+'/' + 'summersale.html'
    webbrowser.open_new_tab(filename)


    
  
if __name__ == "__main__":
     root = tk.Tk()
     App = ParentWindow(root)
     root.mainloop()

