from tkinter import *
from tkinter import messagebox
import ast

# Function to navigate back to the login page.
def goback():
    root.destroy()
    import LoginPage

# Function to handle user sign-up.
def signup():
    username = user.get()
    password = code.get()
    confirm_password = code_confirm.get()

    # Check if any field is empty.
    if not username or not password or not confirm_password:
        messagebox.showerror('Error', 'Please fill in all the fields.')
        return

    if password == confirm_password:
        try:
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet.txt', 'w')
            w = file.write(str(r))
            messagebox.showinfo('Signup', 'Successfully sign up')

        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid', "Both passwords should match")

# Create main Tkinter window.
root = Tk()
root.title('NewAccount')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)

# Load background image.
img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\RegisterPageBackground.png")
Label(root, image=img, bg='white').place(x=1, y=1)

# Entry field for username.
user = Entry(width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=32, y=103)

Frame(width=202, height=2, bg='black').place(x=32, y=125)

# Entry field for password.
code = Entry(width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=32, y=180)

Frame(width=202, height=2, bg='black').place(x=32, y=200)

# Entry field for password confirmation.
code_confirm = Entry(width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code_confirm.place(x=32, y=260)

Frame(width=202, height=2, bg='black').place(x=32, y=280)

# Sign-up button.
Button(width=30, pady=7, text='Create account', bg='#57a1f8', fg='white', border=0, command=signup).place(x=32, y=310)

# Back button to return to the login page.
back = Button(width=20, text='Return to login page', border=0, command=goback, bg='white', fg='#57a1f8')
back.place(x=65, y=360)

# Start the main GUI loop.
root.mainloop()
