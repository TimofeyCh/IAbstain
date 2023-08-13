from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Button
from tkinter import filedialog
import ast

def browse_avatar():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
    if file_path:
        img = PhotoImage(file=file_path)
        img = img.subsample(2)
        avatar_label.config(image=img)
        avatar_label.image = img
        save_avatar_to_file(file_path)  # Save the updated avatar path

def save_avatar_to_file(avatar_path):
    with open("avatar.txt", "w") as file:
        file.write(avatar_path)

def load_avatar_from_file():
    try:
        with open("avatar.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def size_guide():
    info_window = Toplevel(root)
    info_window.title("Avatar information")
    info_window.geometry("300x200")

    info_text = "Please make sure that your image\n size is around 380x380px \n"

    info_label = Label(info_window, text=info_text, font=("Helvetica", 12))
    info_label.pack(pady=20)

def increment_counter(event=None):  # Added event parameter
    global counter_value
    counter_value += 1
    update_counter_display()
    save_counter_to_file()

def reset_counter():
    global counter_value
    counter_value = 0
    update_counter_display()
    save_counter_to_file()

def update_counter_display():
    counter_label.config(text=str(counter_value))

def save_counter_to_file():
    with open("daysprofile.txt", "w") as file:
        file.write(str(counter_value))

def load_counter_from_file():
    try:
        with open("daysprofile.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def update_username():
    global username_value
    username_value = username_entry.get()
    save_username_to_file()

def save_username_to_file():
    with open("username.txt", "w") as file:
        file.write(username_value)

def load_username_from_file():
    try:
        with open("username.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def exit():
    root.destroy()
    import LoginPage
    
root = Tk()
root.title('Your profile!')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\ProfilePageBackground.png")
Label(root, image=img, bg='white').place(x=0, y=0)

default_avatar = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\DefaultIcon.png")
default_avatar = default_avatar.subsample(2)

avatar_path = load_avatar_from_file()
if avatar_path:
    updated_avatar = PhotoImage(file=avatar_path)
    updated_avatar = updated_avatar.subsample(2)
    avatar_label = Label(root, image=updated_avatar, bg='white')
    avatar_label.place(x=5, y=5)
else:
    avatar_label = Label(root, image=default_avatar, bg='white')
    avatar_label.place(x=5, y=5)

avatar_button = Button(root, text='Change Avatar', command=browse_avatar)
avatar_button.place(x=5, y=205)


counter_value = load_counter_from_file()

counter_label = Label(root, text=str(counter_value), font=("Helvetica", 24), bg='white')
counter_label.place(x=35, y=362)

counter_label.bind("<Button-1>", increment_counter)


reset_button = Button(root, text="Reset", command=reset_counter)
reset_button.place(x=25, y=430)


username_value = load_username_from_file()

username_entry = Entry(root)
username_entry.insert(0, username_value)
username_entry.place(x=205, y=5)

update_username_button = Button(root, text='Update Username', command=update_username)
update_username_button.place(x=205, y=27)

info_btn = Button(root, text="?", command=size_guide, width=2, height=2)
info_btn.place(x=205, y=157)

exit_btn = Button(root, text="Logout", command=exit, width=6, height=2)
exit_btn.place(x=350, y=5)

###########################################################################################################
def my_command():
    root.destroy()
    import main

click_btn= PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon1.png")

img_label= Label(image=click_btn)

button= Button(root, image=click_btn,command= my_command, borderwidth=0)
button.place(x=170, y=637)
###########################################################################################################
def my_command1():
    root.destroy()
    import sobrietycalendar

click_btn1= PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon2.png")

img_label1= Label(image=click_btn1)

button= Button(root, image=click_btn1,command= my_command1, borderwidth=0)
button.place(x=87, y=637)

###########################################################################################################
def my_command2():
    root.destroy()
    import SocialPage

click_btn2= PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon3.png")

img_label2= Label(image=click_btn2)

button= Button(root, image=click_btn2,command= my_command2, borderwidth=0)
button.place(x=250, y=637)
###########################################################################################################
def my_command3():
    root.destroy()
    import ProfilePage

click_btn3= PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon4.png")

img_label3= Label(image=click_btn3)

button= Button(root, image=click_btn3,command= my_command3, borderwidth=0)
button.place(x=330, y=637)
###########################################################################################################
def my_command4():
    root.destroy()
    import HelpPage

click_btn4= PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon5.png")

img_label4= Label(image=click_btn4)

button= Button(root, image=click_btn4,command= my_command4, borderwidth=0)
button.place(x=5, y=637)
###########################################################################################################

root.mainloop()
