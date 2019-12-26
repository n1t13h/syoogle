# Imports
import tkinter
from ttkthemes import ThemedTk
import sqlite3
from datetime import datetime
import os
import tkinter.font as tkFont
from tkinter.messagebox import showinfo, showerror
from tkinter import simpledialog
import tkinter as tk
from tkscrolledframe import ScrolledFrame
from tkinter import *
import csv
from tkinter import ttk
from tkcalendar import DateEntry
from fpdf import FPDF
import webbrowser
import babel.numbers
import random
import ctypes
import sys


# COLORS
MAIN_UI_COLOR = "#9556eb"
FRAME_BACKGROUND = random.choice(["#ffffff"])
MAIN_RED = "#808e9b"
path = os.path.normpath(os.path.expanduser("~/Documents/Canteen"))
dbPath = "canteen.db"


def initialize_font():
    if "Open Sans" in tkFont.families():
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(family="Arial", size=12)

        default_font = tkFont.nametofont("TkTextFont")
        default_font.configure(family="Arial", size=12)


class Canteen(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="NEWS")

        self.frames = {}

        for F in [
            PageOne,
            Home
        ]:

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def update_frame(self, page_name):
        frame = self.frames[page_name]
        frame.update()
        self.show_frame(page_name)

    # def show_frame(self, page_name):
    #     for frame in self.frames.values():
    #         frame.grid_remove()
    #     frame = self.frames[page_name]
    #     frame.grid()
    def center_window(self):
        # get screen width and height
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen

        # set the dimensions of the screen
        # and where it is placed
        self.geometry("%dx%d" % (ws, hs))



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=FRAME_BACKGROUND)
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
class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=FRAME_BACKGROUND)
        Label(self,text="MANAGE YOUR ITEM INVENTORY!!!").grid(row=0,column=0,sticky="NEWS",columnspan=4,pady=50)
        Button(self,text="INVENTORY MANAGER",background=MAIN_UI_COLOR,command=lambda:controller.show_frame(PageOne)).grid(ipadx=100,columnspan=4,row=1,column=0)
        Label(self,text="Manage Your Purchase And Sales !!!").grid(row=2,column=0,sticky="NEWS",columnspan=4,pady=50)
        Button(self,text="View Sales Data",background=MAIN_UI_COLOR,command=lambda:controller.show_frame(PageOne)).grid(row=3,column=1,padx=80,ipady=20)
        Button(self,text="Insert Sales Data",background=MAIN_UI_COLOR,command=lambda:controller.show_frame(PageOne)).grid(row=3,column=0,padx=80,ipady=20)
        Button(self,text="Conversion",background=MAIN_UI_COLOR,command=lambda:controller.show_frame(PageOne)).grid(row=3,column=2,padx=80,ipady=20)
        Button(self,text="Manage Expenses",background=MAIN_UI_COLOR,command=lambda:controller.show_frame(PageOne)).grid(row=3,column=3,padx=80,ipady=20)
        Label(self,text="Generate Reports!!!").grid(row=4,column=0,sticky="NEWS",columnspan=4,pady=50)
        Button(self,text="Generate / Manage Reports",background=MAIN_UI_COLOR,command=lambda:controller.show_frame(PageOne)).grid(row=5,ipady=20,column=0,columnspan=4)

app = Canteen() 
app.wm_title("Canteen Manager")
initialize_font()
app.mainloop()
    




