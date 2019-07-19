import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory

import os
import shutil


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry("{}x{}".format(500,225))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')

        self.Source = StringVar()
        self.Destination= StringVar()

        
        # to browse, select and show
        # source path
        
        def selectfile(self):
            files = askdirectory()
            file_name =""

            file_path = os.path.join(files,file_name)

            settext(self,file_path)
            fileName(file_path)
            
        def settext(self,file_path):
            self.Source.set(file_path)
            
            
        # destination path
     
        def selectfile2(self):
            files2 = askdirectory()
            file_name2 =""

            file_path2 = os.path.join(files2,file_name2)


            settext2(self,file_path2)
        
            
        def settext2(self,file_path2):
            self.Destination.set(file_path2)

        ## select .txt files within source directory

        def fileName(self,file_path):
            path = file_path
            f =''
            for f in os.listdir(path):
                if f.endswith('.txt'):
                    names = (os.path.join(path, f))
                    time = (os.path.getmtime(names))
                    print(names,time)
                    return names, time 

        ## move the files from source directory to destination directory
            
        def relocate(names, time, file_path2, file_path):
            f =''
            for f in names:
                shutil.move(file_path, file_path2)
                            
                    
            

        
        self.btnBrowse= Button(self.master,text= 'Browse..', width = 13, height=2, command = lambda: selectfile(self))
        self.btnBrowse.grid(row=2, column= 0, padx=(25,0), pady=(40,0))
        self.txtSource = Entry(self.master, text = self.Source, font = ("Helvetica", 10), fg ='black', bg ='white')
        self.txtSource.grid(row=2, column= 3, columnspan = 2, padx=(25,0), pady=(40,0))

        
        self.btnBrowse2= Button(self.master,text= 'Browse..', width = 13, height=2, command = lambda: selectfile2(self))
        self.btnBrowse2.grid(row= 4, column= 0, padx=(25,0), pady=(40,0))
        self.txtDestination = Entry(self.master, text = self.Destination, font = ("Helvetica", 10), fg ='black', bg ='white')
        self.txtDestination.grid(row=4, column= 3, columnspan = 2, padx=(25,0), pady=(40,0))

        self.btnMove= Button(self.master,text= 'Move Files.', width = 10, height=2, command = lambda: relocate(file_path,file_path2,time,names))
        self.btnMove.grid(row= 4, column= 7, padx=(25,0), pady=(40,0))
        

        
        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()       

