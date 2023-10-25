from tkinter import Tk, Entry, Text, Label, END
import sqlite3
def Keypress(event):
    try:
        print(f'Key={event.keysym}')
        Character = event.keysym
        #Tells if input is anumber

        Isnumber = Character.isdigit()
        IsATOZ = Character.isalnum()
        #Tells if input is anumber
        if Isnumber == True:
            TextOutput.insert(END,"It is a number\n")
        elif IsATOZ == False or (IsATOZ == True and len(Character) > 1):
            TextOutput.insert(END,"It is a non alphanumeric key\n")
        elif IsATOZ == True:
            Lowercase = Character.lower()
            Uppercase = Character.upper()
            if Character== Lowercase :
                TextOutput.insert(END,"It is a lowercase letter\n")
            elif Character == Uppercase:
                TextOutput.insert(END,"It is a uppercase letter\n")
    except:
        print("ERROR Invalid Input")

connect = sqlite3.connect('keypress.db')
cursor = connect.cursor()
root = Tk()
root.title("What character is it?")
root.geometry("680x480")
CharacterEntry = Entry(root)
CharacterEntry.grid(row=1,column=2)
TextOutput = Text(root)
TextOutput.grid(row=2, column=2)
EnterLabel = Label(root,text='Press any key')
EnterLabel.grid(row=0,column=2)
CharacterEntry.bind("<Key>",Keypress)









root.mainloop()

