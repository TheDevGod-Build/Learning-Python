questions = ("What is the capital of France?",
             "What is the largest planet in our solar system?",
             "What is the chemical symbol for gold?")

answers = (("A. London", "B. Berlin", "C. Paris", "D. Madrid"),
        ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
        ("A. Ag", "B. Au", "C. Al", "D. Fe"))

correct_answers = ("C", "C", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for answer in answers[question_num]:
        print(answer)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == correct_answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{correct_answers[question_num]} was the correct answer.")
    question_num += 1

print("--------- QUIZ COMPLETED ---------")
print("Answers: ")
for answer in correct_answers:
    print(answer, end=" ")
print()
print("Guesses: ")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Your final score is: {round(((score)/(len(questions)) * 100), 2)}%")