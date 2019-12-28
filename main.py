import tkinter as tk
from datetime import datetime
from tkinter import messagebox
LARGE_FONT= ("Verdana", 12)

#VARIABLES
que1 = "Who was the first Marvel hero to get a sequel?"
ans1 = "ironman"
clue1 = "U2FsdGVkX1/kfrltdoLLKU+OSSRBFz8TTMw+yEOpMTI=" #3DES
clue1Ans = "Avengers"

class Syoogle(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("{ SynTech-X '19 - '20 }")
        # Gets the requested values of the height and widht.
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        print("Width",windowWidth,"Height",windowHeight)
 
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/2 - windowHeight/2)
 
        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))

        container.grid(row=0,column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        def onSubmit():
            if(len(self.collegeCode.get())>0):
                file = open("game.txt","w")
                txt = self.collegeCode.get() + " started syoogle at " + str(datetime.now())
                file.write(txt)
                file.close()
                controller.show_frame(PageOne)
            else:
                messagebox.showerror("Error","You Kidding?? Enter The Code!!!")

        lbl = tk.Label(self,text="SYOOGLE")
        lbl.grid(row=0,column=0,padx=5,pady=5)
        lbl.configure(background="#8000ff",foreground="#ffffff",font="Arial 40",relief="flat")

        lbl1 = tk.Label(self,text = "ENTER COLLEGE NAME / COLLEGE CODE / TEAM NAME")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(background="#ffffff",foreground="#000000",font="-family {Arial Black} -size 24 -weight bold -slant italic",relief="flat")

        self.collegeCode = tk.Entry(self)
        self.collegeCode.grid(row=2,column=0,padx=5,pady=5)
        self.collegeCode.configure(background="#ffffff",foreground="#8000ff",font="-family {Arial Black} -size 20 -weight bold -slant italic")

        submitButton = tk.Button(self,command=onSubmit,text="SUBMIT")
        submitButton.configure(background="#000000",foreground="#ffffff",font="-family {Arial Black} -size 20 -weight bold -slant italic")
        submitButton.grid(row=3,column=0,padx=5,pady=5)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def checkAnswer():
            if(self.ans.get()==ans1):
                self.ans.configure(foreground="#27ae60")
                self.ans.config(state="readonly")
                
                clue.config(state="normal")
                clue.insert(0,clue1)
                clue.config(state="readonly")

                lbl2['text']="DECRYPT THE TEXT !! Is That 3DES or ShiftCipher?"
                cluechkButton.config(state=tk.ACTIVE)

            else:
                self.ans.configure(foreground="#ff0000")
                

        def checkClue():
            if(clueAns.get()==clue1Ans):
                pass
            else:
                pass



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

        cluechkButton = tk.Button(self,text="Submit",command=checkAnswer,state=tk.DISABLED)
        cluechkButton.grid(row=4,column=0,columnspan=3)
        cluechkButton.configure(background="#000000",foreground="#33d9b2",font="-family {Arial Black} -size 12 -weight bold -slant italic")

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl = tk.Label(self,text="SYOOGLE")
        lbl.grid(row=0,column=0,padx=5,pady=5)
        lbl.configure(background="#8000ff",foreground="#ffffff",font="Arial 40",relief="flat")

        lbl1 = tk.Label(self,text = "ENTER COLLEGE NAME / COLLEGE CODE / TEAM NAME")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(background="#ffffff",foreground="#000000",font="-family {Arial Black} -size 24 -weight bold -slant italic",relief="flat")

        self.collegeCode = tk.Entry(self)
        self.collegeCode.grid(row=2,column=0,padx=5,pady=5)
        self.collegeCode.configure(background="#ffffff",foreground="#8000ff",font="-family {Arial Black} -size 20 -weight bold -slant italic")

        submitButton = tk.Button(self,command=lambda:controller.show_frame(PageOne),text="SUBMIT")
        submitButton.configure(background="#000000",foreground="#ffffff",font="-family {Arial Black} -size 20 -weight bold -slant italic")
        submitButton.grid(row=3,column=0,padx=5,pady=5)
        


app = Syoogle()
app.mainloop()