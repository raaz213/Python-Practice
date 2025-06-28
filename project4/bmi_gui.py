import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showwarning("Invalid Input", "Weight and height must be positive.")
            return

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"Your BMI: {bmi}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# ----- GUI Setup -----
root = tk.Tk()
root.title("🧮 BMI Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Title
tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Weight input
tk.Label(root, text="Enter weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Height input
tk.Label(root, text="Enter height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="lightblue").pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

# Start GUI loop
root.mainloop()
