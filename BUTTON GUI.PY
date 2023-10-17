from tkinter import Tk, Button
from tkinter.messagebox import showinfo #import modulue for displaying gui text
def clicked(): #event handler for the button
    print("Hello GuI world")  #prints in terminal
    showinfo(message='Hello Gui World')#displays text in gui

root = Tk()

#create a button labled "click it" and event handler clicked()
button = Button(root,text='Click it', # text on top of the button
            command=clicked) #button click event handler
button.pack()
root.mainloop() 