print("Quiz - How Well Do You Know Bhoomi?")
score = 0
questions = [
    {  "question": "What is Bhoomi's full name?",
        "options": ["A. Bhoomika Agarwal", "B. Bhoomi Agarwal"],
        "answer": "A"},
    {  "question": "What is Bhoomi's age?",
        "options": ["A. 18", "B. 17"],
        "answer": "B"},
    {   "question": "When is Bhoomi's birthday?",
        "options": ["A. Sep-26", "B. Sep-25"],
        "answer": "B"}
]
for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer (A or B): ")

    if user_answer.upper() == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print("\nQuiz Finished!")
print("Your Score is:", score, "/", len(questions))
