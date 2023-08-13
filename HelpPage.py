from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Button
import webbrowser
import ast
import tkinter as tk

# Function to open a website.
def open_website():
    webbrowser.open("https://www.betterhelp.com/")

# Create the main Tkinter window.
root = Tk()
root.title('Get support')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)

# Load background image.
img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\HelpPageBackground.png")
Label(root, image=img, bg='white').place(x=0, y=0)

# Button to open a website.
button_open = tk.Button(root, text="Get help", command=open_website)
button_open.place(x=10, y=240)

# Function to navigate to the 'main' page.
def my_command():
    root.destroy()
    import main

click_btn = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon1.png")

img_label = Label(image=click_btn)

button = Button(root, image=click_btn, command=my_command, borderwidth=0)
button.place(x=170, y=637)


# Function to navigate to the 'sobrietycalendar' page.
def my_command1():
    root.destroy()
    import sobrietycalendar

click_btn1 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon2.png")

img_label1 = Label(image=click_btn1)

button = Button(root, image=click_btn1, command=my_command1, borderwidth=0)
button.place(x=87, y=637)


# Function to navigate to the 'SocialPage' page.
def my_command2():
    root.destroy()
    import SocialPage

click_btn2 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon3.png")

img_label2 = Label(image=click_btn2)

button = Button(root, image=click_btn2, command=my_command2, borderwidth=0)
button.place(x=250, y=637)

# Function to navigate to the 'ProfilePage' page.
def my_command3():
    root.destroy()
    import ProfilePage

click_btn3 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon4.png")

img_label3 = Label(image=click_btn3)

button = Button(root, image=click_btn3, command=my_command3, borderwidth=0)
button.place(x=330, y=637)

# Function to navigate to the 'HelpPage' page.
def my_command4():
    root.destroy()
    import HelpPage

click_btn4 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon5.png")

img_label4 = Label(image=click_btn4)

button = Button(root, image=click_btn4, command=my_command4, borderwidth=0)
button.place(x=5, y=637)

# Start the main GUI loop.
root.mainloop()
