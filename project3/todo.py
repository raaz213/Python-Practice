

import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task = input("Enter new task: ").strip()
    if task == "":
        print("❗Task cannot be empty.")
        return
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task '{task}' added.")

# View pending tasks
def view_pending():
    tasks = load_tasks()
    print("\n📋 Pending Tasks:")
    found = False
    for idx, t in enumerate(tasks):
        if not t["completed"]:
            print(f"{idx+1}. {t['task']}")
            found = True
    if not found:
        print("🎉 All tasks are completed!")

# Mark a task as completed
def mark_complete():
    tasks = load_tasks()
    view_pending()
    try:
        num = int(input("\nEnter task number to mark as completed: "))
        index = num - 1
        if 0 <= index < len(tasks) and not tasks[index]["completed"]:
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print(f"✅ Task '{tasks[index]['task']}' marked as completed.")
        else:
            print("❌ Invalid task number or task already completed.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Menu system
def menu():
    while True:
        print("\n📌 To-Do List Menu")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_pending()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            print("👋 Goodbye! Stay productive!")
            break
        else:
            print("❗Invalid choice. Please select 1–4.")

# Run the app
if __name__ == "__main__":
    menu()
