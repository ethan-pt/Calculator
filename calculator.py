from tkinter import *

# initialize tkinter
root = Tk()


# window settings
root.title("Calculator")


# define entry
entry = Entry(root, width=19, font='Arial 20', bd=0)

# display entry
entry.grid(row=0, column=0, columnspan=4)


# define buttons
button_1 = Button(root, text="1", padx=30, pady=20, bd=1, command=lambda: num(1))
button_2 = Button(root, text="2", padx=30, pady=20, bd=1, command=lambda: num(2))
button_3 = Button(root, text="3", padx=30, pady=20, bd=1, command=lambda: num(3))
button_4 = Button(root, text="4", padx=30, pady=20, bd=1, command=lambda: num(4))
button_5 = Button(root, text="5", padx=30, pady=20, bd=1, command=lambda: num(5))
button_6 = Button(root, text="6", padx=30, pady=20, bd=1, command=lambda: num(6))
button_7 = Button(root, text="7", padx=30, pady=20, bd=1, command=lambda: num(7))
button_8 = Button(root, text="8", padx=30, pady=20, bd=1, command=lambda: num(8))
button_9 = Button(root, text="9", padx=30, pady=20, bd=1, command=lambda: num(9))
button_0 = Button(root, text="0", padx=66, pady=20, bd=1, command=lambda: num(0))
button_clear = Button(root, text="C", padx=29, pady=20, bd=1, command=clear)
button_divide = Button(root, text="÷", padx=29, pady=20, bd=1, command=divide)
button_multiply = Button(root, text="×", padx=29, pady=20, bd=1, command=multiply)
button_subtract = Button(root, text="-", padx=30, pady=20, bd=1, command=subtract)
button_add = Button(root, text="+", padx=29, pady=52, bd=1, command=add)
button_equals = Button(root, text="=", padx=29, pady=52, bd=1, command=equals)
button_decimal = Button(root, text=".", padx=31, pady=20, bd=1, command=lambda: num('.'))


# window loop
root.mainloop()