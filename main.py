import tkinter as tk
from database import initialize_database
from question_editor import open_question_editor
from quiz_taker import start_quiz

# Initialize the database (ensures tables exist)
initialize_database()

# Main root window
root = tk.Tk()
root.title("Welcome")
root.geometry("300x200")

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
                           command=lambda t=table_name, n=display_name: start_quiz(root,t,n))
        button.pack(pady=5)

# Function to open admin window (currently blank)
def open_admin_window():
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

    for display_name, table_name in course_list:
        button = tk.Button(admin_window, text=display_name, width=20,
                           command=lambda t=table_name, n=display_name: open_question_editor(root, t, n))
        button.pack(pady=5)

# Placeholder for individual course windows 
"""
def open_course_window(course_name):
    window = tk.Toplevel(root)
    window.title(course_name)
    label = tk.Label(window, text=f"Welcome to {course_name}", font=("Arial", 14))
    label.pack(padx=20, pady=20)"""

def open_quiz_menu():
    quiz_window = tk.Toplevel()
    quiz_window.title("Choose a Quiz")

    classes = {
        "ds_3850": "DS 3850",
        "acct_3210": "ACCT 3210",
        "ds_3540": "DS 3540",
        "bmgt_4410": "BMGT 4410",
        "phed_1101": "PHED 1101"
    }

    for table_name, display_name in classes.items():
        btn = tk.Button(quiz_window, text=display_name, width=20,
                        command=lambda t=table_name, n=display_name: start_quiz(root, t, n))
        btn.pack(pady=5)

# Welcome screen buttons
tk.Label(root, text="Welcome!", font=("Arial", 16)).pack(pady=20)

quiz_button = tk.Button(root, text="Take a Quiz", width=20, command=open_quiz_window)
quiz_button.pack(pady=10)

admin_button = tk.Button(root, text="Admin Access", width=20, command=open_admin_window)
admin_button.pack(pady=10)

root.mainloop()