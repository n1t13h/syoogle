
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import definitions

import time

from modules.logger import Logger

class PageFour(tk.Frame):


    def __init__(self, parent, controller):
        logger = Logger()
        self.que1 = "Who was the first Marvel Character to get a sequel?"
        self.ans1 = "ironman"
        self.clue1 = "U2FsdGVkX1/L+2Wg+CsfVl/xE/uLadYSaRhQg8IZt4s14fBOL0lIavYYN+7NsFly" #3DES
        self.clue1Ans = "I am Ironman - Ironman 2007"

        tk.Frame.__init__(self, parent)
        def checkAnswer():
            if(self.ans.get().lower()==self.ans1):
                self.ans.configure(foreground="#27ae60")
                self.ans.config(state="readonly")
                
                clue.config(state="normal")
                clue.insert(0,self.clue1)
                clue.config(state="readonly")

                lbl2['text']="JARVIS: DECRYPT THE TEXT !! How Many Movies in the Sequel?"
                cluechkButton.config(state=tk.ACTIVE)

            else:
                self.ans.configure(foreground="#ff0000")
                

        def checkClue():
            if(clueAns.get()==self.clue1Ans):
                clueAns.configure(foreground="#27ae60")
                clueAns.config(state="readonly")
                cluechkButton.config(state=tk.DISABLED)
                logger.add_message("4: Completed at {}".format(time.strftime("%m/%d/%y %r")))
                controller.show_frame(definitions.PageFive)

            else:
                clueAns.configure(foreground="#ff0000")



        lbl1 = tk.Label(self,text = self.que1)
        lbl1.grid(row=0,column=0,padx=15,pady=15,columnspan=3)
        lbl1.configure(background="#ffffff",foreground="#000000",font="-family {Arial Black} -size 24 -weight bold -slant italic",relief="flat")
        
        self.ans = tk.Entry(self)
        self.ans.grid(row=1,column=0,padx=5,pady=5)
        self.ans.configure(background="#f7f1e3",foreground="#2c2c54",font="-family {Arial Black} -size 20 -weight bold -slant italic")

        chkButton = tk.Button(self,text="✓",command=checkAnswer)
        chkButton.grid(row=1,column=1)
        chkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")



        clue = tk.Entry(self,width=20)
        clue.grid(row=1,column=2,padx=5,pady=5,ipadx=100)
        clue.config(state="disabled")
        clue.configure(background="#ffffff",foreground="#c0392b",font="-family {Arial Black} -size 12 -weight bold -slant italic")
        
        clueAns = tk.Entry(self)
        clueAns.grid(row=3,column=0,padx=5,pady=5,ipadx=100,columnspan=3)
        clue.configure(background="#ffffff",foreground="#c0392b",font="-family {Arial Black} -size 12 -weight bold -slant italic")

        lbl2 = tk.Label(self,text="")
        lbl2.grid(row=2,column=2,padx=5,pady=5)

        cluechkButton = tk.Button(self,text="Submit",command=checkClue,state=tk.DISABLED)
        cluechkButton.grid(row=4,column=0,columnspan=3)
        cluechkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")       
