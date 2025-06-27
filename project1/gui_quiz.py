import tkinter as tk
from tkinter import messagebox

# Questions and answers
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
        self.root.title("Python MCQ Quiz")
        self.root.geometry("500x300")
        
        self.q_index = 0
        self.score = 0

        self.question_var = tk.StringVar()
        self.option_var = tk.StringVar()

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, textvariable=self.question_var, font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.option_var, value="", font=("Arial", 12), anchor='w')
            rb.pack(fill='x', padx=40)
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

    def load_question(self):
        q = questions[self.q_index]
        self.question_var.set(f"Q{self.q_index + 1}: {q['question']}")
        self.option_var.set(None)  # Clear previous selection
        for i, option in enumerate(q['options']):
            self.radio_buttons[i].config(text=option, value=option)

    def next_question(self):
        selected = self.option_var.get()
        if not selected:
            messagebox.showwarning("No selection", "Please select an answer!")
            return

        correct = questions[self.q_index]['answer']
        if selected == correct:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(questions)}")
        self.root.destroy()

# Run the quiz
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
