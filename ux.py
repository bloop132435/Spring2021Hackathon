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
fillOut.place(x=00, y=100)
for i in range(0, 48):
    active.append(i%2==0)
    tmpLbl = Label(root, text=indexToStr(i), bg="green" if active[i] else "white", padx=0)
    timeLine.append(tmpLbl)
    timeLine[i].grid(row=1, column=i)
root.mainloop()
