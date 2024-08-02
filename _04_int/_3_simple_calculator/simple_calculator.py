import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    number=simpledialog.askinteger(title='Calculator', prompt="Write a number here")
    numbers=simpledialog.askinteger(title='Calculator', prompt="Write another number here")
    calculate=simpledialog.askstring(title='Calculate', prompt="Would ")
    """
    * Write a Python program that asks the user for two numbers.

    * Then ask the user if the would like to add, subtract, multiply, or divide.

    * Use if-else statements to provide the desired math operation on the numbers
    and display the result.
    """
