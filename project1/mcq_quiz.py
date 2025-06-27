def run_mcq_quiz():
    print("🎉 Welcome to the Multiple Choice Quiz!\n")
    score = 0

    questions = [
        {
            "question": "1. What is the capital of Nepal?",
            "options": ["A. Pokhara", "B. Kathmandu", "C. Lalitpur", "D. Biratnagar"],
            "answer": "B"
        },
        {
            "question": "2. Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "3. Which of these is a Python data type?",
            "options": ["A. decimal", "B. real", "C. float", "D. double"],
            "answer": "C"
        },
        {
            "question": "4. Who developed Python?",
            "options": ["A. Elon Musk", "B. Dennis Ritchie", "C. Bill Gates", "D. Guido van Rossum"],
            "answer": "D"
        },
        {
            "question": "5. Which one is used to import modules in Python?",
            "options": ["A. include", "B. import", "C. require", "D. attach"],
            "answer": "B"
        }
    ]

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()

        if user_ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            correct_text = q["options"][ord(q["answer"]) - 65]  # Convert A->0, B->1, etc.
            print(f"❌ Wrong. Correct answer: {correct_text}\n")

    print(f"🏁 Quiz Over! Your final score is {score}/{len(questions)}")
    if score == 5:
        print("🎉 Excellent! Full marks!")
    elif score >= 3:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")

if __name__ == "__main__":
    run_mcq_quiz()
