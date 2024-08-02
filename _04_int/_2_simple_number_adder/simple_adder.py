import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    number=simpledialog.askinteger(title='number', prompt="Write one number here")
    numbers=simpledialog.askinteger(title='number', prompt="Write another number here")
    sum = numbers+number
    messagebox.showinfo(title='Sum', message=sum)
    """
    * Write a Python program that asks the user for two numbers.

    * Display the sum of the two numbers to the user
    """
    window.mainloop()
