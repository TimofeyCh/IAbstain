from tkinter import *
from tkinter import messagebox
import ast

# Create main Tkinter window.
root = Tk()
root.title('IAbstain')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)

# Function to navigate to the sign-up page.
def sign_page():
    root.destroy()
    import CreateAccount

# Function to handle user sign-in.
def signin():
    username = user.get()
    password = code.get()
    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password == r[username]:
        root.destroy()
        import main
    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "Wrong username or password. Check spelling.")

# Load background image.
img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\LoginPageBackground.png")
Label(root, image=img, bg='white').place(x=1, y=1)

# Entry field for username.
user = Entry(width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=112, y=410)
user.insert(0, 'Username')

# Function to clear username entry when clicked.
def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)

Frame(width=202, height=2, bg='black').place(x=112, y=432)

# Entry field for password.
code = Entry(width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=112, y=450)
code.insert(0, 'Password')

# Function to clear password entry when clicked.
def on_enter_code(e):
    code.delete(0, 'end')

def on_leave_code(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code.bind('<FocusIn>', on_enter_code)
code.bind('<FocusOut>', on_leave_code)

Frame(width=202, height=2, bg='black').place(x=112, y=472)

# Sign-in button.
Button(width=30, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=105, y=490)

# Sign-up button.
sign_up = Button(width=5, text='Sign up', border=0, command=sign_page, bg='white', fg='#57a1f8')
sign_up.place(x=258, y=542)

# Start the main GUI loop.
root.mainloop()
