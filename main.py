# Import required modules.
from tkinter import *
from tkinter import simpledialog


# Create the main window.
root = Tk()
root.title('Homepage')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)


# Load background image.
img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\MainPageBackground.png")
Label(root, image=img, bg='white').place(x=0, y=0)

# Define navigation commands for buttons.
def my_command():
    # Destroy the current window and open the main page.
    root.destroy()
    import main


def my_command1():
    # Destroy the current window and open the sobriety calendar page.
    root.destroy()
    import sobrietycalendar


def my_command2():
    # Destroy the current window and open the social page.
    root.destroy()
    import SocialPage


def my_command3():
    # Destroy the current window and open the profile page.
    root.destroy()
    import ProfilePage


def my_command4():
    # Destroy the current window and open the help page.
    root.destroy()
    import HelpPage


# Create navigation buttons.

click_btn = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon1.png")
button = Button(root, image=click_btn, command=my_command, borderwidth=0)
button.place(x=170, y=637)


click_btn1 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon2.png")
button1 = Button(root, image=click_btn1, command=my_command1, borderwidth=0)
button1.place(x=87, y=637)


click_btn2 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon3.png")
button2 = Button(root, image=click_btn2, command=my_command2, borderwidth=0)
button2.place(x=250, y=637)


click_btn3 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon4.png")
button3 = Button(root, image=click_btn3, command=my_command3, borderwidth=0)
button3.place(x=330, y=637)


click_btn4 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon5.png")
button4 = Button(root, image=click_btn4, command=my_command4, borderwidth=0)
button4.place(x=5, y=637)

# Timer and Addiction Tracker Section
#########################################################################################################

# Initialize timer values.
days = 0
hours = 0
minutes = 0
seconds = 0

# Label to display days.
days_label = Label(root, text="Days: 0", font=('Microsoft YaHei UI Light', 30), fg="black", bg="lightgray")
days_label.place(x=50, y=60)

# Label to display hours.
hours_label = Label(root, text="Hours: 0", font=('Microsoft YaHei UI Light', 30), fg="black", bg="lightgray")
hours_label.place(x=50, y=120)

# Label to display minutes.
minutes_label = Label(root, text="Minutes: 0", font=('Microsoft YaHei UI Light', 30), fg="black", bg="lightgray")
minutes_label.place(x=50, y=180)

# Label to display seconds.
seconds_label = Label(root, text="Seconds: 0", font=('Microsoft YaHei UI Light', 30), fg="black", bg="lightgray")
seconds_label.place(x=50, y=240)

# Variable to store addiction name.
addiction_name = StringVar()
addiction_name.set(" ")

# Label to display addiction name.
addiction_label = Label(root, textvariable=addiction_name, font=('Microsoft YaHei UI Light', 20), fg="black", bg="lightgray")
addiction_label.place(x=30, y=10)

# Function to save timer values.
def save_timer():
    with open("timer.txt", "w") as file:
        file.write(f"{days},{hours},{minutes},{seconds},{addiction_name.get()}")

# Function to load saved timer values.
def load_timer():
    global days, hours, minutes, seconds, addiction_name

    try:
        with open("timer.txt", "r") as file:
            data = file.readline()
            values = data.split(",")
            if len(values) == 5:
                days, hours, minutes, seconds, addiction = values
                days = int(days)
                hours = int(hours)
                minutes = int(minutes)
                seconds = int(seconds)
                addiction_name.set(addiction)
    except FileNotFoundError:
        pass

# Function to update timer.
def update_timer():
    global days, hours, minutes, seconds

    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
        days += 1

    # Update labels with new timer values.
    days_label.config(text="Days: " + str(days))
    hours_label.config(text="Hours: " + str(hours))
    minutes_label.config(text="Minutes: " + str(minutes))
    seconds_label.config(text="Seconds: " + str(seconds))

    save_timer()  # Save timer values.

    # Update timer after 1000 ms (1 second).
    timer_id = root.after(1000, update_timer)


# Function to set addiction name and reset timer.
def set_addiction():
    global days, hours, minutes, seconds
    new_addiction = simpledialog.askstring("Set Addiction", "Enter the name of what you are sober from:")
    if new_addiction:
        addiction_name.set("I've been " + new_addiction + " free for:")
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
        save_timer()  # Save timer values.

# Load saved timer values, start timer, and set addiction.
load_timer()
update_timer()

# Function to reset the addiction timer.
def reset_addiction_timer():
    global days, hours, minutes, seconds
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    days_label.config(text="Days: 0")
    hours_label.config(text="Hours: 0")
    minutes_label.config(text="Minutes: 0")
    seconds_label.config(text="Seconds: 0")
    save_timer()  # Save timer values.

# Button to reset the addiction timer.
set_addiction_button = Button(root, text="Reset goal", command=set_addiction)
set_addiction_button.place(x=50, y=310)

# Button to reset the timer and addiction.
reset_addiction_button = Button(root, text="Reset timer", command=reset_addiction_timer)
reset_addiction_button.place(x=160, y=310)

# Start the main event loop.
root.mainloop()
