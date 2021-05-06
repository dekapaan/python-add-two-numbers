from tkinter import *

root = Tk()
root.title("Adding Two Numbers")
lb1 = Label(root, text="Please enter first number")
lb1.grid(column=1, row=1)
entry1 = Entry(root)
entry1.grid(column=2, row=1)
lb2 = Label(root, text="Please enter second number")
lb2.grid(column=1, row=2)
entry2 = Entry(root)
entry2.grid(column=2, row=2)
lb3 = Label(root, text="Your answer")
lb3.grid(column=1, row=3)
result = Entry(root, state="readonly")
result.grid(column=2, row=3)


def add_2_numbers():
    total = sum(int(i.get()) for i in (entry1, entry2))
    result.config(state="normal")
    result.insert(0, total)
    result.config(state="readonly")


def delete():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.config(state="normal")
    result.delete(0, END)
    result.config(state="readonly")


add = Button(root, text="Add", width=15, command=add_2_numbers).grid(column=1, row=4)
clear = Button(root, text="Clear", width=15, command=delete).grid(column=2, row=4)
quit = Button(root, text="Exit", width=15, command="exit").grid(column=3, row=4)
root.mainloop()
