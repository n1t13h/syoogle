import os

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from PIL import ImageTk, Image

import definitions

import time

from modules.logger import Logger

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        logger = Logger()
        def checkScript():
            print("Here")
            if str(answer.get())=="Tony : You Trust Me, Steve: Yes I Do":
                answer.configure(foreground="#e74c3c")
                lbl2['text']="JARVIS: You are Smart!!"
                # time.sleep(5)
                logger.add_message("3: completed at {}".format(time.strftime("%m/%d/%y %r")))

                controller.show_frame(definitions.PageFour)

            else:
                lbl2['text']="JARVIS: "+answer.get()+" That Was Clearly Incorrect!!"


                

        tk.Frame.__init__(self, parent)
        #Setting it up
        import urllib.request

        # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #For Windows 
        desktop = os.path.join(os.path.join(os.environ['HOME']), 'Desktop') # For Linux
        urllib.request.urlretrieve("https://i.ibb.co/Xjj8Zsn/tonysteve.jpg", os.path.normpath(desktop+"\\tonysteve.jpg"))
        tonysteve = Image.open(definitions.ROOT_DIR + "/assets/tonysteve.jpg")
        tonysteve = tonysteve.resize((800,300),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(tonysteve)

        #Displaying it
        imgLabel = tk.Label(self, image=img)
        imgLabel.image = img
        imgLabel.grid(row=0,column=0)
        lbl1 = tk.Label(self,text = "You Need A Password To Continue!!")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(background="#ffffff",foreground="#000000",font="-family {Geeza Pro} -size 24 -weight bold -slant italic",relief="flat")
        
        lbl2 = tk.Label(self,text = "JARVIS: There is No Coming Back!!! Also You may set this has wallpaper if you like it, Check The Desktop for Image")
        lbl2.grid(row=2,column=0)
        lbl2.configure(background="#ffffff",foreground="#e55039",font="-family {Arial Black} -size 10 -weight bold -slant italic",relief="flat")
        
        
        
        answer = tk.Entry(self,width=20)
        answer.grid(row=3,column=0,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")
        
        cluechkButton = tk.Button(self,text="Submit",command=checkScript)
        cluechkButton.grid(row=4,column=0)
        cluechkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")