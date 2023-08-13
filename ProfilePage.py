from tkinter import *
from tkinter import messagebox, filedialog
import ast

# Function to browse and select an avatar image
def browse_avatar():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
    if file_path:
        img = PhotoImage(file=file_path)
        img = img.subsample(2)
        avatar_label.config(image=img)
        avatar_label.image = img
        save_avatar_to_file(file_path)  # Save the updated avatar path

# Function to save the selected avatar path to a file
def save_avatar_to_file(avatar_path):
    with open("avatar.txt", "w") as file:
        file.write(avatar_path)

# Function to load avatar path from a file
def load_avatar_from_file():
    try:
        with open("avatar.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

# Function to display avatar size information
def size_guide():
    info_window = Toplevel(root)
    info_window.title("Avatar information")
    info_window.geometry("300x200")

    info_text = "Please make sure that your image\n size is around 380x380px \n"

    info_label = Label(info_window, text=info_text, font=("Helvetica", 12))
    info_label.pack(pady=20)

# Function to increment the counter value
def increment_counter(event=None):  # Added event parameter
    global counter_value
    counter_value += 1
    update_counter_display()
    save_counter_to_file()

# Function to reset the counter value
def reset_counter():
    global counter_value
    counter_value = 0
    update_counter_display()
    save_counter_to_file()

# Function to update the counter display
def update_counter_display():
    counter_label.config(text=str(counter_value))

# Function to save the counter value to a file
def save_counter_to_file():
    with open("daysprofile.txt", "w") as file:
        file.write(str(counter_value))

# Function to load the counter value from a file
def load_counter_from_file():
    try:
        with open("daysprofile.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Function to update the username
def update_username():
    global username_value
    username_value = username_entry.get()
    save_username_to_file()

# Function to save the username to a file
def save_username_to_file():
    with open("username.txt", "w") as file:
        file.write(username_value)

# Function to load the username from a file
def load_username_from_file():
    try:
        with open("username.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

# Function to exit the application
def exit():
    root.destroy()
    import LoginPage
    
# Main Tkinter window
root = Tk()
root.title('Your profile!')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)

# Load background image
img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\ProfilePageBackground.png")
Label(root, image=img, bg='white').place(x=0, y=0)

# Load default avatar
default_avatar = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\DefaultIcon.png")
default_avatar = default_avatar.subsample(2)

# Load or display avatar image
avatar_path = load_avatar_from_file()
if avatar_path:
    updated_avatar = PhotoImage(file=avatar_path)
    updated_avatar = updated_avatar.subsample(2)
    avatar_label = Label(root, image=updated_avatar, bg='white')
    avatar_label.place(x=5, y=5)
else:
    avatar_label = Label(root, image=default_avatar, bg='white')
    avatar_label.place(x=5, y=5)

# Button to change avatar
avatar_button = Button(root, text='Change Avatar', command=browse_avatar)
avatar_button.place(x=5, y=205)

# Load counter value
counter_value = load_counter_from_file()

# Display counter value label
counter_label = Label(root, text=str(counter_value), font=("Helvetica", 24), bg='white')
counter_label.place(x=35, y=362)

# Increment counter when label is clicked
counter_label.bind("<Button-1>", increment_counter)

# Reset counter button
reset_button = Button(root, text="Reset", command=reset_counter)
reset_button.place(x=25, y=430)

# Load and display username
username_value = load_username_from_file()

# Entry field for username
username_entry = Entry(root)
username_entry.insert(0, username_value)
username_entry.place(x=205, y=5)

# Update username button
update_username_button = Button(root, text='Update Username', command=update_username)
update_username_button.place(x=205, y=27)

# Info button
info_btn = Button(root, text="?", command=size_guide, width=2, height=2)
info_btn.place(x=205, y=157)

# Exit button
exit_btn = Button(root, text="Logout", command=exit, width=6, height=2)
exit_btn.place(x=350, y=5)

# Load navigation buttons and start GUI loop

root.mainloop()
