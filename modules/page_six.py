
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from PIL import ImageTk, Image

import definitions

import time

from modules.logger import Logger

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        logger = Logger()
        tk.Frame.__init__(self, parent)
        def answerVerify():
            if(answer1.get()=="groot" or answer1.get()=="Groot"):
                answer1.config(state="disabled")
            if(answer2.get()=="SteveRogers" or answer1.get()=="Steve Rogers" or answer2.get()=="steve rogers"):
                answer2.config(state="disabled")
            if(answer3.get()=="inevitable" or answer3.get()=="inevitable"):
                answer3.config(state="disabled")

            if(answer1.get()=="groot" or answer1.get()=="Groot"):
                if(answer2.get()=="SteveRogers" or answer1.get()=="Steve Rogers" or answer2.get()=="steve rogers"):  
                    if(answer3.get()=="inevitable" or answer3.get()=="inevitable"):
                        logger.add_message("6: Completed at {}".format(time.strftime("%m/%d/%y %r")))
                        logger.on_end()
                        imgLabel.grid(row=6,column=0,columnspan=2)

                        

                
                
        tonysteve = Image.open(definitions.ROOT_DIR + "/assets/cap.jpg")
        tonysteve = tonysteve.resize((800,300),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(tonysteve)

        #Displaying it
        imgLabel = tk.Label(self, image=img)
        imgLabel.image = img
        imgLabel.grid(row=0,column=0,columnspan=2)
        lbl1 = tk.Label(self,text = "I am ")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")

        lbl2 = tk.Label(self,text = "I am ")
        lbl2.grid(row=2,column=0,padx=15,pady=15)
        lbl2.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")
        lbl3 = tk.Label(self,text = "I am ")
        lbl3.grid(row=3,column=0,padx=15,pady=15)
        lbl3.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")
        lbl4 = tk.Label(self,text = "I am ")
        lbl4.grid(row=4,column=0,padx=15,pady=15)
        lbl4.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")

        answer = tk.Entry(self,width=10)
        answer.grid(row=1,column=1,padx=5,pady=5,ipadx=100)
        answer.insert(0,"Ironman")
        answer.config(state="disabled")
        answer.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")

        answer1 = tk.Entry(self,width=10)
        answer1.grid(row=2,column=1,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer1.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")
        answer2 = tk.Entry(self,width=10)
        answer2.grid(row=3,column=1,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer2.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")
        answer3 = tk.Entry(self,width=10)
        answer3.grid(row=4,column=1,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer3.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")

        chkButton = tk.Button(self,text="Submit",command=answerVerify)
        chkButton.grid(row=5,column=0,columnspan=3)
        chkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")       
        
        tonysteve = Image.open(definitions.ROOT_DIR + "/assets/qrcode.png")
        tonysteve = tonysteve.resize((100,100),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(tonysteve)

        #Displaying it
        imgLabel = tk.Label(self, image=img)
        imgLabel.image = img
        # imgLabel.grid(row=6,column=0,columnspan=2)
