
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import definitions

import time

from modules.logger import Logger

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        logger = Logger()
        def checkans():
            if(answer.get()=="103.21.58.98"):
                answer.configure(foreground="#4cd137")
                self.verfiyans=True
                logger.add_message("2.1: completed at {}".format(time.strftime("%m/%d/%y %r")))
                answer.config(state=tk.DISABLED)
                

            else:
                messagebox.showerror("Error","Incorrect Address! Check the GPS Properly!")   
            
            if(answer1.get()=="127.0.0.1"):
                answer1.configure(foreground="#4cd137")
                self.verfiyans1=True
                answer1.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Error","JARVIS: Never Forget The Local Address!!")
            
            if(answer.get()=="103.21.58.98" and answer1.get()=="127.0.0.1"):
                logger.add_message("2: completed at {}".format(time.strftime("%m/%d/%y %r")))

                chkButton.config(state="active")

        def openBrowser():
            webbrowser.open("https://www.google.com/maps/place/RD+and+SH+National+College+and+SWA+Science+College/@19.0641424,72.8329734,17z/data=!3m1!4b1!4m5!3m4!1s0x3be7c916d68399f7:0x7fb4b43fee5ee7d3!8m2!3d19.0641424!4d72.8351621")
        
        tk.Frame.__init__(self, parent)
        
        lbl2 = tk.Label(self,text = "What's The  Address Of RD National College?")
        lbl2.grid(row=1,column=0,padx=15,pady=15)
        lbl2.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")
        answer = tk.Entry(self,width=10)
        answer.grid(row=1,column=1,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")
        
        lbl2 = tk.Label(self,text = "What's The Local Address Of RD National College?")
        lbl2.grid(row=2,column=0,padx=15,pady=15)
        lbl2.configure(foreground="#474787",font="-family {Arial Black} -size 16 -weight bold -slant italic",relief="flat")

        answer1 = tk.Entry(self,width=10)
        answer1.grid(row=2,column=1,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer1.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")

        submitButton = tk.Button(self,text="CHECK",command=checkans)
        submitButton.grid(row=3,column=0)
        submitButton.configure(background="#000000",foreground="#33d9b2",font="-family {Copperplate Gothic Bold} -size 14")

        openB = tk.Button(self,text="Open Maps",command=openBrowser)
        openB.grid(row=3,column=1)
        openB.configure(background="#000000",foreground="#33d9b2",font="-family {Copperplate Gothic Bold} -size 14")

        chkButton = tk.Button(self,text="CONTINUE",command=lambda:controller.show_frame(definitions.PageThree),state=tk.DISABLED)
        chkButton.grid(row=3,column=2)
        chkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")

        lbl2 = tk.Label(self,text = "JARVIS: Sry Boss! I can't help here!!! :(")
        lbl2.grid(row=4,column=0,columnspan=3)
        lbl2.configure(background="#ffffff",foreground="#e55039",font="-family {Arial Black} -size 10 -weight bold -slant italic",relief="flat")
