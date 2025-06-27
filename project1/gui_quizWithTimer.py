import tkinter as tk
from tkinter import messagebox, ttk

# Question Set
questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["Pokhara", "Kathmandu", "Lalitpur", "Biratnagar"],
        "answer": "Kathmandu"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["decimal", "real", "float", "double"],
        "answer": "float"
    },
    {
        "question": "Who developed Python?",
        "options": ["Elon Musk", "Dennis Ritchie", "Bill Gates", "Guido van Rossum"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which one is used to import modules in Python?",
        "options": ["include", "import", "require", "attach"],
        "answer": "import"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Timed Quiz with Progress Bar")
        self.root.geometry("500x400")

        self.q_index = 0
        self.score = 0
        self.total_questions = len(questions)
        self.timer = 15
        self.timer_id = None

        self.question_var = tk.StringVar()
        self.option_var = tk.StringVar()
        self.timer_var = tk.StringVar(value=f"Time left: {self.timer}s")
        self.progress_text = tk.StringVar()

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.timer_label = tk.Label(self.root, textvariable=self.timer_var, font=("Arial", 12), fg="red")
        self.timer_label.pack(pady=5)

        self.progress_label = tk.Label(self.root, textvariable=self.progress_text, font=("Arial", 12))
        self.progress_label.pack()

        self.progress_bar = ttk.Progressbar(self.root, length=400, mode='determinate', maximum=self.total_questions)
        self.progress_bar.pack(pady=5)

        self.question_label = tk.Label(self.root, textvariable=self.question_var, font=("Arial", 14), wraplength=450)
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for _ in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.option_var, value="", font=("Arial", 12), anchor='w')
            rb.pack(fill='x', padx=40, pady=2)
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=15)

    def load_question(self):
        q = questions[self.q_index]
        self.question_var.set(f"Q{self.q_index + 1}: {q['question']}")
        self.option_var.set(None)
        self.progress_text.set(f"Progress: Question {self.q_index + 1} of {self.total_questions}")
        self.progress_bar['value'] = self.q_index

        for i, option in enumerate(q['options']):
            self.radio_buttons[i].config(text=option, value=option)

        # Start timer
        self.timer = 15
        self.update_timer()

    def update_timer(self):
        self.timer_var.set(f"Time left: {self.timer}s")
        if self.timer > 0:
            self.timer -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.auto_next()

    def next_question(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        selected = self.option_var.get()
        correct = questions[self.q_index]['answer']
        if selected == correct:
            self.score += 1

        self.q_index += 1
        if self.q_index < self.total_questions:
            self.load_question()
        else:
            self.show_result()

    def auto_next(self):
        messagebox.showinfo("⏰ Time's up!", "Moving to the next question.")
        self.next_question()

    def show_result(self):
        self.progress_bar['value'] = self.total_questions
        messagebox.showinfo("🏁 Quiz Completed", f"Your Score: {self.score}/{self.total_questions}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
