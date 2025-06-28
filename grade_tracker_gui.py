import tkinter as tk
from tkinter import messagebox
import json
import os

STUDENT_FILE = "students.json"

# Load students from file
def load_students():
    if not os.path.exists(STUDENT_FILE):
        return []
    with open(STUDENT_FILE, "r") as f:
        return json.load(f)

# Save students to file
def save_students(students):
    with open(STUDENT_FILE, "w") as f:
        json.dump(students, f, indent=4)

# Calculate grade from average
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# Add student to file and refresh view
def add_student():
    name = name_entry.get().strip()
    try:
        m1 = float(mark1_entry.get())
        m2 = float(mark2_entry.get())
        m3 = float(mark3_entry.get())

        if not name or not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
            raise ValueError

        avg = round((m1 + m2 + m3) / 3, 2)
        grade = calculate_grade(avg)

        students = load_students()
        students.append({
            "name": name,
            "marks": [m1, m2, m3],
            "average": avg,
            "grade": grade
        })
        save_students(students)
        messagebox.showinfo("Success", f"{name} added with grade: {grade}")
        refresh_list()
        clear_entries()
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid name and marks (0-100).")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    mark1_entry.delete(0, tk.END)
    mark2_entry.delete(0, tk.END)
    mark3_entry.delete(0, tk.END)

# Refresh the listbox
def refresh_list():
    student_list.delete(0, tk.END)
    for s in load_students():
        student_list.insert(tk.END, f"{s['name']} - Avg: {s['average']} - Grade: {s['grade']}")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🎓 Student Grade Tracker")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="Student Grade Tracker", font=("Arial", 16, "bold")).pack(pady=10)

# Name input
tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack(padx=20, fill=tk.X)

# Marks input
tk.Label(root, text="Enter Marks (out of 100)").pack(pady=5)
mark1_entry = tk.Entry(root)
mark1_entry.pack(padx=20, fill=tk.X)
mark2_entry = tk.Entry(root)
mark2_entry.pack(padx=20, fill=tk.X)
mark3_entry = tk.Entry(root)
mark3_entry.pack(padx=20, fill=tk.X)

# Add button
tk.Button(root, text="Add Student", command=add_student, bg="lightgreen").pack(pady=10)

# Student list view
tk.Label(root, text="Student Records").pack()
student_list = tk.Listbox(root, font=("Arial", 12), height=10)
student_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Load records on startup
refresh_list()

# Run app
root.mainloop()
