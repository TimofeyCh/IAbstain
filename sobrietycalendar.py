from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Button
import ast
import calendar

# Function to toggle a day's status (sober or not sober).
def toggle_day(day):
    if day in sober_days:
        sober_days.remove(day)
    else:
        sober_days.append(day)
    update_calendar()

# Function to update the displayed calendar.
def update_calendar():
    # Clear the calendar frame
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    # Display the updated calendar
    show_calendar(calendar_frame, year, month, sober_days)

# Function to display the calendar.
def show_calendar(frame, year, month, sober_days):
    # Create a calendar instance
    cal = calendar.monthcalendar(year, month)

    # Create a label for the month and year
    label = Label(frame, text=calendar.month_name[month] + " " + str(year), font=("Arial", 16, "bold"))
    label.pack(pady=10)

    # Create a table-like layout for the calendar
    for week in cal:
        row_frame = Frame(frame)
        row_frame.pack()
        for day in week:
            if day == 0:
                # Empty cell for days outside the month
                label = Label(row_frame, text=" ", width=5)
            else:
                # Cell displaying the day
                if day in sober_days:
                    # Highlight the sober day
                    button = Button(row_frame, text=str(day), width=5, bg="green", fg="white",
                                    command=lambda day=day: toggle_day(day))
                else:
                    # Regular day
                    button = Button(row_frame, text=str(day), width=5,
                                    command=lambda day=day: toggle_day(day))
                button.pack(side=LEFT)

# Function to navigate to the 'main' page.
def my_command():
    root.destroy()
    import main

# Function to navigate to the 'sobrietycalendar' page.
def my_command1():
    root.destroy()
    import sobrietycalendar

# Function to navigate to the 'SocialPage' page.
def my_command2():
    root.destroy()
    import SocialPage

# Function to navigate to the 'ProfilePage' page.
def my_command3():
    root.destroy()
    import ProfilePage

# Function to navigate to the 'HelpPage' page.
def my_command4():
    root.destroy()
    import HelpPage

# Create the main Tkinter window.
root = Tk()
root.title('The sobriety calendar')
root.geometry('405x720')
root.configure(bg='#fff')
root.resizable(False, False)

# Load background image.
img = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\CalendarPageBackground.png")
Label(root, image=img, bg='white').place(x=0, y=0)

Label(root, text="Sobriety calendar", font=('Microsoft YaHei UI Light', 30), fg="black", bg="lightgray").place(x=50, y=50)

# Set the sober days
sober_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Example sober days

# Create a frame for the calendar
calendar_frame = Frame(root)
calendar_frame.place(x=50, y=150)

# Get the current year and month
year = 2023
month = 8

# Display the calendar
show_calendar(calendar_frame, year, month, sober_days)

click_btn = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon1.png")
button = Button(root, image=click_btn, command=my_command, borderwidth=0)
button.place(x=170, y=637)

click_btn1 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon2.png")
button = Button(root, image=click_btn1, command=my_command1, borderwidth=0)
button.place(x=87, y=637)

click_btn2 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon3.png")
button = Button(root, image=click_btn2, command=my_command2, borderwidth=0)
button.place(x=250, y=637)

click_btn3 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon4.png")
button = Button(root, image=click_btn3, command=my_command3, borderwidth=0)
button.place(x=330, y=637)

click_btn4 = PhotoImage(file=r"C:\Users\User\Documents\NewPythonAPp\assets\Icon5.png")
button = Button(root, image=click_btn4, command=my_command4, borderwidth=0)
button.place(x=5, y=637)

# Start the main GUI loop.
root.mainloop()
