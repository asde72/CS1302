from tkinter import Tk , Label , PhotoImage

    #intialize gui
root = Tk()
    #set title of gui
root.title("My App")
    #Display text 
label = Label(master=root, text="Hello World GUI" )
    #display image
photo = PhotoImage(file='credit.jpg')
logo = Label(master=root, image=photo, width= 300, height=300)
logo.pack
label.pack()
root.mainloop()