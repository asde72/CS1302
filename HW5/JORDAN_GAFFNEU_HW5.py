from tkinter import Tk, Button,Label,Entry, Text, END, NORMAL,DISABLED,font
import sqlite3
from tkinter.messagebox import showinfo
from datetime import datetime
import csv
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
   #iterates records to list them all
   for record in records:
        OutputText.insert(END,   f"PantherID: {record[0]}\nName: {record[1]}\nEmail: {record[2]}\n\n")
def search_student():
    pantheridvar = pantherid.get()
    OutputText.delete(1.0, END)
    #searches database for inputs 
    cursor.execute('SELECT * FROM students WHERE pantherid = ?', (pantheridvar,))
    search_results = cursor.fetchall()
    print(search_results)
    if search_results:
        OutputText.insert(END, 'Search results:\n')
        for result in search_results:
            OutputText.insert(END, f"PantherID: {result[0]}\n Name: {result[1]}\n Email: {result[2]}\n\n")
    else:
        showinfo(message=f'No search record was found for {pantheridvar}  ')


    connect.commit()
    pantherid.delete(0,END)
    name.delete(0,END)
    email.delete(0,END)
def update_record():
    pantheridvar = pantherid.get()
    namevar = name.get()
    emailvar = email.get()
    OutputText.delete(1.0, END)
    # makes sure panther id and email and name are inputed
    if not pantheridvar or not namevar or not emailvar:
        showinfo(message='Please enter PantherID, Name, and Email to update a record.')
        return
    try:
        cursor.execute('SELECT * FROM students WHERE pantherid = ?', (pantheridvar,))
        studentPantherdata = cursor.fetchone()
        if studentPantherdata[0] == int(pantheridvar):
            cursor.execute('UPDATE students SET name = ?, email = ? WHERE pantherid = ?', (namevar, emailvar, pantheridvar))
            showinfo(message="Record updated")
        else:
            showinfo(message=f"No search found for {pantheridvar}\n")
    
    except Exception as e:
        showinfo(message=f"No search found\n")
    print(pantheridvar)
    print(studentPantherdata[0])
    connect.commit()
    pantherid.delete(0,END)
    name.delete(0,END)
    email.delete(0,END)
def delee_record():
    pantheridvar = pantherid.get()
    namevar = name.get()
    emailvar = email.get()
    OutputText.delete(1.0, END)
    # makes sure panther id are inputed

    if not pantheridvar:
        showinfo(message='Please enter a PantherID')
        return
    try:
        #searches for panther id
        cursor.execute('SELECT * FROM students WHERE pantherid = ?', (pantheridvar,))
        studentPantherdata = cursor.fetchone()
        #deleted panther id
        if studentPantherdata[0] == int(pantheridvar):
            cursor.execute('DELETE FROM students WHERE pantherid = ?', (pantheridvar,))
            showinfo(message="Record Erased")
        else:
            showinfo(Message="No exsisting record found")
    
    except Exception as e:
        showinfo(message=f"No search found for {pantheridvar}\n")
    print(pantheridvar)
    print(studentPantherdata[0])
    connect.commit()
    pantherid.delete(0,END)
    name.delete(0,END)
    email.delete(0,END)
    





def export_students():
        try:    
#brought from Hw 4
             #      filenameread = 'studentrecords.db'
                cursor.execute('SELECT * FROM students')
                records = cursor.fetchall()
                filenameCSV = 'student.csv'
                                
                with open(filenameCSV, 'w', newline='') as csv_file:
                    if not filenameCSV.lower().endswith(".csv"):
                        filenameCSV += ".csv"
                    print(filenameCSV)
                    writer = csv.writer(csv_file)
                    #CSV file header
                    writer.writerow(['PantherID','Name','Email'])
                    # Write Data
                    for record in records:
                        writer.writerow(record)
                    showinfo(message='Exported to CSV.')
        except Exception as e:
              print(f"An error occurred during the EXPORT operation {str(e)}")
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
#Entries and Labels
label1 = Label(root, text= "Panther ID")
label2 = Label(root, text= "Name")
label3 = Label(root, text= "Email")
pantherid = Entry(root)
name = Entry(root)
email = Entry(root)

#Create Buttons
addstudentButton = Button(root, text="Add Student")
listStudentButton = Button(root, text="List Students")
searchRecordButton = Button(root, text="Search Record")
deleteRecordButton = Button(root, text="Delete Record")
updateRecordButton = Button(root, text=" Update Record")
exportButton = Button(root, text="Export to CSV")
OutputText = Text(root)

#Grid Poistioning
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
pantherid.grid(row=0,column=1)
name.grid(row=1,column=1)
email.grid(row=2,column=1)
addstudentButton.grid(row=3,column=0,columnspan=1)
listStudentButton.grid(row=4,column=0,columnspan=1)
searchRecordButton.grid(row=3,column=1,columnspan=1)
deleteRecordButton.grid(row=4,column=1,columnspan=1)
updateRecordButton.grid(row=3,column=2,columnspan=1)
exportButton.grid(row=4,column=2,columnspan=1)
OutputText.grid(row=5,column=0,columnspan=3)


#Button Commands
addstudentButton.config(command=addstudents)
listStudentButton.config(command=list_students)
searchRecordButton.config(command=search_student)
updateRecordButton.config(command=update_record)
deleteRecordButton.config(command=delee_record)
exportButton.config(command=export_students)
root.mainloop()
