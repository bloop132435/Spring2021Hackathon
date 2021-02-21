from tkinter import *
import webbrowser

from parse import parse
import os
meetingCount = 0

timeLine = []
active = []
dataBase = []
def updateTimeLine():
    for i in range(0,48):
        if active[i]==True:
            timeLine[i].configure(background="green")
        else:
            timeLine[i].configure(background="white")
def newMeeting():
    os.system("python3 algoTest.py")
    resultFile = open("algoOut.txt","r")
    result = int(resultFile.readline())
    print(result)
    active[result] = True
    updateTimeLine()
    pass
def updateForm():
    os.system("python3 userInput.py")
    global active
    active.clear()
    for _ in range(60):
        active.append(False)
    updateTimeLine()
    pass
def indexToStr(num:int):
    realNum = num//2
    string = str(realNum)
    string+=":"
    string+=("30" if num%2==1 else "00")
    return string
def openform():
    webbrowser.open(
        url="https://docs.google.com/forms/d/e/1FAIpQLScLhRVBB5UY_RZPvBkcFqddnLJNi-jRmNZRo3QZRYa9TarQuA/viewform?usp=sf_link")


root = Tk()
root.title("Meeting Bot")
root.geometry('10000x1000+100+100')  # size/position of root
fillOut = Button(root, text="fill out form", command=openform, padx=0)
fillOut.place(x=10, y=100)
newMeet = Button(root,text="Add a new meeting",command = newMeeting)
newMeet.place(x=100,y=100)
forms = Button(root,text="Update Forms",command = updateForm)
forms.place(x=260,y=100)
for i in range(0, 48):
    active.append(False)
    tmpLbl = Label(root, text=indexToStr(i), bg="green" if active[i] else "white", padx=0)
    timeLine.append(tmpLbl)
    timeLine[i].grid(row=1, column=i)

updateForm()
root.mainloop()
