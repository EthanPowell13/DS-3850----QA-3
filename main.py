import tkinter as tk
from tkinter import messagebox
from database import initialize_database
from question_editor import open_question_editor
from quiz_taker import start_quiz

# Initialize the database (ensures tables exist)
initialize_database()

# Main root window
root = tk.Tk()
root.title("Welcome")
root.geometry("300x200")
ADMIN_PASSWORD = "admin123"

# Function to open quiz selection window
def open_quiz_window():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Choose a Class")
    quiz_window.geometry("300x300")

    # List of course display names and corresponding table names
    course_list = [
        ("DS 3850", "DS_3850"),
        ("ACCT 3210", "ACCT_3210"),
        ("DS 3540", "DS_3540"),
        ("BMGT 4410", "BMGT_4410"),
        ("PHED 1101", "PHED_1101")
    ]

    tk.Label(quiz_window, text="Select a Class", font=("Arial", 14)).pack(pady=10)

    for display_name, table_name in course_list:
        button = tk.Button(quiz_window, text=display_name, width=20, 
                           command=lambda t=table_name, n=display_name: start_quiz(root, t, n))
        button.pack(pady=5)

# Function to open admin window (currently blank)
def open_admin_window(root):
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Panel")
    admin_window.geometry("300x300")

    tk.Label(admin_window, text="Choose Class to Edit", font=("Arial", 14)).pack(pady=10)

    course_list = [
        ("DS 3850", "DS_3850"),
        ("ACCT 3210", "ACCT_3210"),
        ("DS 3540", "DS_3540"),
        ("BMGT 4410", "BMGT_4410"),
        ("PHED 1101", "PHED_1101")
    ]

    # Create buttons for each course
    for display_name, table_name in course_list:
        button = tk.Button(admin_window, text=display_name, width=20,
                           command=lambda t=table_name, n=display_name: open_question_editor(admin_window, t, n))
        button.pack(pady=5)

def check_password(password_entry):
    entered_password = password_entry.get()  # Make sure the widget is an Entry

    if entered_password == ADMIN_PASSWORD:
        messagebox.showinfo("Success", "Password Correct! Accessing Admin Panel.")
        open_admin_window(root)  # Pass the root window to admin panel
        password_window.destroy()  # Close the password window
    else:
        messagebox.showerror("Error", "Incorrect Password! Please try again.")

# Create a password prompt window
def open_password_window():
    password_window = tk.Toplevel(root)  # Open a Toplevel window for the password
    password_window.title("Admin Login")

    # Add a label and password entry field
    label = tk.Label(password_window, text="Enter Admin Password:", font=("Arial", 12))
    label.pack(pady=20)

    password_entry = tk.Entry(password_window, show="*", font=("Arial", 12))  # Correct definition of Entry widget
    password_entry.pack(pady=10)

    # Add a button to check the password
    check_button = tk.Button(password_window, text="Submit", command=lambda: check_password(password_entry))
    check_button.pack(pady=20)

# Welcome screen buttons
tk.Label(root, text="Welcome!", font=("Arial", 16)).pack(pady=20)

quiz_button = tk.Button(root, text="Take a Quiz", width=20, command=open_quiz_window)
quiz_button.pack(pady=10)

admin_button = tk.Button(root, text="Admin Access", width=20, command=open_password_window)
admin_button.pack(pady=10)

root.mainloop()