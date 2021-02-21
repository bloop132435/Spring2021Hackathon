from tkinter import *
import webbrowser

from parse import parse
import os



def updateTimeLine():
    while len(test[0]) < 60:
        test.append(0)
    for i in range(0,48):
        active[i] = test[0][i+1]>0
        if active[i]==True:
            timeLine[i].configure(foreground="green")
def indexToStr(num:int):
    realNum = num//2
    string = str(realNum)
    string+=":"
    string+=("30" if num%2==1 else "00")
    return string
def openform():
    webbrowser.open(
        url="https://docs.google.com/forms/d/e/1FAIpQLSd7PL7Kn-bcslvE4KVNeVY5gA47EowiQQfpkZnlZVyqXCg_VA/viewform?usp=sf_link")
timeLine = []
active = []


root = Tk()
root.title("Meeting Bot")
def update():
    global test, widget
    period = 1
    os.system('python3 userInput.py')
    test = parse()
    widget.after(1000,update)
root.geometry('10000x1000+100+100')  # size/position of root
fillOut = Button(root, text="fill out form", command=openform,
                 font=("Fira Code", "8"), padx=0)
fillOut.place(x=00, y=100)
test = parse()
widget = Label(root)
update()
for i in range(0, 48):
    active.append(int(test[0][i+1]) >0)
    tmpLbl = Label(root, text=indexToStr(i), bg="green" if active[i] else "white", padx=0)
    timeLine.append(tmpLbl)
    timeLine[i].grid(row=1, column=i)
root.mainloop()
