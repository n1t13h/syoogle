class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        lbl = Label(text="syoogle")
        lbl.grid(row=0,column=0,padx=5,pady=5)
        lbl.configure(background="#8000ff",foreground="#ffffff",font="Arial 40",relief="flat")

        lbl1 = Label(text = "ENTER COLLEGE NAME / COLLEGE CODE / TEAM NAME")
        lbl1.grid(row=1,column=0,padx=15,pady=15)
        lbl1.configure(background="#ffffff",foreground="#000000",font="-family {Arial Black} -size 24 -weight bold -slant italic",relief="flat")

        self.collegeCode = ttk.Entry()
        self.collegeCode.grid(row=2,column=0,padx=5,pady=5)
        self.collegeCode.configure(background="#ffffff",foreground="#8000ff",font="-family {Arial Black} -size 20 -weight bold -slant italic")

        submitButton = Button(command=lambda:controller.show_frame(PageOne),text="SUBMIT")
        submitButton.configure(background="#000000",foreground="#ffffff",font="-family {Arial Black} -size 20 -weight bold -slant italic")
        submitButton.grid(row=3,column=0,padx=5,pady=5)