from tkinter import Tk, Button,Label,Entry, Text, END, NORMAL,DISABLED,font
import sqlite3
from tkinter.messagebox import showinfo
from datetime import datetime

def addstudents():
    pantheridvar = pantherid.get()
    namevar = name.get()
    emailvar = email.get()
    cursor.execute('INSERT INTO students (pantherid, name, email) VALUES (?, ?, ?)', (pantheridvar, namevar, emailvar))
    connect.commit()
    showinfo(message='Student record added.')
    pantherid.delete(0,END)
    name.delete(0,END)
    email.delete(0,END)
def list_students():
   cursor.execute('SELECT * FROM students')
   records = cursor.fetchall()
   OutputText.config(state=NORMAL)
   OutputText.delete(1.0, END)
   timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   OutputText.insert(END, f'Student List as of {timestamp}\n')
   for record in records:
        OutputText.insert(END,   f"PantherID: {record[0]}\nName: {record[1]}\nEmail: {record[2]}\n\n") 
#connct to sql database
connect = sqlite3.connect('studentrecords.db')
cursor = connect.cursor()
#CREATE DATABASE FILE
cursor.execute('''CREATE TABLE IF NOT EXISTS students (pantherid INTEGER
PRIMARY KEY, name TEXT, email TEXT)''')
connect.commit()

#create and intialize gui
root = Tk()
root.title("GSU STUDENT RECRODS")
root.geometry("1048x700")
#add font 
#create font
custom_font = font.nametofont("TkDefaultFont") # Start with the default font
custom_font.configure(size=18) # Set the desired font size
root.option_add("*Font", custom_font)

label1 = Label(root, text= "Panther ID")
label2 = Label(root, text= "Name")
label3 = Label(root, text= "Email")
pantherid = Entry(root)
name = Entry(root)
email = Entry(root)
addstudentButton = Button(root, text="Add Student")
listStudentButton = Button(root, text="List Students")
OutputText = Text(root)
OutputText.grid
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
pantherid.grid(row=0,column=1)
name.grid(row=1,column=1)
email.grid(row=2,column=1)
addstudentButton.grid(row=3,column=0,columnspan=2)
listStudentButton.grid(row=4,column=0,columnspan=2)
OutputText.grid(row=5,column=0,columnspan=2)

addstudentButton.config(command=addstudents)
listStudentButton.config(command=list_students)
root.mainloop()
