import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    points=0
    riddle=simpledialog.askstring(title='Riddler', prompt="What do you own but everybody else uses it more?")
    riddles=simpledialog.askstring(title='Riddler', prompt="I have three eyes yet I can't see. Every time I blink I give you commands which you follow with your hands and feet. What am I?")
    riddler=simpledialog.askstring(title='Riddler', prompt="Say my name and I disappear. What am I?")
    if riddle=="your name":
        points+=1
    if riddles=="traffic light":
        points+=1
    if riddler=="silence":
        points+=1
    """
    * Write a python program that asks the user a minimum of 3 riddles.
    
    * You can look at riddles.com if you don't already know any riddles.

    * Collect the response of each riddle from the user and compare their
    answers to the correct answer. 

    * Use a variable to keep track of the correctly answered riddles

    * After all the riddles have been asked, tell the user how many they got
    correct
    """
    messagebox.showinfo(title='Correct answers', message=points)
    window.mainloop()
