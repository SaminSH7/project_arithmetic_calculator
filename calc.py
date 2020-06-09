
from tkinter import Button, Grid, Tk, Entry, END

root = Tk()
root.title("Calc")
e = Entry(root, width=35,  borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10,)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def add():
    first_num = e.get()
    global f_num
    global condition_check
    condition_check = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def sub():
    first_num = e.get()
    global f_num
    global condition_check
    condition_check = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def multiply():
    first_num = e.get()
    global f_num
    global condition_check
    condition_check = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def divide():
    first_num = e.get()
    global f_num
    global condition_check
    condition_check = "division"
    f_num = int(first_num)
    e.delete(0, END)


def equals():
    second_num = e.get()
    e.delete(0, END)
    
    if condition_check == "addition" : 
        e.insert(0, f_num + int(second_num))

    if condition_check == "subtraction" :
        e.insert(0, f_num - int(second_num))    

    if condition_check == "multiplication" :
        e.insert(0, f_num * int(second_num))

    if condition_check == "division" :
        e.insert(0, f_num / int(second_num))

# Define Buttons

button_1 = Button(root, text="1", padx=20, pady=15, command=lambda : button_click(1))
button_2 = Button(root, text="2", padx=17, pady=15, command=lambda : button_click(2))
button_3 = Button(root, text="3", padx=16, pady=15, command=lambda : button_click(3))
button_4 = Button(root, text="4", padx=20, pady=15, command=lambda : button_click(4))
button_5 = Button(root, text="5", padx=17, pady=15, command=lambda : button_click(5))
button_6 = Button(root, text="6", padx=16, pady=15, command=lambda : button_click(6))
button_7 = Button(root, text="7", padx=20, pady=15, command=lambda : button_click(7))
button_8 = Button(root, text="8", padx=17, pady=15, command=lambda : button_click(8))
button_9 = Button(root, text="9", padx=16, pady=15, command=lambda : button_click(9))
button_0 = Button(root, text="0", padx=17, pady=15, command=lambda : button_click(0))

button_add = Button(root, text="+", padx=15, pady=15, command= add)
button_sub = Button(root, text="-", padx=17, pady=15, command=sub)
button_multiply = Button(root, text="X", padx=15, pady=15, command= multiply)
button_divide = Button(root, text="÷", padx=15, pady=15, command=divide)
button_equals = Button(root, text="=", padx=15, pady=15, command=equals)
button_clear = Button(root, text="Cls", padx=15, pady=15, command=clear)


# Put buttons on the screen

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_clear.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_equals.grid(row=5, column=3)
button_divide.grid(row=5, column=2)


root.mainloop()