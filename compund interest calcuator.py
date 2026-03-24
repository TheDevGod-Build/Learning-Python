import math

principle = float(input("Enter the principle: "))
rate = float(input("Enter hte rate of interest: "))
time = float(input("Enter the number of years: "))

amount = principle * math.pow(1+ rate/100 , time )
compound_interest = amount - principle

print(f"Your Compound interest is {compound_interest}")