import tkinter as tk


LARGE_FONT= ("Verdana", 12)


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
        label = tk.Label(self, text="Syoogle", font=LARGE_FONT)
        label.grid(row=0,column=0)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.grid(row=1,column=0)

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=1,column=1)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.grid(row=0,column=0)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1,column=0)

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=2,column=0)


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