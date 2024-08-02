from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window_width = 600
    window_height = 600

    root = tk.Tk()

    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
    canvas.grid()

    # Make a new turtle

    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring(title='Shapes', prompt="Do you want to draw a triangle, circle, or square?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape=="circle":
        canvas.create_oval(100, 100, 0, 200, fill="red", outline="")

    if shape=="square":
        canvas.create_rectangle(100, 100, 0, 200, fill="red", outline="")

    if shape=="triangle":
        canvas.create_polygon(500, 450, 275, 100, 325, 230, fill="red", outline="")
    root.mainloop()


    # Call the turtle .done() method
