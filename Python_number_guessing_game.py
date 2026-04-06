import random

lower_limit = 1
upper_limit = 100

answer = random.randint(lower_limit, upper_limit)
guesses = 0

is_running = True

while is_running:
    guess = (input(f"Guess a number between {lower_limit} and {upper_limit}: "))
    if guess.isdigit():
        guess = int(guess)
        if guess >upper_limit or guess < lower_limit:
            print(f"{guess} is out of range. Please enter a number between {lower_limit} and {upper_limit}.")
        else:
            if guess < answer:
                print("Too low! Try again.")
                guesses += 1
            elif guess > answer:
                print("Too high! Try again.")
                guesses += 1
            else: 
                print(f"Congratulations! You've guessed the number {answer} in {guesses} guesses!")
                is_running = False
                print(f"You've guessed the answer in {guesses} guesses!")
    else:
        print(f"{guess} is not valid. Please enter a number between {lower_limit} and {upper_limit}.")
