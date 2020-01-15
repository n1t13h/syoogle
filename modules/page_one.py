import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from PIL import ImageTk, Image

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        def checkScript():
            print("Here")
            if str(answer.get())=="142356":
                answer.configure(foreground="#e74c3c")
                lbl2['text']="You Got It Right!! Hold On Now Let Me Verify Again And Change The Screen"
                time.sleep(5)
                lbl2['text']="Okay Done"
                consoleLog(file,"1: "+str(datetime.now()))
                controller.show_frame(PageTwo)

            else:
                lbl2['text']="JARVIS: "+answer.get()+" That Was Clearly Incorrect!!"


                

        tk.Frame.__init__(self, parent)
        #Setting it up
        spaceStone = Image.open(ROOT_DIR + "/assets/stones.png")
        spaceStone = spaceStone.resize((800,200),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(spaceStone)

        #Displaying it
        imgLabel = tk.Label(self, image=img)
        imgLabel.image = img
        imgLabel.grid(row=0,column=0)
        lbl1 = tk.Label(self,text = "What If Marvel Sends You An OTP based On Infinty Stones?")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(background="#ffffff",foreground="#000000",font="-family {Arial Black} -size 24 -weight bold -slant italic",relief="flat")
        
        lbl2 = tk.Label(self,text = "JARVIS: Take Your Time, It Won't Expire in 30 Secs!")
        lbl2.grid(row=2,column=0)
        lbl2.configure(background="#ffffff",foreground="#e55039",font="-family {Arial Black} -size 10 -weight bold -slant italic",relief="flat")
        
        
        
        answer = tk.Entry(self,width=20)
        answer.grid(row=3,column=0,padx=5,pady=5,ipadx=100)
        # answer.config(state="disabled")
        answer.configure(background="#ffffff",foreground="#0c2461",font="-family {Arial Black} -size 12 -weight bold -slant italic")
        
        cluechkButton = tk.Button(self,text="Submit",command=checkScript)
        cluechkButton.grid(row=4,column=0)
        cluechkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")


