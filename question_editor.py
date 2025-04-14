import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_question_editor(root, table_name, display_name):
    editor = tk.Toplevel(root)
    editor.title(f"Editing: {display_name}")
    editor.geometry("600x500")

    # Fields for question entry
    entries = {}
    labels = ["Question", "Choice A", "Choice B", "Choice C", "Choice D", "Correct Answer (A/B/C/D)"]

    for i, label in enumerate(labels):
        tk.Label(editor, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(editor, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    # Listbox for showing existing questions
    question_listbox = tk.Listbox(editor, width=80, height=10)
    question_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Load questions into Listbox
    def load_questions():
        question_listbox.delete(0, tk.END)
        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, question FROM {table_name}")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            question_listbox.insert(tk.END, f"{row[0]}: {row[1]}")

    # Load selected question into entry fields
    def on_select(event):
        if not question_listbox.curselection():
            return
        selected = question_listbox.get(question_listbox.curselection())
        qid = selected.split(":")[0]

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (qid,))
        row = cursor.fetchone()
        conn.close()

        if row:
            entries["Question"].delete(0, tk.END)
            entries["Question"].insert(0, row[1])
            entries["Choice A"].delete(0, tk.END)
            entries["Choice A"].insert(0, row[2])
            entries["Choice B"].delete(0, tk.END)
            entries["Choice B"].insert(0, row[3])
            entries["Choice C"].delete(0, tk.END)
            entries["Choice C"].insert(0, row[4])
            entries["Choice D"].delete(0, tk.END)
            entries["Choice D"].insert(0, row[5])
            entries["Correct Answer (A/B/C/D)"].delete(0, tk.END)
            correct = row[6]
            correct_letter = next((k for k,v in {"A": row[2], "B": row[3], "C": row[4], "D": row[5]}.items() if v == correct), "")
            entries["Correct Answer (A/B/C/D)"].insert(0, correct_letter)

    question_listbox.bind("<<ListboxSelect>>", on_select)

    # Add question
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

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()

        cursor.execute(f"""
            INSERT INTO {table_name} (question, choice_a, choice_b, choice_c, choice_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (q, a, b, c, d, correct_value))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Question added.")
        load_questions()

    # Update selected question
    def update_question():
        if not question_listbox.curselection():
            messagebox.showwarning("Warning", "Select a question to update.")
            return
        selected = question_listbox.get(question_listbox.curselection())
        qid = selected.split(":")[0]

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

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE {table_name}
            SET question=?, choice_a=?, choice_b=?, choice_c=?, choice_d=?, correct_answer=?
            WHERE id=?
        """, (q, a, b, c, d, correct_value, qid))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Question updated.")
        load_questions()

    # Delete selected question
    def delete_question():
        if not question_listbox.curselection():
            messagebox.showwarning("Warning", "Select a question to delete.")
            return
        selected = question_listbox.get(question_listbox.curselection())
        qid = selected.split(":")[0]

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this question?")
        if not confirm:
            return

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (qid,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Question deleted.")
        load_questions()

    # Buttons
    tk.Button(editor, text="Add New Question", command=submit_question).grid(row=6, column=0, pady=10)
    tk.Button(editor, text="Update Selected", command=update_question).grid(row=6, column=1, pady=10)
    tk.Button(editor, text="Delete Selected", command=delete_question).grid(row=8, column=0, columnspan=2, pady=10)

    load_questions()