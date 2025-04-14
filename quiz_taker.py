import sqlite3
import tkinter as tk
from tkinter import messagebox

def start_quiz(root, course_table, course_name):
    quiz_window = tk.Toplevel()
    quiz_window.title(f"{course_name} Quiz")

    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM '{course_table}'")
    questions = cursor.fetchall()
    conn.close()

    if not questions:
        messagebox.showinfo("No Questions", f"No questions found for {course_name}.")
        quiz_window.destroy()
        return

    current_question_index = [0]
    score = [0]

    question_label = tk.Label(quiz_window, text="", wraplength=500, font=("Arial", 14), justify="left")
    question_label.pack(pady=20)

    selected_answer = tk.StringVar()
    answer_buttons = []

    def show_question():
        _, question_text, choice1, choice2, choice3, choice4, answer = questions[current_question_index[0]]
        
        question_label.config(text=question_text)
        
        answer_buttons[0].config(text=choice1, value=choice1)
        answer_buttons[1].config(text=choice2, value=choice2)
        answer_buttons[2].config(text=choice3, value=choice3)
        answer_buttons[3].config(text=choice4, value=choice4)
        
        selected_answer.set(None)
    
    def submit_answer():
        selected = selected_answer.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an answer.")
            return

        # Get the correct answer from the database (string form)
        correct_answer = questions[current_question_index[0]][6]  # Correct answer is stored in index 6
        print(f"Correct answer: {correct_answer}")

        # Check if the selected answer matches the correct answer
        if selected == correct_answer:
            score[0] += 1

        current_question_index[0] += 1
        if current_question_index[0] < len(questions):
            show_question()
        else:
            messagebox.showinfo("Quiz Completed", f"You scored {score[0]} out of {len(questions)}.")
            quiz_window.destroy()
    '''def submit_answer():
        selected = selected_answer.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an answer.")
            return

        correct = questions[current_question_index[0]][5]
        if selected == correct:
            score[0] += 1

        current_question_index[0] += 1
        if current_question_index[0] < len(questions):
            show_question()
        else:
            messagebox.showinfo("Quiz Completed", f"You scored {score[0]} out of {len(questions)}.")
            quiz_window.destroy()'''

    for i in range(4):
        btn = tk.Radiobutton(quiz_window, text="", variable=selected_answer, value="", font=("Arial", 12), anchor="w", justify="left")
        btn.pack(fill="x", padx=20, pady=5)
        answer_buttons.append(btn)

    submit_btn = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
    submit_btn.pack(pady=20)

    show_question()