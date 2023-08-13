# Import required modules.
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Button

# Configuration for the text file database
data_post = 'community_posts.txt'


def create_table():
    # Create an empty text file if it doesn't exist
    with open(data_post, 'a') as f:
        pass


def save_post():
    content = post_text.get("1.0", END).strip()
    if content:
        with open(data_post, 'a') as f:
            f.write(content + '\n')
        messagebox.showinfo("Success", "Post saved successfully.")
        post_text.delete("1.0", END)
    else:
        messagebox.showwarning("Error", "Please enter some content for the post.")


def view_posts():
    with open(data_post, 'r') as f:
        posts = f.readlines()

    posts = [post.strip() for post in posts if post.strip()]  # Remove empty lines
    posts.reverse()  # Show the latest posts first

    # Clear the existing text in the display area
    post_display.config(state="normal")
    post_display.delete("1.0", END)

    # Display the posts in the text widget
    for post in posts:
        post_display.insert(END, post + "\n")

    # Disable the "View Posts" widget
    post_display.config(state="disabled")
    
def show_social_info():
    info_window = Toplevel(root)
    info_window.title("Community posts Info")
    info_window.geometry("300x200")

    info_text = "Social Interactions Info:\n\n"
    info_text += "- This is a fully anonymous board.\n"
    info_text += "- Share your thoughts and experiences.\n"
    info_text += "- Make sure to be respectful to everyone.\n"
    info_text += "- Add dates of the time posted if you \n want to be referenced later.\n"
    info_text += "- Add ----- at the end of the posts to \n keep it neat.\n"
    info_text += "- Have fun!\n"

    info_label = Label(info_window, text=info_text, font=("Helvetica", 12))
    info_label.pack(pady=20)

root = Tk()
root.title('Community posts')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\SocialPageBackground.png")
Label(root, image=img, bg='white').place(x=0, y=0)

create_table()

# Button to view community posts
view_posts_btn = Button(root, text="View Posts", command=view_posts, width=20, height=5)
view_posts_btn.place(x=40, y=530)

# Text widget to create a new post
post_text = Text(root, wrap=WORD, width=30, height=6, font=("Helvetica", 12), bd=3)
post_text.place(x=25, y=375)

# Button to save the post
save_post_btn = Button(root, text="Save Post", command=save_post, width=20, height=5)
save_post_btn.place(x=220, y=530)

# Button to view information
information = Button(root, text="?", command=show_social_info, width=10, height=4)
information.place(x=315, y=395)

# Text widget to display community posts
post_display = Text(root, wrap=WORD, width=30, height=15, font=("Helvetica", 12), bd=3, state="disabled")
post_display.place(x=65, y=50)

# Function to handle the "Home" button click
def my_command():
    root.destroy()
    import main

# Load the button image
click_btn = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon1.png")

# Create and place the button
button = Button(root, image=click_btn, command=my_command, borderwidth=0)
button.place(x=170, y=637)

# Function to handle the other buttons and their clicks
def my_command1():
    root.destroy()
    import sobrietycalendar

click_btn1 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon2.png")
button1 = Button(root, image=click_btn1, command=my_command1, borderwidth=0)
button1.place(x=87, y=637)

def my_command2():
    root.destroy()
    import SocialPage

click_btn2 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon3.png")
button2 = Button(root, image=click_btn2, command=my_command2, borderwidth=0)
button2.place(x=250, y=637)

def my_command3():
    root.destroy()
    import ProfilePage

click_btn3 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon4.png")
button3 = Button(root, image=click_btn3, command=my_command3, borderwidth=0)
button3.place(x=330, y=637)

def my_command4():
    root.destroy()
    import HelpPage

click_btn4 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon5.png")
button4 = Button(root, image=click_btn4, command=my_command4, borderwidth=0)
button4.place(x=5, y=637)

root.mainloop()
