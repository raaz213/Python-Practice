import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = "tasksgui.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Refresh the task list in the Listbox
def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for task in load_tasks():
        status = "✅" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

# Add a new task
def add_task():
    task_text = task_entry.get().strip()
    if task_text == "":
        messagebox.showwarning("Warning", "Task cannot be empty.")
        return
    tasks = load_tasks()
    tasks.append({"task": task_text, "completed": False})
    save_tasks(tasks)
    refresh_tasks()
    task_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Task added.")

# Mark selected task as completed
def complete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to mark complete.")
        return

    tasks = load_tasks()
    index = selected[0]
    if tasks[index]["completed"]:
        messagebox.showinfo("Info", "Task is already completed.")
    else:
        tasks[index]["completed"] = True
        save_tasks(tasks)
        refresh_tasks()
        messagebox.showinfo("Success", "Task marked as completed.")

# Delete selected task
def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to delete.")
        return

    tasks = load_tasks()
    index = selected[0]
    task_name = tasks[index]["task"]
    del tasks[index]
    save_tasks(tasks)
    refresh_tasks()
    messagebox.showinfo("Deleted", f"Task '{task_name}' deleted.")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="To-Do List", font=("Arial", 18, "bold")).pack(pady=10)

# Entry field
task_entry = tk.Entry(root, font=("Arial", 12))
task_entry.pack(padx=20, fill=tk.X)

# Buttons
tk.Button(root, text="Add Task", command=add_task, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Mark Completed", command=complete_task, bg="lightblue").pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, bg="salmon").pack(pady=5)

# Listbox
task_listbox = tk.Listbox(root, font=("Arial", 12), height=15)
task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Load tasks on startup
refresh_tasks()

# Run the app
root.mainloop()
