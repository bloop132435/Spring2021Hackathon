from tkinter import *
import webbrowser
from parse import parse
from uxFuncs import *

timeLine = []
active = []


root = Tk()
root.title("Meeting Bot")
root.geometry('10000x1000+100+100')  # size/position of root
fillOut = Button(root, text="fill out form", command=openform,
                 font=("Fira Code", "8"), padx=0)
fillOut.grid(row=0, column=0)
for i in range(0, 24):
    active.append(False)
    tmpLbl = Label(root, text=indexToStr(i), bg="green" if active[i] else "white", padx=34)
    timeLine.append(tmpLbl)
    timeLine[i].grid(row=1, column=i)
root.mainloop()
