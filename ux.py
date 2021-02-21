from tkinter import *
import time
import webbrowser
def openform():
	webbrowser.open(url = "https://docs.google.com/forms/d/e/1FAIpQLSd7PL7Kn-bcslvE4KVNeVY5gA47EowiQQfpkZnlZVyqXCg_VA/viewform?usp=sf_link")
root = Tk()
root.geometry('100x100+100+100') # size/position of root
fillOut = Button(root,text = "fill out form",command = openform)
fillOut.pack()
root.mainloop()