import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    name=simpledialog.askstring(title='Birthdays', prompt="When is your birthday?")
    if name=="8/1/2024":
        messagebox.showinfo(title='Birthdays', message="Happy Birthday!")
    else:
        messagebox.showinfo(title='Birthdays', message="Happy Unbirthday!")
    window.mainloop()
