item = input("What would you like to buy? ")
price = float(input("What is the price of each item? "))
quantity = float(input("How many would you like to buy? "))

total_cost = price * quantity

print (f"Your total cost is {total_cost} for {quantity} {item}.")