# Quiz Application with Admin Panel

# ADMIN PASSWORD
The admin password is 'admin123'
## Overview

This program is a simple quiz application that allows users to take quizzes from various courses and provides an admin panel for managing quiz questions. The admin panel requires an admin password for access. The application uses the Tkinter library for the graphical user interface and SQLite for storing quiz data.

## Features

- **Admin Access**: Secure access to the admin panel via password.
- **Quiz Taking**: Students can take quizzes for different courses.
- **Question Editing**: Admins can add and edit questions for each course via an editor interface.
- **Database**: SQLite database is used to store questions and quiz data.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- SQLite3 (comes pre-installed with Python)

## Files

1. **main.py**: The main script that runs the application, handles user interactions, and manages the GUI.
2. **database.py**: Contains the code to initialize the SQLite database and create tables for storing quiz data.
3. **question_editor.py**: Provides the functionality to edit quiz questions for the admin.
4. **quiz_taker.py**: Contains the logic to start and handle quiz-taking for the students.

## Installation

1. Clone the repository or download the files.
2. Make sure Python 3.x is installed on your system.
3. No additional installations are required for Tkinter and SQLite3 as they are included in Python by default.

## How to Run

1. Navigate to the folder containing the `main.py` script.
2. Run the script using the following command:
   ```bash
   python main.py