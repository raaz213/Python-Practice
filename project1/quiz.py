
def run_quiz():
    print("🎉 Welcome to the Python Quiz!\n")
    score = 0

    # List of questions and answers
    questions = [
        {
            "question": "1. What is the capital of Nepal?",
            "answer": "Kathmandu"
        },
        {
            "question": "2. What data type is used to store True/False?",
            "answer": "boolean"
        },
        {
            "question": "3. Who developed Python programming language?",
            "answer": "Guido van Rossum"
        },
        {
            "question": "4. What does CPU stand for?",
            "answer": "central processing unit"
        },
        {
            "question": "5. What keyword is used to define a function in Python?",
            "answer": "def"
        }
    ]

    # Ask questions
    for q in questions:
        user_ans = input(q["question"] + "\nYour answer: ").strip().lower()
        correct_ans = q["answer"].strip().lower()
        if user_ans == correct_ans:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer: {q['answer']}\n")

    # Final result
    print(f"🏁 Quiz completed! Your score: {score}/{len(questions)}")
    if score == 5:
        print("🎉 Excellent! You're a quiz master!")
    elif score >= 3:
        print("👍 Good job! Keep improving.")
    else:
        print("📚 Keep learning. Practice makes perfect!")

# Run the quiz
if __name__ == "__main__": #To prevent auto-execution during import.Run this code only if the file is executed directly, not when it's imported as a module.
    run_quiz()
