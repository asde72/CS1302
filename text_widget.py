from tkinter import Tk, Text, END

root = Tk()

txt = Text(master=root, width=20, height =5)
txt.pack()
root.mainloop()

txt.insert('END', 'First Line\n')
txt.insert('END', 'Second Line\n')
#Get text
print('Contents of the Text widget:\n'),
#txt.get('1.0','END'))
#Delete text - delete the first line
#txt.delete(1.0,2.0)
#Delete text - delete first three characters
#txt.delete(1.0,1.3)
#Delete entire text content
#txt.delete(1.0, 'END')