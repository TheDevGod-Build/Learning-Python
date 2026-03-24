temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F) : ")

if unit == "C":
    temp = (temp-32) * 5/9
    print (f"Your temp in °F is {temp}")
elif unit == "F":
    temp = (temp * 9/5) + 32
    print(f"Your temp in °C is {temp}")
else:
    print("Invalid Unit")
