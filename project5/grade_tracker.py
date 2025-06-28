import json
import os

STUDENT_FILE = "students.json"

# 🔄 Load student data
def load_students():
    if not os.path.exists(STUDENT_FILE):
        return []
    with open(STUDENT_FILE, "r") as f:
        return json.load(f)

# 💾 Save student data
def save_students(students):
    with open(STUDENT_FILE, "w") as f:
        json.dump(students, f, indent=4)

# 🎓 Grade calculation
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

# ➕ Add student
def add_student():
    name = input("Enter student name: ").strip()
    marks = []
    for i in range(3):
        try:
            mark = float(input(f"Enter mark {i+1}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                print("❗Mark must be between 0 and 100.")
                return
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
            return

    avg = round(sum(marks) / len(marks), 2)
    grade = calculate_grade(avg)

    students = load_students()
    students.append({
        "name": name,
        "marks": marks,
        "average": avg,
        "grade": grade
    })
    save_students(students)
    print(f"✅ Student '{name}' added with Grade: {grade}")

# 📋 View all students
def view_students():
    students = load_students()
    if not students:
        print("📭 No student records found.")
        return

    print("\n📊 Student Grade List:")
    print("-" * 40)
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Average: {s['average']}")
        print(f"Grade: {s['grade']}")
        print("-" * 40)

# 🧭 Menu interface
def menu():
    while True:
        print("\n🎓 Student Grade Tracker Menu")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Choose an option (1–3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("👋 Goodbye! Grades saved.")
            break
        else:
            print("❌ Invalid option. Please choose 1–3.")

# 🚀 Start
if __name__ == "__main__":
    menu()
