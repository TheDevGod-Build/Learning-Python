balance = 0


def check_balance():
    global balance
    print("---------------YOUR BALANCE----------------")
    print(f"Your current balance is: ${balance:.2f}")
    print("-------------------------------------------")

def deposit():
    try:
        deposit = float(input("How much would you like to deposit?"))
    except ValueError:
        print("-------------------ERROR-------------------")
        print("Please enter a valid number.")
        print("-------------------------------------------")
        return
    global balance
    if deposit <= 0:
        print("-------------------ERROR-------------------")
        print("Deposit amount must be greater than zero.")
        print("-------------------------------------------")

    else:
        balance += deposit
        print("------------DEPOSIT SUCCESSFUL-------------")
        print(f"Your Deposit of ${deposit:.2f} was succesfull.")
        print("-------------------------------------------")


def withdraw():
    try:
        withdraw = float(input("How much would you like to withdraw?"))
    except ValueError:
        print("-------------------ERROR-------------------")
        print("Please enter a valid number.")
        print("-------------------------------------------")
        return
    global balance
    if withdraw <= 0:
        print("-------------------ERROR-------------------")
        print("Withdraw amount must be greater than zero.")
        print("-------------------------------------------")

    else:
        if withdraw > balance:
            print("-------------------ERROR-------------------")
            print("You dont have enough balance to withdraw that amount.")
            print("-------------------------------------------")
        else:
            balance -= withdraw
            print("------------WITHDRAW SUCCESSFUL------------")
            print(f"Your Withdraw of ${withdraw:.2f} was succesfull.")
            print("-------------------------------------------")

def main():
    while True:
        print("------------WELCOME TO THE BANK------------")
        print("What would you like to do?" )
        print("1. Check Balance",
              "2. Deposit", 
              "3. Withdraw", 
              "4. Exit", sep="\n")
        print("-------------------------------------------")
        try:
            choice = int(input("What would you like to do? (1-4): "))
        except ValueError:
            print("-------------------ERROR-------------------")
            print("Please enter a valid number.")
            print("-------------------------------------------")
            continue
        match choice:
            case 1:
              check_balance()
            case 2:
               deposit()
            case 3:
               withdraw()
            case 4:
                print("Thank you for banking with us! Visit us again!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()