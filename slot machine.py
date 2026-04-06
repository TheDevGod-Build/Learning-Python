
import random



def spin_row():
    symbols = ["♥", "♦", "♣", "♠"]
    row = []
    for _ in range(3):
        symbol = random.choice(symbols)
        row.append(symbol)
    print(" | ".join(row) + " | ")
    return row

def reward(row, bet):
    if row[0] == row[1] == row[2]== "♥":
        reward = bet * 10
        print(f"Congratulations! You won ${reward}!")
        return reward
    elif row[0] == row[1] == row[2]== "♦":
        reward = bet * 20
        print(f"Congratulations! You won ${reward}!")
        return reward
    elif row[0] == row[1] == row[2]== "♣":
        reward = bet * 30
        print(f"Congratulations! You won ${reward}!")
        return reward
    elif row[0] == row[1] == row[2]== "♠":
        reward = bet * 40
        print(f"Congratulations! You won ${reward}!")
        return reward
    else:
        print("Sorry, you lost. Better luck next time!")
    return 0

def main():
    balance = 100
    
    print("Welcome to the slot machine!")
    print("Symbols: ♥ ♦ ♣ ♠")
    print(f"Your balance is: ${balance}")
    while True:
        try:
            bet = int(input("Enter your bet amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if balance == 0:
            print("Sorry, YOU LOST IT ALL!Its GAME OVER FOR YOU! HEUHHEUHHAHAHAHAHHAHAHAH")
            break
        if balance < bet:
            print("Insufficient balance. Please enter a smaller bet.")
            continue
        balance -= bet
        row = spin_row()
        balance += reward(row, bet)
        print(f"Your balance is: ${balance}")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()          