import math

operator = input("What would you like to do? (+ - * /) : ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print (f"The sum of {num1} and {num2} is {result}.")
elif operator == "-":
    result = num1 - num2
    print (f"The difference between {num1} and {num2} is {result}.")
elif operator == "*":
    result = num1 * num2
    print (f"The product of {num1} and {num2} is {result}.")
elif operator == "/":
    result = num1 / num2
    print (f"The quotient by dividing {num1} and {num2} is {round(result , 4)}")
else:
    print ("Invalid operator")