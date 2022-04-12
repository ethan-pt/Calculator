from tkinter import *

# initialize tkinter
root = Tk()


# window settings
root.title("Calculator")


# define entry
entry = Entry(root, width=19, font='Arial 20', bd=0)

# display entry
entry.grid(row=0, column=0, columnspan=4)


# window loop
root.mainloop()