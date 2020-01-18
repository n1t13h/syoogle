from PIL import ImageTk, Image

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from datetime import datetime
import time

# import winsound
import os

import webbrowser

import definitions

from modules.logger import Logger


file = open(definitions.ROOT_DIR + "/game.txt","a")
LARGE_FONT= ("Verdana", 12)
filename = definitions.ROOT_DIR + "/assets/avengers.wav"
# winsound.PlaySound(filename, winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)


logger = Logger()

class Syoogle(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        def doNothing():
            pass
        self.title("{ SynTech-X '19 - '20 }")

        # Gets the requested values of the height and widht.
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        print("Width",windowWidth,"Height",windowHeight)
 
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/2 - windowHeight/2)
 

        # # Positions the window in the center of the page.
        # self.geometry("+{}+{}".format(positionRight, positionDown))
        self.resizable(False,False)
        container.grid(row=0,column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, definitions.PageOne, definitions.PageTwo, definitions.PageFour, definitions.PageThree, definitions.PageFive, definitions.PageSix):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
    

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.config(background="#dfe4ea")
        def onSubmit():
            if(len(self.collegeCode.get())>0):
                logger.on_start(self.collegeCode.get())
                controller.show_frame(definitions.PageOne)
            else:
                messagebox.showerror("Error","JARVIS : You Kidding?? Enter The Code!!!")

        lbl = tk.Label(self,text="SYOOGLE")
        lbl.grid(row=0,column=0,padx=5,pady=5)
        lbl.configure(background="#8000ff",foreground="#ffffff",font="Arial 40",relief="flat")

        lbl1 = tk.Label(self,text = "ENTER COLLEGE NAME / COLLEGE CODE / TEAM NAME")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(background="#ffffff",foreground="#000000",font="-family {Arial Black} -size 24 -weight bold -slant italic",relief="flat")

        self.collegeCode = tk.Entry(self)
        self.collegeCode.grid(row=2,column=0,padx=5,pady=5)
        self.collegeCode.configure(background="#ced6e0",foreground="#5352ed",font="-family {Arial Black} -size 20 -weight bold -slant italic")

        submitButton = tk.Button(self,command=onSubmit,text="SUBMIT")
        submitButton.configure(background="#000000",foreground="#ffffff",font="-family {Arial Black} -size 20 -weight bold -slant italic")
        submitButton.grid(row=3,column=0,padx=5,pady=5)


if __name__ == "__main__":    

    app = Syoogle()
    app.mainloop() 
