
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