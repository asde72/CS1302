from tkinter import Tk, Button, Entry, Label
from tkinter.messagebox import showinfo

def compute():
    global speedEnt
    speed = int(speedEnt.get())
    if speed < 48:
        showinfo(message="Driving too slow")
    elif speed > 70:
        showinfo(message="Driving too fast")
    else: 
        showinfo(message="Speed is within the limtis")
        speedEnt.delete(0,'end')

root = Tk()
#label
label = Label(root, text='Enter Speed')
label.grid(row=0, column=0)
#entry
speedEnt = Entry(root)
speedEnt.grid(row=0,column=1)
#button
button = Button(root,text="Check speed",command=compute)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()

