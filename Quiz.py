# Python Quiz Game

score = 0

print("===== Python Quiz =====")
print("Answer each question by entering A, B, C, or D.\n")

questions = [
    ("Which keyword is used to define a function?",
     ["A. func", "B. def", "C. function", "D. define"], "B"),

    ("Which symbol is used for comments in Python?",
     ["A. //", "B. <!--", "C. #", "D. /*"], "C"),

    ("Which data type stores True or False?",
     ["A. int", "B. str", "C. float", "D. bool"], "D"),

    ("Which function displays output in Python?",
     ["A. show()", "B. print()", "C. display()", "D. output()"], "B"),

    ("Which operator is used for exponentiation?",
     ["A. ^", "B. **", "C. //", "D. %"], "B")
]

for number, (question, options, answer) in enumerate(questions, 1):
    print(f"\nQuestion {number}: {question}")

    for option in options:
        print(option)

    user_answer = input("Your answer: ").upper()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")

print("\n===== Quiz Finished =====")
print(f"Your score is {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage == 100:
    print("Excellent! Perfect score!")
elif percentage >= 60:
    print("Good job! Keep practicing.")
else:
    print("Keep learning and try again.")

print("\nThank you for playing!")
