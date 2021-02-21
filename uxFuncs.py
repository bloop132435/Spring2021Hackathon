
from math import floor


def updateTimeLine():
    for i in range(0,48):
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