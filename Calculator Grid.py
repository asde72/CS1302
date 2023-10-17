from tkinter import Tk, Label, RAISED
root = Tk()
labels = [['1', '2', '3'], # phone dial label texts
        ['4', '5', '6'], # organized in a grid
        ['7', '8', '9'],
        ['*', '0', '#']]
for r in range(4): # for every row r = 0, 1, 2, 3
    for c in range(3): # for every column c = 0, 1, 2
# create label for row r and column c
        label = Label(root, relief=RAISED, # raised border
        padx=10, # make label wide
        text=labels[r][c]) # label text
# place label in row r and column c
        label.grid(row=r, column=c)
root.mainloop()
