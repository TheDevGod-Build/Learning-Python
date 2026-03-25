import random

options = ("rock", "paper", "scissors")
print("Welcome to Rock, Paper, Scissors!")
score = 0
running = True
while running:
    computer = random.choice(options)
    player = input("rock, paper, scissors? ").lower()
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win! Rock beats scissors.")
        score += 1
    elif player == "paper" and computer == "rock":
        print("You win! Paper beats rock.")
        score += 1
    elif player == "scissors" and computer == "paper":
        print("You win! Scissors beats paper.")
        score += 1
    else:
        print(f"You lose! {computer.capitalize()} beats {player}.")
    running = False if input("Play again? (y/n): ").lower() == "n" else True
print (f"Your score was {score}.")
print ("Thanks for playing!")

