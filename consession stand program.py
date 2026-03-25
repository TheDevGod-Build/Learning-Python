menu = {"hamburger": 5.99, 
        "fries": 2.99, 
        "soda": 1.99, 
        "hot dog": 3.99, 
        "nachos": 4.99}

cart = []

total = 0

for key, value in menu.items():
    print (f"{key:15}: ${value:.2f}")

while True:
    food = input("What would you like to order? (q to quit) ").lower().strip()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print ("Sorry, we don't have that item. Please try again.")

for food in cart: 
    total += menu.get(food, 0)
    print (food, end = " ")

print(f"Total: ${total:.2f}")