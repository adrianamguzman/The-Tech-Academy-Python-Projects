import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry("{}x{}".format(500,200))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')

        self.Search = StringVar()
        self.Search1 = StringVar()

        
        self.btnBrowse= Button(self.master,text= 'Browse..', width = 13, height=1)
        self.btnBrowse.grid(row=2, column= 0, padx=(25,0), pady=(40,0))

        self.btnBrowse1= Button(self.master,text= 'Browse..', width = 13, height=1)
        self.btnBrowse1.grid(row=3, column= 0, padx=(25,0), pady=(10,0))

        self.btnCheck= Button(self.master,text= 'Check Files..', width = 13, height=2)
        self.btnCheck.grid(row=4, column= 0, padx=(25,0), pady= (20,0))

        self.btnClose= Button(self.master,text= 'Close..', width = 13, height=2)
        self.btnClose.grid(row=4, column= 3, padx=(25,0), pady= (20,0), sticky = NE)

        self.txtSearch = Entry(self.master, text = self.Search, font = ("Helvetica", 16), fg ='black', bg ='white')
        self.txtSearch.grid(row=2, column=1, columnspan = 3, padx=(25,0), pady=(40,0)) 

        self.txtSearch1 = Entry(self.master, text = self.Search1, font = ("Helvetica", 16), fg ='black', bg ='white')
        self.txtSearch1.grid(row=3, column= 1, columnspan = 3, padx=(25,0), pady=(10,0))


        

        


        

        























if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()       
