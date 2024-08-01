import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name=simpledialog.askstring(title='Remarkable', prompt="Type one of these names: Steve, George, or Jack")
    if name=="Jack":
        messagebox.showinfo(title='Remarkable', message="Jack was a remarkable doctor")
    if name=="Steve":
        messagebox.showinfo(title='Remarkable', message="Steve was a remarkable artist")
    if name=="George":
        messagebox.showinfo(title='Remarkable', message="George was a remarkable scientist")
    window.mainloop()

