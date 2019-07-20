import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory

import os
import shutil
import sqlite3

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
            path = askdirectory()
            settext(self,path)

        def settext(self,path):
            self.Source.set(path)
            
            
        # destination path
     
        def selectfile2(self):
            path2 = askdirectory()

            settext2(self,path2)

            
        def settext2(self,path2):
            self.Destination.set(path2)

        ## select .txt files within source directory

        ## move the files from source directory to destination directory
            
        def relocate(self):
            Source = self.Source.get()
            Destination = self.Destination.get()
            
            for f in os.listdir(Source):
                if f.endswith('.txt'):
                    conn = sqlite3.connect('FileList.db')

                    with conn:
                        cur = conn.cursor()
                        cur.execute("""INSERT INTO tbl_files (file_list,time_mod) VALUES \
                        (?,?)""",(abPath,time))
                        conn.commit()
                        conn.close()
                    abPath = (os.path.join(Source, f))
                    time = (os.path.getmtime(abPath))
                    print(abPath,time)
                    shutil.move(abPath, Destination)
        
            

                            

        
        self.btnBrowse= Button(self.master,text= 'Browse..', width = 13, height=2, command = lambda: selectfile(self))
        self.btnBrowse.grid(row=2, column= 0, padx=(25,0), pady=(40,0))
        self.txtSource = Entry(self.master, text = self.Source, font = ("Helvetica", 10), fg ='black', bg ='white')
        self.txtSource.grid(row=2, column= 3, columnspan = 2, padx=(25,0), pady=(40,0))

        
        self.btnBrowse2= Button(self.master,text= 'Browse..', width = 13, height=2, command = lambda: selectfile2(self))
        self.btnBrowse2.grid(row= 4, column= 0, padx=(25,0), pady=(40,0))
        self.txtDestination = Entry(self.master, text = self.Destination, font = ("Helvetica", 10), fg ='black', bg ='white')
        self.txtDestination.grid(row=4, column= 3, columnspan = 2, padx=(25,0), pady=(40,0))

        self.btnMove= Button(self.master,text= 'Move Files.', width = 10, height=2, command = lambda: relocate(self))
        self.btnMove.grid(row= 4, column= 7, padx=(25,0), pady=(40,0))
        

        
        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    conn = sqlite3.connect('TEXTFILE.db')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    file_list TEXT, \
                    time_mod INTEGER  \
                    )")
        conn.commit()
    conn.close() 
        
    root.mainloop()
    
