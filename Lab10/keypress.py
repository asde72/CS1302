from tkinter import Tk, Text
def record(event):
    print(f'Key={event.keysym}')
root = Tk()
txt = Text(root, height=3, width=20)

txt.bind('<KeyPress>',record)

txt.pack()
root.mainloop()