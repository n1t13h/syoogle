import tkinter as tk
from datetime import datetime
from tkinter import messagebox
LARGE_FONT= ("Verdana", 12)
import time
import winsound
import os
from PIL import ImageTk, Image
from tkinter import filedialog
filename = "avengers.wav"
import webbrowser
winsound.PlaySound(filename, winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
#VARIABLES
que1 = "Who was the first Marvel Character to get a sequel?"
ans1 = "ironman"
clue1 = "U2FsdGVkX1/L+2Wg+CsfVl/xE/uLadYSaRhQg8IZt4s14fBOL0lIavYYN+7NsFly" #3DES
clue1Ans = "I am Ironman - Ironman 2007"
def consoleLog(txt):
    file = open("game.txt","a")
    file.write(txt)
    file.close()
class Syoogle(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        def doNothing():
            pass
        self.title("{ SynTech-X '19 - '20 }")
        self.protocol('WM_DELETE_WINDOW',doNothing)

        # Gets the requested values of the height and widht.
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        print("Width",windowWidth,"Height",windowHeight)
 
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/2 - windowHeight/2)
 
        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))
        self.resizable(False,False)
        container.grid(row=0,column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo,PageFour,PageThree,PageFive,PageSix):

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
                file = open("game.txt","w")
                txt = self.collegeCode.get() + " started syoogle at " + str(datetime.now())
                file.write(txt)
                file.close()
                controller.show_frame(PageOne)
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




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        def checkScript():
            print("Here")
            if str(answer.get())=="142356":
                answer.configure(foreground="#e74c3c")
                lbl2['text']="You Got It Right!! Hold On Now Let Me Verify Again And Change The Screen"
                time.sleep(5)
                lbl2['text']="Okay Done"
                consoleLog("1: "+str(datetime.now()))
                controller.show_frame(PageTwo)

            else:
                lbl2['text']="JARVIS: "+answer.get()+" That Was Clearly Incorrect!!"


                

        tk.Frame.__init__(self, parent)
        #Setting it up
        spaceStone = Image.open("stones.png")
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



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        
        def checkans():
            if(answer.get()=="103.21.58.98"):
                answer.configure(foreground="#4cd137")
                self.verfiyans=True
                answer.config(state=tk.DISABLED)
                consoleLog("2.1: "+str(datetime.now()))

            else:
                messagebox.showerror("Error","Incorrect Address! Check the GPS Properly!")   
            
            if(answer1.get()=="127.0.0.1"):
                answer1.configure(foreground="#4cd137")
                self.verfiyans1=True
                answer1.config(state=tk.DISABLED)
            else:
                messagebox.showerror("Error","JARVIS: Never Forget The Local Address!!")
            
            if(answer.get()=="103.21.58.98" and answer1.get()=="127.0.0.1"):
                consoleLog("2: "+str(datetime.now()))

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

        chkButton = tk.Button(self,text="CONTINUE",command=lambda:controller.show_frame(PageThree),state=tk.DISABLED)
        chkButton.grid(row=3,column=2)
        chkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")

        lbl2 = tk.Label(self,text = "JARVIS: Sry Boss! I can't help here!!! :(")
        lbl2.grid(row=4,column=0,columnspan=3)
        lbl2.configure(background="#ffffff",foreground="#e55039",font="-family {Arial Black} -size 10 -weight bold -slant italic",relief="flat")

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        def checkScript():
            print("Here")
            if str(answer.get())=="Tony : You Trust Me, Steve: Yes I Do":
                answer.configure(foreground="#e74c3c")
                lbl2['text']="JARVIS: You are Smart!!"
                # time.sleep(5)
                consoleLog("3: "+str(datetime.now()))

                controller.show_frame(PageFour)

            else:
                lbl2['text']="JARVIS: "+answer.get()+" That Was Clearly Incorrect!!"


                

        tk.Frame.__init__(self, parent)
        #Setting it up
        import urllib.request
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        urllib.request.urlretrieve("https://i.ibb.co/Xjj8Zsn/tonysteve.jpg", os.path.normpath(desktop+"\\tonysteve.jpg"))
        tonysteve = Image.open("tonysteve.jpg")
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
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def checkAnswer():
            if(self.ans.get().lower()==ans1):
                self.ans.configure(foreground="#27ae60")
                self.ans.config(state="readonly")
                
                clue.config(state="normal")
                clue.insert(0,clue1)
                clue.config(state="readonly")

                lbl2['text']="JARVIS: DECRYPT THE TEXT !! How Many Movies in the Sequel?"
                cluechkButton.config(state=tk.ACTIVE)

            else:
                self.ans.configure(foreground="#ff0000")
                

        def checkClue():
            if(clueAns.get()==clue1Ans):
                clueAns.configure(foreground="#27ae60")
                clueAns.config(state="readonly")
                cluechkButton.config(state=tk.DISABLED)
                controller.show_frame(PageFive)

            else:
                clueAns.configure(foreground="#ff0000")



        lbl1 = tk.Label(self,text = que1)
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

class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        def checkClue():
            if(answer.get()=="Stan Lee" or answer.get()=="stan lee" or answer.get()=="stanlee"):
                answer.config(state="disabled")
                answer1.config(state="normal")
                messagebox.showinfo("Info","JARVIS: You Know MCU well!! Check The PDF!!")
                webbrowser.open("brail.pdf")
        
        def checkOne():
            print(answer1.get())
            if(answer1.get()=="part of the journey is the end"):
                # print("Hereee")

                controller.show_frame(PageSix)
            else:
                messagebox.showerror("Error","Incorrect!!")
            # print("Here One")    


        tk.Frame.__init__(self, parent)
        tonysteve = Image.open("cap.jpg")
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
        
    

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
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
                        imgLabel.grid(row=6,column=0,columnspan=2)

                        

                
                
        tonysteve = Image.open("cap.jpg")
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
        
        tonysteve = Image.open("qrcode.png")
        tonysteve = tonysteve.resize((100,100),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(tonysteve)

        #Displaying it
        imgLabel = tk.Label(self, image=img)
        imgLabel.image = img
        # imgLabel.grid(row=6,column=0,columnspan=2)

app = Syoogle()
app.mainloop()