import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        
        # Define Entry
        self.entry = tk.Entry(root, width=19, font='Arial 20', bd=0)

        #Define Buttons
        self.button_1 = tk.Button(root, text="1", padx=30, pady=20, bd=1, command=lambda: self.num(1))
        self.button_2 = tk.Button(root, text="2", padx=30, pady=20, bd=1, command=lambda: self.num(2))
        self.button_3 = tk.Button(root, text="3", padx=30, pady=20, bd=1, command=lambda: self.num(3))
        self.button_4 = tk.Button(root, text="4", padx=30, pady=20, bd=1, command=lambda: self.num(4))
        self.button_5 = tk.Button(root, text="5", padx=30, pady=20, bd=1, command=lambda: self.num(5))
        self.button_6 = tk.Button(root, text="6", padx=30, pady=20, bd=1, command=lambda: self.num(6))
        self.button_7 = tk.Button(root, text="7", padx=30, pady=20, bd=1, command=lambda: self.num(7))
        self.button_8 = tk.Button(root, text="8", padx=30, pady=20, bd=1, command=lambda: self.num(8))
        self.button_9 = tk.Button(root, text="9", padx=30, pady=20, bd=1, command=lambda: self.num(9))
        self.button_0 = tk.Button(root, text="0", padx=66, pady=20, bd=1, command=lambda: self.num(0))
        self.button_clear = tk.Button(root, text="C", padx=29, pady=20, bd=1, command=self.clear)
        self.button_divide = tk.Button(root, text="÷", padx=29, pady=20, bd=1, command=self.divide)
        self.button_multiply = tk.Button(root, text="×", padx=29, pady=20, bd=1, command=self.multiply)
        self.button_subtract = tk.Button(root, text="-", padx=30, pady=20, bd=1, command=self.subtract)
        self.button_add = tk.Button(root, text="+", padx=29, pady=52, bd=1, command=self.add)
        self.button_equals = tk.Button(root, text="=", padx=29, pady=52, bd=1, command=self.equals)
        self.button_decimal = tk.Button(root, text=".", padx=31, pady=20, bd=1, command=lambda: self.num('.'))

        # Display necessary items
        self.entry.grid(row=0, column=0, columnspan=4)

        self.button_clear.grid(row=1, column=0)
        self.button_divide.grid(row=1, column=1)
        self.button_multiply.grid(row=1, column=2)
        self.button_subtract.grid(row=1, column=3)

        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_add.grid(row=2, column=3, rowspan=2)

        self.button_4.grid(row=3, column=0)
        self.button_5.grid(row=3, column=1)
        self.button_6.grid(row=3, column=2)

        self.button_1.grid(row=4, column=0)
        self.button_2.grid(row=4, column=1)
        self.button_3.grid(row=4, column=2)
        self.button_equals.grid(row=4, column=3, rowspan=2)

        self.button_0.grid(row=5, column=0, columnspan=2)
        self.button_decimal.grid(row=5, column=2)


    # button logic
    def num(self, number):
        current = tk.entry.get()
        tk.entry.delete(0, tk.END)
        tk.entry.insert(0, str(current) + str(number))

    def clear(self):
        tk.entry.delete(0, tk.END)

    def divide(self):
        global first_num
        global method
        first_num = tk.entry.get()
        method = "division"
        tk.entry.delete(0, tk.END)

    def multiply(self):
        global first_num
        global method
        first_num = tk.entry.get()
        method = "multiplication"
        tk.entry.delete(0, tk.END)

    def subtract(self):
        global first_num
        global method
        first_num = tk.entry.get()
        method = "subtraction"
        tk.entry.delete(0, tk.END)

    def add(self):
        global first_num
        global method
        first_num = tk.entry.get()
        method = "addition"
        tk.entry.delete(0, tk.END)

    def equals(self):
        second_num = tk.entry.get()
        tk.entry.delete(0, tk.END)

        if "." in first_num or "." in second_num:
            if method == "division":
                tk.entry.insert(0, float(first_num) / float(second_num))
            elif method == "multiplication":
                tk.entry.insert(0, float(first_num) * float(second_num))
            elif method == "subtraction":
                tk.entry.insert(0, float(first_num) - float(second_num))
            elif method == "addition":
                tk.entry.insert(0, float(first_num) + float(second_num))
            else:
                tk.entry.insert(0, "Something went wrong.")
        elif not "." in first_num and not "." in second_num:
            if method == "division":
                tk.entry.insert(0, int(first_num) / int(second_num))
            elif method == "multiplication":
                tk.entry.insert(0, int(first_num) * int(second_num))
            elif method == "subtraction":
                tk.entry.insert(0, int(first_num) - int(second_num))
            elif method == "addition":
                tk.entry.insert(0, int(first_num) + int(second_num))
            else:
                tk.entry.insert(0, "Something went wrong.")
        else:
            tk.entry.insert(0, "Something went wrong.")


def main():
    root = tk.Tk()
    root.title('Calculator')

    window = App(root)

    root.mainloop()

if __name__ == '__main__':
    main()