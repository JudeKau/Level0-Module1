import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    # Write a Python program that asks the user for the radius of a circle.
    # Next, ask the user if they would like to calculate the area or circumference of a circle.
    # If they choose area, display the area of the circle using the radius.
    # Otherwise, display the circumference of the circle using the radius.

    #Area = πr^2
    #Circumference = 2πr
    window = Tk()
    window.withdraw()
    radius=simpledialog.askinteger(title='Circle Radius', prompt="What is the radius of a circle?")
    circle=simpledialog.askstring(title='Circle Area/Circumference', prompt="Would you like to calculate the area or circumference of a circle?")
    if circle=="area":
        area=math.pi*radius*radius
        messagebox.showinfo(message=area)
    if circle=="circumference":
        circumference=math.pi*2*radius
        messagebox.showinfo(message=circumference)
    window.mainloop()
