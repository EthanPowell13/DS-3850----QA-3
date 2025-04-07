import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_question_editor(root, table_name, display_name):
    editor = tk.Toplevel(root)
    editor.title(f"Editing: {display_name}")
    editor.geometry("500x400")

    # Labels and entry fields
    entries = {}
    labels = ["Question", "Choice A", "Choice B", "Choice C", "Choice D", "Correct Answer (A/B/C/D)"]

    for i, label in enumerate(labels):
        tk.Label(editor, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(editor, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    def submit_question():
        q = entries["Question"].get()
        a = entries["Choice A"].get()
        b = entries["Choice B"].get()
        c = entries["Choice C"].get()
        d = entries["Choice D"].get()
        ans = entries["Correct Answer (A/B/C/D)"].get().upper()

        if ans not in ["A", "B", "C", "D"]:
            messagebox.showerror("Error", "Correct answer must be A, B, C, or D.")
            return

        correct_value = {"A": a, "B": b, "C": c, "D": d}[ans]

        conn = sqlite3.connect("courses.db")
        cursor = conn.cursor()

        cursor.execute(f"""
            INSERT INTO {table_name} (question, choice_a, choice_b, choice_c, choice_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (q, a, b, c, d, correct_value))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Question added successfully.")
        for entry in entries.values():
            entry.delete(0, tk.END)

    tk.Button(editor, text="Submit Question", command=submit_question).grid(row=6, columnspan=2, pady=20)