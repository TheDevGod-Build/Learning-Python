
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
        print("******************************")
        print(f"Congratulations! You won ${reward}!")
        print("******************************")
        return reward
    elif row[0] == row[1] == row[2]== "♦":
        reward = bet * 20
        print("******************************")
        print(f"Congratulations! You won ${reward}!")
        print("******************************")
        return reward
    elif row[0] == row[1] == row[2]== "♣":
        reward = bet * 30
        print("******************************")
        print(f"Congratulations! You won ${reward}!")
        print("******************************")
        return reward
    elif row[0] == row[1] == row[2]== "♠":
        reward = bet * 40
        print("******************************")
        print(f"Congratulations! You won ${reward}!")
        print("******************************")
        return reward
    else:
        print("******************************")
        print("Sorry, you lost. Better luck next time!")
        print("******************************")
    return 0

def main():
    balance = 100
    print("******************************")
    print("Welcome to the slot machine!")
    print("Symbols: ♥ ♦ ♣ ♠")
    print("******************************")
    print(f"Your balance is: ${balance}")
    print("******************************")
    while True:
        try:
            bet = int(input("Enter your bet amount: "))
        except ValueError:
            print("******************************")
            print("Invalid input. Please enter a valid number.")
            print("******************************")
            continue
        if balance == 0:
            print("**************ERROR: YOU ARE A LOSER**************")
            print("Sorry, YOU LOST IT ALL!Its GAME OVER FOR YOU! HEUHHEUHHAHAHAHAHHAHAHAH")
            break
        if balance < bet:
            print("Insufficient balance. Please enter a smaller bet.")
            print("******************************")
            continue
        balance -= bet
        row = spin_row()
        balance += reward(row, bet)
        print("******************************")
        print(f"Your balance is: ${balance}")
        print("******************************")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            print("******************************")
            print("Thanks for playing! Goodbye!")
            print("******************************")
            break

if __name__ == "__main__":
    main()