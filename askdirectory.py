import tkinter

from tkinter import *
import os

from tkinter.filedialog import askdirectory

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry("{}x{}".format(500,150))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')

        self.Search = StringVar()

        
        def selectfile(self):
            files = askdirectory()
            file_name =""

            file_path = os.path.join(files,file_name)


            settext(self,file_path)
            
        def settext(self,file_path):
            self.Search.set(file_path)
        
            
       
            
        

        
        self.btnBrowse= Button(self.master,text= 'Browse..', width = 13, height=2, command = lambda: selectfile(self))
        self.btnBrowse.grid(row=2, column= 0, padx=(25,0), pady=(40,0))
        self.txtSearch = Entry(self.master, text = self.Search, font = ("Helvetica", 11), fg ='black', bg ='white')
        self.txtSearch.grid(row=2, column= 3, columnspan = 2, padx=(25,0), pady=(40,0))


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()       
