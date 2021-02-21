from tkinter import *
import webbrowser

timeLine = []
active = []
def updateTimeLine():
    for i in range(0,24):
        if active[i]==True:
            timeLine[i].configure(foreground="green")
def indexToStr(num:int):
    string = str(num)+":00"
    return string;
def openform():
    webbrowser.open(
        url="https://docs.google.com/forms/d/e/1FAIpQLSd7PL7Kn-bcslvE4KVNeVY5gA47EowiQQfpkZnlZVyqXCg_VA/viewform?usp=sf_link")


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
