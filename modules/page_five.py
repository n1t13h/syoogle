
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from PIL import ImageTk, Image

import webbrowser

import definitions

import time

from modules.logger import Logger

class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        logger = Logger()
        def checkClue():
            if(answer.get()=="Stan Lee" or answer.get()=="stan lee" or answer.get()=="stanlee"):
                answer.config(state="disabled")
                answer1.config(state="normal")
                messagebox.showinfo("Info","JARVIS: You Know MCU well!! Check The PDF!!")
                webbrowser.open(definitions.ROOT_DIR+"/assets/brail.pdf")
        
        def checkOne():
            print(answer1.get())
            if(answer1.get()=="part of the journey is the end"):
                # print("Hereee")
                logger.add_message("5: Completed at {}".format(time.strftime("%m/%d/%y %r")))
                controller.show_frame(definitions.PageSix)
            else:
                messagebox.showerror("Error","Incorrect!!")
            # print("Here One")    


        tk.Frame.__init__(self, parent)
        tonysteve = Image.open(definitions.ROOT_DIR + "/assets/cap.jpg")
        tonysteve = tonysteve.resize((800,300),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(tonysteve)

        #Displaying it
        imgLabel = tk.Label(self, image=img)
        imgLabel.image = img
        imgLabel.grid(row=0,column=0)

        lbl1 = tk.Label(self,text = "Who is the One above all in MCU?")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")

        answer = tk.Entry(self,width=20)
        answer.grid(row=2,column=0,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")

        cluechkButton = tk.Button(self,text="Check",command=checkClue)
        cluechkButton.grid(row=3,column=0,columnspan=3)
        cluechkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")       

        lbl2 = tk.Label(self,text = "You May get a Clue Ahead Insert That here!!!")
        lbl2.grid(row=4,column=0,padx=15,pady=15)
        lbl2.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")

        answer1 = tk.Entry(self,width=20)
        answer1.grid(row=5,column=0,padx=5,pady=5,ipadx=100)
        answer1.config(state="disabled")
        answer1.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")
        
        chkButton = tk.Button(self,text="Submit",command=checkOne)
        chkButton.grid(row=6,column=0,columnspan=3)
        chkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")       
        
    